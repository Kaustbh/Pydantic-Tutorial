from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):

    name: Annotated[str, Field(max_length=50, title="Patient Name", description="Full name of the patient")]
    age: int = Field(gt=0, le=120)
    email: EmailStr
    linkedin_url: AnyUrl
    weight: Annotated[float, Field(gt=0, strict=True)]
    allergies: Optional[List[str]] = Field(max_length=5) , None
    contact_details: Dict[str, str]
    married : Annotated[bool, Field(default=False, description="Is the patient married?")]


def insert_patient(patient: Patient):

    print(f"Inserting patient: {patient.name}, Age: {patient.age}")

    print(type(patient.age))

details = {'name': 'Nitish', 'email': 'abc@gmail.com','linkedin_url': 'htt://www.linkedin.com', 'age': '30', 'weight': 70, 'allergies': ['pollen','dust'], 'contact_details': {'email': 'abc@gmail.com', 'phone': '1234567890'}}

patient1 = Patient(**details)
insert_patient(patient1)