#################################### Test case - 1 #############################
# Input:

# 5
# Sunita
# Faculty
# 23000
# 2
# Jan
# 4
# March
# 6
# Arun
# Admin
# 30000
# 3
# Feb
# 4
# March
# 12
# June
# 10
# Dipak
# Admin
# 25000
# 3
# Jan
# 12
# July
# 5
# Aug
# 3
# Balen
# HR
# 12000
# 3
# Jan
# 12
# July
# 5
# Aug
# 3
# Tarun
# HR
# 78000
# 3
# Jan
# 12
# July
# 5
# Aug
# 3
# 18
# 100

# Output:

# Sunita False
# Arun True
# Dipak True
# Balen True
# Tarun True
# 8600

#################################### Test case - 2 ###########################

# Input:

# 5
# Sunita
# Faculty
# 23000
# 4
# Jan
# 4
# March
# 6
# apr
# 6
# June
# 3
# Arun
# Admin
# 30000
# 3
# Jan
# 4
# March
# 6
# apr
# 6
# Dipak
# Admin
# 25000
# 3
# Jan
# 4
# March
# 6
# apr
# 6
# Balen
# HR
# 12000
# 3
# Jan
# 4
# March
# 6
# apr
# 6
# Tarun
# HR
# 78000
# 3
# Jan
# 4
# March
# 6
# apr
# 6
# 30
# 100

# Output:

# Sunita False
# Arun False
# Dipak False
# Balen False
# Tarun False
# 0

class Employee:
    def __init__(self, name, des, salary, Over):
        self.name = name
        self.des = des
        self.salary = salary
        self.Over = Over
        self.status = False

class Organisation:
    def __init__(self, l):
        self.l = l
        self.list = []

    def check(self, ts):
        self.ts = ts
        for i in self.l:
            c = 0
            for k, v in i.Over.items():
                c += v
            if c >= ts:
                i.status = True
                self.list.append(c)
                print(i.name, i.status)
            else:
                print(i.name, i.status)

    def output(self, rate):
        self.rate = rate
        t = sum(self.list) * rate
        print(t)


l = []
z = int(input("Enter the number of employees: "))
for _ in range(z):
    name = input("Enter employee name: ")
    des = input("Enter employee designation: ")
    salary = int(input("Enter employee salary: "))
    n = int(input("Enter the number of months: "))
    Over = {}
    for _ in range(n):
        month = input("Enter month: ")
        val = int(input("Enter overtime hours: "))
        Over[month] = val
    l.append(Employee(name, des, salary, Over))

o = Organisation(l)
ts = int(input("Enter the overtime threshold: "))
rate = int(input("Enter the overtime rate: "))

o.check(ts)
o.output(rate)

