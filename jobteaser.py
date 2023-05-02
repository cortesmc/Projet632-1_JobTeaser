from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from time import sleep
import csv

class Job_Teaser:

    def __init__(self):
        PATH = "C:\Program Files (x86)\chromedrive.exe"
        options = webdriver.ChromeOptions() 
        options.add_argument("--auto-open-devtools-for-tabs")
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)
        self.driver = webdriver.Chrome(options=options,executable_path=PATH)
        self.driver.get("https://connect.jobteaser.com/services#sign-in-form")
        
    def get_list(self):  
        pass
    
    def login(self,user,pw):
        input_user = self.driver.find_element(By.ID,("email"))
        input_password = self.driver.find_element(By.ID,("passwordInput"))
        # Sending input text to search field
        input_user.send_keys(user)
        input_password.send_keys(pw)
        # Pressing enter to search input text
        input_user.send_keys(Keys.ENTER)
        sleep(3)
        
        open_btn = self.driver.find_element(By.XPATH,('/html/body/main/div[2]/div/div[2]/a'))
        open_btn.click()
        
        link = self.driver.find_element(By.XPATH,('/html/body/div[1]/header/div/nav/div/ul/li[1]/ul/li[1]/a')).get_attribute('href')
        self.driver.get(link)
          
        open_btn = self.driver.find_element(By.XPATH,('/html/body/div[1]/div/div/div/div/div[1]/div[1]/a'))
        open_btn.click()
        
    def get_link_offre(self):
        sleep(3)
        link = self.driver.find_element(By.XPATH,('/html/body/div[1]/div/header/div/nav/div/div/div/ul/li[4]/a')).get_attribute("href")
        self.driver.get(link)
        
    def get_list_offres(self):
        sleep(3)
        action = ActionChains(self.driver)   
        section_offres = self.driver.find_element(By.XPATH,('/html/body/div[1]/div/div/div[1]/div[3]/div/section'))
        i = 2
        list_offres = []
        while True:
            try:
                ligne = []
                ligne.append(section_offres.find_element(By.XPATH,f"./div[{i}]/a/article/div[2]/h3").text)
                ligne.append(section_offres.find_element(By.XPATH,f"./div[{i}]/a/article/div[2]/div/p").text)
                ligne.append(section_offres.find_element(By.XPATH,f"./div[{i}]/a/article/div[2]/ul/li[1]").text)
                ligne.append(section_offres.find_element(By.XPATH,f"./div[{i}]/a/article/div[2]/ul/li[2]").text)
                ligne.append(section_offres.find_element(By.XPATH,(f'./div[{i}]/a')).get_attribute('href'))
                list_offres.append(ligne)
                i+=1
                action.key_down(Keys.PAGE_DOWN).perform()
            except:
                 break
            else:
                pass
        return list_offres
        
        '''for i in range(2,50) :
            print(section_offres.find_element(By.XPATH,f"./div[{i}]").text + '\n')
            print(section_offres.find_element(By.XPATH,(f'./div[{i}]/a')).get_attribute('href'))
            print('\n --------------------\n')
            action.key_down(Keys.PAGE_DOWN).perform()'''
              
    def get_csv(self,list_info):
        headers = ["Title","Enterprise","Duration","Location","Link"]
        f = open('offres_stage.csv', 'w',newline='',encoding="utf-8")
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(list_info)
        f.close()

if __name__== "__main__":
    bot=Job_Teaser()
    #A completer:
    bot.login("email utilisateur", "password utilisateur")

    bot.get_link_offre()
    list_info = bot.get_list_offres()
    bot.get_csv(list_info)