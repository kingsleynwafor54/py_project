import threading
import queue
import requests


# q=queue.Queue()
# valid_proxies=[]
# with open("proxy_list.txt","r") as f:
#     proxies=f.read().split("\n")
#     for p in proxies:
#         q.put(p)


# def check_proxies():
#     global q
#     while not q.empty():
#         proxy=q.get()
#         try:
#             res=requests.get("http://ipinfo.io/json",
#             proxies={"http":proxy,
#             "https":proxy})
#         except:
#             continue
#         if res.status_code==200:
#             print(proxy)

# for t in range(10):
#     threading.Thread(target=check_proxies).start()

with open("valid_proxies.txt",'r') as f:
    proxies=f.read().split("\n")

site_to_check=["https://www.ups.com/lasso/login?returnto=https%3a//www.ups.com/webqvm/%3floc%3den_US&reasonCode=-2&appid=CVA"]

counter =0
for site  in site_to_check:
    try:
        print(f'Using the proxy:{proxies[counter]}')
        res=requests.get(site,proxies={"http":proxies[counter],
        "htpps":proxies[counter]})
        print(res.status_code)
        print(res.text)
    except:
        print("Failed")
    finally:
        counter+=1