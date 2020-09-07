#import necessary modules and packages
import random

#open the text file using the full path
with open('/Users/danielakinniranye/Documents/Project/Random/words.txt','r') as file:
    content = file.read().split()

number_code = random.randint(1,300)

#combination of the random words and number_code
user_password = random.choice(content) + str(number_code)

stored_password = user_password
print('Your generated password is: ' + stored_password)
