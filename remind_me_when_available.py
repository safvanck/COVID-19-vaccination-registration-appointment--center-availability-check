import requests
import time
import json
import os



district_code = 302 #malappuram
pincode = 676528
a_date = "30-04-2021"


def validate_res(dt):
    if (dt != '{"centers":[]}') and (dt != '{"message":"Too Many Requests"}'):
        if dt == "Unauthenticated access!":
            os.system(f'spd-say "trying again..."')
        else:
            dt_list = [_.get("name") for _ in json.loads(dt).get('centers')]
            os.system(f'spd-say "{dt_list}"')
            print(dt_list)
            return True
    return False




a= True
while a:
    x = requests.get(f'https://cdn-api.co-vin.in/api/v2/appointment/sessions/calendarByPin?pincode={pincode}&date={a_date}')
    data = (x.content).decode("utf-8")
    a = not validate_res(data)
    if a:
        x = requests.get(f'https://cdn-api.co-vin.in/api/v2/appointment/sessions/calendarByDistrict?district_id={district_code}&date={a_date}')
        data = (x.content).decode("utf-8")
        a = not validate_res(data)
    time.sleep(2)
