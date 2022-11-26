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

#Input Loop
def inpt(entr, x):
    while True:
        try:
            if int(entr) not in list(range(0, x)):
                print('Invalid Index')
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
            continue
        else:
            break

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