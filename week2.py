def run():
    
    my_cart = {}
    selections = {'add', 'remove', 'show','quit'}
    
    while True:
        selection = input('add/remove/show/quit')
        if selection == 'add':
            adding(my_cart)
        elif selection == 'remove':
            removing(my_cart)
        elif selection == 'show':
            showing(my_cart)
        elif selection == 'quit':
            break
        while selection not in selections:
            selection = input('Try again. add/remove/show/quit')
            
def adding():
    fruit = input("What will you add to your cart?")
    if fruit not in my_cart:
        my_cart[fruit] = {' '}
    
def removing():
    fruit = input("What will you remove from your cart?")
    if fruit in my_cart:
        del fruit
        print(f"{fruit} has been removed.")
    else:
        print(f"You dont have any {fruit}s.")
        
def showing():
    for fruit in my_cart.items():
        print(f'{fruit}')
        
        
##I know I have close to the right structure of how to set this problem up 
##but I dont understand why I can't connect functions.
##TypeError says adding(), removing(), and showing() take 0 positional arguments but 1 was given. 
##Not sure where that TypeError message leads me
##I assume I'm incorrectly calling my sub-functions in my run() function.