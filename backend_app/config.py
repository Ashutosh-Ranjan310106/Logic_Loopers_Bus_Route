appstate = 'local'
if appstate == 'production':
    host = '192.168.163.145'
elif appstate == 'hamachi':
    host = '25.24.45.37'
else:
    host='127.0.0.1'