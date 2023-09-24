from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

import api.schemas.done as done_schema
import api.cruds.done as done_crud
from api.db import get_db

router = APIRouter()


# タスクに「完了フラグ」を立てる
@router.put("/tasks/{task_id}/done", response_model=done_schema.DoneResponse)
async def mark_task_as_done(task_id: int, db: Session = Depends(get_db)):
  done = done_crud.get_done(db, task_id=task_id)
  if done is not None:
    raise HTTPException(status_code=400, detail="Done already exists")
  
  return done_crud.create_done(db, task_id)

# タスクの「完了フラグ」を削除
@router.delete("/tasks/{task_id}_done", response_model=None)
async def unmark_task_as_done(task_id: int, db: Session = Depends(get_db)):
  done = done_crud.get_done(db, task_id=task_id)
  if done in None:
    raise HTTPException(status_code=404, detail="Done not found")
  
  return done_crud.delete_done(db, original=done)