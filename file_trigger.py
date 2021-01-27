import time
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler


def on_created(event):
    print(f"hey, {event.src_path} has been created!")


def on_moved(event):
    print(f"ok ok ok, someone moved {event.src_path} to {event.dest_path}")


def trigger_files():
    my_event_handler = PatternMatchingEventHandler("*", "", False, True)

    my_event_handler.on_created = on_created
    my_event_handler.on_moved = on_moved

    path = "C:/Users/Muffin/Desktop/python/projects/Telegram-Database/"
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
    trigger_files()