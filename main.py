# python
from typing import Optional
from uuid import UUID, uuid4

# pydantic
from pydantic import BaseModel
from pydantic import Field

# FlaskAPI
from flask import Flask
from flask import request, jsonify

from flask_pydantic import validate

## Models

class Person(BaseModel):
    id : Optional[UUID] = None
    name : str = Field(
        ...,
        min_lenght=1,
        max_length=50
    )
    username : str =  Field(
        ...,
        min_lenght=1,
        max_length=50
    )
    age : int = Field(
        ...,
        gt=0,
        le=110
    )
    user_ip : Optional[str] = None
    
app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
   return {"Hello": "World"}


@app.route('/persons', methods=['POST'])
@validate()
def crrate_person(body: Person):
    person = Person(
        id = uuid4(),
        name = body.name,
        age = body.age,
        username = body.username,
        user_ip= request.remote_addr
    )
   
    return person


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)