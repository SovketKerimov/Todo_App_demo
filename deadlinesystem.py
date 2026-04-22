import time
import threading

def convert_to_sec():
    try:
        hours = float(input("Enter deadline for your task (in hours): "))
        if hours <= 0:
            print("Invalid input")
            return None

        return time.time() + (hours * 3600)
    except ValueError:
        print("Invalid input. Please enter a number.")
        return None

def timer(task_name, seconds_to_wait):

        time.sleep(seconds_to_wait)
        print(f"\n--- ALARM: {task_name} is due now! ---")


def show_time(deadline_timestamp):
        remaining = deadline_timestamp - time.time()
        if remaining <= 0:
            return "Expired"

        days, remainder = divmod(int(remaining), 86400)
        hours, remainder = divmod(remainder, 3600)
        mins, secs = divmod(remainder, 60)
        return f"{days}d {hours:02d}:{mins:02d}:{secs:02d}"

def background_timer(task_name, seconds):

    time.sleep(seconds)
    print(f"\n--- TIME UP: {task_name} ---")
    print("Command (1-5): ", end="")

def start_timer_thread(task_name):
    seconds = convert_to_sec()
    if seconds:
        t = threading.Thread(target=background_timer, args=(task_name, seconds), daemon=True)
        t.start()
        print(f"Timer started for {seconds//3600} hours.")