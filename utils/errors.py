class CommandError(Exception):
    """Base class for all custom command errors."""
    pass


class MissingPermissions(CommandError):
    """Raised when a user lacks the necessary permissions to execute a command."""
    def __init__(self, message="You do not have permission to use this command."):
        super().__init__(message)


class NoVoiceChannel(CommandError):
    """Raised when the user is not in a voice channel."""
    def __init__(self, message="You must be in a voice channel to use this command."):
        super().__init__(message)


class AlreadyConnected(CommandError):
    """Raised when the bot is already connected to a voice channel."""
    def __init__(self, message="The bot is already connected to a voice channel."):
        super().__init__(message)


class NotConnected(CommandError):
    """Raised when the bot is not connected to a voice channel."""
    def __init__(self, message="The bot is not connected to a voice channel."):
        super().__init__(message)


class MissingRequiredArgs(CommandError):
    """Raised when a command is missing required arguments."""
    def __init__(self, message="Missing required arguments."):
        super().__init__(message)


class InvalidSource(CommandError):
    """Raised when the user specifies an invalid music source."""
    def __init__(self, message="Invalid music source."):
        super().__init__(message)


class SongNotFound(CommandError):
    """Raised when the bot cannot find a requested song."""
    def __init__(self, message="Could not find a song matching that query."):
        super().__init__(message)


class APIError(CommandError):
    """Raised when an API request fails."""
    def __init__(self, message="An error occurred while communicating with the API."):
        super().__init__(message)


class DatabaseError(CommandError):
    """Raised when a database operation fails."""
    def __init__(self, message="An error occurred while interacting with the database."):
        super().__init__(message)


class GenericError(CommandError):
    """A general-purpose error class for unexpected errors."""
    def __init__(self, message="An unexpected error occurred."):
        super().__init__(message)