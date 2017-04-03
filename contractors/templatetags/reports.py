from django import template
from django.core import urlresolvers

register = template.Library()

@register.simple_tag
def val_sum(value, value2):
    return value+value2

@register.filter
def list_sum(t_list):
    return sum(t_list)

@register.filter
def gender_total(groups):

	men = 0
	women = 0

	for group in groups:
		men += group.masculine_individuals
		women += group.femenine_individuals

	return [men,women]
gender_total.is_safe = True

@register.filter
def group_gender_total(categories):
	

	G1 = 0
	G2 = 0
	G3 = 0
	G4 = 0
	G5 = 0
	G1f = 0
	G2f = 0
	G3f = 0
	G4f = 0
	G5f = 0

	data = [[0,0,0,0,0],[0,0,0,0,0]]

	for cat in categories:
		G1 += cat.beneficiarygroup_set.get(group_name='M').masculine_individuals
		G1f += cat.beneficiarygroup_set.get(group_name='M').femenine_individuals

		G2 += cat.beneficiarygroup_set.get(group_name='C').masculine_individuals
		G2f += cat.beneficiarygroup_set.get(group_name='C').femenine_individuals

		G3 += cat.beneficiarygroup_set.get(group_name='I').masculine_individuals
		G3f += cat.beneficiarygroup_set.get(group_name='I').femenine_individuals

		G4 += cat.beneficiarygroup_set.get(group_name='D').masculine_individuals
		G4f += cat.beneficiarygroup_set.get(group_name='D').femenine_individuals

		G5 += cat.beneficiarygroup_set.get(group_name='A').masculine_individuals
		G5f += cat.beneficiarygroup_set.get(group_name='A').femenine_individuals

	data = [
		[G1,G2,G3,G4,G5],
		[G1f, G2f, G3f, G4f, G5f],
	]

	return data
