from rest_framework import serializers
from products_app.models import productcls

class productSerializer(serializers.ModelSerializer):
    class Meta:
        model = productcls
        fields = '__all__'
        