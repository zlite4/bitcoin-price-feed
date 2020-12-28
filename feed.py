import requests
import time

print(""" 
    ___   ___   _____    ___    ___    ___   _  _     ___   ___   ___   ___  
   | _ ) |_ _| |_   _|  / __|  / _ \  |_ _| | \| |   | __| | __| | __| |   \ 
   | _ \  | |    | |   | (__  | (_) |  | |  | .` |   | _|  | _|  | _|  | |) |
   |___/ |___|   |_|    \___|  \___/  |___| |_|\_|   |_|   |___| |___| |___/

              Automaticaly displays BTC price over USD,EUR & GBP.

                             Created by XziimP 

                Donations: 3QQmYmPM23TdNb4BStzaSSPg3R8CCnsSLU
         """)

time.sleep(4)

def EUR():
    return "€" + str(json_data['bpi']['EUR']['rate_float'])

def USD():
    return "$" + str(json_data['bpi']['USD']['rate_float'])

def GBP():
    return "£" + str(json_data['bpi']['GBP']['rate_float'])

while True:
    localtime = time.localtime()
    result = time.strftime("%I:%M:%S %p", localtime)
    print(result, end="", flush=True)
    print("\r", end="", flush=True)
    print(f'                                 {result}')

    res = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    json_data = res.json()


    print(f"""                {EUR()} <----> {USD()} <----> {GBP()}      """)

    print(""" 
    ___   ___   _____    ___    ___    ___   _  _     ___   ___   ___   ___  
   | _ ) |_ _| |_   _|  / __|  / _ \  |_ _| | \| |   | __| | __| | __| |   \ 
   | _ \  | |    | |   | (__  | (_) |  | |  | .` |   | _|  | _|  | _|  | |) |
   |___/ |___|   |_|    \___|  \___/  |___| |_|\_|   |_|   |___| |___| |___/
 

                
         """)

    time.sleep(10)



    
               
       


