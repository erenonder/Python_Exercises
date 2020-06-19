import os

# add these type of secret information
# to bash_profile as keys and use from os module
# if this is not working probably i deleted the keys from
# .bash_profile

# db_user = os.environ.get('DB_USER1', default='no_user')
# db_password = os.getenv('DB_PASS1', default='no_pass')

db_user = os.getenv('DB_USER', default='no_user')
db_password = os.getenv('DB_PASS', default='no_pass')

print(db_user)
print(db_password)
