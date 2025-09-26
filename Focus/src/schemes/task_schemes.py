import datetime
from pydantic import BaseModel

#начало схем для обыч.задач
class TaskRegular(BaseModel):
    task: str 
    status: int 

class ReturnTaskRegular(TaskRegular):
    id: int
#конец схем для обыч.задач

#начало схем для раб.задач
class TaskWork(BaseModel):
    task: str
    status: int 

class ReturnTaskWork(TaskWork):
    id: int
#конец схем для раб.задач

#начало схем для спорт.задач
class TaskSport(BaseModel):
    task: str 
    status: int 

class ReturnTaskSport(TaskSport):
    id: int
#конец схем для спорт.задач