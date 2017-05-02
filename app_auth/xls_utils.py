#encoding: utf-8

import StringIO
import xlsxwriter
from django.utils.translation import ugettext

output = StringIO.StringIO()
workbook = xlsxwriter.Workbook(output)

title = workbook.add_format({
    'bold': True,
    'font_size': 14,
    'align': 'center',
    'valign': 'vcenter'
})
header = workbook.add_format({
    'bg_color': '#27ae60',
    'color': 'white',
    'align': 'center',
    'valign': 'vcenter',
    'border': 0
})

header2 = workbook.add_format({
    'bg_color': '#2ecc71',
    'color': 'white',
    'align': 'center',
    'valign': 'vcenter',
    'border': 0
})

header3A = workbook.add_format({
    'bg_color': '#3498db',
    'color': 'white',
    'align': 'center',
    'valign': 'vcenter',
    'border': 0
})
header3B = workbook.add_format({
    'bg_color': '#9b59b6',
    'color': 'white',
    'align': 'center',
    'valign': 'vcenter',
    'border': 0
})


cell = workbook.add_format({
    'bg_color': '#34495e',
    'color': 'white',
    'align': 'center',
    'valign': 'vcenter',
    'border': 0
})

cell_center = workbook.add_format({
    'bg_color': '#ecf0f1',
    'color': 'black',
    'align': 'center',
    'valign': 'vcenter',
    'border': 0
})


def session_report(workbook, session):
	worksheet_s = workbook.add_worksheet(session.date.strftime("%Y-%m-%d")+ " ID"+str(session.id))

	title_text = u"Reporte sesión " + session.date.strftime("%Y-%m-%d")
	worksheet_s.merge_range('B2:BI2', title_text, title)
            

	for index, category in enumerate(session.sessionbeneficiarycategory_set.all()):
		index = 1 if index==0 else index
		worksheet_s.merge_range('B'+str(5*index)+':M'+str(5*index), category.get_age_range_display(), header)


		g = 1
		cat_totals = [0,0]
		for i, group in enumerate(category.beneficiarygroup_set.all()):
			worksheet_s.merge_range(5*index, g, 5*index, g+1, group.get_group_name_display(), header2)
			cat_totals[0]+=group.masculine_individuals
			cat_totals[1]+=group.femenine_individuals
			group_total = group.masculine_individuals + group.femenine_individuals

			worksheet_s.write_string(5*index+1, g, "M", header3A)
			worksheet_s.write_string(5*index+1, g+1, "F", header3B)

			worksheet_s.write_number(5*index+2, g, group.masculine_individuals, cell_center)
			worksheet_s.write_number(5*index+2, g+1, group.femenine_individuals, cell_center)

			worksheet_s.merge_range(5*index+3, g, 5*index+3, g+1, group_total, cell)

			g = g + 2

		worksheet_s.merge_range(5*index, g, 5*index, g+1, "Total", header2)
		worksheet_s.write_string(5*index+1, g, "M", header3A)
		worksheet_s.write_string(5*index+1, g+1, "F", header3B)
		worksheet_s.write_number(5*index+2, g, cat_totals[0], cell_center)
		worksheet_s.write_number(5*index+2, g+1, cat_totals[1], cell_center)
		worksheet_s.merge_range(5*index+3, g, 5*index+3, g+1, sum(cat_totals), cell)

		for row in [5,10,15,20,25,30]:
			worksheet_s.set_row(row-1, 18)
			worksheet_s.set_row(row, 18)

		

	   


def WriteToExcel(sessions):

	for session in sessions:
		session_report(workbook, session)
    
    
	"""
    partners = []   

    for idx, partner in enumerate(partners):
        row = 5 + idx
        worksheet_s.write_number(row, 0, idx + 1, cell_center)
        worksheet_s.write_string(row, 1, str(partner.doc_id), cell)
        worksheet_s.write_string(row, 2, partner.get_full_name(), cell)
        worksheet_s.write(row, 3, partner.club.name, cell_center)
        # the rest of the data

	"""

	workbook.close()
	xlsx_data = output.getvalue()
	# xlsx_data contains the Excel file
	return xlsx_data