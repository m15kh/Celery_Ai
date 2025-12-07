# produce_tasks.py
from celery_app import fake_tts
import time

if __name__ == "__main__":
    for i in range(200):
        enqueued_at = time.time()
        fake_tts.apply_async(args=[i, enqueued_at])
        # اینجا عمداً خیلی سریع می‌فرستیم که صف پر بشه
        # اگر خواستی "آروم‌تر" تست کنی، این خط رو باز کن:
        # time.sleep(0.01)

    print("200 tasks sent.")
