from bs4 import BeautifulSoup
from selenium import webdriver
import requests

def main():
    # sock = requests.request("GET", "http://211.233.22.224/")
    # sock = requests.get("http://211.233.22.224/")
    # parser = BeautifulSoup(sock.text, 'html.parser')

    driver = webdriver.PhantomJS()
    driver.get("http://211.233.22.224/")


    parser = BeautifulSoup(driver.page_source, features='html.parser')
    print(parser)

if __name__ == "__main__":
    main()