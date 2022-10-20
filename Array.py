class Array:
    def __init__(self, size):
      self._size = size
      self._items = [None] * size

    # find the first occurence of a value in the array
    def find(self, value):
      for i in range(len(self._items)):
        if self._items[i] == value:
          return i
      return -1

    # deletes an item at an index
    def delete(self, index):
      if index < 0 or index >= self._size:
        raise Exception("Index out of bounds")
      self._items[index] = None

    def __getitem__(self, index):
      return self._items[index]

    # replaces an item at an index
    def __setitem__(self, index, value):
      if index >= self._size or index < 0:
        raise Exception("Index out of bounds")
      self._items[index] = value

    def __len__(self):
      return self._size

    def __str__(self):
      return str(self._items)