# import platform
# print(platform.python_implementation())

import threading
import multiprocessing
import time

# A CPU-bound function that performs a large number of calculations
def cpu_bound_task(n):
    total = 0
    for i in range(n):
        total += (i ** 2) ** 0.5  # Some arbitrary computation
    return total

# Function to run the task using threading
def run_with_threads(n, num_threads):
    threads = []
    for _ in range(num_threads):
        thread = threading.Thread(target=cpu_bound_task, args=(n,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

# Function to run the task using multiprocessing
def run_with_multiprocessing(n, num_processes):
    processes = []
    for _ in range(num_processes):
        process = multiprocessing.Process(target=cpu_bound_task, args=(n,))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

if __name__ == "__main__":
    n = 15**6  # Number of calculations
    num_threads = 4
    num_processes = 4

    # Measure time for threading
    start_time = time.time()
    run_with_threads(n, num_threads)
    threading_time = time.time() - start_time
    print(f"Time taken with threading: {threading_time:.2f} seconds")

    # Measure time for multiprocessing
    start_time = time.time()
    run_with_multiprocessing(n, num_processes)
    multiprocessing_time = time.time() - start_time
    print(f"Time taken with multiprocessing: {multiprocessing_time:.2f} seconds")

    # If output is verbose, restart session. On top menu bar click on Runtime --> click on Restart Session