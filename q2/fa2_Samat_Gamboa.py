'''
Giovanni Roliz S. Gamboa 
07 
9-Samat FA2 
'''

print("\n   Hospital Billing System")
print("--------------------------------")

class Patient:
    def __init__(self, name, bill):
        self.name = name
        self.bill = float(bill*1.000)
        self.discount = float(bill*0.000)
    def calculate_bill(self):
        final_bill =  float(self.bill-self.discount)
        print(f"Final Bill: {final_bill}\n")
    def get_name(self):
        print(f"Patient Name:  {self.name}")
    def set_name(self,name):
        self.name=name
    def get_bill_amount(self):
        print(f"Original Bill: {self.bill}")
    def set_bill_amounnt(self,name):
        self.bill=bill        
        
class Senior(Patient):
    def __init__(self,name,bill):
        self.name=name
        self.bill = float(bill*1.000)
        self.discount = float(bill*0.200)
        
class PhilHealth(Patient):
    def __init__(self,name,bill):
        self.name=name
        self.bill = float(bill*1.000)
        self.discount = float(bill*0.150)
        
RP = Patient("Juan dela Cruz", 1500)
SP = Senior("Maria Santos", 1500)
PP = PhilHealth("Pedro Reyes", 1500)

RP.get_name()
RP.get_bill_amount()
RP.calculate_bill()

SP.get_name()
SP.get_bill_amount()
SP.calculate_bill()

PP.get_name()
PP.get_bill_amount()
PP.calculate_bill()


        
        
        
