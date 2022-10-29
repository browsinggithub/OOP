from calendar import month_abbr


class Home:
    def __init__(self, final_cost, downpayment, rooms,restrooms, squarefeet):
        self.rooms = rooms
        self.downpayment = downpayment
        self.restrooms = restrooms
        self.squarefeet = squarefeet
        self.final_cost = final_cost
    
    def house_payment(self, years):
        # this function will calculate my monthly payments
        loan_balance = self.final_cost - self.downpayment
        yearly_cost = loan_balance / years 
        monthly_cost = yearly_cost / 12
        print(yearly_cost)
        print(monthly_cost)
       
    

house1 = Home(500000, 30000, 4, 3, 3000)
house1.house_payment(15)
        








        
    
