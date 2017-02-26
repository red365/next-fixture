# TO DO:
# Refactor to use json library for nicer data scraping
# Get previous form (difficult!!!)

import urllib
import sys

def get_team(team):
    # Pass team name in and then return the team number
    feed = urllib.urlopen("http://www.footballwebpages.co.uk/teams.json")
    page = feed.read()
    marker = page.find(team)
    if marker == -1:
        return marker
    snippet = page[marker-25:marker]
    team_num_start = snippet.find(":")
    team_num_end = snippet.find('"', team_num_start+3)
    team_num = snippet[team_num_start+3:team_num_end]
    return team_num

def get_next_fixture(num):
    # Takes team number and inserts it in URL to get the latest fixtures
    url = "http://www.footballwebpages.co.uk/matches.json?team=" + str(num) + "&fixtures=5&results=0" 
    feed = urllib.urlopen(url)
    page = feed.read()
    info = ["date", "competition", "status", "homeTeamName", "awayTeamName", "homeTeamNo"]
    i = 0
    for element in info:
        start_element = page.find(element)
        start_info = page.find(":", start_element)
        end_info = page.find('"', start_info+3)
        info[i] = page[start_info+3:end_info]
        i += 1
    team_name = home_or_away(num, info)
    return info, team_name

def home_or_away(n, p):
    if p[5] == n:
        return p[3]
    else:
        return p[4]

def format_output(p, name):
    output = """    """ + name + """'s next game:
    ----------------------
    """ + p[1] + """
    """ + p[0] + """, """ + p[2] + """
    """ + p[3] + """ v """ + p[4]
              
    return output

def generate_fixture():
     
     a = get_team(sys.argv[1])
     if a != -1:
         p, team = get_next_fixture(a)
         print format_output(p, team)
     else:
         print "Team unknown"
      


generate_fixture()
