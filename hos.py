import requests
import json

# def suggest_hospitals(latitude, longitude, radius):
#     api_key = "AIzaSyDLtlMd6N1SararhW3zXcFrdnDEHbKyoGM"
#     endpoint = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?"
#     location = f"{latitude},{longitude}"
#     query = "hospital"
#     request = f"{endpoint}location={location}&radius={radius}&type={query}&key={api_key}"
#     print(request)
#     response = requests.get(request)
#     response_json = json.loads(response.text)

#     hospitals = []
#     for place in response_json["results"]:
#         name = place["name"]
#         latitude = place["geometry"]["location"]["lat"]
#         longitude = place["geometry"]["location"]["lng"]
#         hospitals.append((name, latitude, longitude))
# latitude = 37.7749
# longitude = -122.4194
# radius = 5000
# hospitals = suggest_hospitals(latitude, longitude, radius)
# print("Nearest Hospitals:")
# for hospital in hospitals:
#     print(f"- {hospital[0]} ({hospital[1]}, {hospital[2]})")
# import requests
# from bs4 import BeautifulSoup
# def suggest_hospitals(latitude, longitude, radius):
#     endpoint = "https://www.google.com/maps/dir/"
#     location = f"{latitude},{longitude}"
#     query = "/search/hospital"
#     url = f"{endpoint}{location}{query}"
#     print(url)
#     response = requests.get(url)
#     soup = BeautifulSoup(response.text, "html.parser")
#     print(soup)
#     hospitals = []
#     l=soup.find_all("div", class_="section-result-content-container")
#     print(l)
#     for place in soup.find_all("div", class_="section-result-content-container"):
#         print(place)
#         name = place.find("h3", class_="section-result-title").text
#         address = place.find("span", class_="section-result-location").text
#         hospitals.append((name, address))

#     return hospitals

# if __name__ == "__main__":
#     latitude = 17.782550
#     longitude = 83.376600
#     radius = 5000
#     hospitals = suggest_hospitals(latitude, longitude, radius)
#     print("Nearest Hospitals:")
#     for hospital in hospitals:
#         print(f"- {hospital[0]} ({hospital[1]})")
# from selenium.webdriver import Chrome
# from selenium.webdriver.chrome.options import Options as ChromeOptions
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from bs4 import BeautifulSoup
# from selenium.webdriver.common.action_chains import ActionChains
# import time
# from flask import Flask, render_template, request
# import requests
# options = ChromeOptions()
# options.add_argument('--headless')
# driver = Chrome()
# def get_doctors(city, pincode):
#     t1 = time.perf_counter()
#     driver.get('https://www.google.com/search?q=hosiptals+near+me&rlz=1C1VDKB_enIN1046IN1046&sxsrf=AJOqlzUYzWYrn5TJThWTbK6qk8FDaJmoNg%3A1677676171081&ei=i07_Y5PHBLrH3LUPp-SvwAg&ved=0ahUKEwjTuObh5rr9AhW6I7cAHSfyC4gQ4dUDCA8&uact=5&oq=hosiptals+near+me&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQAzINCAAQgAQQsQMQyQMQCjIHCAAQgAQQCjIHCAAQgAQQCjIHCAAQgAQQCjIHCAAQgAQQCjIHCAAQgAQQCjIHCAAQgAQQCjIHCAAQgAQQCjIHCAAQgAQQCjIHCAAQgAQQCjoHCCMQ6gIQJzoHCC4Q6gIQJzoMCC4Q6gIQtAIQQxgBOgwIABDqAhC0AhBDGAE6DQgAEI8BEOoCELQCGAI6BAgjECc6CwguEMcBEK8BEJECOgUIABCRAjoLCAAQgAQQsQMQgwE6EQguEIMBEMcBELEDENEDEIAEOgUILhCABDoFCAAQgAQ6BAgAEEM6BwguELEDEEM6EwgAEIAEEBQQhwIQsQMQgwEQyQM6EAguEIAEEBQQhwIQsQMQgwE6CAgAEIAEELEDOgsILhCABBDHARDRAzoICC4QsQMQgwE6DQgAEIAEELEDEEYQ-QE6CggAELEDEMkDEEM6CggAEIAEELEDEAo6BwguEIAEEAo6DQguEIAEELEDEIMBEApKBAhBGABQ9ApYvlFg91NoAnABeACAAZ4CiAHPGZIBBjAuMTMuNZgBAKABAaABArABFMABAdoBBggBEAEYAdoBBggCEAEYCg&sclient=gws-wiz-serp')
#     while True:
#         try:
#             time.sleep(2)
#             driver.find_element_by_xpath("/html/body/section[16]/section/span").click()
#             break
#         except Exception:
#             pass
#     driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
#     time.sleep(5)
#     items = {}
#     page_source = driver.page_source
#     soup = BeautifulSoup(page_source, 'lxml')
#     for count in range(100):
#         card = driver.find_element_by_xpath('//*[@id="bcard{}"]/div[1]'.format(count))
#         names_selector = soup.select_one('#bcard{} > div.col-md-12.col-xs-12.colsp > section > div.col-sm-5.col-xs-8.store-details.sp-detail.paddingR0 > h2 > span > a > span'.format(count))
#         if names_selector == None:
#             name = 'Not Avaialble'
#         else:
#             name = names_selector.text
#         image_selector = card.find_element_by_xpath('//*[@id="newphoto{}"]/img'.format(count))
#         if image_selector == None:
#             image = 'Not Avaialble'
#         else:
#             image = image_selector.get_attribute("src")
#         address_selector = soup.select_one('#morehvr_add_cont{} > span.cont_fl_addr'.format(count))
#         if address_selector == None:
#             address = 'Not Avaialble'
#         else:
#             address = address_selector.text
        
#         ratings_selector = soup.select_one('#bcard{} > div.col-md-12.col-xs-12.colsp > section > div.col-sm-5.col-xs-8.store-details.sp-detail.paddingR0 > p.newrtings > a > span.green-box'.format(count))
#         if ratings_selector == None:
#             rating = 'Not Avaialble'
#         else:
#             rating = ratings_selector.text

#         items[name] = {"name":  name, "image": image, "rating": rating, "address": address}
#     driver.quit()
#     print("Time taken : ",time.perf_counter() - t1)
#     return items
# get_doctors('visakhapatnam',530045)
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time

# def get_hospitals(location):
#     # Set up Chrome options to run headless
#     options = Options()
#     options.headless = True
    
#     # Initialize Chrome driver
#     driver = webdriver.Chrome()
#     driver.maximize_window()
    
#     # Load Google Maps page
#     driver.get("https://www.google.com/maps")
    
#     # Wait for page to load
#     WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "q")))
    
#     # Enter location query and submit
#     search_box = driver.find_element_by_name("q")
#     search_box.send_keys(location + " hospitals")
#     search_box.submit()
    
#     # Wait for search results to load
#     WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "section-result-title")))
    
#     # Scroll down to load more search results
#     SCROLL_PAUSE_TIME = 2
#     last_height = driver.execute_script("return document.documentElement.scrollHeight")
#     while True:
#         driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
#         time.sleep(SCROLL_PAUSE_TIME)
#         new_height = driver.execute_script("return document.documentElement.scrollHeight")
#         if new_height == last_height:
#             break
#         last_height = new_height
    
#     # Parse search results
#     page_source = driver.page_source
#     soup = BeautifulSoup(page_source, 'html.parser')
#     hospitals = []
#     for result in soup.find_all("div", class_="section-result-text-content"):
#         name = result.find("h3", class_="section-result-title").text
#         address = result.find("span", class_="section-result-location").text
#         rating = result.find("span", class_="cards-rating-score")
#         if rating is not None:
#             rating = rating.text
#         else:
#             rating = "Not available"
#         hospitals.append({"name": name, "address": address, "rating": rating})
        
#     # Close Chrome driver
#     driver.quit()
    
#     return hospitals
# get_hospitals('Visakhapatnam')
from flask import Flask, request
def get_city():
    r = requests.get('https://api.ipdata.co?api-key=test').json()
    print(r)
    ip_address = request.remote_addr
    print(ip_address)
    url = f'http://ip-api.com/json/{ip_address}' # using ip-api.com API
    response = requests.get(url).json()
    city = response['city']
    print(city)
get_city()