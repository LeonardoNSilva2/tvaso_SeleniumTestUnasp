from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()))

#SITE PARA AUTOMATIZAÇÃO
driver.get('https://google.com.br')

XPATH_Input = '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input' #CAMINHO DO INPUT DE PESQUISA

#REALIZANDO UMA PESQUISA
driver.find_element_by_xpath(XPATH_Input).send_keys("Unasp")

XPATH_Pesquisa = '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[3]/center/input[1]' #CAMINHO DO BOTÃO DE PESQUISA

driver.find_element_by_xpath(XPATH_Pesquisa).submit()

XPATH_SiteUnasp = '//*[@id="rso"]/div[1]/div/div/div/div/div/div/div[1]/a/h3'

driver.find_element_by_xpath(XPATH_SiteUnasp).click()

time.sleep(10)

XPATH_VerCursos = '//*[@id="slider-135-slide-284-layer-24"]/rs-layer-wrap[4]/rs-loop-wrap/rs-mask-wrap'

driver.find_element_by_xpath(XPATH_VerCursos).click()

time.sleep(5)

XPATH_CursoDeAnalise = '//*[@id="listaDeCursosAncora"]/div/div/div[2]/a[1]'

driver.find_element_by_xpath(XPATH_CursoDeAnalise).click()

time.sleep(5)

XPATH_InscrevaJa = '/html/body/div[3]/div[2]/div[2]/div/div[2]/div/div/a[1]'

driver.find_element_by_xpath(XPATH_InscrevaJa).click()

time.sleep(10)