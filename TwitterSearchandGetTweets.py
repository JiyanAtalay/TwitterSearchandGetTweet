from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

# Search word
key = input("Key:")

driver = webdriver.Chrome()
driver.get("https://twitter.com/i/flow/login")

sleep(5)
# Login
user_name = driver.find_element(By.TAG_NAME, "input")
user_name.send_keys("") # Your Nick

sleep(2)

user_name_button = driver.find_elements(By.XPATH, "//div[@role='button']")
user_name_button[2].click()

sleep(4)

password = driver.find_element(By.TAG_NAME, "input")
password.send_keys("") # Pasword

sleep(2)

password_button = driver.find_elements(By.XPATH, "//div[@role='button']")
password_button[-1].click()
sleep(35)
# Search
driver.get("https://twitter.com/search?q="+key+"&src=typed_query")
sleep(35)
# Scroll down
lenOfPage = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
match=False
while(match==False):
    lastCount = lenOfPage
    sleep(3)
    lenOfPage = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
    if lastCount == lenOfPage:
        match=True
sleep(3)

tweets = driver.find_elements(By.XPATH,"//div[@data-testid='tweetText']")

# Get all tweet
sleep(3)
for i in tweets:
    print("*********************")
    print(i.text)

#driver.back() # Önceki sayfaya dönmemizi sağlar

driver.close()