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

def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False
    
#Table Count 
def count(table):
    cursor = database.connection.cursor()
    cursor.execute(f"SELECT COUNT(id) FROM {table}")
    x = cursor.fetchall()[0][0]
    return x 

#Input Loop
def inpt(entr, x):
    while True:
        try:
            if int(entr) not in list(range(0, x)):
                print('Invalid Index')
                entr = input('Re-Enter Index: ')
                continue
        except ValueError:
            print('Invalid Index')
            entr = input('Re-Enter Index: ')
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
                entr = input('Re-Enter Index: ')
                continue
        except ValueError:
            print('Invalid Index')
            entr = input('Re-Enter Index: ')
            continue
        else:
            break

    return int(entr)

#Clear Terminal
clr_trmnl = lambda: os.system('cls')

#Print Database
def print_database(table):

    if table == 'products':
        if count('products') > 0:
            cursor = database.connection.cursor()
            cursor.execute('SELECT id, name, price FROM products')
            rows = cursor.fetchall()
            for row in rows:
                print(f'[Index {row[0]}] ==> [Name: {row[1]} , Price: {row[2]}]')
        else: print('Table is Empty - Unable to Print')   
    
    elif table == 'couriers':
        if count('couriers') > 0:
            cursor = database.connection.cursor()
            cursor.execute('SELECT id, name, number FROM couriers')
            rows = cursor.fetchall()
            for row in rows:
                print(f'[Index {(row[0])}] ==> [Name: {row[1]} , Number: {row[2]}]')
        else: print('Table is Empty - Unable to Print')

    elif table == 'orders':
        if count('orders') > 0:
            cursor = database.connection.cursor()
            cursor.execute('SELECT id, customer_name, customer_address, customer_number, customers_order, courier, status FROM orders')
            rows = cursor.fetchall()
            for row in rows:
                print(f'[Index {row[0]}] :--\nName: {row[1]}\nAddress: {row[2]}\nPhone Number: {row[3]}\nOrder: {row[4]}\nCourier: {row[5]}\nStatus: {row[6]}\n')
        else: print('Table is Empty - Unable to Print')

def add_product():
    print('\n---Add New Item---')
    
    name =  input('\nEnter Name: ')
    while True:
        price = input('Enter Price: ')
        if isfloat(price) == True:
            break
        else:
            print('Invalid Price Value')
            continue
   
    cursor = database.connection.cursor()
    cursor.execute(f"INSERT INTO products (name, price) VALUES ('{name}', '{price}')")
    database.connection.commit()

    print('')
    print_database('products')

def updt_product():
    if count('products') > 0:
            
        print('\n---Update Item---')
        print_database('products')
        
        entr = input('Enter Item Index to Update: ')
        entr = sql_inpt(entr, 'products')

        new_name = input('\nEnter New Name: ')
        new_price = input('Enter New Price: ')
        
        if new_name == '' or new_price == '':
            print('One\Both Inputs Empty - No Update')
        else:
            while True:
                if isfloat(new_price) == True:
                    cursor = database.connection.cursor()
                    cursor.execute(f"UPDATE products SET name='{new_name}', price='{new_price}' WHERE id='{entr}'")
                    database.connection.commit()
                    break
                else:
                    print('Invalid Price Value')
                    new_price = input('Enter Price: ')
                    continue

        print('')
        print_database('products')
    
    else: print('Table is Empty - Unable to Update')

def dlt_product():
    if count('products') > 0:
            
        print('\n---Delete Item---')
        print_database('products')

        entr = input('\nEnter Item Index to Delete: ')
        entr = sql_inpt(entr, 'products')

        cursor = database.connection.cursor()
        cursor.execute(f"DELETE FROM products WHERE id = '{entr}'")
        database.connection.commit()

        print('')
        print_database('products')
    
    else: print('Table is Empty - Unable to Delete')

#New Courier Menu
def add_courier():
    print('\n---Add New Courier---')
    
    name = input('Enter Courier Name: ')

    while True:
        number = input('Enter Courier Number: ')
        if number.isdigit() == True and len(number) == 11 and number[:2] == '07':
            cursor = database.connection.cursor()
            cursor.execute(f"INSERT INTO couriers (name, number) VALUES ('{name}', '{number}')")
            database.connection.commit()
            break
        else:
            print('Invalid Phone Number - 11 Digit Beginning with 07')
            continue
    
    print('')
    print_database('couriers')

def updt_courier():
    if count('couriers') > 0:
        
        print('\n---Update Courier---')
        print_database('couriers')
        
        entr = input('\nEnter Courier Index to Update: ')
        entr = sql_inpt(entr, 'couriers')

        new_name = input('\nEnter Courier Name: ')
        new_number = input('Enter Courier Phone Number: ')

        if new_name == '' or new_number == '':
            print('One\Both Inputs Empty - No Update')
        else:
            while True:
                if new_number.isdigit() == True and len(new_number) == 11 and new_number[:2] == '07':
                    cursor = database.connection.cursor()
                    cursor.execute(f"UPDATE couriers SET name = '{new_name}', number = '{new_number}' WHERE id = '{entr}'")
                    database.connection.commit()
                    break
                else:
                    print('Invalid Phone Number - 11 Digit Beginning with 07')
                    new_number = input('Enter Courier Phone Number: ')
                    continue

        print('')
        print_database('couriers')
        
    else: print('Table is Empty - Unable to Update')

def dlt_courier():
    if count('couriers') > 0:
    
        print('\n---Delete Courier---')
        print_database('couriers')
        
        entr = input('Enter Courier Index to Delete: ')
        entr = sql_inpt(entr, 'couriers')

        cursor = database.connection.cursor()
        cursor.execute(f"DELETE FROM couriers WHERE id = '{entr}'")
        database.connection.commit()

        print('')
        print_database('couriers')

    else: print('Table is Empty - Unable to Delete')

#New Order Menu
def new_order():
    print('\n---New Order Information---')
 
    while True:
        n = 0
        customer_name = input('Name: ')
        for x in customer_name:
            if x.isdigit() == True:
                n += 1
                print('No Numerical Values Allowed')
                continue
            else:
                pass
        if n == 0: break
    
    customer_address = input('Address: ')
    
    while True:
        customer_number = input('Phone Number: ')
        if customer_number.isdigit() == True and len(customer_number) == 11 and customer_number[:2] == '07':
            break
        else:
            print('Invalid Phone Number - 11 Digit Beginning with 07')
            continue
    customer_order = input('Order Index: ')
    print('')
    print_database('couriers')
    courier = input('\nChoose Courier Index: ')
    courier = sql_inpt(courier, 'couriers')

    cursor = database.connection.cursor()
    cursor.execute(f"INSERT INTO orders (customer_name, customer_address, customer_number, customers_order, courier, status) VALUES ('{customer_name}', '{customer_address}', '{customer_number}', '{customer_order}', '{courier}', 'Preparing')")
    database.connection.commit()

    print('')
    print_database('orders')


def updt_order_status():
    if count('orders') > 0:

        print('\n---Update Order Status---')
        print_database('orders')

        entr = input('Choose Order Information Index: ')
        entr = sql_inpt(entr, 'orders')
        print('\n---Change Order Status---\n[Index 0] ==> Preparing\n[Index 1] ==> Awaiting Pickup\n[Index 2] ==> Out-for-Delivery\n[Index 3] ==> Delivered')
        updte_status = input('Enter Index to Update Order Status: ')
        updte_status = inpt(updte_status, 4)

        cursor = database.connection.cursor()

        if updte_status == 0:
            cursor.execute(f"UPDATE orders SET status = 'Preparing' WHERE id = '{entr}'")
        elif updte_status == 1:
            cursor.execute(f"UPDATE orders SET status = 'Awaiting Pickup' WHERE id = '{entr}'")
        elif updte_status == 2:
            cursor.execute(f"UPDATE orders SET status = 'Out-for-Delivery' WHERE id = '{entr}'")
        elif updte_status == 3:
            cursor.execute(f"UPDATE orders SET status = 'Delivered' WHERE id = '{entr}'")

        database.connection.commit()
        print('')
        print_database('orders')
    
    else: print('Table is Empty - Unable to Update')

def updt_order():
    if count('orders') > 0:

        print('\n---Update Order Information---')
        print_database('orders')

        entr = input('Enter Order Index to Update: ')
        entr = sql_inpt(entr, 'orders')

        while True:
            n = 0
            customer_name = input('Name: ')
            for x in customer_name:
                if x.isdigit() == True:
                    n += 1
                    print('No Numerical Values Allowed')
                    continue
                else:
                    pass
            if n == 0: break
        
        customer_address = input('Address: ')
        while True:
            customer_number = input('Phone Number: ')
            if customer_number.isdigit() == True and len(customer_number) == 11 and customer_number[:2] == '07':
                break
            else:
                print('Invalid Phone Number - 11 Digit Beginning with 07')
                continue
        customer_order = input('Order Index: ')
        print('')
        print_database('couriers')
        courier = input('\nChoose Courier Index: ')
        courier = sql_inpt(courier, 'couriers')

        cursor = database.connection.cursor()
        cursor.execute(f"UPDATE orders SET customer_name = '{customer_name}', customer_address = '{customer_address}', customer_number = '{customer_number}', customers_order = '{customer_order}', courier = '{courier}' WHERE id = '{entr}'")
        database.connection.commit()

        print('')
        print_database('orders')
        
    else: print('Table is Empty - Unable to Update ')

def dlt_order():
    if count('orders') > 0:
        
        print('\n---Delte Order---')
        print_database('orders')
            
        entr = input('Enter Order Index to Delete: ')
        entr = sql_inpt(entr, 'orders')

        cursor = database.connection.cursor()
        cursor.execute(f"DELETE FROM orders WHERE id = '{entr}'")
        database.connection.commit()

        print('')
        print_database('orders')
            
    else: print('Table is Empty - Unable to Delete')