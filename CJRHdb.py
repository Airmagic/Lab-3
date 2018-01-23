import sqlite3
import traceback

# pointing to the db file
db = sqlite3.connect('CJRH.db') # creates or opens db files

# making variable for accessing the db
cur = db.cursor() #need a cursor object to perform operations

# main program
def main():
    # displaying the choice menu
    choice_menu()
    # getting input from user
    choice = input('Enter your selection: ')
    # 1. Showing the list of the records
    if choice == '1':
        see_record()

    # 2. adding a new record to the table
    elif choice == '2':
        add_record()

    # 3. searching the record
    elif choice == '3':
        search_record()

    # 4. updating a record
    elif choice == '4':
        update_record()

    # 5. Deleting a record from the table
    elif choice == '5':
        delete_record()

    # 6. Restarting the record from basic
    elif choice == '6':
        restart_record()

    # q. Quit
    elif choice == 'q':
        db.close()
        quit()

    # message to show if input is not in the menu
    else:
        print('Please enter a valid selection')
        main()

def choice_menu():
    '''Display choices for user, return users' selection'''

    print('''
        Chainsaw Juggling Record Holder Program
        ---------------------------------------
        1. See record list
        2. Add a new record
        3. Search for record
        4. Update a record
        5. Delete a record
        q. Quit
    ''')

def see_record():
    # printing the record for the user
    for row in cur.execute('select * from recordHolder'):
        print(row)
    # recalling the main program
    main()

def add_record():
    # getting input from the user
    personsName = input('Enter name of a chainsaw juggling record holder: ')
    country = input('Enter the country they are from: ')
    catches = int(input('Enter number of catches (as a integer): '))
    anotherPersonAdd = input("Would you like to another person? Y or N ")
    # sending the information to the datebase command line
    cur.execute('insert into recordHolder values (?, ?, ?)', (personsName, country, catches))

    db.commit() #save changes

    # asking user if they want to add another
    if anotherPersonAdd == "y" or anotherPersonAdd == "Y":
        # recalling add program
        add_record()
    # else statement to recall the main
    else:
        main()

def search_record():
    # varible to check the db
    lookingFor = input('Who are you looking for? ')
    #
    persongRecord = cur.execute('select personName from recordHolder')
    print(personRecord)

    main()

def update_record():
    pass

def delete_record():
    pass

def restart_record():
    try:

        reset_record = input('Would you like to restart the record? Y or N ')

        if reset_record == 'Y' or reset_record == 'y':
            cur.execute('drop table recordHolder')# deleting table
            db.commit()

            #create table
            cur.execute('create table recordHolder (personsName text, country text, catches int)')
            cur.execute('Insert into recordHolder values ("Ian Stewart", "Canada", 94) ')
            cur.execute('Insert into recordHolder values ("Aaron Gregg", "Canada", 88) ')
            cur.execute('Insert into recordHolder values ("Chad Taylor", "USA", 78) ')



            #add some

            # cur.execute('insert into recordHolder values (?, ?, ?)', (personsName, country, catches))

            db.commit() #save changes


            for row in cur.execute('select * from recordHolder'):
                print(row)

            db.commit()

            main()
        else:
            print('Did not delete the db')
            main()

    except sqlite3.Error as e:

        print('rolling back changes because of error:', e)
        traceback.print_exe() #displays a stack trace, for debugging
        db.rollback()

    # finally:
    #     print('closing database')
    #     db.close()

if __name__ == '__main__':
    main()
