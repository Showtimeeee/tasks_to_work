# первый класс не справится с большими данными, но простой
# во втором вставка будет заблокирована, как только размер будет достигнут, для больших данных

class Cross:
    def __init__(self):
        self.lst = []
        self.res = ""
    
    def append_el(self, el):
        self.lst.append(el)

    def get_el(self):
        # чистит очередь
        if self.lst:
            res = self.lst.pop(0)
        else:
            res = self.lst[0]
        print(res)
        return res

    def show_lst(self):
        print (self.lst)
       
#crs = Cross()
#crs.append_el(30)
#crs.append_el('item')
#crs.get_el()
#crs.show_lst()


class Cycles_cross:
    def __init__(self, size):
        self._items = [0] * size
        self._head = 0
        self._tail = 0

        self._count = 0
        self._size = size

    def push(self, el):
        if self.full():
            raise Exception("Queue is full!")
        self._items[self._head] = el
        self._count += 1
        self._head = self.next_index(self._head)

    def pop(self):
        if self.empty():
            raise Exception("Queue is empty!")
        item = self._items[self._tail]
        self._count -= 1
        self._tail = self.next_index(self._tail)
        return item

    def count(self):
        return self._count

    def size(self):
        return self._size

    def full(self):
        return self._count == self._size

    def empty(self):
        return self._count == 0

    def next_el(self, index):
        temp = index + 1
        if temp >= self._size:
            temp = 0
        return temp

# ccross = Cycles_cross()
# ccross.push()



