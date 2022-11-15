#Mini-Project
import csv
from mp_files.mp_ecosystem import lst_index, enter_loop, new_ordr, add_item, dlt_order, new_custmr_info, edit_ordr_status, update_info, dlt_custmr_info, add_courier, updt_courier, dlt_courier

menu = [{'Name': 'Coca-cola', 'Price': 2.50}, {'Name': '7Up', 'Price': 2.50}, {'Name': 'Fanta', 'Price': 2.50}, {'Name': 'Water', 'Price': 2.50}]

courier = [{'Name': 'UberEats', 'Phone': '07987654321'}, {'Name': 'Deliveroo', 'Phone': '07123456789'},{'Name': 'JustEat', 'Phone': '07987123456'}, {'Name': 'FoodHub', 'Phone': '07987123456'}]

orders = []

order_nums = []

custmr_dir =[]

while True:
  print('Welcome\n[Index 0] ==> Exit App\n[Index 1] ==> Product\'s Menu\n[Index 2] ==> Courier\'s Menu\n[Index 3] ==> Orders Menu')
  enter = input('Enter a Index: ')
  enter_loop(enter, 4)
  
  if int(enter) == 0:
  
    with open('mini_project_ecosystem/products.csv', 'w', newline='') as file:    
      writer = csv.DictWriter(file, fieldnames = (menu[0].keys()))    
      writer.writeheader()
      for x in menu:
        writer.writerow(x)
      print('Product Information Added to CSV.File')
    
    with open('mini_project_ecosystem/orders.csv', 'w', newline='') as file:    
      if orders:
        writer = csv.DictWriter(file, fieldnames = (orders[0].keys()))    
        writer.writeheader()
        for x in orders:
          writer.writerow(x)
      else:
        print('No Orders Information')
  
    with open('mini_project_ecosystem/courier.csv', 'w', newline='') as file:    
      writer = csv.DictWriter(file, fieldnames = (courier[0].keys())) 
      writer.writeheader()
      for x in courier:
        writer.writerow(x)
      print('Courier Information Added to CSV.File')

    print('\nExit, Thank You')
    break

  elif int(enter) == 1: 
    while True: 
      print('\nProduct Menu \n[Index 0] ==> Return to Main Menu\n[Index 1] ==> Product Menu\n[Index 2] ==> Add New Item\n[Index 3] ==> Update Order\n[Index 4] ==> Delete an Order')
      if orders: print(f'\nCurrent Orders'), lst_index(orders)
      enter = input('Enter Index: ')
      enter_loop(enter, 6)

      if int(enter) == 0:
        break

      elif int(enter) == 1:
        new_ordr(menu, orders, order_nums)

      elif int(enter) == 2:
        add_item(menu, orders)
      
      elif int(enter) == 3:
        break

      elif int(enter) == 4:
        dlt_order(orders)

  elif int(enter) == 2: 
    while True: 
      print('\nCourier\'s Menu \n[Index 0] ==> Return to Main Menu\n[Index 1] ==> Courier\'s List\n[Index 2] ==> Add Courier\n[Index 3] ==> Update Courier List \n[Index 4] ==> Delete Courier')
      enter = input('Enter Index: ')
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

  elif int(enter) == 3:
    while True: 
      print('\nOrders Menu:\n[Index 0] ==> Return to Main Menu\n[Index 1] ==> Orders Dictionary\n[Index 2] ==> Add Customer Information\n[Index 3] ==> Update Order Status\n[Index 4] ==> Update Customer Info\n[Index 5] ==> Delete Customer Information')
      enter = input('Enter Index: ')
      enter_loop(enter, 6)

      if int(enter) == 0:
        break

      elif int(enter) == 1:
        lst_index(custmr_dir)

      elif int(enter) == 2:
        new_custmr_info(custmr_dir, order_nums, courier)
      
      elif int(enter) == 3:
        edit_ordr_status(enter, custmr_dir)
      
      elif int(enter) == 4:
        update_info(custmr_dir)
      
      elif int(enter) == 5:
        dlt_custmr_info(custmr_dir)