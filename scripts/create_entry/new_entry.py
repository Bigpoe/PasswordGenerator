import random

class CreateEntry:

    def __init__(self):
        self.capital_case = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        self.lower_case = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        self.numbers = ['0','1','2','3','4','5','6','7','8','9']
        self.special_characters = ['@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '{', '}', '[', ']', '|', ';', ':', '<', '>', '.', '?']

    def ask_url(self):
        url_name = input('Enter the URL: ')
        return url_name


    def ask_username(self):
        username = input('Enter your Username: ')
        return username


    def generate_password(self):
        ## Concatenates the all the lists to create a pool of characters ##
        characters_pool = self.capital_case + self.lower_case + self.numbers + self.special_characters
        ## Shuffles the characters in the pool of characters ##
        random.shuffle(characters_pool)
        ## Pick randomly 16 characters to generate the password ##
        characters_list = random.sample(characters_pool, k=16)
        ## Joins each element in the characters_list to generate the password string ##
        password = ''.join(element for element in characters_list)

        return password
