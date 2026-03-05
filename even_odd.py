#modulus (%)
n = int(input("Sisesta täisarv: "))

# if n % 2 == 0:
#     print("Arv on paaris")
# else:
#     print("Arv on paaritu")

#termary operator
# print("Arv on paaris" if n % 2 == 0 else "Arv on paaritu")

from colorama import Fore, Style, init
init()
match n % 2:
    case 0:
        print(Fore.BLUE + "Arv on paaris" + Style.RESET_ALL)
    case _:
        print(Fore.RED + "Arv on paaritu" + Style.RESET_ALL)