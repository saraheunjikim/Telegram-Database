import time
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler

path_folder = "C:/Users/Muffin/Desktop/python/projects/Telegram-Database/"
path_folder_jobs = "C:/Users/Muffin/Desktop/python/projects/Telegram-Database/files/jobs"
path_folder_corona = "C:/Users/Muffin/Desktop/python/projects/Telegram-Database/files/corona"
path_folder_etc = "C:/Users/Muffin/Desktop/python/projects/Telegram-Database/files/etc"

def on_created(event):
    print(f"{event.src_path} has been created.")


def on_moved(event):
    print(f"Moved {event.src_path} to {event.dest_path}")


def trigger_files(path):
    my_event_handler = PatternMatchingEventHandler("*", "", False, True)

    my_event_handler.on_created = on_created
    my_event_handler.on_moved = on_moved

    my_observer = Observer()
    my_observer.schedule(my_event_handler, path, recursive=True)

    my_observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        my_observer.stop()
        my_observer.join()

if __name__ == '__main__':
    trigger_files(path_folder)
    trigger_files(path_folder_jobs)
    trigger_files(path_folder_corona)
    trigger_files(path_folder_etc)
