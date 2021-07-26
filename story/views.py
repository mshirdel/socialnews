from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from .serializers import StorySerializer
from .models import Story


class CreateStoryView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = StorySerializer
    queryset = Story.stories.select_related("user")

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={"user":request.user})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class RetrieveUpdateDestroyStoryView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = StorySerializer
    queryset = Story.stories.select_related("user")