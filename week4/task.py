#this program reads a file and writes a modified version to a new file
try:
    #reads file
    source = input("Enter source file to read from: ")
    with open(source, "r") as f:
        content = f.read()
    
    #modifies file
    modify = input("Enter new filename to write to: ")
    with open(modify, "w") as newfile:
        newfile.write(content.upper())
    print("File created successfully!")
    
    #handle errors
except FileNotFoundError:
    print("File not found")
except PermissionError:
    print("You do not have permission to read or write this file")
except Exception as e:
    print("Error!")