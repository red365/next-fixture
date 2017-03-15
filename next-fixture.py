import json
import urllib
import sys

def get_team_id(my_team):
    teams = get_json("http://www.footballwebpages.co.uk/teams.json")
    for team in teams["teams"]["team"]:
        if team["name"] == my_team:
            return team["id"]

def get_next_fixture(team_id):
    return get_json("http://www.footballwebpages.co.uk/matches.json?team=%s&fixtures=5&results=0" % team_id)         

def get_form(team_id, team_name):
    dataset = get_json("http://www.footballwebpages.co.uk/form.json?team=" + str(team_id))
    form = ""
    if dataset != "":
        for team in dataset["formGuide"]["team"]:
            if team["name"] == team_name:            
                for match in team["match"]:
                    if match["result"] == "Won":
                        form += "W"
                    elif match["result"] == "Drew":
                        form += "D"
                    else:
                        form += "L"
    return form

def get_json(url):
    try:
        page = urllib.urlopen(url)
        json_data = page.read()
        decoded_json = json_data.decode('iso-8859-1')
        data = json.loads(decoded_json)
    except:
        return ""
    return data

def format_fixture(fixture_info):
    next_match = fixture_info["matchesTeam"]["match"][0]
    formatted_fixture = """    %s's next game:
    ----------------------
    %s
    %s %s 
    %s v %s 
    Home Form: %s   Away Form: %s """ % (fixture_info["matchesTeam"]["team"],
                                           next_match["competition"],
                                           next_match["date"],
                                           next_match["status"],
                                           next_match["homeTeamName"],
                                           next_match["awayTeamName"],
                                           get_form(next_match["homeTeamNo"], next_match["homeTeamName"]),
                                           get_form(next_match["awayTeamNo"], next_match["awayTeamName"])
                                           )
    
       
    return formatted_fixture

def generate_fixture():     
     team_id_no = get_team_id(sys.argv[1])
     if team_id_no:
         print format_fixture(get_next_fixture(team_id_no))
     else:
         print "Team unknown or team name is incomplete ---> Check spelling and capitalisation"
      
generate_fixture()
