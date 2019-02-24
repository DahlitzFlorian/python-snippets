from selenium import webdriver


website_link = "https://github.com/login"
username = ""
password = ""

element_for_username = "login"
element_for_password = "password"
element_for_submit = "commit"

browser = webdriver.Firefox()
browser.get(website_link)

try:
    username_field = browser.find_element_by_name(element_for_username)
    username_field.send_keys(username)
    password_field = browser.find_element_by_name(element_for_password)
    password_field.send_keys(password)
    signInButton = browser.find_element_by_name(element_for_submit)
    signInButton.click()

    # to quit the browser uncomment the following lines
    # time.sleep(3)
    # browser.quit()
    # time.sleep(1)
    # browserExe = "Safari"
    # os.system("pkill "+browserExe)
except Exception as e:
    print(e)

# to quit the browser uncomment the following lines
# browser.quit()
# browserExe = "Safari"
# os.system("pkill "+browserExe)
