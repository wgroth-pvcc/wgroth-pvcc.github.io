# MODULES
import itertools
from itertools import product
import zipfile

# METHOD SELECTION
print("Please select the password cracking method. \n1 - Attempt to crack using brute force \n2 - Attempt to crack using a dictionary. \n3 - Attempt to crack using both a dictionary and brute force. \n4 - Quit the program.")
method = input()

# METHOD FUNCTION
def crack(method):
    if method == "1":
        print("Brute force crack will be attempted.")
        zip_file = open_zip_file()
        try:
            brute_force_crack(zip_file)
        except:
            pass
        print("Check folder to see if file was successfully extracted.")
        prompt()
        
    elif method == "2":
        print("Dictionary crack will be attempted.")
        zip_file = open_zip_file()
        dict_file = open_dict_file()
        try:
            dict_crack(zip_file, dict_file)
        except:
            pass
        print("Check folder to see if file was successfully extracted.")
        prompt()
        
    elif method == "3":
        print("Dictionary crack will be attempted. If that fails, brute force crack automatically will be attempted.")
        zip_file = open_zip_file()
        dict_file = open_dict_file()
        try:
            dict_crack(zip_file, dict_file)
        except:
            pass
        try:
            brute_force_crack(zip_file)
        except:
            pass
        print("Check folder to see if file was successfully extracted.")
        prompt()

    elif method == "4":
        quit()
    else:
        print("Invalid input.")
        print("Please select the password cracking method. \n1 - Crack using brute force \n2 - Crack using a dictionary. \n3 - Crack using a dictionary. If that fails, crack by brute force. \n4 - Quit the program.")
        method = input()
        crack(method)

# OPEN_ZIP_FILE FUNCTION
def open_zip_file():
    print("Enter the name of the .zip file. Include the file extension.")
    try:
        filename = input()
        zip_file = zipfile.ZipFile(filename)
        return zip_file
    except FileNotFoundError:
        print("Error. File not found.")
        open_zip_file()

# OPEN_DICT_FILE FUNCTION
def open_dict_file():
    print("Enter the name of the .txt file. Include the file extension.")
    try:
        dict_file = open(input())
        dict_file = dict_file.readlines()
        return dict_file
    except FileNotFoundError:
        print("Error. File not found.")
        open_dict_file()

# BRUTE_FORCE_CRACK FUNCTION
def brute_force_crack(zip_file):
    r = 1
    while r <=20:
        for items in product("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890", repeat = r):
            password = ''.join(items)
            try:
                zip_file.extractall(pwd=password.encode())
            except:
                r += 1
                pass

# DICT_CRACK FUNCTION
def dict_crack(zip_file, dict_file):
    for password in dict_file:
        try:
            zip_file.extractall(pwd=password.encode())
        except:
            pass

# PROMPT FUNCTION
def prompt():
    print("1 - Try another file or method. \n2 - Quit the program.")
    choice = input()
    if choice == "1":
        print("Please select the password cracking method. \n1 - Crack using brute force \n2 - Crack using a dictionary. \n3 - Crack using a dictionary. If that fails, crack by brute force. \n4 - Quit the program.")
        method = input()
        crack(method)
    elif choice == "2":
        quit()
    else:
        print("Invalid input.")
        prompt()

# FUNCTION CALLS
crack(method)
