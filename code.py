value=int(input("Enter the offset: \n"))
emsg=input("Enter the encoded message: \n")
omsg=""
for c in emsg:
    if c.isupper():
        n = ord(c) - 65
        text = chr(((n - value) % 26) + 65)
        omsg = omsg + text
    elif c.islower():
        n= ord(c) - 97
        text = chr(((n - value) % 26) + 97)
        omsg = omsg + text
        
print("Original Message:",omsg)
