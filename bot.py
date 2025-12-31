import discord
from discord.ext import commands
import asyncio

# Bot setup with required intents
intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.guilds = True

bot = commands.Bot(command_prefix='!', intents=intents)

# Server configuration
ROLES = [
    "Owner",
    "Co-Owner",
    "Admin",
    "Moderator",
    "Staff",
    "Member"
]

CHANNELS = {
    "announcements": discord.ChannelType.text,
    "rules": discord.ChannelType.text,
    "welcome": discord.ChannelType.text,
    "general": discord.ChannelType.text,
    "off-topic": discord.ChannelType.text,
    "staff-chat": discord.ChannelType.text,
    "logs": discord.ChannelType.text,
    "suggestions": discord.ChannelType.text,
    "reports": discord.ChannelType.text,
}

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    print('------')

@bot.command(name='setup', help='Setup the server with channels and roles')
@commands.has_permissions(administrator=True)
async def setup_server(ctx):
    """Complete server setup with roles and channels"""
    
    guild = ctx.guild
    
    # Feedback message
    setup_msg = await ctx.send("🔧 Starting server setup...")
    
    try:
        # Create all roles
        created_roles = []
        for role_name in ROLES:
            try:
                # Check if role already exists
                existing_role = discord.utils.get(guild.roles, name=role_name)
                if existing_role:
                    created_roles.append(existing_role)
                    await setup_msg.edit(content=f"✅ Role '{role_name}' already exists")
                else:
                    role = await guild.create_role(
                        name=role_name,
                        color=discord.Color.blue(),
                        hoist=False,
                        mentionable=True
                    )
                    created_roles.append(role)
                    await setup_msg.edit(content=f"✅ Created role: {role_name}")
                    await asyncio.sleep(0.5)  # Rate limit protection
            except discord.Forbidden:
                await setup_msg.edit(content=f"❌ Permission denied creating role: {role_name}")
            except Exception as e:
                await setup_msg.edit(content=f"❌ Error creating role {role_name}: {str(e)}")
        
        # Create all channels
        created_channels = []
        for channel_name, channel_type in CHANNELS.items():
            try:
                existing_channel = discord.utils.get(guild.text_channels, name=channel_name)
                if existing_channel:
                    created_channels.append(existing_channel)
                    await setup_msg.edit(content=f"✅ Channel '{channel_name}' already exists")
                else:
                    # Create channel without permissions first
                    channel = await guild.create_text_channel(channel_name)
                    created_channels.append(channel)
                    await setup_msg.edit(content=f"✅ Created channel: {channel_name}")
                    await asyncio.sleep(0.5)  # Rate limit protection
            except discord.Forbidden:
                await setup_msg.edit(content=f"❌ Permission denied creating channel: {channel_name}")
            except Exception as e:
                await setup_msg.edit(content=f"❌ Error creating channel {channel_name}: {str(e)}")
        
        # Set permissions for staff-chat channel (Staff role gets access)
        staff_role = discord.utils.get(guild.roles, name="Staff")
        staff_channel = discord.utils.get(guild.text_channels, name="staff-chat")
        
        if staff_channel and staff_role:
            try:
                # Give staff role access to staff-chat
                await staff_channel.set_permissions(
                    staff_role,
                    read_messages=True,
                    send_messages=True,
                    view_channel=True
                )
                
                # Hide from @everyone
                await staff_channel.set_permissions(
                    guild.default_role,
                    read_messages=False,
                    send_messages=False,
                    view_channel=False
                )
                
                await setup_msg.edit(content="✅ Staff permissions set for staff-chat channel")
                await asyncio.sleep(0.5)
            except Exception as e:
                await setup_msg.edit(content=f"❌ Error setting staff permissions: {str(e)}")
        
        # Final message
        await setup_msg.edit(content=f"""
✅ **Server Setup Complete!**

📋 **Created Roles ({len(created_roles)}):**
{', '.join([r.name for r in created_roles])}

📝 **Created Channels ({len(created_channels)}):**
{', '.join([c.name for c in created_channels])}

🔐 **Permissions Applied:**
- Staff role has access to #staff-chat
- No other roles have channel permissions
- @everyone is hidden from #staff-chat

**Next Steps:**
- Assign roles to members using `!addrole @user @role`
- Configure additional permissions as needed
        """)
        
    except Exception as e:
        await setup_msg.edit(content=f"❌ Setup failed: {str(e)}")

@bot.command(name='addrole', help='Add a role to a member')
@commands.has_permissions(administrator=True)
async def add_role(ctx, member: discord.Member, *, role_name: str):
    """Add a role to a member"""
    
    role = discord.utils.get(ctx.guild.roles, name=role_name)
    
    if not role:
        await ctx.send(f"❌ Role '{role_name}' not found!")
        return
    
    try:
        await member.add_roles(role)
        await ctx.send(f"✅ Added {role.name} role to {member.mention}")
    except discord.Forbidden:
        await ctx.send("❌ I don't have permission to add roles!")
    except Exception as e:
        await ctx.send(f"❌ Error: {str(e)}")

@bot.command(name='removerole', help='Remove a role from a member')
@commands.has_permissions(administrator=True)
async def remove_role(ctx, member: discord.Member, *, role_name: str):
    """Remove a role from a member"""
    
    role = discord.utils.get(ctx.guild.roles, name=role_name)
    
    if not role:
        await ctx.send(f"❌ Role '{role_name}' not found!")
        return
    
    try:
        await member.remove_roles(role)
        await ctx.send(f"✅ Removed {role.name} role from {member.mention}")
    except discord.Forbidden:
        await ctx.send("❌ I don't have permission to remove roles!")
    except Exception as e:
        await ctx.send(f"❌ Error: {str(e)}")

@bot.command(name='roles', help='List all server roles')
async def list_roles(ctx):
    """List all roles in the server"""
    
    roles = ctx.guild.roles
    role_list = '\n'.join([f"• {role.name}" for role in reversed(roles)])
    
    embed = discord.Embed(
        title="📋 Server Roles",
        description=role_list if role_list else "No roles found",
        color=discord.Color.blue()
    )
    
    await ctx.send(embed=embed)

@bot.command(name='channels', help='List all server channels')
async def list_channels(ctx):
    """List all channels in the server"""
    
    channels = ctx.guild.text_channels
    channel_list = '\n'.join([f"• #{channel.name}" for channel in channels])
    
    embed = discord.Embed(
        title="📝 Server Channels",
        description=channel_list if channel_list else "No channels found",
        color=discord.Color.blue()
    )
    
    await ctx.send(embed=embed)

if __name__ == "__main__":
    bot.run('YOUR_BOT_TOKEN_HERE')
