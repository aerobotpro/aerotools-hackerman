import requests
from random import choice
from datetime import datetime

def err(inp):
    print(f'[{str(datetime.now())}] {inp}')

def ip_loca(ip):
    r = requests.get(
        "https://json.geoiplookup.io/{}".format(ip)
    )
    a = r.json()
    return a['city'] + " ," + a['country_name']

#Get proxies from list
def get_proxies(fname):
    go = True
    try:
        #as '[]' / aka "List"
        with open(fname) as f:
            x = f.readlines()    
    except Exception as e:
        x = None
        #err("No Proxy File Detected Or File Is Empty!")
        err(e)
        go = False
        proxies = None
    # GET A RANDOM PROXY    
    if go == True:
        prox = choice(list(x))
        proxies = {
            'http': f'socks5h://{prox}'.strip('\n'),
            'https': f'socks5h://{prox}'.strip('\n')
            }  
    return proxies 


def get_headers():
    useragents = [
    ('Mozilla/5.0 (X11; Linux x86_64) '
        'AppleWebKit/537.36 (KHTML, like Gecko) '
        'Chrome/57.0.2987.110 '
        'Safari/537.36'),  # chrome
    ('Mozilla/5.0 (X11; Linux x86_64) '
        'AppleWebKit/537.36 (KHTML, like Gecko) '
        'Chrome/61.0.3163.79 '
        'Safari/537.36'),  # chrome
    ('Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:55.0) '
        'Gecko/20100101 '
        'Firefox/55.0'),  # firefox
    ('Mozilla/5.0 (X11; Linux x86_64) '
        'AppleWebKit/537.36 (KHTML, like Gecko) '
        'Chrome/61.0.3163.91 '
        'Safari/537.36'),  # chrome
    ('Mozilla/5.0 (X11; Linux x86_64) '
        'AppleWebKit/537.36 (KHTML, like Gecko) '
        'Chrome/62.0.3202.89 '
        'Safari/537.36'),  # chrome
    ('Mozilla/5.0 (X11; Linux x86_64) '
        'AppleWebKit/537.36 (KHTML, like Gecko) '
        'Chrome/63.0.3239.108 '
        'Safari/537.36'),  # chrome
    ]
    user_agent = choice(useragents)
    headers = {'User-Agent' : user_agent}
    return headers

#Essentially MAIN JOB
# Create a session and get proxies + useragent + Proxies
def scrape(address):
    session = requests.session()
    session.proxies = get_proxies('proxies.txt')
    print(str(session.proxies))
    #session.headers = get_headers()
    #print(str(session.headers))
    try:
        r = session.get(str(address))
        x = {
            'response': str(r.status_code),
            'text': r.text,
            'proxy_used': session.proxies['http'].split(':')[0],
            'proxy_location': ip_info(session.proxies['http'].split(':')[0])
        }
    except Exception as d:
        x = "Failed to reach {}, bad proxy? Try again mabye.".format(address)
        print(d)
        pass
    return x


err(str(scrape('http://3g2upl4pq6kufc4m.onion/')))



    



