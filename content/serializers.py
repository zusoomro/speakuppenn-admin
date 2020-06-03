from rest_framework import serializers
from .models import Match, Contribute


class MatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Match
        fields = '__all__'


class ContributeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contribute
        fields = '__all__'
