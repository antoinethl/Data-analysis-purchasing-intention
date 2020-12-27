from django.db import models


class Shopping(models.Model):

    Administrative = models.IntegerField()
    Administrative_Duration = models.FloatField()
    Informational = models.IntegerField()
    Informational_Duration = models.FloatField()
    ProductRelated = models.IntegerField()
    ProductRelated_Duration = models.FloatField()
    BounceRates = models.FloatField()
    ExitRates = models.FloatField()
    PageValues = models.FloatField()
    SpecialDay = models.FloatField()
    Month = models.TextField()
    OperatingSystems = models.IntegerField()
    Browser = models.IntegerField()
    Region = models.IntegerField()
    TrafficType = models.IntegerField()
    VisitorType = models.TextField()
    Weekend = models.BooleanField()
    Revenue = models.BooleanField(null=True)

    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']

