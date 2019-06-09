# Left child: 2i + 1
# Right child: 2i + 2
# Parent: (i - 1) // 2


class Heap:
    def __init__(self):
        self.storage = []

    def insert(self, value):
        self.storage.append(value)

        return self._bubble_up(self.get_size() - 1)

    def delete(self):
        storage = self.storage

        storage[0], storage[self.get_size() - 1] = (
            storage[self.get_size() - 1],
            storage[0],
        )

        pop = storage.pop()
        self._sift_down(0)

        return pop

    def get_max(self):
        return self.storage[0]

    def get_size(self):
        return len(self.storage)

    def _bubble_up(self, index):
        storage = self.storage

        if index == 0:
            return

        if storage[(index - 1) // 2] > storage[index]:
            return
        elif storage[(index - 1) // 2] < storage[index]:
            storage[(index - 1) // 2], storage[index] = (
                storage[index],
                storage[(index - 1) // 2],
            )

        return self._bubble_up((index - 1) // 2)

    def _sift_down(self, index):
        storage = self.storage
        max_child_index = None

        if index * 2 + 1 > self.get_size():
            return
        elif index * 2 + 2 >= self.get_size():
            max_child_index = index * 2 + 1
        elif storage[index * 2 + 1] > storage[index * 2 + 2]:
            max_child_index = index * 2 + 1
        else:
            max_child_index = index * 2 + 2

        if storage[index] < storage[max_child_index]:
            storage[index], storage[max_child_index] = (
                storage[max_child_index],
                storage[index],
            )
            self._sift_down(max_child_index)
        else:
            return
