from PyQt5.QtCore import QRectF, QSize, Qt
from PyQt5.QtGui import QIcon, QImage, QPainter, QPainterPath, QPixmap, QRegion
from PyQt5.QtWidgets import QSizePolicy, QToolButton, QHBoxLayout, QWidget
class CustomTitleBar(QWidget):
    def __init__(self, MainWindow, parent=None):
        super().__init__(parent)
        self.parent = MainWindow
        self.setAutoFillBackground(True)
        self.setFixedHeight(30)  # 设置标题栏的高度

        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)  # 设置大小策略

        # 创建按钮布局
        button_layout = QHBoxLayout()
        button_layout.setContentsMargins(5, 0, 5, 0)

        button_layout.setSpacing(0)

        # 创建最小化按钮
        self.minimize_button = QToolButton(self)
        self.minimize_button.setIcon(QIcon("D:\\DESK\\remHENKEAI\\SUOXIAO.ico"))
        self.minimize_button.setIconSize(QSize(20, 20))  # 设置图标尺寸
        self.minimize_button.clicked.connect(self.parent.showMinimized)

        # 创建最大化/还原按钮
        self.maximize_button = QToolButton(self)
        self.maximize_button.setIcon(QIcon("D:\\DESK\\remHENKEAI\\FANGDA.ico"))
        self.maximize_button.setIconSize(QSize(20, 20))  # 设置图标尺寸
        self.maximize_button.clicked.connect(self.toggle_maximize_restore)

        # 创建关闭按钮
        self.close_button = QToolButton(self)
        self.close_button.setIcon(QIcon("D:\\DESK\\remHENKEAI\\GUANBI.ico"))
        self.close_button.setIconSize(QSize(20, 20))  # 设置图标尺寸
        self.close_button.clicked.connect(self.parent.close)

        # 将按钮添加到按钮布局中
        button_layout.addWidget(self.minimize_button)
        button_layout.addWidget(self.maximize_button)
        button_layout.addWidget(self.close_button)

        # 创建一个新的水平布局，并添加弹性空间和按钮布局
        layout = QHBoxLayout(self)
        layout.setContentsMargins(5, 0, 15, 0)

        layout.setSpacing(0)

        # 添加空白QWidget到标题栏左侧，使按钮布局靠右
        left_empty_widget = QWidget(self)
        left_empty_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        layout.addWidget(left_empty_widget)

        layout.addLayout(button_layout)  # 将按钮布局添加到标题栏布局中

        self._is_maximized = False

    def toggle_maximize_restore(self):
        if self._is_maximized:
            self.parent.showNormal()
            self.maximize_button.setIcon(QIcon("D:\\DESK\\remHENKEAI\\FANGDA.ico"))
        else:
            self.parent.showMaximized()
            self.maximize_button.setIcon(QIcon("D:\\DESK\\remHENKEAI\\HUIFU.ico"))
        self._is_maximized = not self._is_maximized
    
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.parent.mousePressEvent(event)
            # 记录鼠标位置，用于计算窗口移动距离
            self.drag_pos = event.globalPos() - self.parent.frameGeometry().topLeft()

    def mouseMoveEvent(self, event):
        if event.buttons() & Qt.LeftButton:
            # 获取窗口的当前位置
            current_pos = event.globalPos()
            # 计算窗口移动的距离
            move = current_pos - self.drag_pos
            # 移动窗口
            self.parent.move(move)
    def mouseDoubleClickEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.toggle_maximize_restore()  # 调用放大缩小函数
