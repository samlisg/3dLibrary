from sqlalchemy.orm import Session
from . import models, schemas

def get_projects(db: Session):
    return db.query(models.Project).all()

def create_project(db: Session, project: schemas.ProjectCreate):
    db_project = models.Project(**project.dict())
    db.add(db_project)
    db.commit()
    db.refresh(db_project)
    return db_project

def create_file(db: Session, file: schemas.FileCreate, project_id: int):
    db_file = models.File(**file.dict(), project_id=project_id)
    db.add(db_file)
    db.commit()
    db.refresh(db_file)
    return db_file
