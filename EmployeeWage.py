import random

class EmployeeWage:
    wage_Per_Hour = 20
    workHour = 0
    dailyWage = 0
    isAbsent = 0
    isFullTime = 1
    isPartTime = 2
    fullTimeHours = 8
    partTimeHours = 4


    def checkAttendance(self):
        attendance = random.randint(0, 2)
        return attendance

    def perDayHours(self, attendance_of_emp):
        switcher = {
            0: 0,
            1: EmployeeWage.fullTimeHours,
            2: EmployeeWage.partTimeHours
        }
        EmployeeWage.workHour = switcher.get(attendance_of_emp)
        print(EmployeeWage.workHour)

    def calculateWage(self):
        EmployeeWage.dailyWage =  EmployeeWage.wage_Per_Hour * EmployeeWage.workHour
        print('Daily Wage is')
        return EmployeeWage.dailyWage

if __name__ == '__main__':
    print('Welcome to Employee Wage Computation Program')
    emp = EmployeeWage()
    print(emp.checkAttendance())
    print(emp.perDayHours(emp.checkAttendance()))

    print(emp.calculateWage())
