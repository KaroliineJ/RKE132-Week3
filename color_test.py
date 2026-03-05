from colorama import Fore, Style

""" color = input("Sisesta oma lemmikvärv:").lower() 

if color == "punane":
    print("Sa oled energiline inimene")
elif color == "roosa":
    print("Sa oled romantik!")
elif color == "roheline":
    print("Sa oled rahulik inimene!")
elif color == "sinine":
    print("Sa oled keskendunud inimene!")
else:
    print("Sa oled imeline ükssarvik") """



color = input("Sisesta värv: ")
match color: 
    case "punane":
        print(Fore.RED + "Sa oled energiline inimene!" + Style.RESET_ALL)
    case "roosa":
        print(Fore.MAGENTA + "Sa oled romantik!" + Style.RESET_ALL)
    case "roheline":
        print(Fore.GREEN + "Sa oled rahulik inimene!" + Style.RESET_ALL)    
    case "sinine":
        print(Fore.BLUE + "Sa oled keskendunud inimene!" + Style.RESET_ALL)   
    case _:
        print(Fore.CYAN + "Sa oled imeline ükssarvik!" + Style.RESET_ALL)  