from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QFileDialog, QMenu, QListWidget, QAction

class ContactList(QListWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

    def contextMenuEvent(self, event):
        context_menu = QMenu(self)

        change_avatar_action = QAction("更换头像", self)
        delete_chat_action = QAction("删除聊天", self)
        context_menu.addAction(change_avatar_action)
        context_menu.addAction(delete_chat_action)

        change_avatar_action.triggered.connect(self.change_avatar)
        delete_chat_action.triggered.connect(self.delete_chat)

        context_menu.exec_(event.globalPos())

    def change_avatar(self):
        current_item = self.currentItem()
        if not current_item:
            return

        new_avatar_path, _ = QFileDialog.getOpenFileName(self, "选择头像", "", "Images (*.png *.xpm *.jpg *.bmp *.gif)")
        if not new_avatar_path:
            return

        # 更新联系人的头像
        contact = current_item.data(Qt.UserRole)
        contact.choose_avatar(new_avatar_path)

    def delete_chat(self):
        current_item = self.currentItem()
        if not current_item:
            return

        self.takeItem(self.row(current_item))
    