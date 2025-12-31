# 🎮 ERLC Bombay City Border Roleplay - Discord Bot

A comprehensive Discord bot for the **Erlc (Emergency Response Liberty County)** Roblox game community. Handles automated server setup with realistic roleplay departments, channels, and role management for your Bombay City Border roleplay server.

---

## ✨ Features

### 🚀 **One-Command Server Setup**
- **25+ Roleplay Roles** - Police, Fire, EMS, Civilian, Criminal, and Management roles
- **6 Department Categories** - Organized channels for each department
- **20+ Channels** - Pre-configured with proper permissions
- **Automatic Permissions** - Police, Fire, and Staff channels protected
- **Color-Coded Roles** - Easy identification (Blue=Police, Red=Fire, Green=Civilian, etc.)

### 🛡️ **Law Enforcement**
- Police Commissioner, Captain, Lieutenant, Sergeant, Officer, Cadet
- Private police channels with Officer-only access
- Dispatch and training channels

### 🚒 **Emergency Services**
- Fire Chief, Firefighter roles
- Paramedic, EMT roles
- Fire dispatch and operations channels

### 🏢 **Civilian Roleplay**
- Citizen, Taxi Driver, Truck Driver, Bus Driver
- Mechanic, Medic, Businessman roles
- Dedicated civilian chat and job channels

### ⚠️ **Criminal System**
- Criminal, Gang Member, Wanted, Smuggler roles
- Separate roleplay space

### 👨‍💼 **Management**
- Owner, Co-Owner, Administrator, Moderator, Staff
- Staff-only channels for administrative discussions

### 📊 **Easy Management Commands**
```
!setup                    - Initialize the entire server
!addrole @user role       - Assign a role
!removerole @user role    - Remove a role
!duty @user on/off        - Mark players on/off duty
!roleslist                - View all available roles
!channelslist             - View all channels
!serverinfo               - Show server statistics
```

---

## 📋 Role Structure

### 🚨 **Law Enforcement & Emergency (10 roles)**
```
Police Commissioner → Captain → Lieutenant → Sergeant → Officer → Cadet
Fire Chief → Firefighter
Paramedic → EMT
```

### 👥 **Civilian (7 roles)**
```
Citizen, Taxi Driver, Truck Driver, Bus Driver, Mechanic, Medic, Businessman
```

### 🔴 **Criminal (4 roles)**
```
Criminal, Gang Member, Wanted, Smuggler
```

### 🛡️ **Management (5 roles)**
```
Owner, Co-Owner, Administrator, Moderator, Staff
```

---

## 🏗️ Channel Structure

### 📢 **Announcements Category** (5 channels)
- **#announcements** - Important server announcements
- **#rules** - Server rules & roleplay guidelines
- **#updates** - Game and server updates
- **#welcome** - Welcome new members

### 🚔 **Police Department** (4 channels) *Officer Access Only*
- **#police-main** - General police chat
- **#police-reports** - Incident reports & case files
- **#police-dispatch** - Active calls and operations
- **#police-training** - Training and procedures

### 🚒 **Fire & EMS** (3 channels) *Firefighter/EMS Access Only*
- **#fire-main** - General fire department chat
- **#fire-dispatch** - Emergency calls
- **#ems-chat** - Paramedic/EMT operations

### 🏢 **Civilian** (4 channels) *Public*
- **#civilian-chat** - General roleplay chat
- **#jobs** - Job and employment discussions
- **#business** - Business and trading
- **#events** - Community events

### ⚠️ **Reports** (3 channels) *Public*
- **#reports** - Player reports & complaints
- **#appeals** - Ban/warning appeals
- **#suggestions** - Server suggestions

### 👨‍💼 **Staff** (3 channels) *Staff Access Only*
- **#staff-chat** - Staff discussions
- **#logs** - Server activity logs
- **#admin-chat** - Administrator communications

---

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- Discord bot token
- Server with admin permissions

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/aurora9161/bombay-city-border-roleplay.git
   cd bombay-city-border-roleplay
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Create Discord Bot**
   - Go to [Discord Developer Portal](https://discord.com/developers/applications)
   - Click "New Application"
   - Go to "Bot" and click "Add Bot"
   - Copy the token

4. **Configure bot token**
   ```bash
   cp .env.example .env
   ```
   - Open `.env` and replace `your_bot_token_here` with your token

5. **Set Bot Permissions**
   - Go to OAuth2 → URL Generator
   - Scopes: `bot`
   - Permissions:
     - Manage Roles
     - Manage Channels
     - Read Messages
     - Send Messages
     - Embed Links
     - Read Message History
   - Copy generated URL and invite bot to your server

6. **Run the bot**
   ```bash
   python bot.py
   ```

7. **Initialize server**
   ```
   !setup
   ```

---

## 📖 Commands Guide

### **Setup Commands**

#### `!setup`
Runs complete Erlc server initialization. Creates all roles, channels, and permissions.

```
!setup
```

**Requirements:** Administrator

---

### **Role Management**

#### `!addrole @user rolename`
Add a role to a member.

```bash
!addrole @john Police Officer
!addrole @sarah Firefighter
!addrole @mike Criminal
```

#### `!removerole @user rolename` (or `!demote`)
Remove a role from a member.

```bash
!removerole @john Police Officer
!demote @john Police Officer
```

---

### **Information Commands**

#### `!roleslist`
View all available roles organized by department.

```
!roleslist
```

#### `!channelslist`
View all channels organized by category.

```
!channelslist
```

#### `!serverinfo`
Display server statistics and information.

```
!serverinfo
```

---

### **Roleplay Commands**

#### `!duty @user on/off`
Mark a player as on-duty or off-duty (for tracking).

```bash
!duty @john on     # John is now on duty
!duty @john off    # John is now off duty
```

---

## 🔐 Permission System

| Channel | View | Send | Roles Allowed |
|---------|------|------|---------------|
| #police-* | ❌ | ❌ | Police Officer+ |
| #fire-* | ❌ | ❌ | Firefighter+ |
| #ems-chat | ❌ | ❌ | Paramedic, EMT |
| #staff-chat | ❌ | ❌ | Staff+ |
| #logs | ❌ | ❌ | Administrator+ |
| #admin-chat | ❌ | ❌ | Administrator+ |
| Others | ✅ | ✅ | Everyone |

---

## 🎯 Role Hierarchy

```
┌─ MANAGEMENT
│  ├─ Owner (gold)
│  ├─ Co-Owner (gold)
│  ├─ Administrator (purple)
│  ├─ Moderator (magenta)
│  └─ Staff (light gray)
│
├─ LAW ENFORCEMENT
│  ├─ Police Commissioner (blue)
│  ├─ Police Captain (blue)
│  ├─ Police Lieutenant (blue)
│  ├─ Police Sergeant (blue)
│  ├─ Police Officer (blue)
│  └─ Police Cadet (blue)
│
├─ EMERGENCY SERVICES
│  ├─ Fire Chief (red)
│  ├─ Firefighter (red)
│  ├─ Paramedic (orange)
│  └─ EMT (orange)
│
├─ CIVILIAN
│  ├─ Citizen (green)
│  ├─ Taxi Driver (yellow)
│  ├─ Truck Driver (gold)
│  ├─ Bus Driver (orange)
│  ├─ Mechanic (dark gray)
│  ├─ Medic (purple)
│  └─ Businessman (dark gray)
│
└─ CRIMINAL
   ├─ Criminal (dark red)
   ├─ Gang Member (dark red)
   ├─ Wanted (dark red)
   └─ Smuggler (dark red)
```

---

## 🐛 Troubleshooting

### **Bot not responding?**
1. Check if bot is online in Discord
2. Verify bot token in `.env` file
3. Ensure bot has required permissions
4. Check Python console for errors

### **Permission denied errors?**
1. Move bot role ABOVE other roles in server settings
2. Give bot "Administrator" or specific permissions:
   - Manage Roles
   - Manage Channels
3. Restart the bot

### **Channels/roles already exist?**
No problem! The bot checks for existing items and won't duplicate them. Safe to run `!setup` multiple times.

### **Bot token not working?**
1. Go to [Discord Developer Portal](https://discord.com/developers/applications)
2. Select your application
3. Copy the bot token from "Bot" section
4. Update `.env` with new token
5. Restart bot

---

## 📝 Configuration

Edit the following in `bot.py` to customize:

```python
# Line 24-30: Modify role names
AUTHORITY_ROLES = ["Police Officer", ...]

# Line 45-75: Modify channel structure and categories
DEPARTMENT_CHANNELS = {...}

# Line 244-265: Customize role colors
role_colors = {...}
```

---

## 🤝 Contributing

Feel free to fork and submit pull requests for improvements!

---

## 📄 License

MIT License - Use freely in your projects

---

## 🎮 For ERLC Community

Made with ❤️ for the **Erlc Bombay City Border Roleplay** community!

- 🎮 [Roblox ERLC Game](https://www.roblox.com/games/2534724415/)
- 📚 Supports realistic roleplay scenarios
- 👥 Organized team management
- 🔐 Secure role-based access

---

## 📞 Support

For issues or feature requests, open an issue on GitHub!

---

**Last Updated:** December 2025
**Made for:** Erlc Bombay City Border Roleplay
**Language:** Python 3.8+
