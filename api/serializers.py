from rest_framework import serializers
from rest_framework.reverse import reverse
from django.conf import settings

from .models import Attraction

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attraction
        fields = ('image_url')

class AttractionSerializer(serializers.ModelSerializer):
    attr_types = serializers.StringRelatedField(many=True)
    location = serializers.StringRelatedField(many=False)
    image_url = serializers.SerializerMethodField()
    current_point = serializers.SerializerMethodField()

    def get_image_url(self, obj): #именно такое название функции должно быть, с get_ + имя поля
        if obj.image_url:
            return settings.PATH_TO_IMAGES + obj.image_url.url

#это просто тестовая приколюха для получения пути к текущей точки. она нам не нужна, можно будет удалить, просто эксперимент
    def get_current_point(self, obj):
        url = reverse('api:attractions')
        return url

    #image_url = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='attractions')

    class Meta:
        model = Attraction
        fields = '__all__'
        '''
        fields = (
            'id',
            'title',
            'image_url',
            'short_description',
            'description',
            'attr_types',
            'work_time',
            'age',
            'height',
            'location',
            'with_adults',
            'is_purchased_separately',
            'specs',
            'is_active',
            'is_working',
            'sorting',
            'wait_time'
                )'''

