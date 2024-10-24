import requests
from bs4 import BeautifulSoup
import csv


date = input("Enter the date (MM/DD/YYYY): ")
page = requests.get(f"https://www.yallakora.com/match-center/?date={date}")


def main(page):

    src = page.content
    sope = BeautifulSoup(src, "lxml")
    print(sope)

main(page)
