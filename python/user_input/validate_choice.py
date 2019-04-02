def user_says_yes(message=""):
    '''Check if user input is either 'y' or 'n'. Returns a boolean.'''

    while True:
        choice = input(message).lower()
        if choice == 'y':
            choice = True
            break
        elif choice == 'n':
            choice = False
            break
        else:
            print("Please enter either 'y' or 'n'.")

    return choice
