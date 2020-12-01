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
    monthlyWageData = []

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
        
     def perDayHours(self, attendance_of_emp):
        switcher = {
            0: 0,
            1: EmployeeWage.fullTimeHours,
            2: EmployeeWage.partTimeHours
        }
        EmployeeWage.workHour = switcher.get(attendance_of_emp)
        print(EmployeeWage.workHour)


    def calculateMonthlyWage(self):
        monthlyWage = 0
        empHours = 0
        day = 1
        attendance = 0
        while True:
            daily_wage_data = {}
            print(f"day {day} : ")
            attendance = EmployeeWage.checkAttendance(self)
            EmployeeWage.hours_per_day = EmployeeWage.employee_work_hours(self, attendance)
            empHours = empHours + EmployeeWage.workHour
            EmployeeWage.empDailyWage = EmployeeWage.wage_Per_Hour * EmployeeWage.workHour
            print(f"Employee's salary for day {day} is : {EmployeeWage.empDailyWage}")
            employee_wage_for_a_month = monthlyWage + EmployeeWage.empDailyWage
            daily_wage_data[f"{EmployeeWage.empDailyWage}"] = f"{monthlyWage}"
            EmployeeWage.monthlyWageData.append(daily_wage_data)
            day = day + 1
            if (empHours >= 100) or (day >= 20):
                print(f"Employee hours : {empHours} and Days : {day}")
                break

        print(f"\nEmployee's Salary for the Entire Month is: {employee_wage_for_a_month}")
        print(f"\n{EmployeeWage.monthlyWageData}")
if __name__ == '__main__':
    print('Welcome to Employee Wage Computation Program')
    emp = EmployeeWage()
    print(emp.perDayHours(emp.checkAttendance()))
    print(emp.calculateMonthlyWage())
