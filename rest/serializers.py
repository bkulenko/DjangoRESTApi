from rest_framework import serializers
from rest.models import Movie, Comment


class MovieSerializer(serializers.ModelSerializer):
    Ratings = serializers.JSONField()
    Released = serializers.DateField(input_formats=["%d %b %Y"])

    class Meta:
        model = Movie
        fields = '__all__'

    def create(self, validated_data):
        return Movie.objects.create(**validated_data)


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

    def create(self, validated_data):
        return Comment.objects.create(**validated_data)
