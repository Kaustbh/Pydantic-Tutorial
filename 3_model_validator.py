from pydantic import BaseModel, EmailStr, AnyUrl, Field, model_validator
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

    @model_validator(mode='after')
    def validate_emergency_contact(cls, model):
        if model.age > 60 and 'emergency' not in model.contact_details:
            raise ValueError("Emergency contact is required for patients over 60 years old.")

        return model
   


def insert_patient(patient: Patient):

    print(f"Inserting patient: {patient.name}, Age: {patient.age}")

    print(type(patient.age))

details = {'name': 'Nitish', 'email': 'abc@hdfc.com','linkedin_url': 'htt://www.linkedin.com', 'age': 50, 'weight': 70, 'allergies': ['pollen','dust'], 'contact_details': {'email': 'abc@gmail.com', 'phone': '1234567890'}}

patient1 = Patient(**details)
insert_patient(patient1)