from pydantic import BaseModel
from typing import List, Dict, Optional
'''
# 1. Pydantic Model Building

from pydantic import BaseModel

class Patient(BaseModel):
    name : str
    age: int
    
def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print('Data inserted')  
    
# Update
def update_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print('Data Updated')        
    
# Obj for pydantic

# patient_info = {'name' : 'Nagaraj', 'age':30}
patient_info = {'name' : 'Nagaraj', 'age':'30'} # age is str but need id int it automaticcally update/do it

# Step-3
patient_1 = Patient(**patient_info)

insert_patient_data(patient_1)


'''


# Advanced level Pydantic  

# 1. Pydantic Model Building


class Patient(BaseModel):
    name : str
    age: int
    weight: float
    married: bool
    allergies: Optional[List[str]] = None
    contact_details : Dict[str, str]
    
def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)
    print('Data inserted')  
    
# Update
def update_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print('Data Updated')        
    
# Obj for pydantic

patient_info = {'name' : 'Nagaraj', 'age':30, 'weight': 45, 'married':True, 'allergies': ['pollen', 'dust'], 'contact_details' : {'email':'ns1234@gmail.com', 'phone': '1234567890'}}

# patient_info = {'name' : 'Nagaraj', 'age':'30'} # age is str but need id int it automaticcally update/do it

# Step-3
patient_1 = Patient(**patient_info)

insert_patient_data(patient_1)