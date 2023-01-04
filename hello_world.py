# Python
from typing import Optional

# Pydantic
from pydantic import BaseModel

# FastAPI
from fastapi import FastAPI, Body, Query, Path

app = FastAPI()

# Models
class Person(BaseModel):
    first_name: str
    last_name: str
    age: int
    hair_color: Optional[str] = None
    is_married: Optional[bool] = None

@app.get("/")
def home():
    return {"Hello" : "World"}

# Request and response body

@app.post("/person/new")
def create_person(person: Person = Body(...)): #variale persion = class Person = object body will response with a body (json) the "..." means that it's mandatory to recive the parameters
    return person

# Validations: Query Parameters

@app.get("/person/detail")
def show_person(
        name: Optional[str] = Query(
            None,
            min_length=1,
            max_length=50,
            title = "Person Name",
            description = "This is the person name, It's between 1 and 50 characters"
            ), # name is an optional string = Query(default_value, min, max)
        age: str = Query(
            ...,
            title = "Person Age",
            description = "This is the person age and it's required"
            ) #Query parameters shouldn't be mandatory, age is an string = Query (mandatory input)
    ):
    return {name : age}

# Path parameters

@app.get("/person/detail/{person_id}")
def show_person(
        person_id: int = Path(
            ...,
            gt=0,
            title= "Person ID",
            description= "This is the person id, must be grater than 0 and is required"
            )
    ):
    return {person_id : "It exists!"}
