from selenium import webdriver

chrome_browser = webdriver.Chrome('./chromedriver')

#print(chrome_browser)

chrome_browser.maximize_window()
chrome_browser.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')

assert 'Selenium Easy Demo' in chrome_browser.title
show_messge_button = chrome_browser.find_element_by_class_name('btn-default')
print(show_messge_button.get_attribute('innerHTML'))

assert 'Show Message' in chrome_browser.page_source

user_message = chrome_browser.find_element_by_id('user-message')
#user_button2 = chrome_browser.find_element_by_css_selector('')
user_message.clear()
user_message.send_keys("I am Extra Cool")


show_messge_button.click()
output_message = chrome_browser.find_element_by_id('display')

assert 'I am Extra Cool' in output_message

chrome_browser.close()      #closes window
chrome_browser.close()

chrome_browser.quit()     #closes entire chrome driver