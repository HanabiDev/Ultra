#encoding: utf-8
from django.conf import settings
from reportlab.lib.pagesizes import letter, cm
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import BaseDocTemplate, Frame, PageTemplate, Paragraph

from reportlab.graphics.shapes  import Line
from functools import partial 

from reportlab.lib.enums import TA_JUSTIFY, TA_CENTER


from reportlab.graphics.shapes import Drawing

from reports.plot_types import BreakdownPieDrawing

styles = getSampleStyleSheet()
styleN = styles['Normal']


styleH = ParagraphStyle(
        'title',
        fontName='Helvetica-Bold',
        fontSize=12,
        leading=42,
        alignment=TA_CENTER,
    )

styleH2 = ParagraphStyle(
    'title',
    fontName='Helvetica-Bold',
    fontSize=10,
    leading=42,
    alignment=TA_CENTER,
)

styleH2E = ParagraphStyle(
    'title',
    fontName='Helvetica-Bold',
    fontSize=10,
    leading=12,
    alignment=TA_CENTER,
)


styleN.alignment = TA_JUSTIFY
styleH.alignment = TA_CENTER


def drawPie(canvas, doc,  data, categories, type):
    if type==2:
        #d = BreakdownPieDrawing2(8 * cm, 8 * cm, doc.leftMargin + 2 * cm, doc.bottomMargin+2*cm)
        #d.drawOn(canvas, 0, 0)
        pass
    else:
        d = BreakdownPieDrawing(8*cm, 8*cm, doc.leftMargin+2*cm, doc.height-10*cm)
        d.drawOn(canvas, 0, 0)



def header(canvas, doc, content):
    canvas.saveState()

    ultra_logo = settings.BASE_DIR + '/reports/logo.jpg'
    company_logo = settings.BASE_DIR + '/reports/company.jpg'

    canvas.drawImage(company_logo, doc.leftMargin, doc.height+1*cm, 4.128*cm, 1.199*cm,preserveAspectRatio=True)
    canvas.drawImage(ultra_logo, doc.width+doc.rightMargin-3.275*cm, doc.height+1.2*cm,  3.275*cm, 0.800*cm,preserveAspectRatio=True)

    main_title = Paragraph("INDEPORTES BOYACÁ ", styleH)
    main_title.wrapOn(canvas, doc.width-8.5*cm, 1*cm)
    main_title.drawOn(canvas, 6*cm, doc.height+doc.topMargin - 1.8*cm)

    main_title = Paragraph("SISTEMA ULTRA", styleH)
    main_title.wrapOn(canvas, doc.width - 8.5 * cm, 1 * cm)
    main_title.drawOn(canvas, 6 * cm, doc.height + doc.topMargin - 2.4 * cm)

    content.wrapOn(canvas, doc.width - 8.5 * cm, 1 * cm)
    content.drawOn(canvas, 6*cm, doc.height + doc.topMargin - 3*cm)

    d = Drawing(doc.width, 0)
    line = Line(0, 0, doc.width, 0)
    line.strokeWidth = 3
    d.add(line)
    d.wrapOn(canvas, doc.width, 1 * cm)
    d.drawOn(canvas, 1.5*cm, doc.height + doc.topMargin - 2.4 * cm)

    d = Drawing(doc.width, 0)
    line = Line(0, 0, doc.width, 0)
    line.strokeWidth = 1
    d.add(line)
    d.wrapOn(canvas, doc.width, 1 * cm)
    d.drawOn(canvas, 1.5*cm, doc.height + doc.topMargin - 2.6 * cm)


    drawPie(canvas, doc, None, None, 2)


    canvas.restoreState()


doc = BaseDocTemplate('test.pdf', topMargin=2.5*cm, 
                                  leftMargin=1.5*cm,
                                  rightMargin=1.5*cm,
                                  bottomMargin=1.5*cm, 
                                  pagesize=letter)


frame = Frame(1.5*cm,doc.bottomMargin,doc.width,doc.height-doc.bottomMargin, topPadding=0.5*cm) #Frame(1.5*cm, 2*cm, doc.width, doc.height-2*cm, id='normal', showboundary)


header_content = Paragraph("REPORTE DE DEPORTISTAS POR LIGA", styleH2)
template = PageTemplate(id='test', frames=frame, onPage=partial(header, content=header_content))
doc.addPageTemplates([template])

text = []
for i in range(111):
    text.append(Paragraph("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis dapibus, sapien vel egestas interdum, ex mauris consequat sem, in suscipit orci mauris sed leo. Nunc nec ante vitae eros vehicula sodales ac eu felis. Proin elementum elit eget augue porta, ac scelerisque nibh aliquam. Etiam laoreet ultricies dui, vitae facilisis arcu maximus vel. Nam turpis urna, consequat at purus id, ultricies interdum sapien. Integer quis dui eget urna suscipit vehicula sed nec ipsum. Nullam venenatis feugiat velit vitae aliquam. Ut risus libero, commodo id leo sed, dictum fringilla elit. Phasellus volutpat, leo eget convallis vestibulum, magna dui luctus quam, vitae aliquam velit magna eu ante.", styleN))

doc.build(text)
