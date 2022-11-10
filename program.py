import subprocess
import colorama
from colorama import Style, Fore
import time
import os
os.system('cls')
colorama.init()

## TAGS ##

tag_spicetify = f'{Fore.BLUE}[{Fore.LIGHTRED_EX}SPICETIFY{Fore.BLUE}]{Style.RESET_ALL}'
tag_user = f'{Fore.LIGHTYELLOW_EX}[{Fore.LIGHTGREEN_EX}USER{Fore.LIGHTYELLOW_EX}] {Style.RESET_ALL}'
tag_powershell = f'{Fore.LIGHTRED_EX}[{Fore.LIGHTBLUE_EX}POWERSHELL{Fore.LIGHTRED_EX}]'

## TAGS ##

## Powershell

powershell = r'C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe'

## Powershell


class titles:
    def spicetify(self):
        print(f"""{Fore.LIGHTRED_EX}


   _____ ____  _________________________________  __
  / ___// __ \/  _/ ____/ ____/_  __/  _/ ____| \/ /
  \__ \/ /_/ // // /   / __/   / /  / // /_    \  / 
 ___/ / ____// // /___/ /___  / / _/ // __/    / /  
/____/_/   /___/\____/_____/ /_/ /___/_/      /_/   
                                                    
    {Fore.LIGHTBLUE_EX}Github: github.com/DarkmayGOD


{Style.RESET_ALL}
""")
    def spaces(self):
        print("""
        
        
        """)
    def powershell_title(self):
        print(f"""{Fore.LIGHTYELLOW_EX}
        
        If you want to close the Powershell terminal, just please type:
        
        - exit / EXIT
        - close / CLOSE
        - exit / EXIT
        
        """)
    def backmenu(self):
        titles.spicetify(self='self')
        print(f"""
   {tag_spicetify}{Fore.LIGHTYELLOW_EX} 1. Install (1)
   {tag_spicetify}{Fore.LIGHTYELLOW_EX} 2. Apply (2)
   {tag_spicetify}{Fore.LIGHTYELLOW_EX} 3. Help (3)
   {tag_spicetify}{Fore.LIGHTYELLOW_EX} 4. Powershell Tool (4)
   {tag_spicetify}{Fore.LIGHTYELLOW_EX} 5. Restore (5)
   {tag_spicetify}{Fore.LIGHTYELLOW_EX} 6. Backup (6)
   {tag_spicetify}{Fore.LIGHTRED_EX} 5. Close App (7)
        
""")

class options:
    def mainmenu(self):
        titles.backmenu(self='self')
        main_choice = input(tag_user)
        if main_choice == '1':
            functions.install(self='self') # install function
        elif main_choice == '2':
            functions.apply(self='self') # Apply Function
        elif main_choice == '3':
            functions.help(self='self') # Help function
        elif main_choice == '4':
            functions.powershelltool(self='self') # Powershell Tool Function
        elif main_choice == '5':
            functions.restore(self='self') # Restore Function
        elif main_choice == '6':
            functions.backup(self='self') # Backup Function
        elif main_choice == '7': # End Function
            options.end(self='self')
        elif main_choice != '1' and main_choice != '2' and main_choice != '3' and main_choice != '4' and main_choice != '5' and main_choice != '6' and main_choice != '7':
            options.mainmenu(self='self')
    def end(self):
        titles.spicetify(self='self')
        print(f'{tag_spicetify} {Fore.LIGHTRED_EX}Are you really sure about closing the app? (Y/N)')
        end_sure = input(tag_user)
        if end_sure == 'Y' or end_sure == 'y':
            print(f'{tag_spicetify} {Fore.GREEN}Closing the app in...')
            for i in range(1, 4):
                print(f'{tag_spicetify} {Fore.RED}{i}')
                time.sleep(1)
            print(f'{tag_spicetify} {Fore.GREEN}Closing...')
        elif end_sure != 'Y' or 'y':
            options.mainmenu(self='self')
class functions:
    def install(self):
        titles.spicetify(self='self')
        print(f"{tag_spicetify} {Fore.WHITE}Do you really want to install {Fore.LIGHTRED_EX}Spicetify? {Fore.BLUE}(Y/N)")
        spicetify_install = input(tag_user)
        if spicetify_install == 'y' or spicetify_install == 'Y':
            time.sleep(1)
            print(f'{tag_spicetify} Sending the command to Powershell..)')
            time.sleep(0.5)
            subprocess.run(f'start install.bat', stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
            print('Done!')
            options.mainmenu(self='self')
        else:
            print(tag_spicetify, 'Giving you back to the menu...')
            options.mainmenu(self='self')
    def restore(self):
        titles.spicetify(self='self')
        print(f"{tag_spicetify} {Fore.WHITE}Do you really want to {Fore.RED}restore backups from {Fore.LIGHTRED_EX}Spicetify? {Fore.BLUE}(Y/N)")
        restore1 = input(f"{tag_user} ")
        if restore1 == 'Y' or restore1 == 'y':
            print(f"{tag_spicetify} {Fore.WHITE}Do you really want to {Fore.RED}restore backups from {Fore.LIGHTRED_EX}Spicetify? {Fore.WHITE}This will remove your backups!{Fore.BLUE}(Y/N)")
            restore2 = input(f"{tag_user} ")
            if restore2 == 'y' or restore2 == 'Y':
                print(f"{Fore.LIGHTRED_EX}Okay.. Uninstalling the Spicetify.. Goodbye :(")
                time.sleep(1.5)
                subprocess.call(f'{powershell} spicetify restore', shell=True)
                time.sleep(2)
                print(tag_spicetify, 'Going to main menu...')
                options.mainmenu(self='self')
            else:
                options.mainmenu(self='self')
        else:
            options.mainmenu(self='self')
    def backup(self):
        titles.spicetify(self='self')
        print(f"{tag_spicetify} {Fore.WHITE}Do you really want to make {Fore.LIGHTRED_EX}Back up? {Fore.BLUE}(Y/N)")
        backup_sure = input(f'{tag_user} ')
        if backup_sure == 'Y' or backup_sure == 'y':
            print('Making the backup...')
            subprocess.call(f'{powershell} spicetify backup', shell=True)
            time.sleep(2)
            print(tag_spicetify, 'Going to main menu...')
            options.mainmenu(self='self')
        else:
            options.mainmenu(self='self')
    def apply(self):
        titles.spicetify(self='self')
        print(f"{tag_spicetify} {Fore.WHITE}Do you really want to apply changes? {Fore.BLUE}(Y/N)")
        changes_sure = input(tag_user)
        if changes_sure == 'Y' or changes_sure == 'y':
            subprocess.call(f'{powershell} spicetify apply', shell=True)
            time.sleep(2)
            print(tag_spicetify, 'Going to main menu...')
            options.mainmenu(self='self')
        else:
            print(tag_spicetify, 'Going back to main menu..')
            options.mainmenu(self='self')
    def help(self):
        titles.spicetify(self='self')
        print(f'{tag_spicetify} Printing the help commands..')
        time.sleep(2)
        subprocess.call(f'{powershell} spicetify -h', shell=True)
        titles.spaces(self='self')
        print(tag_spicetify, 'Press ENTER to go to menu')
        input(tag_user)
        options.mainmenu(self='self')
    def powershelltool(self):
        titles.powershell_title(self='self')
        print(f"{tag_spicetify} {Fore.WHITE}Do you understand and you want to continue? {Fore.BLUE}(Y/N)")
        powershell_sure = input(tag_user)
        if powershell_sure == 'Y' or 'y':
            while True:
                powershelltool = input(tag_powershell)
                print(tag_spicetify + 'Sending the command to Powershell..')
                time.sleep(1)
                subprocess.call(f'{powershell} {powershelltool}', shell=True)
                if powershelltool == 'exit' or powershelltool == 'EXIT' or powershelltool == 'close' or powershelltool == 'CLOSE' or powershelltool == 'close' or powershelltool == 'menu'or powershelltool == 'MENU':
                    options.mainmenu(self='self')
                    break
        else:
            options.mainmenu(self='self')
##APP

options.mainmenu(self='self')