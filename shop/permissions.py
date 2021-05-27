# class BasePermission(object):

#     """
#     A base class from which all permission classes shoud inherit
#     """

#     def has_permission(self,request,view):
#         """
#         Return true if permission is granted ,False if not
#         """
#         return True

#     def has_object_permission(self,request,view,obj):
#         """
#         Return True if permission is granted, False if not
#         """    
#         return True

from rest_framework import permissions

class IsAuthorOrReadOnly (permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        # Read-only permission are allowed for amy request
        if request.method in permissions.SAFE_METHODS:
            return True
        # Write permissions are  only allowed to the author of the post    
        return obj.author == request.user    

        #return super().has_object_permission(request, view, obj)