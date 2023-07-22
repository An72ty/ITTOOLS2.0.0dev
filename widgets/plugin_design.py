# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'widgets\plugin_design.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Plugin(object):
    def setupUi(self, Plugin):
        Plugin.setObjectName("Plugin")
        Plugin.resize(617, 84)
        Plugin.setStyleSheet("QWidget {\n"
"    background-color: #0d1117;\n"
"    border: none;\n"
"}")
        self.name = QtWidgets.QLabel(Plugin)
        self.name.setGeometry(QtCore.QRect(84, 10, 380, 41))
        self.name.setStyleSheet("font: 20px \"Verdana\";\n"
"color: white;\n"
"border: none;")
        self.name.setObjectName("name")
        self.icon = QtWidgets.QLabel(Plugin)
        self.icon.setGeometry(QtCore.QRect(10, 10, 64, 64))
        self.icon.setStyleSheet("border: none;")
        self.icon.setText("")
        self.icon.setPixmap(QtGui.QPixmap("widgets\\../images/icons/ITTOOLS_icon.ico"))
        self.icon.setObjectName("icon")
        self.reinstall = QtWidgets.QPushButton(Plugin)
        self.reinstall.setGeometry(QtCore.QRect(475, 25, 35, 35))
        self.reinstall.setStyleSheet("QPushButton {\n"
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
        self.reinstall.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("widgets\\../images/icons/download.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.reinstall.setIcon(icon)
        self.reinstall.setIconSize(QtCore.QSize(30, 30))
        self.reinstall.setObjectName("reinstall")
        self.remove = QtWidgets.QPushButton(Plugin)
        self.remove.setGeometry(QtCore.QRect(520, 25, 35, 35))
        self.remove.setStyleSheet("QPushButton {\n"
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
        self.remove.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("widgets\\../images/icons/exit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.remove.setIcon(icon1)
        self.remove.setIconSize(QtCore.QSize(30, 30))
        self.remove.setObjectName("remove")
        self.activate = QtWidgets.QPushButton(Plugin)
        self.activate.setGeometry(QtCore.QRect(565, 25, 35, 35))
        self.activate.setStyleSheet("QPushButton {\n"
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
        self.activate.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("widgets\\../images/icons/touch.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.activate.setIcon(icon2)
        self.activate.setIconSize(QtCore.QSize(30, 30))
        self.activate.setObjectName("activate")
        self.version = QtWidgets.QLabel(Plugin)
        self.version.setGeometry(QtCore.QRect(84, 53, 380, 20))
        self.version.setStyleSheet("font: 15px \"Verdana\";\n"
"color: #47525E;\n"
"border: none;")
        self.version.setObjectName("version")

        self.retranslateUi(Plugin)
        QtCore.QMetaObject.connectSlotsByName(Plugin)

    def retranslateUi(self, Plugin):
        _translate = QtCore.QCoreApplication.translate
        Plugin.setWindowTitle(_translate("Plugin", "Plugin"))
        self.name.setText(_translate("Plugin", "Plugin"))
        self.version.setText(_translate("Plugin", "Plugin Version"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Plugin = QtWidgets.QWidget()
    ui = Ui_Plugin()
    ui.setupUi(Plugin)
    Plugin.show()
    sys.exit(app.exec_())
