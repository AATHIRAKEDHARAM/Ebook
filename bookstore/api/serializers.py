from rest_framework import serializers

from api.models import Register


class RegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model=Register
        fields=["name","phonenumber","username","password"]
        extra_kwargs= {'password':{'write_only':True}}

   
    def validate(self, attrs):
        queryset = Register.objects.filter(username=attrs['username'])
        
        if queryset:
            raise serializers.ValidationError({
                "message":"Username already exists."
            })
        return attrs
