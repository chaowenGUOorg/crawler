import selenium.webdriver, time, PIL, io, asyncio, aiohttp, pytesseract
async def f():
    async with aiohttp.ClientSession() as session:
        async with session.get('https://www.alexamaster.net/sec/image.php') as response:
            a = PIL.Image.open(io.BytesIO(await response.content.read()))
            a = a.convert("L")  # 处理灰度
            pixels = a.load()
            for x in range(a.width):
                for y in range(a.height):
                    if pixels[x, y] > 150: pixels[x, y] = 255
                else: pixels[x, y] = 0
            a.save('ocr.png')
            return pytesseract.image_to_string(a)   

options = selenium.webdriver.ChromeOptions()
options.headless = True
options.add_argument('--disable-popup-blocking')
options.add_argument('--incognito')
options.add_argument('--no-first-run')
driver = selenium.webdriver.Chrome(options=options)
driver.get('https://www.alexamaster.net/sec/login.php')
driver.execute_script('globalThis.scrollTo(0,1000)')
time.sleep(10)
driver.find_element_by_css_selector('[placeholder="Your Email ..."]').send_keys('chaowen.guo1@gmail.com')
driver.find_element_by_css_selector('[placeholder="Your Password ..."]').send_keys('HL798820y+')
driver.find_element_by_css_selector('[value="Login Now"]').click()
time.sleep(60)
driver.save_screenshot('good.png')
print(asyncio.run(f()))
driver.close()
