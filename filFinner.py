import os 

current_dir = os.getcwd()
dir_list = os.listdir(current_dir)

print("")
print("-"*20)
print("Her er en liste over filer:")
for i in range(len(dir_list)):
    print(i,":",dir_list[i])