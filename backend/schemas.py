from pydantic import BaseModel
from typing import Optional, List

class FileBase(BaseModel):
    filename: str
    file_type: str

class FileCreate(FileBase):
    pass

class File(FileBase):
    id: int
    class Config:
        orm_mode = True

class ProjectBase(BaseModel):
    name: str
    description: Optional[str]
    source: Optional[str]
    version: Optional[str]
    parent_id: Optional[int]

class ProjectCreate(ProjectBase):
    pass

class Project(ProjectBase):
    id: int
    files: List[File] = []
    class Config:
        orm_mode = True
