from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
import re
import urllib.request



def getImageUrl(browser):
    # Again waiting some time

    try:
        imageElement = browser.find_element(By.CLASS_NAME, "sc-artwork-40x")
        imageElementSyle = imageElement.get_attribute("style")
        


    except Exception as e:
        print(f"No image could be found: {e}")

    regex = r"\".*\""
    try:
        imageUrl = re.search(regex, imageElementSyle).group(0).replace('"', '')

    except Exception as e:
        print(f"Error parsing the imageurl: {e}")
    
    return imageUrl

def getSongTitle(browser):
    try:
        parentTitleElement = browser.find_element(By.CLASS_NAME, "soundTitle__title")
        songTitle = parentTitleElement.find_element(By.CSS_SELECTOR, "span").text
        return songTitle
    
    except Exception as e:
        print(e)

def getArtist(browser):
    try:
        parentArtistElement = browser.find_element(By.CLASS_NAME, "soundTitle__username")
        artistName = parentArtistElement.find_element(By.CSS_SELECTOR, "a").text
        return artistName
    except Exception as e:
        print(e)


def downloadImage(imageUrl, songTitle, artistName):
    fileName = f"{artistName} - {songTitle}"
    for x in fileName:
        if x == "/" or x == "\\" or x == ".":
            x = ""
    fileName = "./output/" + fileName
    fileName += ".jpg"

    import os
    if not os.path.exists("./output"):
        os.makedirs("./output")

    urllib.request.urlretrieve(imageUrl, fileName)
    print(f"\nSaved in the directory output as {fileName}\n")


def run(url):
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), chrome_options=options)

    print("\n Opening the website...")
    browser.get(url)

    time.sleep(4)

    try:
        browser.find_element(By.ID, "onetrust-accept-btn-handler").click()

    except Exception as e:
        print(f"No cookies to accept: {e}")

    print("\n Parsing the response...")
    imageUrl = getImageUrl(browser)
    songTitle = getSongTitle(browser)
    artistName = getArtist(browser)

    print("\n Saving the image...")
    downloadImage(imageUrl, songTitle, artistName)

    browser.close()


if __name__ == "__main__":
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    browser.get("PUT YOUR SONGPATH IN HERE")

    time.sleep(4)

    try:
        browser.find_element(By.ID, "onetrust-accept-btn-handler").click()

    except Exception as e:
        print(f"No cookies to accept: {e}")

    imageUrl = getImageUrl(browser)
    songTitle = getSongTitle(browser)
    artistName = getArtist(browser)

    downloadImage(imageUrl, songTitle, artistName)






#


