from PyQt5.QtCore import Qt
from PyQt5.QtChart import *
 
class MYChartView(QChartView):
# view 总窗口
    def __init__(self,parent):
        super(MYChartView, self).__init__()
        self.lastpoint = None
        self.setParent(parent)
        
        self.setCursor(Qt.CursorShape.OpenHandCursor)
        

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.lastpoint = event.pos()
            self.setCursor(Qt.CursorShape.ClosedHandCursor)
          
    def mouseMoveEvent(self, event):
        if event.buttons() & Qt.MouseButton.LeftButton :  
            offset = event.pos()-self.lastpoint
            self.chart().scroll(-offset.x(),offset.y())
            self.lastpoint = event.pos()
            

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.setCursor(Qt.CursorShape.OpenHandCursor)
        if event.button() == Qt.MouseButton.RightButton:
            self.chart().zoomReset()
            self.chart().zoom(0.99999)
            
    def wheelEvent(self, event):
        if event.angleDelta().y() > 0:
            self.chart().zoomIn()
        else:
            self.chart().zoomOut()

    def keyPressEvent(self, event):
        pass
    def keyReleaseEvent(self, event):
        pass


