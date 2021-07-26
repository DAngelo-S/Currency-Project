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
                raise erro.RequestError("catch_exchange", "catch_exchange", str(req.status_code))

            return req.json()
        except erro.RequestError as ex:
            print(ex.message)
            try:
                tries = tries + 1
                if tries >= limit:
                    raise erro.TimeRequestError("catch_exchange", "catch_exchange", tries)
                print("New try in {} seconds\n".format(sec * (2 ** (tries-1))))
                sleep(sec * (2 ** tries))
            except erro.TimeRequestError as ex:
                print(ex.message)
                print("Try again in a few hours or check the url!\n")
                exit(0)
        except BaseException as ex:
            print(erro.writeError("UnknownError", "catch_exchange", "catch_exchange", "", ex))
            exit(0)


def read_data(arq = 'data.json'):
    try:
        f = open(arq)
    except FileNotFoundError as ex:
        print(erro.writeError("FileNotFoundError", "read_data",  "catch_exchange", f"Read {arq}", "File not found"))
        exit(0)
    except BaseException as ex:
        print(erro.writeError("UnknownError", "read_data", "catch_exchange", "", ex))
        exit(0)
        
    try:
        data = json.load(f)
    except json.decoder.JSONDecodeError as ex:
        print(erro.writeError("JSONDecodeError", "read_data", "catch_exchange", "Convert json data to dict", f"Not json. File: {arq}"))
        exit(0);
    except BaseException as ex:
        print(erro.writeError("UnknownError", "read_data", "catch_exchange", "", ex))
        exit(0)
    
    f.close()
    
    return data

def verify_if_it_s_same_countries(old_ones, new_ones):
    try:
        if not (set(old_ones).issubset(set(new_ones))):
            raise erro.NotSubset("verify_if_it_s_same_countries", "catch_exchange", f"{old_ones}", f"{new_ones}")
        return True
    except erro.NotSubset as ex:
        print(ex.message)
        exit(0)
    except BaseException as ex:
        print(erro.writeError("UnknownError", "Request Exchange API - catch_exchange", "", ex))
        exit(0)

def updated():
    data = read_data()

    try:
        timeline = data["timeline"]
    except KeyError as ex:
        print(erro.writeError("KeyError (in old data)", "updated", "catch_exchange", f"one of: {list(data.keys())}", ex))
        exit(0)
    except BaseException as ex:
        print(erro.writeError("UnknownError (in old data)", "updated" , "catch_exchange", "", ex))
        exit(0)
    
    data = catch_exchange()

    try:
        time_unix = data['time_last_update_unix']
    except KeyError as ex:
        print(erro.writeError("KeyError (in new data)", "updated", "catch_exchange", f"one of: {list(data.keys())}", ex))
        exit(0)
    except BaseException as ex:
        print(erro.writeError("UnknownError (in new data)", "updated", "catch_exchange", "", ex))
        exit(0)
    
    if time_unix in timeline:
        return False
    
    insert_data()
    return True

def insert_data():
    data = catch_exchange()

    try:
        time_unix, currency = data['time_last_update_unix'], data['rates']
    except KeyError as ex:
        print(erro.writeError("KeyError (in new data)", "insert_data", "catch_exchange", f"one of: {list(data.keys())}", ex))
        exit(0)
    except BaseException as ex:
        print(erro.writeError("UnknownError (in new data)", "insert_data", "catch_exchange", "", ex))
        exit(0)
    
    old_data = read_data()
    
    new_data = old_data
    new_data["timeline"].append(time_unix)

    my_countries = list(old_data["values"].keys())
    
    verify_if_it_s_same_countries(my_countries, list(currency.keys()))
    
    for country in my_countries:
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

def periods(arq = 'data.json'):
    data = read_data(arq)

    size = size = len(data['values']['USD'])

    tmp_period = [2, 3, 7, 15, 30, 90, 180, 365, 730, 1095, 1460, 1825, 3650]

    period = []

    for p in tmp_period:
        if p <= size:
            period.append(p)
        else:
            return period
    
    return period

if __name__ == "__main__":
    print("TEST")
    #catch_exchange()
    #print(read_data())
    #print(verify_if_it_s_same_countries(["USD", "BRL"], ["BRL", "ASL"])) False
    #print(verify_if_it_s_same_countries(["USD", "BRL"], ["BRL", "USD"])) True
    #print(verify_if_it_s_same_countries(["USD", "BRL"], ["BRL", "ASL", "USD"])) True
    #print(verify_if_it_s_same_countries(["USD", "BRL", "BIRL"], ["BRL", "ASL", "ABA", "USD", "DIN"]))
    #updated()
    #insert_data()
    #print(periods())

    # ---------------------	ATTENTION !!!!! -----------------
    # Removing the comment from the next line will erase perma-
    # nentily all our data!! Be carefull.

    #clean_data_json()
