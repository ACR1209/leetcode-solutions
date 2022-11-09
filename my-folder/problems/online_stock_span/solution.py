class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        output = 1
        while self.stack:
            pricetmp,val = self.stack.pop()
            if price < pricetmp:
                self.stack.append((pricetmp,val))
                self.stack.append((price,output))
                return output
            else:
                output += val
        self.stack.append((price,output))
        return output
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)