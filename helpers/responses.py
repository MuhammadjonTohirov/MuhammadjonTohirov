import datetime
from datetime import timezone


class AppResponse:
    def __init__(self, body, is_error=False):
        self.body = body
        self.is_error = is_error

    def __str__(self):
        return self.body

    def unknown_error_body(self, message='Failure', code=101):
        return {
            'message': message,
            'error': {
                'body': self.body,
                'server_time': datetime.datetime.now(),
            },
            'status': code
        }

    def success_body(self, key: str, updated_at, code=200):
        return {
            'message': 'Success',
            'success': {
                key: self.body,
                'updated_at': updated_at if updated_at is not None else datetime.datetime.now(),
                'server_time': datetime.datetime.now(),
            },
            'status': code
        }
