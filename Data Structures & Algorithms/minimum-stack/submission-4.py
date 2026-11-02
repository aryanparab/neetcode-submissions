class MinStack:

    def __init__(self):
        self.st = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.st.append(val)
        # Store the minimum up to this point
        val_min = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val_min)

    def pop(self) -> None:
        self.st.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.st[-1]

    def getMin(self) -> int:
        return self.minStack[-1]