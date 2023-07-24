import os, sys, json

cwd = os.getcwd()
sys.path.append('/'.join(cwd.split('/')[:-1]) + '/src')

from resources.RiotAPI import RiotAPI
from resources.DatabaseHandler import DatabaseHandler
from enumerators.PlatformEndpoints import PlatformEndpoints
from enumerators.RegionalEndpoints import RegionalEndpoints

dbh = DatabaseHandler('../src/database.sqlite')
rito = RiotAPI(dbh=dbh)
match_id = "NA1_3893314203"
resp = rito.get_league_match_by_id(platform=None, region=RegionalEndpoints.Americas, match_id=match_id)

print(resp['response'])

f = open('../sample-responses/RAPILeagueMatch.json','w')
f.write(json.dumps(json.loads(resp['response']), indent=4, separators=(',',':')))
f.close()
