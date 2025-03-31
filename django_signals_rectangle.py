"""
Assignment: Django Signals & Custom Classes in Python

This file contains answers to the Django Signals and Custom Classes questions,
including theoretical explanations, code snippets, and expected outputs.
"""

import time
import threading
from django.db import transaction
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

# ------------------------------
# Question 1: Are Django signals executed synchronously or asynchronously?
# Answer: By default, Django signals are executed synchronously.
# The following code proves this by adding a delay in the signal.
#
# Expected Output:
# Signal started
# (Waits 5 seconds)
# Signal finished
# User creation finished
# ------------------------------

@receiver(post_save, sender=User)
def my_signal_handler(sender, instance, **kwargs):
    print("Signal started")
    time.sleep(5)  # Simulating a delay
    print("Signal finished")

# Triggering the signal
User.objects.create(username="testuser")
print("User creation finished")

# ------------------------------
# Question 2: Do Django signals run in the same thread as the caller?
# Answer: Yes, Django signals execute in the same thread as the caller.
#
# Expected Output:
# Main thread: MainThread
# Signal running in thread: MainThread
# ------------------------------

print(f"Main thread: {threading.current_thread().name}")

@receiver(post_save, sender=User)
def thread_check_signal(sender, instance, **kwargs):
    print(f"Signal running in thread: {threading.current_thread().name}")

User.objects.create(username="testuser2")

# ------------------------------
# Question 3: Do Django signals run in the same database transaction as the caller?
# Answer: Yes, Django signals run inside the same transaction unless explicitly delayed.
#
# Expected Output:
# Signal is running inside the same transaction
# ------------------------------

@receiver(post_save, sender=User)
def transaction_signal(sender, instance, **kwargs):
    if transaction.get_connection().in_atomic_block:
        print("Signal is running inside the same transaction")
    else:
        print("Signal is running outside the transaction")

with transaction.atomic():
    User.objects.create(username="testuser3")

# ------------------------------
# Custom Classes in Python: Implementing an Iterable Rectangle Class
#
# Task: Create a Rectangle class that allows iteration.
# When iterated over, it should return:
# {'length': <value>} first, then {'width': <value>}.
#
# Expected Output:
# {'length': 10}
# {'width': 5}
# ------------------------------

class Rectangle:
    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width
        self._values = iter([{"length": self.length}, {"width": self.width}])

    def __iter__(self):
        return self

    def __next__(self):
        return next(self._values)

# Example Usage
rect = Rectangle(10, 5)
for value in rect:
    print(value)
