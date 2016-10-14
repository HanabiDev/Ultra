from django.http import HttpResponse
from datetime import date
from io import BytesIO


from reports.models import ReportModel

# Create your views here.


def render_report(request):
	response = HttpResponse(content_type='application/pdf')
	today = date.today()
	filename = 'pdf_demo' + today.strftime('%Y-%m-%d')
	#response['Content-Disposition'] = 'attachement; filename={0}.pdf'.format(filename)
	buffer = BytesIO()
	report = ReportModel(buffer)
	pdf = report.get_report()
	response.write(pdf)
	return response