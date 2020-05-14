from cryptography.fernet import Fernet as fnet

input_file = input("> inter your file path ")

with open(input_file,"rb+") as file:
    t = file.read()
key = b'54h612MgospYPvWeVBYCCd-W4U29LEOzFh84RpuNxog='


#with open("key.txt","r") as file:
#    key = file.read()
f = fnet(key)
decrypted_file = f.decrypt(t)

with open(input_file,"wb") as file:
    file.write(decrypted_file)
