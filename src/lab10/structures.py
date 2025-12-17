from collections import deque

class Stack:
    def __init__(self):
        # внутреннее хранилище стека
        self._data = []

    def push(self, item):
        # корректно: добавление в конец списка O(1) амортизированно
        self._data.append(item)

    def pop(self):
        # обработка случая пустого стека (сейчас IndexError от list)
        if self.is_empty():
            raise IndexError('Пустой стек')
        return self._data.pop()

    def peek(self):
        # вернуть None для пустого стека
        if self.is_empty():
            return None
        return self._data[-1]

    def is_empty(self) -> bool:
        return len(self._data) == 0
    
    def __len__(self):
        return len(self._data)


class Queue:
    def __init__(self):
        
        self._data = deque()

    def enqueue(self, item):
        # вставка в конец
        self._data.append(item)

    def dequeue(self):
        # ошибка: удаление с конца, а не с начала
        return self._data.popleft()

    def peek(self):
        # TODO: корректное поведение при пустой очереди
        if not self.is_empty():
            return None
        return self._data[0]

    def is_empty(self) -> bool:
        return len(self._data) == 0
    
    def __len__(self):
        return len(self._data)
    
print('Stack')
stack = Stack()
print(f'Пустой стек: {stack.is_empty()}')  # True
# добавляем элементы
stack.push(24)
stack.push(25)
stack.push(26)
print(f'размер стека после добавления 3 элементов: {len(stack)}')  # 3
# верхний элемент без удаления
print(f'верхний элемент (peek): {stack.peek()}')  # 26
# удаляем элементы (LIFO - Last In First Out)
print(f'удаляем {stack.pop()}')  # 26
print(f'удаляем {stack.pop()}')  # 25
print(f'оставшийся размер: {len(stack)}')  # 1

print('Queue')
queue = Queue()
print(f'пустая очередь: {queue.is_empty()}')  # True
# добавляем элементы
queue.enqueue(15)
queue.enqueue(20)
queue.enqueue(25)
print(f'размер очереди после добавления 3 элементов: {len(queue)}')  # 3
# первый элемент без удаления
print(f'первый элемент: {queue.peek()}') # 15
# удаляем элементы (FIFO - First In First Out)
print(f'удаляем (dequeue): {queue.dequeue()}')  # 15
print(f'удаляем (dequeue): {queue.dequeue()}')  # 20
print(f'оставшийся размер: {len(queue)}')  # 1