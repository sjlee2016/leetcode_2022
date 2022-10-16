class Page :
    def __init__(self, url, prev=None) :
        self.url = url
        self.next = None 
        self.prev = prev 
        
class BrowserHistory:

    def __init__(self, homepage: str):
        self.homePage = Page(homepage,None) 
        self.currentPage = self.homePage  

    def visit(self, url: str) -> None:
        newPage = Page(url, self.currentPage)
        self.currentPage.next = newPage 
        newPage.prev = self.currentPage
        self.currentPage = newPage 

    def back(self, steps: int) -> str:
        
        for _ in range(steps) :
            if self.currentPage.prev is None :
                return self.currentPage.url
            else :
                self.currentPage = self.currentPage.prev 
        return self.currentPage.url

    def forward(self, steps: int) -> str:
        

        for _ in range(steps) :
            if self.currentPage.next is None :
                return self.currentPage.url
            else :
                self.currentPage = self.currentPage.next 
                
        return self.currentPage.url

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)