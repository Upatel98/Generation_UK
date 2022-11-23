Generation UK - Mini-Project (Week 1 - Week 5)

Description:
A client has launched a pop-up café and they require a software application which helps them log and track orders. The software application works as a User Interface 
and runs on the Command Line performing different operations depending on the client’s needs. 

Client Requirements:
- Maintain a collection of products and couriers' information.
- Record a customer's new order onto the system and be able to update their information and their order status.
- At the start of the application all persisted data is loaded to the program.
- After the end of the application all data is persisted and saved. 
- Perform a Unit Test to test and ensure the app program is proven to works.
- Receive regular software updates.

Application Requirements:
- Python 3.10.9
- Docker Desktop
- CSV 
- Terminal
- Git/GitHub
- Packages:
  - csv
  - os
  - pymysql

Project Design:
The whole projects workout load was split into weekly goals in order to focus on each area of the applications code. Each of the applications individuals’ menus were  
focused on initially with their respective functions. During each week the code was reviewed and any possible improvements where made. 

The structure of the code was examined first, as it contains multiple while loops and if statements performing different operations, to another coder it would be hard 
to understand/examine due to the code being bulky. Therefore two files were made, the initial file to run the application and a second file to act as an ecosystem 
containing multiple functions to perform operations depending on the if statement. The initial code is more easily read, with anyone able to read and understand what
each if statement code executes and the functions in the ecosystem file can be examined and debugged if necessary. 

To contain the product and courier information initially a list variable was used however this created an issue of not persisting the data. Therefore, at different 
stages of project design either a text or CSV file to contain/access and edit the data. In the end an online host was used to create a SQL database. This was accessed
through a python file in a virtual environment run through a docker container. 

Example of the Project Code:

from mp_ecosystem import new_order, updt_order_status, updt_order, dlt_order

orders = []
read_orders_csv(orders)

while True:
  print('\n---Welcome---\n[Index 0] ==> Exit App\n[Index 1] ==> Products Menu\n[Index 2] ==> Couriers Menu\n[Index 3] ==> Orders Menu')
  entr = input('Enter Index: ')
  entr = inpt(entr, 4)
  cls_trmnl()

  if entr == 0:
    close_database()
    write_orders_csv(orders)
    print('Exit, Thank You')
    break

Example of Code Ecosystem:

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

Guarantee Project Requirements:

Improvements:
- Currently the projects file structure is not organised and unstructured. Inside the directory there are multiple other files from other projects, there is a virtual 
  environment running but only for the project files and not for the additional files and using git has become more of a task due to the untracked/additional files.
- Streamline the applications code by removing/combining lines of code to maximise python performance.
- Use more advance python programming skills like object orientation programming techniques. 
- Improve the visuals of the User Interface in the Command Line. 
