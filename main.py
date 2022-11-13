# Design Imports
import json
import random
import time
from concurrent.futures import ThreadPoolExecutor

# Design Imports
from utils.design import prefix
from utils.design import banner

# Commandline Imports
from utils.commandline import clear
from utils.commandline import slow_title

# API Imports
from utils.api import original_ip
from utils.api import github_version
from utils.api import check_proxy
from utils.api import extract_proxies


class EliteScraper:
    def __init__(self):
        self.ipaddr = original_ip()
        self.newest_version = github_version()
        self.version = json.loads(open('config/settings.json', 'r').read())["version"]
        self.show_dead_proxies = None
        self.threads = 0
        self.proxy_website_check = ''
        self.timeout = 0
        self.output_file = ''
        self.delete_old_proxies_in_file = None

        self.proxies_working = []
        self.loaded_proxies = []

    def checker(self):
        pass

    def main(self):
        try:
            clear()
            banner()
            if github_version() > self.version:
                slow_title(f'EliteScraper v{str(self.version)} | github.com/marl0nx/EliteScraper')
                print(
                    prefix.FAILED + f'A New Version Of EliteScraper Is Available On GitHub (v{str(github_version())})! Please Download The Newest Version To Continue!')
                input()
                exit()
            slow_title(f'EliteScraper v{str(github_version())} | github.com/marl0nx/EliteScraper')
            print(prefix.INFO + 'Loading Config Settings ..')
            config = json.loads(open('config/settings.json', 'r').read())
            self.show_dead_proxies = config["show_dead_proxies"]
            self.threads = config["threads"]
            self.proxy_website_check = config["proxy_website_check"]
            self.timeout = config["timeout"]
            self.output_file = config["output_path"]
            self.delete_old_proxies_in_file = config["delete_old_proxies_in_file"]
            time.sleep(1.49)
            print()
            print(prefix.INFO + 'Loaded Config Successfully!')
            time.sleep(1)
            if self.delete_old_proxies_in_file:
                print()
                print(prefix.INFO + 'Deleting Old Proxies in Proxy File ..')
                print()
                f = open(self.output_file, 'w')
                f.write('')
                f.close()
                time.sleep(1)
                print(prefix.INFO + 'Deleted Old Proxies in Proxy File Successfully!')
            time.sleep(1)
            print()
            print(prefix.INFO + 'Scraping Proxies From The World Wide Web ..')
            time.sleep(2)
            print()
            for _ in open('config/urls.txt', 'r').readlines():
                print(prefix.INFO_TWO + 'Scraping ' + _)
                for i in extract_proxies(_):
                    if not ':' in i:
                        pass
                    elif i in self.loaded_proxies:
                        pass
                    else:
                        self.loaded_proxies.append(i)
            print()
            print(prefix.INFO + 'Scraped Proxies Successfully! Got ' + str(len(self.loaded_proxies)) + ' Proxies!')
            random.shuffle(self.loaded_proxies)
            time.sleep(1)
            print()
            print(prefix.INFO + f'Checking Proxies If Work for {self.proxy_website_check} ..')
            print()
            with ThreadPoolExecutor(max_workers=self.threads) as e:
                for _ in self.loaded_proxies:
                    e.submit(check_proxy, _, self.ipaddr, self.timeout, self.proxy_website_check, self.output_file,
                             self.show_dead_proxies)
            print()
            print(prefix.INFO + 'Checked Proxies Successfully!')
            input()
        except KeyboardInterrupt:
            pass


EliteScraper().main()
