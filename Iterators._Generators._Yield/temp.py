def hello_world(n):
    for i in range(n):
        yield 'hello world'


if __name__ == '__main__':
    for item in hello_world(4):
        print(item)


def my_range(start, finish):

    while start < finish:
        yield start
        start += 1


if __name__ == '__main__':
    for item in my_range(1, 5):
        print(item)

class HelloWorld:

    def __init__(self, n):
        self.n = n

    def __iter__(self):
        self.cursor = 0
        return self

    def __next__(self):
        if self.cursor >= self.n:
            raise StopIteration
        self.cursor += 1
        return 'hello world'


if __name__ == '__main__':
    for item in HelloWorld(4):
        print(item)
