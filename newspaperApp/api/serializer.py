from rest_framework import serializers
from .models import Users,Authors,Articles,Comments

#usersSerializer
class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields='__all__'

# AuthorSerializer
class AuthorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Authors
        fields='__all__'
    
# ArticleSerializer
class ArticalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Articles
        fields='__all__'

#CommentsSerializer
class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields='__all__'