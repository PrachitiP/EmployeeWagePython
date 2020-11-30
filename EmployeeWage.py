import random

class EmployeeWage:
    wage_Per_Hour = 20
    workHour = 0
    dailyWage = 0
    isFullTime = 1
    isPartTime = 2
    fullTimeHours = 8
    partTimeHours = 4
    def checkAttendance(self):
        attendance = (random.randint(0, 2))
        if attendance == EmployeeWage.isFullTime:
            EmployeeWage.workHour = EmployeeWage.fullTimeHours
            return 'Employee is present full time'

        elif attendance == EmployeeWage.isPartTime:
            EmployeeWage.workHour == EmployeeWage.partTimeHours
            return 'Employee is present part time'

        else:
            EmployeeWage.workHour = 0
            return 'Employee is absent'
    def calculateWage(self):
        EmployeeWage.dailyWage = EmployeeWage.workHour * EmployeeWage.wage_Per_Hour
        print('Daily Wage is')
        return EmployeeWage.dailyWage

if __name__ == '__main__':
    print('Welcome to Employee Wage Computation Program')
    emp = EmployeeWage()
    print(emp.checkAttendance())
    print(emp.calculateWage())
