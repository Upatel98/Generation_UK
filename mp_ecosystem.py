import os
import csv
import mysql_database.mini_project_database as database

#Reading CSV Files
def read_orders_csv(list):
    with open('orders.csv', 'r', newline='') as file:    
      reader = csv.DictReader(file)    
      for x in reader:
        list.append(x)

    file.close()
    print('Orders CSV File Uploaded')

#Writing CSV Files
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

#Closing Database
def close_database():
    cursor = database.connection.cursor()
    cursor.close()
    database.connection.close()
    print('\nProducts Database Uploaded')
    print('Couriers Database Uploaded')

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

#SQL Input Loop
def sql_inpt(entr, table):
    while True:
        cursor = database.connection.cursor()
        cursor.execute(f'SELECT id FROM {table}')
        try:
            if int(entr) not in [x[0] for x in cursor.fetchall()]:
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

#Clear Terminal
def cls_trmnl():
    os.system('cls')

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
    price = input('Enter Price: ')
   
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
    name = input('\nEnter New Name: ')
    price = input('Enter New Price: ')

    if name == '' or price == '':
        print('One\Two Inputs Empty')
    else:
        cursor = database.connection.cursor()
        cursor.execute(f"UPDATE products SET name='{name}', price='{price}' WHERE id='{entr}'")
        database.connection.commit()

    print('')
    print_products_database()

def dlt_product():
    print('\n---Delete Item---')
    print_products_database()

    entr = input('\nEnter Item Index to Delete: ')
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
    number = input('Enter Courier Number: ')

    cursor = database.connection.cursor()
    cursor.execute(f"INSERT INTO couriers (name, number) VALUES ('{name}', '{number}')")
    database.connection.commit()

    print('')
    print_couriers_database()

def updt_courier():
    print('\n---Update Courier---')
    print_couriers_database()
    
    entr = input('Enter Courier Index to Update: ')
    entr = sql_inpt(entr, 'couriers')
    name = input('Enter Courier Name: ')
    number = input('Enter Courier Phone Number: ')

    if name == '' or number == '':
        print('One\Two Inputs Empty')
    else:    
        cursor = database.connection.cursor()
        cursor.execute(f"UPDATE couriers SET name = '{name}', number = '{number}' WHERE id = '{entr}'")
        database.connection.commit()

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
def new_order(list1):
    print('\n---New Order Information---')
    ths_dict = {
        "customer_name": input('Name: '),
        "customer_address": [input('House/Flat Number: '),input('Street Name: '),input('Town: '),input('Postcode: ')],
        "customer_phone": input('Phone Number: '),
        "customer_order": input('Order Index: '),
        "courier": input('Courier Index: '),
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
        list[entr]['customer_name'] = input('New Name: ')
        list[entr]['customer_address'][0] = input('New House/Flat Number: ')
        list[entr]['customer_address'][1] = input('New Street Name: ')
        list[entr]['customer_address'][2] = input('New Town: ')
        list[entr]['customer_address'][3] = input('New Postcode: ')
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