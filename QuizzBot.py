from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import requests
from time import sleep



class QuizzBot:
    def __init__(self):
        self.chrome_options = Options()
        self.chrome_options.add_argument('headless')
        self.chrome_options.add_argument(r'load-extension=C:\Users\quentin\AppData\Local\Google\Chrome\User Data\Default\Extensions\enaobbodnmbpecahhojidoiblhmnohef\2.2.3_0')
        self.driver = webdriver.Chrome(chrome_options = self.chrome_options, executable_path=r'C:\Users\quentin\Documents\Code\Python\Bot_Scrapeur_Quizz\chromedriver.exe')

    def connect_to_VPN(self):
        self.driver.get("chrome-extension://enaobbodnmbpecahhojidoiblhmnohef/popup.html")
        sleep(5)
        clickVPN = WebDriverWait(self.driver, 120).until(EC.presence_of_element_located((By.ID,"vpn-on")))
        sleep(2)
        clickVPN.click()
        sleep(10)
        
    def connct_to_SQUIZ(self):
        self.driver.get(
            "https://squiz.cc/"
            )
        sleep(2)

    def connect_to_twitch(self, id, pw):
        clickBTwitch = WebDriverWait(self.driver, 120).until(EC.presence_of_element_located((By.XPATH,"/html/body/div/div[3]/div[4]/div/div/div/main/div/div/div[1]/div[1]/div[1]/a")))
        clickBTwitch.click()
        sleep(1)

        writeUserNameTwitch = WebDriverWait(self.driver, 120).until(EC.presence_of_element_located((By.XPATH,"/html/body/div[1]/div/div[1]/div[3]/div/div/div/div[3]/form/div/div[1]/div/div[2]/input")))
        writeUserNameTwitch.send_keys(id)
        sleep(1)

        writePwTwitch = WebDriverWait(self.driver, 120).until(EC.presence_of_element_located((By.XPATH,"/html/body/div[1]/div/div[1]/div[3]/div/div/div/div[3]/form/div/div[2]/div/div[1]/div[2]/div[1]/input")))
        writePwTwitch.send_keys(pw)
        sleep(1)

        clickBTwitch = WebDriverWait(self.driver, 120).until(EC.presence_of_element_located((By.XPATH,"/html/body/div[1]/div/div[1]/div[3]/div/div/div/div[3]/form/div/div[3]/button")))
        clickBTwitch.click()

    def connect_to_initie(self):
        initie = WebDriverWait(self.driver, 120).until(EC.presence_of_element_located((By.XPATH,"/html/body/div/div[3]/div[4]/div/div/div/main/div/div/div[2]/div/div/div/button[1]/h3")))
        initie.click()

    def connect_to_expert(self):
        self.driver.find_element_by_xpath("/html/body/div/div[3]/div[4]/div/div/div/main/div/div/div[2]/div/div/div/button[3]")\
            .click()     

    def scrapping_questions(self):
        question = WebDriverWait(self.driver, 120).until(EC.presence_of_element_located((By.XPATH,'/html/body/div/div[3]/div[4]/div/div/div/main/div/div[2]/div[2]/div[1]/div/div[1]/div[2]/p')))
        return question.text

    def scrapping_answers(self):
        answers = WebDriverWait(self.driver, 120).until(EC.presence_of_element_located((By.XPATH,'/html/body/div/div[3]/div[4]/div/div/div/main/div/div[2]/div[2]/div[1]/div/div[2]/div[1]/div/div')))
        return answers.text

    def write_answer(self, answer):
        reply = WebDriverWait(self.driver, 120).until(EC.presence_of_element_located((By.XPATH,"/html/body/div/div[3]/div[4]/div/div/div/main/div/div[2]/div[2]/div[3]/div[3]/form/div/input")))
        reply.send_keys(answer)
        reply.send_keys(Keys.ENTER)
