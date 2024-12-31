from rest_framework import serializers
from notes.models import Note


class NoteSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField(read_only=True)

    def get_author(self, obj):
        return str(obj.author.email)

    class Meta:
        model = Note
        fields = '__all__'


class ThinSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='notes-detail')

    class Meta:
        model = Note
        fields = ('id', 'title', 'url')

# class NoteSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     title = serializers.CharField(required=True, max_length=255)
#     text = serializers.CharField(required=False, max_length=255, allow_blank=True)
#
#     def create(self, validated_data):
#         return Note.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.title = validated_data.get('title', instance.title)
#         instance.text = validated_data.get('text', instance.text)
#         instance.save()
#         return instance
