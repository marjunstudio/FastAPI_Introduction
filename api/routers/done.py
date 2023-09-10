from fastapi import APIRouter

router = APIRouter()

# タスクに「完了フラグ」を立てる
@router.put("/tasks/{task_id}/done")
async def mark_task_as_done():
  pass

# タスクの「完了フラグ」を削除
@router.delete("/tasks/{task_id}_done")
async def unmark_task_as_done():
  pass