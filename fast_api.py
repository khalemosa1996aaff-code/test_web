from typing import Annotated, Literal

from fastapi import FastAPI, Query,Body,Cookie,Header
from pydantic import BaseModel, Field

app = FastAPI()

@app.get("/test/")
async def read_coockie(myid: Annotated[int | None,Header()]=None):
    return myid