class ListNode: 
    def __init__(self, url: str):
        self.url = url 
        self.prev = None 
        self.next = None 

class BrowserHistory:

    def __init__(self, homepage: str):
        self.current = ListNode(homepage) 
        self.length = 0
        
    def visit(self, url: str) -> None:
        node, prev = ListNode(url), self.current 
        prev.next = node 
        node.prev = prev 
        node.next = None
        self.current = node 
        
    def back(self, steps: int) -> str:

        while self.current.prev and steps > 0:
                self.current = self.current.prev
                steps -= 1 
            
        return self.current.url 
        
        
        
    def forward(self, steps: int) -> str:

        while self.current.next and steps > 0: 
                self.current = self.current.next 
                steps -= 1 
        
        return self.current.url  
        



# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)