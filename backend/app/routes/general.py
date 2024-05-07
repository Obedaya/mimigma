from fastapi import APIRouter, Request
router = APIRouter()

@router.get("/")
def read_root():
    return {"Hello": "World"}


# wird noch in extra Datei verschoben: (vlt. KeyRouter.py?)
@router.get("/output")
def create_output(key = ""):
    if key != "":
        outret = key 
    else:
        outret = "output will appear here"
    return {"output": outret}

@router.post("/input")
def read_input(request: Request):
    key = request.query_params.get("key")
    create_output(key) 
    return {"input": key}
