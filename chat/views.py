from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import MessageSerializer
from .utils.chat_queries import get_user_messages, send_user_messages


class MessageList(APIView, PageNumberPagination):
    """
    An endpoint For messages .
    Includes pagination `page number pagination` .
    """

    permission_classes = (IsAuthenticated,)
    serializer_class = MessageSerializer

    def get(self, request):
        """
        GET method Show user messages with pagination
        """
        queryset = get_user_messages(request.user)
        result = self.paginate_queryset(queryset, request, view=self)
        serializer = self.serializer_class(result, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        """
        POST method sends user message .
        Get sender -> username, receiver -> username and message .
        `sender` is authenticated user and dont be change if get other username .
        """
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            send_user_messages(
                user=request.user,
                receiver=serializer.validated_data.get("receiver"),
                message=serializer.data.get("message"),
            )
            return Response(
                status=status.HTTP_200_OK,
                data={"message": "Message sent successfully"},
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
