import re
from operator import add, sub, mul
from enum import Enum

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

class OperationType(Enum):
	ADDITION = "addition"
	SUBTRACTION ="subtraction"
	MULTIPLICATION = "multiplication"


class RequestBodyModel(BaseModel):
	x: int | None = None
	y: int | None = None
	operation_type: OperationType


class ResponseBodyModel(BaseModel):
	slackUsername: str = "olakanmi"
	operation_type: OperationType
	result: int


operation_dict = {
	OperationType.ADDITION: add,
	OperationType.SUBTRACTION: sub,
	OperationType.MULTIPLICATION: mul
}


app = FastAPI()
# app.add_middleware(
# 	CORSMiddleware,
# 	allow_origins=["*"],
# 	allow_credentials=["*"],
# 	allow_methods=["*"],
# 	allow_headers=["*"],
# )


@app.get("/")
def index():
	return { "slackUsername": "olakanmi", "backend": True, "age": 25, "bio": "hello world. I love chihuahuas" }


@app.post("/")
async def create_result(request_body: RequestBodyModel):

	x, y = request_body.x, request_body.y
	operation_type = request_body.operation_type
	operation_type_value = operation_type.value 
	
	func = operation_dict[operation_type]
	result = func(x, y)
	return {"slackUsername": "olakanmi", "result": result, "operation_type": operation_type_value, }	
