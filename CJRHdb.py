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
    elif choice in ('q', "Q"):
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
    # asking to see what one the user wants it ordered in
    whichWay = input("Do you want it by Name, Catches, or Country? N or C or Co ")
    # if statements to check whichWay to order the db info
    if whichWay in ("Name", "N", "n"):
        # printing the record for the user
        for row in cur.execute('select * from recordHolder ORDER BY personsName '):
            print(row)
    elif whichWay in ("Catches",  "C", "c"):
        # printing the record for the user
        for row in cur.execute('select * from recordHolder ORDER BY catches desc'):
            print(row)
    elif whichWay in ("Country", "country", "Co", "co"):
        # printing the record for the user
        for row in cur.execute('select * from recordHolder ORDER BY country'):
            print(row)
    # else statement if the user doesn't choose one of the options
    else:
        print("please pick one")
        see_record()
    # calling the main method after the printout
    main()

def add_record():
    # try statement incase of inccorect input for interger
    try:
        # getting input from the user
        personsName = input('Enter name of a chainsaw juggling record holder: ')
        # formating for the db
        personsName = personsName.lower().title()
        country = input('Enter the country they are from: ')
        country = country.lower().title()
        catches = int(input('Enter number of catches (as a integer): '))
        # sending the information to the datebase command line
        cur.execute('insert into recordHolder values (?, ?, ?)', (personsName, country, catches))

        db.commit() #save changes

        # asking the user if they want to add another
        anotherPersonAdd = input("Would you like to another person? Y or N ")
        # asking user if they want to add another
        if anotherPersonAdd in ("y", "Y"):
            # recalling add program
            add_record()
        # else statement to recall the main
        else:
            # calling main program
            main()

    # errror handling
    except ValueError:
        print("Needs to be a number")
        add_record()


def search_record():
    # varible to check the db
    lookingFor = input('Who are you looking for? ')
    lookingFor = lookingFor.lower().title()

    # calling the database for that person
    personRecord = cur.execute("select * from recordHolder where personsName = ?" , (lookingFor,))
    print(personRecord.fetchone())
    # calling the main
    main()

def update_record():
    try:
        # getting input from the user
        whoUpdating = input('Who do you want to update? ')
        # formating the information from the user
        whoUpdating = whoUpdating.lower().title()
        whatToUpdate = input('What do you want to update Name, Country, or Catches? ')
        # if statement to direct what changes the user wants to make
        if whatToUpdate in ("Name", "N", 'n', "name"):
            whatToUpdate = "personsName"
            newInputUpdate = input('What do you want to change it to? ')
            newInputUpdate = newInputUpdate.lower().title()
        elif whatToUpdate in ("Country", "Co", "co", "country"):
            whatToUpdate = "country"
            newInputUpdate = input('What country do you want to changed to? ')
            newInputUpdate = newInputUpdate.lower().title()
        elif whatToUpdate in ("Catches", "Ca", "ca", "catches"):
            whatToUpdate = "catches"
            newInputUpdate = int(input('how many catches do you want to changed to? '))
        # else statement if they don't choose on of the options
        else:
            print("Needs to be either Name (N) or Country (Co) or Catches (Ca)")

        # making sure the user wants to make the update
        areYouSure = input('Are you sure you want to update '+ whatToUpdate + ' for ' + whoUpdating + ' ? Y or N ')

        # if statment to make changes or not
        if areYouSure in ('Y', 'y', 'Yes'):
            print(whatToUpdate + newInputUpdate + whoUpdating,)

            cur.execute("UPDATE recordHolder set {} = ? where personsName = ?".format(whatToUpdate),(newInputUpdate, whoUpdating,))
            db.commit()
            print('The person ' + whoUpdating + ' now has ' + newInputUpdate + ' in ' + whatToUpdate)
        else:
            print("Record is unchanged")
            main()

        main()

    # error handler to check the interger
    except ValueError:
        print("Needs to be a number")

def delete_record():
    # getting the record that the user wants to delete
    whoToDelete = input("Who whould you like to delete? ")
    # making sure the user wants to delete the record
    areYouSure = input("Are you sure you want to delete " + whoToDelete + " ?")
    # if statement for deleting the record or not
    if areYouSure in ("Yes", "yes", "Y", "y"):
        cur.execute('DELETE FROM recordHolder WHERE personsName = ?', (whoToDelete,))
        print("Recorded deleted")
        main()
    else:
        print("record not deleted")
        main()


def restart_record():
    # this is a hidden option to reset the db back to the beginning
    try:
        making sure they want to reset the database
        reset_record = input('Would you like to restart the record? Y or N ')

        # if statement to reset the db or not
        if reset_record in ('Y', 'y'):
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

            main()
        else:
            print('Did not reset the db')
            main()

    # error handling if there is a problem and roll back the db
    except sqlite3.Error as e:

        print('rolling back changes because of error:', e)
        traceback.print_exe() #displays a stack trace, for debugging
        db.rollback()

# calling the main program
if __name__ == '__main__':
    main()
