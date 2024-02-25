from rest_framework import serializers
from.models import User

class Userserializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','password']
        extra_kwargs = {
            'password':{
                'write_only':True
            }
        }

    def create(self,valid_data):
        password = valid_data.pop('password',None)
        instance = self.Meta.model(**valid_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance
