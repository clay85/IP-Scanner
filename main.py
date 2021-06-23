from colorama import Fore , init
init()
import os , time , requests , json
os.system("cls" or "clear")
clear = lambda: os.system('cls' or "clear")
def logo():
    print(Fore.RED+("||||||||||||     |||||||                 |||||||     |||||||     |||||||"))
    print(Fore.RED+("||||||||||||      |||||||               |||||||      |||||||     |||||||"))
    print(Fore.RED+("|||                |||||||             |||||||       |||||||     |||||||"))
    print(Fore.RED+("|||                 |||||||           |||||||        |||||||     |||||||"))
    print(Fore.RED+("||||||||||||         |||||||         |||||||         |||||||     |||||||"))
    print(Fore.RED+("||||||||||||          |||||||       |||||||          |||||||     |||||||"))
    print(Fore.RED+("|||                    |||||||     |||||||           |||||||     |||||||"))
    print(Fore.RED+("|||                     |||||||   |||||||            |||||||     |||||||||||||||||||"))
    print(Fore.RED+("||||||||||||             ||||||| |||||||             |||||||     |||||||||||||||||||"))
    print(Fore.RED+("||||||||||||              |||||||||||||              |||||||     |||||||||||||||||||"))
    print(Fore.WHITE+"MADE BY Arman.Security")





while True:
    clear()
    logo()
    time.sleep(1)
    print(Fore.MAGENTA+"IP ADDRESS CHOSEN!")
    print(Fore.GREEN+("1) GEO.IP LOOKUP"))
    print(Fore.GREEN+("2) REVERSE IP LOOKUP"))
    print(Fore.GREEN+("3) TCP PORT SCAN"))
    print(Fore.GREEN+("4) SUBNET LOOKUP"))
    print(Fore.GREEN+("5) ASN LOOKUP"))
    print(Fore.GREEN+("6) BANNER GRABBING (SEARCH)"))
    print(Fore.BLUE+("ENTER 'exit' TO END PROGRAM"))
    IP_ENTER=input(Fore.RED+("ENTER YOUR MOOD: "))

    if IP_ENTER == 'exit':
        clear()
        time.sleep(1)
        break


    elif IP_ENTER == '1': #GEO.IP LOOKUP
        clear()
        logo()
        time.sleep(1)
        print(Fore.MAGENTA+("GEO.IP LOOKUP CHOSEN!"))
        print(Fore.BLUE+("ENTER 'exit' TO BACK MENU"))
        print(Fore.CYAN+"EXAMPLE: 1.1.1.1")

        while True:
            
            GEO_url = input(Fore.RED+"ENTER TARGET IP: ").lower()
            try:
                
                if "exit" in GEO_url:
                    clear()
                    logo()
                    time.sleep(1)
                    break
                GEO_IP = requests.get("https://api.hackertarget.com/geoip/?q="+GEO_url).text
                if "API count exceeded - Increase Quota with Membership" in GEO_IP :
                    print(Fore.LIGHTGREEN_EX+("TIME OUT!"))
                    time.sleep(1)
                    break
                else:
                    print(Fore.GREEN+GEO_IP)
            except:
                pass


    elif IP_ENTER == '2': #REVERSE IP LOOKUP
        clear()
        logo()
        time.sleep(1)
        print(Fore.MAGENTA+("REVERSE IP LOOKUP CHOSEN!"))
        print(Fore.CYAN+"EXAMPLE: SITE.COM")
        while True:

            try:
                SITE = input(Fore.RED+"Enter TAGET SITE: ")

                if "exit" in SITE:
                    clear()
                    logo()
                    time.sleep(1)
                    break
                a = {"remoteAddress":SITE}

                http = requests.post("https://domains.yougetsignal.com/domains.php",data=a).text

                data = json.loads(http)
                site_list = []
                for i in data["domainArray"]:
                    print(Fore.GREEN+i[0])
                    site_list.append(i[0])
            except:
                pass


    elif IP_ENTER == '3': #TCP PORT SCAN
        clear()
        logo()
        time.sleep(1)
        print(Fore.MAGENTA+("TCP PORT SCAN CHOSEN!"))
        print(Fore.BLUE+("ENTER 'exit' TO BACK MENU"))
        print(Fore.CYAN+"EXAMPLE: 1.1.1.1")
        while True:
            TCP_url = input(Fore.RED+"ENTER TARGET IP: ").lower()
            try:
                
                if TCP_url == 'exit':
                    clear()
                    logo()
                    time.sleep(1)
                    break
                TCP_req = requests.get("https://api.hackertarget.com/nmap/?q="+TCP_url).text
                if "API count exceeded - Increase Quota with Membership" in TCP_req:
                    print(Fore.LIGHTGREEN_EX+("TIME OUT!"))
                    time.sleep(1)
                    break
                else:
                    print(Fore.GREEN+TCP_req)
            except:
                pass


    elif IP_ENTER == "4" : #SUBNET LOOKUP
        clear()
        logo()
        time.sleep(1)
        print(Fore.MAGENTA+("SUBNET LOOKUP CHOSEN!"))
        print(Fore.BLUE+("ENTER 'exit' TO BACK MENU"))
        print(Fore.CYAN+"EXAMPLE: 192.168.1.0/24")
        while True:
            
            
            try:
                SUBNET_LOOKUP_req = requests.get("https://api.hackertarget.com/subnetcalc/?q="+SUBNET_LOOKUP_url).text
                if SUBNET_LOOKUP_url == 'exit':
                    clear()
                    logo()
                    time.sleep(1)
                    break
                SUBNET_LOOKUP_url= input(Fore.RED+"ENTER TARGET IP: ").lower()
                if "API count exceeded - Increase Quota with Membership" in SUBNET_LOOKUP_req:
                    print(Fore.LIGHTGREEN_EX+("TIME OUT!"))
                    time.sleep(1)
                    break
                else:
                    print(Fore.GREEN+SUBNET_LOOKUP_req)
            except:
                pass


    elif IP_ENTER == "5" : #ASN LOOKUP
        clear()
        logo()
        time.sleep(1)
        print(Fore.MAGENTA+("ASN LOOKUP CHOSEN!"))
        print(Fore.BLUE+("ENTER 'exit' TO BACK MENU"))
        print(Fore.CYAN+"EXAMPLE: 1.1.1.1 OR AS15169")
        while True:
            
            ASN_LOOKUP_url= input(Fore.RED+"ENTER TARGET IP: ").lower()
            try:
                
                if ASN_LOOKUP_url == "exit":
                    clear()
                    logo()
                    time.sleep(1)
                    break
                ASN_LOOKUP_req = requests.get("https://api.hackertarget.com/aslookup/?q="+ASN_LOOKUP_url).text
                if "API count exceeded - Increase Quota with Membership" in ASN_LOOKUP_req:
                    print(Fore.LIGHTGREEN_EX+("TIME OUT!"))
                    time.sleep(1)
                    break
                else:
                    print(Fore.GREEN+ASN_LOOKUP_req)
            except:
                pass


    elif IP_ENTER == "6" : #BANNER GRABBING (SEARCH)
        clear()
        logo()
        time.sleep(1)
        print(Fore.MAGENTA+("BANNER GRABBING (SEARCH) CHOSEN!"))
        print(Fore.BLUE+("ENTER 'exit' TO BACK MENU"))
        print(Fore.CYAN+"EXAMPLE: 2.2.2.2/24")
        while True:
            
            
            try:
                BANNER_REQ = requests.get("https://api.hackertarget.com/bannerlookup/?q="+BANNER_URL).text
                if str(BANNER_URL) == 'exit':
                    clear()
                    logo()
                    time.sleep(1)
                    break
                BANNER_URL= input(Fore.RED+"ENTER TARGET IP: ").lower()
                if "API count exceeded - Increase Quota with Membership" in BANNER_REQ:
                    print(Fore.LIGHTGREEN_EX+("TIME OUT!"))
                    time.sleep(1)
                    break
                else:
                    print(Fore.GREEN+BANNER_REQ)
            except:
                pass