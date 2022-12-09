import os
import random
import time
import colorama
import sys
from os import system, name
from time import sleep
from colorama import Fore, Back, Style

colorama.init()
import time
import random


def cls():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)


    #functions
def g(rolls):
    data = "qwertyuioplkjhgfdsazxcvbnm1234567890QWERTYUIOPLKJHGFDSAZXCVBNM"
    result = ""
    while rolls >= 1:
        c = random.choice(data)
        result = c + result
        rolls = rolls - 1
    return result


def title():
    print(f'''{Fore.LIGHTBLUE_EX} 
 ___  _  _  ___  ___   ___ __   __       ___  __  __  __  __ 
| __|| \| || __|| _ \ / __|\ \ / /     / __||  \/  ||  \/  |
| _| | .  || _| |   /| (_ | \   /      \__ \| |\/| || |\/| |
|___||_|\_||___||_|_\ \___|  |_|       |___/|_|  |_||_|  |_|''')
    print(f"{Fore.WHITE}                Skateborder#5696 | .gg/energysmm")

title()
print(" ")

print(f"{Fore.BLUE} Checked: ")
print(" ")
print(f"{Fore.GREEN}   [1] {Fore.WHITE}Amazon Store Card")
print(f"{Fore.GREEN}   [2] {Fore.WHITE}Discord Nitro Gen + Checker")
print(f"{Fore.GREEN}   [3] {Fore.WHITE}Xbox Gift Card")
print(f"{Fore.GREEN}   [4] {Fore.WHITE}Playstation Gift Card")
print(" ")
print(f"{Fore.BLUE} Unchecked: ")
print(" ")
print(f"{Fore.GREEN}   [5] {Fore.WHITE}Netflix Gift Code")
print(f"{Fore.GREEN}   [6] {Fore.WHITE}Other Unchecked")
print(" ")
print(f"{Fore.BLUE} Enter Choice: ")
print(" ")
choice = int(input(f"{Fore.GREEN}   [?] > "))

if choice == 1:
    import random
    import time
    import colorama
    from colorama import Fore, Back, Style
    colorama.init()

    class validator():

        def __init__(self):
            self.cardNumber = None
            self.Brand = None

        def __findBrand(self):
            if self.cardNumber[:2] in ['34', '37']:
                self.Brand = 'American Express'
            elif self.cardNumber[:3] in [
                    '300', '301', '302', '303', '304', '305'
            ]:
                self.Brand = 'Diners Club - Carte Blanche'
            elif self.cardNumber[:2] in ['36']:
                self.Brand = 'Diners Club - International'
            elif self.cardNumber[:2] in ['54']:
                self.Brand = 'Diners Club - USA & Canada'
            elif self.cardNumber[:4] in ['6011'] or self.cardNumber[0:3] in [
                    '644', '645', '646', '647', '648', '649'
            ] or self.cardNumber[0:2] in ['65'] or self.cardNumber[0:6] in [
                    str(x) for x in range(622126, 622926)
            ]:
                self.Brand = 'Discover'
            elif self.cardNumber[:3] in ['637', '638', '639']:
                self.Brand = 'InstaPayment'
            elif self.cardNumber[:4] in [str(x) for x in range(3528, 3590)]:
                self.Brand = 'JCB'
            elif self.cardNumber[:4] in [
                    '5018', '5020', '5038', '5893', '6304', '6759', '6761',
                    '6762', '6763'
            ]:
                self.Brand = 'Maestro'
            elif self.cardNumber[:2] in ['51', '52', '53', '54', '55'
                                         ] or self.cardNumber[:6] in [
                                             str(x)
                                             for x in range(222100, 272100)
                                         ]:
                self.Brand = 'MasterCard'
            elif self.cardNumber[:4] in [
                    '4026', '4508', '4844', '4913', '4917'
            ] or self.cardNumber[:6] == '417500':
                self.Brand = 'VISA Electron'
            elif self.cardNumber[0] in ['4']:
                self.Brand = 'VISA'
            else:
                self.Brand = 'Unknown Brand'

        def validate(self, number):
            """
            number: str or int credit card number
            """
            if number is None:
                return f'{Fore.RED}Not a valid Credit Card Number'
            if number is bool:
                return f'{Fore.RED}Not a valid Credit Card Number'
            if number is float:
                return f'{Fore.RED}Not a valid Credit Card Number'
            number = ''.join(x for x in str(number).strip().split())
            if number.isdigit() and 13 <= len(number) <= 19:
                # Identify Brand
                self.cardNumber = number
                self.__findBrand()
                # Luhn's Algorithm
                lastDigit = int(number[-1])
                base = [int(x) for x in reversed(number[:-1])]
                base = [x if i % 2 != 0 else 2 * x for i, x in enumerate(base)]
                base = [x if x <= 9 else x - 9 for x in base]
                base = sum(base)
                base = (base * 9) % 10
                if base == lastDigit:
                    print(Fore.GREEN)
                    return f'{Fore.GREEN}[!] {self.cardNumber} is a valid Store Card!'
                    file = open("cards.txt", "w")
                    number = repr(number)
                    file.write(number)
                    file.close()
                else:
                    print(Fore.RED)
                    return f'[!] {self.cardNumber} is not a valid Store Card!'
            else:
                return 'Not a valid Credit Card Number'

    cls()
    title()
    print(Fore.RED + " ")
    print(f" {Fore.RED}[1] {Fore.WHITE}1k Card")
    print(f" {Fore.RED}[2] {Fore.WHITE}2k Card")
    print(f" {Fore.RED}[3] {Fore.WHITE}5k Card")
    print(f" {Fore.RED}[4] {Fore.WHITE}10k Card")
    print(" ")
    print(" Which card to generate: ")
    print(" ")
    whatcard = input(f"{Fore.RED} [?] > ")
    print(" ")
    whatcard = int((whatcard))
    randomnums = "0123456789"

    if whatcard == 1:
        cls()
        title()
        print("")
        print(" [?] How Many Cards Do You Want? ")
        print(" ")
        howmany = input(f"{Fore.RED} [?] > ")
        time.sleep(0.8)
        print("           [/] Starting")
        time.sleep(0.8)
        howmany = int(howmany)

        for x in range(howmany):
            bin = "60457811425"
            ff1 = random.choice(randomnums)
            ff2 = random.choice(randomnums)
            ff3 = random.choice(randomnums)
            ff4 = random.choice(randomnums)
            ff5 = random.choice(randomnums)
            cc = str(bin) + str(ff1) + str(ff2) + str(ff3) + str(ff4) + str(
                ff5)
            print(validator().validate(int(cc)))

    if whatcard == 2:
        howmany = input(" [?] How Many Cards Do You Want? ")
        time.sleep(0.8)
        print("[/] Starting")
        time.sleep(0.8)
        howmany = int(howmany)
        for x in range(howmany):
            bin = "604578114"
            ff1 = random.choice(randomnums)
            ff2 = random.choice(randomnums)
            ff3 = random.choice(randomnums)
            ff4 = random.choice(randomnums)
            ff5 = random.choice(randomnums)
            ff6 = random.choice(randomnums)
            ff7 = random.choice(randomnums)
            cc = str(bin) + str(ff1) + str(ff2) + str(ff3) + str(ff4) + str(
                ff5) + str(ff6) + str(ff7)
            print(validator().validate(int(cc)))

    if whatcard == 3:
        howmany = input(" [?] How Many Cards Do You Want? ")
        howmany = int(howmany)
        for x in range(howmany):
            bin = "604578118"
            ff1 = random.choice(randomnums)
            ff2 = random.choice(randomnums)
            ff3 = random.choice(randomnums)
            ff4 = random.choice(randomnums)
            ff5 = random.choice(randomnums)
            ff6 = random.choice(randomnums)
            ff7 = random.choice(randomnums)
            cc = str(bin) + str(ff1) + str(ff2) + str(ff3) + str(ff4) + str(
                ff5) + str(ff6) + str(ff7)
            print(validator().validate(int(cc)))

    if whatcard == 4:
        howmany = input(" [?] How Many Cards Do You Want? ")
        time.sleep(0.8)
        print("[/] Starting")
        time.sleep(0.8)
        howmany = int(howmany)
        for x in range(howmany):
            bin = "6045781123"
            ff1 = random.choice(randomnums)
            ff2 = random.choice(randomnums)
            ff3 = random.choice(randomnums)
            ff4 = random.choice(randomnums)
            ff5 = random.choice(randomnums)
            ff6 = random.choice(randomnums)
            cc = str(bin) + str(ff1) + str(ff2) + str(ff3) + str(ff4) + str(
                ff5) + str(ff6)
            print(validator().validate(int(cc)))

elif choice == 2:
    cls()
    import os
    import ctypes
    import requests
    import random
    import string
    import time

    title()
    print(" ")

    num = int(input(' Input How Many Codes to Generate and Check: '))

    with open("Nitro Codes.txt", "w", encoding='utf-8') as file:
        print(" Your nitro codes are being generated, be patient!")

        start = time.time()

        for i in range(num):
            code = "".join(
                random.choices(string.ascii_uppercase + string.digits +
                               string.ascii_lowercase,
                               k=19))

            file.write(f"https://discord.gift/{code}\n")

        print(f" Generated {num} codes | Time taken: {time.time() - start}\n")

    with open("Nitro Codes.txt") as file:
        for line in file.readlines():
            nitro = line.strip("\n")

            url = "https://discordapp.com/api/v6/entitlements/gift-codes/" + nitro + "?with_application=false&with_subscription_plan=true"

            r = requests.get(url)

            if r.status_code == 200:
                print(f"{Fore.GREEN} Valid | {nitro} ")
                break
            else:
                print(f"{Fore.RED} Invalid | {nitro} ")

    time.sleep(0.2)

    print(" ")
    print(
        f"{Fore.WHITE} Valid codes will be in Valid Codes.txt - if there none then keep generating :)"
    )

elif choice == 5:
    cls()
    title()
    import colorama
    import random, string

    upper_letter = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lower_letter = 'abcdefghijklmnopqrstuvwxyz'
    digits = '0123456789'
    print(" ")
    amount = int(input(" Gift Code Amount : "))
    print(" ")
    print(f"{Fore.RED} All giftcodes aren't checked and are saved in netflixcodes.txt meaning you need to get a checker. ")
    print(f"{Fore.WHITE} ")
    for i in range(amount):
        code = "https://www.netflix.com/redeem/" + "".join(
            random.choices(string.ascii_uppercase + string.digits, k=11))
        print(" [GENERATED] " + code)
        giftcode = open('netflixcodes.txt', 'a')
        giftcode.write(code + "\n")

elif choice == 3:
    cls()
    title()
    import requests
    print("")
    print(" How many of them?")
    print(" ")
    nn = input(f"{Fore.RED} [?] > ")
    print(f"{Fore.WHITE}")
    n = int(nn)
    for x in range(n):
        print("")
        v = g(5) + "-" + g(5) + "-" + g(5) + "-" + g(5) + "-" + g(5)
        url = "https://microsoft.com/api/entitlements/redeem/" + v

        s = requests.get(url)

        if s == 200:
            print(f"{Fore.GREEN} Valid | {v} ")
            break
        else:
            print(f"{Fore.RED} Invalid | {v} ")
    print(" ")
    print(f"{Fore.GREEN} Done!")

elif choice == 4:
    cls()
    title()
    import requests
    print(" ")
    print(" Checked PS codes")
    print("")
    print(" How many of them?")
    print(" ")
    nn = input(f"{Fore.RED} [?] > ")
    print("")
    n = int(nn)
    for x in range(n):
        print("")
        v = (g(4) + "-" + g(4) + "-" + g(4))
        url = "https://playstation.com/api/redeem/" + v

        s = requests.get(url)

        if s == 200:
            print(f"{Fore.GREEN} Valid | {v} ")
            break
        else:
            print(f"{Fore.RED} Invalid | {v} ")

elif choice == 6:
    cls()
    title()
    #interface
    print(" ")
    print(f"{Fore.RED} JUST SO YOU KNOW THESE ARE UNCHECKED SO YOU'RE GONNA HAVE TO GO FIND A CHECKER FOR YOUR CODES")

    print(f"{Fore.WHITE}")
    print(" What Giftcard you need to generate?")

    tt = input("\n [-] Amazon\n [-] Roblox\n [-] Fortnite\n [-] Ebay\n [-] iTunes\n [-] Paypal\n [-] Visa\n [-] Playstation\n [-] Steam\n [-] Xbox\n [-] PlayStore\n [-] Minecraft\n\n Enter Name: \n [?] > ")

    t = tt.lower()
    print("")
    print(" How many of them?")
    print(" ")
    nn = input(" [?] > ")
    print("")
    n = int(nn)
    if t == "minecraft":
	    for x in range(n):
		    print("")
		    print(g(4)+"-"+g(4)+"-"+g(4))
		
    if t == "paypal":
	    for x in range(n):
		    print("")
		    print(g(4)+"-"+g(4)+"-"+g(4))
			
    if t == "amazon":
	    for x in range(n):
		    print("")
		    print(g(4)+"-"+g(6)+"-"+g(4))
		
    if t == "netflix":
	    for x in range(n):
		    print("")
		    print(g(4)+"-"+g(6)+"-"+g(4))
		
    if t == "steam":
	    for x in range(n):
		    print("")
		    print(g(4)+"-"+g(6)+"-"+g(5))
		
    if t == "fortnite":
	    for x in range(n):
		    print("")
		    print(g(5)+"-"+g(4)+"-"+g(4))
		
    if t == "roblox":
	    for x in range(n):
		    print("")
		    print(g(3)+"-"+g(3)+"-"+g(4))
		
    if t == "itunes":
	    for x in range(n):
		    print("")
		    print(g(16))
		
    if t == "ebay":
	    for x in range(n):
		    print("")
		    print(g(10))
			
    if t == "playstore":
	    for x in range(n):
		    print("")
		    print(g(4)+"-"+g(4)+"-"+g(4)+"-"+g(4)+"-"+g(4))
		
    print("")
    print("-----Generation completed-----")
    time.sleep(360)
