from exception import *


class Bureaucrat:

    def __init__(self, name: str, grade: int):
        self.name = name
        if grade > 150:
            raise GradeTooLowException
        elif grade < 1:
            raise GradeTooHighException
        self.grade = grade

    def __str__(self):
        return f"{self.name} grade: {self.grade}"



if __name__=='__main__':
    bureaucrat1 = Bureaucrat('Bob', 1000)
    print(bureaucrat1)
    # print(bureaucrat1.name, bureaucrat1.grade)