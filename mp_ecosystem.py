import csv
from random import randint

#Reading CSV Files

def read_products_csv(list):
    with open('products.csv', 'r', newline='') as file:    
      reader = csv.DictReader(file)    
      for x in reader:
        list.append(x)

    file.close()
    print('\nProducts CSV File Uploaded')

def read_couriers_csv(list):
    with open('couriers.csv', 'r', newline='') as file:    
      reader = csv.DictReader(file)    
      for x in reader:
        list.append(x)

    file.close()
    print('Couriers CSV File Uploaded')

def read_orders_csv(list):
    with open('orders.csv', 'r', newline='') as file:    
      reader = csv.DictReader(file)    
      for x in reader:
        list.append(x)

    file.close()
    print('Orders CSV File Uploaded')

#Writing CSV Files
def write_products_csv(list):
    with open('products.csv', 'w', newline='') as file:    
        writer = csv.DictWriter(file, fieldnames=(['Name', 'Price']))    
        writer.writeheader()
        for x in list:
            writer.writerow(x)

    file.close()
    print('\nProducts CSV File Updated')

def write_couriers_csv(list):
    with open('couriers.csv', 'w', newline='') as file:    
        writer = csv.DictWriter(file, fieldnames=(['Name','Phone Number']))    
        writer.writeheader()
        for x in list:
            writer.writerow(x)

    file.close()
    print('Couriers CSV File Updated')

def write_orders_csv(list):
    with open('orders.csv', 'w', newline='') as file:    
        if list:
            writer = csv.DictWriter(file, fieldnames=(list[0].keys()))    
            writer.writeheader()
            for x in list:
                writer.writerow(x)
            print('Orders CSV File Updated')
            
        else:
            print('No Orders Information to Upload')

    file.close()

#Create an Index
def lst_indx(list):
    for x in list:
        print(f'Index[{list.index(x)}] ==> {x}')

#Input Loop
def inpt(entr, x):
    while True:
        try:
            if int(entr) not in list(range(0, x)):
                print('Invalid Index')
                entr = input('Enter Index: ')
                continue
        except ValueError:
            print('Invalid Index')
            entr = input('Enter Index: ')
            continue
        else:
            break
    return int(entr) 

#Blank Loop
def blnk():
    try:
        New_Name = input('Enter New Name: ')
        Price = input('Enter New Price: ')
    except ValueError:
        print('Minimum One Input was Empty')
    return 

#New Products Menu
def add_product(list):
    print('\n---Add New Item---')
    ths_dict = {
        'Name': input('Enter Name: '), 
        'Price': float(input('Enter Price: '))
    }
    list.append(ths_dict)
    lst_indx(list)

def updt_product(list):
    print('\n---Update Item---')
    lst_indx(list)
    entr = input('Enter Item Index to Update: ')
    entr = inpt(entr, len(list))
    
    ths_dict = {
        'Name': input('Enter New Name: '),
        'Price': float(input('Enter New Price: '))
    }
    list[entr] = ths_dict
    lst_indx(list)

def dlt_product(list):
    print('\n---Delete Item---')
    lst_indx(list)
    entr = input('Enter Item Index to Update: ')
    entr = inpt(entr, len(list))
    list.pop(entr)

    lst_indx(list)

#New Courier Menu
def add_courier(list):
    print('\n---Add New Courier---')
    ths_dict = {
        'Name': input('Enter Courier Name: '),
        'Phone': int(input('Enter Courier Phone: '))
        }

    list.append(ths_dict)
    lst_indx(list)

def updt_courier(list):
    print('\n---Update Courier---')
    lst_indx(list)
    entr = input('Enter Courier Index to Update: ')
    entr = inpt(entr, len(list))
    ths_dict = {
        'Name': input('New Courier Name: '),
        'Phone': int(input('New Courier Phone Number: '))
        }

    list[entr] = ths_dict
    lst_indx(list)

def dlt_courier(list):
    print('\n---Delete Courier---')
    lst_indx(list)
    entr = input('Enter Courier Index to Delete: ')
    entr = inpt(entr, len(list))
    del list[int(entr)]

    lst_indx(list)

#New Order Directory
def new_order(list1, list2):
    print('\n---New Order Information---')
    ths_dict = {
        "customer_name": input('Name: '),
        "customer_address": {
            'home_number': input('House/Flat Number: '),
            'street_name': input('Street Name: '),
            'town': input('Town: '),
            'postcode': input('Postcode: '),
        },
        "customer_phone": input('Phone Number: '),
        "customer_order": input('Order Index: '),
        "courier": list2.index(list2[randint(0,(len(list2)-1))]),
        "status": "Preparing"}

    list1.append(ths_dict)
    lst_indx(list1)

def updt_order_status(list):
    if list:
        print('\n---Update Order Status---')
        lst_indx(list)
        entr = input('Choose Order Information Index: ')
        entr = inpt(entr, len(list))  
        print('\n---Change Order Status---\n[Index 0] ==> Preparing\n[Index 1] ==> Awaiting Pickup\n[Index 2] ==> Out-for-Delivery\n[Index 3] ==> Delivered')
        updte_status = input('Enter Index to Update Order Status: ')
        updte_status = inpt(updte_status, 5)
        if updte_status == 1:
            (list[entr]).update({"status": "Preparing"})
        elif updte_status == 2:
            (list[entr]).update({"status": "Awaiting Pickup"})
        elif updte_status == 3:
            (list[entr]).update({"status": "Out-for-Delivery"})
        elif updte_status == 4:
            (list[entr]).update({"status": "Delivered"})
        lst_indx(list)
    else:
        print('No Orders')

def updt_order(list):
    if list:
        print('\n---Update Order Information---')
        lst_indx(list)
        entr = input('Enter Order Index to Update: ')
        entr = inpt(entr, len(list))
        list[entr]['customer_name'] = input('NewName: ')
        list[entr]['customer_address']['home_number'] = input('New House/Flat Number: ')
        list[entr]['customer_address']['street_name'] = input('New Street Name: ')
        list[entr]['customer_address']['town'] = input('New Town: ')
        list[entr]['customer_address']['postcode'] = input('New Postcode: ')
        list[entr]['customer_phone'] = input('New Phone Number: ')
        list[entr]["customer_order"]: input('Order Index: ')

        lst_indx(list)
    else:
        print('No Order')

def dlt_order(list):
    if list:
        print('\n---Delte Order---')
        lst_indx(list)
        entr = input('Enter Order Index to Delete: ')
        entr = inpt(entr, len(list))
        list.pop(entr)
        lst_indx(list)
    else:
        print('No Orders')