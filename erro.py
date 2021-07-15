from datetime import datetime

class Error(Exception):
    pass

class RequestError(Error):
    def __init__(self, status):
        message = error_msg("Request Exchange API - catch_exchange", 200, status)
        add_log(message)
        self.message = message

class TimeRequestError(Error):
    def __init__(self, tries):
        message = error_msg("Request Exchange API - catch_exchange", "", "Exceeded the limit of tries ({})".format(tries))
        add_log(message)
        self.message = message

def UnknownError(local, ex):
        message = error_msg(local, "", ex)
        add_log(message)
        return message

def error_msg(where, expected, received):
    where = str(where)
    expected = str(expected)
    received = str(received)
    
    date = datetime.now()
    date = date.strftime("%d/%m/%Y %H:%M:%S")
    msg = date + " Error local: " + where + "\n\tExpected: " + expected + "\n\tReceived: " + received + "\n"

    return msg

def add_log(msg):
    with open('log_file', 'a') as log:
        log.write(msg)