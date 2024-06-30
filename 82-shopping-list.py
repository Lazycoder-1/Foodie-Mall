# Foodie Shopping Mall
# add , remove and everything 
# use of mutable data types 

main_cart = []
def show_menu():
    print('Welcome To Foodie Mall ')
    print('Enter items you want to add to your shopping list')
    print('Press DONE to complete your order')
    print('Press REMOVE to remove an item from the cart')
    print('Press SHOW to display your shopping list')
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
    if main_cart == []:
        print('You do not have anything in your list')
    else:
        print('This is your shopping list')
        for item in main_cart:
            print(item)

# main logic for the application
show_menu()
while True:
    user_input = input(' >  ')
    if user_input == 'DONE':
        show_menu()
        print('Thanks for shopping with Foodie Mall ')
        break
    elif user_input == 'HELP':
        show_menu()
        print('Type to add an item to your shopping list')
        continue
    elif user_input == 'SHOW':
        #show_menu()
        display_items()
    elif user_input == 'REMOVE':
        display_items()
        item_remove = input('Enter item to remove: ')
        show_menu()
        remove_from_cart(item_remove)
        continue
    else:
        show_menu()
        add_to_cart(user_input)

display_items()


# show_menu()
# add_to_cart('mango')
# remove_from_cart()
# add_to_cart('guava')
# add_to_cart('apples')
# display_items()








