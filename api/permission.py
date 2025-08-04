from rest_framework.permissions import BasePermission,SAFE_METHODS
class IsReadOnly(BasePermission):
    def has_permission(self,request,view):
        print(request.method)
        if request.method in SAFE_METHODS:
            return True
        else:
            return False
class isGetALL(BasePermission):
    def has_permission(self, request, view):
        allowed_class=['GET','PATCH','DELETE']

        if request.method in allowed_class:
            return True
        else:
            return False
        
class isname(BasePermission):
    def has_permission(self,request,view):
        username = request.user.username

        if username.lower() =='sunny':
            return True
        elif username != '' and len(username) %2 ==0 and request.method in SAFE_METHODS:
            return True
        else:
            return False
        