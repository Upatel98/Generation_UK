<<<<<<< HEAD
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

=======
import os
import mysql_database.mini_project_database as database

#Closing Database
def close_database():
    cursor = database.connection.cursor()
    cursor.close()
    database.connection.close()
    print('\nProducts Database Uploaded')
    print('Couriers Database Uploaded')
    print('Orders Database Uploaded')

>>>>>>> databases
#Input Loop
def inpt(entr, x):
    while True:
        try:
            if int(entr) not in list(range(0, x)):
                print('Invalid Index')
<<<<<<< HEAD
                entr = input('Enter Index: ')
                continue
        except ValueError:
            print('Invalid Index')
            entr = input('Enter Index: ')
=======
                entr = input('Re-enter Index: ')
                continue
        except ValueError:
            print('Invalid Index')
            entr = input('Re-enter Index: ')
            continue
        else:
            break
    return int(entr) 

#SQL Input Loop
def sql_inpt(entr, table):
    while True:
        cursor = database.connection.cursor()
        cursor.execute(f'SELECT id FROM {table}')
        try:
            if int(entr) not in [x[0] for x in cursor.fetchall()]:
                print('Invalid Index')
                entr = input('Re-enter Index: ')
                continue
        except ValueError:
            print('Invalid Index') 
            entr = input('Re-enter Index: ')
>>>>>>> databases
            continue
        else:
            break
    return int(entr) 

<<<<<<< HEAD
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
=======
    return int(entr)

#Clear Terminal
clr_trmnl = lambda : os.system('cls')

#Float
def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False

#New Products Menu
def print_products_database():
   
    cursor = database.connection.cursor()
    cursor.execute('SELECT id, name, price FROM products')
   
    rows = cursor.fetchall()
    for row in rows:
        print(f'[Index {row[0]}] ==> [Name: {row[1]} , Price: {row[2]}]')

def add_product():
    print('\n---Add New Item---')

    name =  input('Enter Name: ')
    while True:
        price = input('Enter Price: ')
        if isfloat(price) == True:
            break
        else:
            print('Price Entered Invalid')
            continue
   
    cursor = database.connection.cursor()
    cursor.execute(f"INSERT INTO products (name, price) VALUES ('{name}', '{price}')")
    database.connection.commit()

    print('')
    print_products_database()

def updt_product():
    print('\n---Update Item---')
    print_products_database()
    
    entr = input('Enter Item Index to Update: ')
    entr = sql_inpt(entr, 'products')

    name =  input('Enter Name: ')
    while True:
        price = input('Enter Price: ')
        if name == '' or price == '':
            print('One\Both Inputs Empty - No Update')
            break
        elif isfloat(price) == True:
            cursor = database.connection.cursor()
            cursor.execute(f"UPDATE products SET name='{name}', price='{price}' WHERE id='{entr}'")
            database.connection.commit()
            break
        else:
            print('Price Entered Invalid')
            continue

    print('')
    print_products_database()

def dlt_product():
    print('\n---Delete Item---')
    print_products_database()

    entr = input('Enter Item Index to Delete: ')
    entr = sql_inpt(entr, 'products')
    cursor = database.connection.cursor()
    cursor.execute(f"DELETE FROM products WHERE id = '{entr}'")
    database.connection.commit()

    print('')
    print_products_database()

#New Courier Menu
def print_couriers_database():
    
    cursor = database.connection.cursor()
    cursor.execute('SELECT id, name, number FROM couriers')
    
    rows = cursor.fetchall()
    for row in rows:
        print(f'[Index{str(row[0])}] ==> [Name: {row[1]} , Number: {row[2]}]')

def add_courier():
    print('\n---Add New Courier---')
    
    name = input('Enter Courier Name: ')
    while True:
        number = input('Enter Courier Phone Number: ')
        if number.isdigit() == True and len(number) == 11 and number[0:2] == '07':
            cursor = database.connection.cursor()
            cursor.execute(f"INSERT INTO couriers (name, number) VALUES ('{name}', '{number}')")
            database.connection.commit()
            break 
        else:
            print('Phone Number Needs to be 11 Digits Starting with 07')
            continue

    print('')
    print_couriers_database()

def updt_courier():
    print('\n---Update Courier---')
    print_couriers_database()
    
    entr = input('Enter Courier Index to Update: ')
    entr = sql_inpt(entr, 'couriers')

    new_name = input('Enter Courier Name: ')
    while True:
        new_number = input('Enter Courier Phone Number: ')
        if new_name == '' or new_number == '':
            print('One\Both Inputs Empty - No Update')
        elif new_number.isdigit() == True and len(new_number) == 11 and new_number[0:2] == '07':
            cursor = database.connection.cursor()
            cursor.execute(f"UPDATE couriers SET name = '{new_name}', number = '{new_number}' WHERE id = '{entr}'")
            database.connection.commit()
            break 
        else:
            print('Phone Number Needs to be 11 Digits Starting with 07')
            continue

    print('')
    print_couriers_database()

def dlt_courier():
    print('\n---Delete Courier---')
    print_couriers_database()
    
    entr = input('Enter Courier Index to Delete: ')
    entr = sql_inpt(entr, 'couriers')
    cursor = database.connection.cursor()
    cursor.execute(f"DELETE FROM couriers WHERE id = '{entr}'")
    database.connection.commit()

    print('')
    print_couriers_database()

#New Order Directory
def print_orders_database():
   
    cursor = database.connection.cursor()
    cursor.execute('SELECT id, customer_name, customer_address, customer_number, customers_order, courier, status FROM orders')
   
    rows = cursor.fetchall()
    for row in rows:
        print(f'\n[Index {row[0]}]\nName: {row[1]}\nAddress: {row[2]}\nNumber: {row[3]}\nOrder: {row[4]}\nCourier: {row[5]}\nStatus: {row[6]}')

def new_order():
    print('\n---New Order Information---')

    customer_name = input('Name: ')
    customer_address = input('Address: ')
    while True:
        customer_number = input('Phone Number: ')
        if customer_number.isdigit() == True and len(customer_number) == 11 and customer_number[0:2] == '07':
            break
        else:
            print('Phone Number Needs to be 11 Digits Starting with 07')
            continue
    customers_order = input('Order Index: ')
    print('')
    print_couriers_database()
    courier = input('Choose Courier Index: ')
    courier = sql_inpt(courier, 'couriers')
    status = "Preparing"
    
    cursor = database.connection.cursor()
    cursor.execute(f"INSERT INTO orders (customer_name, customer_address, customer_number, customers_order, courier, status) VALUES ('{customer_name}', '{customer_address}', '{customer_number}', '{customers_order}', '{courier}', '{status}')")
    database.connection.commit()

    print('')
    print_orders_database()

def updt_order_status():
    print('\n---Update Order Status---')
    print_orders_database()
    
    entr = input('\nEnter Order Index to Update Status: ')
    entr = sql_inpt(entr, 'orders')
    
    print('\n---Change Order Status---\n[Index 0] ==> Preparing\n[Index 1] ==> Awaiting Pickup\n[Index 2] ==> Out-for-Delivery\n[Index 3] ==> Delivered')
    updte_status = input('Enter Index to Update Order Status: ')
    updte_status = inpt(updte_status, 5)
    cursor = database.connection.cursor()
    if updte_status == 1:
        cursor.execute(f"UPDATE orders SET status = 'Preparing' WHERE id = '{entr}'")
    elif updte_status == 2:
        cursor.execute(f"UPDATE orders SET status = 'Awaiting Pickup' WHERE id = '{entr}'")
    elif updte_status == 3:
        cursor.execute(f"UPDATE orders SET status = 'Out-for-Delivery' WHERE id = '{entr}'")
    elif updte_status == 4:
        cursor.execute(f"UPDATE orders SET status = 'Delivered' WHERE id = '{entr}'")
    
    database.connection.commit()

    print('')
    print_orders_database()

def updt_order():
    print('\n---Update Order Information---')
    print_orders_database()

    entr = input('\nEnter Order Index to Update: ')
    entr = sql_inpt(entr, 'orders')

    new_name = input('New Name: ')
    new_address = input('New Address: ')
    while True:
        new_number = input('New Phone Number: ')
        if new_number.isdigit() == True and len(new_number) == 11 and new_number[0:2] == '07':
            break
        else:
            print('Phone Number Needs to be 11 Digits Starting with 07')
            continue
    new_order =  input('New Order: ')
    print('')
    print_couriers_database()
    new_courier = input('Choose New Courier')
    new_courier = sql_inpt(new_courier, 'couriers')

    cursor = database.connection.cursor()
    cursor.execute(f"UPDATE orders set customer_name = '{new_name}', customer_address = '{new_address}', customer_number = '{new_number}', customers_order = '{new_order}', courier = '{new_courier}'")
    database.connection.commit()

def dlt_order():
    print('\n---Delete Order---')
    print_orders_database()
    entr = input('Enter Order Index to Delete: ')
    entr = sql_inpt(entr, 'couriers')
    
    cursor = database.connection.cursor()
    cursor.execute(f"DELETE FROM orders WHERE id = '{entr}'")
    database.connection.commit()

    print('')
    print_orders_database() 
>>>>>>> databases
