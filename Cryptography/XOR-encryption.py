#!/bin/python3.9
# origin functions ripped from https://en.wikipedia.org/wiki/XOR_cipher#CITEREFRichter2012
# inspired by https://blog.xrds.acm.org/2012/08/unbreakable-cryptography-in-5-minutes/


from os import urandom


def genkey(length: int) -> bytes:
    """Generate key."""
    return urandom(length)


def xor_strings(s, t) -> bytes:
    """Concate xor two strings together."""
    if isinstance(s, str):
        # Text strings contain single characters
        return "".join(chr(ord(a) ^ b) for a, b in zip(s, t)).encode('utf8')
    else:
        # Bytes objects contain integer values in the range 0-255
        return bytes([a ^ b for a, b in zip(s, t)])

def unitTest():
        message = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'
        print('Message:', message)
        key = genkey(len(message))
        print('Key:', key)
        cipherText = xor_strings(message.encode('utf8'), key)
        print('cipherText:', cipherText)
        print('decrypted:', xor_strings(cipherText, key).decode('utf8'))
        # Verify
        if xor_strings(cipherText, key).decode('utf8') == message:
            print('Unit test passed')
        else:
            print('Unit test failed')

# Generate a key based on a password supplied by the user
def passGenKey(m) -> bytes:
        p=input("enter a password:") # Get the password
        key=b'' # Make a key variuble
        chunks=len(m) // len(p) # Get result from a modulus on the length of the mssage and the length of the key
        oddbits=len(m)-(len(p)*chunks) # Determine the number of odd bits will be left after iterating through the string
        for i in range(0,len(m)-1, len(p) ): # Iterate through the message starting at 0 and ending at the length of the message with a step of however long the password is
                for j in range( len(p) ): # for each charicter in the password
                        key=key+ord(p[j]).to_bytes(1, byteorder="big") # add the byte value of the password to the end of the key
        return key # Return the key
        # the key should be as long as the message

message = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'
key=passGenKey(message) # Get the keystring described in the function above
cypherText=xor_strings(message.encode("utf8"),key) # transform the message into cyphertext
print(cypherText) # check we have some nice cyphertext
decoded=xor_strings(cypherText, key) # verify the message can be decrypted using the same method and the same password
print(decoded.decode("utf8"))
