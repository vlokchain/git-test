def show_homepage():
    print("     === DonateMe Homepage ===            ")
    print("------------------------------------------")
    print("| 1.   Login     | 2.   Register         |")
    print("------------------------------------------")
    print("------------------------------------------")
    print("| 3.   Donate    | 4.   Show Donations   |")
    print("------------------------------------------")
    print("|             5. Exit                    |")
    print("------------------------------------------")

def donate(username):
    donation_amt = (input("\nEnter amount to donate: "))
    donation_string = username + " donated $" + donation_amt
    print("Thank you for your donation!")
    return donation_string

def show_donations(donations):
    print("\n----All Donations----")
    if donations == []:
        print("\nCurrently, there are no donations.")
    else:
        for amount in donations:
            print(amount)