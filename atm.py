class Atm (object):
    def __init__(self,atm_card_no,pin_number,address):
        
        self.atm_card_no = atm_card_no
        self.pin_number = pin_number
        self.Address = address

        def CashWithDrawl(self):
            print (" You Have with dawed $100 From your bank account")
        def BalanceEnquiry(self):
            print (" You have $325.45 Left in ur bank")
        def BankEnquiry(self):
            print(" Have you taken out $100 from your account? If not then pls click this link:- https://this_is_a_troll.com")
        def Address(self):
            print("is this your address")
user1= Atm("23784832","7346","chennai")
print(user1.pin_number)   
user2 = Atm("994782781","2783","marashtra")
print(user2.atm_card_no)
