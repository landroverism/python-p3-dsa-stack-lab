class Stack:

    def __init__(self, items = [], limit = 100):
        pass

    def isEmpty(self):
        pass

    def push(self, item):
        pass

    def pop(self):
        pass

    def peek(self):
        pass
    
    def size(self):
        pass

    def full(self):
        pass

    def search(self, target):
        pass

    if target in self.items:
            return self.size() - self.items.index(target) - 1
          return -1

    #Bonus Questions
class TestStack:
    def test_init(self):
        stk = Stack([1, 2, 3, 4, 5], 10)
        expected = [1, 2, 3, 4, 5]
        assert all(expected[index] == stk.items[index] for index in range(len(expected)))
        assert stk.limit == 10

    def test_push(self):
        stk = Stack([1, 2, 3, 4, 5], 6)
        stk.push(6)
        assert stk.size() == 6
        assert stk.full()

        try:
            stk.push(7)
        except Exception as e:
            assert str(e) == "Stack is full"

    def test_size(self):
        stk = Stack([1, 2, 3, 4, 5], 10)
        assert stk.size() == 5

    def test_empty(self):
        stk = Stack()
        assert stk.isEmpty()

        stk.push(1)
        assert not stk.isEmpty()

        stk.pop()
        assert stk.isEmpty()

    def test_full(self):
        stk = Stack([1, 2, 3, 4, 5], 5)
        assert stk.full()

        stk.pop()
        assert not stk.full()

    def test_search(self):
        stk = Stack([5, 6, 7, 8, 9, 10], 10)
        assert stk.search(5) == 5
        assert stk.search(6) == 4
        assert stk.search(7) == 3
        assert stk.search(8) == 2
        assert stk.search(9) == 1
        assert stk.search(10) == 0
        assert stk.search(15) == -1


test = TestStack()
test.test_init()
test.test_push()
test.test_size()
test.test_empty()
test.test_full()
test.test_search()
