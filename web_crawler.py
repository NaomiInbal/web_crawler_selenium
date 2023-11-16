from selenium import webdriver
from selenium.webdriver.common.by import By
import os
login_page_url = os.getcwd() +'/login.html'

# Initialize Chrome driver
driver = webdriver.Chrome()

try:
    # Open the login page
    driver.get(login_page_url)

    # Find username and password fields
    username_field = driver.find_element(By.ID,'username')
    password_field = driver.find_element(By.ID,'password')
    submit_btn = driver.find_element(By.TAG_NAME,'button')
    # Enter credentials
    username_field.send_keys('example')
    password_field.send_keys('password')
    # Submit form
    submit_btn.click()
    print('abc')

    main_page_element = driver.find_element(By.XPATH, '//div[@class="menu-wrap"]')

    # Find the "Pages" link and click it to open the dropdown
    pages_link = driver.find_element(By.XPATH, '//a[text()="Pages"]')
    print(pages_link)
    pages_link.click()

    # Find the "Download csv" link within the dropdown using its href attribute
    download_csv_link = driver.find_element(By.XPATH, '//ul[@class="drop-menu"]//a[contains(@href, "test.csv")]')
    download_csv_link.click()
    input("Press Enter to close the browser window")


finally:
    # Close the browser window
    driver.quit()
    print('Finished!')
