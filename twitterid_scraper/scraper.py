import time
from time import sleep
from typing import List, Dict
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options

def handle_to_id(twitter_handles:List[str], sleep_seconds:int=3)->Dict:
    """Scrape https://tweeterid.com/ to convert twitter handles into twitter ids.
    Args:
        twitter_handles:
        sleep_seconds:
    Returns:

    """
    tic = time.time()
    url = "https://tweeterid.com/"
    options = Options()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    # driver = webdriver.Chrome()
    driver.implicitly_wait(3)
    driver.get(url)
    for twitter_handle in twitter_handles:
        # sleep(sleep_seconds)
        print(f'converting: {twitter_handle}')
        python_input = driver.find_element_by_id("twitter")
        python_button = driver.find_element_by_id("twitterButton")
        python_input.clear()
        python_input.send_keys(twitter_handle)
        python_button.click()
        # print(f'sleeping {sleep_seconds} seconds.')
        sleep(sleep_seconds)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    containers =  soup.find_all('div', {'class':"output"})
    p_elements = containers[0].find_all('p')
    output_tuples=[]
    for p_element in p_elements[1:]:
        output_tuples.append(tuple(p_element.text.split('=> ')))
    newspapers_dict = dict(output_tuples)
    toc=time.time()
    print(f'execution time: {toc-tic} seconds.')
    print(f'{len(newspapers_dict)} handles converted into ids.')
    return newspapers_dict