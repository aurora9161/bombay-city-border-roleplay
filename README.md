# Bombay City Border Roleplay - Discord Bot

A Discord bot for automated server setup for the **Erlc Bombay City Border Roleplay** community. This bot handles creation of channels, roles, and permission management.

## Features

✨ **Automated Server Setup**
- Creates all required roles (Owner, Co-Owner, Admin, Moderator, Staff, Member)
- Creates all necessary channels (announcements, rules, welcome, general, off-topic, staff-chat, logs, suggestions, reports)
- Automatically configures permissions

🔐 **Permission Management**
- Staff role gets exclusive access to #staff-chat
- No other roles receive channel permissions by default
- Easy role assignment and removal commands

⚡ **Easy to Use**
- Simple commands for server administration
- Built-in role and channel listing

## Installation

### Prerequisites
- Python 3.8+
- pip (Python package manager)
- Discord bot token

### Setup Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/aurora9161/bombay-city-border-roleplay.git
   cd bombay-city-border-roleplay
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Create a Discord Application**
   - Go to [Discord Developer Portal](https://discord.com/developers/applications)
   - Click "New Application"
   - Go to "Bot" section and click "Add Bot"
   - Copy your bot token

4. **Configure bot token**
   - Copy `.env.example` to `.env`
   - Replace `your_bot_token_here` with your actual token
   ```bash
   cp .env.example .env
   ```

5. **Set bot permissions**
   - Go to OAuth2 > URL Generator
   - Select scopes: `bot`
   - Select permissions:
     - Manage Roles
     - Manage Channels
     - View Channels
     - Send Messages
     - Read Messages
   - Copy generated URL and invite bot to your server

6. **Run the bot**
   ```bash
   python bot.py
   ```

## Commands

### `!setup`
Runs the complete server setup. Creates all roles and channels with proper permissions.

**Usage:**
```
!setup
```

**Requirements:** Administrator permission

### `!addrole`
Add a role to a member.

**Usage:**
```
!addrole @username rolename
```

**Examples:**
```
!addrole @john Staff
!addrole @admin Admin
```

### `!removerole`
Remove a role from a member.

**Usage:**
```
!removerole @username rolename
```

### `!roles`
List all roles in the server.

**Usage:**
```
!roles
```

### `!channels`
List all text channels in the server.

**Usage:**
```
!channels
```

## Server Structure

### Roles Created
- Owner
- Co-Owner
- Admin
- Moderator
- Staff
- Member

### Channels Created
- **#announcements** - Important announcements
- **#rules** - Server rules
- **#welcome** - Welcome messages
- **#general** - General chat
- **#off-topic** - Off-topic discussions
- **#staff-chat** - Private staff channel (Staff role only)
- **#logs** - Server logs
- **#suggestions** - Suggestions from members
- **#reports** - Report channel

## Permissions

- ✅ **Staff role**: Can view and send messages in #staff-chat
- ✅ **Everyone**: Has access to all other channels
- ✅ **No role restrictions**: Other roles don't have special channel permissions

## Troubleshooting

### Bot not responding?
1. Check if bot is online in Discord
2. Verify bot token is correct in `.env`
3. Ensure bot has required permissions
4. Check console for error messages

### Permission denied errors?
1. Ensure bot role is above other roles
2. Give bot "Manage Roles" and "Manage Channels" permissions
3. Make sure bot has administrator permissions

### Channels/roles already exist?
The bot checks for existing channels and roles before creating them, so you can safely run `!setup` multiple times.

## Support

For issues or questions, please create an issue on GitHub.

## License

MIT License - Feel free to use and modify!

## Made for
🎮 **Erlc Bombay City Border Roleplay** Community
