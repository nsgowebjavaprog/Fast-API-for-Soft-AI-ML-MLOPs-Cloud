from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator
from typing import List, Dict, Optional, Annotated

# Model
class Patient(BaseModel):
    name : Annotated[str, Field(max_length=50, title='Name of the patient', description='Give the name of the patient', examples=['Abc','xrs'])]
    email : EmailStr
    linkedin_url : AnyUrl
    age: int
    weight: float = Field(gt=0, lt=120)
    married: bool = False
    allergies: Optional[List[str]] = Field(default=None, max_length=5)
    contact_details : Dict[str, str]

# --------------------------------------------------
# Name Validator
# --------------------------------------------------

    @field_validator('name')
    @classmethod
    def name_validator(cls, value):
        if len(value.strip()) < 3:
            raise ValueError('Name must contain at least 3 characters')
        return value.title()

# --------------------------------------------------
# Email Validator
# --------------------------------------------------

    @field_validator('email')
    @classmethod
    def email_validator(cls, value):
        valid_domain = ['hdfc.com', 'icici.com']

        domain_name = value.split('@')[-1]

        if domain_name not in valid_domain:
            raise ValueError('Not a valid Domain')

        return value

# --------------------------------------------------
# LinkedIn URL Validator
# --------------------------------------------------

    @field_validator('linkedin_url')
    @classmethod
    def linkedin_validator(cls, value):
        if 'linkedin.com' not in str(value):
            raise ValueError('Enter a valid LinkedIn URL')
        return value

# --------------------------------------------------
# Age Validator
# --------------------------------------------------

    @field_validator('age')
    @classmethod
    def age_validator(cls, value):
        if value < 1 or value > 120:
            raise ValueError('Age must be between 1 and 120')
        return value

# --------------------------------------------------
# Weight Validator
# --------------------------------------------------

    @field_validator('weight')
    @classmethod
    def weight_validator(cls, value):
        if value < 10:
            raise ValueError('Weight should be at least 10 kg')
        return value

# --------------------------------------------------
# Allergies Validator
# --------------------------------------------------

    @field_validator('allergies')
    @classmethod
    def allergies_validator(cls, value):
        if value is not None and len(value) > 5:
            raise ValueError('Maximum 5 allergies are allowed')
        return value

# --------------------------------------------------
# Contact Details Validator
# --------------------------------------------------

    @field_validator('contact_details')
    @classmethod
    def contact_validator(cls, value):

        if 'email' not in value:
            raise ValueError('Email is required in contact_details')

        if 'phone' not in value:
            raise ValueError('Phone is required in contact_details')

        if len(value['phone']) != 10:
            raise ValueError('Phone number must contain exactly 10 digits')

        return value

# --------------------------------------------------

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
    'email' : 'abc@hdfc.com',
    'linkedin_url' : 'https://linkedin.com/in/1234',
    'age' : 30,
    'weight' : 45,
    'married' : True,
    'allergies' : ['pollen', 'dust'],
    'contact_details' : {
        'email' : 'abc@hdfc.com',
        'phone' : '1234567890'
    }
}

patient_1 = Patient(**patient_info)

insert_patient_data(patient_1)