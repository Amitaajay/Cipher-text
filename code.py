import sys
check=sys.version
flag = 0
if check.startswith("3"):
    value=int(input("Enter the offset: \n"))
    emsg=input("Enter the encoded message: \n")
    flag = 1
    
else: 
    value=int(raw_input("Enter the offset: \n"))
    emsg=raw_input("Enter the encoded message: \n")
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
    else:
        omsg = omsg + c
print('Original Message: '+omsg)

