from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
import random
from rest_framework.permissions import IsAuthenticated

from transaction.api.serializers import AccountDetailSerializer



def randomNum():
    return int(random.uniform(1000000000, 9999999999))

@api_view(['POST',])
@permission_classes((IsAuthenticated, ))
def account_detail_view(request):
    user = request.user
    if user.is_authenticated:
        serializer = AccountDetailSerializer(data=request.data)
        if request.method == "POST":
            if serializer.is_valid():
                serializer.account_number = randomNum()
                serializer.account_type = 'savings'
                serializer.balance = 0
                serializer.user_name = request.user
                serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)

        

