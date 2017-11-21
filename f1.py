#!/usr/bin/env python3

"""
This little module downloads and parses information about formula 1 seasons,
tracks, drivers, etc.
"""

import pandas as pd
import requests
import sys
import os

pd.set_option('display.width', 2000)


def races_that_year(year):
    columns = ['Date', 'Grand Prix', 'Car', 'Winner', 'Time', 'Laps']
    filename = "races/%d.html" % year

    if os.path.isfile(filename):
        content = open(filename).read()
        print("Using local cache...")
    else:
        races_url = "https://www.formula1.com/en/results.html/%d/races.html"
        # using requests only because we want to use https
        response = requests.get(races_url % year)
        content = response.content

    df = pd.read_html(content)[0]
    return df[columns]


def drivers_that_year(year):
    columns = ['Driver', 'Pts', 'Car', 'Nationality']

    filename = "drivers/%d.html" % year

    if os.path.isfile(filename):
        content = open(filename).read()
        print("Using local cache...")
    else:
        races_url = "https://www.formula1.com/en/results.html/%d/drivers.html"
        # using requests only because we want to use https
        response = requests.get(races_url % year)
        content = response.content

    df = pd.read_html(content)[0]
    return df[columns]


def teams_that_year(year):
    columns = ['Pos', 'Pts', 'Team']
    filename = "team/%d.html" % year

    if os.path.isfile(filename):
        content = open(filename).read()
        print("Using local cache...")
    else:
        races_url = "https://www.formula1.com/en/results.html/%d/team.html"
        # using requests only because we want to use https
        response = requests.get(races_url % year)
        content = response.content
    df = pd.read_html(content)[0]
    return df[columns]


if __name__ == "__main__":
    year = int(sys.argv[1])
    assert 1950 <= int(year) <= 2017
    print("Races")
    print(races_that_year(year=year))
    print("Drivers")
    print(drivers_that_year(year=year))
    print("Teams")
    print(teams_that_year(year=year))
