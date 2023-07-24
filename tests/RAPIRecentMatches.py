import os, sys, json

#Add available working directory to the path
cwd = os.getcwd()
sys.path.append('/'.join(cwd.split('/')[:-1]) + '/src')

from resources.RiotAPI import RiotAPI
from resources.DatabaseHandler import DatabaseHandler
from enumerators.PlatformEndpoints import PlatformEndpoints
from enumerators.RegionalEndpoints import RegionalEndpoints

na = PlatformEndpoints.NorthAmerica
dbh = DatabaseHandler('../src/database.sqlite')
rapi = RiotAPI(dbh=dbh)
name_resp = rapi.get_summoner_by_name(platform=na, name='YYRRRTTTT')
print(name_resp, '\n\n')
reg = RegionalEndpoints.Americas
fetch_matches = rapi.get_league_match_by_puuid(region=reg, puuid=json.loads(name_resp['response'])['puuid'])
print(fetch_matches)
