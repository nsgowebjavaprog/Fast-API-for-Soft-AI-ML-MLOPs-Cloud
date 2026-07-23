# Advanced level and Checking Data-Validation 
# More advanced feature and build the below application

from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict, Optional, Annotated

# Model
class Patient(BaseModel):
    name : Annotated[str, Field(max_length=50, title='Name of the patient', description='Give the name of the patient', examples=['Abc','xrs'])]
    # name : str = Field(max_length=50)
    email : EmailStr
    linkedin_url : AnyUrl
    age: int
    weight: float = Field(gt=0, lt=120)   # gt = greater than 0, 
    married: bool = False
    allergies: Optional[List[str]] = Field(max_lenght=5)
    contact_details : Dict[str, str]

def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.email)
    print(patient.linkedin_url)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)
    print('Data inserted')

patient_info = {
    'name' : 'Nagaraj',
    'email' : 'ns1234@gmail.com',
    'linkedin_url' : 'https://linkedin.com/in/1234',   # use https
    'age' : 30,
    'weight' : 45,
    'married' : True,
    'allergies' : ['pollen', 'dust'],
    'contact_details' : {
        'email' : 'ns1234@gmail.com',
        'phone' : '1234567890'
    }
}

patient_1 = Patient(**patient_info)

insert_patient_data(patient_1)