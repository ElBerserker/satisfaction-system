# Author: Hernandez  Lopez Raul  @Neo
# Email:     freeenergy1975@gmail.com
# Date: Viernes 14 de Julio  del 2022

from pydantic import BaseModel
from typing import Optional

class SatisfactionSurveyBaseModel(BaseModel):
    level_of_satisfaction: int
    coment: str
    # Indicates that the data type is optional and if
    # not specified a default value will be assigned.
    folio_ticket: Optional[str] = None
