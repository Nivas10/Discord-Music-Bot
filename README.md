<h1 align="center">
  <br>Discord-Music-Bot
</h1>
<h3 align="center">◦ A Discord bot built with Python, Discord.py and FFmpeg for enhanced music experiences within Discord servers.</h3>
<h3 align="center">◦ Developed with the software and tools below.</h3>
<p align="center">
  <img src="https://img.shields.io/badge/Language-Python-blue" alt="">
  <img src="https://img.shields.io/badge/Framework-Discord.py-red" alt="">
  <img src="https://img.shields.io/badge/Audio-FFmpeg-blue" alt="">
  <img src="https://img.shields.io/badge/Database-SQLite-black" alt="">
</p>
<p align="center">
  <img src="https://img.shields.io/github/badge/license-GNU_AGPLv3?style=flat-square&color=5D6D7E" alt="GitHub license" />
  <img src="https://img.shields.io/github/last-commit/spectra-ai-codegen/Discord-Music-Bot?style=flat-square&color=5D6D7E" alt="git-last-commit" />
  <img src="https://img.shields.io/github/commit-activity/m/spectra-ai-codegen/Discord-Music-Bot?style=flat-square&color=5D6D7E" alt="GitHub commit activity" />
  <img src="https://img.shields.io/github/languages/top/spectra-ai-codegen/Discord-Music-Bot?style=flat-square&color=5D6D7E" alt="GitHub top language" />
</p>

## 📑 Table of Contents
- [📍 Overview](#overview)
- [📦 Features](#features)
- [📂 Repository Structure](#repository-structure)
- [💻 Installation](#installation)
- [🏗️ Usage](#usage)
- [🌐 Hosting](#hosting)
- [📄 License](#license)
- [👏 Authors and Acknowledgments](#authors-and-acknowledgments)

## 📍 Overview
This repository contains a project called "Discord-Music-Bot" which is a Python-based Discord bot designed to enhance music experiences within Discord servers. The bot utilizes the Discord.py library and FFmpeg for seamless music playback, queue management, and a range of interactive features. 

## 📦 Features
- **Music Playback:**  Plays music from various sources like YouTube, SoundCloud, Spotify, and local audio files.
- **Voice Channel Integration:** Connects to voice channels to play music for all members.
- **User Interaction:**  Users can interact with the bot using commands to search for music, manage the queue, and provide feedback.
- **Queue Management:**  Provides commands to add, remove, list, and clear songs from the playback queue.
- **Advanced Controls:** Offers features like looping, shuffling, and equalizer settings for customized music playback.
- **Database Integration:** Uses SQLite (or optionally other databases like MySQL/PostgreSQL/MongoDB) to store data, server settings, and queue information.
- **Customizable Commands:** Server administrators can customize command prefixes and aliases.

## 📂 Repository Structure

```
Discord-Music-Bot
├── bot.py
├── cogs
│   ├── music.py
│   └── admin.py
├── utils
│   ├── config.py
│   ├── errors.py
│   ├── database.py
│   └── checks.py
├── main.py
├── requirements.txt
└── .env
```

  ## 💻 Installation
  ### 🔧 Prerequisites
  - Python 3.7 or higher
  - pip (Python package installer)
  
  ### 🚀 Setup Instructions
  1. Clone the repository:
     - 'git clone https://github.com/spectra-ai-codegen/Discord-Music-Bot.git'
  2. Navigate to the project directory:
     - 'cd Discord-Music-Bot'
  3. Install dependencies:
     - 'pip install -r requirements.txt'
  4. Create a `.env` file (if it doesn't exist) and add the following environment variables:
     - `DISCORD_TOKEN=YOUR_BOT_TOKEN`
     - `YOUTUBE_API_KEY=YOUR_YOUTUBE_API_KEY` (optional, if you want to use YouTube)
     - `SOUNDCLOUD_CLIENT_ID=YOUR_SOUNDCLOUD_CLIENT_ID` (optional, if you want to use SoundCloud)
     - `SOUNDCLOUD_CLIENT_SECRET=YOUR_SOUNDCLOUD_CLIENT_SECRET` (optional, if you want to use SoundCloud)
     - `SPOTIFY_CLIENT_ID=YOUR_SPOTIFY_CLIENT_ID` (optional, if you want to use Spotify)
     - `SPOTIFY_CLIENT_SECRET=YOUR_SPOTIFY_CLIENT_SECRET` (optional, if you want to use Spotify)
     - `GENIUS_ACCESS_TOKEN=YOUR_GENIUS_ACCESS_TOKEN` (optional, if you want to display lyrics)
     - `MUSIXMATCH_API_KEY=YOUR_MUSIXMATCH_API_KEY` (optional, if you want to display lyrics)
     - `TUNEIN_API_KEY=YOUR_TUNEIN_API_KEY` (optional, if you want to use TuneIn Radio)
     - `IHEARTRADIO_API_KEY=YOUR_IHEARTRADIO_API_KEY` (optional, if you want to use iHeartRadio)
     - `DATABASE_URI=sqlite:///music.db` (for SQLite) or your preferred database URI
  
  ## 🏗️ Usage
  ### 🏃‍♂️ Running the Bot
  1. Run the bot:
     - 'python main.py'
  2. Invite the bot to your Discord server. 
  
  ## 🌐 Hosting
  ### 🚀 Deployment Instructions
  1. **Docker:**
     - Build a Docker image: 'docker build -t discord-music-bot .'
     - Run the Docker container: 'docker run -d -p 80:80 discord-music-bot'
  2. **Cloud Platforms (e.g., Heroku):**
     - Create a new Heroku app.
     - Set environment variables (as in the `.env` file).
     - Deploy the bot using Git (refer to Heroku documentation for details). 
  
  ## 📄 License
  This project is licensed under the [GNU AGPLv3](https://choosealicense.com/licenses/agpl-3.0/).
  
  ## 👥 Authors and Acknowledgments
  - **Author Name** - [Spectra.codes](https://spectra.codes)
  - **Creator Name** - [DRIX10](https://github.com/Drix10)

  <p align="center">
    <h1 align="center">🌐 Spectra.Codes</h1>
  </p>
  <p align="center">
    <em>Why only generate Code? When you can generate the whole Repository!</em>
  </p>
  <p align="center">
	<img src="https://img.shields.io/badge/Developer-Drix10-red" alt="">
	<img src="https://img.shields.io/badge/Website-Spectra.codes-blue" alt="">
	<img src="https://img.shields.io/badge/Backed_by-Google_&_Microsoft_for_Startups-red" alt="">
	<img src="https://img.shields.io/badge/Finalist-Backdrop_Build_v4-black" alt="">
  <p>
