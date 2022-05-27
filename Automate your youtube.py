from selenium import webdriver

# this the library of python which is used to import the required output


driver = webdriver.Chrome()
driver.get('https://youtube.com')
searchbox = driver.find_element_by_xpath('/html/body/ytd-app/div[1]/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div[1]/div[1]/input')
searchbox.send_keys('innovation begins channel')

searchButton=driver.find_element_by_xpath('/html/body/ytd-app/div[1]/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/button/yt-icon')
searchButton.click()
