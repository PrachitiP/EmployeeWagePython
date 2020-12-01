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
    empDailyWage = 0

    def checkAttendance(cls):
        presence = random.randint(0, 2)
        return presence

    def employee_work_hours(cls, attendance_of_employee):
        if attendance_of_employee == EmployeeWage.isFullTime:
            print("Employee is present for : Full Time")
            return EmployeeWage.fullTimeHours
        elif attendance_of_employee == EmployeeWage.isPartTime:
            print("Employee is present for : Part time")
            return EmployeeWage.partTimeHours
        else:
            print("Employee is Absent")
            return 0

    def calculateMonthlyWage(self):
        monthlyWage = 0
        empHours = 0
        day = 1
        attendance = 0
        while True:
            print(f"day {day} : ")
            attendance = EmployeeWage.checkAttendance(self)
            EmployeeWage.workHours = EmployeeWage.employee_work_hours(self, attendance)
            empHours = empHours + EmployeeWage.workHour
            EmployeeWage.employee_daily_wage = EmployeeWage.wage_Per_Hour * EmployeeWage.workHour
            print(f"Employee's salary for day {day} is : {EmployeeWage.empDailyWage}")
            monthlyWage = monthlyWage + EmployeeWage.empDailyWage
            day = day + 1
            if (empHours >= 100) or (day >= 20):
                print(f"Employee hours : {empHours} and Days : {day}")
                break

        print(f"\nEmployee's Salary for the Entire Month is: {monthlyWage}")


if __name__ == '__main__':
    print('Welcome to Employee Wage Computation Program')
    emp = EmployeeWage()
    print(emp.calculateMonthlyWage())
