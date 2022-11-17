#Mini-Project

from mp_ecosystem import read_products_csv, read_couriers_csv, read_orders_csv, write_products_csv, write_couriers_csv, write_orders_csv, inpt, lst_indx, add_product, updte_product, dlt_product, add_courier, updt_courier, dlt_courier, new_order, updt_order_status, updt_order, dlt_order

products = []
read_products_csv(products)

couriers = []
read_couriers_csv(couriers)

orders = []
read_orders_csv(orders)

print('Products CSV File Uploaded\nCouriers CSV File Uploaded\nOrders CSV File Uploaded')

while True:
  print('\n---Welcome---\n[Index 0] ==> Exit App\n[Index 1] ==> Products Menu\n[Index 2] ==> Couriers Menu\n[Index 3] ==> Orders Menu')

  entr = input('Enter Index: ')
  entr = inpt(entr, 4)
    
  if entr == 0:

    write_products_csv(products)
    print('Products CSV File Updated')
    write_couriers_csv(couriers)
    print('Couriers CSV File Updated')
    write_orders_csv(orders)
    print('Orders CSV File Updated')
    print('\nExit, Thank You')

    break

  elif entr == 1: 
    while True: 
      print('\n---Product Menu---\n[Index 0] ==> Return to Main Menu\n[Index 1] ==> Products Menu\n[Index 2] ==> Add New Item\n[Index 3] ==> Update Item\n[Index 4] ==> Delete an Item')
      entr = input('Enter Index: ')
      entr = inpt(entr, 6)

      if entr == 0:
        break

      elif entr == 1:
        lst_indx(products)

      elif entr == 2:
        add_product(products)
      
      elif entr == 3:
        updte_product(products)

      elif entr == 4:
        dlt_product(products)

  elif entr == 2: 
    while True: 
      print('\n---Courier Menu---\n[Index 0] ==> Return to Main Menu\n[Index 1] ==> Couriers\n[Index 2] ==> Add Courier\n[Index 3] ==> Update Courier\n[Index 4] ==> Delete Courier')
      entr = input('Enter Index: ')
      entr = inpt(entr, 5)
    
      if entr == 0:
        break

      elif entr == 1:
        lst_indx(couriers)

      elif entr == 2:
        add_courier(couriers)

      elif entr == 3:
        updt_courier(couriers)

      elif entr == 4:
        dlt_courier(couriers) 

  elif entr == 3:
    while True: 
      print('\n---Orders Menu---\n[Index 0] ==> Return to Main Menu\n[Index 1] ==> Orders Directory\n[Index 2] ==> Add Customer Information\n[Index 3] ==> Update Order Status\n[Index 4] ==> Update Customer Info\n[Index 5] ==> Delete Customer Information')
      entr = input('Enter Index: ')
      entr = int(inpt(entr, 6))

      if entr == 0:
        break

      elif entr == 1:
        lst_indx(orders) if orders else print('No Orders')

      elif entr == 2:
        new_order(orders, couriers)
      
      elif entr == 3:
        updt_order_status(orders)
      
      elif entr == 4:
        updt_order(orders)
      
      elif entr == 5:
        dlt_order(orders)