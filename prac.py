#multithraeding and multiprocessing
# In Python, multithreading is useful in situations where your program is I/O-bound, meaning it spends time waiting for input/output operations such as:
# ✅ Use multithreading when:
# Tasks involve a lot of waiting (e.g., downloading files, calling APIs)
# You want to improve responsiveness (e.g., in a GUI app)
# You are performing concurrent I/O operations


# import threading
# import time

# def print_numbers():
#     for i in range(5):
#         time.sleep(2)
#         print(f"Number: {i}")

# def print_letters():
#     for letter in 'abcde':
#         time.sleep(2)
#         print(f"Letter: {letter}")
# #create 2 threads
# t1 = threading.Thread(target=print_numbers)
# t2 = threading.Thread(target=print_letters)

# t = time.time()
# t1.start() 
# t2.start()

# t1.join() # wait for thread 1 to finish
# t2.join() # wait for thread 2 to finish
# print(f"Finished time = {time.time() - t}")



#multiprocessing:  Multiprocessing is used when you want to run CPU-bound tasks in parallel by utilizing multiple cores of your CPU. Unlike multithreading, it bypasses the Global Interpreter Lock (GIL), making it ideal for tasks like:
# Heavy computations
# Image processing
# Data analysis
# Machine learning training

# import multiprocessing
# import time


# def square_numbers():
#     for n in range(5):
#         time.sleep(1)
#         print(f"Square: {n * n}")
# def cube_numbers():
#     for n in range(5):
#         time.sleep(1.5)
#         print(f"Cube: {n * n * n}")

# if __name__ == "__main__":
#     # This is necessary to avoid recursive process creation on Windows
#     # and to ensure that the code runs only when the script is executed directly.
#     # On Unix-like systems, this check is not strictly necessary but is still a good practice.
#     # It prevents the child processes from executing the same code again.
#     multiprocessing.freeze_support()    
#     p1= multiprocessing.Process(target=square_numbers)
#     p2= multiprocessing.Process(target=cube_numbers)
#     t = time.time()
#     p1.start()
#     p2.start()
#     p1.join()
#     p2.join()

#     print(f"Finished time = {time.time() - t}")




# #multithreading with threadpool executor
# from concurrent.futures import ThreadPoolExecutor
# import time

# def print_number(n):
#     time.sleep(1)
#     return f"Number: {n}"

# numbers = [1,2,3,4,5,6,7,8,9,10]

# with ThreadPoolExecutor(max_workers=3) as executor:
#     results = executor.map(print_number, numbers)

# for result in results:
#     print(result)  # <-- this is printing None



#multiprocessing with processpool executor

# from concurrent.futures import ProcessPoolExecutor
# import time

# def square(n):
#     time.sleep(1)
#     return n * n
# numbers = [1,2,3,4,5,6,7,8,9,10]
# if __name__ == "__main__":
#    with ProcessPoolExecutor(max_workers=3) as executor:
#     results = executor.map(square, numbers)

#    for result in results:
#     print(result)  # <-- this is printing None




# # #multithreading with requests
# import sys
# import io
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# import threading
# import requests
# from bs4 import BeautifulSoup

# urls = [
#     'https://python.langchain.com/docs/tutorials/',
#     'https://python.langchain.com/docs/concepts/',
#     'https://python.langchain.com/docs/how_to/pydantic_compatibility/'
# # ]

# def fetch_content(url):
#     response = requests.get(url)
#     if response.status_code == 200:
#         soup = BeautifulSoup(response.content, 'html.parser')
#         title = soup.title.string if soup.title else 'No title found'
#         print(f"\nTitle: {title}")
#         print(f"Fetched {len(soup.text)} characters from {url}")
#     else:
#         print(f"Failed to fetch {url}")

# threads = []

# # Start all threads
# for url in urls:
#     thread = threading.Thread(target=fetch_content, args=(url,))
#     threads.append(thread)
#     thread.start()

# # Wait for all threads to complete
# for thread in threads:
#     thread.join()

# print("All threads have finished.")



# import multiprocessing
# import time
# import sys
# import math

# sys.set_int_max_str_digits(10000000)

# def compute_factorial(onumber):
    # time.sleep(1)  # Simulate long computation
#     result = math.factorial(onumber)
#     print(f"Factorial of {onumber} is {result}")
#     return result

# if __name__ == "__main__":
#     numbers = [10000, 2000, 300, 400, 5000]
#     start_time = time.time()
    
#     with multiprocessing.Pool(processes=3) as pool:
#         results = pool.map(compute_factorial, numbers)

#     print("All computations are done.")
#     end_time = time.time()
    
#     print(f"Results: {results}")
#     print(f"Total time taken: {end_time - start_time} seconds")



#MEMORY MANAGEMENT
# In Python, memory management is handled by the Python Memory Manager

#Reference counting in Python is a memory management technique used by the Python memory manager to keep track of the number of references pointing to an object. When an object’s reference count drops to zero, Python automatically deallocates the memory used by that object.

# import sys

# a = []
# print(sys.getrefcount(a))  # Usually 2: one for 'a', one for getrefcount argument

# b = a
# print(sys.getrefcount(a))  # Now 3

# del b
# print(sys.getrefcount(a))  # Back to 2



#Garbage collection : in Python is a mechanism for automatically reclaiming memory by removing objects that are no longer in use. Python uses a combination of reference counting and a cyclic garbage collector to manage memory.

# import gc
# gc.enable()  # Enable automatic garbage collection
# gc.disable()  # Disable automatic garbage collection
# unreachable = gc.collect()
# print("Unreachable objects:", unreachable)
# print("Garbage:", gc.garbage)  # List of objects found but not freed (with print
# print(gc.get_stats())  # Get statistics about the collector
# print(gc.get_count())  # Get the current count of unreachable objects




# #memory management best practices
# 1. **Avoid unnecessary references** – Don’t keep unused variables around.
# 2. **Use `del` for large objects** – Manually delete big objects when no longer needed.
# 3. **Use generators over lists** – Saves memory by yielding data lazily.
# 4. **Avoid circular references** – Be cautious with objects referencing each other.
# 5. **Use weak references** – Use `weakref` for cache or observer patterns.
# 6. **Use `gc.collect()` wisely** – Trigger garbage collection manually if needed.
# 7. **Profile memory usage** – Use `tracemalloc` or `memory_profiler` to monitor memory.
# 8. **Close file/network resources** – Always use `with` blocks or explicitly close.
# 9. **Use slots for small classes** – Use `__slots__` to reduce memory overhead.
# 10. **Batch data processing** – Break large data into chunks for processing.


# import gc

# class MyObject:
#     def __init__(self, name):
#         self.name = name
#         print(f"Object {self.name} created")

#     def __del__(self):
#         print(f"Object {self.name} deleted")

# # Create circular reference
# obj1 = MyObject("A")
# obj2 = MyObject("B")

# obj1.ref = obj2
# obj2.ref = obj1


# # Delete external references
# del obj1
# del obj2


# # Collect garbage
# print(gc.collect())
# print("Garbage collection completed")


#generator for mem eff

# def generate_numbers(n):
#     for i in range(n):
#         yield i * i
# for num in generate_numbers(10000):
#     print(num)
#     if num>10:
#       break  # This will print squares of numbers from 0 to 9





# #profiling mem usage with tracemalloc4
# import tracemalloc

# def create_large_list():
#     return [i for i in range(1000000)]

# def main():
#     tracemalloc.start()
    
#     # Snapshot before allocation
#     snapshot1 = tracemalloc.take_snapshot()

#     # Create memory-heavy object
#     big_list = create_large_list()

#     # Snapshot after allocation
#     snapshot2 = tracemalloc.take_snapshot()
    
#     # Compare the difference
#     top_stats = snapshot2.compare_to(snapshot1, 'lineno')
    
#     print("[ Top 15 Memory Usage Differences ]")
#     for stat in top_stats[:15]:
#         print(stat)
    
#     tracemalloc.stop()

# main()
