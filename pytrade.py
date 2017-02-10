import requests
import requests_oauthlib

import config

sandbox_url = 'https://etwssandbox.etrade.com'
base_url = 'https://etws.etrade.com/'
oauth_session = requests_oauthlib.OAuth1Session(config.oauth_consumer_key, config.consumer_secret, callback_uri='oob')


def get_request_token():
    path = 'oauth/request_token'
    url = base_url + path
    return oauth_session.fetch_request_token(url)


def get_authorization_url(request_token):
    url_format = 'https://us.etrade.com/e/t/etws/authorize?key={oauth_consumer_key}&token={oauth_token}'
    url = url_format.format(oauth_consumer_key=config.oauth_consumer_key, oauth_token=request_token['oauth_token'])
    return oauth_session.authorization_url(url)


def get_quote(symbol):
    path = 'market/sandbox/rest/quote/'
    url = sandbox_url + path + symbol + '.json'
    response = requests.get(url)
    return response


def main():
    request_token = get_request_token()
    print(get_authorization_url(request_token))
    print(get_quote('SQ'))


if __name__ == '__main__':
    main()
