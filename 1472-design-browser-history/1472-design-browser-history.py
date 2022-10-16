class ListNode:
    def __init__(self, url, prev_node= None, next_node=None):
        self.url = url
        self.prev_node = prev_node
        self.next_node = next_node

class BrowserHistory:
    def __init__(self, homepage: str):
        self.head = self.current_node = ListNode(homepage)

    def visit(self, url: str) -> None:
        self.current_node.next_node = ListNode(url, prev_node=self.current_node)
        self.current_node = self.current_node.next_node

    def back(self, steps: int) -> str:
        for _ in range(steps):
            if self.current_node.prev_node is not None:
                self.current_node = self.current_node.prev_node
            else:
                return self.current_node.url
        return self.current_node.url

    def forward(self, steps: int) -> str:
        for _ in range(steps):
            if self.current_node.next_node is not None:
                self.current_node = self.current_node.next_node
            else:
                return self.current_node.url
        return self.current_node.url