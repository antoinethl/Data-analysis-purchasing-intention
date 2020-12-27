from rest_framework import serializers
from .models import Shopping


class ShopperSerializer(serializers.Serializer):

    Administrative = serializers.IntegerField()
    Administrative_Duration = serializers.FloatField()
    Informational = serializers.IntegerField()
    Informational_Duration = serializers.FloatField()
    ProductRelated = serializers.IntegerField()
    ProductRelated_Duration = serializers.FloatField()
    BounceRates = serializers.FloatField()
    ExitRates = serializers.FloatField()
    PageValues = serializers.FloatField()
    SpecialDay = serializers.FloatField()
    Month = serializers.CharField()
    OperatingSystems = serializers.IntegerField()
    Browser = serializers.IntegerField()
    Region = serializers.IntegerField()
    TrafficType = serializers.IntegerField()
    VisitorType = serializers.CharField()
    Weekend = serializers.BooleanField()

    Revenue = serializers.BooleanField(allow_null=True)

    def create(self, validated_data):
        """Create and return a new `House` instance, given the validated data."""
        return Shopping.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """"Update and return an existing `House` instance, given the validated data."""
        instance.Administrative = validated_data.get('Administrative', instance.Administrative)
        instance.Administrative_Duration = validated_data.get('Administrative_Duration', instance.Administrative_Duration)
        instance.Informational = validated_data.get('Informational', instance.Informational)
        instance.Informational_Duration = validated_data.get('Informational_Duration', instance.Informational_Duration)
        instance.ProductRelated = validated_data.get('ProductRelated', instance.ProductRelated)
        instance.ProductRelated_Duration = validated_data.get('ProductRelated_Duration', instance.ProductRelated_Duration)
        instance.BounceRates = validated_data.get('BounceRates', instance.BounceRates)
        instance.ExitRates = validated_data.get('ExitRates', instance.ExitRates)
        instance.PageValues = validated_data.get('PageValues', instance.PageValues)
        instance.SpecialDay = validated_data.get('SpecialDay', instance.SpecialDay)
        instance.Month = validated_data.get('Month', instance.Month)
        instance.OperatingSystems = validated_data.get('OperatingSystems', instance.OperatingSystems)
        instance.Browser = validated_data.get('Browser', instance.Browser)
        instance.Region = validated_data.get('Region', instance.Region)
        instance.TrafficType = validated_data.get('TrafficType', instance.TrafficType)
        instance.VisitorType = validated_data.get('VisitorType', instance.VisitorType)
        instance.Weekend = validated_data.get('Weekend', instance.Weekend)

        # instance.Revenue = validated_data.get('Revenue', instance.Revenue)
        instance.save()

        return instance
