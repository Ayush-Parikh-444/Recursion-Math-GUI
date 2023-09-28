import tkinter as tk

# Calculate the factorial of a number using recursion
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Generate Fibonacci numbers using recursion
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Display the result for the calculated factorial
def calculate_factorial():
    num = int(factorial_entry.get())
    if num < 0:
        result_label.config(text="Factorial is not defined for negative numbers.")
    else:
        result = factorial(num)
        result_label.config(text=f"{num}! = {result}")

# Display the generated Fibonacci sequence
def generate_fibonacci():
    num = int(fibonacci_entry.get())
    if num < 0:
        result_label.config(text="Please enter a non-negative integer.")
    else:
        fibonacci_sequence = [str(fibonacci(i)) for i in range(num)]
        result_label.config(text="Fibonacci Sequence:\n" + ", ".join(fibonacci_sequence))

# Create the main window
window = tk.Tk()
window.title("Recursive Functions GUI")

# Factorial section
factorial_label = tk.Label(window, text="Calculate Factorial")
factorial_label.pack()

factorial_entry = tk.Entry(window)
factorial_entry.pack()

factorial_button = tk.Button(window, text="Calculate", command=calculate_factorial)
factorial_button.pack()

# Fibonacci section
fibonacci_label = tk.Label(window, text="Generate Fibonacci Numbers")
fibonacci_label.pack()

fibonacci_entry = tk.Entry(window)
fibonacci_entry.pack()

fibonacci_button = tk.Button(window, text="Generate", command=generate_fibonacci)
fibonacci_button.pack()

# Result label
result_label = tk.Label(window, text="")
result_label.pack()

# Start the GUI event loop
window.mainloop()
