import os
import json
import asyncio
import requests
import argparse
from datetime import datetime
import discord
from discord import app_commands

from resources.RiotAPI import RiotAPI
from resources.DatabaseHandler import DatabaseHandler
from resources.DatabaseHandler import DatabaseEventType
from enumerators.PlatformEndpoints import PlatformEndpoints
from enumerators.RegionalEndpoints import RegionalEndpoints

argpar = argparse.ArgumentParser(prefix_chars="-")
argpar.add_argument("-debug", action="store_true")
args = argpar.parse_args()

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.messages = True
intents.presences = True

with open('../config.json', 'r') as f:
    tokens = json.loads(f.read())

string_time = "%d-%m-%Y %H:%M:%S"
dbh = DatabaseHandler(tokens['Riot Games'])
rito = RiotAPI(dbh=dbh)

command = {}

class MyClient(discord.Client):
    def __init__(self, *, intents: discord.Intents):
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        await self.tree.sync()

client = MyClient(intents=intents)
tree = client.tree

@client.event
async def on_ready():
    print(f"Logged in as {client.user} with client id {client.user.id}")
    # print(f"https://discord.com/oauth2/authorize?client_id={client.application_id}&scope=bot&permissions=309668928")

@client.event
async def on_message(message):
    dbh.new_event(DatabaseEventType.message_received, message.guild.id, message.channel.id, False, False, message.created_at)
    dbh.new_message(message.id, message.guild.id, message.channel.id, message.author.id, message.created_at, message.content.replace("\"", "'"))

@client.event
async def on_message_edit(before, after):
    guild_channel = dbh.get_guild_logging_channel(after.guild.id)
    if guild_channel is not None:
        guild_channel = int(guild_channel)
        name = before.author.nick
        if type(name) is type(None):
            name = before.author.name
        name += "#%s" % before.author.discriminator
        embed = discord.Embed(color=discord.Colour.orange())
        embed.add_field(name="Message before edit", value=before.content, inline=False)
        embed.add_field(name="Message after edit", value=after.content, inline=False)
        embed.set_footer(text="%s | %s" % (name, after.edited_at.strftime(string_time)))
        channel = after.guild.get_channel(guild_channel)
        await channel.send('', embed=embed)
        dbh.new_event(DatabaseEventType.message_received, after.guild.id, after.channel.id, False, False, after.edited_at)
        dbh.message_edit(after.id, after.content, after.edited_at)

@client.event
async def on_message_delete(message):
    guild_channel = dbh.get_guild_logging_channel(message.guild.id)
    if guild_channel is not None:
        # guild_channel = int(guild_channel)
        name = message.author.nick
        if type(name) is type(None):
            name = message.author.name
        name += "#%s" % message.author.discriminator
        embed = discord.Embed(color=discord.Colour.red())
        embed.add_field(name="Deleted Message", value=message.content, inline=False)
        embed.add_field(name="Message ID", value=message.id, inline=False)
        embed.add_field(name="Channel", value=message.channel.mention)
        embed.set_footer(text="%s | %s" % (name, datetime.now().strftime(string_time)))
        channel = await message.guild.fetch_channel(guild_channel)
        await channel.send('', embed=embed)
        dbh.new_event(DatabaseEventType.message_deleted, message.guild.id, message.channel.id, False, False, datetime.now())

@client.event
async def on_raw_message_delete(payload):
    guild_channel = dbh.get_guild_logging_channel(str(payload.guild_id))
    if guild_channel is not None:
        guild_channel = int(guild_channel)
        msg = dbh.get_message(str(payload.message_id), str(payload.guild_id))
        await asyncio.sleep(3)
        last_message = None
        async for message in client.get_channel(guild_channel).history(limit=10):
            if message.author == client.user:
                if len(message.embeds) == 1:
                    if len(message.embeds[0].fields) >= 2:
                        for i in range(len(message.embeds[0].fields)):
                            if "Message ID" in message.embeds[0].fields[i].name:
                                if str(message.embeds[0].fields[i].value) in str(payload.message_id):
                                    last_message = message
        if type(last_message) is type(None):
            if type(msg) is not type(None):
                embed = discord.Embed(color=discord.Colour.red(), title="Message deleted")
                embed.add_field(name="Message content", value="%s" % msg["content"])
                user = client.get_user(msg['author_id'])
                if type(user) is type(None):
                    user = client.get_guild(payload.guild_id).get_member(msg['author_id'])
                if type(user) is not type(None):
                    embed.set_footer(text="Author - %s#%s" % (user.name, str(user.discriminator)))
                else:
                    embed.set_footer(text='Author ID: %s' % msg['author_id'])
                channel = client.get_channel(guild_channel)
                await channel.send('', embed=embed)
            else:
                embed = discord.Embed(color=discord.Colour.red(), title="Old message deleted")
                embed.add_field(name="Deleted Message", value="ID: %s" % payload.message_id)
                embed.add_field(name="Deleted in Channel", value="ID: %s" % payload.channel_id)
                channel = client.get_channel(guild_channel)
                await channel.send('', embed=embed)
            dbh.new_event(DatabaseEventType.message_deleted, payload.message_id, payload.channel_id, False, False, datetime.now())
        dbh.delete_message(payload.message_id, payload.guild_id)

@client.event
async def on_member_join(member):
    guild_channel = dbh.get_guild_logging_channel(member.guild.id)
    if guild_channel is not None:
        guild_channel = int(guild_channel)
        name = member.nick
        if type(name) is type(None):
            name = member.name
        name += "#%s" % member.discriminator
        embed = discord.Embed(color=discord.Colour.green(), title="User joined")
        embed.set_footer(text="%s | %s" % (name, member.joined_at.strftime(string_time)))
        channel = member.guild.get_channel(guild_channel)
        await channel.send('', embed=embed)
        dbh.new_event(DatabaseEventType.member_joined, member.guild.id, "", False, False, member.joined_at)

@client.event
async def on_member_remove(member):
    guild_channel = dbh.get_guild_logging_channel(member.guild.id)
    if guild_channel is not None:
        guild_channel = int(guild_channel)
        name = member.nick
        if type(name) is type(None):
            name = member.name
        name += "#%s" % member.discriminator
        embed = discord.Embed(color=discord.Colour.red(), title="User left server")
        embed.set_footer(text=name)
        channel = member.guild.get_channel(guild_channel)
        await channel.send('', embed=embed)
        dbh.new_event(DatabaseEventType.member_banned, member.guild.id, "", False, False, datetime.now())

@client.event
async def on_guild_join(guild):
    dbh.new_event(DatabaseEventType.guild_joined, guild.id, "", False, False, datetime.now())
    splash = ""
    if hasattr(guild, "splash_url"):
        splash = guild.splash_url
    banner = ""
    if hasattr(guild, "banner_url"):
        banner = guild.banner_url
    icon = ""
    if hasattr(guild, "icon_url"):
        icon = guild.icon_url
    dbh.add_server(guild.id, guild.owner_id, splash, banner, icon)

@client.event
async def on_guild_remove(guild):
    dbh.new_event(DatabaseEventType.guild_left, guild.id, "", False, False, datetime.now())

@client.event
async def on_presence_update(before, after):
    for act in after.activities:
        if type(act) is type(discord.Game):
            name = act.name
            start = act.start
            if type(act.end) is type(None):
                dbh.add_activity_update("GAME", game_name=name, start=start)
        elif type(act) is type(discord.Streaming):
            game = act.game
            stream_name = act.name
            url = act.url
            dbh.add_activity_update("STREAM", game_name=game, ref_url=url)

########################
#### Admin Commands ####
########################
@client.tree.command()
async def setlog(interaction:discord.Interaction):
    """Sets the channel to commit all message edits, user joins, user leaves, etc through"""
    dbh.set_guild_logging_channel(interaction.guild.id, interaction.channel.id, datetime.now())
    await interaction.response.send_message(f"Set up channel - {interaction.channel.mention} - for message logging functionality")

@client.tree.command()
@app_commands.describe(
    messages_to_delete='The number of messages we would like to delete'
)
async def clean(interaction:discord.Interaction, messages_to_delete:int):
    """Bulk delete messages within the channel the command is sent to"""
    messages = [message async for message in interaction.channel.history(limit=messages_to_delete)]
    if messages[-1].created_at.timestamp() > messages[0].created_at.timestamp():
        del messages[-1]
    else:
        del messages[0]
    await interaction.channel.delete_messages(messages)
    await interaction.response.send_message(f"Deleted {messages_to_delete} messages", ephemeral=True)

@client.tree.command()
@app_commands.describe(
    id='The id of the user you would like to ban'
)
async def shadowban(interaction:discord.Interaction, id:str):
    """Bans a user by ID so they do not have to be joined to the server to be banned."""
    user = await client.fetch_user(id)
    await interaction.guild.ban(user=user)
    await interaction.response.send_message(f"Banned {user.name}#{user.discriminator}.")

#############################
#### Riot Games Commands ####
#############################
@client.tree.command()
@app_commands.describe(
    summoner_name="Name of the player you want to search for",
    endpoint=f"{PlatformEndpoints._member_names_}"
)
async def recentleaguematch(interaction:discord.Interaction, summoner_name:str, endpoint:str="NorthAmerica"):
    if endpoint in PlatformEndpoints._member_names_:
        plat = PlatformEndpoints._member_map_[endpoint]
        name_resp = rito.get_summoner_by_name(platform=plat, name=summoner_name)
        reg = RegionalEndpoints.Americas
        match_list = rito.get_league_match_by_puuid(region=reg, puuid=json.loads(name_resp['response'])['puuid'])
        match_details = json.loads(rito.get_league_match_by_id(region=reg, match_id=json.loads(match_list['response'])[0])['response'])
        participant_info = {}
        for i in match_details['info']['participants']:
            if summoner_name.lower() in str(i['summonerName']).lower():
                participant_info = i
        print(participant_info)
        k_d_a:int = (participant_info['kills'] + participant_info['assists']) / participant_info['deaths']
        participant_info.update({'kda': k_d_a})
        embed = discord.Embed(title="LoL Match")
        embed.add_field(name="Role", value=participant_info['role'])
        embed.add_field(name="Champion", value=participant_info['championName'])
        embed.add_field(name="Kills", value=participant_info['kills'])
        embed.add_field(name="Deaths", value=participant_info['deaths'])
        embed.add_field(name="Assists", value=participant_info['assists'])
        embed.add_field(name="K/D/A Ratio", value="%.2f" % participant_info['kda'])
        embed.add_field(name="Lane", value=participant_info['lane'])
        await interaction.response.send_message('', embed=embed)
    else:
        plat_names = [str(i) for i in PlatformEndpoints._member_names_]
        plat_list = "[%s]" % ','.join(plat_names)
        embed = discord.Embed(title="Error", description=f'Platform unknown.. Please try again using one of the following: {plat_list}')
        await interaction.response.send_message('', embed=embed)

@client.tree.command()
@app_commands.describe(
    summoner_name="Name of the user you would like to look up (ex. ZeusChops, C9 Sneaky, )",
    endpoint=f"{PlatformEndpoints._member_names_}"
)
async def summonerinfo(interaction:discord.Interaction, summoner_name:str, endpoint:str='NorthAmerica'):
    if endpoint in PlatformEndpoints._member_names_:
        plat = PlatformEndpoints._member_map_[endpoint]
        resp = json.loads(rito.get_summoner_by_name(platform=plat, name=summoner_name)['response'])
        embed = discord.Embed(title=summoner_name, color=discord.Colour.green())
        print(resp)
        embed.add_field(name='id', value=resp['id'])
        embed.add_field(name='accountId', value=resp['accountId'])
        embed.add_field(name='puuid', value=resp['puuid'])
        embed.add_field(name='name', value=resp['name'])
        embed.add_field(name='profileIconId', value=resp['profileIconId']) #TODO: Update to use Profile Icon in embed
        embed.add_field(name='Last Updated', value=resp['revisionDate'])
        embed.add_field(name='Level', value=resp['summonerLevel'])
        await interaction.response.send_message('', embed=embed)
    else:
        plat_names = [str(i) for i in PlatformEndpoints._member_names_]
        plat_list = "[%s]" % ','.join(plat_names)
        embed = discord.Embed(title="Error", description=f'Platform unknown.. Please try again using one of the following: {plat_list}')
        await interaction.response.send_message('', embed=embed)

@client.tree.command()
@app_commands.describe(
    endpoint=f"{PlatformEndpoints._member_names_}"
)
async def champrotations(interaction:discord.Interaction, endpoint:str='NorthAmerica'):
    if endpoint in PlatformEndpoints._member_names_:
        plat = PlatformEndpoints[endpoint]
        champ_rot = json.loads(rito.get_champion_rotations(platform=plat)['response'].replace("'", '"'))
        ddragon = rito.get_ddragon_champion_json()
        champ_dict = ddragon['data']
        key_champ = {}
        for champion in list(champ_dict):
            key_champ.update({champ_dict[champion]['key']:champion})
        free_rot_champs = [[], []]
        for i in champ_rot['freeChampionIds']:
            free_rot_champs[0].append(key_champ[str(i)])
        for j in champ_rot['freeChampionIdsForNewPlayers']:
            free_rot_champs[1].append(key_champ[str(j)])
        embed = discord.Embed(title='Free Champion Rotation')
        embed.add_field(name='General', value='\n'.join(free_rot_champs[0]))
        embed.add_field(name='New Players', value='\n'.join(free_rot_champs[1]))
        await interaction.response.send_message('', embed=embed)
    else:
        plat_names = [str(i) for i in PlatformEndpoints._member_names_]
        plat_list = "[%s]" % ','.join(plat_names)
        embed = discord.Embed(title="Error", description=f'Platform unknown.. Please try again using one of the following: {plat_list}')
        await interaction.response.send_message('', embed=embed)

@client.tree.command()
@app_commands.describe(
    summoner_name="Which summoner name you would like to see recent matches for.",
    endpoint=f"Different locations to pick from - [{','.join(RegionalEndpoints._member_names_)}]"
)
async def recentmatches(interaction:discord.Interaction, summoner_name:str, endpoint:str="NorthAmerica"):
    if endpoint in PlatformEndpoints._member_names_:
        plat = PlatformEndpoints[endpoint]
        acct = json.loads(rito.get_summoner_by_name(platform=plat, name=summoner_name)['response'])
        print(acct)
        #TODO: Adjust RegionalEndpoints to have a lookup from PlatformEndpoints
        resp = rito.get_league_match_by_puuid(region=RegionalEndpoints.Americas, puuid=acct['puuid']) #This should not be hardcoded in in this way
        match_arr = json.loads(resp['response'])
        embed = discord.Embed(title="Recent Matches")
        embed.add_field(name="Matches", value='\n'.join(match_arr))
        await interaction.response.send_message('', embed=embed)
    else:
        plat_names = [str(i) for i in PlatformEndpoints._member_names_]
        plat_list = "[%s]" % ','.join(plat_names)
        embed = discord.Embed(title="Error", description=f'Platform unknown.. Please try again using one of the following: {plat_list}')
        await interaction.response.send_message('', embed=embed)

#############################
##### General  Commands #####
#############################
@client.tree.command()
@app_commands.describe(
    url="URL to check if it has been shortened."
)
async def urlcheck(interaction:discord.Interaction, url:str):
    """Checks to see if a URL is shortened."""
    if not url.startswith("https://"):
        url = "https://" + url
    req = requests.get(url)
    if url.lower() in req.url.lower().replace("https://www.","https://"):
        await interaction.response.send_message(f"URL ({url}) not shortened!")
    else:
        await interaction.response.send_message(f"URL shortened. Original is {req.url}")

@client.tree.command()
async def ping(interaction:discord.Interaction):
    """Determines the latency of the bot to Discord's API"""
    await interaction.response.send_message(f"Pong! ({str(int(round(interaction.client.latency*1000,0)))} ms)")

@client.tree.command()
async def invite(interaction:discord.Interaction):
    """Sends an invite to invite the bot to your server."""
    embed = discord.Embed(title="Invite me to your server!", url=f"https://discord.com/oauth2/authorize?client_id={interaction.client.application_id}&scope=bot&permissions=309668928")
    await interaction.response.send_message(embed=embed, ephemeral=True)

@client.tree.command()
async def github(interaction:discord.Interaction):
    """Requests the GitHub link for the project for this discord bot"""
    embed = discord.Embed(title="Check me out on GitHub!", url="https://github.com/riigess/Luna")
    embed.set_image(url='https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png')
    await interaction.response.send_message(embed=embed, ephemeral=True)


service_name = "discord"
token = tokens[service_name]
client.run(token)
