from PyQt5.QtCore import Qt, QEvent
from PyQt5.QtWidgets import QApplication, QPushButton, QTextEdit, QVBoxLayout, QWidget, QSizePolicy

class ChatInputTextEdit(QTextEdit):
    def __init__(self, parent=None):
        super(ChatInputTextEdit, self).__init__(parent)

        self.setPlaceholderText("输入聊天内容")
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.setAcceptRichText(False)

        self.send_button = QPushButton("发送", self)
        self.send_button.clicked.connect(self.send_message)
        self.send_button.setFixedSize(50, 25)

        # 让发送按钮始终显示在输入框的右下角
        self.installEventFilter(self)

    def send_message(self):
        message = self.toPlainText().strip()
        if message:
            print("发送的消息:", message)
            self.clear()

    def eventFilter(self, obj, event):
        if obj == self:
            if event.type() == QEvent.Resize or event.type() == QEvent.Move:
                button_width = self.send_button.width()
                button_height = self.send_button.height()
                margin = 5

                # 将按钮移到输入框的右下角
                x = self.width() - button_width - margin
                y = self.height() - button_height - margin
                self.send_button.move(x, y)

        return super(ChatInputTextEdit, self).eventFilter(obj, event)

    def send_text(self):
        text = self.toPlainText().strip()
        if text:
            # 在这里发送文本
            print(f"发送: {text}")
            self.clear()



if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    main_window = QWidget()
    layout = QVBoxLayout(main_window)

    input_area = ChatInputTextEdit()
    layout.addWidget(input_area)

    main_window.show()
    sys.exit(app.exec_())
