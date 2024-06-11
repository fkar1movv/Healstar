from rest_framework import serializers

from core.models import Department, Hospital, HospitalDepartment, HospitalBranch


class DepartmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Department
        fields = '__all__'


class HospitalDepartments(serializers.ModelSerializer):

    class Meta:
        model = HospitalDepartment
        exclude = ('hospital',)

    def to_representation(self, instance):

        department = DepartmentSerializer(instance.department).data

        return department


class HospitalBranches(serializers.ModelSerializer):

    class Meta:
        model = HospitalBranch
        exclude = ('hospital',)


class HospitalSerializer(serializers.ModelSerializer):
    departments = HospitalDepartments(many=True)
    branches = HospitalBranches(many=True)

    class Meta:
        model = Hospital
        fields = '__all__'
