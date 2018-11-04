from .models import *
import django_filters
from django_filters import rest_framework as filters



class ProductFilter(filters.FilterSet):
    product_name = django_filters.CharFilter(lookup_expr='contains')
    class Meta:
        model = Product
        fields = ['catid','product_name']

###################################################################
class ImgFilter(filters.FilterSet):
    class Meta:
        model = Images
        fields = ['product_image']
###################################################################

class QmFilter(filters.FilterSet):
    class Meta:
        model = RatingAPi
        fields = ['quality_rate','price_rate','product_qm','total']


###################################################################

class CommentFilter(filters.FilterSet):
    class Meta:
        model = ProductComment
        fields = ['usercm_id','productcm_id']
###################################################################

filters.LOOKUP_TYPES = [
    ('', '---------'),
    ('exact', 'Is equal to'),
    ('not_exact', 'Is not equal to'),
    ('lt', 'Lesser than'),
    ('gt', 'Greater than'),
    ('gte', 'Greater than or equal to'),
    ('lte', 'Lesser than or equal to'),
    ('startswith', 'Starts with'),
    ('endswith', 'Ends with'),
    ('contains', 'Contains'),
    ('not_contains', 'Does not contain'),
]
