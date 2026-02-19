from basketball_reference_web_scraper import client
from basketball_reference_web_scraper.data import Team, OutputType

import requests
r = requests.get('https://httpbin.org/headers')
print(r.json())
