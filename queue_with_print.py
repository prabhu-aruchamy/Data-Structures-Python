class queue:
    def __init__(self, max_size, size=0, front=0, rear=0):
        self.queue = [[] for i in range(5)] #creates a list [0,0,0,0,0]
        self.max_size = max_size
        self.size = size
        self.front = front
        self.rear = rear


    def enqueue(self, data):
        if not self.isFull():
            self.queue[self.rear] = data
            self.rear = int((self.rear + 1) % self.max_size)
            self.size += 1
        else:
          print('Queue is full')

    def dequeue(self):
        if not self.isEmpty():
            print(self.queue[self.front], 'is removed')
            self.front = int((self.front + 1) % self.max_size)
            self.size -= 1
        else:
            print('Queue is empty')

    def isEmpty(self):
        return self.size == 0

    def isFull(self):
        return self.size == self.max_size

    def show(self):
        print ('Queue contents are:')
        for i in range(self.size):
             print (self.queue[int((i+self.front)% self.max_size)])

    # driver program
q = queue(5)
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
q.dequeue()
q.show()