def print_order(menu, order_list):
    if order_list:
        print("\n--------BASKET--------")
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
                    space = 30 - (len(str(product_id)) + len(items[product_id]["name"]) + len(str(quantity)))
                    print(f"  {items[product_id]['name']}:{space * '.'}{quantity} pcs")
                print()
    else: 
        print("Basket is empty")
        
                