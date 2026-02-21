from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.pagination import PageNumberPagination

from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from .permissions import IsOwnerOrReadOnly

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

class StandardPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    pagination_class = StandardPagination
    filter_backends = [SearchFilter]
    search_fields = ['title', 'content']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by('-created_at')
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    pagination_class = StandardPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_feed(request):
    followed_users = request.user.following.all()
    posts = Post.objects.filter(author__in=followed_users).order_by('-created_at')
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)
  

# from rest_framework import generics, permissions
# from rest_framework.response import Response
# from .models import Post
# from .serializers import PostSerializer


# class FeedView(generics.GenericAPIView):
#     permission_classes = [permissions.IsAuthenticated]
#     serializer_class = PostSerializer

#     def get(self, request):
#         following_users = request.user.following.all()

#         posts = Post.objects.filter(
#             author__in=following_users
#         ).order_by('-created_at')

#         serializer = self.get_serializer(posts, many=True)
#         return Response(serializer.data)
