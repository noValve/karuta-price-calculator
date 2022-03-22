import math
from string import whitespace
from os import system, name

'''
Source code for a Karuta Price Calculating program by @noValve
'''
def clear():
	if (name == 'nt'):
		_ = system('cls')
	else:
		_ = system('clear')

def logo():
    print("""      ___           ___         ___     
     /__/|         /  /\       /  /\    
    |  |:|        /  /::\     /  /:/    
    |  |:|       /  /:/\:\   /  /:/     
  __|  |:|      /  /:/~/:/  /  /:/  ___ 
 /__/\_|:|____ /__/:/ /:/  /__/:/  /  /\\
 \  \:\/:::::/ \  \:\/:/   \  \:\ /  /:/
  \  \::/~~~~   \  \::/     \  \:\  /:/ 
   \  \:\        \  \:\      \  \:\/:/  
    \  \:\        \  \:\      \  \::/   
     \__\/         \__\/       \__\/    """)
    print("\nCoded by @noValve")
    print("\n\n")

def inputs():
    logo()
    wishlist = input("Amount of wishlists? ")
    wishlist.translate(dict.fromkeys(map(ord, whitespace)))
    while (wishlist.isnumeric() == False or int(wishlist) < 0):
        wishlist = input("The amount has to be at least 0 and an integer. ")
        wishlist.translate(dict.fromkeys(map(ord, whitespace)))
    wishlist = int(wishlist)
    clear()

    logo()
    edition = input("What edition? (1/2) ")
    edition.translate(dict.fromkeys(map(ord, whitespace)))
    while (edition.isnumeric() == False or (edition != str(1) and edition != str(2))):
        edition = input("The edition has to either be 1 or 2. ")
        edition.translate(dict.fromkeys(map(ord, whitespace)))
    edition = int(edition)
    clear()

    logo()
    print_amount = input("What print? ")
    print_amount.translate(dict.fromkeys(map(ord, whitespace)))
    while (print_amount.isnumeric() == False or int(print_amount) < 1):
        print_amount = input("The print number has to be at least 1 and be an integer. ")
        print_amount.translate(dict.fromkeys(map(ord, whitespace)))
    print_amount = int(print_amount)
    clear()

    logo()
    quality = input("How many stars? ")
    quality.translate(dict.fromkeys(map(ord, whitespace)))
    while (quality.isnumeric() == False or (int(quality) < 0 or int(quality) > 4)):
        quality = input("The amount of stars can't be less than 0, greater than 4 and has to be an integer. ")
        quality.translate(dict.fromkeys(map(ord, whitespace)))
    quality = int(quality)
    clear()
    logo()
    return wishlist, edition, print_amount, quality


def calc():
    wishlist, edition, print_amount, quality = inputs()
    tickets = 0
    if edition == 1:
        if print_amount > 1000:
            if quality == 0 or quality == 1:
                tickets = wishlist / 85
            elif quality == 2 or quality == 3 or quality == 4:
                tickets = wishlist / 80
        elif print_amount < 100:
            return "Take offers."
        else:
            if quality == 0 or quality == 1:
                tickets = wishlist / 35
            elif quality == 2 or quality == 3 or quality == 4:
                tickets = wishlist / 30
    elif edition == 2:
        if print_amount > 1000:
            if quality == 0 or quality == 1:
                tickets = wishlist / 65
            elif quality == 2 or quality == 3 or quality == 4:
                tickets = wishlist / 60
        elif print_amount < 100:
            return "Take offers."
        else:
            if quality == 0 or quality == 1:
                tickets = wishlist / 25
            elif quality == 2 or quality == 3 or quality == 4:
                tickets = wishlist / 20
    
    tickets = math.ceil(tickets)
    gems = tickets*20
    gold = tickets*500
    result = "This card is worth " + str(tickets) + " tickets, " + str(gems) + " gems and " + str(gold) + " gold."
    return result

print(calc())