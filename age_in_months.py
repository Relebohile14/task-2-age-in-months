#looping the script
while True:

    #Get and validate name
    while True:
        name = str(input("What is your name? ").title())
        if name.isalpha():
            break
        else:
            print("Please enter valid name (letters only).")

    print (f"Hello {name}!")

    #Get favourite Subject
    fav_sub = input("\nWhat is your favourite subject? ").title().strip()
    print(f"{fav_sub} is a great subject!")

    #Get age and convert to months
    #try, except for error handling
    while True:
         try:
             age = int(input("\nHow old are you? "))
             break
         except ValueError:
             print("Please enter a number.")

    months = age * 12
    print (f"You are {age} years old, which is {months} months!\n" )

#Ask to repeat
    opt = input("Do you wish to repeat (yes/no)? ").lower().strip()
    if opt != "yes":
        print(f"\nEnjoy the rest of your day {name}! Goodbye!")
        break
