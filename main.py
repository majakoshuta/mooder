while True:
    moodInput = input("How do you feel? ")
    mood = moodInput.casefold()
    if mood == "depressed":
         print("Drink a glass of water and pick a cloud from the sky.")
    elif mood == "eh":
        print("It's going to get better, for now just read a random chapter from the nearest book.")
    elif mood == "nervous":
        print("Breathe in for 4 seconds, hold for 4 seconds, breath out for 6 seconds.")
    elif mood.isdigit():
        number = str(mood)
        print("You feel it " + number + " times the intensity, right? Go nap!")
    elif mood == "happy":
        print("Rock on!")
    elif mood == "sad":
        print("It's okay to be sad. Think about what you're grateful for right now. Call your sister.")
    elif mood == "angry":
        print("Put on some electro-dance or death metal and go run!")
    elif mood == "bored":
        print("Did you know that the least interesting day in history was April 11th 1954?")
    elif mood == "confused":
        print("Ummm hmmmm aaaaam eeeee")
    else:
        print("One foot after the other, darling!")
        break