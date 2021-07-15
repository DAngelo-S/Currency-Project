from datetime import datetime

class Error(Exception):
    pass

class RequestError(Error):
    def __init__(self, func, module, status):
        message = error_msg(f"RequestError: {func} - {module}", 200, status)
        add_log(message)
        self.message = message

class TimeRequestError(Error):
    def __init__(self, func, module, tries):
        message = error_msg(f"TimeRequestError: {func} - {module}", "", "Exceeded the limit of tries ({})".format(tries))
        add_log(message)
        self.message = message

class NotSubset(Error):
    def __init__(self, func, module, exp, rec):
        message = error_msg(f"NotSubset: {func} - {module}", exp, rec)
        add_log(message)
        self.message = message

def writeError(errorType, func, module, exp, rec):
        message = error_msg(str(errorType) + ": " + str(func) + " - " + str(module), exp, rec)
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