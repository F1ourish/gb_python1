import requests

server = 'https://apiv3.apifootball.com/?action='
api_key = 'APIkey=7beefc62a2a8f56c7c9fd6949e7313c5a206176c2df6b626fa1290305d889419'
countries = (server+'get_countries&'+api_key)
ticket_1 = requests.get(countries)
print(ticket_1.json())
country_id = input("Enter Country Id from upper text which you would like to read about:")
leagues = (server+'get_leagues&country_id='+country_id+'&'+api_key)
ticket_2 = requests.get(leagues)
print(ticket_2.json())
league_id = input("Enter League Id from upper text which you would like to read about:")
teams = (server+'get_teams&league_id='+league_id+'&'+api_key)
ticket_3 = requests.get(teams)
print(ticket_3.json())
player_id = input("Enter Player Id from upper text which you would like to read about:")
players = (server+'get_players&player_id='+player_id+'&'+api_key)
ticket_4 = requests.get(players)
print(ticket_4.json())
