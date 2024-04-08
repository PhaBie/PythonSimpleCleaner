import os
import colorama
from colorama import Fore, Back, Style
import webbrowser
from time import sleep
import shutil
import getpass

clear = lambda: os.system('cls')
clear()

print(Fore.RED + " ██████╗ ██╗  ██╗ █████╗ ██████╗ ██╗███████╗    ███████╗██╗   ██╗███████╗████████╗███████╗███╗   ███╗ ")
print(Fore.GREEN + " ██╔══██╗██║  ██║██╔══██╗██╔══██╗██║██╔════╝    ██╔════╝╚██╗ ██╔╝██╔════╝╚══██╔══╝██╔════╝████╗ ████║ ")
print(Fore.YELLOW + " ██████╔╝███████║███████║██████╔╝██║█████╗      ███████╗ ╚████╔╝ ███████╗   ██║   █████╗  ██╔████╔██║ ")
print(Fore.CYAN + " ██╔═══╝ ██╔══██║██╔══██║██╔══██╗██║██╔══╝      ╚════██║  ╚██╔╝  ╚════██║   ██║   ██╔══╝  ██║╚██╔╝██║ ")
print(Fore.RED + " ██║     ██║  ██║██║  ██║██████╔╝██║███████╗    ███████║   ██║   ███████║   ██║   ███████╗██║ ╚═╝ ██║ ")
print(Fore.CYAN + " ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝ ╚═╝╚══════╝    ╚══════╝   ╚═╝   ╚══════╝   ╚═╝   ╚══════╝╚═╝     ╚═╝ ")       
print(Fore.GREEN + "                                                                                                      ") 

while True:

    print(Fore.RED + " ██████╗ ██╗  ██╗ █████╗ ██████╗ ██╗███████╗    ███████╗██╗   ██╗███████╗████████╗███████╗███╗   ███╗ ")
    print(Fore.GREEN + " ██╔══██╗██║  ██║██╔══██╗██╔══██╗██║██╔════╝    ██╔════╝╚██╗ ██╔╝██╔════╝╚══██╔══╝██╔════╝████╗ ████║ ")
    print(Fore.LIGHTYELLOW_EX + " ██████╔╝███████║███████║██████╔╝██║█████╗      ███████╗ ╚████╔╝ ███████╗   ██║   █████╗  ██╔████╔██║ ")
    print(Fore.CYAN + " ██╔═══╝ ██╔══██║██╔══██║██╔══██╗██║██╔══╝      ╚════██║  ╚██╔╝  ╚════██║   ██║   ██╔══╝  ██║╚██╔╝██║ ")
    print(Fore.RED + " ██║     ██║  ██║██║  ██║██████╔╝██║███████╗    ███████║   ██║   ███████║   ██║   ███████╗██║ ╚═╝ ██║ ")
    print(Fore.CYAN + " ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝ ╚═╝╚══════╝    ╚══════╝   ╚═╝   ╚══════╝   ╚═╝   ╚══════╝╚═╝     ╚═╝ ")       
    print(Fore.GREEN + "                                                                                                      ") 

    user = os.getlogin()

    print('#'*43)
    print('#', ' '*39, '#')
    print('#',' '*9,'Welcome Mr. ',user,' '*10,'#',)
    print('#', ' '*39, '#')
    print('#'*43)

    print("1.Clean temporary file")
    print("2.Auto Open Browser")
    print("3.All In One")
    print("4.End Program")

    choose = int(input('Enter Option what you want: '))

    if choose == 1:
        folders = [
                f'C:\\Windows\\Temp',
                f'C:\\Users\\{user}\\AppData\\Local\\Cache',
                f'C:\\Users\\{user}\\AppData\\Local\\Temp',
                'C:\\$RECYCLE.BIN',
                f'C:\\Users\\{user}\\AppData\\Roaming\\discord\\Code Cache',
                f'C:\\Users\\{user}\\AppData\\Roaming\\discord\\Cache',
                f'C:\\Users\\{user}\\AppData\\Roaming\\discord\\GPUCache',
            ]

        for folder in folders:
            for filename in os.listdir(folder):
                file_path = os.path.join(folder, filename)

                try:
                    if os.path.isfile(file_path) or os.path.islink(file_path):
                        os.unlink(file_path)

                        print(f"Delete: {filename}")
                    elif os.path.isdir(file_path):
                         shutil.rmtree(file_path)
                except Exception as e:
                    message = 'Failed to delete %s. Reason: %s' % (file_path, e)
        print(Fore.YELLOW + 'Success clean all temp file')

    elif choose == 2:
        webbrowser.get('windows-default').open_new_tab('https://www.youtube.com/')
        webbrowser.get('windows-default').open_new_tab('https://www.facebook.com/')
        webbrowser.get('windows-default').open_new_tab('https://www.instagram.com/')

    elif choose == 3:

        folders = [
                f'C:\\Windows\\Temp',
                f'C:\\Windows\\Prefetch',
                f'C:\\Users\\{user}\\AppData\\Local\\Cache',
                f'C:\\Users\\{user}\\AppData\\Local\\Temp',
                'C:\\$RECYCLE.BIN',
                f'C:\\Users\\{user}\\AppData\\Roaming\\discord\\Code Cache',
                f'C:\\Users\\{user}\\AppData\\Roaming\\discord\\Cache',
                f'C:\\Users\\{user}\\AppData\\Roaming\\discord\\GPUCache',
            ]

        for folder in folders:
            for filename in os.listdir(folder):
                file_path = os.path.join(folder, filename)

                try:
                    if os.path.isfile(file_path) or os.path.islink(file_path):
                        os.unlink(file_path)

                        print(f"Delete: {filename}")
                    elif os.path.isdir(file_path):
                         shutil.rmtree(file_path)
                except Exception as e:
                    message = 'Failed to delete %s. Reason: %s' % (file_path, e)
        print(Fore.YELLOW + 'Success clean all temp file')
        sleep(3)
        webbrowser.get('windows-default').open_new_tab('https://www.youtube.com/')
        webbrowser.get('windows-default').open_new_tab('https://www.facebook.com/')
        webbrowser.get('windows-default').open_new_tab('https://www.instagram.com/')
        

    elif choose == 4:
        break


    sleep(2)
    print('Success!!')
    sleep(1)
    print('Please Wait!!!')
    sleep(4)

    clear = lambda: os.system('cls')
    clear()