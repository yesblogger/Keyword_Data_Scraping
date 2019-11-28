from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
import time
import random


class dataFetcher:
    # setting up the driver object
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 60)

    def endSession(self):
        """[Close the connection with the browser]
        """
        self.driver.quit()

    def fetchData(self, keyword, file):
        try:
            # parsing the keyword into proper format
            keyword_f = '%20'.join(keyword.split(' '))
            # making the search query
            self.driver.get(
                f'https://app.neilpatel.com/en/ubersuggest/overview?keyword={keyword_f}&locId=2840&lang=en')
            # pausing the script for maximum 5 seconds
            time.sleep(random.randint(2, 5))
            # we will wait till volume element is loaded
            volume = self.wait.until(ec.presence_of_element_located(
                (By.XPATH, '//div[@class="css-1jd9o2h"]/div[1]/div[2]/span'))).get_attribute('textContent')
            competition = self.driver.find_element_by_xpath(
                '//div[@class="css-1jd9o2h"]/div[2]/div[2]/span').get_attribute('textContent')
            cpc = self.driver.find_element_by_xpath(
                '//div[@class="css-1jd9o2h"]/div[4]/div[2]/span').get_attribute('textContent')
            # convert the data into numbers
            volume, competition, cpc = self.convert(volume, competition, cpc)
            # writing the data to the file
            file.writerow({'Keyword': keyword, 'Volume': volume,
                           'Competion': competition, 'CPC': cpc})
            # pausing the script for maximum 4 seconds
            time.sleep(random.randint(2, 4))
        except Exception as error:
            print(error)
            self.driver.quit()

    @staticmethod
    def convert(volume, competition, cpc):
        """
        [converting key parameters into number]

        Arguments:
            volume {[string]} -- [keyword volume]
            competition {[string]} -- [organic competion score of a keyword]
            cpc {[string]} -- [cost per click of keyword]
        """
        # converting the parameters
        volume = int(''.join(i for i in volume if i != ','))
        competition = int(''.join(i for i in competition if i != ','))
        cpc = float(''.join(i for i in cpc if i != '$'))

        return (volume, competition, cpc)
