# Author: Hernandez  Lopez Raul  @Neo
# Email:     freeenergy1975@gmail.com
# Date:Miercoles 19 de enero del 2022

from pydantic import BaseModel
from typing import Optional

# Models for evaluating input data types
class UserBaseModel(BaseModel):
    name_of_user: str
    password: str
    # Indicates that the data type is optional and if 
    # not specified a default value will be assigned.
    type_of_user: Optional[str] = 'STANDAR'
    status: Optional[str] = 'ACTIVE'
