from colorama import Fore, Style
from termcolor import colored
from selenium import webdriver
import os
import getpass
import pyfiglet
import requests
import threading
import time
os.system("clear")


correct_password = "Lashen Masr"

password = getpass.getpass("Enter password: ")

if password == correct_password:
    text = "Lashen Masr"
    big_text = pyfiglet.figlet_format(text, font="big")
    yellow_big_text = colored(big_text, "yellow")

    print(yellow_big_text)
    
    text = "----------------------------------------"
    green_text = colored(text, "green")

    print(green_text.ljust(30))
    
    text = "Welcome My Friend"
    magenta_text = colored(text, "magenta")

    print(magenta_text.ljust(30))
    text = "----------------------------------------"
    green_text = colored(text, "green")

    print(green_text.ljust(30))
    print("                      ")
    getpass.getpass("Press Enter to continue...")
    os.system("clear")
else:
    print("Incorrect password entered!")
    
    
os.system("clear")

text = "WhatsApp  Ban"
big_text = pyfiglet.figlet_format(text, font="big")
yellow_big_text = colored(big_text, "yellow")

print(yellow_big_text)

text = "Made By Lashen Masr"
magenta_text = colored(text, "magenta")

print(magenta_text.ljust(30))

text = "------------------------------------------------------------------------"
green_text = colored(text, "green")

print(green_text.ljust(30))

text = "Subscribe to the YouTube channel: https://youtube.com/@lashen_masr"
red_text = colored(text, "red")

print(red_text.ljust(30))

text = "------------------------------------------------------------------------"
green_text = colored(text, "green")

print(green_text.ljust(30))



text = "whatsap : +201508327066"
cyan_text = colored(text, "cyan")

print(cyan_text.ljust(30))
text = "telegram : @lashenmasrr"
cyan_text = colored(text, "cyan")

print(cyan_text.ljust(30))
text = "Facebook : Lashen Android"
cyan_text = colored(text, "cyan")

print(cyan_text.ljust(30))

text = "Instagram : lashen.masr"
cyan_text = colored(text, "cyan")

print(cyan_text.ljust(30))
text = "Gmail : lashenmasrr@gmail.com"
cyan_text = colored(text, "cyan")

print(cyan_text.ljust(30))

text = "----------------------------------------"
green_text = colored(text, "green")

print(green_text.ljust(30))

text = "example: https://wa.me/+201012345678"
red_text = colored(text, "red")

print(red_text.ljust(30))

print("                ")


url_text = input(Fore.YELLOW + "Enter the number link to ban: " + Style.RESET_ALL)
num_requests = int(input(Fore.YELLOW + "Enter the number of reports: " + Style.RESET_ALL))
num_threads = 100


def send_request():
    while True:
        response = requests.get(url_text)
        if response.status_code == 200:
          text = "The repot has been sent to the target number by Lashen Masr"
          red_text = colored(text, "red")   
          print(red_text.ljust(30))

threads = []
start_time = time.time()
for i in range(num_threads):
    t = threading.Thread(target=send_request)
    threads.append(t)
    t.start()
    
for t in threads:
    t.join()

end_time = time.time()
total_time = end_time - start_time
requests_per_second = num_threads / total_time
print(f"{requests_per_second} requests per second")

