# Author: Hernandez  Lopez Raul  @Neo
# Email:     freeenergy1975@gmail.com
# Date:  Viernes 14 de Julio del 2023

import os
os.environ['PYTHONPATH'] = 'Python_WS/'

from peewee import *
from datetime import datetime
from connection.connection import database

# These templates create the database tables.
class SatisfactionSurvey(Model):
    id_satisfaction_survey = AutoField(primary_key = True)
    level_of_satisfaction = IntegerField()
    coment = TextField()
    folio_ticket = CharField(max_length = 18, unique = True)
    date_and_time = DateTimeField(default = datetime.now)

    def __str__(self):
        return self.id_satisfaction_survey

    class Meta:
        database = database
        table_name = 'satisfaction_survey'
