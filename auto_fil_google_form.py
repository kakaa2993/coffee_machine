from selenium import webdriver
from time import sleep

CHROME_WEBDRIVER_PATH = "your webdriver path"
GOOGLE_FORM = "https://docs.google.com/forms/d/e/1FAIpQLSerfUOJUB7H6AZgyFiE5LimsC3e5KVsD99YAJom5PUI-NNz7A/viewform?usp=sf_link"


class AutoFill:
    def __init__(self):
        self.driver = webdriver.Chrome(CHROME_WEBDRIVER_PATH)

    def auto_fill_form(self, data_zip):
        self.driver.get(GOOGLE_FORM)
        address, prices, links = data_zip

        for index in range(len(address)):
            sleep(5)
            inputs = self.driver.find_elements(by="css selector", value="div >div > div > input")
            submit_button = self.driver.find_element(by="css selector", value="span.l4V7wb.Fxmcue")
            sleep(3)
            adders_input, price_input, link_input = inputs
            adders_input.click()
            adders_input.send_keys(address[index])
            price_input.click()
            price_input.send_keys(prices[index])
            link_input.click()
            link_input.send_keys(links[index])
            submit_button.click()
            sleep(2)
            another_response = self.driver.find_element(by="css selector", value=".c2gzEf a")
            another_response.click()
        self.driver.quit()