import requests
from urllib.parse import urljoin
import os
from players import TEST
from pprint import pprint
from bs4 import BeautifulSoup


baseUrl = r'https://playoverwatch.com/en-us/career'

def createPlayerUrl(playerDict:dict) -> str:
    return '/'.join([baseUrl, playerDict['platform'], playerDict['tag']])


def getSr(playerUrl:str) -> dict:
    srDict = {}
    response = requests.get(playerUrl)
    if response.status_code != 200:
        raise Exception('Not 200 status code')
    soup = BeautifulSoup(response.text, 'html.parser')
    tankSrSibling = soup.find('div', {'data-ow-tooltip-text': 'Tank Skill Rating'})
    # print(tankSrSibling)
    if tankSrSibling is not None:
        tankSr = int(tankSrSibling.parent.find('div', {'class': 'competitive-rank-level'}).text)
        srDict.update({'tank': tankSr})
    dpsSrSibling = soup.find('div', {'data-ow-tooltip-text': 'Damage Skill Rating'})
    # print(dpsSrSibling)
    if dpsSrSibling is not None:
        dpsSr = int(dpsSrSibling.parent.find('div', {'class': 'competitive-rank-level'}).text)
        srDict.update({'dps': dpsSr})
    supportSrSibling = soup.find('div', {'data-ow-tooltip-text': 'Support Skill Rating'})
    # print(supportSrSibling)
    if supportSrSibling is not None:
        supportSr = int(supportSrSibling.parent.find('div', {'class': 'competitive-rank-level'}).text)
        srDict.update({'support': supportSr})

    return srDict



if __name__ == '__main__':
    url = createPlayerUrl(TEST)
    pprint(getSr(url))