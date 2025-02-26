import django_filters
from .models import*
from django_filters import CharFilter

class PostFilter(django_filters.FilterSet):
    title = CharFilter(field_name='title', lookup_expr='icontains',label='title')
    class Meta:
        model = Post
        fields = "__all__"
        exclude = ['image', 'body', 'created', 'title', 'updated']
        
        
class SchoolFilter(django_filters.FilterSet):
    class Meta:
        model= School_Profile
        fields = ['locality', ]    

class DebtorFilter(django_filters.FilterSet):
    student_name = CharFilter(field_name='student_name', lookup_expr='icontains', label='Student')
    class Meta:
        model = Debtor
        fields = [ ]