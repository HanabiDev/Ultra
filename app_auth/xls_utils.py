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

sheets = []


def session_report(workbook, session):
	worksheet_s = workbook.add_worksheet("SES-"+session.date.strftime("%Y-%m-%d")+ "-ID"+str(session.id))
	sheets.append("SES-"+session.date.strftime("%Y-%m-%d")+ "-ID"+str(session.id))

	title_text = u"Reporte sesión " + session.date.strftime("%Y-%m-%d")
	worksheet_s.merge_range('B2:M2', title_text, title)
            

	for index, category in enumerate(session.sessionbeneficiarycategory_set.all()):
		index +=1

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

			worksheet_s.merge_range(37, g, 37, g+1, group.get_group_name_display(), header2)
			worksheet_s.write_string(38, g, "M", header3A)
			worksheet_s.write_string(38, g+1, "F", header3B)

			g = g + 2

		worksheet_s.merge_range(5*index, g, 5*index, g+1, "Total", header2)
		worksheet_s.merge_range(37, g, 37, g+1, "Total", header2)
		worksheet_s.write_string(5*index+1, g, "M", header3A)
		worksheet_s.write_string(5*index+1, g+1, "F", header3B)
		worksheet_s.write_string(38, g, "M", header3A)
		worksheet_s.write_string(38, g+1, "F", header3B)
		worksheet_s.write_number(5*index+2, g, cat_totals[0], cell_center)
		worksheet_s.write_number(5*index+2, g+1, cat_totals[1], cell_center)
		worksheet_s.merge_range(5*index+3, g, 5*index+3, g+1, sum(cat_totals), cell)

		for row in [5,10,15,20,25,30, 37, 38]:
			worksheet_s.set_row(row-1, 18)
			worksheet_s.set_row(row, 18)

		worksheet_s.merge_range('B37:M37', 'TOTAL', header)


		worksheet_s.write_formula('B40','=SUM(B8,B13,B18,B23,B28,B33)', cell_center)
		worksheet_s.write_formula('C40','=SUM(C8,C13,C18,C23,C28,C33)', cell_center)
		worksheet_s.write_formula('D40','=SUM(D8,D13,D18,D23,D28,D33)', cell_center)
		worksheet_s.write_formula('E40','=SUM(E8,E13,E18,E23,E28,E33)', cell_center)
		worksheet_s.write_formula('F40','=SUM(F8,F13,F18,F23,F28,F33)', cell_center)
		worksheet_s.write_formula('G40','=SUM(G8,G13,G18,G23,G28,G33)', cell_center)
		worksheet_s.write_formula('H40','=SUM(H8,H13,H18,H23,H28,H33)', cell_center)
		worksheet_s.write_formula('I40','=SUM(I8,I13,I18,I23,I28,I33)', cell_center)
		worksheet_s.write_formula('J40','=SUM(J8,J13,J18,J23,J28,J33)', cell_center)
		worksheet_s.write_formula('K40','=SUM(K8,K13,K18,K23,K28,K33)', cell_center)
		worksheet_s.write_formula('L40','=SUM(L8,L13,L18,L23,L28,L33)', cell_center)
		worksheet_s.write_formula('M40','=SUM(M8,M13,M18,M23,M28,M33)', cell_center)

		worksheet_s.merge_range('B41:C41','=SUM(B40,C40)', cell)
		worksheet_s.merge_range('D41:E41','=SUM(D40,E40)', cell)
		worksheet_s.merge_range('F41:G41','=SUM(F40,G40)', cell)
		worksheet_s.merge_range('H41:I41','=SUM(H40,I40)', cell)
		worksheet_s.merge_range('J41:K41','=SUM(J40,K40)', cell)
		worksheet_s.merge_range('L41:M41','=SUM(L40,M40)', cell)
		



		
def event_report(workbook, event):
	worksheet_s = workbook.add_worksheet("EVE-"+event.date.strftime("%Y-%m-%d")+ "-ID"+str(event.id))
	sheets.append("EVE-"+event.date.strftime("%Y-%m-%d")+ "-ID"+str(event.id))

	title_text = u"Reporte evento " + event.date.strftime("%Y-%m-%d")
	worksheet_s.merge_range('B2:M2', title_text, title)
            

	for index, category in enumerate(event.eventbeneficiarycategory_set.all()):
		index +=1

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

			worksheet_s.merge_range(37, g, 37, g+1, group.get_group_name_display(), header2)
			worksheet_s.write_string(38, g, "M", header3A)
			worksheet_s.write_string(38, g+1, "F", header3B)

			g = g + 2

		worksheet_s.merge_range(5*index, g, 5*index, g+1, "Total", header2)
		worksheet_s.merge_range(37, g, 37, g+1, "Total", header2)
		worksheet_s.write_string(5*index+1, g, "M", header3A)
		worksheet_s.write_string(5*index+1, g+1, "F", header3B)
		worksheet_s.write_string(38, g, "M", header3A)
		worksheet_s.write_string(38, g+1, "F", header3B)
		worksheet_s.write_number(5*index+2, g, cat_totals[0], cell_center)
		worksheet_s.write_number(5*index+2, g+1, cat_totals[1], cell_center)
		worksheet_s.merge_range(5*index+3, g, 5*index+3, g+1, sum(cat_totals), cell)

		for row in [5,10,15,20,25,30, 37, 38]:
			worksheet_s.set_row(row-1, 18)
			worksheet_s.set_row(row, 18)

		worksheet_s.merge_range('B37:M37', 'TOTAL', header)


		worksheet_s.write_formula('B40','=SUM(B8,B13,B18,B23,B28,B33)', cell_center)
		worksheet_s.write_formula('C40','=SUM(C8,C13,C18,C23,C28,C33)', cell_center)
		worksheet_s.write_formula('D40','=SUM(D8,D13,D18,D23,D28,D33)', cell_center)
		worksheet_s.write_formula('E40','=SUM(E8,E13,E18,E23,E28,E33)', cell_center)
		worksheet_s.write_formula('F40','=SUM(F8,F13,F18,F23,F28,F33)', cell_center)
		worksheet_s.write_formula('G40','=SUM(G8,G13,G18,G23,G28,G33)', cell_center)
		worksheet_s.write_formula('H40','=SUM(H8,H13,H18,H23,H28,H33)', cell_center)
		worksheet_s.write_formula('I40','=SUM(I8,I13,I18,I23,I28,I33)', cell_center)
		worksheet_s.write_formula('J40','=SUM(J8,J13,J18,J23,J28,J33)', cell_center)
		worksheet_s.write_formula('K40','=SUM(K8,K13,K18,K23,K28,K33)', cell_center)
		worksheet_s.write_formula('L40','=SUM(L8,L13,L18,L23,L28,L33)', cell_center)
		worksheet_s.write_formula('M40','=SUM(M8,M13,M18,M23,M28,M33)', cell_center)

		worksheet_s.merge_range('B41:C41','=SUM(B40,C40)', cell)
		worksheet_s.merge_range('D41:E41','=SUM(D40,E40)', cell)
		worksheet_s.merge_range('F41:G41','=SUM(F40,G40)', cell)
		worksheet_s.merge_range('H41:I41','=SUM(H40,I40)', cell)
		worksheet_s.merge_range('J41:K41','=SUM(J40,K40)', cell)
		worksheet_s.merge_range('L41:M41','=SUM(L40,M40)', cell)
	   
def total_report(event):
	worksheet_s = workbook.add_worksheet("Reporte total")

	title_text = u"Reporte total de beneficiarios del mes"
	worksheet_s.merge_range('B2:M2', title_text, title)

	

	for let in ['B','C','D','E','F','G','H','I','J','K','L','M']:
		sn = ""
		for s in sheets:
			sn += "'"+s+"'!"+let+"40,"
		sn = sn[0:-1]
		print sn
		worksheet_s.write_formula(let+'6','=SUM('+sn+')', cell_center)
	
	worksheet_s.merge_range('B4:C4','Mestizos', header2)
	worksheet_s.merge_range('D4:E4','Campesinos', header2)
	worksheet_s.merge_range('F4:G4',u'Indígenas', header2)
	worksheet_s.merge_range('H4:I4','Pers. con discapacidad', header2)
	worksheet_s.merge_range('J4:K4','Afrodescendientes', header2)
	worksheet_s.merge_range('L4:M4','Total', header2)

	worksheet_s.write_string('B5', 'M', header3A)
	worksheet_s.write_string('C5', 'F', header3B)
	worksheet_s.write_string('D5', 'M', header3A)
	worksheet_s.write_string('E5', 'F', header3B)
	worksheet_s.write_string('F5', 'M', header3A)
	worksheet_s.write_string('G5', 'F', header3B)
	worksheet_s.write_string('H5', 'M', header3A)
	worksheet_s.write_string('I5', 'F', header3B)
	worksheet_s.write_string('J5', 'M', header3A)
	worksheet_s.write_string('K5', 'F', header3B)
	worksheet_s.write_string('L5', 'M', header3A)
	worksheet_s.write_string('M5', 'F', header3B)

	worksheet_s.merge_range('B7:C7','=SUM(B6,C6)', cell)
	worksheet_s.merge_range('D7:E7','=SUM(D6,E6)', cell)
	worksheet_s.merge_range('F7:G7','=SUM(F6,G6)', cell)
	worksheet_s.merge_range('H7:I7','=SUM(H6,I6)', cell)
	worksheet_s.merge_range('J7:K7','=SUM(J6,K6)', cell)
	worksheet_s.merge_range('L7:M7','=SUM(L6,M6)', cell)


def WriteToExcel(sessions, events):

	for session in sessions:
		session_report(workbook, session)


	for event in events:
		event_report(workbook, event)

	total_report(events[0])
    

	workbook.close()
	xlsx_data = output.getvalue()
	# xlsx_data contains the Excel file
	return xlsx_data