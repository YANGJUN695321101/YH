from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QTextEdit, QSizePolicy


class ChatHistoryTextEdit(QTextEdit):
    def __init__(self, parent=None):
        super(ChatHistoryTextEdit, self).__init__(parent)
        self.setReadOnly(True)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.sender_avatar_path = "YOUR_USER_AVATAR_PATH"  # 替换为您的用户头像路径

    def set_receiver_avatar_path(self, avatar_path):
        self.receiver_avatar_path = avatar_path

    def add_message(self, message, is_sender):
        if is_sender:
            html_message = self.sender_message_to_html(message)
        else:
            html_message = self.receiver_message_to_html(message)

        self.append(html_message)
        

    def sender_message_to_html(self, message):
        return f"""
            <div style="
                display: inline-block;
                background-color: #DCF8C6;
                max-width: 60%;
                padding: 8px;
                border-radius: 5px;
                border-top-right-radius: 0;
                margin-bottom: 8px;
                margin-left: auto;
            ">
                <div style="
                    word-wrap: break-word;
                    width: 100%;
                ">
                    {message}
                </div>
            </div>
        """

    def receiver_message_to_html(self, message):
        return f"""
            <div style="
                display: inline-block;
                background-color: #FFFFFF;
                max-width: 60%;
                padding: 8px;
                border-radius: 5px;
                border-top-left-radius: 0;
                margin-bottom: 8px;
                margin-right: auto;
            ">
                <div style="
                    word-wrap: break-word;
                    width: 100%;
                ">
                    {message}
                </div>
            </div>
        """



def add_messages():
    history_text_edit.add_message("你好，你好吗？", is_sender=True)
    history_text_edit.add_message("我很好，谢谢！", is_sender=False)

if __name__ == "__main__":
    app = QApplication([])
    window = QMainWindow()
    central_widget = QWidget()
    layout = QVBoxLayout(central_widget)
    history_text_edit = ChatHistoryTextEdit()
    layout.addWidget(history_text_edit)
    window.setCentralWidget(central_widget)
    window.show()

    # 使用 QTimer 来在事件循环开始后添加消息
    timer = QTimer()
    timer.timeout.connect(add_messages)
    timer.setSingleShot(True)
    timer.start(0)

    app.exec_()
