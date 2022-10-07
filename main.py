import coverGrabber

def stayActive():
    stayactive = True
    thisactive = True
    while thisactive:
        answer = input("Do you want to start over? (yes, y, j / no, n): ")

        if answer == "yes" or answer == "y" or answer == "j":
            stayactive = True
            thisactive = False
            return stayactive
        
        elif answer == "no" or answer == "n":
            stayactive = False
            thisactive = False
            return stayactive
        
        else:
            print("Please enter yes or no!")
            thisactive = True




if __name__ == "__main__":
    
    active = True

    while active:
        print(" ")
        mode = input("Please select which action should be performed \n - (1) to dowload the cover of a song \n - (2) coming soon... \n Your choice: ")

        if mode == "1":
            print(" ")
            url = input("Please paste the soundcloud url into this window (ctrl + shift + v // cmd + v) and press enter: ")
            coverGrabber.run(url)
            active = stayActive()

        elif mode == "2":
            print(" ")
            print("This function is not implemented yet and will come soon :))")
            print(" ")
            active = stayActive()
        else:
            print("Please input 1 or 2!")