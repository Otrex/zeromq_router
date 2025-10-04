from .BaseException import BaseException

class NotFoundException(BaseException):
  def __init__(self, message=None, path=None):
    super().__init__(message, 404, path)
    self.message = message
    self.status_code = 404
    self.error_code = 'NOT_FOUND'
    self.path = path
