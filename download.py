#!/usr/bin/env python3
# coding: utf-8

"""
Downloads all the stats from f1 website.
"""

import os
import time

import requests

MIN_YEAR, MAX_YEAR = 1950, 2017
BASE_URL = "https://www.formula1.com/en/results.html/"


def download(url):
    full_url = BASE_URL + url
    response = requests.get(full_url)
    return response.content


def filename(prefix):
    return "%s/%d.html" % (prefix, year)


def download_teams(year):
    return filename("teams"), download("%d/team.html" % year)


def download_races(year):
    return filename("races"), download("%d/races.html" % year)


def download_drivers(year):
    return filename("drivers"), download("%d/drivers.html" % year)


def store(filename, content):
    directory = os.path.dirname(os.path.realpath(filename))
    if not os.path.isdir(directory):
        os.makedirs(directory)

    with open(filename, 'w') as html_file:
        html_file.write(content)

    return filename


if __name__ == "__main__":
    for year in range(MIN_YEAR, MAX_YEAR + 1):
        print(store(*download_races(year)))
        print(store(*download_drivers(year)))
        print(store(*download_teams(year)))
        time.sleep(0.5)
