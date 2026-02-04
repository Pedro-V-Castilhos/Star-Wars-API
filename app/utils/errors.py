from fastapi import HTTPException

# Custom exceptions for better error control
class ResourceNotFoundError(Exception):
    """Exception raised when a resource is not found in the API"""
    pass

class InvalidOrderFieldError(Exception):
    """Exception raised when the sorting field is invalid"""
    def __init__(self, field: str):
        self.field = field
        super().__init__(f"Invalid field for sorting: {field}")

class InvalidPageParameterError(HTTPException):
    """Exception raised when the page parameter is invalid"""
    def __init__(self, detail: str):
        super().__init__(status_code=400, detail=detail)

class InvalidQueryParameterError(HTTPException):
    """Exception raised when a query parameter is invalid"""
    def __init__(self, detail: str):
        super().__init__(status_code=400, detail=detail)

class ExternalAPIError(HTTPException):
    """Exception raised for general external API errors"""
    def __init__(self, status_code: int, detail: str):
        super().__init__(status_code=status_code, detail=detail)
