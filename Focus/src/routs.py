import uvicorn
from fastapi import FastAPI, HTTPException
from schemes.task_schemes import TaskRegular, TaskSport, TaskWork
from models.task_model import TaskModel
from models.task_model import Base
from data.database_task import SessionDep_task
from data.database_task import task_engine

app = FastAPI(title='Focus')

@app.post('/setup_database/', tags=['База данных'], summary='Устанавливаем соединение с БД', response_model=None)
async def setup_database():
    async with task_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

        try:
            return {'✅ База успешно настроена!'}
        except Exception as e:
            return {f'🤔 Хмм, ошибка подключения к базе! <<{e}>>'}
        
@app.post('/add_regular_task/', tags=['🌙 Обычные задачи'], summary='Добавляем новую задачу', response_model=None)
async def add_regular_task(task_reg: TaskRegular, data_reg: TaskModel, session: SessionDep_task):
    task_data = session(
        task=task_reg.task,
        status=task_reg.status,
    )

    session.add(task_data)
    await session.commit()

@app.post('add_work_task/', tags=['💻 Рабочии задачи'], summary='Добавляем новую задачу', response_model=None)
async def add_work_task(task_work: TaskWork):
    pass

@app.post('/add_sport_task/', tags=['🏆 Спортивные задачи'], summary='Добавляем новую задачу', response_model=None)
async def add_sport_task(task_sport: TaskSport):
    pass

if  __name__ == '__main__':
    uvicorn.run('routs:app', reload=True)