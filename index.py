from functions.menu import get_menu
from functions.order import order
from functions.check_user_action import check_user_action
from functions.print_functions.print_basket import print_order
from functions.print_functions.print_check import print_check


def main():  
    print()
    print ("Welcome to the pizzeria \nMENU:\n")
    
    menu = get_menu() 
    order_list = {}
    
    while True:
        action = check_user_action()
        
        if action == "":
            order(menu, order_list)
        elif action == "1":
            print_order(menu, order_list)
        elif action == "2":
            print_check(menu, order_list)

    
main()


    

    

    
    
    