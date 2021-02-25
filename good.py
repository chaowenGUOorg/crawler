import selenium.webdriver, time, PIL, io, pytesseract, argparse
parser = argparse.ArgumentParser() 
parser.add_argument('password')
options = selenium.webdriver.ChromeOptions()
options.headless = True
options.add_argument('--disable-popup-blocking')
options.add_argument('--incognito')
options.add_argument('--no-first-run')
driver = selenium.webdriver.Chrome(options=options)
driver.get('https://www.alexamaster.net/sec/login.php')
driver.execute_script('globalThis.scrollTo(0,1000)')
time.sleep(10)
driver.find_element_by_css_selector('input[placeholder="Your Email ..."]').send_keys('chaowen.guo1@gmail.com')
driver.find_element_by_css_selector('input[placeholder="Your Password ..."]').send_keys(parser.parse_args().password)
driver.find_element_by_css_selector('input[value="Login Now"]').click()
time.sleep(60)
ocr = driver.find_element_by_css_selector('img[src="image.php"]')
good = PIL.Image.open(io.BytesIO(driver.get_screenshot_as_png()))
ocr = good.crop((ocr.location['x'], ocr.location['y'], ocr.location['x'] + ocr.size['width'], ocr.location['y'] + ocr.size['height'])).convert('L').point(lambda _:0 if _ > 160 else 255)
driver.find_element_by_css_selector('input[placeholder="Type above number here ..."]').send_keys(pytesseract.image_to_string(ocr))
driver.find_element_by_css_selector('input[value="Validate Account"]').click()
time.sleep(60)
driver.save_screenshot('good.png')
driver.close()
