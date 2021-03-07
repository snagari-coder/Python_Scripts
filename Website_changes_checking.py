## Small script to monitor website changes.
## When the website find a particular string, you get a beep sound.
## If it does not find some text, it waits 60 seconds and downloads the webpage again.

# Import requests (to download the page)
import requests

# Import BeautifulSoup (to parse what we download)
from bs4 import BeautifulSoup

# Import Time (to add a delay between the times the scape runs)
import time
import winsound




# while this is true (it is true by default),
while True:
    # set the url as VentureBeat,
    url = "https://www.signupgenius.com/tabs/13577df01a0cfedc5ac5-vaccine3"
    url1 = "https://www.signupgenius.com/tabs/13577df01a0cfedc5ac5-vaccine2"
    # set the headers like we are a browser,
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1)  Chrome/39.0.2171.95'
    }
    # download the homepage
    response = requests.get(url, headers=headers)
    response1 = requests.get(url1, headers=headers)
    # parse the downloaded homepage and grab all text, then,
    #soup = BeautifulSoup(response.text, "lxml")
    soup = BeautifulSoup(response.text, "html.parser")
    soup1 = BeautifulSoup(response1.text, "html.parser")
    #print(soup)
    print("running")
    # if the number of times the given date occurs on the page is less than 1,
    if str(soup).find("03/06/2021") == -1 and str(soup1).find("03/06/2021") == -1:
        # wait 60 seconds,
        time.sleep(120)
        # continue with the script,
        continue

    # but if the given date occurs any other number of times,
    else:

        print("something changed")
        frequency = 2500  # Set Frequency To 2500 Hertz
        duration = 5000  # Set Duration To 1000 ms == 1 second
        winsound.Beep(frequency, duration)

        break
