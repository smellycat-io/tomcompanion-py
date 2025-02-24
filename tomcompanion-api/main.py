import json
import os

# Initialize Memory
MEMORY_FILE = "memory.json"

def load_memory():
    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "r") as file:
            return json.load(file)
    return{"name": "Tom", "age":0, "tasks_completed":0}

def save_memory(memory):
    with open(MEMORY_FILE, "w") as file:
        json.dump(memory, file, indent=4)

def interact(memory):
    print(f"Hi! I'm {memory['name']}! I'm {memory['age']} sessions old.")
    greetings_list = [
            'say hello',
            'hello',
            'hi',
            'greetings',
            'hola',
            'sup',
            'sup?',
        ]
    while True:
        user_input = input("What would you like me to do? (say hello, learn, exit):").strip().lower()
        if user_input == "exit":
            print("Goodbye!")
            break
        elif user_input in greetings_list:
            print(f"{memory['name']}: Hello! 😊")
        elif user_input == "learn":
            memory["tasks_completed"] += 1
            print(f"{memory['name']} learned something new! Total tasks: {memory['tasks_completed']}")
        else:
            print("I don't know how to do that yet.")

        # Update age (or any other properties)
        memory["age"] += 1
        save_memory(memory)

if __name__ == "__main__":
    memory = load_memory()
    interact(memory)
