from collections import deque

"""
    
"""


class CoopCorouCore:
    def __init__(self) -> None:
        self.readyRoutines: deque = deque()

    def hold_call(self, coroutine) -> None:
        self.readyRoutines.append(coroutine)

    def run(self) -> None:
        while self.readyRoutines:
            self.curr = self.readyRoutines.popleft()
            try:
                self.curr.send(None)
                if self.curr:
                    self.hold_call(self.curr)
            except StopIteration:
                pass
