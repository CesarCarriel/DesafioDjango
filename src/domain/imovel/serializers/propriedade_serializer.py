from rest_framework import serializers
from domain.imovel.models import Propriedade


class PropriedadeSerializer(serializers.HyperlinkedModelSerializer):
    distance = serializers.SerializerMethodField()

    class Meta:
        model = Propriedade
        fields = ['nome', 'valor', 'distance']

    def get_distance(self, obj):
        if hasattr(obj, 'distance'):
            if hasattr(obj.distance, 'm'):
                if obj.distance.m < 1000:
                    return "{0:.0f} m".format(obj.distance.m)
                else:
                    return "{0:.0f} km".format(obj.distance.km)
        return None
