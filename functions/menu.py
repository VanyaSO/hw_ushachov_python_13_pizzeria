def get_menu():

    # Create menu
    menu = {    
        "pizza" : {
            101 : {"name": "Supreme Delight", "price": 10},
            102 : {"name": "Margherita Eleganza", "price": 12},
            103: {"name": "BBQ Bliss", "price": 17},
            104: {"name": "Mediterranean Marvel", "price": 15}
        },
                
        "drinks": {
            201: {"name": "Coca cola", "price": 4},
            202: {"name": "Sprite", "price": 2},
            203: { "name": "Fanta", "price": 1.5}
        }
    }

    # Print category and add opportunity to use items in category
    for category, items in menu.items(): 
        print(f"{category.capitalize()}")
        
        # Cycle for item in category
        for id, product in items.items():
            space = 30 - (len(str(id)) + len(product["name"]) + len(str(product["price"])))
            print(f" {product["name"]}:{space * '.'}{product["price"]}$...id {id}")
            
        
            
        print()
        
    return menu

