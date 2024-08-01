import discord
from discord.ext import commands
import asyncio
import ffmpeg
from pydub import AudioSegment
import requests
from utils.config import Config
from utils.errors import *
from utils.checks import is_connected

class Music(commands.Cog):
    """Music commands for the bot."""

    def __init__(self, bot):
        self.bot = bot
        self.config = Config()
        self.queue = []
        self.current_song = None
        self.is_playing = False
        self.is_paused = False
        self.volume = 0.5  # Default volume

    async def search_song(self, query):
        """Searches for a song on YouTube, SoundCloud, or Spotify."""
        allowed_sources = self.config.get_allowed_sources(self.ctx.guild.id)
        if 'youtube' in allowed_sources:
            youtube_url = self.search_youtube(query)
            if youtube_url:
                return 'youtube', youtube_url

        if 'soundcloud' in allowed_sources:
            soundcloud_url = self.search_soundcloud(query)
            if soundcloud_url:
                return 'soundcloud', soundcloud_url

        if 'spotify' in allowed_sources:
            spotify_url = self.search_spotify(query)
            if spotify_url:
                return 'spotify', spotify_url

        raise SongNotFound(f"Could not find a song matching '{query}' on any of the allowed sources.")

    def search_youtube(self, query):
        """Searches for a song on YouTube."""
        # Implement YouTube API search here
        # Use the YouTube Data API v3 to search for videos
        # Retrieve the video URL if found
        # Return the video URL or None if no match is found
        return None

    def search_soundcloud(self, query):
        """Searches for a song on SoundCloud."""
        # Implement SoundCloud API search here
        # Use the SoundCloud API to search for tracks
        # Retrieve the track URL if found
        # Return the track URL or None if no match is found
        return None

    def search_spotify(self, query):
        """Searches for a song on Spotify."""
        # Implement Spotify API search here
        # Use the Spotify API to search for tracks
        # Retrieve the track URL if found
        # Return the track URL or None if no match is found
        return None

    async def play_song(self, source, url):
        """Plays a song from the specified source."""
        if not self.is_playing:
            self.is_playing = True

        if source == 'youtube':
            # Download and convert YouTube video to audio
            try:
                audio_stream = ffmpeg.input(url)
                audio_stream = audio_stream.audio
                audio_stream = audio_stream.output('temp.wav', format='wav')
                audio_stream.run()
                audio = AudioSegment.from_wav('temp.wav')
            except Exception as e:
                raise APIError(f"Failed to download and convert YouTube video: {e}")

        elif source == 'soundcloud':
            # Download SoundCloud track
            try:
                response = requests.get(url)
                response.raise_for_status()
                with open('temp.mp3', 'wb') as f:
                    f.write(response.content)
                audio = AudioSegment.from_mp3('temp.mp3')
            except Exception as e:
                raise APIError(f"Failed to download SoundCloud track: {e}")

        elif source == 'spotify':
            # Download Spotify track
            try:
                # Implement Spotify track download logic using the Spotify API
                # (This may involve fetching track data and then using the Spotify API to download the audio)
                # Store the downloaded audio in a temporary file (e.g., 'temp.mp3')
                audio = AudioSegment.from_mp3('temp.mp3')
            except Exception as e:
                raise APIError(f"Failed to download Spotify track: {e}")

        else:
            raise InvalidSource(f"Unsupported music source: {source}")

        # Set the audio segment's volume
        audio = audio.apply_gain(-100 + (20 * self.volume))
        audio.export("temp.wav", format="wav")

        # Play the audio in the voice channel
        self.voice_client.play(discord.FFmpegPCMAudio(executable="ffmpeg", source="temp.wav"), after=self.song_finished)

        self.current_song = url
        await self.ctx.send(f"Now playing: {self.current_song}")

    def song_finished(self, error):
        """Handles the event when a song finishes playing."""
        if error:
            print(f"An error occurred during playback: {error}")

        self.is_playing = False
        self.current_song = None
        asyncio.run_coroutine_threadsafe(self.next_song(), self.bot.loop)

    async def next_song(self):
        """Plays the next song in the queue."""
        if len(self.queue) > 0:
            source, url = self.queue.pop(0)
            await self.play_song(source, url)
        else:
            self.is_playing = False
            self.current_song = None
            await self.ctx.send("Queue is empty. Stopped playback.")

    @commands.command(name='play', aliases=['p'])
    @is_connected()
    async def play_command(self, ctx, *, query):
        """Plays a song from YouTube, SoundCloud, or Spotify."""
        self.ctx = ctx
        try:
            source, url = await self.search_song(query)
            if self.voice_client is None:
                self.voice_client = await ctx.author.voice.channel.connect()
            await self.play_song(source, url)
        except SongNotFound as e:
            await ctx.send(e)
        except APIError as e:
            await ctx.send(e)
        except InvalidSource as e:
            await ctx.send(e)

    @commands.command(name='pause')
    @is_connected()
    async def pause_command(self, ctx):
        """Pauses the currently playing song."""
        self.ctx = ctx
        if self.is_playing and not self.is_paused:
            self.voice_client.pause()
            self.is_paused = True
            await ctx.send("Paused playback.")
        else:
            await ctx.send("No song is currently playing or already paused.")

    @commands.command(name='resume')
    @is_connected()
    async def resume_command(self, ctx):
        """Resumes a paused song."""
        self.ctx = ctx
        if self.is_paused:
            self.voice_client.resume()
            self.is_paused = False
            await ctx.send("Resumed playback.")
        else:
            await ctx.send("No song is currently paused.")

    @commands.command(name='skip', aliases=['s'])
    @is_connected()
    async def skip_command(self, ctx):
        """Skips the current song."""
        self.ctx = ctx
        if self.is_playing:
            self.voice_client.stop()
            await self.next_song()
        else:
            await ctx.send("No song is currently playing.")

    @commands.command(name='stop')
    @is_connected()
    async def stop_command(self, ctx):
        """Stops playback and clears the queue."""
        self.ctx = ctx
        if self.voice_client:
            self.voice_client.stop()
            self.queue.clear()
            self.is_playing = False
            self.current_song = None
            await self.ctx.send("Stopped playback and cleared the queue.")
            await self.voice_client.disconnect()

    @commands.command(name='queue', aliases=['q'])
    @is_connected()
    async def queue_command(self, ctx, *, query):
        """Adds a song to the queue."""
        self.ctx = ctx
        try:
            source, url = await self.search_song(query)
            self.queue.append((source, url))
            await ctx.send(f"Added {query} to the queue.")
        except SongNotFound as e:
            await ctx.send(e)
        except APIError as e:
            await ctx.send(e)
        except InvalidSource as e:
            await ctx.send(e)

    @commands.command(name='clear')
    @is_connected()
    async def clear_queue_command(self, ctx):
        """Clears the song queue."""
        self.ctx = ctx
        self.queue.clear()
        await ctx.send("Cleared the queue.")

    @commands.command(name='list')
    @is_connected()
    async def list_queue_command(self, ctx):
        """Lists the current song queue."""
        self.ctx = ctx
        if len(self.queue) > 0:
            queue_list = "\n".join(f"{i+1}. {song[1]}" for i, song in enumerate(self.queue))
            await ctx.send(f"Current queue:\n{queue_list}")
        else:
            await ctx.send("The queue is empty.")

    @commands.command(name='volume')
    @is_connected()
    async def volume_command(self, ctx, volume: float):
        """Sets the bot's volume."""
        self.ctx = ctx
        if volume < 0 or volume > 1:
            await ctx.send("Volume must be between 0 and 1.")
            return
        self.volume = volume
        self.voice_client.source.volume = volume
        await ctx.send(f"Volume set to {volume}.")

def setup(bot):
    bot.add_cog(Music(bot))