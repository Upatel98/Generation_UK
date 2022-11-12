#Mini-Project

from mp_ecosystem import lst_index, enter_loop, new_ordr, add_item, dlt_order, new_custmr_info, edit_ordr_status, update_info, dlt_custmr_info, add_courier, updt_courier, dlt_courier
from random import randint

menu = [{'Name': 'Coca-cola', 'Price': 2.50}, {'Name': '7Up', 'Price': 2.50}, {'Name': 'Fanta', 'Price': 2.50}, {'Name': 'Water', 'Price': 2.50}]

courier = ['John', 'Smith', 'David', 'Manny', 'Floyd', 'Daniel']

orders = []

custmr_dir =[]

while True:
  print('\nWelcome\n[Index 0] ==> Exit App\n[Index 1] ==> Product\'s Menu\n[Index 2] ==> Orders Menu\n[Index 3] ==> Courier\'s Menu')
  enter = input('Enter a Index: ')
  enter_loop(enter, 4)
  
  if int(enter) == 0:
    print('\nExit, Thank You')
    break

  elif int(enter) == 1: 
    while True: 
      print('\nProduct Menu \n[Index 0] ==> Return to Main Menu\n[Index 1] ==> Product Menu\n[Index 2] ==> Add New Item\n[Index 3] ==> Update Order\n[Index 4] ==> Delete an Order')
      enter = input('\nEnter Index: ')
      enter_loop(enter, 6)

      if int(enter) == 0:
        break

      elif int(enter) == 1:
        new_ordr(menu, orders, enter)
      
      elif int(enter) == 2:
        add_item(menu, orders)
      
      elif int(enter) == 3:
        break

      elif int(enter) == 4:
        dlt_order(orders, enter)

  elif int(enter) == 2:
    while True: 
      print('\nOrders Menu:\n[Index 0] ==> Return to Main Menu\n[Index 1] ==> Orders Dictionary\n[Index 2] ==> Add Customer Information\n[Index 3] ==> Update Order Status\n[Index 4] ==> Update Customer Info\n[Index 5] ==> Delete Customer Information')
      enter = input('Enter Index: ')
      enter_loop(enter, 6)

      if int(enter) == 0:
        break

      elif int(enter) == 1:
        lst_index(custmr_dir)

      elif int(enter) == 2:
        new_custmr_info(custmr_dir)
      
      elif int(enter) == 3:
        edit_ordr_status(enter, custmr_dir)
      
      elif int(enter) == 4:
        update_info(custmr_dir)
      
      elif int(enter) == 5:
        dlt_custmr_info(custmr_dir)
  
  elif int(enter) == 3: 
    while True: 
      print('\nCourier\'s Menu \n[Index 0] ==> Return to Main Menu\n[Index 1] ==> Courier\'s List\n[Index 2] ==> Courier\'s List\n[Index 3] ==> Update Courier List \n[Index 4] ==> Delete Courier')
      enter = input('\nEnter Index: ')
      enter_loop(enter, 5)
    
      if int(enter) == 0:
        break

      elif int(enter) == 1:
        lst_index(courier)

      elif int(enter) == 2:
        add_courier(courier)

      elif int(enter) == 3:
        updt_courier(courier)

      elif int(enter) == 4:
        dlt_courier(courier)