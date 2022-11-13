import json
from fake_headers import Headers
import requests

# Design Imports
from utils.design import prefix

# Commandline Imports
from utils.commandline import update_title


proxies_working = []
proxies_dead = []


def country_code(ip: str):
    try:
        return requests.get(f'https://ipapi.co/{ip}/json', timeout=1).json()['country_code']
    except Exception:
        return '/'


def github_version():
    return json.loads(requests.get('https://raw.githubusercontent.com/marl0nx/EliteScraper/main/config/settings.json').text)["version"]


# ToDo: Add support for scraping from any website.
def extract_proxies(url: str):
    try:
        proxies = []
        r = requests.get(url.replace('\n', ''), timeout=5, verify=True)
        lines = r.text.splitlines()
        for _ in lines:
            if not _ in proxies:
                proxies.append(_)
        return proxies
    except Exception:
        return []
        pass


def parse_anonymity(proxy: str, ipaddr: str, timeout: int, print_dead: bool):
    try:
        r = requests.get('http://api.ipify.org', proxies={'http': proxy, 'https': proxy}, timeout=timeout)
        if ipaddr in r:
            return 'Transparent'

        privacy_headers = [
            'VIA',
            'X-FORWARDED-FOR',
            'X-FORWARDED',
            'FORWARDED-FOR',
            'FORWARDED-FOR-IP',
            'FORWARDED',
            'CLIENT-IP',
            'PROXY-CONNECTION'
        ]

        if any([header in r for header in privacy_headers]):
            return 'Anonymous'

        return 'Elite'
    except Exception:
        proxies_dead.append(proxy)
        update_title(
            f'EliteScraper v{str(github_version())} | github.com/marl0nx/EliteScraper ~ ALIVE: {str(len(proxies_working))} | DEAD: {str(len(proxies_dead))}')
        if print_dead is True:
            print(prefix.DEAD + proxy)


def original_ip():
    return requests.get('http://api.ipify.org').text


def check_proxy(proxy: str, ipaddr: str, timeout: int, host: str, path: str, print_dead: bool):
    timeout = round(timeout / 1000)
    try:
        header = Headers(
            browser="chrome",
            os="win",
            headers=True
        )
        first_check = parse_anonymity(proxy, ipaddr, timeout, print_dead)
        if not 'Elite' in first_check:
            proxies_dead.append(proxy)
            update_title(
                f'EliteScraper v{str(github_version())} | github.com/marl0nx/EliteScraper ~ ALIVE: {str(len(proxies_working))} | DEAD: {str(len(proxies_dead))}')
            if print_dead is True:
                print(prefix.DEAD + proxy)
        else:
            r = requests.get(host, proxies={'http': proxy, 'https': proxy}, headers=header.generate(), timeout=timeout)
            if r.status_code == 200 or r.status_code == 201:
                if not ':' in proxy:
                    proxies_dead.append(proxy)
                    update_title(
                        f'EliteScraper v{str(github_version())} | github.com/marl0nx/EliteScraper ~ ALIVE: {str(len(proxies_working))} | DEAD: {str(len(proxies_dead))}')
                    if print_dead is True:
                        print(prefix.DEAD + proxy)
                else:
                    r2 = parse_anonymity(proxy, ipaddr, timeout, print_dead)
                    if not 'Elite' in r2:
                        proxies_dead.append(proxy)
                        update_title(
                            f'EliteScraper v{str(github_version())} | github.com/marl0nx/EliteScraper ~ ALIVE: {str(len(proxies_working))} | DEAD: {str(len(proxies_dead))}')
                        if print_dead is True:
                            print(prefix.DEAD + proxy)
                    else:
                        if proxy in proxies_working:
                            pass
                        else:
                            print(prefix.ALIVE + proxy)
                            f = open(path, 'a+')
                            f.write(proxy + '\n')
                            f.close()
                            proxies_working.append(proxy)
                            update_title(
                                f'EliteScraper v{str(github_version())} | github.com/marl0nx/EliteScraper ~ ALIVE: {str(len(proxies_working))} | DEAD: {str(len(proxies_dead))}')
            else:
                if print_dead is True:
                    print(prefix.DEAD + proxy)
    except Exception:
        pass
