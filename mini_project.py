#Mini-Project

drinks = ['Coca-cola', '7Up', 'Fanta']

def drinks_index():
  for x in drinks:
    print(f'{((drinks.index(x)) + 1)}. {x}')

while True:

  print('\nWelcome\nEnter 0 to Exit App\nEnter 1 for Product Menu')
  enter = int(input('Enter: '))

  while enter != 0 and enter != 1:
      print('\nPlease Enter 0/1')
      enter = int(input('Enter: '))

  if enter == 0:
    print('\nExit, Thank You')
    break
  elif enter == 1:
    while True: 
      print('\nProduct Menu - Choose an Option:\n0. Return to Main Menu\n1. Product List\n2. Create New Product\n3. Update Product\n4. Delete a Product')
      user_input = int(input('Enter: '))
      
      while user_input != 0 and user_input != 1 and user_input != 2 and user_input != 3 and user_input != 4:
        print('Enter Number from the List')
        user_input = int(input())
  
      if user_input == 0:
        break
  
      elif user_input == 1:
        print('\nDrinks List:')
        drinks_index()
        cstmr_drink = input('\nChoose your Drink:\n')
        while str(cstmr_drink) not in drinks:
          print('Choose a Drink from the List:')
          cstmr_drink = str(input())
        print(f'\n{cstmr_drink}')
        print('\nWould you like Ice \nEnter yes/no:')
        option_input = str(input())
        while option_input != 'yes' and option_input != 'no':
          print('\nEnter yes/no')
          option_input = str(input())
        if option_input == 'yes':
          print(f'\nServing {cstmr_drink} with Ice')
        else:
          print(f'\nServing {cstmr_drink} without Ice')
        
      elif user_input == 2:
        add_item = input('\nAdd Item:\n')
        drinks.append(str(add_item))
        print('\nNew Drink List:')
        drinks_index()
  
      elif user_input == 3:
        print('\nChoose a List Item to Changed')
        drinks_index()
        print('\nItem to Change:')
        drinks_change = str(input())
        while drinks_change not in drinks:
          print('\nChoose a Item from the List')
          print('\nItem to Change:')
          drinks_change = str(input())
        drinks_add = str(input('\nItem to Add: '))
        drinks[(drinks.index(drinks_change))] = drinks_add
        drinks_index()
  
      elif user_input == 4:
        print('\nDrinks List')
        drinks_index()
        print('\nDelete an Item')
        del_input = input('Delete: ')
        while del_input not in drinks:
          print('\nChhose an Item in the List')
          del_input = input('Delete: ')
        if del_input in drinks:
          drinks.remove(del_input)
          print(f'\n{del_input} has been deleted\n')  
          drinks_index()