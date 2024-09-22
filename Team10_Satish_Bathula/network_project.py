import json
import platform
import subprocess
import os
from user_input import choice

def netinfo():
    #read the ifcfg.conf file
    input_conf_file="ifcfg.conf"
    open_file=open(input_conf_file,mode='r').read()
    print(open_file)
    
    #initialize the dictionary
    conf_dictionary={}
    for item in open_file.strip().splitlines():
        if "=" in item:
            key,value=item.split("=",1)
            conf_dictionary[key.strip()]=value.strip()
    print(conf_dictionary)    

    #modify the dictionary
    if "onboot" in conf_dictionary:
        conf_dictionary['onboot']='yes'   
    if "bootproto" in conf_dictionary:
        conf_dictionary['bootproto']="static" 
    if "deferoute" in conf_dictionary:
        conf_dictionary["deferoute"]='no'  
    print(conf_dictionary)   
    #add new item
    conf_dictionary["ipaddr"]=input("Enter the IP Address: ")
    conf_dictionary['prefix']=input("Enter the Subnet Number")
    print(conf_dictionary)   

    selection(conf_dictionary)

    #write to the net_ifcfg.config
    update_conf_file="net_ifcfg.config"
    update_conf=open(update_conf_file,'w')
    for keys,values in conf_dictionary.items():
        update_conf.write(f"{keys} = {values}\n")
    print(update_conf)

    #write to the net_ifcfg.json
    j=json.dumps(conf_dictionary)
    js_file=open("net_ifcfg.json",mode='w').write(j)
    print(js_file)
    
    #determine the operating system
    os_name=platform.system().lower()
    print(os_name)
    
    netinfo ={}
    if os_name.startswith('linux'):
        os_key='linux'
        commands=['ifconfig','netstat','nmcli genral']
    elif os_name.startswith('windows'):
        os_key='windows'
        commands=['powershell Get-NetRoute','powershell Get-NetIpAddress']
    elif os_name.startswith('darwin'):
        os_key='macos'
        commands=['ifconfig','networksetup -getinfo wi-fi']    
    else:
        print("Unsupported os")
        return        
    
    #Excute commands and append results to the dictionary
    command_results=[]
    for comm in commands:
        try:
            result=subprocess.run(comm,shell=True,capture_output=True,text=True)
            command_results.append(result.stdout)
        except Exception as exception:
            command_results.append(str(exception))  


    #add results to the netinfo dictionary
    netinfo[os_key]=command_results

    #append the netinfo dictionary to the existing net_ifcfg.json file
    jsload=open("net_ifcfg.json",'r')
    existing_data=json.load(jsload)

    existing_data['netinfo']=netinfo      

    jsresult=open("net_ifcfg.json",'w')
    json.dump(existing_data,jsresult,indent=4)    


def selection(conf_dictionary):
    print("Please select a option from below")
    print("1)ONBOOT  2)BOOTPROTO  3)DEFEROUTE  4)IPADDR  5)PREFIX")
    option = int(input("Your option: "))
    choice(option, conf_dictionary)
if __name__ == "__main__":
    netinfo()