from exception import *


class Form:

    def __init__(self, name:str, grade_sign:int, grade_exec:int ,is_signed:bool=False):
        self.name = name
        self.is_signed = is_signed
        if grade_sign > 150 or grade_exec > 150:
            raise GradeTooLowException
        elif grade_sign < 1 or grade_exec < 1:
            raise GradeTooHighException
        self.grade_sign = grade_sign
        self.grade_exec = grade_exec

    def __str__(self):
        return f"{self.name} sign grade: {self.grade_sign}, exec grade: {self.grade_exec}, is signed: {self.is_signed}"


if __name__=='__main__':
    form1 = Form('Awesome form', False, 80, 40)
    print(form1)
    # print(bureaucrat1.name, bureaucrat1.grade)