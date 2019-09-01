
class GradeException(Exception):
   """Base class for other exceptions"""
   pass

class GradeTooHighException(GradeException):
   """Raised when the input value is too small"""
   pass
class GradeTooLowException(GradeException):
   """Raised when the input value is too large"""
   pass
