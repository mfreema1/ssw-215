class bankAccount:
    'Class made to model a bank account for the Scrooge McDuck assignment'
    name_of_scrooge = 'Scrooge McDuck'
    percentage_of_max_withdraw = 0.1
    penalty_cost = 5
    ducks = []

    def __init__(self, name, accID, balance):
        self.numWithdrawals = 0
        self.numDeposits = 0
        self.numPenalties = 0
        self.name = name
        self.accID = accID
        self.balance = balance
        self.maxWithdraw = self.balance * self.percentage_of_max_withdraw
        self.ducks.append(self)

    def withdraw(self, amount):
        if(amount > self.maxWithdraw):
            self.numPenalties += 1
            self.balance -= self.penalty_cost
            self.updateMaxWithdrawAmount()
            self.depositInScrooge(self.penalty_cost)
            self.printAccounts()
        else:
            self.balance -= amount
            self.numWithdrawals += 1
            self.depositInOtherDucks(self.accID, amount)
            self.printAccounts()

    def depositInOtherDucks(self, accID, amount):
        for duck in self.ducks:
            if(duck.accID != accID):
                duck.deposit(amount)
                self.withDrawFromScrooge(amount)
        self.printAccounts()

    def depositInScrooge(self, amount):
        for duck in self.ducks:
            if duck.name == self.name_of_scrooge:
                duck.balance += amount

    def withDrawFromScrooge(self, amount):
        for duck in self.ducks:
            if duck.name == self.name_of_scrooge:
                duck.balance -= amount

    def updateMaxWithdrawAmount(self):
        self.maxWithdraw = self.balance * self.percentage_of_max_withdraw

    def printAccounts(self):
        for duck in self.ducks:
            print(duck.name + ' has ' + str(duck.balance) + ' dollars in their account')
        print()

    def deposit(self, amount):
        self.balance += amount
        self.numDeposits += 1

scrooge = bankAccount('Scrooge McDuck', 100001, 1000000)
huey = bankAccount('Huey Duck', 700007, 150)
dewey = bankAccount('Dewey Duck', 800008, 350)
louie = bankAccount('Louie Duck', 900009, 25)

#run simulation
louie.withdraw(2)
dewey.withdraw(20)
huey.withdraw(20)
louie.withdraw(10)
dewey.withdraw(20)
huey.withdraw(30)
louie.withdraw(40)