#Mini-Project - Week 6

from mp_ecosystem import prnt_database, cls_database, inpt, clr_trmnl
from mp_ecosystem import products, couriers, orders

while True:
  print('\n---Welcome---\n[Index 0] ==> Exit App\n[Index 1] ==> Products Menu\n[Index 2] ==> Couriers Menu\n[Index 3] ==> Orders Menu')
  entr = inpt(input('Enter Index: '), 4)
  clr_trmnl()

  if entr == 0:

    cls_database()
    print('Exit, Thank You')
    break

  elif entr == 1: 
    while True:
      print('\n---Product Menu---\n[Index 0] ==> Return to Main Menu\n[Index 1] ==> Products Menu\n[Index 2] ==> Add New Item\n[Index 3] ==> Update Item\n[Index 4] ==> Delete an Item')
      entr = inpt(input('Enter Index: '), 6)

      if entr == 0:
        clr_trmnl()
        break

      elif entr == 1:
        print('\n---Product List---')
        prnt_database('products')

      elif entr == 2:
        products.add()
      
      elif entr == 3:
        products.updt()

      elif entr == 4:
        products.dlt()

  elif entr == 2: 
    while True: 
      print('\n---Courier Menu---\n[Index 0] ==> Return to Main Menu\n[Index 1] ==> Couriers\n[Index 2] ==> Add Courier\n[Index 3] ==> Update Courier\n[Index 4] ==> Delete Courier')
      entr = inpt(input('Enter Index: '), 5)
    
      if entr == 0:
        clr_trmnl()
        break

      elif entr == 1:
        print('\n---Courier List---')
        prnt_database('couriers')

      elif entr == 2:
        couriers.add()

      elif entr == 3:
        couriers.updt()
        
      elif entr == 4:
        couriers.dlt() 

  elif entr == 3:
    while True: 
      print('\n---Orders Menu---\n[Index 0] ==> Return to Main Menu\n[Index 1] ==> Orders Directory\n[Index 2] ==> Add Customer Information\n[Index 3] ==> Update Order Status\n[Index 4] ==> Update Customer Information\n[Index 5] ==> Delete Customer Information')
      entr = inpt(input('Enter Index: '), 6)

      if entr == 0:
        clr_trmnl()
        break

      elif entr == 1:
        print('\n---Order Directory---')
        prnt_database('orders')

      elif entr == 2:
        orders.add()
      
      elif entr == 3:
        orders.updt_status()
      
      elif entr == 4:
        orders.updt_info()
      
      elif entr == 5:
        orders.dlt()