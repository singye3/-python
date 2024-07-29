def requires_role(required_role):
    def decorator(func):
        def wrapper(self,*args, **kargs):
            if self.role != required_role:
                raise PermissionError(f'Required {required_role} role to access')
            return func(self,*args, **kargs)
        return wrapper
    return decorator
    
class User:
    def __init__(self, role):
        self.role = role
    
    @requires_role('admin')
    def perform_admin_task(self):
        print('Admin task')

guest = User('guest')
try:
    guest.perform_admin_task()
except PermissionError as e:
    print(e)

# Create a User instance with an admin role
admin = User("admin")
admin.perform_admin_task()
        