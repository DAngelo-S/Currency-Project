from datetime import datetime

class Error(Exception):
    pass

class RequestError(Error):
    def __init__(self, status):
        message = error_msg("RequestError: Request Exchange API - catch_exchange", 200, status)
        add_log(message)
        self.message = message

class TimeRequestError(Error):
    def __init__(self, tries):
        message = error_msg("TimeRequestError: Request Exchange API - catch_exchange", "", "Exceeded the limit of tries ({})".format(tries))
        add_log(message)
        self.message = message

class NotSameCountries:
    def __init__(self, exp, rec):
        message = error_msg("NotSameCountries: Verify if it's same countries - catch_exchange", sexp, rec)
        add_log(message)
        self.message = message

def writeError(errorType, local, exp, rec):
        message = error_msg(str(errorType) + ": " + str(local), str(exp), str(rec))
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