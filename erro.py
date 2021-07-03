def add_log(where, expected, received):
    where = str(where)
    expected = str(expected)
    received = str(received)
    
    date = datetime.now()
    date = date.strftime("%d/%m/%Y %H:%M:%S")
    erro_msg = date + " Error local: " + where + "\n\tExpected: " + expected + "\n\tReceived: " + received + "\n"
    
    with open ('log_file', 'a') as log:
        log.write(erro_msg)
    
    print("Erro! Verifique o arquivo de log!\n")
    exit(0)