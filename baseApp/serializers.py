# this file takes in the data from the created model and converts it into JSON
# so that the API can understand what is happening

from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import Developers, Company

class CompanySerializers(ModelSerializer):
    employee_count = SerializerMethodField(read_only=True)
    class Meta:
        model = Company
        fields = '__all__'

    def get_employee_count(self, obj):
        count = obj.developers_set.count()
        return count

class DevelopersSerializers(ModelSerializer):
    company = CompanySerializers()
    class Meta:
        model = Developers
        # fields = '__all__'
        fields = ['username', 'bio', 'company']
