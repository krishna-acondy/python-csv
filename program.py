import csv
from collections import namedtuple

with open("data.csv") as data:
    reader = csv.reader(data)
    Person = namedtuple("Person", next(reader))
    rows = [Person(*r) for r in reader]
    with open("other-data.csv") as otherData:
        otherReader = csv.reader(otherData)
        Salary = namedtuple("Salary", next(otherReader))
        otherRows = [Salary(*r) for r in otherReader]
        PersonSalary = namedtuple("PersonSalary", "empId firstName lastName salary")
        personSalaries = [];
        for index, row in enumerate(rows):
            for otherIndex, otherRow in enumerate(otherRows):
                if otherRow.empId == row.empId:
                    personSalary = PersonSalary(row.empId, row.firstName, row.lastName, otherRow.salary)
                    personSalaries.append(personSalary);

        with open('output.csv', 'w') as outputFile:
            writer = csv.writer(outputFile)
            writer.writerow(('empId', 'firstName', 'lastName', 'salary'))    # field header
            writer.writerows([(data.empId, data.firstName, data.lastName, data.salary) for data in personSalaries])