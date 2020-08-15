import requests
import bs4



def get_price_int(st):
    d = [str(x) for x in range(0,10)]
    p = ""
    for i in st:
        if(i=='.'):
            return int(p)
        if(i in d):
            p+=i
    return(int(p))

def get_price(classes,data):
    for i in classes:
        price = data.find(id=i)
        if(price!=None):
            return get_price_int(price.text)
    return get_price_int(price.text)

usr_ag = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"
headers = {'User-agent':usr_ag}



def price(url):
    classes = ["priceblock_ourprice",'priceblock_dealprice']
    req = requests.get(url, headers = headers)
    if not (req.status_code == requests.codes.ok):
        return "Invaid URL"
    data = bs4.BeautifulSoup(req.text,'html.parser')
    return get_price(classes, data)
