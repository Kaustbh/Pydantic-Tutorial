from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):

    name: str
    age: int
    email: EmailStr
    linkedin_url: AnyUrl
    weight: float
    allergies: Optional[List[str]] = None
    contact_details: Dict[str, str]
    married : bool = None

    @field_validator('email')
    @classmethod
    def email_validator(cls, value):

        valid_domains = ['hdfc.com', 'icici.com']
        # abc@gmail.com

        domain_name = value.split('@')[-1]
        if domain_name not in valid_domains:
            raise ValueError(f"Email domain must be one of {valid_domains}")

        return value
    
    @field_validator('name')
    @classmethod
    def name_validator(cls, value):
        return value.upper()
    
    @field_validator('age', mode='before')
    @classmethod
    def age_validator(cls, value):
        if 0 < value < 100:
            return value
        else:
            raise ValueError("Age must be between 1 and 99")


def insert_patient(patient: Patient):

    print(f"Inserting patient: {patient.name}, Age: {patient.age}")

    print(type(patient.age))

details = {'name': 'Nitish', 'email': 'abc@hdfc.com','linkedin_url': 'htt://www.linkedin.com', 'age': 30, 'weight': 70, 'allergies': ['pollen','dust'], 'contact_details': {'email': 'abc@gmail.com', 'phone': '1234567890'}}

patient1 = Patient(**details)
insert_patient(patient1)