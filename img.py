from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import dryscrape
from lxml import html


drscrp = dryscrape.Session(base_url = 'http://google.com')
drscrp.set_attribute('auto_load_images', False)
pathtochr = '/Users/vvaysse/PycharmProjects/arminer/chromedriver'
wb = webdriver.Chrome(pathtochr)
wb.get('https://www.google.fr/')
lemot = 'recherche'
wb.find_element_by_xpath("//input[@id='lst-ib']").send_keys(lemot) # cheche le mot
wb.find_element_by_xpath("//input[@value='Recherche Google']").click()
WebDriverWait(wb, 40).until(EC.presence_of_element_located((By.XPATH, "//a[contains(.,'Images')]"))) # attend chargement de la page
#affiche les images
wb.find_element_by_xpath("//a[contains(.,'Images')]").click()
imginp = wb.find_elements_by_xpath("//a[contains(@href,'imgres')]")
allpreimg = [i.get_attribute('href') for i in imginp]  #trouve l'url de la page ou se cache le vrai lien de l'img
allimg = []
# pour trouver la vrai url vers l'img on process tout avec request +fast
for i in allpreimg:
    drscrp.visit(i)
    pi = drscrp.at_xpath('//img[@class="irc_mi"]')
    print(pi)