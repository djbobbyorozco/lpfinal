from .models import Organization
import django_filters

class OrganizationFilter(django_filters.FilterSet):
	class Meta:
		model = Organization
		fields = ['orgName', 'orgCode', 'description']