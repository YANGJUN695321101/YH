from PyQt5.QtCore import QRect, QSize, Qt
from PyQt5.QtGui import QBrush, QColor, QMovie, QPainter, QPixmap
from PyQt5.QtWidgets import QFileDialog, QHBoxLayout, QLabel, QWidget


class ContactItem(QWidget):
    def __init__(self, name, avatar_path):
        super().__init__()

        self.name = name
        self.avatar_path = avatar_path

        self.initUI()

    def initUI(self):
        self.layout = QHBoxLayout()

        # 创建头像标签
        self.avatar_label = QLabel()
        self.avatar_label.setCursor(Qt.PointingHandCursor)  # 设置鼠标指针为手形
        self.layout.addWidget(self.avatar_label)

        self.update_avatar()

        # 联系人名称
        self.name_label = QLabel(self.name)
        self.layout.addWidget(self.name_label)

        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(10)
        self.setLayout(self.layout)

    def choose_avatar(self, avatar_path):
        """
        使用提供的 avatar_path 更改头像。
        """
        self.avatar_path = avatar_path
        self.update_avatar()

    def update_avatar(self):
        pixmap = QPixmap(self.avatar_path)
        pixmap = pixmap.scaled(64, 64, Qt.KeepAspectRatio, Qt.SmoothTransformation)

        if self.avatar_path.endswith(".gif"):
            movie = QMovie(self.avatar_path)
            movie.setScaledSize(QSize(64, 64))
            self.avatar_label.setMovie(movie)
            movie.start()
        else:
            self.avatar_label.setPixmap(pixmap)

        # 为新头像设置圆角矩形遮罩
        mask = QPixmap(64, 64)
        mask.fill(Qt.transparent)
        painter = QPainter(mask)
        painter.setBrush(QBrush(QColor("white")))
        painter.setPen(Qt.NoPen)
        painter.drawRoundedRect(QRect(0, 0, 64, 64), 32, 32)
        painter.end()
        self.avatar_label.setMask(mask.createMaskFromColor(Qt.transparent))
