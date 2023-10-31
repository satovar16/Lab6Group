# Santiago Tovar                       Date: 10/30/2023
# This function will take a password and encode it by shifting up the number by 3 '12345' --> '45678'
# This file also include the main function 
def encode(password):                          #Create function
    if len(password) != 8:
        print('The password should be 8 digit')

    password_list = []
    password_string = ''                        #Initiate variables

    for num in password:

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

        elif num == '5':
            num = '8'

        elif num == '6':
            num = '9'

        elif num == '7':
            num = '0'

        elif num == '8':
            num = '1'

        elif num == '9':
            num = '2'

        password_list.append(num)

    for i in password_list:
        password_string += '' + i

    return password_string


def main():
    user_password = '1234567'
    while True:
        print('Menu\n-------------')
        print('1. Encode\n2. Decode\n3. Quit\n')
        user_selection = input('Please enter an option: ')

        if user_selection == '1':
            while len(user_password) != 8:
                user_password = input('Please enter your password to encode: ')
                print('Error: Password should be 8 digit long\n')
            encoded_password = encode(user_password)
            print('Your password has been encoded and stored!\n')

        elif user_selection == '2':
            decoded_password = decode(encoded_password)
            print('The encoded password is', encoded_password, 'and the original password is', decoded_password, end='')
            print('.')

        elif user_selection == '3':
            break

        else:
            print('Please select a valid option\n')

if __name__ == "__main__":                                      #Call main function
    main()


