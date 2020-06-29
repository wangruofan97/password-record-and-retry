import base64
import hashlib
import sys

def check(site, username):
    f= open('cypher.txt','r')
    lines = f.readlines()
    input_site = base64.b64encode(site.encode('utf-8')).decode('utf-8')
    input_user = base64.b64encode(username.encode('utf-8')).decode('utf-8')
    for line in lines:
        info = line.strip('\n').split(' ')
        if input_site == info[0]:
            if input_user == info[1]:
                return info[2]
            else:
                user = base64.b64decode(info[1].encode('utf-8')).decode('utf-8')
                print("Maybe your username is "+user+".")
    return '0'

site = input('site: ')
username = input('username: ')
ans = check(site, username)
if ans == '0':
    print('Not found.')
    sys.exit()

while(True):
    password = input('password: ')
    sha = hashlib.sha256()
    sha.update(password.encode('utf-8'))
    res = sha.hexdigest()
    print(res)
    if res == ans:
        print("Correct!")
        break
    else:
        print("Wrong, please retry.")
        