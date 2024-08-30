import threading
import time

def print_even_numbers():
    for num in range(2, 201, 2):
        print(f"Even: {num}")
        time.sleep(0.5)

def print_odd_numbers():
    for num in range(1, 201, 2):
        print(f"Odd: {num}")
        time.sleep(0.5)

even_thread = threading.Thread(target=print_even_numbers)
odd_thread = threading.Thread(target=print_odd_numbers)

even_thread.start()
odd_thread.start()

even_thread.join()
odd_thread.join()
