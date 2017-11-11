#!/usr/bin/env python3

"""
This little module downloads and parses information about formula 1 seasons,
tracks, drivers, etc.
"""

import pandas as pd
import requests
import sys

pd.set_option('display.width', 2000)


def races_that_year(year):
    columns = ['Date', 'Grand Prix', 'Car', 'Winner', 'Time', 'Laps']
    races_url = "https://www.formula1.com/en/results.html/%d/races.html"
    # using requests only because we want to use https
    response = requests.get(races_url % year)
    df = pd.read_html(response.content)[0]
    return df[columns]


def drivers_that_year(year):
    columns = ['Driver', 'Pts', 'Car', 'Nationality']
    races_url = "https://www.formula1.com/en/results.html/%d/drivers.html"
    # using requests only because we want to use https
    response = requests.get(races_url % year)
    df = pd.read_html(response.content)[0]
    return df[columns]


if __name__ == "__main__":
    year = int(sys.argv[1])
    assert 1950 <= int(year) <= 2017
    print("Races")
    print(races_that_year(year=year))
    print("Drivers")
    print(drivers_that_year(year=year))