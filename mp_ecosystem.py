from random import randint

#Create an Index
def lst_index(arg):
    for x in arg:
        print(f'Index[{arg.index(x)}] ==> {x}')

#Enter Loop
def enter_loop(enter, x):
    while True:
        try:
            if int(enter) not in range(0, x):
                enter = input('Enter a Valid Index: ')
                continue
        except ValueError:
            enter = input('Enter a Valid Index: ')
            continue
        else:
            break

#Product Menu
def new_ordr(menu, orders):
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
    orders.append(ths_dict)
    print('\n')
    lst_index(orders)

def add_item(menu, orders):
    print('\nOrder:')
    lst_index(orders)
    enter = input('Enter Index to Edit Order: ')
    enter_loop(enter, len(orders))
    lst_index(menu)
    add_inpt = input('Enter Index to Add Item: ')
    enter_loop(add_inpt, len(menu))
    orders[int(enter)]['Order'].append(menu[int(add_inpt)]['Name'])
    orders[int(enter)]['Price'] += menu[int(add_inpt)]['Price']
    print(f'\n{orders[(int(enter))]}')

def dlt_order(orders):
    lst_index(orders)
    enter = input('Enter Index to Delete Order: ')
    enter_loop(enter, len(orders))
    del orders[int(enter)]
    print('\n')
    lst_index(orders)

#Order Directory
def new_custmr_info(custmr_dir):
    print('\nCustomer Information:')
    cstmr_info = {
          "customer_name": input('Name: '),
          "customer_address": input('Address: '),
          "customer_phone": input('Phone Number: '),
          "status": "Preparing"}
    
    custmr_dir.append(cstmr_info)
    print('\n')
    lst_index(custmr_dir)

def edit_ordr_status(enter, custmr_dir):
    lst_index(custmr_dir)
    enter = input('Enter Index to Update Order Status: ')
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

def update_info(custmr_dir):
    print('\n')
    lst_index(custmr_dir)
    enter = input('Enter Index to Update Customer Info: ')
    enter_loop(enter, len(custmr_dir)) 
    custmr_dir[(int(enter))]['customer_name'] = input('Name: ')
    custmr_dir[(int(enter))]['customer_address'] = input('Address: ')
    custmr_dir[(int(enter))]['customer_phone'] = input('Phone: ')
    print('\n')
    lst_index(custmr_dir)

def dlt_custmr_info(custmr_dir):
    print('\n')
    lst_index(custmr_dir)
    enter = input('Enter Index to Delete Customer Info: ')
    enter_loop(enter, len(custmr_dir))
    custmr_dir.pop((int(enter)))
    print('\n')
    lst_index(custmr_dir)

#Courier Menu
def add_courier(courier):
    enter = input('Enter Courier Name to add to list: ')
    courier.append(enter)
    lst_index(courier)

def updt_courier(courier):
    lst_index(courier)
    enter = input('Enter Index to Update Courier: ')
    enter_loop(enter, len(courier))
    updt_name = input('Enter New Name: ')
    courier[int(enter)] = updt_name
    print('\n')
    lst_index(courier)

def dlt_courier(courier):
    lst_index(courier)
    enter = input('Enter Index to Delete Courier: ')
    enter_loop(enter, len(courier))
    del courier[int(enter)]
    print('\n')
    lst_index(courier)