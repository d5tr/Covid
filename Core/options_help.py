from Core.colors import *

class Optionshelp :

    def __init__(self, target='             ', port='5555       ', payload='adb_payload.sh'):

        self.target = target
        self.port = port
        self.payload = payload

    def option_adb(self):
        
        print(f'''
        
        Name          Current Setting       Required      Description
        -------       ----------------      ---------     -----------    
        target        {self.target}         {Green}Yes{White}           Target IPv4 
        port          {self.port}           No            Exploit port (default: 5555)
        payload       {self.payload}        No            path payload to upload (default: adb_payload.sh) using this payload i make it  

        ''')
    

    def help(self):

        print('''
        commands:
        
            help                         print this message
            set <name>   <options>       set options
            show options                 see options 
            set target <target>          set target to attack
            set payload <path>           set payload to use for attack 
            set port <port>              set port to attack
            run                          start attack
            banner                       print the banner
            clear                        clear screen
            exit                         exit tool
        
        ''')