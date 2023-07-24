import requests

from enumerators.PlatformEndpoints import PlatformEndpoints
from enumerators.RegionalEndpoints import RegionalEndpoints
from resources.DatabaseHandler import DatabaseHandler

class RiotAPI:
    def __init__(self, dbh:DatabaseHandler=None):
        self.dbh = dbh
    
    def fetch(self, platform:PlatformEndpoints=None, region:RegionalEndpoints=None, endpoint:str=""):
        if type(platform) is not type(None):
            return self.dbh.check_for_cache(f'https://{platform.value}.api.riotgames.com{endpoint}')
        elif type(region) is not type(None):
            return self.dbh.check_for_cache(f'https://{region.value}.api.riotgames.com{endpoint}')
        raise Exception("Issues with querying RiotAPI: both platform and region cannot be None.")

    ### ACCOUNT-V1
    def get_riot_account_by_puuid(self, platform:PlatformEndpoints=None, region:RegionalEndpoints=None, puuid:str="") -> dict:
        return self.fetch(platform=platform, region=region, endpoint="/riot/account/v1/accounts/by-puuid/" + puuid)

    def get_riot_account_by_id(self, platform:PlatformEndpoints=None, region:RegionalEndpoints=None, gameName:str="", tagLine:str="") -> dict:
        return self.fetch(platform=platform, region=region, endpoint="/riot/account/v1/accounts/by-riot-id/" + gameName + "/" + tagLine)

    def get_riot_active_shards(self, platform:PlatformEndpoints=None, region:RegionalEndpoints=None, game:str="", puuid:str="") -> dict:
        return self.fetch(platform=platform, region=region, endpoint="/riot/account/v1/active-shards/by-game/" + game + "/by-puuid/" + puuid)

    ### CHAMPION-MASTERY-V4
    def get_champion_mastery_summoner_all(self, platform:PlatformEndpoints=None, region:RegionalEndpoints=None, summonerId:str="") -> dict:
        return self.fetch(platform=platform, region=region, endpoint="/lol/champion-mastery/v4/champion-masteries/by-summoner/" + summonerId)

    def get_champion_mastery_summoner_champion(self, platform:PlatformEndpoints=None, region:RegionalEndpoints=None, summonerId:str="", championId:str="") -> dict:
        return self.fetch(platform=platform, region=region, endpoint="/lol/champion-mastery/v4/champion-masteries/by-summoner/" + summonerId + "/by-champion/" + championId)

    def get_champion_master_scores(self, platform:PlatformEndpoints=None, region:RegionalEndpoints=None, summonerId:str="") -> dict:
        return self.fetch(platform=platform, region=region, endpoint="/lol/champion-mastery/v4/scores/by-summoner/" + summonerId)

    ### CHAMPION-V3
    def get_champion_rotations(self, platform:PlatformEndpoints=None, region:RegionalEndpoints=None) -> dict:
        return self.fetch(platform=platform, region=region, endpoint="/lol/platform/v3/champion-rotations")

    ### CLASH-V1
    def get_clash_by_summoner(self, platform:PlatformEndpoints=None, region:RegionalEndpoints=None, summonerId:str="") -> dict:
        return self.fetch(platform=platform, region=region, endpoint="/lol/clash/v1/players/by-summoner/" + summonerId)

    def get_clash_team(self, platform:PlatformEndpoints=None, region:RegionalEndpoints=None, teamId:str="") -> dict:
        return self.fetch(platform=platform, region=region, endpoint="/lol/clash/v1/teams/" + teamId)

    def get_clash_tournaments(self, platform:PlatformEndpoints=None, region:RegionalEndpoints=None) -> dict:
        return self.fetch(platform=platform, region=region, endpoint="/lol/clash/v1/tournaments")

    def get_clash_tournament_by_team(self, platform:PlatformEndpoints=None, region:RegionalEndpoints=None, teamId:str="") -> dict:
        return self.fetch(platform=platform, region=region, endpoint="/lol/clash/v1/tournaments/by-team/" + teamId)

    def get_clash_tournament_by_id(self, platform:PlatformEndpoints=None, region:RegionalEndpoints=None, tournamentId:str="") -> dict:
        return self.fetch(platform=platform, region=region, endpoint="/lol/clash/v1/tournaments/" + tournamentId)

    ### LEAGUE-EXP-V4
    def get_league_exp_entry(self, platform:PlatformEndpoints=None, region:RegionalEndpoints=None, queue:str="", tier:str="", division:str="") -> dict:
        return self.fetch(platform=platform, region=region, endpoint="/lol/league-exp/v4/entries/%s/%s/%s" % (queue, tier, division))

    ### LEAGUE-V4
    def get_league_challenger_by_queue(self, platform:PlatformEndpoints=None, region:RegionalEndpoints=None, queue:str="") -> dict:
        return self.fetch(platform=platform, region=region, endpoint="/lol/league/v4/challenger/leagues/by-queue/" + queue)

    def get_league_entry_by_summoner(self, platform:PlatformEndpoints=None, region:RegionalEndpoints=None, summonerId:str="") -> dict:
        return self.fetch(platform=platform, region=region, endpoint="/lol/league/v4/entries/by-summoner/" + summonerId)

    def get_league_entry(self, platform:PlatformEndpoints=None, region:RegionalEndpoints=None, queue:str="", tier:str="", division:str="") -> dict:
        return self.fetch(platform=platform, region=region, endpoint="/lol/league/v4/entries/%s/%s/%s" % (queue, tier, division))

    def get_league_grandmastersleague(self, platform:PlatformEndpoints=None, region:RegionalEndpoints=None, queue:str="") -> dict:
        return self.fetch(platform=platform, region=region, endpoint="/lol/league/v4/grandmasterleagues/by-queue/" + queue)

    def get_league_by_id(self, platform:PlatformEndpoints=None, region:RegionalEndpoints=None, leagueId:str="") -> dict:
        return self.fetch(platform=platform, region=region, endpoint="/lol/league/v4/leagues/" + leagueId)

    def get_league_masterleagues(self, platform:PlatformEndpoints=None, region:RegionalEndpoints=None, queue:str="") -> dict:
        return self.fetch(platform=platform, region=region, endpoint="/lol/league/v4/masterleagues/by-queue/" + queue)

    ### LOL-STATUS-V3
    def get_shard_status(self, platform:PlatformEndpoints=None, region:RegionalEndpoints=None) -> dict:
        return self.fetch(platform=platform, region=region, endpoint="/lol/status/v3/shard-data")

    ### LOL-STATUS-V4
    def get_platform_data(self, platform:PlatformEndpoints=None, region:RegionalEndpoints=None) -> dict:
        return self.fetch(platform=platform, region=region, endpoint="/lol/status/v4/platform-data")

    ### LOR-MATCH-V1
    def get_lor_match_by_puuid(self, platform:PlatformEndpoints=None, region:RegionalEndpoints=None, puuid:str="") -> dict:
        return self.fetch(platform=platform, region=region, endpoint="/lor/match/v1/matches/by-puuid/%s/ids" % puuid)

    def get_lor_match(self, platform:PlatformEndpoints=None, region:RegionalEndpoints=None, match_id:str="") -> dict:
        return self.fetch(platform=platform, region=region, endpoint="/lor/match/v1/matches/" + match_id)

    ### LOR-RANKED-V1
    def get_lor_ranked_leaderboards(self, platform:PlatformEndpoints=None, region:RegionalEndpoints=None) -> dict:
        return self.fetch(platform=platform, region=region, endpoint="/lor/ranked/v1/leaderboards")

    ### LOR-STATUS-V1
    def get_lor_status(self, platform:PlatformEndpoints=None, region:RegionalEndpoints=None) -> dict:
        return self.fetch(platform=platform, region=region, endpoint="/lor/status/v1/platform-data")

    ### MATCH-V4
    def get_league_match_by_id(self, platform:PlatformEndpoints=None, region:RegionalEndpoints=None, match_id:str="") -> dict:
        return self.fetch(platform=platform, region=region, endpoint="/lol/match/v5/matches/" + match_id)

    def get_league_match_by_puuid(self, region:RegionalEndpoints=RegionalEndpoints.Americas, puuid:str="") -> dict:
        return self.fetch(platform=None, region=region, endpoint=f"/lol/match/v5/matches/by-puuid/{puuid}/ids")

    def get_league_match_timeline_by_id(self, platform:PlatformEndpoints=None, region:RegionalEndpoints=None, match_id:str="") -> dict:
        return self.fetch(platform=platform, region=region, endpoint="/lol/match/v4/timelines/by-match/" + match_id)

    def get_league_matches_by_tournament_code(self, platform:PlatformEndpoints=None, region:RegionalEndpoints=None, tournament_code:str="") -> dict:
        return self.fetch(platform=platform, region=region, endpoint="/lol/match/v4/matches/by-tournament-code/%s/ids" % tournament_code)

    def get_league_match_by_tournament_code(self, platform:PlatformEndpoints=None, region:RegionalEndpoints=None, match_id:str="", tournament_code:str="") -> dict:
        return self.fetch(platform=platform, region=region, endpoint="/lol/match/v4/matches/%s/by-tournament-code/%s" % (match_id, tournament_code))

    ### SPECTATOR-V4
    def get_league_spectator_by_summoner(self, platform:PlatformEndpoints=None, region:RegionalEndpoints=None, summoner_id:str="") -> dict:
        return self.fetch(platform=platform, region=region, endpoint="/lol/spectator/v4/active-games/by-summoner/" + summoner_id)

    def get_league_spectator_featured_games(self, platform:PlatformEndpoints=None, region:RegionalEndpoints=None) -> dict:
        return self.fetch(platform=platform, region=region, endpoint="/lol/spectator/v4/featured-games")

    ### SUMMONER-V4
    def get_summoner_by_name(self, platform:PlatformEndpoints=None, region:RegionalEndpoints=None, name:str="") -> dict:
        return self.fetch(platform=platform, region=region, endpoint="/lol/summoner/v4/summoners/by-name/" + name)

    def get_summoner_by_account(self, platform:PlatformEndpoints=None, region:RegionalEndpoints=None, account_id:str="") -> dict:
        return self.fetch(platform=platform, region=region, endpoint="/lol/summoner/v1/summoners/by-account/" + account_id)

    def get_summoner_by_puuid(self, platform:PlatformEndpoints=None, region:RegionalEndpoints=None, puuid:str="") -> dict:
        return self.fetch(platform=platform, region=region, endpoint="/lol/summoner/v1/summoners/by-puuid/" + puuid)

    def get_summoner_by_id(self, platform:PlatformEndpoints=None, region:RegionalEndpoints=None, summonerId:str="") -> dict:
        return self.fetch(platform=platform, region=region, endpoint="/lol/summoner/v1/summoners/" + summonerId)

    ### TFT-LEAGUE-V1
    def get_tft_challenger(self, platform:PlatformEndpoints=None, region:RegionalEndpoints=None) -> dict:
        return self.fetch(platform=platform, region=region, endpoint="/tft/league/v1/challenger")

    def get_tft_entries_by_summoner(self, platform:PlatformEndpoints=None, region:RegionalEndpoints=None, summoner_id:str="") -> dict:
        return self.fetch(platform=platform, region=region, endpoint="/tft/league/v1/entries/by-summoner/" + summoner_id)

    def get_tft_entries(self, platform:PlatformEndpoints=None, region:RegionalEndpoints=None, tier:str="", division:str="") -> dict:
        return self.fetch(platform=platform, region=region, endpoint="/tft/league/v1/entries/%s/%s" % (tier, division))

    def get_tft_grandmaster(self, platform:PlatformEndpoints=None, region:RegionalEndpoints=None):
        return self.fetch(platform=platform, region=region, endpoint="/tft/league/v1/grandmaster")

    def get_tft_leagues_by_id(self, platform:PlatformEndpoints=None, region:RegionalEndpoints=None, league_id:str="") -> dict:
        return self.fetch(platform=platform, region=region, endpoint="/tft/league/v1/leagues/" + league_id)

    def get_tft_master(self, platform:PlatformEndpoints=None, region:RegionalEndpoints=None) -> dict:
        return self.fetch(platform=platform, region=region, endpoint="/tft/league/v1/master")

    ### TFT-MATCH-V1
    def get_tft_match_by_puuid(self, platform:PlatformEndpoints=None, region:RegionalEndpoints=None, puuid:str="") -> dict:
        return self.fetch(platform=platform, region=region, endpoint="/tft/match/v1/matches/by-puuid/%s/ids" % puuid)

    def get_tft_match_by_id(self, platform:PlatformEndpoints=None, region:RegionalEndpoints=None, match_id:str="") -> dict:
        return self.fetch(platform=platform, region=region, endpoint="/tft/match/v1/matches/" + match_id)

    ### TFT-SUMMONER-V1
    def get_tft_summoner_by_account(self, platform:PlatformEndpoints=None, region:RegionalEndpoints=None, account_id:str="") -> dict:
        return self.fetch(platform=platform, region=region, endpoint="/tft/summoner/v1/summoners/by-account/" + account_id)

    def get_tft_summoner_by_name(self, platform:PlatformEndpoints=None, region:RegionalEndpoints=None, name:str="") -> dict:
        return self.fetch(platform=platform, region=region, endpoint="/tft/summoner/v1/summoners/by-name/" + name)

    def get_tft_summoner_by_puuid(self, platform:PlatformEndpoints=None, region:RegionalEndpoints=None, puuid:str="") -> dict:
        return self.fetch(platform=platform, region=region, endpoint="/tft/summoner/v1/summoners/by-puuid/" + puuid)

    def get_tft_summoner_by_id(self, platform:PlatformEndpoints=None, region:RegionalEndpoints=None, summoner_id:str="") -> dict:
        return self.fetch(platform=platform, region=region, endpoint="/tft/summoner/v1/summoners/" + summoner_id)

    ### THIRD-PARTY-CODE-V4
    def get_third_party_code(self, platform:PlatformEndpoints=None, region:RegionalEndpoints=None, summoner_id:str="") -> dict:
        return self.fetch(platform=platform, region=region, endpoint="/lol/platform/v4/third-party-code/by-summoner/" + summoner_id)

    ### TOURNAMENT-STUB-V4
    def get_league_tournament_stub_codes(self, platform:PlatformEndpoints=None, region:RegionalEndpoints=None) -> dict:
        return self.fetch(platform=platform, region=region, endpoint="/lol/tournament-stub/v4/codes")

    def get_league_tournament_stub_by_code(self, platform:PlatformEndpoints=None, region:RegionalEndpoints=None, code:str="") -> dict:
        return self.fetch(platform=platform, region=region, endpoint="/lol/tournament-stub/v4/lobby-events/by-code/" + code)

    def get_league_tournament_stub_providers(self, platform:PlatformEndpoints=None, region:RegionalEndpoints=None) -> dict:
        return self.fetch(platform=platform, region=region, endpoint="/lol/tournament-stub/v4/providers")

    def get_league_tournament_stubs(self, platform:PlatformEndpoints=None, region:RegionalEndpoints=None) -> dict:
        return self.fetch(platform=platform, region=region, endpoint="/lol/tournament-stub/v4/tournaments")

    ### TOURNAMENT-V4
    def get_league_tournament_codes(self, platform:PlatformEndpoints=None, region:RegionalEndpoints=None) -> dict:
        return self.fetch(platform=platform, region=region, endpoint="/lol/tournament/v4/codes")

    def get_league_tournament_code_by_code(self, platform:PlatformEndpoints=None, region:RegionalEndpoints=None, code:str="") -> dict:
        return self.fetch(platform=platform, region=region, endpoint="/lol/tournament/v4/codes/" + code)

    def get_league_tournament_lobby_by_code(self, platform:PlatformEndpoints=None, region:RegionalEndpoints=None, code:str="") -> dict:
        return self.fetch(platform=platform, region=region, endpoint="/lol/tournament/v4/lobby-events/by-code/" + code)

    def get_league_tournament_providers(self, platform:PlatformEndpoints=None, region:RegionalEndpoints=None) -> dict:
        return self.fetch(platform=platform, region=region, endpoint="/lol/tournament/v4/providers")

    def get_league_tournament_tournaments(self, platform:PlatformEndpoints=None, region:RegionalEndpoints=None) -> dict:
        return self.fetch(platform=platform, region=region, endpoint="/lol/tournament/v4/tournaments")

    ### VAL-CONTENT-V1
    def get_valorant_content(self, platform:PlatformEndpoints=None, region:RegionalEndpoints=None) -> dict:
        return self.fetch(platform=platform, region=region, endpoint="/val/content/v1/contents")

    ### VAL-MATCH-V1
    def get_valorant_match_by_id(self, platform:PlatformEndpoints=None, region:RegionalEndpoints=None, match_id:str="") -> dict:
        return self.fetch(platform=platform, region=region, endpoint="/val/match/v1/matches/" + match_id)

    def get_valorant_match_by_puuid(self, platform:PlatformEndpoints=None, region:RegionalEndpoints=None, puuid:str="") -> dict:
        return self.fetch(platform=None, region=region, endpoint="/val/match/v1/matchlists/by-puuid/" + puuid)

    def get_valorant_match_by_queue(self, platform:PlatformEndpoints=None, region:RegionalEndpoints=None, queue:str="") -> dict:
        return self.fetch(platform=platform, region=region, endpoint="/val/match/v1/recent-matches/by-queue/" + queue)

    ### VAL-RANKED-V1
    def get_valorant_ranked_by_act(self, platform:PlatformEndpoints=None, region:RegionalEndpoints=None, act_id:str="") -> dict:
        return self.fetch(platform=platform, region=region, endpoint="/val/ranked/v1/leaderboards/by-act/" + act_id)

    ### VAL-STATUS-V1
    def get_valorant_platform_data(self, platform:PlatformEndpoints=None, region:RegionalEndpoints=None):
        return self.fetch(platform=platform, region=region, endpoint="/val/status/v1/platform-data")

    ### DDragon for League of Legends
    def get_ddragon_champion_json(self):
        return self.dbh.check_for_cache('http://ddragon.leagueoflegends.com/cdn/12.6.1/data/en_US/champion.json')['response']
