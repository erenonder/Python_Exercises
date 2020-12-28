from file2 import Employee as emp


if __name__ == '__main__':
    test_emp = emp('Nihan', 35)
    test_emp.check_employee(40)

    print(test_emp.__str__())
    print(test_emp)
