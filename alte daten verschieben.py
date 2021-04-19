import os
import datetime
import shutil


directory = input("Pfad einkopieren")
os.chdir(f"{directory}")
years = [x for x in range(2010,2023)]
def moveold(directory):

    for year in years:
        y = datetime.datetime(year, 1, 1)
        z = y.strftime(y.strftime('%Y'))
        #print(f"{plan} - erstellt am {x}")
        filename = f"{year-1}"

        ## Check if dir is there: if not create on, else pass
        files = os.listdir(directory)
        if filename in os.listdir(directory):
            pass
        else:
            os.mkdir(f"{year-1}")
        #Check the dates of the files and move them in the right directory
        for file in files:
            date = os.path.getmtime(f"{file}")
            v = datetime.datetime.fromtimestamp(date)
            if v < y:
                shutil.move(f"{file}", f"{filename}")
        #After Moving check if there's a empty directory left
        #if it's left, remove it
        if len(os.listdir(f"{year-1}")) == 0:
            os.rmdir(f"{year-1}")


# Check if it's a directory
def isdirectory(typ):

    if os.path.isdir(f"{typ}") == True:
        return True
    else:

        return False

#recursion for check the hierarchy
def recursion():
    #check the filtetypes
    types = os.listdir(os.getcwd())

    for typ in types:
        #if its a directory change into the directory and check again
        if isdirectory(f"{typ}") == True:
            os.chdir(f"{os.getcwd()}\\{typ}")

            recursion()
        #if not move the files and create the directorys
        else:
            #print("Ist eine Datei")
            #print(os.getcwd())
            #print("würde jetzt kopieren")
            moveold(os.getcwd())
        #if the directory is empty go back until you're in the root folder

        full = [x for x in os.listdir(os.getcwd()) if os.path.isfile(x) == True]

        if len(full) == 0:
            if os.getcwd() == directory:
                pass
            else:
                os.chdir("..")

recursion()
print("Files Moved")
