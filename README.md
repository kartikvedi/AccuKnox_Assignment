# AccuKnox_Assignment
Django Signals & Custom Classes in Python

Overview

This repository contains answers to Django Signals and Python Custom Classes questions. It includes theoretical explanations, code snippets, and expected outputs.

Questions

Django Signals

1. Are Django signals executed synchronously or asynchronously?

By default, Django signals are executed synchronously.

The provided code demonstrates this by adding a delay in the signal execution.

Expected Output:

Signal started
(Waits 5 seconds)
Signal finished
User creation finished

2. Do Django signals run in the same thread as the caller?

Yes, Django signals execute in the same thread as the caller.

The provided code prints the thread name for both the main program and the signal.

Expected Output:

Main thread: MainThread
Signal running in thread: MainThread

3. Do Django signals run in the same database transaction as the caller?

Yes, Django signals run inside the same transaction unless explicitly delayed.

The provided code checks if the signal is executed within an atomic block.

Expected Output:

Signal is running inside the same transaction

Custom Classes in Python

Task: Implement an Iterable Rectangle Class

Create a Rectangle class that allows iteration.

When iterated over, it should return:

{'length': <value>}
{'width': <value>}

Expected Output:

{'length': 10}
{'width': 5}

How to Run This Project

Prerequisites

Python 3.x

Django installed (pip install django)

Steps to Run

Clone this repository:

git clone https://github.com/yourusername/django-signals-rectangle.git
cd django-signals-rectangle

Ensure Django is installed:

pip install django

Run the Python script:

python django_signals_rectangle.py

This will execute all the questions and print the expected outputs.

License

This project is open-source and available under the MIT License.

