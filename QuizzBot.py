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
        #self.driver = webdriver.Chrome()
        #self.driver.get("https://squiz.cc/")
        self.driver.get("https://squiz.cc/?token=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdWQiOiJodHRwczovL2lkZW50aXR5dG9vbGtpdC5nb29nbGVhcGlzLmNvbS9nb29nbGUuaWRlbnRpdHkuaWRlbnRpdHl0b29sa2l0LnYxLklkZW50aXR5VG9vbGtpdCIsImlhdCI6MTU5Mjc2NjQxNSwiZXhwIjoxNTkyNzcwMDE1LCJpc3MiOiJmaXJlYmFzZS1hZG1pbnNkay1xNmNxcUBzcXVpei1iZXRhLXByb2R1Y3Rpb24uaWFtLmdzZXJ2aWNlYWNjb3VudC5jb20iLCJzdWIiOiJmaXJlYmFzZS1hZG1pbnNkay1xNmNxcUBzcXVpei1iZXRhLXByb2R1Y3Rpb24uaWFtLmdzZXJ2aWNlYWNjb3VudC5jb20iLCJ1aWQiOiJkckR1Z0FyV2tOZzBzM0tWVUpHSTVkSXlSSkgyIiwiY2xhaW1zIjp7InR3aXRjaCI6eyJpZCI6IjU0NDQxNzMyOCIsIm5hbWUiOiJ4YXJpX2xlX2Zhc3QiLCJkaXNwbGF5TmFtZSI6InhhcmlfbGVfZmFzdCIsInR5cGUiOm51bGwsImJyb2FkY2FzdGVyVHlwZSI6bnVsbCwicHJvZmlsZUltYWdlVXJsIjoiaHR0cHM6Ly9zdGF0aWMtY2RuLmp0dm53Lm5ldC91c2VyLWRlZmF1bHQtcGljdHVyZXMtdXYvMTNlNWZhNzQtZGVmYS0xMWU5LTgwOWMtNzg0ZjQzODIyZTgwLXByb2ZpbGVfaW1hZ2UtMzAweDMwMC5wbmciLCJhY2Nlc3NUb2tlbiI6IjFhMWlycmJyYzBodmlwdW4zNjNieHd4YmszemlhaiIsInJlZnJlc2hUb2tlbiI6IjhrdTY4aXNxNXNvemNybGhueThzNHRmd2EyMjM4bnE4NmR1aXV0YjdrODJodHprbG9oIn19fQ.I_QPkRUGXVhfe51pXfglx_fOIz0K3a3qpKvEdU541WV4upXN6hbxT9GS-e7Iln7-tZ_Eg_0XRKLbtn99Q8rWclLPSePfj1QtZIgSxM-nPn-S8hkIKwNyrZyQum_V5ehQpRyMu7seXQnkpggqsjLoOM-ur7lBTdUdYFv692_iNx28WzAshdbeDX0hvL9aosjZDdn4MlR5udxyvTW7ujcQRpoqOxoXv7qbAxCsZupXBECRDqpBfO5EueM29TTcA1W50dId6lOAFGrCbn0e1eG_lnTR4uMDdDiP5DUl-9J54YfWXEEy1b91FyxI0ikViP9QJGkZgUBVh5JSD0R8Dx60yg")
        sleep(1)


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
