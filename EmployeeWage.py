import random

class EmployeeWage:
    def checkAttendance(self):
        attendance = (random.randint(0, 1))
        if attendance == 1:
            return 'Employee is present'
        else:
            return 'Employee is absent'

if __name__ == '__main__':
    print('Welcome to Employee Wage Computation Program')
    emp = EmployeeWage()
    print(emp.checkAttendance())