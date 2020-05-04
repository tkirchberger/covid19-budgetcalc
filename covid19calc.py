import math
import random
from datetime import datetime
import urllib.request
import requests
import time

def main():
    c = False
    b = False
    g = False

    # getting COVID-19 from GitHub repository
    r = requests.get('https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-states.csv')
    print("COVID-19 data was successfully loaded as a .csv. Starting calculator.")

    time.sleep(3)

    print("")
    print("=================================================================================")
    print("========================= COVID-19 BUDGETING CALCULATOR =========================")
    print("=================================================================================")
    print("                            Today's date: " + str(datetime.date(datetime.now())))
    print("")

    pos = input("Enter your budgeting position ([C] consumer, [B] business owner, [G] gov. personnel): ")
    if pos == 'C':
        c = True
    if pos == 'B':
        b = True
    if pos == 'G':
        g = True
    state = input("What state would you like to budget for? ")

main()
