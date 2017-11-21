#!/usr/bin/env python3
# coding: utf-8

"""
Downloads all the stats from f1 website.
"""

import requests

MIN_YEAR, MAX_YEAR = 1950, 2017


def download_races(year):
    races_url = "https://www.formula1.com/en/results.html/%d/races.html"
    response = requests.get(races_url % year)
    return response.content


def store_race(year, content):
    filename = 'races/%d.html' % year
    with open(filename, 'w') as html_file:
        html_file.write(content)

    return filename


if __name__ == "__main__":
    for year in range(MIN_YEAR, MAX_YEAR + 1):
        print(store_race(year, download_races(year)))
