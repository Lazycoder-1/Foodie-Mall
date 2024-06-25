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
        print('You have {} items in your cart'.format(len(main_cart)))
    else:
        print('You have that item in your cart already')

def remove_from_cart(item):
    item = item.capitalize()
    if item in main_cart:
        main_cart.remove(item)
        print('You have that item already in your in cart')
        print('You have {} items in your cart'.format(len(main_cart)))
    else:
        print('Please you do not have that item in your cart')

show_menu()
add_to_cart('mango')
#remove_from_cart('mango')
print(main_cart)






