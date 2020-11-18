from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from os import path


driver_path = '/home/mrraven/PycharmProjects/TM-skills-study/chromedriver'
google_search_xpath = '//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input'
goole_first_search_result_xpas = '//*[@id="rso"]/div[1]/div/div[1]/a'
goole_url = 'https://www.google.by/'
twitter_followers_xpass = '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/div[1]/div[2]/div[4]/div[2]/a'

class Find_twitter:
    def __init__(
            self,
            *,
            driver_path_: str,
            person_name: str,
            google_url: str,
            goole_result_xpas:
            str, twitter_xpass: str
    ):
        self.driver = webdriver.Chrome(executable_path=driver_path_)
        self._google_url = google_url
        self.person_name = person_name
        self.goole_result_xpas = goole_result_xpas
        self.twitter_xpass = twitter_xpass
        self._find_person_twitter()
        self._find_person_twitter()
        self._write_subscribers_to_file()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.driver:
            self.driver.close()

    def _find_person_twitter(self):
        self.driver.get(self._google_url)
        goole_input = self.driver.find_element_by_xpath(google_search_xpath)
        if goole_input:
            goole_input.send_keys(f'twitter {self.person_name}')
            goole_input.send_keys(Keys.ENTER)
        self.driver.find_element_by_xpath(self.goole_result_xpas).send_keys(Keys.ENTER)

    def _write_subscribers_to_file(self):
        number_of_subscribers = self.driver.find_element_by_xpath(self.twitter_xpass).get_attribute("title")
        if path.isfile('log.txt'):
            with open('log.txt', 'a') as log_file:
                log_file.write(number_of_subscribers)
        else:
            with open('log.txt', 'w') as log_file:
                log_file.write(number_of_subscribers)







if __name__ == '__main__':
    with Find_twitter(
            driver_path_=driver_path,
            person_name='Солодуха',
            google_url=goole_url,
            twitter_xpass=twitter_followers_xpass,
            goole_result_xpas=goole_first_search_result_xpas
    ):
        pass

