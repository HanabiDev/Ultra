from reportlab.graphics.shapes import _DrawingEditorMixin, Drawing
from reportlab.lib.colors import white, HexColor
from reportlab.graphics.charts.legends import Legend
from reportlab.lib.pagesizes import cm
from reportlab.graphics.charts.piecharts import Pie

pdf_chart_colors = [
    HexColor("#1abc9c"),
    HexColor("#f1c40f"),
    HexColor("#e74c3c"),
    HexColor("#8e44ad"),
    HexColor("#2c3e50"),
    HexColor("#3498db")
]

def setItems(n, obj, attr, values):
    m = len(values)
    i = m // n
    for j in xrange(n):
        setattr(obj[j],attr,values[j*i % m])

class BreakdownPieDrawing(_DrawingEditorMixin,Drawing):
    def __init__(self,width=400,height=200, x=0, y=0, data=[0,0,0], labels=['None', 'none', 'none'], *args,**kw):
        apply(Drawing.__init__,(self,width,height)+args,kw)
        # adding a pie chart to the drawing


        self._add(self,Pie(),name='pie',validate=None,desc=None)
        self.pie.width                  = width
        self.pie.height                 = height
        self.pie.x                      = x
        self.pie.y                      = y
        self.pie.data = data
        self.pie.labels = labels
        self.pie.simpleLabels           = 1

        self.pie.slices.label_visible   = 0
        self.pie.slices.popout = 2
        self.pie.slices.fontColor       = None
        self.pie.slices.strokeColor     = white
        self.pie.slices.strokeWidth     = 1

        # adding legend
        self._add(self,Legend(),name='legend',validate=None,desc=None)
        self.legend.x               = self.pie.x+self.pie.width+2*cm
        self.legend.y               = self.pie.y+self.pie.height-3*cm
        self.legend.dx              = 8
        self.legend.dy              = 8
        self.legend.fontName        = 'Helvetica'
        self.legend.fontSize        = 10
        self.legend.boxAnchor       = 'w'
        self.legend.columnMaximum   = 10
        self.legend.strokeWidth     = 1
        self.legend.strokeColor     = white
        self.legend.deltax          = 75
        self.legend.deltay          = 10
        self.legend.autoXPadding    = 5
        self.legend.yGap            = 5
        self.legend.dxTextSpace     = 5
        self.legend.alignment       = 'right'
        self.legend.dividerLines    = 1|2|4
        self.legend.dividerOffsY    = 8
        self.legend.subCols.rpad    = 30
        n = len(self.pie.data)
        setItems(n,self.pie.slices,'fillColor',pdf_chart_colors)
        self.legend.colorNamePairs = [(self.pie.slices[i].fillColor, (labels[i][0:20], '%d' % data[i])) for i in xrange(n)]



from reportlab.lib.colors import PCMYKColor,black
from reportlab.graphics.charts.legends import Legend
from reportlab.graphics.shapes import Drawing, _DrawingEditorMixin
from reportlab.lib.validators import Auto
from reportlab.lib import colors
from reportlab.graphics.widgets.table import TableWidget
from reportlab.graphics.charts.barcharts import VerticalBarChart

class GroupedBarChart(_DrawingEditorMixin,Drawing):
    def __init__(self,data, labels, categories, small, padded, width=403,height=163,*args,**kw):
        Drawing.__init__(self,width,height,*args,**kw)
        fontName = 'Helvetica'
        fontSize = 11
        bFontName = 'Helvetica'
        bFontSize = 11
        colorsList = pdf_chart_colors

        self.hAlign = 'CENTER'
        self.width = 18 * cm
        self.height = 200

        self._add(self,VerticalBarChart(),name='chart',validate=None,desc=None)
        self.chart.height                  = 4*cm
        self.chart.width                  = 12.7*cm
        self.chart.fillColor               = None
        self.chart.data                    = data
        self.chart.bars.strokeWidth        = 0.5
        self.chart.bars.strokeColor        = colors.transparent
        for i, color in enumerate(colorsList): self.chart.bars[i].fillColor = color


        self.chart.valueAxis.labels.fontName       = fontName
        self.chart.valueAxis.labels.fillColor      = colors.HexColor('#777777')
        self.chart.valueAxis.labels.fontSize       = 9
        self.chart.valueAxis.strokeDashArray       = (5,0)
        self.chart.valueAxis.visibleGrid           = False
        self.chart.valueAxis.visibleTicks          = False
        self.chart.valueAxis.tickLeft              = 0
        self.chart.valueAxis.tickRight             = 11
        self.chart.valueAxis.strokeWidth           = 0.25
        self.chart.valueAxis.strokeColor = colors.HexColor('#777777')
        self.chart.valueAxis.avoidBoundFrac        = 0#1#0.5
        self.chart.valueAxis.rangeRound            ='both'
        self.chart.valueAxis.gridStart             = 13
        self.chart.valueAxis.gridEnd               = 342
        self.chart.valueAxis.labelTextFormat        = None #DecimalFormatter(1, suffix=None, prefix=None)
        self.chart.valueAxis.forceZero              = True
        self.chart.valueAxis.labels.boxAnchor       = 'e'
        self.chart.valueAxis.labels.dx              = -1






        self.chart.categoryAxis.strokeDashArray     = (1,0)
        self.chart.categoryAxis.visibleGrid         = False
        self.chart.categoryAxis.visibleTicks        = False
        self.chart.categoryAxis.strokeWidth         = 0.25
        self.chart.categoryAxis.strokeColor = colors.HexColor('#777777')
        self.chart.categoryAxis.tickUp              = 5
        self.chart.categoryAxis.tickDown            = 0
        self.chart.categoryAxis.labelAxisMode       ='low'
        self.chart.categoryAxis.labels.textAnchor   ='middle'
        self.chart.categoryAxis.labels.fillColor    = colors.HexColor('#777777')
        self.chart.categoryAxis.labels.angle        = 0
        self.chart.categoryAxis.labels.fontName     = bFontName
        self.chart.categoryAxis.labels.fontSize     = bFontSize
        self.chart.categoryAxis.labels.boxAnchor    = 'c'
        self.chart.categoryAxis.labels.dx           = 0#-10
        self.chart.categoryAxis.labels.dy           = -10
        self._add(self,Legend(),name='legend',validate=None,desc=None)



        self.legend.deltay           = 8
        self.legend.fontName         = fontName
        self.legend.fontSize         = fontSize
        self.legend.strokeWidth      = 0.5
        self.legend.strokeColor      = PCMYKColor(0,0,0,100)
        self.legend.autoXPadding     = 0
        self.legend.dy               = 5
        self.legend.variColumn       = True
        self.legend.subCols.minWidth = self.chart.width/2 # 175
        self.legend.colorNamePairs   = Auto(obj=self.chart)

        self._add(self,TableWidget(),name='table',validate=None,desc=None)

        if small:
            self.table.width = 17 * cm
            self.table.x = 1*cm
        else:
            self.table.width = 18 * cm
            self.table.x = 0

        self.table.y = 0
        if padded:
            self.table.height = 100
            self.table.y = -60
        else:
            self.table.height = 45

        self.table.borderStrokeColor = colors.transparent
        self.table.fillColor = colors.HexColor("#ecf0f1")
        self.table.borderStrokeWidth = 0.5
        self.table.horizontalDividerStrokeColor = colors.HexColor('#dddddd')
        self.table.verticalDividerStrokeColor = None
        self.table.horizontalDividerStrokeWidth = 0.5
        self.table.verticalDividerStrokeWidth = 0
        self.table.dividerDashArray = None
        self.table.data = labels
        self.table.boxAnchor = 'n'
        self.table.fontName = bFontName
        self.table.fontSize = bFontSize
        self.table.fontColor = colors.HexColor("#333333")
        self.table.alignment = 'left'
        self.table.textAnchor = 'middle'


        for i in range(len(self.chart.data)):
            self.chart.bars[i].name = labels[i][0]

        self.chart.categoryAxis.categoryNames = categories




        self.legend.dx             = 8
        self.legend.dxTextSpace    = 5
        self.legend.deltax         = 0
        self.legend.alignment      = 'right'
        self.legend.columnMaximum  = 6
        self.chart.y               = 75
        self.chart.barWidth        = 2
        self.chart.groupSpacing    = 5
        self.chart.barSpacing      = 0.5
        self.chart.x               = 150
        self.legend.y              = 75
        self.legend.boxAnchor      = 'sw'
        self.legend.x              = 24




        self.chart.bars[0].fillColor   = pdf_chart_colors[0]
        self.chart.bars[1].fillColor   = pdf_chart_colors[3]
        self.chart.bars[2].fillColor   = pdf_chart_colors[2]
        self.chart.bars[3].fillColor   = pdf_chart_colors[1]
        self.chart.bars[4].fillColor   = pdf_chart_colors[4]
        self.chart.bars[4].fillColor   = pdf_chart_colors[5]