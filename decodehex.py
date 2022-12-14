'''
Cyber Security IPB - Early Challenge

Category : Cryptography
Writeup  : https://naufalardhani.medium.com/cyber-security-ipb-agrihack-early-challenge-82ae02d8ab92
'''

def decode(**csi):
    ciphertext = csi['hex']
    a_string = bytes.fromhex(ciphertext)
    a_string = a_string.decode("ascii")
    return a_string

if __name__ == "__main__":
    ciphertext = "6561726c795f6368616c6c5f637369"
    decode_hex = decode(hex=ciphertext)
    print(decode_hex)
