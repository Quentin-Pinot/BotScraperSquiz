from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import requests
from time import sleep


class QuizzBot:
    def __init__(self):
        self.op = webdriver.ChromeOptions()
        self.op.add_argument('headless')
        self.driver = webdriver.Chrome(options=self.op)

        self.driver.get("https://squiz.cc/")
        sleep(2)


    def connect_to_twitch(self, id, pw):
        self.driver.find_element_by_xpath("/html/body/div/div[3]/div[4]/div/div/div/main/div/div/div[1]/div[1]/div[1]/a")\
            .click()
        sleep(1)
        self.driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[3]/div/div/div/div[3]/form/div/div[1]/div/div[2]/input")\
            .send_keys(id)
        sleep(2)
        self.driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[3]/div/div/div/div[3]/form/div/div[2]/div/div[1]/div[2]/div[1]/input")\
            .send_keys(pw)
        sleep(1)
        self.driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[3]/div/div/div/div[3]/form/div/div[3]/button')\
            .click()
        sleep(2)

    def connect_to_initie(self):
        initie = WebDriverWait(self.driver, 60).until(EC.presence_of_element_located((By.XPATH,"/html/body/div/div[3]/div[4]/div/div/div/main/div/div/div[2]/div/div/div/button[1]")))
        initie.click()
        sleep(2)

    def connect_to_expert(self):
        self.driver.find_element_by_xpath("/html/body/div/div[3]/div[4]/div/div/div/main/div/div/div[2]/div/div/div/button[3]")\
            .click()
        sleep(2)     

    def scrapping_questions(self):
        question = WebDriverWait(self.driver, 60).until(EC.presence_of_element_located((By.XPATH,'/html/body/div/div[3]/div[4]/div/div/div/main/div/div[2]/div[2]/div[1]/div/div[1]/div[2]/p')))
        return question.text

    def scrapping_answers(self):
        answers = WebDriverWait(self.driver, 60).until(EC.presence_of_element_located((By.XPATH,'/html/body/div/div[3]/div[4]/div/div/div/main/div/div[2]/div[2]/div[1]/div/div[2]/div[1]/div/div')))
        return answers.text

    def write_answer(self, answer):
        reply = WebDriverWait(self.driver, 60).until(EC.presence_of_element_located((By.XPATH,"/html/body/div/div[3]/div[4]/div/div/div/main/div/div[2]/div[2]/div[3]/div[3]/form/div/input")))
        reply.send_keys(answer)
        reply.send_keys(Keys.ENTER)
        