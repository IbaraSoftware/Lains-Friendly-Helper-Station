'''
Lain's Friendly Helper Station
            by rav3ndust
A friendly application for helping new users configure their Arch setups. 
   This app will help users: 
   - update their systems
   - install new packages
   - access the AUR
   - ...and more
'''
import PySimpleGUI as gui 
import os as sh
# vars 
HELPER = "Lain's Friendly Helper Station"
SYSTEM_INFO_COMM = "uname -a"
UPDATE_COMM = "sudo pacman -Syu" 
UPDATE_OPT = "Update my system!"
SEARCH_OPT = "Search for packages." 
AUR_OPT = "Enable the Arch User Repository (AUR)"
EXIT_OPT = "Exit" 
# gui theming
gui.theme('Dark')
# button functionality 
def updateButton():
    updating = "Updating system..."
    updatesDone = "System updated."
    notif = "notify-send 'Lains Friendly Helper Station' 'Update Finished.'"
    print(updating)
    sh.system(f'{UPDATE_COMM}')
    sh.system(f'{notif}')
    print(updatesDone)
def pkgSearch():
    choice = "What would you like to search for?"
    insert = "Please type your search request here: "
    results = "Search results displayed above."
    print(choice)
    search_req = input(insert)
    print(f'Searching for {search_req}...')
    sh.system(f'pacman -Ss {search_req}')
    print(results)
def enableAUR():
    aur1 = "Enabling the Arch User Repository..."
    getYay = "git clone https://aur.archlinux.org/yay.git"
    yayInst = "Yay AUR Helper installed. You can now search for and install packages from the AUR."
    print(aur1)
    sh.system(f'{getYay}')
    print(yayInst)
def exitWindow():
    exiting = "Exiting the program..."
    window.close()        
# window layout and functionality
winLayout = [
    [gui.Text(f'{HELPER}')],
    [gui.Text("Your friendly helper app to get things done on your system.")],
    [gui.Button(f'{UPDATE_OPT}'), gui.Button(f'{SEARCH_OPT}'), gui.Button(f'{AUR_OPT}'), gui.Button(f'{EXIT_OPT}')]
]
window = gui.Window(f'{HELPER}', winLayout)
while True: 
    event, values = window.read()
    if event == gui.WIN_CLOSED:
        break
    elif event == f'{UPDATE_OPT}':
        updateButton()
    elif event == f'{SEARCH_OPT}':
        pkgSearch()
    elif event == f'{AUR_OPT}':
        enableAUR()
    else event == f'{EXIT_OPT}':
        exitWindow()
window.close()
