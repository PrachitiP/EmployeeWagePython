import random

class EmployeeWage:
    wage_Per_Hour = 20
    workHour = 0
    dailyWage = 0
    def checkAttendance(self):
        attendance = (random.randint(0, 1))
        if attendance == 1:
            EmployeeWage.workHour = 8
            return 'Employee is present'
        else:
            return 'Employee is absent'

    def calculateWage(self):
        EmployeeWage.dailyWage = EmployeeWage.workHour * EmployeeWage.wage_Per_Hour
        print('Daily Wage is', EmployeeWage.dailyWage)

if __name__ == '__main__':
    print('Welcome to Employee Wage Computation Program')
    emp = EmployeeWage()
    print(emp.checkAttendance())
    print(emp.calculateWage())