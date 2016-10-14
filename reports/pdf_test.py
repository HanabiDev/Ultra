#encoding: utf-8

from reportlab.lib.pagesizes import letter, cm
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import BaseDocTemplate, Frame, PageTemplate, Paragraph
from functools import partial 

from reportlab.lib.enums import TA_JUSTIFY, TA_CENTER

styles = getSampleStyleSheet()
styleN = styles['Normal']
styleH = styles['Heading1']


styleN.alignment = TA_JUSTIFY
styleH.alignment = TA_CENTER


def header(canvas, doc, content):
    canvas.saveState()

    canvas.drawImage('company.jpg', doc.leftMargin, doc.height+1*cm, 5.009*cm, 1.482*cm,preserveAspectRatio=True)
    canvas.drawImage('logo.jpg', doc.width+doc.rightMargin-4.516*cm, doc.height+1*cm, 4.516*cm, 1.305*cm,preserveAspectRatio=True)

    content.drawOn(canvas, 6*cm, doc.height + doc.topMargin - 1*cm)
    canvas.restoreState()





doc = BaseDocTemplate('test.pdf', topMargin=2.5*cm, 
                                  leftMargin=1.5*cm,
                                  rightMargin=1.5*cm,
                                  bottomMargin=1.5*cm, 
                                  pagesize=letter)

                                  


frame = Frame(1.5*cm,0,doc.width,doc.height, showBoundary=1) #Frame(1.5*cm, 2*cm, doc.width, doc.height-2*cm, id='normal', showboundary)




header_content = Paragraph("INDEPORTES BOYACÁSISTEMA ULTRA\nCLASIFICACIÓN DE DEPORTISTAS POR DISCIPLINA" * 1, styleH)
template = PageTemplate(id='test', frames=frame, onPage=partial(header, content=header_content))
doc.addPageTemplates([template])

text = []
for i in range(111):
    text.append(Paragraph("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis dapibus, sapien vel egestas interdum, ex mauris consequat sem, in suscipit orci mauris sed leo. Nunc nec ante vitae eros vehicula sodales ac eu felis. Proin elementum elit eget augue porta, ac scelerisque nibh aliquam. Etiam laoreet ultricies dui, vitae facilisis arcu maximus vel. Nam turpis urna, consequat at purus id, ultricies interdum sapien. Integer quis dui eget urna suscipit vehicula sed nec ipsum. Nullam venenatis feugiat velit vitae aliquam. Ut risus libero, commodo id leo sed, dictum fringilla elit. Phasellus volutpat, leo eget convallis vestibulum, magna dui luctus quam, vitae aliquam velit magna eu ante.", styleN))
doc.build(text)
