from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, permissions
from django.shortcuts import get_object_or_404
from .models import CustomUser


@api_view(['POST'])
@permissions.permission_classes([permissions.IsAuthenticated])
def followuser(request, user_id):
    users = CustomUser.objects.all()
    user_to_follow = get_object_or_404(users, id=user_id)

    if user_to_follow == request.user:
        return Response(
            {"detail": "You cannot follow yourself."},
            status=status.HTTP_400_BAD_REQUEST
        )

    request.user.following.add(user_to_follow)
    return Response(
        {"detail": f"You are now following {user_to_follow.username}"},
        status=status.HTTP_200_OK
    )


@api_view(['POST'])
@permissions.permission_classes([permissions.IsAuthenticated])
def unfollowuser(request, user_id):
    users = CustomUser.objects.all()
    user_to_unfollow = get_object_or_404(users, id=user_id)

    request.user.following.remove(user_to_unfollow)
    return Response(
        {"detail": f"You have unfollowed {user_to_unfollow.username}"},
        status=status.HTTP_200_OK
    )
