import time
from selenium import webdriver
import requests

url = input("URL: ")

driver = webdriver.Chrome("driver.exe")
driver.get(url)

count = 0

input()

for num in range(1, len(driver.window_handles)):
    browser.close()


yeet = driver.window_handles

while True:
    count += 1
    r = requests.get(url)
    print(str(count) + " : " + str(r.status_code))
    driver.refresh()
    # Change the "0.5" to how many seconds you want in between reloads
    time.sleep(0.5)
