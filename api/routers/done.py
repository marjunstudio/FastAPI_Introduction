from fastapi import APIRouter

router = APIRouter()

# タスクに「完了フラグ」を立てる
@router.put("/tasks/{task_id}/done", response_model=None)
async def mark_task_as_done(task_id: int):
  return

# タスクの「完了フラグ」を削除
@router.delete("/tasks/{task_id}_done", response_model=None)
async def unmark_task_as_done(task_id: int):
  return