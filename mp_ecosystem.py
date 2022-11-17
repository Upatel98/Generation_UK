import csv
from random import randint

#Reading CSV Files

def read_products_csv(list):
    with open('products.csv', 'r', newline='') as file:    
      reader = csv.DictReader(file)    
      for x in reader:
        list.append(x)

def read_couriers_csv(list):
    with open('couriers.csv', 'r', newline='') as file:    
      reader = csv.DictReader(file)    
      for x in reader:
        list.append(x)

def read_orders_csv(list):
    with open('orders.csv', 'r', newline='') as file:    
      reader = csv.DictReader(file)    
      for x in reader:
        list.append(x)

#Writing CSV Files
def write_products_csv(list):
    with open('products.csv', 'w', newline='') as file:    
        writer = csv.DictWriter(file, fieldnames=(['Name', 'Price']))    
        writer.writeheader()
        for x in list:
            writer.writerow(x)

def write_couriers_csv(list):
    with open('couriers.csv', 'w', newline='') as file:    
        writer = csv.DictWriter(file, fieldnames=(['Name','Phone Number']))    
        writer.writeheader()
        for x in list:
            writer.writerow(x)

def write_orders_csv(list):
    with open('orders.csv', 'w', newline='') as file:    
        if list:
            writer = csv.DictWriter(file)    
            writer.writeheader()
            for x in list:
                writer.writerow(x)
        else:
            print('No Orders Information')

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
    ths_dict = {
        'Name': input('Enter Name: '), 
        'Price': float(input('Enter Price: '))
    }
    list.append(ths_dict)

def updte_product(list):
    print('Menu:')
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
    print('Menu:')
    lst_indx(list)
    entr = input('Enter Item Index to Update: ')
    entr = inpt(entr, len(list))
    list.pop(entr)

#New Courier Menu
def add_courier(list):
    ths_dict = {
        'Name': input('Enter Courier Name: '),
        'Phone': int(input('Enter Courier Phone: '))
        }

    list.append(ths_dict)
    lst_indx(list)

def updt_courier(list):
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
    lst_indx(list)
    entr = input('Enter Courier Index to Delete: ')
    entr = inpt(entr, len(list))
    del list[int(entr)]
    lst_indx(list)

#New Order Directory
def new_order(list1, list2):
    print('Customer Information:')
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
        lst_indx(list)
        entr = input('Choose Order Information Index: ')
        entr = inpt(entr, len(list))  
        print('\n---Change Order Status---\n[Index 0] ==> Preparing\n[Index 1] ==> Awaiting Pickup\n[Index 2] ==> Out-for-Delivery\n[Index 3] ==> Delivered')
        updte_status = input('Enter Index to Update Order Status: ')
        updte_status = inpt(updte_status, 5)
        if updte_status == 1:
            (list[int(entr)]).update({"status": "Preparing"})
        elif updte_status == 2:
            (list[int(entr)]).update({"status": "Awaiting Pickup"})
        elif updte_status == 3:
            (list[int(entr)]).update({"status": "Out-for-Delivery"})
        elif updte_status == 4:
            (list[int(entr)]).update({"status": "Delivered"})
        lst_indx(list)
    else:
        print('No Orders')

def updt_order(list):
    if list:
        lst_indx(list)
        entr = input('Enter Order Index to Update: ')
        entr = inpt(entr, len(list))
        list[(int(entr))]['customer_name'] = input('NewName: ')
        list[(int(entr))]['customer_address']['home_number'] = input('New House/Flat Number: ')
        list[(int(entr))]['customer_address']['street_name'] = input('New Street Name: ')
        list[(int(entr))]['customer_address']['town'] = input('New Town: ')
        list[(int(entr))]['customer_address']['postcode'] = input('New Postcode: ')
        list[(int(entr))]['customer_phone'] = input('New Phone Number: ')
        list[(int(entr))]["customer_order"]: input('Order Index: ')

        lst_indx(list)
    else:
        print('No Order')

def dlt_order(list):
    if list:
        lst_indx(list)
        entr = input('Enter Order Index to Delete: ')
        entr = inpt(entr, len(list))
        list.pop(entr)
        lst_indx(list)
    else:
        print('No Orders')

'''

#Courier Menu
def ad_courier(courier):
    courier_info = {
        'Name': input('Enter Courier Name: '),
        'Phone': input('Enter Courier Phone: ')
        }

    courier.append(courier_info)
    print('\n')
    lst_index(courier)



#Product Menu
def new_ordr(menu, orders, order_nums):
    print('\nMenu:')
    lst_index(menu)
    enter = input('Enter Index to Start New Order: ')
    enter_loop(enter, len(menu))

    ths_dict = {
        'Order Number': randint(0,99), 
        'Order':[], 
        'Price':0
    }
    ths_dict['Order'].append(menu[int(enter)]['Name'])
    ths_dict['Price'] += menu[int(enter)]['Price']
    order_nums.append(ths_dict['Order Number'])
    orders.append(ths_dict)
    print('\n')
    lst_index(orders)

def add_item(menu, orders):
    if orders:
        print('\nOrders to Update:')
        lst_index(orders)
        enter = input('\nEnter Order Index: ')
        enter_loop(enter, len(orders))
        lst_index(menu)
        add_inpt = input('Enter Index to Add Item: ')
        enter_loop(add_inpt, len(menu))
        orders[int(enter)]['Order'].append(menu[int(add_inpt)]['Name'])
        orders[int(enter)]['Price'] += menu[int(add_inpt)]['Price']
        print(f'\nUpdated Order\n{orders[(int(enter))]}')
    else:
        print('\nNo Order Information in Directory')

def dltE_order(orders):
    if orders:
        lst_index(orders)
        enter = input('Enter Index to Delete Order: ')
        enter_loop(enter, len(orders))
        del orders[int(enter)]
        print('\n')
        lst_index(orders)
    else: 
        print('\nNo Order Information in Directory')

def updte_order(menu, orders):
    if orders:
        print('\nOrders to Update:')
        lst_index(orders)
        updt_enter = input('\nEnter Update Order Index: ')
        enter_loop(updt_enter, len(orders))
        if len(orders[int(updt_enter)]['Order']) == 1:
            lst_index(menu)
            chnge_to = input('Enter Item Index to Add: ')
            enter_loop(int(chnge_to), len(menu))
            orders[int(updt_enter)]['Order'][0] = menu[int(chnge_to)]['Name']
            orders[int(updt_enter)]['Price'] = 0 + menu[int(chnge_to)]['Price']
        else:
            print('\nChoose Item Index to Delete within the Order')
            lst_index((orders[int(updt_enter)]['Order']))
            choose_enter = input('Enter an Index: ')
            del orders[int(updt_enter)]['Order'][int(choose_enter)]
            
#Order Directory
def new_custmr_info(custmr_dir, order_nums, courier):
    if order_nums: 
        print('\nCustomer Information:')
        cstmr_info = {
            "customer_name": input('Name: '),
            "customer_address": {
                'home_number': input('House/Flat Number: '),
                'street_name': input('Street Name: '),
                'town': input('Town: '),
                'postcode': input('Postcode: '),
            },
            "customer_phone": input('Phone Number: '),
            "customer_order_number": order_nums[0],
            "courier": courier.index(courier[randint(0,(len(courier)-1))]),
            "status": "Preparing"}
        order_nums.pop(0)
        custmr_dir.append(cstmr_info)
        print('\n')
        lst_index(custmr_dir)
    else:
        print('Create an Order to Add Customer Information')

def edit_ordr_status(enter, custmr_dir):
    if custmr_dir:
        print('\n')
        lst_index(custmr_dir)
        enter = input('Enter Customer Information Index: ')
        enter_loop(enter, len(custmr_dir))  
        print('\nChange Order Status:\n[Index 1] ==> Preparing\n[Index 2] ==> Awaiting Pickup\n[Index 3] ==> Out-for-Delivery\n[Index 4] ==> Delivered')
        updte_status = input('Enter Index to Update Order Status: ')
        enter_loop(updte_status, 5)
        if int(updte_status) == 1:
            (custmr_dir[int(enter)]).update({"status": "Preparing"})
        elif int(updte_status) == 2:
            (custmr_dir[int(enter)]).update({"status": "Awaiting Pickup"})
        elif int(updte_status) == 3:
            (custmr_dir[int(enter)]).update({"status": "Out-for-Delivery"})
        elif int(updte_status) == 4:
            (custmr_dir[int(enter)]).update({"status": "Delivered"})
        print('\n')
        lst_index(custmr_dir)
    else:
        print('\nNo Customer Information in Directory')

def update_info(custmr_dir):
    if custmr_dir:
        print('\n')
        lst_index(custmr_dir)
        enter = input('Enter Customer Information Index: ')
        enter_loop(enter, len(custmr_dir)) 
        custmr_dir[(int(enter))]['customer_name'] = input('Name: ')
        custmr_dir[(int(enter))]['customer_address']['home_number'] = input('House/Flat Number: ')
        custmr_dir[(int(enter))]['customer_address']['street_name'] = input('Street Name: ')
        custmr_dir[(int(enter))]['customer_address']['town'] = input('Town: ')
        custmr_dir[(int(enter))]['customer_address']['postcode'] = input('Postcode: ')
        custmr_dir[(int(enter))]['customer_phone'] = input('Phone: ')
        print('\n')
        lst_index(custmr_dir)
    else:
        print('\nNo Customer Information in Directory')
    
def dlt_custmr_info(custmr_dir):
    if custmr_dir:
        print('\n')
        lst_index(custmr_dir)
        enter = input('Enter Customer Information Index to Delete: ')
        enter_loop(enter, len(custmr_dir))
        custmr_dir.pop((int(enter)))
        print('\n')
        lst_index(custmr_dir)
    else:
        print('\nNo Customer Information in Directory')

#Courier Menu
def ad_courier(courier):
    courier_info = {
        'Name': input('Enter Courier Name: '),
        'Phone': input('Enter Courier Phone: ')
        }

    courier.append(courier_info)
    print('\n')
    lst_index(courier)

def upt_courier(courier):
    if courier:
        print('\n')
        lst_index(courier)
        enter = input('Enter Index to Update Courier: ')
        enter_loop(enter, len(courier))
        courier[int(enter)].update({'Name': input('Enter Courier Name: ')})
        courier[int(enter)].update({'Phone': input('Enter Courier Name: ')})
        print('\n')
        lst_index(courier)
    else:
        print('\nNo Courier Information in Directory')

def dl_courier(courier):
    if courier:
        print('\n')
        lst_index(courier)
        enter = input('Enter Index to Delete Courier: ')
        enter_loop(enter, len(courier))
        del courier[int(enter)]
        print('\n')
        lst_index(courier)
    else:
        print('\nNo Courier Information in Directory')
        '''