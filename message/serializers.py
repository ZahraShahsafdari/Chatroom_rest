from rest_framework import serializers
from message.models import Conversations, Messages
from users.serializers import UserSerializer

class ConversationSerializer(serializers.ModelSerializer):
    members = UserSerializer(many = True)
    class Meta:
        model = Conversations
        fields = '__all__'



class RequestGetMessageSerializer(serializers.Serializer):
    conversation = serializers.IntegerField()


class MessageSerializer(serializers.ModelSerializer):

    sender = UserSerializer()
    class Meta:
        model = Messages
        fields = '__all__'


class AddMessageSerializer(serializers.Serializer):
    conversation = serializers.IntegerField()
    text = serializers.CharField(
        max_length = 100,
        allow_blank = False)

    def validate_text(self, data):
        if 'benzin' in data:
            return '*****'
        elif 'tazahorat' in data:
            raise serializers.ValidationError('Your request contains bad words!')
        return data


    def validate(self, data):
        if data['conversation'] != 5 and 'enghelab' in data['text']:
                raise serializers.ValidationError('Just 5')
        return data


    def create(self, validated_data):
        print('validated_data:', validated_data)
        print(self.context)
        c = Conversation.objects.get(
            id = validated_data['conversation'])
        m = Messages(
            text = validated_data['text'],
            sender = self.context['user'],
            conversation = c
        )
        m.save()
        return m