import sqlite3
import os
from dotenv import load_dotenv

load_dotenv()
DATABASE_URI = os.getenv('DATABASE_URI')

class Config:
    def __init__(self):
        self.conn = sqlite3.connect(DATABASE_URI)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        """Creates the database table if it doesn't exist."""
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS server_config (
                server_id INTEGER PRIMARY KEY,
                key TEXT,
                value TEXT
            )
        """)
        self.conn.commit()

    def get_prefix(self, server_id):
        """Returns the command prefix for the server."""
        return self.select(server_id, 'prefix') or '!'

    def set_prefix(self, server_id, prefix):
        """Sets the command prefix for the server."""
        self.insert(server_id, 'prefix', prefix)

    def get_volume(self, server_id):
        """Returns the volume for the bot on the server."""
        return float(self.select(server_id, 'volume')) or 0.5

    def set_volume(self, server_id, volume):
        """Sets the volume for the bot on the server."""
        self.insert(server_id, 'volume', str(volume))

    def get_allowed_sources(self, server_id):
        """Returns the allowed music sources for the server."""
        sources_str = self.select(server_id, 'sources')
        if sources_str:
            return sources_str.split(',')
        else:
            return ['youtube', 'soundcloud', 'spotify']

    def set_allowed_sources(self, server_id, sources):
        """Sets the allowed music sources for the server."""
        self.insert(server_id, 'sources', ','.join(sources))

    def insert(self, server_id, key, value):
        """Inserts a new row into the database table."""
        try:
            self.cursor.execute("INSERT INTO server_config (server_id, key, value) VALUES (?, ?, ?)", (server_id, key, value))
            self.conn.commit()
        except sqlite3.IntegrityError:
            self.update(server_id, key, value)

    def update(self, server_id, key, value):
        """Updates an existing row in the database table."""
        self.cursor.execute("UPDATE server_config SET value=? WHERE server_id=? AND key=?", (value, server_id, key))
        self.conn.commit()

    def select(self, server_id, key):
        """Selects data from the database table based on a query."""
        self.cursor.execute("SELECT value FROM server_config WHERE server_id=? AND key=?", (server_id, key))
        result = self.cursor.fetchone()
        return result[0] if result else None

    def close(self):
        """Closes the database connection."""
        self.conn.close()