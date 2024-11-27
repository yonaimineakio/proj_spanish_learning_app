from fastapi import FastAPI
from typing import Dict, List

app = FastAPI()

@app.get("/examples")
async def get_examples() -> Dict[str, List[str]]:
    examples = ["Example 1: FastAPI is great!", 
                "Example 2: TypeScript ensures type safety.", 
                "Example 3: Docker keeps environments consistent."]
    return {"examples": examples}

@app.get("/")
async def root() -> Dict[str, str]:
    return {"message": "Welcome to the FastAPI server!"}
