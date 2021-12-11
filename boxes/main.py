import requests
import json
import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from seleniumwire import webdriver
import asyncio
import aiohttp
from config import *
    

headers = {}

def salePage():
    url = 'https://www.binance.com/ru/nft/goods/sale/14571476255560?isBlindBox=1&isOpen=false'
    driver.get(url)
    time.sleep(5)

    input_sum = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/main/div/div/div[5]/div[2]/div/div[1]/input')
    input_sum.click() 
    input_sum.clear()
    input_sum.send_keys(5)

    time.sleep(5)
    driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/main/div/div/div[8]/button[2]').click()

def clickConfirm(headers):
    if check_exists_by_xpath('/html/body/div[4]/div/div/div[7]/button[2]'):
        confirm = driver.find_element_by_xpath('/html/body/div[4]/div/div/div[7]/button[2]')
    elif check_exists_by_xpath('/html/body/div[5]/div/div/div[7]/button[2]'):
        confirm = driver.find_element_by_xpath('/html/body/div[5]/div/div/div[7]/button[2]')
    elif check_exists_by_xpath('/html/body/div[6]/div/div/div[7]/button[2]'):
        confirm = driver.find_element_by_xpath('/html/body/div[6]/div/div/div[7]/button[2]')
    else:
        confirm = driver.find_element_by_xpath('/html/body/div[7]/div/div/div[7]/button[2]')
    ActionChains(driver).move_to_element(confirm).click().perform()
    print("Нажали confirm")

    time.sleep(3)

    for request in driver.requests:
        if str(request.url) == 'https://www.binance.com/bapi/nft/v1/private/nft/nft-trade/product-onsale':
            cookies = request.headers['cookie']
            csrftoken = request.headers['csrftoken']
            deviceinfo='eyJzY3JlZW5fcmVzb2x1dGlvbiI6Ijg1OCwxNTI1IiwiYXZhaWxhYmxlX3NjcmVlbl9yZXNvbHV0aW9uIjoiODEzLDE1MjUiLCJzeXN0ZW1fdmVyc2lvbiI6IldpbmRvd3MgNyIsImJyYW5kX21vZGVsIjoidW5rbm93biIsInN5c3RlbV9sYW5nIjoiZW4tVVMiLCJ0aW1lem9uZSI6IkdNVCs2IiwidGltZXpvbmVPZmZzZXQiOi0zNjAsInVzZXJfYWdlbnQiOiJNb3ppbGxhLzUuMCAoV2luZG93cyBOVCA2LjE7IFdpbjY0OyB4NjQ7IHJ2OjkzLjApIEdlY2tvLzIwMTAwMTAxIEZpcmVmb3gvOTMuMCIsImxpc3RfcGx1Z2luIjoiIiwiY2FudmFzX2NvZGUiOiIyOWI5YmU4MyIsIndlYmdsX3ZlbmRvciI6Ikdvb2dsZSBJbmMuIiwid2ViZ2xfcmVuZGVyZXIiOiJBTkdMRSAoSW50ZWwoUikgSEQgR3JhcGhpY3MgRGlyZWN0M0QxMSB2c181XzAgcHNfNV8wKSIsImF1ZGlvIjoiMzUuNzM4MzI5NTkzMDkyMiIsInBsYXRmb3JtIjoiV2luMzIiLCJ3ZWJfdGltZXpvbmUiOiJBc2lhL0FsbWF0eSIsImRldmljZV9uYW1lIjoiRmlyZWZveCBWOTMuMCAoV2luZG93cykiLCJmaW5nZXJwcmludCI6Ijg3YmY0OTA2ZDU3NDc4ZTE0NjAwMzQwYmY3MWUyYTUzIiwiZGV2aWNlX2lkIjoiIiwicmVsYXRlZF9kZXZpY2VfaWRzIjoiMTYyOTEzODQ2NTA4NHBCVTJIS2JOeWhjRWRKRkpHMGksMTYyOTk4Mjk5NzgwMnBPQWVDMGRmcldqUUZxV2NZTmEsMTYyOTk4NTIzMTY3MXlndGlyOFhBOWZWWW93TWFRRDcifQ=='
            useragent='Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0'

            xNftCheckbotSitekey = request.headers['x-nft-checkbot-sitekey']
            xNftCheckbotToken = request.headers['x-nft-checkbot-token']
            xTraceId = request.headers['x-trace-id']
            xUiRequestTrace = request.headers['x-ui-request-trace']

            headers = {
                'Host':'www.binance.com',
                'Accept':'*/*',
                'Accept-Language':'en-US,en;q=0.5',
                'Accept-Encoding':'gzip, deflate, br',
                'clienttype':'web',
                'x-nft-checkbot-token':xNftCheckbotToken,
                'x-nft-checkbot-sitekey':xNftCheckbotSitekey,
                'x-trace-id':xTraceId,
                'x-ui-request-trace' : xUiRequestTrace,
                'content-type':'application/json',
                'cookie' : cookies,
                'csrftoken': csrftoken, 
                'device-info': deviceinfo,
                'user-agent': useragent
            }
    print(headers)
    return headers

def check_exists_by_xpath(path):
    try:
        driver.find_element_by_xpath(path)
    except NoSuchElementException:
        return False
    return True


results = []
url = 'https://www.binance.com/bapi/nft/v1/private/nft/mystery-box/purchase'


def get_tasks(session):
    tasks = []
    

    for i in range(0,requestsNumber):
        tasks.append(asyncio.create_task(session.post(url, data = json.dumps(js), ssl=False)))

    # tasks.extend([asyncio.create_task(session.post(url, data = json.dumps(js), ssl=False))] * 100)
    print(len(tasks))
    return tasks




async def get_symbols(headers):
    async with aiohttp.ClientSession(headers=headers) as session:
        tasks = get_tasks(session)
        print(time.time())
        responses = await asyncio.gather(*tasks)
        for response in responses:
            results.append(await response.text())


def startSsc(headers):
    asyncio.get_event_loop().run_until_complete(get_symbols(headers))






driver = webdriver.Chrome(executable_path=path)

driver.maximize_window()

driver.get("https://binance.com/ru/nft")


a = input('Залогинтесь и нажмите Enter: ')


salePage()

print('hi')


rqStart = 0
rqStop = 0
while True:
    ts = time.time()
    if saleTime>ts:
        print(f'{saleTime-ts} - осталось секунд')
    if saleTime-ts < 7.0:
        break
rqStart=time.time()

headers = clickConfirm({})

while True:
    ts = time.time()
    if saleTime>ts:
        print(f'{saleTime-ts} - осталось секунд')
    if saleTime<ts:
        startSsc(headers)
        break
        

# while True:
# bm32
#     ts = time.time()
#     saleTime = 1632227100-0.3
#     if saleTime>ts:  
#         print(f'{saleTime-ts} - осталось секунд')
#     else:
#         headers = clickConfirm({})
#         break

# print(headers)
# startSsc(headers)


rqStop = time.time()
for r in results:
    if len(r)>250:
        print('blocked')
    else:
        print(r)


print(f'{rqStart - rqStop}')
