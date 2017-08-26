"""
Python utility functions for working with the SeeClickFix api v2 and data.

SeeClickFix data is licensed under a Creative Commons Attribution-Noncommercial-Share Alike 3.0 United States License.
Attribution should be to seeclickfix.com.

This code is licensed under the MIT License (c) 2017 by the Newport Data Project. email: hello@newportdataproject.org
"""

import urllib.request
import pandas as pd


def get_issue_page(url):
    # GET a page of a dataset and convert to pandas
    rawdata = urllib.request.urlopen(url).read()  # GET the data
    data = "[" + str(rawdata, 'utf-8') + "]"  # convert from bytestring to json array string
    df = pd.read_json(data, typ='frame', orient='columns', convert_dates=True)  # convert to pandas
    return df


def get_issues_by_place(place_url, max_pages=20):
    # Get all issues from the seeclickfix api within a specific place_url. max_pages is set to avoid huge huge datasets
    # Returns a pandas dataframe of pages.
    url = "http://seeclickfix.com/api/v2/issues?place_url=" + place_url  # define the initial api query
    dataset = get_issue_page(url)

    total_pages = dataset.metadata[0]['pagination']['pages']  # get total number of pages in the dataset
    if total_pages > max_pages:
        total_pages = max_pages  # enforce max page limit

    current_page = dataset.metadata[0]['pagination']['page']  # get current page
    next_url = dataset.metadata[0]['pagination']['next_page_url']  # get url for next page

    # iterate through pages
    while current_page < total_pages:
        url = next_url
        df = get_issue_page(url)
        current_page = df.metadata[0]['pagination']['page']
        next_url = df.metadata[0]['pagination']['next_page_url']
        dataset = pd.concat([dataset, df], ignore_index=True)  # concatenate

    # TODO unpack isues into a single dataframe
    # TODO flatten issue data and return that istead of all of it

    return dataset

# TODO get issues by other geography: http://dev.seeclickfix.com/#geography
