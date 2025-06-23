from rest_framework.response import Response
from rest_framework import status as drf_status

class CustomResponseMixin:
    def custom_response(self, data=None, success=True, err_msg="", status_code=drf_status.HTTP_200_OK):
        return Response({
            "status": success,
            "data": data if success else "",
            "err_msg": err_msg
        }, status=status_code)
