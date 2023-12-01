# Здесь парсится сайт и собирает данные в json

import requests
import json

br = 0
count_last_coef = 0
list_of_cof = []
list_all_users_count = []
data = []
checker = 0

while(True):
    
    r = requests.get("https://lucky-jet-history.gamedev-atech.cc/public/history/api/history/replay") #Ссылку на api нужно периодически обновлять
    
    replay = r.json()

    last_coef = replay['current_coefficients']
    dop_proverka = replay['next_state_time']
    
    if (dop_proverka != None):

        if(type(last_coef) == float):

            list_of_cof.append(last_coef)
           
            for i in list_of_cof:
                if len(list_of_cof) >= 2 and list_of_cof[-1] == list_of_cof[-2]:
                    list_of_cof.pop()
                    checker += 1

            if checker == 0:
                with open ("fullcofs.json", "r") as json_file_r:
                    cofsjson = json.load(json_file_r)

                a = list_of_cof[-1]
                cofsjson['cofs'].append(a)

                with open("fullcofs.json", 'w') as json_file:
                    json.dump(cofsjson, json_file, indent=2)

                print (list_of_cof, type(list_of_cof))

        count_last_coef = 0
        
    if (br == last_coef): 

        count_last_coef+=1

    checker = 0
    br = last_coef