try:
    file = open('assignment.ipynb',"r")
    print(file.read())  
except:
    print("File not found")
finally:
    print("File closed")
    file.close()