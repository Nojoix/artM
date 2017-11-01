from selenium import webdriver
import selenium


pathtochr = '/Users/vvaysse/PycharmProjects/arminer/chromedriver'
wb = webdriver.Chrome(pathtochr)
wb.get('https://www.google.fr/')
lemot = 'recherche'
wb.find_element_by_xpath("//input[@id='lst-ib']").send_keys(lemot) # cheche le mot
wb.find_element_by_xpath("//input[@id='Recherche Google']").click()
WebDriverWait(wb, 40).until(EC.presence_of_element_located((By.XPATH, "//a[contains(.,'Images')]"))) # attend chargement de la page
#affiche les images
wb.find_element_by_xpath("//a[contains(.,'Images')]").click()
imginp = wb.find_elements_by_xpath("//a[contains(@href,'imgres')]")
allimg = [i.get_attribute('href') for i in imginp]
print(allimg)