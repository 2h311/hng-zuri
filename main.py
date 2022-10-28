from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
	CORSMiddleware,
	allow_origins=["*"],
	allow_credentials=["*"],
	allow_methods=["*"],
	allow_headers=["*"],
)

@app.get("/")
def index():
	return { "slackUsername": "olakanmi", "backend": True, "age": 25, "bio": "hello world. I love chihuahuas" }