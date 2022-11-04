import math

class Max_Heap:
	def __init__(self, array=[]):
		self.heaplist = array
		self.heapsize = len(array)
	def parent(self, i):
		return (i - 1)//2

#Определяем левого и правого потомка
	def left(self, i): 
		return 2 * i + 1
	def right(self, i):
		return 2* i + 2

#достраивает невозрастающую пирамиду с корнем в root
	def max_heapify(self, root):
		l, r = self.left(root), self.right(root)
		largest = root
		if l < self.heapsize:
			if self.heaplist[l] > self.heaplist[root]:
				largest = l
		if r < self.heapsize:
			if self.heaplist[r] > self.heaplist[largest]:
				largest = r
		if largest != root:
			self.heaplist[largest], self.heaplist[root] = self.heaplist[root], self.heaplist[largest]
			self.max_heapify(largest)

	def build_heap(self):			#строит пирамиду по массиву
		for i in range(self.heapsize//2 - 1, -1, -1):
			self.max_heapify(i)

	def heap_sort(self):
		self.build_heap()
		for i in range(self.heapsize - 1, 0, -1):
			self.heaplist[0], self.heaplist[self.heapsize - 1] = self.heaplist[self.heapsize - 1], self.heaplist[0]
			self.heapsize -= 1
			self.max_heapify(0)

	def heap_maximum(self):
		return self.heaplist[0]

	def heap_extract_max(self):
		if self.heapsize < 1:
			print('Очередь пуста')
		else:
			maximum = self.heap_maximum()
			self.heaplist[0] = self.heaplist[self.heapsize - 1]
			self.heapsize -= 1
			self.max_heapify(0)
			return maximum 

	def heap_increase_key(self, i, key):
		if self.heaplist[i] > key:
			print('Недопустимое значение ключа')
		else:
			self.heaplist[i] = key
			while self.heaplist[self.parent(i)] <= self.heaplist[i] and i > 0:
				self.heaplist[self.parent(i)], self.heaplist[i] = self.heaplist[i], self.heaplist[self.parent(i)]
				i = self.parent(i)
			return True

	def heap_insert(self, key):
		self.heaplist.append(-math.inf)
		self.heapsize += 1
		self.heap_increase_key(self.heapsize - 1, key)

	def heap_delete(self, i):
		self.heaplist[i] 



## Добавил первый комментарий


heap1 = Max_Heap([21 ,20, 5,6,3, 1, 7656, 32,4 ,543])
heap1.build_heap()
print(heap1.heaplist, len(heap1.heaplist))
heap1.heap_extract_max()
print(heap1.heaplist, len(heap1.heaplist))


