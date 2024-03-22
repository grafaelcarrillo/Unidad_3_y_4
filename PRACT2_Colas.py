class Order:
    def __init__(self, qtty, customer):
        self.customer = customer
        self.qtty = qtty
    
    def print_info(self):
        print("     Customer: " + self.get_customer())
        print("     Quantity: " + str(self.get_qtty()))
        print("     ------------")
    
    def get_qtty(self):
        return self.qtty
    
    def get_customer(self):
        return self.customer
