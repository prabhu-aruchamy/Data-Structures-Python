class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def show(self):
        print('Queue contents are:')
        for i in range(self.size):
            print(self.queue[int((i + self.front) % self.max_size)])

q = Queue()
q.enqueue('5')
q.enqueue('5')
q.enqueue('5')
q.enqueue('5')
q.dequeue()
q.show()