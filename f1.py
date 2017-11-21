#!/usr/bin/env python3

"""
This little module downloads and parses information about formula 1 seasons,
tracks, drivers, etc.
"""

import pandas as pd
import sys
import os

from download import download, filename

pd.set_option('display.width', 2000)


def get_content(type, year):
    assert type in ["races", "drivers", "team"]
    _filename = filename(type, year)

    if os.path.isfile(_filename):
        content = open(_filename).read()
        print("Using local cache...")
    else:
        _, content = download(type, year)
        print("Using internet...")

    return content


def make_df(content, columns):
    return pd.read_html(content)[0][columns]


def races_that_year(year):
    columns = ['Date', 'Grand Prix', 'Car', 'Winner', 'Time', 'Laps']
    content = get_content("races", year)
    return make_df(content, columns)


def drivers_that_year(year):
    columns = ['Driver', 'Pts', 'Car', 'Nationality']
    content = get_content("drivers", year)
    return make_df(content, columns)


def teams_that_year(year):
    columns = ['Pos', 'Pts', 'Team']
    content = get_content("team", year)
    return make_df(content, columns)


if __name__ == "__main__":
    year = int(sys.argv[1])
    assert 1950 <= int(year) <= 2017
    print("Races")
    print(races_that_year(year=year))
    print("Drivers")
    print(drivers_that_year(year=year))
    print("Teams")
    print(teams_that_year(year=year))
