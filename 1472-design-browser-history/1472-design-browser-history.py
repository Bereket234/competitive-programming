class ListNode:
    def __init__(self, url= "", next_ = None, prev= None):
        self.url= url
        self.next= next_
        self.prev= prev
class BrowserHistory:

    def __init__(self, homepage: str):
        self.head= ListNode(homepage)
        self.curr= self.head
        

    def visit(self, url: str) -> None:
        self.curr.next= ListNode(url, None, self.curr)
        self.curr= self.curr.next

    def back(self, steps: int) -> str:
        temp= self.curr
        while temp.prev and steps > 0:
            temp= temp.prev
            steps -= 1
        self.curr= temp
        return temp.url
            

    def forward(self, steps: int) -> str:
        temp= self.curr
        
        while temp.next and steps > 0:
            temp = temp.next
            steps-=1
        self.curr = temp
        return temp.url


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)