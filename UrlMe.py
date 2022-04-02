try:    
    from platform import system    
except BaseException:
    print("Error no except method Trying to help ..")
    os.system("pip install requests,re ")
import sys,os,time

try:
	import re,requests
except BaseException:
	if Sys=='Linux': 
    		os.system("pip3 install requests,re")

	elif Sys=='Windows': 
    		os.system("pip3 install requests,re ")
	else: 
    		print("Please try to Install Requests and re Methode to Your python !")
Red = '\033[91m'
Green = '\033[92m'
White = '\033[97m'




#-----------------------------------------------------------------------------------------
def logo():
    
    print(r"""{}
    (\____/)
     (_oo_)
       (O)   Urls Maker Coded By (LQzouikri)  
     __||__    \)
  []/______\[] /
  / \______/ \/
 /    /__\
(\   /____\

    """.format(Green))
    
    
def Get_URLS(Url,path):
    requests.get("https://web.archive.org/cdx/search/cdx?url=")
    Get=path+"*."+Url+"%2F*&output=text&fl=original&collapse=urlkey&filter=statuscode%3A200"
    return(requests.get(Get).text)

def UrlBody(Url):      
    if Url.startswith("http://"):
        Url=Url.replace("http://","") 
    if Url.startswith("https://"):
        Url=Url.replace("https://","")
    if Url[-1] == "/":
        Url=Url.replace("/","")
    return Url

def Check_Endpoint(Url,Red,White,Green):
    json=re.search("(.*?).js",Url)
    php=re.search("(.*?).php",Url)
    svg=re.search("(.*?).svg",Url)
    if json:
        print ("{}JSON :\t{}".format(Red,Url))
    elif php:
        print ("{}PHP :\t{}".format(Green,Url))
    elif svg:
        print ("{}SVG :\t{}".format(White,Url))
def main():  

    Sys=system()
    
    if Sys=='Linux': 
        os.system("clear")
        logo()
    if Sys=='Windows': 
        os.system("cls")
        logo()
    path="https://web.archive.org/cdx/search/cdx?url="
    Url=input("{}URL:".format(White))
    print("[+] Verify Link...")
    Url=UrlBody(Url)
    time.sleep(3)
    if requests.get(("http://"+Url)).status_code == 200:
        print("[+] URL WORK...")
    else :
        print("[+] URL NOT WORK...")
    print(Get_URLS(Url,path)) 
    time.sleep(3)   
    print("[+] Saving Links... ")
    try:
        with open("Save.txt","w") as URLContent:
            URLContent.write(Get_URLS(Url,path))
        print("[+] Links Has Been Saved In Save.txt")
    except IOError:
        print("No File Has Been Saved!!")
            
            

    print("[+] Filtration Links ...")
    time.sleep(3)
    with open("Save.txt","r") as FileContent:
        lines = FileContent.readlines()
        for i in lines:
            Url=i.strip()
            Check_Endpoint(Url,Red,White,Green)

            



if __name__ == '__main__':main()
