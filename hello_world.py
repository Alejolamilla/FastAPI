# Python
from typing import Optional
from enum import Enum #to enumerate strings

# Pydantic
from pydantic import BaseModel, Field # same as body, query or path but related to pydantic

# FastAPI
from fastapi import FastAPI, Body, Query, Path

app = FastAPI()

# Models
class HairColor(Enum):
    white = "white"
    brown = "rown"
    black = "Black"
    blonde = "blonde"
    red = "red"

class Person(BaseModel):
    first_name: str = Field(
        ...,
        min_length=1,
        max_length=50,
        example="Alejandro"
        )
    last_name: str = Field(
        ...,
        min_length=1,
        max_length=50,
        example="Tovar"
        )
    age: int = Field(
        ...,
        gt=0,
        le=115,
        example=25
    )
    hair_color: Optional[HairColor] = Field(default=None, example="Black")
    is_married: Optional[bool] = Field(default=None, example="false")

"""    class config:
        schema_extra = {
            "example": {
                "first_name" : "Alejandro",
                "last_name" : "Tovar",
                "age" : "25",
                "hair_color" : "Black",
                "is_married" : "false"
            }
        } """

class Location(BaseModel):
    city: str
    state: str
    country: str


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

# Vaalidation: Request Body

@app.put("/person/{person_id}")
def update_person(
        person_id: int = Path(
            ...,
            title= "Person ID",
            description="This is the person ID",
            gt=0
        ),
        person: Person = Body(...),
       # location: Location = Body(...)
    ):
    #results = person.dict()
    #results.update(location.dict())

    return person