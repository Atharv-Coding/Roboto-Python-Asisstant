def sendWhatsappMsg():
    import time
    from Final import speak
    from Final import takeCommand
    from selenium import webdriver
    driver = webdriver.Chrome(port=9515)
    driver.get('https://web.whatsapp.com')

    time.sleep(10)

    searchBox = driver.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/div/div[2]')
    searchBox.send_keys("Ulhas")

    time.sleep(5)

    messageBox = driver.find_element_by_xpath('//*[@id="pane-side"]/div[1]/div/div/div[3]/div')
    messageBox.click()

sendWhatsappMsg()
