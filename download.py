#!/usr/bin/env python3
# coding: utf-8

"""
Downloads all the stats from f1 website.
"""

import os
import time

import requests

MIN_YEAR, MAX_YEAR = 1950, 2017


def download_races(year):
    races_url = "https://www.formula1.com/en/results.html/%d/races.html"
    response = requests.get(races_url % year)
    return response.content


def store_race(year, content):
    if not os.path.isdir('races/'):
        os.makedirs('races/')

    filename = 'races/%d.html' % year
    with open(filename, 'w') as html_file:
        html_file.write(content)

    return filename


def download_drivers(year):
    drivers_url = "https://www.formula1.com/en/results.html/%d/drivers.html"
    response = requests.get(drivers_url % year)
    return response.content


def store_drivers_table(year, content):
    if not os.path.isdir('drivers/'):
        os.makedirs('drivers/')

    filename = 'drivers/%d.html' % year
    with open(filename, 'w') as html_file:
        html_file.write(content)

    return filename


def download_teams(year):
    teams_url = "https://www.formula1.com/en/results.html/%d/team.html"
    response = requests.get(teams_url % year)
    return response.content


def store_teams_table(year, content):
    if not os.path.isdir('teams/'):
        os.makedirs('teams/')

    filename = 'teams/%d.html' % year
    with open(filename, 'w') as html_file:
        html_file.write(content)

    return filename


if __name__ == "__main__":
    for year in range(MIN_YEAR, MAX_YEAR + 1):
        print(store_race(year, download_races(year)))
        print(store_drivers_table(year, download_drivers(year)))
        print(store_teams_table(year, download_teams(year)))
        time.sleep(0.5)
