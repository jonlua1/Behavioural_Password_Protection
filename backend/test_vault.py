from vault import Vault
from account import Account

vault = Vault()
vault.create_vault(vault.request_master_password())

john = Account("Facebook", "John Smith", "password")

#adding account
user_input = vault.request_master_password()
if(vault.authenticate_user(user_input)):
    vault.add_account(john, user_input)

#delete account
user_input = vault.request_master_password()
if(vault.authenticate_user(user_input)):
    vault.delete_account(1)

#get list of accounts to display
print(vault.get_accounts())

#view password for account
user_input = vault.request_master_password()
if(vault.authenticate_user(user_input)):
    print(vault.view_password(1, user_input))

#edit account password
user_input = vault.request_master_password()
if(vault.authenticate_user(user_input)):
    vault.edit_account(2, "password2", user_input)

#search account
print(vault.search_vault("ohn"))

#edit account
vault.edit_account(1, "Youtube", "Bob")

