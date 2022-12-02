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
    def configmenu_title(self):
        titles.spicetify(self='self')
        print(f'''
        
        {tag_spicetify} {Fore.LIGHTYELLOW_EX}1. Change Color scheme (1)
        {tag_spicetify} {Fore.LIGHTYELLOW_EX}2. Overwrite assets (2)
        {tag_spicetify} {Fore.LIGHTYELLOW_EX}3. Current theme (3)
        {tag_spicetify} {Fore.LIGHTYELLOW_EX}4. Inject css (4)
        {tag_spicetify} {Fore.LIGHTYELLOW_EX}5. Replace colors (5)
        {tag_spicetify} {Fore.LIGHTYELLOW_EX}6. Config Directory (6)
        {tag_spicetify} {Fore.LIGHTRED_EX}7. Go to Main menu (7)
        
        ''')
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
    def install_title(self):
        print(f'''
        {tag_spicetify}{Fore.LIGHTYELLOW_EX} 1. Install Spicetify (1)
        {tag_spicetify}{Fore.LIGHTYELLOW_EX} 2. Install Marketplace (2)
        {tag_spicetify}{Fore.LIGHTRED_EX} 3. Go to main menu (3)
        
        ''')
    def backmenu(self):
        titles.spicetify(self='self')
        print(f"""
   {tag_spicetify}{Fore.LIGHTYELLOW_EX} 1. Install menu (1)
   {tag_spicetify}{Fore.LIGHTYELLOW_EX} 2. Apply (2)
   {tag_spicetify}{Fore.LIGHTYELLOW_EX} 3. Help (3)
   {tag_spicetify}{Fore.LIGHTYELLOW_EX} 4. Powershell Terminal (4)
   {tag_spicetify}{Fore.LIGHTYELLOW_EX} 5. Restore (5)
   {tag_spicetify}{Fore.LIGHTYELLOW_EX} 6. Backup (6)
   {tag_spicetify}{Fore.LIGHTYELLOW_EX} 7. Config menu (7)
   {tag_spicetify}{Fore.LIGHTYELLOW_EX} 8. Upgrade (8)
   {tag_spicetify}{Fore.LIGHTRED_EX} 9. Close App (9)
        
""")

class options:
    def install_opt(self):
        titles.install_title(self='self')
        installmenuchoice = input(tag_user)
        if installmenuchoice == '2':
            functions.market_placeinstall(self='self')
        if installmenuchoice == '1':
            functions.install(self='self')
        if installmenuchoice != '1' and installmenuchoice != '2':
            options.mainmenu(self='self')
    def mainmenu(self):
        titles.backmenu(self='self')
        main_choice = input(tag_user)
        if main_choice == '1':
            options.install_opt(self='self') # install function
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
        elif main_choice == '7': # Config menu
            functions.config_menu(self='self')
        elif main_choice == '8': # Upgrade
            functions.upgrade(self='self')
        elif main_choice == '9': # End Function
            options.end(self='self')
        elif main_choice != '1' and main_choice != '2' and main_choice != '3' and main_choice != '4' and main_choice != '5' and main_choice != '6' and main_choice != '7' and main_choice != '8' and main_choice != '9':
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
    def upgrade(self):
        print(f'{tag_spicetify} {Fore.WHITE}Do you really want to upgrade Spicetify? (Y/N)')
        upgrade_sure = input(tag_user)
        if upgrade_sure == 'Y' or upgrade_sure == 'y':
            subprocess.call(f'{powershell} spicetify upgrade', shell=True)
            print(f'{tag_spicetify} {Fore.LIGHTGREEN_EX}Done!')
            time.sleep(1)
            options.mainmenu(self='self')
        else:
            options.mainmenu(self='self')
    def config_menu(self):
        titles.configmenu_title(self='self')
        configmenu_sure = input(tag_user)
        with open('requirements/installed.txt', 'r') as installed1:
            installed3 = installed1.read()
            if installed3 == 'true':
                if configmenu_sure == '1': ## Color scheme
                    print(tag_spicetify,f'{Fore.WHITE}Name of the Color scheme?')
                    nameofthescheme = input(tag_user)
                    time.sleep(1)
                    print(tag_spicetify, 'Name of the scheme is', '"'+nameofthescheme+'"', 'Is this right? (Y/N)')
                    nmschm_sure = input(tag_user)
                    if nmschm_sure == 'y' or nmschm_sure == 'Y':
                        print(tag_spicetify, f'{Fore.WHITE} Rewriting...')
                        time.sleep(0.5)
                        subprocess.call(f'{powershell} spicetify config color_scheme {nameofthescheme}', shell=True)
                        for i in range(3):
                            titles.spaces(self='self')
                        subprocess.call(f'{powershell} spicetify apply', shell=True)
                        print(tag_spicetify, f'{Fore.LIGHTGREEN_EX} Done!')
                        print(tag_spicetify, f'{Fore.WHITE}Going back to main menu..')
                        options.mainmenu(self='self')
                    else:
                        functions.config_menu(self='self')
                elif configmenu_sure == '2': ## Overwrite access
                    print(tag_spicetify, f'{Fore.WHITE}Do you want to enable(Y) or disable overwrite access (N)? (Y/N)')
                    overwriteassets = input(tag_user)
                    if overwriteassets == 'y' or overwriteassets == 'Y':
                        print(tag_spicetify, f'{Fore.WHITE}You want to enable Overwrite assets, is this right? (Y/N)')
                        overwriteassets_sure = input(tag_user)
                        if overwriteassets_sure == 'Y' or overwriteassets_sure == 'y':
                            print('Rewriting overwrite to 1...')
                            time.sleep(0.5)
                            subprocess.call(f'{powershell} spicetify config overwrite_assets 1', shell=True)
                            subprocess.call(f'{powershell} spicetify apply', shell=True)
                            print(tag_spicetify, f'{Fore.LIGHTGREEN_EX}Done!')
                            print(tag_spicetify, f'{Fore.LIGHTGREEN_EX}Spicetify were reloaded!')
                            options.mainmenu(self='self')
                        else:
                            functions.config_menu(self='self')
                    if overwriteassets == 'n' or overwriteassets == 'N':
                        print(tag_spicetify, f'{Fore.WHITE}You want to disable Overwrite assets, is this right? (Y/N)')
                        overwriteassets_sure = input(tag_user)
                        if overwriteassets_sure == 'Y' or overwriteassets_sure == 'y':
                            print('Rewriting overwrite to 0...')
                            time.sleep(0.5)
                            subprocess.call(f'{powershell} spicetify config overwrite_assets 0', shell=True)
                            subprocess.call(f'{powershell} spicetify apply', shell=True)
                            print(tag_spicetify, f'{Fore.LIGHTGREEN_EX}Done!')
                            print(tag_spicetify, f'{Fore.LIGHTGREEN_EX}Spicetify were reloaded!')
                            options.mainmenu(self='self')
                        else:
                            functions.config_menu(self='self')
                elif configmenu_sure == '3': ## Theme
                    print(tag_spicetify,f'{Fore.WHITE}Name of the "Current theme"?')
                    nameofthescheme = input(tag_user)
                    time.sleep(1)
                    print(tag_spicetify, 'Name of the Current theme is', '"'+nameofthescheme+'"', 'Is this right? (Y/N)')
                    nmschm_sure = input(tag_user)
                    if nmschm_sure == 'y' or nmschm_sure == 'Y':
                        print(tag_spicetify, f'{Fore.WHITE} Rewriting...')
                        time.sleep(0.5)
                        subprocess.call(f'{powershell} spicetify config current_theme {nameofthescheme}', shell=True)
                        for i in range(3):
                            titles.spaces(self='self')
                        subprocess.call(f'{powershell} spicetify apply', shell=True)
                        print(tag_spicetify, f'{Fore.LIGHTGREEN_EX} Done!')
                        print(tag_spicetify, f'{Fore.WHITE}Going back to main menu..')
                        options.mainmenu(self='self')
                    else:
                        functions.config_menu(self='self')
                elif configmenu_sure == '4': ## Inject CSS
                    print(tag_spicetify, f'{Fore.WHITE}Do you want to enable(Y) or disable Inject css (N)? (Y/N)')
                    overwriteassets = input(tag_user)
                    if overwriteassets == 'y' or overwriteassets == 'Y':
                        print(tag_spicetify, f'{Fore.WHITE}You want to enable Inject css, is this right? (Y/N)')
                        overwriteassets_sure = input(tag_user)
                        if overwriteassets_sure == 'Y' or overwriteassets_sure == 'y':
                            print('Rewriting inject_css to 1...')
                            time.sleep(0.5)
                            subprocess.call(f'{powershell} spicetify config inject_css 1', shell=True)
                            subprocess.call(f'{powershell} spicetify apply', shell=True)
                            print(tag_spicetify, f'{Fore.LIGHTGREEN_EX}Done!')
                            print(tag_spicetify, f'{Fore.LIGHTGREEN_EX}Spicetify were reloaded!')
                            options.mainmenu(self='self')
                        else:
                            functions.config_menu(self='self')
                    elif overwriteassets == 'n' or overwriteassets == 'N':
                        print(tag_spicetify, f'{Fore.WHITE}You want to disable Inject css, is this right? (Y/N)')
                        overwriteassets_sure = input(tag_user)
                        if overwriteassets_sure == 'Y' or overwriteassets_sure == 'y':
                            print('Rewriting inject_css to 0...')
                            time.sleep(0.5)
                            subprocess.call(f'{powershell} spicetify config inject_css 0', shell=True)
                            subprocess.call(f'{powershell} spicetify apply', shell=True)
                            print(tag_spicetify, f'{Fore.LIGHTGREEN_EX}Done!')
                            print(tag_spicetify, f'{Fore.LIGHTGREEN_EX}Spicetify were reloaded!')
                            options.mainmenu(self='self')
                        else:
                            functions.config_menu(self='self')
                elif configmenu_sure == '5': ## Replace colors
                    print(tag_spicetify, f'{Fore.WHITE}Do you want to enable(Y) or disable Replace colors(N)? (Y/N)')
                    overwriteassets = input(tag_user)
                    if overwriteassets == 'y' or overwriteassets == 'Y':
                        print(tag_spicetify, f'{Fore.WHITE}You want to enable Replace colors, is this right? (Y/N)')
                        overwriteassets_sure = input(tag_user)
                        if overwriteassets_sure == 'Y' or overwriteassets_sure == 'y':
                            print('Rewriting replace_colors to 1...')
                            time.sleep(0.5)
                            subprocess.call(f'{powershell} spicetify config replace_colors 1', shell=True)
                            subprocess.call(f'{powershell} spicetify apply', shell=True)
                            print(tag_spicetify, f'{Fore.LIGHTGREEN_EX}Done!')
                            print(tag_spicetify, f'{Fore.LIGHTGREEN_EX}Spicetify were reloaded!')
                            options.mainmenu(self='self')
                        else:
                            functions.config_menu(self='self')
                    elif overwriteassets == 'n' or overwriteassets == 'N':
                        print(tag_spicetify, f'{Fore.WHITE}You want to disable Replace colors assets, is this right? (Y/N)')
                        overwriteassets_sure = input(tag_user)
                        if overwriteassets_sure == 'Y' or overwriteassets_sure == 'y':
                            print('Rewriting replace_colors to 0...')
                            time.sleep(0.5)
                            subprocess.call(f'{powershell} spicetify config replace_colors 0', shell=True)
                            subprocess.call(f'{powershell} spicetify apply', shell=True)
                            print(tag_spicetify, f'{Fore.LIGHTGREEN_EX}Done!')
                            print(tag_spicetify, f'{Fore.LIGHTGREEN_EX}Spicetify were reloaded!')
                            options.mainmenu(self='self')
                        else:
                            functions.config_menu(self='self')
                elif configmenu_sure == '6':
                    print(tag_spicetify, 'Config menu directory: ')
                    subprocess.call(f'{powershell} spicetify --config', shell=True)
                    input(f'{tag_spicetify} Press any button to go to menu.')
                    options.mainmenu(self='self')

                #### END OF CONFIG MENU STORY HERE
                if configmenu_sure != '1' and configmenu_sure != '2' and configmenu_sure != '3' and configmenu_sure != '4' and configmenu_sure != '5' and configmenu_sure != '6':
                    options.mainmenu(self='self')
                installed1.close()
            else:
                print(f'{Fore.RED}You dont have installed Spicetify!')
                options.mainmenu(self='self')

    def install(self):
        titles.spicetify(self='self')
        print(f"{tag_spicetify} {Fore.WHITE}Do you really want to install {Fore.LIGHTRED_EX}Spicetify? {Fore.BLUE}(Y/N)")
        spicetify_install = input(tag_user)
        if spicetify_install == 'y' or spicetify_install == 'Y':
            time.sleep(1)
            print(f'{tag_spicetify} Sending the command to Powershell..')
            time.sleep(0.5)
            subprocess.run(f'requirements/install.bat', stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
            print(f'{tag_spicetify}{Fore.LIGHTGREEN_EX} Done!')
            subprocess.call(f'{powershell} spicetify apply', stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
            with open('requirements/installed.txt', 'w') as f:
                f.write('true')
            options.mainmenu(self='self')
        else:
            print(tag_spicetify, 'Giving you back to the menu...')
            options.mainmenu(self='self')
    def market_placeinstall(self):
        titles.spicetify(self='self')
        with open('requirements/installed.txt', 'r') as f:
            f_installed = f.read()
        if f_installed == 'true':
            print(f'{tag_spicetify} {Fore.WHITE}Do you really want to install {Fore.LIGHTRED_EX}Spicetify marketplace? {Fore.BLUE}(Y/N)')
            marketplace_sure = input(tag_user)
            if marketplace_sure == 'Y' or marketplace_sure == 'y':
                time.sleep(0.5)
                print(f'{tag_spicetify} Sending the command to Powershell...')
                time.sleep(0.5)
                subprocess.run('requirements/spicetify_market.bat', stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
                subprocess.call(f'{powershell} spicetify apply', stdout=subprocess.PIPE, stderr=subprocess.STDOUT,shell=True)
                print(f'{Fore.LIGHTGREEN_EX}Done!')
                options.mainmenu(self='self')
            else:
                options.mainmenu(self='self')
        else:
            print(tag_spicetify, f'{Fore.RED}You need to install Spicetify first!')
    def restore(self):
        titles.spicetify(self='self')
        print(f"{tag_spicetify} {Fore.WHITE}Do you really want to {Fore.RED}restore backups from {Fore.LIGHTRED_EX}Spicetify? {Fore.BLUE}(Y/N)")
        restore1 = input(f"{tag_user} ")
        if restore1 == 'Y' or restore1 == 'y':
            print(f"{tag_spicetify} {Fore.WHITE}Do you really want to {Fore.RED}restore backups from {Fore.LIGHTRED_EX}Spicetify? {Fore.WHITE}This will remove your backups!{Fore.BLUE}(Y/N)")
            restore2 = input(f"{tag_user} ")
            if restore2 == 'y' or restore2 == 'Y':
                print(f"{Fore.LIGHTRED_EX}Restoring the spicetify backups...")
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
    def createfile(self):
        cwd = os.getcwd()
        folder = cwd+r'/requirements/'
        path = cwd+r'/requirements/installed.txt'
        marketbat = cwd+r'/requirements/spicetify_market.bat'
        marketps = cwd+r'/requirements/spicetify_market.ps1'
        installbat = cwd+r'/requirements/install.bat'
        installps = cwd+r'/requirements/install.ps1'
        ## FOLDER CREATE
        if os.path.exists(folder):
            pass
        else:
            os.mkdir(cwd+'/requirements')
        ## INSTALLED.TXT
        if os.path.exists(path):
            pass
        else:
            with open(path, 'w+') as f:
                f.write('false')
                f.close()
        ## SPICETIFY MARKET ##
        # MARKET.BAT
        if os.path.exists(marketbat):
            pass
        else:
            with open(marketbat, 'w+') as p:
                p.write('''powershell.exe -executionpolicy remotesigned -File  "spicetify_market.ps1"
taskkill /F /IM cmd.exe''')
                p.close()
        # MARKET.ps1
        if os.path.exists(marketps):
            pass
        else:
            with open(marketps, 'w+') as r:
                r.write('iwr -useb https://raw.githubusercontent.com/spicetify/spicetify-marketplace/main/resources/install.ps1 | iex')
                r.close()
        # INSTALL.BAT
        if os.path.exists(installbat):
            pass
        else:
            with open(installbat, 'w+') as g:
                g.write('''powershell.exe -executionpolicy remotesigned -File  "install.ps1"
taskkill /F /IM cmd.exe''')
        # INSTALL.PS1
        if os.path.exists(installps):
            pass
        else:
            with open(installps, 'w+') as l:
                l.write('iwr -useb https://raw.githubusercontent.com/spicetify/spicetify-cli/master/install.ps1 | iex')
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
if __name__ == '__main__':
    functions.createfile(self='self')
    options.mainmenu(self='self')