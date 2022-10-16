class BrowserHistory:

    def __init__(self, homepage: str):
        self.ptr = 0
        self.page = [homepage] 

    def visit(self, url: str) -> None:
        self.page = self.page[:self.ptr+1] 
        self.page.append(url)
        self.ptr += 1 

    def back(self, steps: int) -> str:
        self.ptr = max(0, self.ptr-steps)
        return self.page[self.ptr]

    def forward(self, steps: int) -> str:
        self.ptr = min(len(self.page)-1, self.ptr + steps)
        return self.page[self.ptr]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)