from LinkedList import LinkedList

'''
Stack Class
'''
class Stack(LinkedList):
	'Stack implemented as a Linked List - LIFO'

	# ctor
	def __init__(self):
		self.stack = LinkedList()

	# push element to top of stack
	def push(self, val):
		self.stack.insertFront(val)

	# pop element from top of stack
	def pop(self):
		popVal = self.stack.head.data
		self.stack.removeFront()
		return popVal

	# show the top element in stack
	def peek(self):
		print self.stack.head.data

	# print out the stack
	def printStack(self):
		self.stack.printLL()


'''
Queue Class
'''
class Queue(LinkedList):
	'Queue implemented as a Linked List - FIFO'

	# ctor
	def __init__(self):
		self.queue = LinkedList()

	# enqueue element into back of queue
	def enqueue(self, val):
		self.queue.insertBack(val)

	# dequeue element from front of queue
	def dequeue(self):
		deqVal = self.queue.head.data
		self.queue.removeFront()
		return deqVal

	# print out the queue
	def printQueue(self):
		self.queue.printLL()


if __name__ == "__main__":
	print "Here is the Stack:"
	stack = Stack()
	stack.push(1)
	stack.push(2)
	stack.push(3)
	stack.push(3)
	stack.push(3)
	#stack.pop()
	#stack.pop()
	#stack.peek()
	stack.printStack()

	print "Here is the Queue:"
	queue = Queue()
	queue.enqueue(1)
	queue.enqueue(2)
	queue.enqueue(3)
	#queue.dequeue()
	queue.printQueue()