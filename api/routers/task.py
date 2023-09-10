from fastapi import APIRouter
import api.schemas.task as task_schema

router = APIRouter()

# タスクの一覧を表示
@router.get("/tasks", response_model=list[task_schema.Task])
async def list_tasks():
  return [task_schema.Task(id=1, title="1つ目のToDoタスク")]

# タスクを作成
@router.post("/tasks")
async def create_task():
  pass

# タスクの更新 
@router.put("/tasks/{task_id}")
async def update_task():
  pass

# タスクの削除
@router.delete("/tasks/{task_id}")
async def delete_task():
  pass