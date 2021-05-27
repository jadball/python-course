from bs4 import os, BeautifulSoup

CHROMEDRIVER = "chromedriver-linux"
CHROMEDRIVER = "chromedriver-mac"

# must be able to locate chromedriver on the PATH
from selenium import webdriver


def getPuzzle():
    os.environ["PATH"] = "." + os.pathsep + os.environ["PATH"]

    # load Chrome
    driver = webdriver.Chrome(executable_path=CHROMEDRIVER)
    print(f"Chrome Driver Version: {driver.capabilities['chrome']['chromedriverVersion']}")
    site = "https://alzheimer.ca/en/on/Living-with-dementia/BrainBooster/Sudoku"
    site = "https://www.nytimes.com/puzzles/sudoku/easy"
    site = "https://www.nytimes.com/puzzles/sudoku/medium"
    site = "https://www.nytimes.com/puzzles/sudoku/hard"
    driver.get(site)

    driver.implicitly_wait(10)  # seconds
    span = driver.find_element_by_css_selector("#a_")
    span.click()

    gridSelector = "#pz-game-root > div.su-app > div > div.su-app__play > div > div > div"
    # click some buttons to get expert sudoku
    content = driver.find_element_by_css_selector(gridSelector)
    # extract cell by cell
    result = ""
    for n in range(1, 82):
        cellSelector = f'/html/body/div[1]/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div[{n}][@aria-label]'
        cell = driver.find_element_by_xpath(cellSelector)
        html = cell.get_attribute('innerHTML')
        try:
            soup = BeautifulSoup(html, 'html.parser')
            result += soup.svg['number']
        except:
            result += "-"

    # close chrome
    driver.quit()
    return result


if __name__ == "__main__":
    print(getPuzzle())
