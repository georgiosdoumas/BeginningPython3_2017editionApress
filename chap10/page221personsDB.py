#!/usr/local/bin/python3 
# page 221 My implementation of database.py with enhancements for handling some exceptions
import sys, shelve, os
db_store_file = '/home/gdoumas/Documents/ProgrammingOther/PYTHONbooks/Beginning.Python.3rdEd.2017/ch10/persons.dat'

def IDexists(pid, pdb):
    try:
        info = pdb[pid]
        return True
    except KeyError:
        return False
    
def store_person(db):
    """
    Query user for data and store it in the shelf object
    """
    pid = input('Enter unique ID number: ')
    if IDexists(pid, db):
        print("The ID you gave already exists:", pid)
        print(db[pid])
    else:
        person = {}     # initially empty dictionary, to be populated by users entered values
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
        if field == 'all':
            print(info)
        else:
            try:
                info = db[pid][field]
                print(field.capitalize() + ':', db[pid][field])
            except KeyError:
                print(field, " is not a recognized field of information. Printing all fields of ",pid, ":")
                print(info)
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
    print('?      : Prints this message')


def main():
    database = shelve.open(db_store_file)
    print("The database is opened, and its type is :", type(database))
    try:
        while True:
            cmd = enter_command()
            if  cmd == 'store':
                store_person(database)
            elif cmd == 'lookup':
                lookup_person(database)
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
