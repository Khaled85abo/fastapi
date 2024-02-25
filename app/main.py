from fastapi import FastAPI, UploadFile,  HTTPException, Depends, status
from fastapi.responses import FileResponse
from app.db_setup import init_db, get_db
from contextlib import asynccontextmanager
from fastapi import Request
from sqlalchemy.orm import Session, joinedload, selectinload
from sqlalchemy import select, update, delete, insert
from app.database.models import Company, CompanyType
from app.database.schemas import CompanySchema, CompanyOutSchema, CompanyTypeSchema, CompanyTypeOutSchema
from uuid import uuid4
import os
# Funktion som körs när vi startar FastAPI -
# perfekt ställe att skapa en uppkoppling till en databas
IMAGEDIR = "images/"
@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db() # Vi ska skapa denna funktion
    yield

app = FastAPI(lifespan=lifespan)

@app.get("/company", status_code=200, tags=["company"])
def list_companies(db: Session = Depends(get_db)) -> list[CompanySchema]:
    programs = db.scalars(select(Company)).all()
    if not programs:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No companies found")
    return programs


@app.post("/company", status_code=201, tags=["company"])
def add_company( company: CompanySchema  ,db: Session = Depends(get_db)) -> CompanyOutSchema:
    db_company = Company(**company.model_dump())
    db.add(db_company)
    db.commit()
    db.refresh(db_company)
    return db_company

@app.post("/companytype", status_code=201 ,tags=["company"])
def add_company_type(companyType: CompanyTypeSchema, db: Session = Depends(get_db)) -> CompanyTypeOutSchema:
    db_company_type= CompanyType(**companyType.model_dump())
    db.add(db_company_type)
    db.commit()
    db.refresh(db_company_type)
    return db_company_type


@app.post("/images/upload", tags=["images"])
async def upload_image(file: UploadFile):
    accepted_img_extensions = ['jpg', 'jpeg', 'bmp', 'webp']
    data = file.file
    filename = file.filename
    filename_splitted = filename.split(".")
    file_extension  = filename_splitted[-1]
    new_img_name = uuid4()
    if file_extension not in accepted_img_extensions:
        raise HTTPException(status_code=404, detail="Image extension is not supported")
    file.filename = f"{new_img_name}.{file_extension}"
    contents = await file.read()
    with open(f"{IMAGEDIR}{file.filename}", "wb") as f:
        f.write(contents)
    return  {"uploaded image: ": file.filename}

@app.get("/images/{image_name}", tags=["images"])
def get_image(image_name: str):
    images = os.listdir(IMAGEDIR)
    return FileResponse(f"{IMAGEDIR}{image_name}")
