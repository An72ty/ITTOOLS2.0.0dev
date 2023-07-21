from PyQt5 import QtWidgets
from PyQt5 import QtGui
from design import Ui_MainWindow
from dialogs import install_plugin
import sys


BASE_TOP_MENU_PANEL_BUTTON_STYLESHEET = """QPushButton {
                                            border: 0px;
                                            color: #C2C2C2;
                                            font: 25px "Verdana";
                                            }

                                            QPushButton::hover {
                                                color: white;
                                            }
                                        """
CLICKED_TOP_MENU_PANEL_BUTTON_STYLESHEET = """QPushButton {
                                            border: 0px;
                                            color: white;
                                            font: 25px "Verdana";
                                            }

                                            QPushButton::hover {
                                                color: white;
                                            }
                                        """
BASE_TOP_MENU_PANEL_SETTINGS_BUTTON_STYLESHEET = """QPushButton {
                                            border: 0px;
                                            color: white;
                                            font: 25px "Verdana";
                                            border-radius: 10px;
                                            }

                                            QPushButton::hover {
                                                background-color: #5a6677;
                                            }
                                        """
CLICKED_TOP_MENU_PANEL_SETTINGS_BUTTON_STYLESHEET = """QPushButton {
                                            border: 0px;
                                            background-color: #18202c;
                                            font: 25px "Verdana";
                                            border-radius: 10px;
                                            }

                                            QPushButton::hover {
                                                background-color: #18202c;
                                            }
                                        """


class MainWindow(Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.MainWindow = QtWidgets.QMainWindow()
        ui = super()
        ui.setupUi(self.MainWindow)

        self.add_functions_to_top_menu_panel_buttons()
        self.add_functions_to_left_menu_panel_buttons()

    def add_functions_to_top_menu_panel_buttons(self):
        def show_whats_new_frame():
            self.whats_new_btn.setStyleSheet(
                CLICKED_TOP_MENU_PANEL_BUTTON_STYLESHEET)
            self.eternal_arts_btn.setStyleSheet(
                BASE_TOP_MENU_PANEL_BUTTON_STYLESHEET)
            self.credits_btn.setStyleSheet(
                BASE_TOP_MENU_PANEL_BUTTON_STYLESHEET)
            self.about_btn.setStyleSheet(BASE_TOP_MENU_PANEL_BUTTON_STYLESHEET)
            self.settings_btn.setStyleSheet(
                BASE_TOP_MENU_PANEL_SETTINGS_BUTTON_STYLESHEET)

            self.whats_new_frame.raise_()

        def show_eternal_arts_frame():
            self.whats_new_btn.setStyleSheet(
                BASE_TOP_MENU_PANEL_BUTTON_STYLESHEET)
            self.eternal_arts_btn.setStyleSheet(
                CLICKED_TOP_MENU_PANEL_BUTTON_STYLESHEET)
            self.credits_btn.setStyleSheet(
                BASE_TOP_MENU_PANEL_BUTTON_STYLESHEET)
            self.about_btn.setStyleSheet(BASE_TOP_MENU_PANEL_BUTTON_STYLESHEET)
            self.settings_btn.setStyleSheet(
                BASE_TOP_MENU_PANEL_SETTINGS_BUTTON_STYLESHEET)

            self.eternal_arts_frame.raise_()

        def show_credits_frame():
            self.whats_new_btn.setStyleSheet(
                BASE_TOP_MENU_PANEL_BUTTON_STYLESHEET)
            self.eternal_arts_btn.setStyleSheet(
                BASE_TOP_MENU_PANEL_BUTTON_STYLESHEET)
            self.credits_btn.setStyleSheet(
                CLICKED_TOP_MENU_PANEL_BUTTON_STYLESHEET)
            self.about_btn.setStyleSheet(BASE_TOP_MENU_PANEL_BUTTON_STYLESHEET)
            self.settings_btn.setStyleSheet(
                BASE_TOP_MENU_PANEL_SETTINGS_BUTTON_STYLESHEET)

            self.credits_frame.raise_()

        def show_about_frame():
            self.whats_new_btn.setStyleSheet(
                BASE_TOP_MENU_PANEL_BUTTON_STYLESHEET)
            self.eternal_arts_btn.setStyleSheet(
                BASE_TOP_MENU_PANEL_BUTTON_STYLESHEET)
            self.credits_btn.setStyleSheet(
                BASE_TOP_MENU_PANEL_BUTTON_STYLESHEET)
            self.about_btn.setStyleSheet(
                CLICKED_TOP_MENU_PANEL_BUTTON_STYLESHEET)
            self.settings_btn.setStyleSheet(
                BASE_TOP_MENU_PANEL_SETTINGS_BUTTON_STYLESHEET)

            self.about_frame.raise_()

        def show_settings_frame():
            self.whats_new_btn.setStyleSheet(
                BASE_TOP_MENU_PANEL_BUTTON_STYLESHEET)
            self.eternal_arts_btn.setStyleSheet(
                BASE_TOP_MENU_PANEL_BUTTON_STYLESHEET)
            self.credits_btn.setStyleSheet(
                BASE_TOP_MENU_PANEL_BUTTON_STYLESHEET)
            self.about_btn.setStyleSheet(BASE_TOP_MENU_PANEL_BUTTON_STYLESHEET)
            self.settings_btn.setStyleSheet(
                CLICKED_TOP_MENU_PANEL_SETTINGS_BUTTON_STYLESHEET)

            self.settings_frame.raise_()

        self.whats_new_btn.clicked.connect(show_whats_new_frame)
        self.eternal_arts_btn.clicked.connect(show_eternal_arts_frame)
        self.credits_btn.clicked.connect(show_credits_frame)
        self.about_btn.clicked.connect(show_about_frame)
        self.settings_btn.clicked.connect(show_settings_frame)

    def add_functions_to_left_menu_panel_buttons(self):
        def show_show_plugins_frame():
            self.set_base_stylesheet_to_top_menu_panel_buttons()
            self.show_plugins_frame.raise_()

        def show_install_plugin_dialog():
            self.set_base_stylesheet_to_top_menu_panel_buttons()
            dialog = install_plugin.Dialog()
            dialog.Dialog.exec_()

        self.show_plugins_btn.clicked.connect(show_show_plugins_frame)
        self.install_plugin_btn.clicked.connect(show_install_plugin_dialog)
        self.exit_btn.clicked.connect(self.MainWindow.close)

    def set_base_stylesheet_to_top_menu_panel_buttons(self):
        self.whats_new_btn.setStyleSheet(BASE_TOP_MENU_PANEL_BUTTON_STYLESHEET)
        self.eternal_arts_btn.setStyleSheet(
            BASE_TOP_MENU_PANEL_BUTTON_STYLESHEET)
        self.credits_btn.setStyleSheet(BASE_TOP_MENU_PANEL_BUTTON_STYLESHEET)
        self.about_btn.setStyleSheet(BASE_TOP_MENU_PANEL_BUTTON_STYLESHEET)
        self.settings_btn.setStyleSheet(
            BASE_TOP_MENU_PANEL_SETTINGS_BUTTON_STYLESHEET)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.MainWindow.show()
    sys.exit(app.exec_())
