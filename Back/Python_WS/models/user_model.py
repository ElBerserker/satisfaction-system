# Author: Hernandez  Lopez Raul  @Neo
# Email:     freeenergy1975@gmail.com
# Date:  Viernes 14 de Julio del 2023

import os
os.environ['PYTHONPATH'] = 'Python_WS/connection'

from peewee import *
from connection.connection import database

# These templates create the database tables.
class User(Model):
    id_user = AutoField(primary_key = True)
    name_of_user = CharField(max_length = 50, unique = True)
    password = CharField(max_length = 40)
    type_of_user = CharField(max_length = 15, default='STANDAR')
    status = CharField(max_length = 10, default='ACTIVE')

    def __str__(self):
        return self.name_of_user

    class Meta:
        database = database
        table_name = 'users'
