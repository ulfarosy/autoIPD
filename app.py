from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time, random

USERNAME = '2416100007' # insert your integra username here
PASSWORD = 'Makanmakan16' # insert your integra password here
SCORE_RANGE = (4,4) # (A, B) between A and B, inclusive

def choose(driver):
    for a in range(1,11):
        random_number = random.randint(SCORE_RANGE[0], SCORE_RANGE[1])
        driver.find_element_by_id('MK{}{}'.format(a, random_number)).click()
    driver.find_element_by_id('txtKomentar').send_keys('Sudah bagus')
    driver.find_element_by_id('chkPermanent').click()
    driver.find_element_by_xpath('//input[@value="SIMPAN"]').click()

def dosen(driver):
    driver.find_element_by_xpath('//*[text()="Isi Kuesioner"]').click()
    for a in range(1,11):
        random_number = random.randint(SCORE_RANGE[0], SCORE_RANGE[1])
        driver.find_element_by_id('DO{}{}'.format(a, random_number)).click()
    driver.find_element_by_id('txtKomentar').send_keys('Sudah bagus')
    driver.find_element_by_id('chkPermanent').click()
    driver.find_element_by_xpath('//input[@value="SIMPAN"]').click()
    driver.find_element_by_xpath('//*[text()="<< Kembali ke Kuesioner Mata Kuliah"]').click()

driver = webdriver.Chrome('chromedriver.exe')
driver.get('http://integra.its.ac.id')
userid_area = driver.find_element_by_id('userid')
password_area = driver.find_element_by_id('password')
button = driver.find_element_by_tag_name('button')
userid_area.send_keys(USERNAME)
password_area.send_keys(PASSWORD)
button.send_keys(Keys.ENTER)
driver.find_element_by_xpath('//*[@title="Masuk ke SI Akademik  "]').click()
driver.get('http://akademik.its.ac.id/ipd_kuesionermk.php')
dropdown = driver.find_element_by_id('mk_kuesioner')
dropdown_item = [a for a in dropdown.find_elements_by_tag_name('option')]
pilihan = len(dropdown_item)
for index in range(pilihan):
    dropdown = driver.find_element_by_id('mk_kuesioner')
    dropdown_item = [a for a in dropdown.find_elements_by_tag_name('option')]
    dropdown_item[index].click()
    try:
        choose(driver)
    except:
        pass
    try:
        dosen(driver)
    except:
        pass
    time.sleep(3)

# driver.close()
