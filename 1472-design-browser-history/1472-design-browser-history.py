class BrowserHistory:
    def __init__(self, homepage: str):
        self.history = [None] * 5000
        self.ptr = 0
        self.history[self.ptr] = homepage
        self.size = 1
        
    def visit(self, url: str) -> None:
        self.ptr += 1
        self.history[self.ptr] = url
        self.size = self.ptr + 1
        
    def back(self, steps: int) -> str:
        while self.ptr > 0 and steps > 0:
            self.ptr -= 1
            steps -= 1
        return self.history[self.ptr]

    def forward(self, steps: int) -> str:
        while self.ptr < self.size - 1 and steps > 0:
            self.ptr += 1
            steps -= 1
        return self.history[self.ptr]
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)