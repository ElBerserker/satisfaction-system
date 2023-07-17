# Author: Hernandez  Lopez Raul  @Neo
# Email:     freeenergy1975@gmail.com
# Date:  Viernes 17 de Julio del 2022


from fastapi import APIRouter
from models.survey_model import SatisfactionSurvey
from schemas.survey_schema import SatisfactionSurveyBaseModel

survey = APIRouter()

@survey.post('/satisfaction_survey/')
async def create_satisfaction_survey(satisfaction_survey: SatisfactionSurveyBaseModel):
    satisfaction_survey = SatisfactionSurvey.create(
        level_of_satisfaction = satisfaction_survey.level_of_satisfaction,
        coment = satisfaction_survey.coment,
        folio_ticket = satisfaction_survey.folio_ticket
    )

    return satisfaction_survey.id_satisfaction_survey

@survey.get('/surveys/')
async def get_surveys():
    survey = SatisfactionSurvey.select()
    return list(survey)
        
