import selenium.webdriver, time
options = selenium.webdriver.ChromeOptions()
options.headless = True
options.add_argument('--single-process')
options.add_argument('--disable-popup-blocking')
options.add_argument('--incognito')
options.add_argument('--no-first-run')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--no-sandbox')
#options.add_argument('--window-size=1960,1080')
driver = selenium.webdriver.Chrome(options=options)
#driver.execute_script('globalThis.open("https://chrome.google.com/webstore/detail/ebesucher-addon/agchmcconfdfcenopioeilpgjngelefk")')
#for _ in driver.window_handles:
#    driver.switch_to.window(_)
#    if 'ebesucher' in driver.current_url: break
#driver.find_element_by_id('connect_button').click()
#driver.find_element_by_id('login_email').send_keys('c#driver.find_element_by_id('login_passwd').send_keys(parser.parse_args().password)
#driver.find_element_by_id('connexion').click()
#driver.find_element_by_id('menu_link_credit').click()
#driver.find_element_by_css_selector('a[onClick^="return visio("]').click()
driver.execute_script('globalThis.open("http://www.crunchingbaseteam.com/view.php?user=chaowenguo")')
driver.get('https://www.alexamaster.net/Master/157701')
while True:
    print(driver.title)
    while driver.title == 'Surfing...': 
        time.sleep(60)
        print(driver.title, len(driver.window_handles))
    driver.refresh()
#driver.save_screenshot('ha.png')
#driver.quit()
