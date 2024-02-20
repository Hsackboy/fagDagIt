import os 
import kultBiblotek2 as kB

# current_dir = os.getcwd()


def finnFil(current_dir):
    dir_list = os.listdir(current_dir)

    print("")
    print("-"*20)
    print("Her er en liste over filer:")
    kB.print1DList(dir_list)

    brukerInput = kB.betterInput(variableType="int",inputText=f"Hvilken fil vil du ha?(0-{len(dir_list)-1}): ",errorText="Dette var ikke et heltall",forventet=[i for i in range(len(dir_list))])
    current_dir +="/"+dir_list[brukerInput]


    while os.path.isdir(current_dir)==True:
        print("")
        print("-"*20)
        dir_list = os.listdir(current_dir)
        print("Her er en liste over filer:")
        kB.print1DList(dir_list)
        brukerInput = kB.betterInput(variableType="int",inputText=f"Hvilken fil vil du ha?(0-{len(dir_list)-1}): ",errorText="Dette var ikke et heltall",forventet=[i for i in range(len(dir_list))])
        current_dir +="/"+dir_list[brukerInput]
    
    return current_dir


if __name__ =="__main__":
    print(finnFil(os.getcwd()))
