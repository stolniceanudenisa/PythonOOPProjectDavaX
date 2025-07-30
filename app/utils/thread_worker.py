from threading import Thread
from queue import Queue

task_queue = Queue()

def worker():
    while True:
        func, args = task_queue.get()
        try: func(args)
        except Exception as e: print(f"[THREAD ERROR] {e}")
        finally: task_queue.task_done()

Thread(target=worker, daemon=True).start()

def submit_task(func, *args):
    task_queue.put((func, *args))
