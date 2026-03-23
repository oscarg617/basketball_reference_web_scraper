from basketball_reference_web_scraper import client
from basketball_reference_web_scraper.data import Team, OutputType

import requests
# r = requests.get('https://httpbin.org/headers')
# print(r.json())

client.play_by_play(Team.CHARLOTTE_HORNETS, 2, 11, 2025, output_type=OutputType.CSV, output_file_path='bad_game.csv')
