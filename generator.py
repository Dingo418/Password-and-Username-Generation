from msilib.schema import Error
import sys
import random
class gen():

    def __init__(self):
        # command feedback for various arguments
        pas_length, amount = 8, 1  # Sets defaults
        try:
            pas_length = int(sys.argv[1])  # sees if their is an argument for agr 1
        except (IndexError, ValueError):
            pass
        try:
            amount = int(sys.argv[2]) # sees if their is an argument for agr 2
        except (IndexError, ValueError):
            pass
        try:
            if sys.argv[1] == "help":  # if the first argument is "help"
                print("Usage: \n"  # print the usage instructions
                      "    generator <password_length>\n"
                      "    generator <password_length> <amount_of_logins>\n")
                sys.exit()
        except IndexError:  # if the user did not pass anything threw
            print("No length specified, using default of 8.")
        gen.genuser_password(amount, pas_length)
    def genlist():
        lower = "abcdefghijklmnopqrstuvwxyz"
        upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        num = '0123456789'
        symbols = "!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
        return lower + upper + num + symbols #simply returns a full list to choice from
    
    def word_list():
        words = open("words.txt", "r")
        word_list = []
        for line in words: #repeats for as many lines in the text file
            stripped_line = line.strip() #strips all the words from a line making it a list
            line_list = stripped_line.split() 
            word_list.append(line_list)
        words.close() 
        return word_list #returns a list full of words

    def genpassword(pasLength):
        list = gen.genlist() #gets the big list
        temp = random.choices(list, k=pasLength) #gets a defined amount of random charaters and puts it into a list
        return ''.join(temp) #Changes list from list to string

    def genuser():
        word_list = gen.word_list() #gets the word list
        return "".join(word_list[random.randrange(0, len(word_list))]) + "".join(word_list[random.randrange(0, len(word_list))]) + str(random.randrange(100, 999)) #returns two words and a random 3 digit number together
    
    def genuser_password(amount, paslength):
        for i in range(0, amount): #loops for as many times in amount
            user = gen.genuser() #gets a random username
            password = gen.genpassword(paslength) #gets a random password with determined length
            print(f"Your username is: {user} | Your password is: {password}") #outputs it into console


gen()