# Foodie Shopping Mall
# add , remove and everything 
# use of mutable data types 

main_cart = []
def show_menu():
    print('Welcome To Foodie Mall ')
    print('Enter items you want to add to your shopping list')
    print('Press DONE to complete your order')
    print('Press REMOVE to remove an item from the cart')
    print('Press HELP for assistance')
    print('-------------------------')

def add_to_cart(item):
    item = item.capitalize()
    if item not in main_cart:
        main_cart.append(item)
        print('You have added {} to your cart'.format(item))
        print('You have {} item(s) in your cart'.format(len(main_cart)))
    else:
        print('You have that item in your cart already')

def remove_from_cart(item):
    item = item.capitalize()
    if item in main_cart:
        main_cart.remove(item)
        print('{} was removed from your cart'.format(item))
        print('You have {} item(s) in your cart'.format(len(main_cart)))
    else:
        print('Please you do not have that item in your cart')

def display_items():
    print('This is your shopping list')
    for item in main_cart:
        print(item)

show_menu()
add_to_cart('mango')
#remove_from_cart()
add_to_cart('guava')
add_to_cart('apples')
display_items()


#print(main_cart)






