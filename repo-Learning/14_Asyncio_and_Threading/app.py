import asyncio
import time
import threading

# # Synchronous approach
# def make_coffee_sync():
#     print(f"\tMaking coffee... : Thread Name: {threading.current_thread().name}")
#     time.sleep(2)  # Simulate coffee preparation time
#     print("\tCoffee is ready!")

# def make_pastry_sync():
#     print(f"\tMaking pastry... : Thread Name: {threading.current_thread().name}")
#     time.sleep(3)  # Simulate pastry preparation time
#     print("\tPastry is ready!")

# def order_sync():
#     make_coffee_sync()
#     make_pastry_sync()
    
# # Run the synchronous example
# print("Synchronous approach:")
# start_time = time.time()

# print("Main thread entring order_sync()")
# order_sync()
# print("Main thread exiting order_sync()")

# print(f"Total time: {time.time() - start_time} seconds")


# # Asynchronous approach using Asyncio
# async def make_coffee_async():
#     print(f"\tMaking coffee... : Thread Name: {threading.current_thread().name}")
#     await asyncio.sleep(2)  # Simulate coffee preparation time
#     print("\tCoffee is ready!")

# async def make_pastry_async():
#     print(f"\tMaking pastry... : Thread Name: {threading.current_thread().name}")
#     await asyncio.sleep(3)  # Simulate pastry preparation time
#     print("\tPastry is ready!")

# async def order_async():
#     tasks = [
#         asyncio.create_task(make_coffee_async()),
#         asyncio.create_task(make_pastry_async())
#     ]
#     await asyncio.gather(*tasks)

# print("\nAsynchronous approach:")

# async def main():
#     start_time = time.time()
#     print("Main thread entring order_async()")
#     await asyncio.create_task(order_async()) # Workaround for Colab, # Option 2: schedule as a background task
#     print("Main thread exiting order_async()")
#     print(f"Total time: {time.time() - start_time} seconds")

# asyncio.run(main())


# Asyncio aur Await Samjhna
# Asyncio:
# Definition: Asyncio ek Python library hai jo aik thread par multiple concurrent (ek sath chalne wale) tasks likhnay mein madad deti hai. Yeh khas tor par I/O-bound tasks, jaise network requests ya database queries, handle karne ke liye behtareen hai.

# Mukhya Components (Ahem Hissay):
# Event Loop: Yeh event loop tasks ko schedule aur manage karta hai.
# Coroutines: Aisi functions jo async def se likhi jati hain aur execution ko suspend ya resume kar sakti hain.
# Tasks: Yeh coroutines ko concurrently run karne ke liye istemal hoti hain.
# Futures: Aise objects jo aik result represent karte hain jo abhi complete nahi hua (isko baad mein detail mein discuss karenge).
# Await:
# Definition: await aik keyword hai jo kisi async function ke andar likha jata hai taake us coroutine ka execution temporarily suspend ho jaye jab tak awaited task complete na ho jaye. Isse event loop ko doosray tasks handle karne ka moka milta hai.

# Usage: await ka istemal coroutines, tasks, ya futures ka intezar karne ke liye hota hai. Yeh non-blocking operations ko enable karta hai.

# Asyncio aur Await ka Farq:
# Asyncio: Yeh aik library hai jo asynchronous operations ka framework provide karti hai, jisme event loop aur tasks create aur manage karne ke tools shamil hain.
# Await: Yeh aik keyword hai jo async functions ke andar likha jata hai taake execution event loop ko wapas de diya jaye, taake doosray tasks parallel run ho sakein.
# Dono Ko Sath Istemaal Karna:
# Aik async function define karein async def ke saath.
# Function ke andar await likhein taake kisi coroutine ka intezar kiya ja sake.
# Top-level async function ko run karne ke liye asyncio.run() ka istemal karein.

# import asyncio

# async def task1():
#        await asyncio.sleep(4)
#        print("Task 1 done")

# async def task2():
#        await asyncio.sleep(1)
#        print("Task 2 done")

# async def main():
#        t1 = asyncio.create_task(task1())
#        t2 = asyncio.create_task(task2())
#        await asyncio.gather(t1, t2)

# asyncio.run(main())

# async def my_coroutine():
#     await asyncio.sleep(1)
#     return "Coroutine completed"

# async def main():
#     # Create a Task (which returns a Future)
#     future = asyncio.create_task(my_coroutine())

#     print("Going to Maldives on a 2 day vacation")
#     await asyncio.sleep(5)
#     print("Come back from vacation")


#     # Await the Future
#     result = await future
#     print(result)

# asyncio.run(main()).

# Function to be run in a thread
# def print_numbers():
#     for i in range(5):
#         print(f"Number: {i} : Thread Name: {threading.current_thread().name}")
#         time.sleep(3) # change the sleep value, play and learn

# # Create a thread
# my_thread = threading.Thread(target=print_numbers, name='Worker Thread')

# # Start the thread
# my_thread.start()

# # Main thread continues executing
# print(f"After spawning other threads Main thread is continue doing its works! : Thread Name: {threading.current_thread().name}")

# time.sleep(0) # change the sleep value, play and learn

# print(f"Main thread is waiting for other threads to join: my_thread.join() : Thread Name: {threading.current_thread().name}")
# # Wait for the thread to finish
# my_thread.join()

# print(f"Main thread starts executing becuase all other threads join main thread : Thread Name: {threading.current_thread().name}")

# print(f"Main Thread finished! : Thread Name: {threading.current_thread().name}")

# class MyThread(threading.Thread):
#     def run(self):
#         for i in range(5):
#             print(f"Thread {threading.current_thread().name}: {i}")
#             time.sleep(1)

# # Create and start the thread
# my_thread = MyThread(name="MyCustomThread")


# # Wait for the thread to finish
# my_thread.start()

# # Wait for the thread to finish
# my_thread.join()
# print("Thread execution completed.")

# def print_numbers():
#     for i in range(10):
#         time.sleep(2)  # simulate some work
#         print(f"Thread {threading.current_thread().name}: Number: {i}")

# def print_letters():
#     for letter in "ABCDEFGHIJ":
#         time.sleep(1)  # simulate some work
#         print(f"Thread {threading.current_thread().name}: Letter: {letter}")

# # Create two threads
# thread1 = threading.Thread(target=print_numbers)
# thread2 = threading.Thread(target=print_letters)

# # Start the threads
# thread1.start()
# thread2.start()

# # Wait for the threads to finish
# thread1.join()
# thread2.join()

# print("Both threads have finished.")

# def background_task():
#     while True:
#         print("Background task is running...")
#         time.sleep(1)
        
# demon_thread = threading.Thread(target=background_task,daemon=True)
# demon_thread.start()

# time.sleep(5)
# print("Main thread exiting...")

# conter1 = 0
# conter2 = 0
# counter_lock = threading.Lock()

# def incrementer():
#     global conter1, conter2
#     for _ in range(100000):
#         with counter_lock:
#             conter1 += _
#             conter2 += _

# # Create two threads
# thread1 = threading.Thread(target=incrementer)
# thread2 = threading.Thread(target=incrementer)

# # Start threads
# thread1.start()
# thread2.start()

# # Wait for threads to finish
# thread1.join()
# thread2.join()

# print(f"Final Counter Value: counter_1={conter1} , counter_2={conter2}")


import queue
# import random
# # Function for the producer thread
# def producer(q, num_items):
#     for i in range(num_items):
#         item = random.randint(1, 100)  # Produce a random number
#         q.put(item)  # Put the item in the queue
#         print(f"Produced: {item}")
#         time.sleep(random.uniform(0.1, 0.5))  # Simulate variable production time
#     q.put(None)  # Signal the consumer to stop

# # Function for the consumer thread
# def consumer(q):
#     while True:
#         item = q.get()  # Get an item from the queue
#         if item is None:  # Check for the stop signal
#             break
#         print(f"Consumed: {item}")
#         time.sleep(random.uniform(0.1, 0.5))  # Simulate variable processing time
#     print("Consumer finished processing.")

# if __name__ == "__main__":
#     num_items = 10  # Number of items to produce
#     q = queue.Queue()  # Create a queue

#     # Create producer and consumer threads
#     producer_thread = threading.Thread(target=producer, args=(q, num_items))
#     consumer_thread = threading.Thread(target=consumer, args=(q,))

#     # Start the threads
#     producer_thread.start()
#     consumer_thread.start()

#     # Wait for the threads to finish
#     producer_thread.join()
#     consumer_thread.join()

#     print("All threads have finished.")
    
    
import concurrent.futures
import time
import random

# A function that simulates a time-consuming task
def task(n):
    sleep_time = random.uniform(0.5, 2.0)  # Random sleep time between 0.5 and 2 seconds
    print(f"Task {n} will sleep for {sleep_time:.2f} seconds.")
    time.sleep(sleep_time)
    return f"Task {n} completed."

if __name__ == "__main__":
    num_tasks = 10  # Number of tasks to execute
    results = []

    # Using ThreadPoolExecutor to manage threads
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        # Submit tasks to the executor
        future_to_task = {executor.submit(task, i): i for i in range(num_tasks)}

        # Process the results as they complete
        for future in concurrent.futures.as_completed(future_to_task):
            task_number = future_to_task[future]
            try:
                result = future.result()  # Get the result of the task
                results.append(result)
                print(result)
            except Exception as exc:
                print(f"Task {task_number} generated an exception: {exc}")

    print("All tasks have been completed.")