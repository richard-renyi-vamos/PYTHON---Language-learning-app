import tkinter as tk
import sqlite3

# Function to fetch German lessons from a database
def fetch_lessons():
    # Connect to SQLite database
    connection = sqlite3.connect('german_lessons.db')
    cursor = connection.cursor()

    # Fetch lessons
    cursor.execute("SELECT * FROM lessons")
    lessons = cursor.fetchall()

    # Close connection
    connection.close()

    return lessons

# Function to display lessons in the GUI
def display_lessons():
    lessons = fetch_lessons()
    for lesson in lessons:
        # Display lessons in the GUI
        lesson_label = tk.Label(root, text=lesson[1])  # Assuming lesson[1] holds lesson names
        lesson_label.pack()

# Create the main window
root = tk.Tk()
root.title("German Learning App")

# Fetch and display lessons
display_lessons()

# Run the app
root.mainloop()
