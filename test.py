import pandas as pandas
import re
import requests
from bs4 import BeautifulSoup

############################################ TEAM STATS ############################################

url = 'https://www.mlb.com/stats/team/on-base-percentage'
page = requests.get(url)

soup = BeautifulSoup(page.text, 'html.parser')

teams = soup.findAll('th data-col=0 data-row=0')
tags = soup.findAll('td')
data = []
teamslist = []

for team in teams:
    teamslist.append(team.text)

for tag in tags:
    data.append(tag.text)

print(data)
# Team names
mydivs = soup.find_all("span", {"class":"header__subnav--teams__team--name"})
# <span class="header__subnav--teams__team--name">

# print(mydivs)

for div in mydivs:
    teamslist.append(div.text)

# print(teamslist)

anotherlist = []
myteams = soup.find_all("th", {"data-col":"0"}, {"data-row":"0"})

for team in myteams:
    anotherlist.append(team.text)

anotherlist.pop(0)

data_dict = {}
all_data_dict = {}
heads = ['League', 'G', 'AB', 'R', 'H', '2B', '3B', 'HR', 'RBI', 'BB', 'SO', 'SB', 'CS', 'AVG', 'OBP', 'SLG', 'OPS']

count = 0
team_count = 0
for team in anotherlist:

    for c in range(0,17):
        data_dict[heads[c]] = data[count]
        all_data_dict[anotherlist[team_count]] = data_dict
        count += 1

    team_count += 1
    data_dict = {}

    

dataframe = pandas.DataFrame.from_dict(all_data_dict)

# print(dataframe['1Houston AstrosAstros1‌‌‌']['OBP'])


team_count = 0
for teams in anotherlist:
    print(dataframe[anotherlist[team_count]]['OBP'])
    team_count += 1

################################### DAILY MATCHUPS ########################################

url = 'https://www.mlb.com/schedule'
page = requests.get(url)

soup = BeautifulSoup(page.text, 'html.parser')

matchups = soup.find_all("div", {"TeamWrappersstyle__DesktopTeamWrapper-uqs6qh-0 hkpegb"})

matchups = soup.find_all("div", {"#gridWrapper:nth-child(2)"})
match_list = []
for match in matchups:
    match_list.append(match.text)

print(match_list)






#################################### BETTING ODDS #########################################


################################### FINAL DATAFRAME #######################################


################################## MACHINE LEARNING #######################################

