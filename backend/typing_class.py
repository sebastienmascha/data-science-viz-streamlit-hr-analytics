from pydantic import BaseModel


class PersonData(BaseModel):
    gender: str
    relevent_experience: str
    enrolled_university: str
    education_level: str
    major_discipline: str
    experience: str
    company_size: str
    company_type: str
    last_new_job: str
    training_hours: str
    city_development_index: str
    city: str