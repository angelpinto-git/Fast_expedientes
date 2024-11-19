from datetime import datetime

from pydantic import BaseModel


class NewRecordRequest(BaseModel) :
    title: str
    status: str = 'new'
    description: str = ''

class RecordRequest(BaseModel) :
    title: str | None = None
    status: str | None = None 
    description: str | None = None

class RecordResponse(BaseModel) :
    id: int
    title: str
    status: str = 'new'
    description: str = ''
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()
    