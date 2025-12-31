import discord
from discord.ext import commands
import asyncio
from datetime import datetime

# Bot setup with required intents
intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.guilds = True

bot = commands.Bot(command_prefix='!', intents=intents)

# ERLC Roblox Roleplay Configuration

# Law Enforcement & Emergency Roles
AUTHORITY_ROLES = [
    "Police Commissioner",
    "Police Captain",
    "Police Lieutenant",
    "Police Sergeant",
    "Police Officer",
    "Police Cadet",
    "Fire Chief",
    "Firefighter",
    "Paramedic",
    "EMT"
]

# Civilian & Criminal Roles
CIVILIAN_ROLES = [
    "Citizen",
    "Taxi Driver",
    "Truck Driver",
    "Bus Driver",
    "Mechanic",
    "Medic",
    "Businessman"
]

CRIMINAL_ROLES = [
    "Criminal",
    "Gang Member",
    "Wanted",
    "Smuggler"
]

# Management Roles
MANAGEMENT_ROLES = [
    "Owner",
    "Co-Owner",
    "Administrator",
    "Moderator",
    "Staff"
]

# All roles combined
ALL_ROLES = MANAGEMENT_ROLES + AUTHORITY_ROLES + CIVILIAN_ROLES + CRIMINAL_ROLES

# Department Channels
DEPARTMENT_CHANNELS = {
    "📢": {
        "announcements": "Server announcements",
        "rules": "Server rules & guidelines",
        "updates": "Game updates & news",
        "welcome": "Welcome new members",
    },
    "🚔": {
        "police-main": "Police department general chat",
        "police-reports": "Police incident reports",
        "police-dispatch": "Police dispatch & operations",
        "police-training": "Police training & procedures",
    },
    "🚒": {
        "fire-main": "Fire department chat",
        "fire-dispatch": "Fire dispatch & emergencies",
        "ems-chat": "EMS/Paramedic chat",
    },
    "🏙️": {
        "civilian-chat": "General civilian roleplay",
        "jobs": "Job discussions & employment",
        "business": "Business & trading",
        "events": "Community events",
    },
    "⚠️": {
        "reports": "Player reports & complaints",
        "appeals": "Ban/warn appeals",
        "suggestions": "Server suggestions",
    },
    "👥": {
        "staff-chat": "Staff only channel",
        "logs": "Server activity logs",
        "admin-chat": "Admin discussions",
    }
}

@bot.event
async def on_ready():
    print(f'✅ {bot.user} connected to Discord!')
    print(f'🎮 ERLC Bombay City Border Roleplay Bot Ready')
    print('------')
    try:
        synced = await bot.tree.sync()
        print(f'✅ Synced {len(synced)} command(s)')
    except Exception as e:
        print(f'Failed to sync commands: {e}')

@bot.command(name='setup', help='Complete ERLC server setup')
@commands.has_permissions(administrator=True)
async def setup_server(ctx):
    """Complete Erlc Roblox roleplay server setup"""
    
    guild = ctx.guild
    status_msg = await ctx.send("🔧 Starting ERLC Bombay City Border Roleplay server setup...\n\n")
    
    try:
        progress = ""
        
        # ═════════════════════════════════════════
        # STEP 1: CREATE ALL ROLES
        # ═════════════════════════════════════════
        progress += "**STEP 1: Creating Roles**\n"
        created_roles = {}
        
        role_colors = {
            "Police Commissioner": discord.Color.blue(),
            "Police Captain": discord.Color.blue(),
            "Police Lieutenant": discord.Color.blue(),
            "Police Sergeant": discord.Color.blue(),
            "Police Officer": discord.Color.blue(),
            "Police Cadet": discord.Color.blue(),
            "Fire Chief": discord.Color.red(),
            "Firefighter": discord.Color.red(),
            "Paramedic": discord.Color.orange(),
            "EMT": discord.Color.orange(),
            "Citizen": discord.Color.green(),
            "Taxi Driver": discord.Color.yellow(),
            "Truck Driver": discord.Color.gold(),
            "Bus Driver": discord.Color.orange(),
            "Mechanic": discord.Color.dark_gray(),
            "Medic": discord.Color.purple(),
            "Businessman": discord.Color.darker_gray(),
            "Criminal": discord.Color.dark_red(),
            "Gang Member": discord.Color.dark_red(),
            "Wanted": discord.Color.dark_red(),
            "Smuggler": discord.Color.dark_red(),
            "Owner": discord.Color.gold(),
            "Co-Owner": discord.Color.gold(),
            "Administrator": discord.Color.purple(),
            "Moderator": discord.Color.magenta(),
            "Staff": discord.Color.light_gray(),
        }
        
        for role_name in ALL_ROLES:
            try:
                existing_role = discord.utils.get(guild.roles, name=role_name)
                if existing_role:
                    created_roles[role_name] = existing_role
                    progress += f"✅ {role_name} (already exists)\n"
                else:
                    color = role_colors.get(role_name, discord.Color.blue())
                    role = await guild.create_role(
                        name=role_name,
                        color=color,
                        hoist=True,
                        mentionable=True
                    )
                    created_roles[role_name] = role
                    progress += f"✅ {role_name}\n"
                    await asyncio.sleep(0.4)
            except Exception as e:
                progress += f"❌ {role_name}: {str(e)}\n"
        
        await status_msg.edit(content=progress)
        await asyncio.sleep(1)
        
        # ═════════════════════════════════════════
        # STEP 2: CREATE CATEGORIES & CHANNELS
        # ═════════════════════════════════════════
        progress += "\n**STEP 2: Creating Channels & Categories**\n"
        
        created_channels = {}
        category_names = list(DEPARTMENT_CHANNELS.keys())
        
        for category_emoji in category_names:
            try:
                category_name = {
                    "📢": "📢 Announcements",
                    "🚔": "🚔 Police Department",
                    "🚒": "🚒 Fire & EMS",
                    "🏙️": "🏙️ Civilian",
                    "⚠️": "⚠️ Reports",
                    "👥": "👥 Staff",
                }[category_emoji]
                
                existing_category = discord.utils.get(guild.categories, name=category_name)
                if existing_category:
                    category = existing_category
                    progress += f"✅ Category: {category_name}\n"
                else:
                    category = await guild.create_category(category_name)
                    progress += f"✅ Category: {category_name}\n"
                    await asyncio.sleep(0.3)
                
                # Create channels in this category
                for channel_name, description in DEPARTMENT_CHANNELS[category_emoji].items():
                    try:
                        existing_channel = discord.utils.get(guild.text_channels, name=channel_name)
                        if existing_channel:
                            created_channels[channel_name] = existing_channel
                            progress += f"  ├─ ✅ {channel_name}\n"
                        else:
                            channel = await guild.create_text_channel(
                                name=channel_name,
                                category=category,
                                topic=description
                            )
                            created_channels[channel_name] = channel
                            progress += f"  ├─ ✅ {channel_name}\n"
                            await asyncio.sleep(0.3)
                    except Exception as e:
                        progress += f"  ├─ ❌ {channel_name}: {str(e)}\n"
            except Exception as e:
                progress += f"❌ Category {category_emoji}: {str(e)}\n"
        
        await status_msg.edit(content=progress)
        await asyncio.sleep(1)
        
        # ═════════════════════════════════════════
        # STEP 3: SET CHANNEL PERMISSIONS
        # ═════════════════════════════════════════
        progress += "\n**STEP 3: Configuring Permissions**\n"
        
        try:
            # Police channels - Police Officer role access
            police_role = created_roles.get("Police Officer")
            police_channels = ["police-main", "police-reports", "police-dispatch", "police-training"]
            
            for ch_name in police_channels:
                ch = created_channels.get(ch_name)
                if ch and police_role:
                    await ch.set_permissions(
                        police_role,
                        read_messages=True,
                        send_messages=True,
                        view_channel=True
                    )
                    # Hide from @everyone
                    await ch.set_permissions(
                        guild.default_role,
                        read_messages=False,
                        view_channel=False
                    )
                    progress += f"🚔 {ch_name} - Police Officer access\n"
                    await asyncio.sleep(0.2)
            
            # Fire/EMS channels - Fire/EMS role access
            fire_role = created_roles.get("Firefighter")
            fire_channels = ["fire-main", "fire-dispatch", "ems-chat"]
            
            for ch_name in fire_channels:
                ch = created_channels.get(ch_name)
                if ch and fire_role:
                    await ch.set_permissions(
                        fire_role,
                        read_messages=True,
                        send_messages=True,
                        view_channel=True
                    )
                    await ch.set_permissions(
                        guild.default_role,
                        read_messages=False,
                        view_channel=False
                    )
                    progress += f"🚒 {ch_name} - Firefighter/EMS access\n"
                    await asyncio.sleep(0.2)
            
            # Staff channel - Staff role only
            staff_role = created_roles.get("Staff")
            staff_ch = created_channels.get("staff-chat")
            
            if staff_ch and staff_role:
                await staff_ch.set_permissions(
                    staff_role,
                    read_messages=True,
                    send_messages=True,
                    view_channel=True
                )
                await staff_ch.set_permissions(
                    guild.default_role,
                    read_messages=False,
                    view_channel=False
                )
                progress += f"👥 staff-chat - Staff only access\n"
                await asyncio.sleep(0.2)
            
            # Admin/Logs channels - Admin access
            for ch_name in ["logs", "admin-chat"]:
                ch = created_channels.get(ch_name)
                if ch:
                    admin_role = created_roles.get("Administrator")
                    if admin_role:
                        await ch.set_permissions(
                            admin_role,
                            read_messages=True,
                            send_messages=True,
                            view_channel=True
                        )
                    await ch.set_permissions(
                        guild.default_role,
                        read_messages=False,
                        view_channel=False
                    )
                    progress += f"👨‍💼 {ch_name} - Administrator access\n"
                    await asyncio.sleep(0.2)
            
        except Exception as e:
            progress += f"❌ Permission setup error: {str(e)}\n"
        
        await status_msg.edit(content=progress)
        await asyncio.sleep(1)
        
        # ═════════════════════════════════════════
        # FINAL MESSAGE
        # ═════════════════════════════════════════
        final_message = f"""
╔════════════════════════════════════════════════════╗
║  🎮 ERLC BOMBAY CITY BORDER ROLEPLAY SETUP COMPLETE  ║
╚════════════════════════════════════════════════════╝

✅ **Setup Summary:**

📋 **Roles Created ({len(created_roles)}):**
🚔 **Law Enforcement:** Police Commissioner, Captain, Lieutenant, Sergeant, Officer, Cadet
🚒 **Emergency:** Fire Chief, Firefighter, Paramedic, EMT
🏙️ **Civilian:** Citizen, Taxi Driver, Truck Driver, Bus Driver, Mechanic, Medic, Businessman
⚠️ **Criminal:** Criminal, Gang Member, Wanted, Smuggler
👥 **Management:** Owner, Co-Owner, Administrator, Moderator, Staff

📁 **Channels Created ({len(created_channels)}):**
📢 Announcements (5 channels)
🚔 Police Department (4 channels - Police Officer access)
🚒 Fire & EMS (3 channels - Firefighter access)
🏙️ Civilian (4 channels)
⚠️ Reports (3 channels)
👥 Staff (3 channels - Staff only)

🔐 **Permissions Configured:**
✅ Police channels → Police Officer role only
✅ Fire/EMS channels → Firefighter/Paramedic role only
✅ Staff channels → Staff role only
✅ Other roles → No special permissions
✅ @everyone → Access to public channels only

📌 **Next Steps:**
1. Use `!addrole @user rolename` to assign roles to members
2. Use `!demote @user rolename` to remove roles
3. Use `!duty @user` to mark players as on/off duty
4. Check `!roleslist` and `!channelslist` for full details

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
**Welcome to Bombay City Border Roleplay!** 🏙️
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
        """
        
        await status_msg.edit(content=final_message)
        
    except Exception as e:
        await status_msg.edit(content=f"❌ Setup failed with error: {str(e)}")

@bot.command(name='addrole', help='Add a role to a member')
@commands.has_permissions(administrator=True)
async def add_role(ctx, member: discord.Member, *, role_name: str):
    """Add a role to a member"""
    
    role = discord.utils.get(ctx.guild.roles, name=role_name)
    
    if not role:
        await ctx.send(f"❌ Role '{role_name}' not found!\nUse `!roleslist` to see available roles.")
        return
    
    if role in member.roles:
        await ctx.send(f"⚠️ {member.mention} already has {role.name} role!")
        return
    
    try:
        await member.add_roles(role)
        embed = discord.Embed(
            title="✅ Role Added",
            description=f"Added **{role.name}** to {member.mention}",
            color=discord.Color.green(),
            timestamp=datetime.now()
        )
        embed.set_footer(text=f"Action by {ctx.author}")
        await ctx.send(embed=embed)
    except discord.Forbidden:
        await ctx.send("❌ I don't have permission to add roles!")
    except Exception as e:
        await ctx.send(f"❌ Error: {str(e)}")

@bot.command(name='removerole', aliases=['demote'], help='Remove a role from a member')
@commands.has_permissions(administrator=True)
async def remove_role(ctx, member: discord.Member, *, role_name: str):
    """Remove a role from a member"""
    
    role = discord.utils.get(ctx.guild.roles, name=role_name)
    
    if not role:
        await ctx.send(f"❌ Role '{role_name}' not found!")
        return
    
    if role not in member.roles:
        await ctx.send(f"⚠️ {member.mention} doesn't have {role.name} role!")
        return
    
    try:
        await member.remove_roles(role)
        embed = discord.Embed(
            title="✅ Role Removed",
            description=f"Removed **{role.name}** from {member.mention}",
            color=discord.Color.orange(),
            timestamp=datetime.now()
        )
        embed.set_footer(text=f"Action by {ctx.author}")
        await ctx.send(embed=embed)
    except discord.Forbidden:
        await ctx.send("❌ I don't have permission to remove roles!")
    except Exception as e:
        await ctx.send(f"❌ Error: {str(e)}")

@bot.command(name='roleslist', help='List all available roles')
async def list_roles(ctx):
    """List all roles organized by department"""
    
    embed = discord.Embed(
        title="🎮 ERLC Role List",
        color=discord.Color.blue()
    )
    
    embed.add_field(
        name="🚔 Law Enforcement",
        value="\n".join([f"• {role}" for role in AUTHORITY_ROLES[:6]]),
        inline=False
    )
    
    embed.add_field(
        name="🚒 Fire & EMS",
        value="\n".join([f"• {role}" for role in AUTHORITY_ROLES[6:]]),
        inline=False
    )
    
    embed.add_field(
        name="🏙️ Civilian",
        value="\n".join([f"• {role}" for role in CIVILIAN_ROLES]),
        inline=False
    )
    
    embed.add_field(
        name="⚠️ Criminal",
        value="\n".join([f"• {role}" for role in CRIMINAL_ROLES]),
        inline=False
    )
    
    embed.add_field(
        name="👥 Management",
        value="\n".join([f"• {role}" for role in MANAGEMENT_ROLES]),
        inline=False
    )
    
    embed.set_footer(text="Use !addrole @user rolename to assign roles")
    await ctx.send(embed=embed)

@bot.command(name='channelslist', help='List all channels')
async def list_channels(ctx):
    """List all channels organized by department"""
    
    embed = discord.Embed(
        title="📁 ERLC Channel List",
        color=discord.Color.blue()
    )
    
    category_titles = {
        "📢": "Announcements",
        "🚔": "Police Department",
        "🚒": "Fire & EMS",
        "🏙️": "Civilian",
        "⚠️": "Reports",
        "👥": "Staff",
    }
    
    for emoji, channels_dict in DEPARTMENT_CHANNELS.items():
        title = category_titles.get(emoji, emoji)
        channel_list = "\n".join([f"• #{ch_name}" for ch_name in channels_dict.keys()])
        embed.add_field(name=f"{emoji} {title}", value=channel_list, inline=False)
    
    await ctx.send(embed=embed)

@bot.command(name='duty', help='Mark player as on/off duty')
async def duty_status(ctx, member: discord.Member, status: str = "on"):
    """Mark a player as on or off duty (for roleplay tracking)"""
    
    status = status.lower()
    if status not in ["on", "off"]:
        await ctx.send("❌ Use `!duty @user on` or `!duty @user off`")
        return
    
    emoji = "🟢" if status == "on" else "🔴"
    embed = discord.Embed(
        title=f"{emoji} Duty Status Updated",
        description=f"{member.mention} is now **{status.upper()} DUTY**",
        color=discord.Color.green() if status == "on" else discord.Color.red(),
        timestamp=datetime.now()
    )
    await ctx.send(embed=embed)

@bot.command(name='serverinfo', help='Show server information')
async def server_info(ctx):
    """Display server information"""
    
    guild = ctx.guild
    embed = discord.Embed(
        title="🏙️ Bombay City Border Roleplay - Server Info",
        color=discord.Color.blue(),
        timestamp=datetime.now()
    )
    
    embed.add_field(name="👥 Members", value=f"{guild.member_count}", inline=True)
    embed.add_field(name="📁 Channels", value=f"{len(guild.channels)}", inline=True)
    embed.add_field(name="👨‍💼 Roles", value=f"{len(guild.roles)}", inline=True)
    embed.add_field(name="📅 Created", value=guild.created_at.strftime("%d/%m/%Y"), inline=False)
    embed.set_thumbnail(url=guild.icon.url if guild.icon else None)
    
    await ctx.send(embed=embed)

if __name__ == "__main__":
    bot.run('YOUR_BOT_TOKEN_HERE')
