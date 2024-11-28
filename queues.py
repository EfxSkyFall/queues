
while True:
    print("1 -> View the current queue")
    print("2 -> Add item to queue")
    print("3 -> Remove an item from the queue")
    print("4 -> See front of queue")
    print("5 -> Exit")
    choice = input("What operation do you want to utilise : ")

    if choice == "1":
        enqueue()



class queue:

   def __init__(self,size):

       self.maxSize = size
       self.queue = []
       self.front = 0
       self.rear = -1
       self.size = 0

       for i in range(self.maxSize):
           self.queue.append(None)

   def is_full(self):
        if self.size == self.maxSize:
            return True
        else:
            return False
        
   def is_empty(self):
        if self.size == 0:
            return True
        else:
            return False

   def enqueue(self,item):
            if self.is_full() == True:
                print('queue is full!!!')
                return

            else:
                self.rear = (self.rear + 1) % self.maxSize
                item = input("what do you want to enter into this queue? \n")
                self.queue[self.rear] = item
                print('item added to queue')
                self.size += 1

   def show_queue(self):
       print(self.queue)

test_queue = queue(4)
test_queue.enqueue()
test_queue.show_queue()
    
