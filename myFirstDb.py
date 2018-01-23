import sqlite3
import traceback

try:
    db = sqlite3.connect('my_first_db.db') # creates or opens db files

    cur = db.cursor() #need a cursor object to perform operations

    #create table
    cur.execute('create table if not exists phones (brand text, version int)')

    brand = input('Enter Brand of Phone: ')
    version = int(input('Enter version of phone(as a integer): '))

    #add some
    # cur.execute('insert into phones values ("Android", 5)')
    # cur.execute('insert into phones values ("iPhone", 6)')
    cur.execute('insert into phones values (?, ?)', (brand, version))

    # db.commit() #save changes


    for row in cur.execute('select * from phones'):
        print(row)

    db.commit()

    # db.close()

except sqlite3.Error as e:

    print('rolling back changes because of error:', e)
    traceback.print_exe() #displays a stack trace, for debugging
    db.rollback()

finally:
    print('closing database')
    db.close()
