# Santiago Tovar                       Date: 10/30/2023
# This function will take a password and encode it by shifting up the 
number by 3 '12345' --> '45678'
# This file also include the main function
def encode(password):                          #Create function
    if len(password) != 8:
        print('The password should be 8 digit')

    password_list = []
    password_string = ''                        #Initiate variables

    for num in password:			#For loop to iterate between the numbers of the password

        if num == '0':
            num = '3'

        elif num == '1':			
            num = '4'

        elif num == '2':
            num = '5'

        elif num == '3':
            num = '6'

        elif num == '4':
            num = '7'

        elif num == '5':			#Go through the numbers and change their value shifting up 3
            num = '8'

        elif num == '6':
            num = '9'

        elif num == '7':
            num = '0'

        elif num == '8':
            num = '1'

        elif num == '9':
            num = '2'

        password_list.append(num)		#Append the updated value

    for i in password_list:			#For loop concatenate the password in a string
        password_string += '' + i

    return password_string			#return encoded password


def main():					#main function
    user_password = '1234567'
    while True:
        print('Menu\n-------------')			#create variable for the loop
        print('1. Encode\n2. Decode\n3. Quit\n')
        user_selection = input('Please enter an option: ')			#print menu and prompt user for password 

        if user_selection == '1':
            user_password = input('Please enter your password to encode: ')
            while len(user_password) != 8: #
                print('Error: Password should be 8 digit long\n')			#create the if-elif statements and main workflow
                user_password = input('Please enter your password to encode: ')
            encoded_password = encode(user_password)
            print('Your password has been encoded and stored!\n')

        elif user_selection == '2':
            decoded_password = decode(encoded_password)
            print('The encoded password is', encoded_password, 'and the 
original password is', decoded_password, end='')
            print('.\n')
            user_password = '1234567'

        elif user_selection == '3':
            break

        else:									#else if the user enters an invalid option
            print('Please select a valid option\n')
# Bernardo Lechuga                  Date: 10/31/2023	
def decode(encoded_password):

    if not encoded_password.isdigit() or len(encoded_password) != 8:
        raise ValueError("Encoded password must be an 8-digit string 
containing only integers.")

    original_password = ""
    for char in encoded_password:

        original_digit = (int(char) - 3) % 10
        original_password += str(original_digit)

    return original_password


if __name__ == "__main__":                                      #Call main 
function
    main()

