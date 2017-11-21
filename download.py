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


def filename(prefix, year):
    return "%s/%d.html" % (prefix, year)


def url(what, year):
    return BASE_URL + "%d/%s.html" % (year, what)


def download(what, year):
    assert what in ["team", "races", "drivers"]
    response = requests.get(url(what, year))
    return filename(what, year), response.content


def store(filename, content):
    directory = os.path.dirname(os.path.realpath(filename))
    if not os.path.isdir(directory):
        os.makedirs(directory)

    with open(filename, 'w') as html_file:
        html_file.write(content)

    return filename


if __name__ == "__main__":
    for year in range(MIN_YEAR, MAX_YEAR + 1):
        print(store(*download("races", year)))
        print(store(*download("drivers", year)))
        print(store(*download("team", year)))
        time.sleep(0.5)
