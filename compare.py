import sys 
base_apps = sys.argv[1]
current_apps = sys.argv[2]

list = []


file_base_apps = open(base_apps, "r")
file_current_apps = open(current_apps, "r")
final_base_file = open("final_base.txt", "w")
final_current_file = open("final_current.txt", "w")
restult = open("result.txt", "w")

while file_base_apps.readline():
    line = file_base_apps.readline()
    p = line.split()   
    final_base_file.write(p[0])
    final_base_file.write("\n")

while file_current_apps.readline():
    line = file_current_apps.readline()
    p = line.split()   
    final_current_file.write(p[0])
    final_current_file.write("\n")

with open("final_base.txt", "r") as file:
    with open("final_current.txt", 'r') as file2:
        while file2.readline():
            if file.readline() == file2.readline():
                pass
            else:
                restult.write(file2.readline())

file.close()
file2.close()