#encoding: utf-8

from __future__ import unicode_literals

from django.db import models

# Create your models here.

from reportlab.graphics.shapes import Drawing
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY
from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.units import mm
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle

from reportlab.pdfgen import canvas

from django.conf import settings



class ReportModel:

	# initialize class
	def __init__(self, buffer):
		self.buffer = buffer
		self.pageSize = letter
		self.width, self.height = self.pageSize
		self.canvas = canvas.Canvas(self.buffer)

	def pageNumber(self, canvas, doc):
		number = canvas.getPageNumber()
		canvas.drawCentredString(100*mm, 15*mm, str(number))


	def draw_header(self, title, subtitle, date):

		ultra_logo = settings.BASE_DIR+'/Ultra/static/assets/img/logo.jpg'
		company_logo = settings.BASE_DIR+'/Ultra/static/assets/img/company.jpg'

		self.canvas.drawImage(ultra_logo, 157*mm, 750, 120, 90,preserveAspectRatio=True)
		self.canvas.drawImage(company_logo, 10*mm, 750, 120, 90,preserveAspectRatio=True)


		self.canvas.setFont("Helvetica", 12)
		self.canvas.drawString(230, 790, u"INDEPORTES BOYACÁ")
		self.canvas.setFont("Helvetica", 12)
		self.canvas.drawString(230, 770, u"Sistema de Gestión deportiva Ultra")
		self.canvas.setFont("Helvetica", 14)
		self.canvas.drawString(200, 770, u"REPORTE DE PERSONAS")

	def get_report(self):

		self.draw_header("a", "b", "day")
		self.canvas.showPage()
		self.canvas.save()
		pdf = self.buffer.getvalue()
		self.buffer.close()
		return pdf




