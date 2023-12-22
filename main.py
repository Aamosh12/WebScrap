import json
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from pymongo import MongoClient


class WebScraper:
    def __init__(self):
        self.file_name = 'bank.json'
        self.options = Options()
        self.options.add_argument("--headless")
        self.options.add_argument("window-size=1920,1080")
        self.driver = webdriver.Chrome(options=self.options)
        self.wait = WebDriverWait(self.driver, 10)
        self.client = MongoClient("mongodb+srv://aamoshmaharjan234:QOpFnRrwRCaJjzBd@cluster0.1cjd14y.mongodb.net/")  # Update with your MongoDB connection string
        self.db = self.client["webScrap"] # Update with your MongoDB database name

    def connect_to_mongo(self):
        # Connect to MongoDB and return the collection
        return self.db["bank_collection"] # You can change according to your collection name

    def insert_into_mongo(self, data):
        collection = self.connect_to_mongo()
        collection.insert_one(data)

    def navigate_to_page(self, url):
        self.driver.get(url)

    def get_bank_name(self):
        self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "card-title")))
        card = self.driver.find_element(By.CLASS_NAME, "card-title")
        bank = card.text
        return bank

    def select_options(self):
        select = Select(self.driver.find_element(By.ID, "exampleFormControlSelect1"))
        options = select.options
        return options

    def scrape_data(self, url):
        final_data = []
        self.navigate_to_page(url)
        bank_options = self.select_options()
        for index in range(1, len(bank_options)):
            bank_name = self.get_bank_name()
            data = {
                "bank": bank_name,
                "data": []
            }
            bank_data_single = self.bank_data()
            data["data"].extend(bank_data_single)
            final_data.append(data)
            self.insert_into_mongo(data)
            print(f'Extracted From {bank_name}')
            if index < len(bank_options) - 1:
                Bank_select = Select(self.driver.find_element(By.ID, "exampleFormControlSelect1"))
                Bank_select.select_by_index(index + 1)


    def bank_data(self):
        whole_data = []
        Status = True
        while Status:
            soup = BeautifulSoup(self.driver.page_source, 'html.parser')
            table = soup.find('table', attrs={'id': 'banklist-table'})
            table_body = table.find('tbody')
            for row in table_body.find_all('tr'):
                row_data = {}
                columns = row.find_all('td')
                row_data["code"] = columns[1].text
                row_data["address"] = columns[2].text
                row_data["district"] = columns[3].text
                row_data["branchName"] = columns[4].text
                row_data["date"] = columns[5].text

                whole_data.append(row_data)
            next_button = self.driver.find_element(By.ID, 'banklist-table_next')
            if 'disabled' in next_button.get_attribute('class'):
                Status = False
            self.driver.execute_script("arguments[0].scrollIntoView();", next_button)
            next_button.click()
        return whole_data


if __name__ == "__main__":
    scraper = WebScraper()
    url = 'https://www.nrb.org.np/bank-list/'
    scraper.scrape_data(url)
