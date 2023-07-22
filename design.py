# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(950, 650)
        MainWindow.setMinimumSize(QtCore.QSize(950, 650))
        MainWindow.setMaximumSize(QtCore.QSize(950, 6500))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/icons/ITTOOLS_icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("")
        MainWindow.setAnimated(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.left_menu_panel = QtWidgets.QFrame(self.centralwidget)
        self.left_menu_panel.setGeometry(QtCore.QRect(0, 0, 311, 650))
        self.left_menu_panel.setStyleSheet("background-color: #161b22;\n"
"")
        self.left_menu_panel.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.left_menu_panel.setFrameShadow(QtWidgets.QFrame.Raised)
        self.left_menu_panel.setObjectName("left_menu_panel")
        self.title = QtWidgets.QLabel(self.left_menu_panel)
        self.title.setGeometry(QtCore.QRect(20, 20, 251, 61))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.title.setFont(font)
        self.title.setStyleSheet("color: white;\n"
"font: 55px \"Verdana\";\n"
"")
        self.title.setObjectName("title")
        self.show_plugins_btn = QtWidgets.QPushButton(self.left_menu_panel)
        self.show_plugins_btn.setGeometry(QtCore.QRect(0, 160, 451, 61))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.show_plugins_btn.setFont(font)
        self.show_plugins_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.show_plugins_btn.setStyleSheet("QPushButton {\n"
"    border: 0px;\n"
"    color: white;\n"
"    font: 25px \"Verdana\";\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"    background-color: #5a6677;\n"
"}\n"
"")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images/icons/show.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.show_plugins_btn.setIcon(icon1)
        self.show_plugins_btn.setIconSize(QtCore.QSize(40, 40))
        self.show_plugins_btn.setObjectName("show_plugins_btn")
        self.install_plugin_btn = QtWidgets.QPushButton(self.left_menu_panel)
        self.install_plugin_btn.setGeometry(QtCore.QRect(0, 220, 451, 61))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.install_plugin_btn.setFont(font)
        self.install_plugin_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.install_plugin_btn.setStyleSheet("QPushButton {\n"
"    border: 0px;\n"
"    color: white;\n"
"    font: 25px \"Verdana\";\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"    background-color: #5a6677;\n"
"}\n"
"")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("images/icons/download.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.install_plugin_btn.setIcon(icon2)
        self.install_plugin_btn.setIconSize(QtCore.QSize(40, 40))
        self.install_plugin_btn.setObjectName("install_plugin_btn")
        self.activate_plugin_btn = QtWidgets.QPushButton(self.left_menu_panel)
        self.activate_plugin_btn.setGeometry(QtCore.QRect(0, 280, 441, 61))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.activate_plugin_btn.setFont(font)
        self.activate_plugin_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.activate_plugin_btn.setStyleSheet("QPushButton {\n"
"    border: 0px;\n"
"    color: white;\n"
"    font: 25px \"Verdana\";\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"    background-color: #5a6677;\n"
"}\n"
"")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("images/icons/touch.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.activate_plugin_btn.setIcon(icon3)
        self.activate_plugin_btn.setIconSize(QtCore.QSize(40, 40))
        self.activate_plugin_btn.setObjectName("activate_plugin_btn")
        self.remove_plugin_btn = QtWidgets.QPushButton(self.left_menu_panel)
        self.remove_plugin_btn.setGeometry(QtCore.QRect(0, 340, 441, 61))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.remove_plugin_btn.setFont(font)
        self.remove_plugin_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.remove_plugin_btn.setStyleSheet("QPushButton {\n"
"    border: 0px;\n"
"    color: white;\n"
"    font: 25px \"Verdana\";\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"    background-color: #5a6677;\n"
"}\n"
"")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("images/icons/remove.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.remove_plugin_btn.setIcon(icon4)
        self.remove_plugin_btn.setIconSize(QtCore.QSize(40, 40))
        self.remove_plugin_btn.setObjectName("remove_plugin_btn")
        self.exit_btn = QtWidgets.QPushButton(self.left_menu_panel)
        self.exit_btn.setGeometry(QtCore.QRect(0, 480, 381, 61))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.exit_btn.setFont(font)
        self.exit_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.exit_btn.setStyleSheet("QPushButton {\n"
"    border: 0px;\n"
"    color: white;\n"
"    font-size: 25px;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"    background-color: #5a6677;\n"
"}\n"
"")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("images/icons/exit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.exit_btn.setIcon(icon5)
        self.exit_btn.setIconSize(QtCore.QSize(40, 40))
        self.exit_btn.setObjectName("exit_btn")
        self.contet_panel = QtWidgets.QFrame(self.centralwidget)
        self.contet_panel.setGeometry(QtCore.QRect(310, 74, 641, 576))
        self.contet_panel.setStyleSheet("background-color: #0d1117;\n"
"font: 25px \"Verdana\";\n"
"")
        self.contet_panel.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.contet_panel.setFrameShadow(QtWidgets.QFrame.Raised)
        self.contet_panel.setObjectName("contet_panel")
        self.whats_new_frame = QtWidgets.QFrame(self.contet_panel)
        self.whats_new_frame.setGeometry(QtCore.QRect(0, 0, 641, 576))
        self.whats_new_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.whats_new_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.whats_new_frame.setObjectName("whats_new_frame")
        self.any_new = QtWidgets.QFrame(self.whats_new_frame)
        self.any_new.setGeometry(QtCore.QRect(30, 30, 341, 111))
        self.any_new.setStyleSheet("QFrame {\n"
"    border: 2px dotted #214C87;\n"
"    background-color: #131C30;\n"
"}\n"
"QLabel {\n"
"    color: white;\n"
"    border: none;\n"
"    font-size: 18px;\n"
"}\n"
"")
        self.any_new.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.any_new.setFrameShadow(QtWidgets.QFrame.Raised)
        self.any_new.setObjectName("any_new")
        self.label = QtWidgets.QLabel(self.any_new)
        self.label.setGeometry(QtCore.QRect(10, 10, 241, 21))
        self.label.setObjectName("label")
        self.eternal_arts_frame = QtWidgets.QFrame(self.contet_panel)
        self.eternal_arts_frame.setGeometry(QtCore.QRect(0, 0, 641, 576))
        self.eternal_arts_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.eternal_arts_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.eternal_arts_frame.setObjectName("eternal_arts_frame")
        self.any_eternal = QtWidgets.QFrame(self.eternal_arts_frame)
        self.any_eternal.setGeometry(QtCore.QRect(30, 30, 341, 111))
        self.any_eternal.setStyleSheet("border: 2px dotted #214C87;\n"
"background-color: #131C30;")
        self.any_eternal.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.any_eternal.setFrameShadow(QtWidgets.QFrame.Raised)
        self.any_eternal.setObjectName("any_eternal")
        self.credits_frame = QtWidgets.QFrame(self.contet_panel)
        self.credits_frame.setGeometry(QtCore.QRect(0, 0, 641, 576))
        self.credits_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.credits_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.credits_frame.setObjectName("credits_frame")
        self.any_credits = QtWidgets.QFrame(self.credits_frame)
        self.any_credits.setGeometry(QtCore.QRect(30, 30, 341, 111))
        self.any_credits.setStyleSheet("border: 2px dotted #214C87;\n"
"background-color: #131C30;")
        self.any_credits.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.any_credits.setFrameShadow(QtWidgets.QFrame.Raised)
        self.any_credits.setObjectName("any_credits")
        self.about_frame = QtWidgets.QFrame(self.contet_panel)
        self.about_frame.setGeometry(QtCore.QRect(0, 0, 641, 576))
        self.about_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.about_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.about_frame.setObjectName("about_frame")
        self.any_about = QtWidgets.QFrame(self.about_frame)
        self.any_about.setGeometry(QtCore.QRect(30, 30, 341, 111))
        self.any_about.setStyleSheet("border: 2px dotted #214C87;\n"
"background-color: #131C30;")
        self.any_about.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.any_about.setFrameShadow(QtWidgets.QFrame.Raised)
        self.any_about.setObjectName("any_about")
        self.settings_frame = QtWidgets.QFrame(self.contet_panel)
        self.settings_frame.setGeometry(QtCore.QRect(0, 0, 641, 576))
        self.settings_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.settings_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.settings_frame.setObjectName("settings_frame")
        self.any_settings = QtWidgets.QFrame(self.settings_frame)
        self.any_settings.setGeometry(QtCore.QRect(30, 30, 341, 111))
        self.any_settings.setStyleSheet("QFrame {\n"
"    border: 2px dotted #214C87;\n"
"    background-color: #131C30;\n"
"}\n"
"")
        self.any_settings.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.any_settings.setFrameShadow(QtWidgets.QFrame.Raised)
        self.any_settings.setObjectName("any_settings")
        self.show_plugins_frame = QtWidgets.QFrame(self.contet_panel)
        self.show_plugins_frame.setGeometry(QtCore.QRect(0, 0, 641, 576))
        self.show_plugins_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.show_plugins_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.show_plugins_frame.setObjectName("show_plugins_frame")
        self.frame_title = QtWidgets.QLabel(self.show_plugins_frame)
        self.frame_title.setGeometry(QtCore.QRect(100, 10, 381, 31))
        self.frame_title.setStyleSheet("color: #ffffff;")
        self.frame_title.setObjectName("frame_title")
        self.hint = QtWidgets.QLabel(self.show_plugins_frame)
        self.hint.setGeometry(QtCore.QRect(80, 50, 431, 31))
        self.hint.setStyleSheet("color: #47525E;")
        self.hint.setObjectName("hint")
        self.plugin_input = QtWidgets.QLineEdit(self.show_plugins_frame)
        self.plugin_input.setGeometry(QtCore.QRect(130, 90, 260, 35))
        self.plugin_input.setStyleSheet("QLineEdit {\n"
"    background-color: white;\n"
"    color: black;\n"
"    font-size: 17px;\n"
"    border-radius: 10px;\n"
"}")
        self.plugin_input.setObjectName("plugin_input")
        self.plugins = QtWidgets.QScrollArea(self.show_plugins_frame)
        self.plugins.setGeometry(QtCore.QRect(9, 129, 621, 451))
        self.plugins.setStyleSheet("border: 1px solid #47525E;")
        self.plugins.setWidgetResizable(True)
        self.plugins.setObjectName("plugins")
        self.plugins_area_content = QtWidgets.QWidget()
        self.plugins_area_content.setGeometry(QtCore.QRect(0, 0, 619, 449))
        self.plugins_area_content.setObjectName("plugins_area_content")
        self.plugins.setWidget(self.plugins_area_content)
        self.install = QtWidgets.QPushButton(self.show_plugins_frame)
        self.install.setGeometry(QtCore.QRect(400, 90, 35, 35))
        self.install.setStyleSheet("QPushButton {\n"
"    border: 0px;\n"
"    color: white;\n"
"    font: 25px \"Verdana\";\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"    background-color: #5a6677;\n"
"}\n"
"")
        self.install.setText("")
        self.install.setIcon(icon2)
        self.install.setIconSize(QtCore.QSize(30, 30))
        self.install.setObjectName("install")
        self.credits_frame.raise_()
        self.about_frame.raise_()
        self.settings_frame.raise_()
        self.eternal_arts_frame.raise_()
        self.show_plugins_frame.raise_()
        self.whats_new_frame.raise_()
        self.top_menu_panel = QtWidgets.QFrame(self.centralwidget)
        self.top_menu_panel.setGeometry(QtCore.QRect(310, -7, 641, 81))
        self.top_menu_panel.setStyleSheet("background-color: #0d1117;")
        self.top_menu_panel.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.top_menu_panel.setFrameShadow(QtWidgets.QFrame.Raised)
        self.top_menu_panel.setObjectName("top_menu_panel")
        self.border_line = QtWidgets.QFrame(self.top_menu_panel)
        self.border_line.setGeometry(QtCore.QRect(0, 76, 641, 6))
        self.border_line.setMinimumSize(QtCore.QSize(0, 3))
        self.border_line.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.border_line.setLineWidth(0)
        self.border_line.setFrameShape(QtWidgets.QFrame.HLine)
        self.border_line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.border_line.setObjectName("border_line")
        self.whats_new_btn = QtWidgets.QPushButton(self.top_menu_panel)
        self.whats_new_btn.setGeometry(QtCore.QRect(10, 6, 163, 70))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.whats_new_btn.setFont(font)
        self.whats_new_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.whats_new_btn.setStyleSheet("QPushButton {\n"
"    border: 0px;\n"
"    color: white;\n"
"    font: 25px \"Verdana\";\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"    color: white;\n"
"}\n"
"")
        self.whats_new_btn.setIconSize(QtCore.QSize(40, 40))
        self.whats_new_btn.setObjectName("whats_new_btn")
        self.eternal_arts_btn = QtWidgets.QPushButton(self.top_menu_panel)
        self.eternal_arts_btn.setGeometry(QtCore.QRect(170, 6, 163, 70))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.eternal_arts_btn.setFont(font)
        self.eternal_arts_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.eternal_arts_btn.setStyleSheet("QPushButton {\n"
"    border: 0px;\n"
"    color: #C2C2C2;\n"
"    font: 25px \"Verdana\";\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"    color: white;\n"
"}\n"
"\n"
"")
        self.eternal_arts_btn.setIconSize(QtCore.QSize(40, 40))
        self.eternal_arts_btn.setObjectName("eternal_arts_btn")
        self.credits_btn = QtWidgets.QPushButton(self.top_menu_panel)
        self.credits_btn.setGeometry(QtCore.QRect(330, 6, 104, 70))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.credits_btn.setFont(font)
        self.credits_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.credits_btn.setStyleSheet("QPushButton {\n"
"    border: 0px;\n"
"    color: #C2C2C2;\n"
"    font: 25px \"Verdana\";\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"    color: white;\n"
"}\n"
"")
        self.credits_btn.setIconSize(QtCore.QSize(40, 40))
        self.credits_btn.setObjectName("credits_btn")
        self.about_btn = QtWidgets.QPushButton(self.top_menu_panel)
        self.about_btn.setGeometry(QtCore.QRect(440, 6, 84, 70))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.about_btn.setFont(font)
        self.about_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.about_btn.setStyleSheet("QPushButton {\n"
"    border: 0px;\n"
"    color: #C2C2C2;\n"
"    font: 25px \"Verdana\";\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"    color: white;\n"
"}\n"
"")
        self.about_btn.setIconSize(QtCore.QSize(40, 40))
        self.about_btn.setObjectName("about_btn")
        self.settings_btn = QtWidgets.QPushButton(self.top_menu_panel)
        self.settings_btn.setGeometry(QtCore.QRect(590, 15, 41, 51))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.settings_btn.setFont(font)
        self.settings_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.settings_btn.setStyleSheet("QPushButton {\n"
"    border: 0px;\n"
"    color: white;\n"
"    font: 25px \"Verdana\";\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"    background-color: #5a6677;\n"
"}\n"
"")
        self.settings_btn.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("images/icons/settings.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.settings_btn.setIcon(icon6)
        self.settings_btn.setIconSize(QtCore.QSize(40, 40))
        self.settings_btn.setObjectName("settings_btn")
        self.contet_panel.raise_()
        self.left_menu_panel.raise_()
        self.top_menu_panel.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ITTOOLS"))
        self.title.setText(_translate("MainWindow", "ITTOOLS"))
        self.show_plugins_btn.setText(_translate("MainWindow", "Show plugins                     "))
        self.install_plugin_btn.setText(_translate("MainWindow", "Install plugin                      "))
        self.activate_plugin_btn.setText(_translate("MainWindow", "Activate plugin                   "))
        self.remove_plugin_btn.setText(_translate("MainWindow", "Remove plugin                   "))
        self.exit_btn.setText(_translate("MainWindow", "Exit                                "))
        self.label.setText(_translate("MainWindow", "We are working! :)"))
        self.frame_title.setText(_translate("MainWindow", "No your plugin here? Install it!"))
        self.hint.setText(_translate("MainWindow", "Write <devname>\\<pluginname>"))
        self.whats_new_btn.setText(_translate("MainWindow", "Whats new?"))
        self.eternal_arts_btn.setText(_translate("MainWindow", "Eternal Arts"))
        self.credits_btn.setText(_translate("MainWindow", "Credits"))
        self.about_btn.setText(_translate("MainWindow", "About"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
