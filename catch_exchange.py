import json
import requests
import os
import erro
from time import sleep

# os.system('pip3 install requests')

def catch_exchange():
    sec = 5
    tries = 0
    limit = 10
    while True:
        try:
            exchange_url = "https://api.exchangerate-api.com/v6/latest"
            req = requests.get(exchange_url)

            if req.status_code != 200:
                raise erro.RequestError(str(req.status_code))

            return req.json()
        except erro.RequestError as ex:
            print(ex.message)
            try:
                tries = tries + 1
                if tries >= limit:
                    raise erro.TimeRequestError(tries)
                print("New try in {} seconds\n".format(sec * (2 ** (tries-1))))
                sleep(sec * (2 ** tries))
            except erro.TimeRequestError as ex:
                print(ex.message)
                print("Try again in a few hours or check the url!\n")
                exit(0)
        except BaseException as ex:
            print(erro.writeError("UnknownError", "Request Exchange API - catch_exchange", "", ex))
            exit(0)


def read_data():
    try:
        arq = 'data.json'
        f = open(arq)
    except FileNotFoundError as ex:
        print(erro.writeError("FileNotFoundError", "Read Data - catch_exchange", f"Read {arq}", "File not found"))
        exit(0);
    except BaseException as ex:
        print(erro.writeError("UnknownError", "Request Exchange API - catch_exchange", "", ex))
        exit(0)
        
    try:
        data = json.load(f)
    except json.decoder.JSONDecodeError as ex:
        print(erro.writeError("JSONDecodeError", "Read Data - catch_exchange", "Convert json data to dict", f"Not json. File: {arq}"))
        exit(0);
    except BaseException as ex:
        print(erro.writeError("UnknownError", "Request Exchange API - catch_exchange", "", ex))
        exit(0)
    
    f.close()
    
    return data

def verify_if_it_s_same_countries(old_ones, new_ones):
    try:
        if old_ones != new_ones:
            raise erro.NotSameCountries(f"{old_ones}", f"{new_ones}")
        return True
    except erro.NotSameCountries as ex:
        print(ex.message)
        exit(0)
    except BaseException as ex:
        print(erro.writeError("UnknownError", "Request Exchange API - catch_exchange", "", ex))
        exit(0)

def updated():
    data = read_data()
    timeline = data["timeline"]
    
    data = catch_exchange()
    time_unix = data['time_last_update_unix']
    
    if time_unix in timeline:
        return False
    
    insert_data()
    return True

def insert_data():
    data = catch_exchange()
    time_unix, currency = data['time_last_update_unix'], data['rates']
    #print(datetime.utcfromtimestamp(time_unix).strftime('%Y-%m-%d %H:%M:%S'))
    
    old_data = read_data()
    
    new_data = old_data
    new_data["timeline"].append(time_unix)
    
    verify_if_it_s_same_countries(list(old_data["values"].keys()), list(currency.keys()))
    
    for country in currency:
        new_data["values"][country].append(round(currency['USD']/currency[country], 3))
    
    
    with open('data.json', 'w') as writer:
        json.dump(new_data, writer)

# Be carreful when using this function. It will erase all of your data!

def clean_data_json():
    data = catch_exchange()

    countries = list(data['rates'].keys())


    data = {
        "timeline": [],
        "values": {}
    }

    for c in countries:
        data["values"][c] = []

    with open('data.json', 'w') as writer:
        json.dump(data, writer)
        
    return data

def dell_last_data():
    data = read_data()

    data["timeline"].pop()
    for i in data["values"]:
        data["values"][i].pop()
    
    with open('data.json', 'w') as writer:
        json.dump(data, writer)

    return data

if __name__ == "__main__":
    #catch_exchange()
    read_data()