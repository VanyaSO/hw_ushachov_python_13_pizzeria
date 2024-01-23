def print_check(menu, order_list):
    pizza_amount = 0
    drinks_amount = 0
    drinks_sum = 0
    discount = 0
    total_sum = 0
    
    if order_list:
        print("\n--------CHECK--------")  
        for category, items in menu.items(): 
            # Items in category
            isItemsCategory = False
            
            # Check order item in menu
            for product_id in items.keys():
                if product_id in order_list:
                    isItemsCategory = True
                    break
                    
            if isItemsCategory:
                print(f" {category.capitalize()}")
            
                
                
                # Print products with order_list
                for product_id, quantity in order_list.items():
                    if product_id in items:
                        price = items[product_id]["price"]

                        space = 30 - (len(str(product_id)) + len(items[product_id]['name']) + len(str(quantity)))
                        print(f"  {items[product_id]["name"]}:{space * '.'}{price}$ x {quantity}pcs = {price * quantity}$")
                        
                        if category == "pizza":
                            i = 1
                            while i <= quantity:
                                pizza_amount += 1
                                
                                if pizza_amount % 5 == 0:
                                    discount += price                  
                                i += 1
                        elif category == "drinks":
                            
                            i = 1
                            while i <= quantity:
                                if price > 2:
                                    drinks_amount += 1
                                i += 1
                            drinks_sum += price * quantity
                                
                        total_sum += quantity * price
                        
        
        
        if total_sum > 50:
            total_sum -= total_sum * (20 / 100)
        
        if drinks_amount > 3:
            discount +=  drinks_sum * (15 / 100)
           
        total_sum -= discount
        print(f'Total sum: {total_sum}$')
                            
    else: 
        print("Check is empty")