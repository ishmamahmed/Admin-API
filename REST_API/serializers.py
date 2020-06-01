from rest_framework import serializers
from .models import SysAdmin

# Serialize the data in SysAdmin model.
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = SysAdmin
        fields = ('id', 'name', 'email', 'description')

