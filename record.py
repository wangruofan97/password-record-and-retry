import base64
import hashlib

f = open('info.txt','r+')
output = open('cypher.txt','a')
lines = f.readlines()
for line in lines:
    myfile = line.strip('\n').split(" ")
    site = myfile[0]
    username = myfile[1]
    cypher = myfile[2]

    a=base64.b64encode(site.encode('utf-8')).decode('utf-8')
    b=base64.b64encode(username.encode('utf-8')).decode('utf-8')
    sha = hashlib.sha256()
    sha.update(cypher.encode('utf-8'))
    res = sha.hexdigest()

    output.write(a+' '+b+' '+res+'\n')

f.seek(0)
f.truncate()
f.close()
