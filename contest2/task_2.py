class Queue:
    def __init__(self) -> None:
        self._list = list()

    def push(self, element) -> None:
        self._list.append(element)

    def get(self):
        if len(self._list) == 0:
            pass
        else:
            return self._list.pop(0)

    def isEmpty(self) -> bool:
        return len(self._list) == 0

    def expansion(self) -> None:
        lenQueue = len(self._list)
        if lenQueue == 0:
            pass
        else:
            bufQueue = list()
            for i in range(lenQueue):
                value = self._list.pop(0)
                bufQueue.append(value)
                bufQueue.append(value)
            self._list = bufQueue


queue = Queue()
buf = []
countRequest = int(input())
while countRequest:
    num = input().split()
    if num[0] == "1":
        queue.push(int(num[1]))
    elif num[0] == "2":
        queue.expansion()
    else:
        buf.append(queue.get())
    countRequest -= 1

for i in range(len(buf)):
    print(buf[i])