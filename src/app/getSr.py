import requests
from urllib.parse import urljoin
import os
from players import TEST
from pprint import pprint
from bs4 import BeautifulSoup


baseUrl = r'https://playoverwatch.com/en-us/career'

def createPlayerUrl(playerDict:dict) -> str:
    return '/'.join([baseUrl, playerDict['platform'], playerDict['tag']])

def _getSrForRole(soup:BeautifulSoup, srDict:dict, role:str):
    srSibling = soup.find('div', {'data-ow-tooltip-text': f'{role.capitalize()} Skill Rating'})
    # print(tankSrSibling)
    if srSibling is not None:
        sr = int(srSibling.parent.find('div', {'class': 'competitive-rank-level'}).text)
        srDict.update({role: sr})


def getSr(playerUrl:str) -> dict:
    srDict = {}
    response = requests.get(playerUrl)
    if response.status_code != 200:
        raise Exception('Not 200 status code')
    soup = BeautifulSoup(response.text, 'html.parser')

    for role in ['tank', 'damage', 'support']:
        _getSrForRole(soup, srDict, role)

    return srDict



if __name__ == '__main__':
    url = createPlayerUrl(TEST)
    pprint(getSr(url))