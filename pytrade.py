import requests
import requests_oauthlib

import config

sandbox_url = 'https://etwssandbox.etrade.com'
base_url = 'https://etws.etrade.com/'

def get_request_token():
    path = 'oauth/request_token'
    url = base_url + path
    oauth = requests_oauthlib.OAuth1Session(config.oauth_consumer_key, config.consumer_secret, callback_uri='oob')
    return oauth.fetch_request_token(url)

def get_quote(symbol):
    path = 'market/sandbox/rest/quote/'
    url = sandbox_url + path + symbol + '.json'
    response = requests.get(url)
    return response

def main():
    print(get_request_token())
    print(get_quote('SQ'))

if __name__ == '__main__':
    main()