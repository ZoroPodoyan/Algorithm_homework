"Implement a Custom Queue using either an array, a list, or any other structure you prefer."

class MyQueue:
    def __init__(self):
        self.queue = []

    # adds an elements at the end of the queue
    def enqueue(self, item):
        self.queue.append(item)
        print(f"{item} added in the queue.")

    # deletes the element from the front of the queue
    def dequeue(self):
        if len(self.queue) == 0:
            print("ERROR! The queue is empty")
            return None
        return self.queue.pop(0)

    # Check if the queue is empty
    def is_empty(self):
        return len(self.queue) == 0

    # Display the queue
    def display(self):
        if len(self.queue) == 0:
            print("ERROR! The queue is empty")
        else:
            print(f"Queue: {self.queue}")

queue = MyQueue()

queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

queue.display()

print(f"{queue.dequeue()} removed from the queue")
queue.display()

if queue.is_empty():
    print("The queue is empty!")
else:
    print("There are elements in the queue")

queue.dequeue()
queue.display()
queue.enqueue(6)
queue.display()

