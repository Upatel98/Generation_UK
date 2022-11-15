from random import randint

#Create an Index
def lst_index(arg):
    for x in arg:
        print(f'Index[{arg.index(x)}] ==> {x}')

#Enter Loop
def enter_loop(enter, x):
    while True:
        try:
            if int(enter) not in list(range(0, x)):
                enter = input('Enter a Valid Index: ')
                continue
        except ValueError:
            enter = input('Enter a Valid Index: ')
            continue
        else:
            break

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

def dlt_order(orders):
    if orders:
        lst_index(orders)
        enter = input('Enter Index to Delete Order: ')
        enter_loop(enter, len(orders))
        del orders[int(enter)]
        print('\n')
        lst_index(orders)
    else: 
        print('\nNo Order Information in Directory')

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
def add_courier(courier):
    courier_info = {
        'Name': input('Enter Courier Name: '),
        'Phone': input('Enter Courier Phone: ')
        }

    courier.append(courier_info)
    print('\n')
    lst_index(courier)

def updt_courier(courier):
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

def dlt_courier(courier):
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