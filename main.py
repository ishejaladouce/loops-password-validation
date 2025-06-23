#Initialize the correct password and the attempts counter
exact_password = "Secret123" 
attempts = 0  

while True:
    #Ask the user for password and increment attempt counter
    password = input("Enter your password: ")  
    attempts += 1  

    # Count digits in password 
    digit_count = 0
    for char in password:
        if char.isdigit():
            digit_count += 1

    # Print length of entered password
    print(len("Your pswd length is: " +password))  

    # Check password type for feedback
    if password.isdigit():
        print("Password is numeric")
    elif password.isalpha():
        print("Password is alphabetic")
    else:
        print("Password contains a mix of characters and digits")

    # If no digits, print error and continue
    if digit_count == 0:
        print("Error: Need a digit.")
        continue

    # If password is correct, grant access and break loop
    if password == exact_password:
        print("Access granted")
        break
    else:
        # Wrong password with at least one digit
        print("Access denied.")  
        
        # Print alert if more than two wrong attempts
        if attempts > 2:
            print("Retry Alert: Too many failed attempts!")
