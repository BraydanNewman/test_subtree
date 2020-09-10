import time
from selenium import webdriver
import requests

driver = webdriver.Chrome("driver.exe")


def main():
    url = input("URL: ")
    driver.get(url)
    count = 0
    input()
    tap_closer()

    while True:
        count += 1
        r = requests.get(url)
        print(str(count) + " : " + str(r.status_code))
        driver.switch_to.window(driver.window_handles[0])
        driver.refresh()
        # Change the "0.5" to how many seconds you want in between reloads
        time.sleep(0.5)
        tap_closer()


def tap_closer():
    check = True
    while check:
        if len(driver.window_handles) > 1:
            driver.switch_to.window(driver.window_handles[1])
            driver.close()
            check = False


if __name__ == "__main__":
    main()
