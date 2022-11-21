#Mini-Project

from mp_ecosystem import read_orders_csv
from mp_ecosystem import write_orders_csv, close_database
from mp_ecosystem import inpt, lst_indx
from mp_ecosystem import print_products_database, add_product, updt_product, dlt_product
from mp_ecosystem import print_couriers_database, add_courier, updt_courier, dlt_courier
from mp_ecosystem import new_order, updt_order_status, updt_order, dlt_order

orders = []
read_orders_csv(orders)

while True:
  print('\n---Welcome---\n[Index 0] ==> Exit App\n[Index 1] ==> Products Menu\n[Index 2] ==> Couriers Menu\n[Index 3] ==> Orders Menu')

  entr = input('Enter Index: ')
  entr = inpt(entr, 4)
    
  if entr == 0:

    close_database()
    write_orders_csv(orders)
    print('Exit, Thank You')
    break

  elif entr == 1: 
    while True: 
      print('\n---Product Menu---\n[Index 0] ==> Return to Main Menu\n[Index 1] ==> Products Menu\n[Index 2] ==> Add New Item\n[Index 3] ==> Update Item\n[Index 4] ==> Delete an Item')
      entr = input('Enter Index: ')
      entr = inpt(entr, 6)

      if entr == 0:
        break

      elif entr == 1:
        print('\n---Product List---')
        print_products_database()

      elif entr == 2:
        add_product()
      
      elif entr == 3:
        updt_product()

      elif entr == 4:
        dlt_product()

  elif entr == 2: 
    while True: 
      print('\n---Courier Menu---\n[Index 0] ==> Return to Main Menu\n[Index 1] ==> Couriers\n[Index 2] ==> Add Courier\n[Index 3] ==> Update Courier\n[Index 4] ==> Delete Courier')
      entr = input('Enter Index: ')
      entr = inpt(entr, 5)
    
      if entr == 0:
        break

      elif entr == 1:
        print('\n---Courier List---')
        print_couriers_database()

      elif entr == 2:
        add_courier()

      elif entr == 3:
        updt_courier()

      elif entr == 4:
        dlt_courier() 

  elif entr == 3:
    while True: 
      print('\n---Orders Menu---\n[Index 0] ==> Return to Main Menu\n[Index 1] ==> Orders Directory\n[Index 2] ==> Add Customer Information\n[Index 3] ==> Update Order Status\n[Index 4] ==> Update Customer Info\n[Index 5] ==> Delete Customer Information')
      entr = input('Enter Index: ')
      entr = int(inpt(entr, 6))

      if entr == 0:
        break

      elif entr == 1:
        (print('\nOrders'), lst_indx(orders)) if orders else print('\nNo Orders')

      elif entr == 2:
        new_order(orders)
      
      elif entr == 3:
        updt_order_status(orders)
      
      elif entr == 4:
        updt_order(orders)
      
      elif entr == 5:
        dlt_order(orders)