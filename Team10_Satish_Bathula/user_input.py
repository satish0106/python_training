
def choice(option, conf_dictionary):
    try:
        print("1)ONBOOT  2)BOOTPROTO  3)DEFEROUTE  4)IPADDR  5)PREFIX  6)Exit")
        if option==1:
            print("ONBOOT selected")
            conf_dictionary['onboot'] = input('Enter value:')
        elif option==2:
            print("BOOTPROTO selected")
            conf_dictionary['bootproto'] = input('Enter value:')
        elif option==3:
            print("DEFEROUTE selected")
            conf_dictionary['deferoute'] = input('Enter value:')
        elif option==4:
            print("IPADDR selected")
            conf_dictionary['ipaddr'] = input('Enter value:')
        elif option==5:
            print("PREFIX selected")
            conf_dictionary['prefix'] = input('Enter value:')
        elif option==6:
            print("Exited")
            temp=False
        else:
            raise ValueError
    except ValueError:
        print("Please enter valid option.")
        option = input('Your option: ')
        choice(option, conf_dictionary)