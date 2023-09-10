from fastapi import APIRouter

router = APIRouter()

# タスクの一覧を表示
@router.get("/tasks")
async def list_tasks():
  pass

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