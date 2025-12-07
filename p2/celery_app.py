# celery_app.py
from celery import Celery
import time

app = Celery(
    "tts_demo",
    broker="redis://localhost:6379/0",
    backend="redis://localhost:6379/1",
)

@app.task
def fake_tts(task_id, enqueued_at):
    """
    شبیه‌سازی یه کار TTS که 0.5 ثانیه طول می‌کشه
    """
    start = time.time()
    queue_wait = start - enqueued_at

    # اینجا فرض کن مدل TTS روی GPU داره ران می‌شه
    time.sleep(0.5)

    end = time.time()

    print(
        f"[task {task_id}] queue_wait={queue_wait:.2f}s "
        f"proc_time={end - start:.2f}s total={end - enqueued_at:.2f}s"
    )
    return {
        "task_id": task_id,
        "queue_wait": queue_wait,
        "proc_time": end - start,
        "total": end - enqueued_at,
    }
