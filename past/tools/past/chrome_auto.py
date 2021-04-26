from splinter import Browser

url = "https://steamdb.info/calculator/76561198031813016/?cc=cn"

executable_path = {'executable_path':"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"}
browser = Browser('chrome', **executable_path)

browser.visit("baidu.com")
