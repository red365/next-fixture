import urllib

def get_next_fixture():
    feed = urllib.urlopen("http://www.footballwebpages.co.uk/matches.json?team=70&fixtures=5&results=0")
    page = feed.read()
    info = ["date", "competition", "status", "homeTeamName", "awayTeamName"]
    i = 0
    for element in info:
        start_element = page.find(element)
        start_info = page.find(":", start_element)
        end_info = page.find('"', start_info+3)
        info[i] = page[start_info+3:end_info]
        i += 1

    return info

def format_output(p):
    output = """    Bristol Rovers next game:
    ----------------------
    """ + p[1] + """
    """ + p[0] + """, """ + p[2] + """
    """ + p[3] + """ v """ + p[4]
              
    return output



print format_output(get_next_fixture())
