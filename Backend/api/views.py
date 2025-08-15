from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from utils import extras

@api_view(['GET'])
def validate(request):
    try:
        original_url = request.headers.get("X-O-URL")
        if not original_url:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        is_malicious = extras.prediction(original_url)
        if is_malicious:
            return Response(status=status.HTTP_403_FORBIDDEN)
        return Response(status=status.HTTP_200_OK)
    except Exception:
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
