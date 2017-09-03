from http import server

import requests_oauthlib

import config

sandbox_url = 'https://etwssandbox.etrade.com'
base_url = 'https://etws.etrade.com'


class Authorization:
    def __init__(self):
        self.oauth_session = requests_oauthlib.OAuth1Session(config.oauth_consumer_key, config.consumer_secret,
                                                             callback_uri='oob')
        self.oauth_url = base_url + "/oauth"
        print(self.get_authorization_url())
        self.run_authorization_server()

    def get_request_token(self):
        request_token_path = '/request_token'
        url = self.oauth_url + request_token_path
        return self.oauth_session.fetch_request_token(url)

    def get_authorization_url(self):
        request_token = self.get_request_token()
        url_format = 'https://us.etrade.com/e/t/etws/authorize?key={oauth_consumer_key}&token={oauth_token}'
        url = url_format.format(oauth_consumer_key=config.oauth_consumer_key, oauth_token=request_token['oauth_token'])
        return self.oauth_session.authorization_url(url)

    def get_access_token(self, verification_code):
        access_token_path = '/access_token'
        url = self.oauth_url + access_token_path
        return self.oauth_session.fetch_access_token(url, verifier=verification_code)

    def run_authorization_server(self):
        host_name = 'localhost'
        host_port = 80
        with server.HTTPServer((host_name, host_port), AuthenticationCallbackHandler) as httpd:
            httpd.serve_forever()


class AuthenticationCallbackHandler(server.BaseHTTPRequestHandler):
    def do_GET(self):
        print('do_GET()')
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b'<html><title>Authorized</title><body><h1 align="center">Authorized</h1></body></html>')


def get_quote(symbol, auth):
    path = 'market/sandbox/rest/quote/'
    url = base_url + path + symbol + '.json'
    response = auth.oauth_session.get(url)
    return response


def main():
    auth = Authorization()


if __name__ == '__main__':
    main()
