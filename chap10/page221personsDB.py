#!/usr/local/bin/python3 
# page 221 My implementation of database.py with enhancements for handling some exceptions
import sys, shelve, os
db_store_file = '/home/yourusrename/Documents/PYTHONbooks/Beginning.Python.3rdEd.2017/ch10/persons.dat'

def IDexists(pid, pdb):
    try:
        info = pdb[pid]
        return True
    except KeyError:
        return False
    
def delete_person(db):
    pid = input('Enter unique ID number of person to remove: ')
    if IDexists(pid, db):
        del db[pid]
    else:
        print("This ID does not exist. Nothing to remove!")
    
def store_person(db):
    """
    Query user for data and store it in the shelf object
    """ 
    pid = input('Enter unique ID number: ')
    if IDexists(pid, db):
        print("The ID you gave already exists:", pid)
        print(db[pid])
        answer = input("Do you want to overwrite it? (N/y)")
        if answer.strip().lower() == 'n':
            print("  Not altering existing record")
            return    # do nothing more and exit function store_person(), else for 'y' continue with next lines
    person = {}          # initially empty dictionary, to be populated by users entered values
    person['name'] = input('Enter name: ')
    person['age'] = input('Enter age: ')
    person['phone'] = input('Enter phone number: ')
    db[pid] = person  # adding this small person dictionary to the others, exisitng in database  
        
def lookup_person(db):
    """
    Query user for ID and desired field, and fetch the corresponding data from the shelf object
    """
    pid = input('Enter ID number: ')
    try:
        info = db[pid]
        field = input('What would you like to know? (name, age, phone, all) ')
        field = field.strip().lower()
        try:
            info = db[pid][field]
            print(field.capitalize() + ':', db[pid][field])
        except KeyError:
            if field != 'all':    # user typed something strange, give him a message about it, and the whole info
                print(field, " is not a recognized field of information. Printing all fields of ",pid, ":")
            print(info)           # if user typed 'all', of course we again print the whole info 
    except KeyError:
        print("The ID you gave ", pid, " does not exists in the database of persons!")
    
def enter_command():
    cmd = input('Enter command (? for help): ')
    cmd = cmd.strip().lower()
    return cmd

def print_help():
    print('The available commands are:')
    print('store  : Stores information about a person')
    print('lookup : Looks up a person from ID number')
    print('quit   : Save changes and exit')
    print("delete : removes a person's record")
    print('?      : Prints this message')

def main():
    database = shelve.open(db_store_file)
    print("The database is opened, placed in RAM, and it has an object-type of :", type(database))
    try:
        while True:
            cmd = enter_command()
            if  cmd == 'store':
                store_person(database)
            elif cmd == 'lookup':
                lookup_person(database)
            elif cmd == 'delete':
                delete_person(database)
            elif cmd == '?':
                print_help()
            elif cmd == 'quit':
                return
            else:
                print("Not recognized input")
                print_help()
    finally:
        print("Even if something bad happened, do not worry! I am closing the databese now!")
        database.close()

if __name__ == '__main__':
    main()
