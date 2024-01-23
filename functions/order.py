from functions.check_user_action import check_user_action

def order(menu, order_list):
    
    while True:
        code = 0
        quantity = 0
        # Cycle for get code
        while True:
            # Status error when entering values
            isError = False
            code = input("Enter product code: ") 
            
            # Check the value of ${code} for a number
            if code.isdigit() and int(code) > 100:
                # Check for ${code} in the menu
                for items in menu.values(): 
                    if int(code) in items.keys():
                        isError = True
                        break
                    
            # if ${code} not number or not in the menu
            if not isError: 
                print("ERROR: enter correct code")
            else:
                break
            
        # Cycle for get quantity
        while True:
            quantity = input("Enter the quantity of the product: ")
            
            # Check the value of ${quantity} for a number
            if quantity.isdigit():
                break
            else:
                print("ERROR: enter correct quantity")
                
        # Сheck the order for the product in the order list 
        if int(code) in order_list:
            # if product already one, add the quantity
            order_list[int(code)] += int(quantity)
        else: 
            order_list[int(code)] = int(quantity)
            
        return order_list      
