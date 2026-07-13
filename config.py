"""
Configuration settings for Paw Island Bot
"""

import os
from dotenv import load_dotenv

load_dotenv()

# Discord Bot Token
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

# Staff Role ID - Only members with this role can use staff commands
STAFF_ROLE_ID = int(os.getenv("STAFF_ROLE_ID", 0))

# Moderation Log Channel ID - Where all moderation actions are logged
MOD_LOG_CHANNEL_ID = int(os.getenv("MOD_LOG_CHANNEL_ID", 0))

# Bot Command Prefix (if not using slash commands)
BOT_PREFIX = "!"

# Warning threshold before auto-action (optional)
WARNING_THRESHOLD = 3

# Database configuration
DATABASE_PATH = "paw_island.db"

# Colors for embeds (Discord embed color integers)
COLORS = {
    "warning": 0xFFA500,      # Orange
    "ban": 0xFF0000,           # Red
    "kick": 0xDD0000,          # Dark Red
    "verbal": 0xFFFF00,        # Yellow
    "success": 0x00FF00,       # Green
    "info": 0x0099FF,          # Blue
}
