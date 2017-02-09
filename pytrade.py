import requests

sandbox_url = 'https://etwssandbox.etrade.com'
base_url = 'https://etws.etrade.com/'

def get_quote(symbol):
    path = 'market/sandbox/rest/quote/'
    url = sandbox_url + path + symbol + '.json'
    response = requests.get(url)
    return response

def main():
    print(get_quote('SQ'))

if __name__ == '__main__':
    main()