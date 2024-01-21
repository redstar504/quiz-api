import time
import datetime

def run_background_task():
    while True:
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"Background task is running at {current_time}")
        time.sleep(10)

if __name__ == '__main__':
    run_background_task()