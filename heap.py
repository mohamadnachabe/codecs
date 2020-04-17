import enum


def get_left_child_index(parent_i):
    return (parent_i * 2) + 2


def get_parent_index(child_i):
    return int((child_i - 2) / 2)


def get_right_child_index(parent_i):
    return (parent_i * 2) + 1


def has_parent(child_i):
    return child_i != 0


class MinHeap:
    heap = []

    def __init__(self):
        pass

    def has_right_child(self, parent_i):
        return (parent_i * 2) + 1 < len(self.heap)

    def has_left_child(self, parent_i):
        return (parent_i * 2) + 2 < len(self.heap)

    def get_parent(self, index):
        if not has_parent(index):
            return None
        parent_index = get_parent_index(index)
        return self.heap[parent_index]

    def get_right_child(self, index):
        if not self.has_right_child(index):
            return None
        child_index = get_right_child_index(index)
        return self.heap[child_index]

    def get_left_child(self, index):
        if not self.has_left_child(index):
            return None
        child_index = get_left_child_index(index)
        return self.heap[child_index]

    def swap(self, index1, index2):
        tmp = self.heap[index1]
        self.heap[index1] = self.heap[index2]
        self.heap[index2] = tmp

    def peek(self):
        if len(self.heap) > 0:
            return self.heap[0]
        else:
            return None

    def pop(self):
        if len(self.heap) == 0:
            return None

        popped = self.heap[0]
        last_element = self.heap[self.last()]
        del self.heap[self.last()]

        self.heap[0] = last_element

        self.heapify_down()
        return popped

    def insert(self, element):
        self.heap.append(element)
        self.heapify_up()

    def last(self):
        return len(self.heap) - 1

    def heapify_down(self):
        index = 0
        while self.has_left_child(index):
            if self.get_left_child(index) < self.heap[index] \
                    and self.get_left_child(index) < self.get_right_child(index):
                self.swap(get_left_child_index(index), index)
                index = get_left_child_index(index)

            elif self.get_right_child(index) < self.heap[index]:
                self.swap(get_right_child_index(index), index)
                index = get_right_child_index(index)

            else:
                return

    def heapify_up(self):
        index = self.last()
        while has_parent(index) and self.get_parent(index) > self.heap[index]:
            self.swap(index, get_parent_index(index))
            index = get_parent_index(index)


if __name__ == '__main__':
    heap = MinHeap()
    heap.insert(8)
    heap.insert(9)
    heap.insert(15)
    heap.insert(9)
    heap.insert(3)
    heap.insert(20)
    heap.insert(4)
    heap.insert(7)
    heap.insert(10)
    heap.insert(13)
    heap.insert(1)

    print(heap.pop())
    print(heap.pop())
    print(heap.pop())
    print(heap.pop())
    print(heap.pop())
    print(heap.pop())
    print(heap.pop())
    print(heap.pop())
    print(heap.pop())

    print()
