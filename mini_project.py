#Mini-Project

drinks = ['Coca-cola', '7Up', 'Fanta']

def drinks_index():
  for x in drinks:
    print(f'{((drinks.index(x)) + 1)}. {x}')

ordr_dir = []

def ordr_index():
  for x in ordr_dir:
    print(f'{((ordr_dir.index(x)) + 1)}. {x}')

while True:

  print('\nWelcome\nEnter 0 to Exit App\nEnter 1 for Product Menu\nEnter 2 for Orders Menu')
  enter = int(input('Enter: '))

  while enter < 0 or enter > 2:
      print('\nPlease Enter 0/1/2')
      enter = int(input('Enter: '))

  if enter == 0:
    print('\nExit, Thank You')
    break
  elif enter == 1:
    while True: 
      print('\nProduct Menu - Choose an Option:\n0. Return to Main Menu\n1. Product List\n2. Create New Product\n3. Update Product\n4. Delete a Product')
      user_input = int(input('Enter: '))
      
      while user_input < 0 or user_input > 4:
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
    
  else:
    while True: 
      print('\nOrders Menu - Choose an Option:\n0. Return to Main Menu\n1. Orders Dictionary\n2. Customer Information\n3. Update Order Status\n4. Update Customer Info\n5. Delete Order')
      user_input = int(input('Enter: '))
              
      while  user_input < 0 or user_input > 5:
        print('Enter Number from the List')
        user_input = int(input())

      if user_input == 0:
        break

      elif user_input == 1:
        ordr_index()

      elif user_input == 2:
        cstmr_info = {
          "customer_name": input('Name: '),
          "customer_address": input('Address: '),
          "customer_phone": input('Phone Number: '),
          "status": "preparing"}
        ordr_dir.append(cstmr_info)

      elif user_input == 3:
        print('\nChoose Order to Edit:')
        ordr_index()
        edt_ordr = int(input('Enter: '))
        while edt_ordr < 1 or edt_ordr > len(ordr_dir):
          print('Enter a Number from the Index')
          edt_ordr = int(input('Enter: '))
        print('\nChange Order Status:\n1. Preparing\n2. Awaiting Pickup\n3. Out-for-Delivery\n4. Delivered')
        ordr_status = int(input('Enter: '))
        while ordr_status < 1 and ordr_status > 4:
          print('Enter a Number from the Index')
          ordr_status = int(input('Enter: '))
        if ordr_status == 1:
          (ordr_dir[(edt_ordr - 1)]).update({"status": 'Preparing'})
        elif ordr_status == 2:
          (ordr_dir[(edt_ordr - 1)]).update({"status": 'Awaiting Pickup'})
        elif ordr_status == 3:
          (ordr_dir[(edt_ordr - 1)]).update({"status": 'Out-for-Delivery'})
        elif ordr_status == 3:
          (ordr_dir[(edt_ordr - 1)]).update({"status": 'Delivered'})

      elif user_input == 4:
        print('\nChoose Customer Info to Edit:')
        ordr_index()
        edt_info = int(input('Enter: '))
        while edt_info < 1 or edt_ordr > len(ordr_dir):
          print('Enter a Number from the Index')
          edt_info = int(input('Enter: '))        
        
        def create_dictionary(**kwargs):
          this_dict = {}
          for key, value in kwargs.items():
            this_dict[key] = value
          return this_dict

        chng_ordr = create_dictionary(customer_name = input('Name: '), customer_address = input('Address: '), customer_phone = input('Phone: '), status = (ordr_dir[(edt_info - 1)]).get("status"))
        ordr_dir[(edt_info - 1)] = chng_ordr
        
      elif user_input == 5:
        ordr_index()
        print('\nDelete an Order')
        dlt_ordr = int(input('Enter: '))
        while dlt_ordr < 1 and dlt_ordr > len(ordr_dir):
          print('Enter a Number from the Index')
          dlt_ordr = int(input('Enter: '))
        ordr_dir.pop((dlt_ordr - 1))
        print('\n')
        ordr_index()