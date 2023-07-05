import os

usernames = ['alonso', 'matias', 'benjamin']
passwords = ['guajardo', 'toro', 'sepulveda']

def crearusers():
    for username, password in zip(usernames, passwords):
        os.system(f'curl --insecure -X POST -d "username={username}&password={password}" https://localhost:9500/signup/v2')

def logearusers():
    for username, password in zip(usernames, passwords):
        os.system(f'curl --insecure -X POST -d "username={username}&password={password}" https://localhost:9500/login/v2')

os.system('clear')
#crea usuarios en la lista
crearusers()

#logea los usuarios anteriormente creados
logearusers()