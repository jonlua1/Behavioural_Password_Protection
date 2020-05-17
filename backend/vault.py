import os
import sqlite3
from sqlite3 import Error

from account import Account
from crypto import encrypt, decrypt, generate_hash, check_hash

class Vault():
    def __init__(self):
        pass

    #create vault db
    def create_vault(self, master_password, vault_db):
       
        sql_create_accounts_table = """CREATE TABLE IF NOT EXISTS accounts (
                                        id INTEGER PRIMARY KEY,
                                        account VARCHAR NOT NULL,
                                        user_name VARCHAR NOT NULL,
                                        password BLOB NOT NULL
                                    );"""

        sql_create_master_table = """CREATE TABLE IF NOT EXISTS master (
                                        hash BLOB NOT NULL
                                    );"""

        data = generate_hash(master_password)

        insert_data = """INSERT INTO master(hash)
                            VALUES(?)"""
        
        #create a database connection
        conn = self.create_connection(vault_db)
        
        #create tables
        if conn is not None:
            #create accounts table
            try:
                cur = conn.cursor()
                cur.execute(sql_create_accounts_table)
                cur.execute(sql_create_master_table)
                cur.execute(insert_data, (data,))
                conn.commit()
                conn.close()
            except Error as e:
                print(e)
        else:
            print("Cannot create the database connection.")

    #add account to vault
    def add_account(self, website, password, user_name, master_password):
        #vault db file path
        vault_db = os.path.expanduser('~\Documents\ezPass\\vault')

        #ezPass logs folder path
        folder_path = os.path.expanduser('~\Documents\ezPass')
        os.chdir(folder_path)

        add_account_sql = """INSERT INTO accounts(account, user_name, password)
                            VALUES(?,?,?)"""
        
        encrypted_password = encrypt(password, master_password)

        #create a database connection
        conn = self.create_connection(vault_db)
        with conn:
            cur = conn.cursor()
            cur.execute(add_account_sql, (website, user_name, encrypted_password))


    #delete account based on website and user_name in vault
    def delete_account(self, id):
        #vault db file path
        vault_db = os.path.expanduser('~\Documents\ezPass\\vault')

        #ezPass logs folder path
        folder_path = os.path.expanduser('~\Documents\ezPass')
        os.chdir(folder_path)

        delete_account_sql = """DELETE FROM accounts WHERE id = ? """

        #create a database connection
        conn = self.create_connection(vault_db)
        with conn:
            cur = conn.cursor()
            cur.execute(delete_account_sql, (id,))
            conn.commit()
 
    #get account data from database 
    def get_accounts(self):
        #vault db file path
        vault_db = os.path.expanduser('~\Documents\ezPass\\vault')

        #ezPass logs folder path
        folder_path = os.path.expanduser('~\Documents\ezPass')
        os.chdir(folder_path)

        #create a database connection
        conn = self.create_connection(vault_db)
        with conn:
            cur = conn.cursor()
            cur.execute("""SELECT id, account, user_name FROM accounts ORDER BY account ASC""")
            rows = cur.fetchall()
        
        return rows

    #create a database connection to the SQLite database specified by db_file
    #return Connection object or None
    def create_connection(self, db_file):
        conn = None
        try:
            conn = sqlite3.connect(db_file)
        except Error as e:
            print(e)
        
        return conn

    def request_master_password(self):
        master_password = input("Please enter master password: ")
        return master_password

    #authenticate user by checking if the password matches the 
    #hashed one in the database
    def authenticate_user(self, master_password):
        #vault db file path
        vault_db = os.path.expanduser('~\Documents\ezPass\\vault')

        #ezPass logs folder path
        folder_path = os.path.expanduser('~\Documents\ezPass')
        os.chdir(folder_path)

        #create a database connection
        conn = self.create_connection(vault_db)
        with conn:
            cur = conn.cursor()
            cur.execute("""SELECT hash FROM master""")
            rows = cur.fetchall()
        
        data = rows[0][0]

        return check_hash(data, master_password)

    #view password of account upon authentication
    def view_password(self, id, master_password):
        #vault db file path
        vault_db = os.path.expanduser('~\Documents\ezPass\\vault')

        #ezPass logs folder path
        folder_path = os.path.expanduser('~\Documents\ezPass')
        os.chdir(folder_path)

        #create a database connection
        conn = self.create_connection(vault_db)
        with conn:
            cur = conn.cursor()
            cur.execute("""SELECT password FROM accounts where id = ?""", (id,))
            rows = cur.fetchall()

        data = rows[0][0]
        return bytes.decode(decrypt(data, master_password))

    #edit password on selected account
    def edit_account_password(self, id, new_password, master_password):
        #vault db file path
        vault_db = os.path.expanduser('~\Documents\ezPass\\vault')

        #ezPass logs folder path
        folder_path = os.path.expanduser('~\Documents\ezPass')
        os.chdir(folder_path)

        encrypted_password = encrypt(new_password, master_password)

        #create a database connection
        conn = self.create_connection(vault_db)
        with conn:
            cur = conn.cursor()
            cur.execute("""UPDATE accounts
                            SET password = ?
                            WHERE id = ?"""
                            ,(encrypted_password, id))
        
        print("Account password successfully updated")

    #search vault and return accounts which contains words from user_input
    def search_vault(self, search_input):
        #vault db file path
        vault_db = os.path.expanduser('~\Documents\ezPass\\vault')

        #ezPass logs folder path
        folder_path = os.path.expanduser('~\Documents\ezPass')
        os.chdir(folder_path)

        #create a database connection
        conn = self.create_connection(vault_db)
        with conn:
            cur = conn.cursor()
            cur.execute("""SELECT id, account, user_name
                            FROM accounts
                            WHERE account OR user_name LIKE ?
                            ORDER BY account ASC"""
                            ,('%'+search_input+'%',))
            rows = cur.fetchall()
        
        return rows

    #edit account name and user name based on account id
    def edit_account(self, id, account_name, user_name):
        #vault db file path
        vault_db = os.path.expanduser('~\Documents\ezPass\\vault')

        #ezPass logs folder path
        folder_path = os.path.expanduser('~\Documents\ezPass')
        os.chdir(folder_path)

        #create a database connection
        conn = self.create_connection(vault_db)
        with conn:
            cur = conn.cursor()
            cur.execute("""UPDATE accounts
                            SET account = ?, user_name = ?
                            WHERE id = ?"""
                            ,(account_name, user_name, id))

        print("Account successfully updated")