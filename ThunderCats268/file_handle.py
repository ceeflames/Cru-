#ToDo::
    #ENCRYPTION/DECRYPTION
import os
#from cryptography.fernet import Fernet
from pathlib import Path



class File_man():
    def __init__(self, **kwargs):
        pass
 
    def file_list(self, path):
        file_list = []
        file_list = os.listdir(path)
        return file_list

    def clean_data(self, data, delim):
        n_data = data[2:-2]
        n_list = n_data.split(str(delim))
        return n_list


    def get_file_list(self, file_name, delim):
        if file_name:
            try:
                with open(file_name, "r") as rf:
                    data = rf.readlines()
                    rf.close()
                    return (data)
            except Exception as e:
                print("ERROR_READING_FILE", str(e))
                return "ERROR_READING_FILE"
    


    def read_file(self, file_name, delim):
        if file_name:
            try:
                with open(file_name, "r") as rf:
                    data = rf.readlines()
                    rf.close()
                    if str(data) == "[]" or str(data) == "['']":
                        return ''
                    return (self.clean_data(str(data), delim))
            except Exception as e:
                print("ERROR_READING_FILE", str(e))
                return "ERROR_READING_FILE"
    
    def write_file(self, file_name, data, delim, rwm):

        text = ""
        fc = self.check_file(file_name)
        if fc == False:
            os.system('touch ' + file_name)
        if file_name:
            if type(data) == str:
                text = data + "\n"
                print("WRITING STR:: ", str(text))
            elif type(data) == list:
                for _ in data:
                    text += str(_) + str(delim)
                print("WRITING LIST:: ", str(data))
            elif type(data) == str or len(data) == 0:
                text = ""

            elif type(data) == str and "\n" in data:
                text = ""

            print(f'TEXT_TO_WRITE: \n {text}')      
            with open(file_name, rwm) as wf:
                wf.write(text)
                wf.close()
            return

    def check_file(self, file_name):
        path_to_file = file_name
        path = Path(path_to_file)
        if path.is_file():
            #print(f'[file exists] : {file_name}')
            return True
        else:
            print(f'[file]: {path_to_file} !does_not_exist!')
            return False



#FOR LATER ON...


#    def encrypt(self, data):
#        pass
#
#    def decrypt(self, data):
#        pass
#
#    def load_key(self):   
#        """
#        Loads the key from the current directory named `key.key`
#        """
#        return open("login.txt", "rb").read()
#
#    def write_key():
#        """
#        Generates a key and save it into a file
#        """
#        key = Fernet.generate_key()
#        with open("key.key", "wb") as key_file:
#            key_file.write(key)    