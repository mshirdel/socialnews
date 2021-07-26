from rest_framework import serializers
from accounts.serializers import UserSerializer
from .models import Story


class StorySerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Story
        fields = [
            "id",
            "title",
            "slug",
            "story_url",
            "story_body_text",
            "number_of_comments",
            "number_of_votes",
            "url_domain_name",
            "rank",
            "user",
        ]
        read_only_fields = [
            "number_of_comments",
            "number_of_votes",
            "url_domain_name",
            "rank",
            "slug",
        ]

    def validate(self, data):
        story_url = data.get("story_url", None)
        story_body_text = data.get("story_body_text", None)
        if story_url is None and story_body_text is None:
            raise serializers.ValidationError(
                "One of story_url or story_body_text is required."
            )
        return data

    def create(self, validated_data):
        user = self.context.get("user")
        story = Story.objects.create(user=user, **validated_data)
        return story
