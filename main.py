import selenium.webdriver, pynat
print(pynat.get_ip_info(include_internal=True))
options = selenium.webdriver.ChromeOptions()
options.headless = True
options.add_argument('--disable-popup-blocking')
options.add_argument('--incognito')
driver = selenium.webdriver.Chrome(chrome_options=options)
driver.get('https://www.alexamaster.net/Master/157701')
while True: pass
#driver.close()
