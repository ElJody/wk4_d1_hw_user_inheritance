from datetime import datetime as dt
import os 

class User():
    def __init__(self, first, last, email):
        self.first = first.title()
        self.last = last.title()
        self.email = email
        self.created_on = dt.utcnow()

    def change_first(self):
        name = self.first
        print(f'{self.first}, Is Your Current First Name...')
        self.first = input('\nPlease Enter a New First Name: ').title()
        print(f'{name} - Has Now Been Changed To - {self.first}')

    def change_last(self):
        name = self.last
        print(f'{self.last}, Is Your Current Last Name...')
        self.last = input('\nPlease Enter a New Last Name: ').title()
        print(f'{name} - Has Now Been Changed To - {self.last}')

    def __str__(self):
        return f'<User | {self.email}>'

    def __repr__(self):
        return f'<User | {self.email}+{self.created_on.strftime("%c")}>'

    def __hash__(self):
        return hash(self.email + self.created_on.strftime("%c"))

    def __eq__(self, __o):                                                         
        return self.created_on == __o.created_on
    
    def __lt__(self, __o):
        return self.created_on < __o.created_on

    def __gt__(self, __o):
        return self.created_on > __o.created_on

    def __le__(self, __o):
        return self.created_on <= __o.created_on

    def __ge__(self, __o):
        return self.created_on >= __o.created_on 
    

class Employee(User):
    def __init__(self, first, last, email, address, security, dept):
        super().__init__(first, last, email)
        self.address = address
        self.security = security
        self.dept = dept.title()

    @property
    def id(self):
        return self.first+' '+self.last+'-'+self.dept
    
    def change_dept(self):
        dept = self.dept
        print(f'Your Current Department Is : {self.dept}')
        self.dept = input('\nPlease Enter New Department: ').title()
        print(f'{dept} - Has Now Been Changed To - {self.dept}')

class Customer(User):
    def __init__(self, first, last, email, shipping, billing):
        super().__init__(first, last, email)
        self.shipping = shipping
        self.billing = billing

    @property
    def id(self):
        return self.email+' / '+self.shipping
    
    def change_billing(self):
        address = self.billing
        print(f"{self.billing} <- Is Your Current Billing Address...")
        self.billing = input('\nPlease Enter a New Billing Address ->')
        print(f'{address} <- Has Now Been Changed To ->  {self.billing}')
    
    def change_shipping(self):
        address = self.shipping
        print(f"{self.shipping} <- Is Your Current Billing Address...")
        self.shipping = input('\nPlease Enter a New Billing Address -> ')
        print(f'{address} <- Has Now Been Changed To -> {self.shipping}')

    
todd = Employee('Todd', 'Rundgren', 'todd@nooneknows.com', '227 Main', 7, 'HR' )
bob = Employee('Bob', 'Calvert', 'bob@ohno.com', '5544 Lucy St.', 2, 'Reclamation' )
sully = Employee('Sully', 'Davis', 'whenindoubt@whipitout.com', '1313 Mockingbird Ln', 9, 'IT' )
bill = Customer('Bill', 'Parker', 'bill@oksure.com', '313 Canvas St.', '333 Oakland Ave.' )
pete = Customer('Pete', 'Pan', 'pete@help.org', '871 Tuffit Ln', '2319 Park Dr.' )
suzy = Customer('Suzy', 'Snoddgrass', 'suzy@yesnomaybe.com', '969 Waylon St.', '696 Alma Dr.')

users = sorted([todd, bill, suzy, sully, bob, pete], reverse=True)
print(users)