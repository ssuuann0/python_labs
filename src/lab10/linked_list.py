class Node:  # узел односвязного списка.
    def __init__(self, value, next=None):
        self.value = value  # значение элемента.
        self.next = next  # ссылка на следующий узел или None, если это последний узел.


class SinglyLinkedList:  # односвязный список, состоящий из узлов Node
    def __init__(self):
        self.head: Node | None = None  # первый узел
        self.tail: Node | None = None  # хвост списка 
        # ошибка: размер не обновляется
        self._size = 0

    def append(self, value):
        """Добавить элемент в конец """
        new_node = Node(value)
        if self.head is None:
            # если список пуст, новый узел становится и head и tail
            self.head = new_node
            self.tail = new_node
        else:
            # добавляем после tail и обновляем tail
            self.tail.next = new_node
            self.tail = new_node
        self._size += 1

    def prepend(self, value):
        """Добавить элемент в начало списка"""
        new_node = Node(value, next=self.head)
        self.head = new_node
        self._size += 1

    def insert(self, idx, value):
        """Вставка по индексу"""
        if idx < 0 or idx > self._size:
            raise IndexError(f"Index {idx} out of range [0, {self._size}]")

        if idx == 0:
            self.prepend(value)
            return

        if idx == self._size:  # оптимизация для вставки в конец
            self.append(value)
            return

        current = self.head
        # Нет ошибки: idx проверен выше, current гарантированно не None для idx > 0
        for _ in range(idx - 1):
            current = current.next

        new_node = Node(value, next=current.next)
        current.next = new_node

        # обновляем tail если вставили после него
        if current == self.tail:
            self.tail = new_node

        self._size += 1  # увеличиваем размер

    def remove(self, value):
        """Удалить первое вхождение значения value"""
        if self.head is None:
            return  # список пуст, нечего удалять

        # eсли удаляем первый элемент
        if self.head.value == value:
            self.head = self.head.next
            self._size -= 1
            if self.head is None:  # если список стал пустым
                self.tail = None
            return

        # ищем элемент для удаления
        current = self.head
        while current.next is not None and current.next.value != value:
            current = current.next

        # если нашли элемент для удаления
        if current.next is not None:
            current.next = current.next.next
            self._size -= 1
            # если удалили последний элемент
            if current.next is None:
                self.tail = current

    def remove_at(self, idx):
        """удалить элемент по индексу idx"""
        if idx < 0 or idx >= self._size:
            raise IndexError(f"Index {idx} out of range [0, {self._size - 1}]")

        if idx == 0:
            self.head = self.head.next
            self._size -= 1
            if self.head is None:  # если список стал пустым
                self.tail = None
            return

        current = self.head
        for _ in range(idx - 1):
            current = current.next

        # удаляем элемент
        current.next = current.next.next
        self._size -= 1

        # обновляем tail если удалили последний элемент
        if current.next is None:
            self.tail = current

    def __iter__(self):
        current = self.head
        while current is not None:
            yield current.value
            current = current.next

    def __len__(self):
        return self._size

    def __repr__(self):
        values = list(self)
        return f"SinglyLinkedList({values})"
    
lst = SinglyLinkedList()
# добавление элементов
lst.append(1)
lst.append(2)
lst.append(3)
print(lst)  # SinglyLinkedList([1, 2, 3])
print(len(lst))  # 3
# добавление в начало
lst.prepend(0)
print(lst)  # SinglyLinkedList([0, 1, 2, 3])
# вставка по индексу
lst.insert(2, 99)
print(lst)  # SinglyLinkedList([0, 1, 99, 2, 3])
# удаление по значению
lst.remove(99)
print(lst)  # SinglyLinkedList([0, 1, 2, 3])