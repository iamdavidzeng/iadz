class ObjectPool:
    def __init__(self, queue, auto_get=False) -> None:
        self._queue = queue
        self.item = self._queue.get() if auto_get else None

    def __enter__(self):
        if self.item is None:
            self.item = self._queue.get()
        return self.item

    def __exit__(self, Type, value, traceback):
        if self.item is not None:
            self._queue.put(self.item)
            self.item = None

    def __del__(self):
        if self.item is not None:
            self._queue.put(self.item)
            self.item = None


def main():
    """
    >>> import queue
    >>> def test_object(queue):
    ...    pool = ObjectPool(queue, True)
    ...    print('Inside func: {}'.format(pool.item))
    >>> sample_queue = queue.Queue()
    >>> sample_queue.put('yam')
    >>> with ObjectPool(sample_queue) as obj:
    ...    print('Inside with: {}'.format(obj))
    Inside with: yam
    >>> print('Outside with: {}'.format(sample_queue.get()))
    Outside with: yam
    >>> sample_queue.put('sam')
    >>> test_object(sample_queue)
    Inside func: sam
    >>> print('Outside func: {}'.format(sample_queue.get()))
    Outside func: sam

    if not sample_queue.empty():
        print(sample_queue.get())
    """


if __name__ == "__main__":
    import doctest

    doctest.testmod()
