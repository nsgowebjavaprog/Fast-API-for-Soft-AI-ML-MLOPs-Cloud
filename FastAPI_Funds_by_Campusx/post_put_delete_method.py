from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr, Field
from typing import Optional
import json

app = FastAPI()

# ------------------------------------
# Load Data
# ------------------------------------

def load_data():
    with open("patients.json", "r") as f:
        data = json.load(f)
    return data


# ------------------------------------
# Save Data
# ------------------------------------

def save_data(data):
    with open("patients.json", "w") as f:
        json.dump(data, f, indent=4)


# ------------------------------------
# Request Body
# ------------------------------------

class Patient(BaseModel):
    id: str
    name: str = Field(..., min_length=3, max_length=50)
    age: int = Field(..., gt=0, lt=120)
    email: EmailStr
    weight: float = Field(..., gt=0)
    height: float = Field(..., gt=0)
    married: bool = False
    city: Optional[str] = None


# ==================================================
# 1. POST Method [CREATE]
# ==================================================

@app.post("/create")
def create_patient(patient: Patient):

    data = load_data()

    if patient.id in data:
        raise HTTPException(
            status_code=400,
            detail="Patient already exists"
        )

    data[patient.id] = patient.model_dump()

    save_data(data)

    return {
        "message": "Patient Added Successfully",
        "patient": patient
    }


# ==================================================
# 2. PUT Method [UPDATE]
# ==================================================

@app.put("/update")
def update_patient(patient: Patient):

    data = load_data()

    if patient.id not in data:
        raise HTTPException(
            status_code=404,
            detail="Patient not found"
        )

    data[patient.id] = patient.model_dump()

    save_data(data)

    return {
        "message": "Patient Updated Successfully",
        "patient": patient
    }


# ==================================================
# 3. DELETE Method [DELETE]
# ==================================================

@app.delete("/delete/{patient_id}")
def delete_patient(patient_id: str):

    data = load_data()

    if patient_id not in data:
        raise HTTPException(
            status_code=404,
            detail="Patient not found"
        )

    deleted_patient = data.pop(patient_id)

    save_data(data)

    return {
        "message": "Patient Deleted Successfully",
        "patient": deleted_patient
    }