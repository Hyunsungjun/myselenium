from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get("https://google.com")
#여기까진 거의 고정이겠군
##
search_bar = browser.find_element_by_class_name("gLFyf")
search_bar.send_keys("hello!")
search_bar.send_keys(Keys.ENTER)

search_results = browser.find_elements_by_class_name("g")

for search_result in search_results:
    title = search_result.find_element_by_tag_name("h3")
    if title:
        print(title.text)