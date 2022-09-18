from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import json

with open('./secret.json', 'r') as f:
  secret = json.load(f)


class App:
    def __init__(self, email= secret['username'], password= secret['password'], 
                 path='/home/omar/Downloads/chromedriver_linux64/chromedriver.exe'):
        #defining main variables
        self.email = email
        self.password = password
        self.path = path
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.main_url = "https://www.facebook.com"
        self.used_item_links = []

        #automation steps
        self.get_website()
        self.log_in()
        self.search_area()
        self.scrape_items_list()
        self.process_ads()
        self.driver.quit()
        
    def get_website(self):
        self.driver.get(self.main_url)
        self.driver.maximize_window() # For maximizing window
        self.driver.implicitly_wait(2) 

    def log_in(self):
        email_input = self.driver.find_element("id", "email")
        email_input.send_keys(self.email)
        sleep(0.5)
        password_input = self.driver.find_element("id", "pass")
        password_input.send_keys(self.password)
        sleep(0.5)
        login_button = self.driver.find_element("xpath", "//*[@type='submit']")
        login_button.click()
        sleep(3)

    def search_area(self):
        self.driver.get("https://www.facebook.com/marketplace/category/propertyrentals?exact=false&latitude=48.4438&longitude=-123.418&radius=12")
        sleep(2)
        zoomout_button = self.driver.find_element("xpath", "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div[2]/div/div/div[3]/div[1]/div[1]/div[3]/div/div/div/div[2]")
        self.driver.execute_script("arguments[0].click();", zoomout_button)
        sleep(2)
        self.driver.execute_script("arguments[0].click();", zoomout_button)

    def scrape_items_list(self): 
        sleep(2)
        loading_element = True
        while(loading_element):
            try:
                loading_element = self.driver.find_element(By.CLASS_NAME,'mfclru0v.ikduhi8d.trbvugp6.j94dm2s7.j32recxq.p5mefues.jkp44r48')
            except:
                break

            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            sleep(1)
        self.used_item_links = self.driver.find_elements(By.CLASS_NAME,'qi72231t.nu7423ey.n3hqoq4p.r86q59rh.b3qcqh3k.fq87ekyn.bdao358l.fsf7x5fv.rse6dlih.s5oniofx.m8h3af8h.l7ghb35v.kjdc1dyq.kmwttqpk.srn514ro.oxkhqvkx.rl78xhln.nch0832m.cr00lzj9.rn8ck1ys.s3jn8y49.icdlwmnq.jxuftiz4.l3ldwz01')
        sleep(10)

    def process_ads(self):
        extracted_links = []
        for element in self.used_item_links:
            extracted_links.append({"link":element.get_attribute('href')})
        print(extracted_links[0])
        links_to_json = {"links":extracted_links}

        with open('extracted_links.txt', 'w') as json_file:
            json.dump(links_to_json, json_file)

            
        


if __name__ == '__main__':
    app = App()
