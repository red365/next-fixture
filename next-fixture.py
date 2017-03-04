# TO DO:
# Get previous form - DIFFICULT.

import json
import urllib
import sys

def get_team_id(my_team):
    teams = get_json("http://www.footballwebpages.co.uk/teams.json")
    inner_list = teams["teams"]["team"][:]
    for team in inner_list:
        if team["name"] == my_team:
            return team["id"]
    return -1

def get_next_fixture(team_id):
    return get_json("http://www.footballwebpages.co.uk/matches.json?team=%s&fixtures=5&results=0" % (str(team_id)))         
    

def get_json(url):
    page = urllib.urlopen(url)
    json_data = page.read()
    decoded_json = json_data.decode('iso-8859-1')
    data = json.loads(decoded_json)
    return data

def format_fixture(fixture_info):
    next_match = fixture_info["matchesTeam"]["match"][:]
    formatted_fixture = """    %s's next game:
    ----------------------
    %s
    %s %s 
    %s v %s """ % (fixture_info["matchesTeam"]["team"],
                    next_match[0]["competition"],
                    next_match[0]["date"],
                    next_match[0]["status"],
                    next_match[0]["homeTeamName"],
                    next_match[0]["awayTeamName"])
       
    return formatted_fixture

def generate_fixture():     
     team_id_no = get_team_id(sys.argv[1])
     if team_id_no != -1:
         print format_fixture(get_next_fixture(team_id_no))
     else:
         print "Team unknown or team name is incomplete ---> Check spelling and capitalisation"
      
generate_fixture()
