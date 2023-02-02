from rest_framework import serializers

from users.models import User
from users.utils import send_whatsapp_message


class UserSerializer(serializers.ModelSerializer):
    phone = serializers.CharField(max_length=50, required=True, allow_blank=False)

    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):
        email = validated_data.get('email')
        if User.objects.filter(email__iexact=email).exists():
            raise serializers.ValidationError('user with this email address already exists.')

        create_user = User(**validated_data)
        create_user.set_password(validated_data['password'])
        create_user.save()

        return create_user

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            if attr == 'password':
                instance.set_password(value)
            else:
                setattr(instance, attr, value)
        instance.save()
        return instance


