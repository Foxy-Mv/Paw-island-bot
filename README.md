# Paw Island Bot

A Discord staff bot for the Paw Island server. This bot helps staff members track and manage user warnings, bans, kicks, and verbal warnings.

## Features

- 🚨 **Warning System** - Issue and track user warnings with reasons
- 🚫 **Ban Management** - Record and manage user bans
- ⚠️ **Verbal Warnings** - Track unofficial warnings
- 👢 **Kick Management** - Log server kicks
- 📋 **User Records** - View complete moderation history for any user
- 📊 **Audit Logging** - Track all staff actions
- 🔐 **Staff Only** - Commands restricted to authorized staff members

## Features

- 🚨 **Warning System** - Issue and track user warnings with reasons
- 🚫 **Ban Management** - Record and manage user bans
- ⚠️ **Verbal Warnings** - Track unofficial warnings
- 👢 **Kick Management** - Log server kicks
- 📋 **User Records** - View complete moderation history for any user
- 📊 **Audit Logging** - Track all staff actions
- 🔐 **Staff Only** - Commands restricted to authorized staff members

## Setup

### Prerequisites
- Python 3.8+
- discord.py library
- SQLite3 (included with Python)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/Foxy-Mv/Paw-Island-Bot.git
cd Paw-Island-Bot
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the root directory:
```env
DISCORD_TOKEN=your_bot_token_here
STAFF_ROLE_ID=your_staff_role_id
MOD_LOG_CHANNEL_ID=your_moderation_log_channel_id
```

4. Run the bot:
```bash
python main.py
```

## Commands

### Staff Commands

- `/warn <user> [reason]` - Issue a warning to a user
- `/unban <user_id> [reason]` - Remove a warning from a user
- `/ban <user> [reason]` - Ban a user from the server
- `/kick <user> [reason]` - Kick a user from the server
- `/verbal <user> [reason]` - Issue a verbal warning
- `/record <user>` - View complete moderation history for a user
- `/clear-record <user_id>` - Clear all records for a user (Admin only)

## Configuration

Edit `config.py` to customize:
- Staff role requirements
- Logging channels
- Bot prefix
- Warning thresholds

## Database

The bot uses SQLite to store:
- User warnings
- Ban records
- Kick records
- Verbal warnings
- Staff action audit log

## Contributing

This is a private bot for Paw Island staff. Contact the owner for contributions.

## License

Proprietary - Paw Island Server
