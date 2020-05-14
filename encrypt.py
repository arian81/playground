from cryptography.fernet import Fernet as fnet
key = fnet.generate_key()
f = fnet(key)
input_file = input("> inter your file path ")
with open(input_file,"rb+") as file:
    t = file.read()

encrypted_file = f.encrypt(t)
with open("key.txt","w") as x:
    x.write(str(key))

with open(input_file,"wb") as file:
    file.write(encrypted_file)
