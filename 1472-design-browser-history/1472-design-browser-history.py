class BrowserHistory:
    def __init__(self, homepage: str):
        self.curr = homepage
        self.fstack = deque()
        self.bstack = deque()

    def visit(self, url: str) -> None:
        self.bstack.append(self.curr)
        self.curr = url
        self.fstack.clear()

    def back(self, steps: int) -> str:
        while len(self.bstack) > 0 and steps > 0:
            self.fstack.append(self.curr)
            self.curr = self.bstack.pop()
            steps -= 1
        return self.curr

    def forward(self, steps: int) -> str:
        while len(self.fstack) > 0 and steps > 0:
            self.bstack.append(self.curr)
            self.curr = self.fstack.pop()
            steps -= 1
        return self.curr
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)