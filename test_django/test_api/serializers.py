from rest_framework import serializers
from .models import Polls, Answer, UserAnswer


class AnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Answer
        fields = ('text',)


class PollsSerializer(serializers.ModelSerializer):
    answer_text = AnswerSerializer(required=True)
    class Meta:
        model = Polls
        fields = '__all__'

    def create(self, validated_data):
        answer_instance = Answer.objects.create(text=validated_data['answer_text']['text'])
        validated_data['answer_text'] = answer_instance
        instance = Polls.objects.create(**validated_data)
        return instance

    def update(self, instance, validated_data):
        answer_instance = Answer.objects.filter(text=validated_data['answer_text']['text'])
        if answer_instance:
            instance.answer_text = answer_instance[0]
        else:
            answer_instance = Answer.objects.create(text=validated_data['answer_text']['text'])
            instance.answer_text = answer_instance
        instance.name = validated_data['name']
        instance.finish_date = validated_data['finish_date']
        instance.definition = validated_data['definition']
        instance.save()
        return instance

    def to_representation(self, instance):
        representation = super(PollsSerializer, self).to_representation(instance)
        representation['answer_text'] = AnswerSerializer(instance.answer_text).data
        return representation


class UserAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAnswer
        fields = '__all__'

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        # Access self.context here to add contextual data into ret
        #ret['user_id'] = self.context['user_id']
        return ret