from fastapi import FastAPI, Path, HTTPException, Query
import json
app = FastAPI()

# 1 Simple working of FastAPI
'''
@app.get("/")

def greeting_u():
    return "Good Morning"

    # OR
    
    # return {'message': 'Good Morning [23-07-2026]'}

@app.get("/about")
def date():
    return "23/07/2026"    
    
'''

# 2  HTTP Methods
'''
# reeturn data  ----> HTTP GET METHOS
@app.get("/")

def greeting_u():
    return "Data related"


def load_data():
    with open('patients.json', 'r') as f:
        data = json.load(f)
    return data    

@app.get('/view')
def view():
    data = load_data()
    return data

'''

# 3 Path Params in FastAPI
'''
def load_data():
    with open('patients.json', 'r') as f:
        data = json.load(f)
    return data


@app.get('/patients/{id}')   # http://127.0.0.1:8000/patients/P001
def patients_data_by_id(id):
    data = load_data()
    if id in data:
        return data[id]
    else:
        return "DATA NOT-FOUND"
            
'''
# Path
'''
@app.get('/patients/{id}') 
def patients_data_by_id(id:str = Path(..., description='Id of the patient present in DB', example='P001')):
    data = load_data()
    if id in data:
        return data[id]
    # else:
    #     # return "DATA NOT-FOUND"
    raise HTTPException(status_code=404, detail='Patient not found')    
'''

# 4 Query Params in FastAPI

'''
def load_data():
    with open('patients.json', 'r') as f:
        data = json.load(f)
    return data


@app.get('/sort')
def sort_patients(sort_by: str=Query(..., description='Sort on bases of height, weigth, bmi'), order: str=Query('asc', description='sort in ascending/desending order')):
    valid_feilds = ['height', 'weight', 'bmi']
    if sort_by not in valid_feilds:
        raise HTTPException(status_code=400, detail=f'invalid feilds{valid_feilds}')
    
    if order not in ['asc', 'desc']:
        raise HTTPException(status_code=400, details='invalid order selected b/w asc&desc')
    
    data = load_data()
    
    sorder_data = ''
    return sorder_data
'''


# Pydantic Crash Course | Data Validation in Python |




# 



# 




# 




# 




# 




# 