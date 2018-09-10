# -*- coding: utf-8 -*-
from __future__ import print_function
"""
Created on Wed Apr 18 19:13:11 2018

@author: Wenqi Zheng
"""


import requests
import sys
# This client code can run on Python 2.x or 3.x.  Your imports can be
# simpler if you only need one of those.
try:
    # For Python 3.0 and later
    from urllib.parse import quote
    from urllib.error import HTTPError
except ImportError:
    # Fall back to Python 2's urllib2 and urllib
    from urllib import quote
    from urllib2 import HTTPError


# Yelp Fusion no longer uses OAuth as of December 7, 2017.
# You no longer need to provide Client ID to fetch Data
# It now uses private keys to authenticate requests (API Key)
# You can find it on
# https://www.yelp.com/developers/v3/manage_app
API_KEY='F76fZ80dYsfXG7kde1gU9-EvbDoCVQBdv-CmBNVFrb4gXTpAcrJ5oNnk7UrtYC7r1zlaXMjBIbpB01uW44WI5PwYGl7SDaU92U2Qm3-92PFD3Pd1N77wGMfwpjrBWnYx'
# API constants, you shouldn't have to change these.
API_HOST = 'https://api.yelp.com'
SEARCH_PATH = '/v3/businesses/search'
BUSINESS_PATH = '/v3/businesses/'  # Business ID will come after slash.


# Defaults for our simple example.

SEARCH_LIMIT = 50


def request(host, path, api_key, url_params=None):
    """Given your API_KEY, send a GET request to the API.
    Args:
        host (str): The domain host of the API.
        path (str): The path of the API after the domain.
        API_KEY (str): Your API Key.
        url_params (dict): An optional set of query parameters in the request.
    Returns:
        dict: The JSON response from the request.
    Raises:
        HTTPError: An error occurs from the HTTP request.
    """
    url_params = url_params or {}
    url = '{0}{1}'.format(host, quote(path.encode('utf8')))
    headers = {
        'Authorization': 'Bearer %s' % api_key,
    }

    print(u'Querying {0} ...'.format(url))

    response = requests.request('GET', url, headers=headers, params=url_params)
    return response.json()
    
def get_business(business_id):
    """Query the Business API by a business ID.
    Args:
        business_id (str): The ID of the business to query.
    Returns:
        dict: The JSON response from the request.
    """
    api_key=API_KEY
    business_path = BUSINESS_PATH + business_id

    return request(API_HOST, business_path, api_key)
#def get_reviews(api_key, business_id):
    
def search(api_key,inputVal):
    """Query the Search API by a search term and location.
    Args:
        term (str): The search term passed to the API.
        location (str): The search location passed to the API.
    Returns:
        dict: The JSON response from the request.
    """

    url_params = {
        'term': inputVal.term.replace(' ', '+'),
        'location': inputVal.location.replace(' ', '+'),
        'price': inputVal.price.replace(' ', '+'),
        'offset':inputVal.offset,
        'limit': SEARCH_LIMIT
    }
    return request(API_HOST, SEARCH_PATH, api_key, url_params=url_params)



def query_api(inputVal):
    """Queries the API by the input values from the user.
    Args:
        term (str): The search term to query.
        location (str): The location of the business to query.
    """
    term=inputVal.term
    location=inputVal.location
    price=inputVal.price
    priceTag=['any','$','$$','$$$','$$$$','$$$$$']
    response = search(API_KEY, inputVal)
    if(price!=''):
        price=int(price)
    else:
        price=0
    if 'error' in response:
        print(u'No businesses for {0} in {1} of price level {3} found.'.format(term, location,priceTag[price]))
    else:
        print('{0} businesses for {1} in {2} of price level {3}'.format(response['total'],term, location,priceTag[price]))
    return response

def searchInputVal(input_values):
    try:
        response=query_api(input_values)
        return response
    except HTTPError as error:
        sys.exit(
            'Encountered HTTP error {0} on {1}:\n {2}\nAbort program.'.format(
                error.code,
                error.url,
                error.read(),
            )
        )

def searchReviews(business_id):
    """Query the Business API by a business ID.
    Args:
        business_id (str): The ID of the business to query.
    Returns:
        dict: The JSON response from the request.
    """
    api_key=API_KEY
    business_path = BUSINESS_PATH + business_id+'/reviews'
    return request(API_HOST, business_path, api_key)

