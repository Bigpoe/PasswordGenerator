import os
import pathlib
from os.path import exists


class SaveEntry:

    def __init__(self):
        self.passwords_folder = 'passwords'
        self.file_name = 'passwords.txt'
        project_path = pathlib.Path().resolve()
        self.path = os.path.join(project_path, self.passwords_folder, self.file_name) 


    def check_if_url_exists(self, url_name):
        try:
            ## Check if the new URL already exists in the Passwords.txt file ##
            ## --> I need to improve the validation method ##
            if exists(self.path):
                with open(self.path) as file:
                    file_content = file.read()
                if url_name in file_content:
                    url_exists = True
                else:
                    url_exists =False 
            return url_exists
        
        except NameError:
            print('Something wrong happened evaluating if the URL exists in the Passwords.txt file')


    def save_entry(self, url_name, username, password):
        try:
            separator = ','
            entry = []
            entry.append(url_name)
            entry.append(username)
            entry.append(password)
            entry = separator.join(entry)
            
            ## Creates the Passwords.csv file if it does not exist ##
            if not exists(self.path):
                with open(self.path, 'w') as file:
                    file.write("")
                print('Passwords.txt file created')
            
            url_exists = self.check_if_url_exists(url_name)
            if url_exists:
                add_again = input(f'WARNING: An entry with the URL `{url_name}` already exists in your Passwords file. Do you want to add it again?\nY/N\n\n')
                ## If 'add_again' is 'N' or 'n', the execution is interrupted ##
                if add_again == 'N' or add_again == 'n':
                    raise SystemExit(0)
            
            ## Writes the new entry in the Passwords.txt file ##
            with open(self.path, 'a') as file:
                file.write(entry + '\n')

        except NameError:
            print('Something wrong happened saving the entry in the Passwords.csv file ')
