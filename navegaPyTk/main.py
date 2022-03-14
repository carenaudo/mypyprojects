# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 20:20:21 2022

__author__ = "Carlos Renaudo"
__credits__ = ["Carlos Renaudo"]
__license__ = "MIT"
__version__ = "1.0.1"
__maintainer__ = "Carlos Renaudo"
__email__ = "c.a.renaudo@gmail.com"
__status__ = "Alpha, for learning only"
"""
#The following lines are based on the example from https://github.com/Andereoo/TkinterWeb/
#Based on https://epicchasgamer.com/2016/12/11/python-gtk-and-webkit-creating-a-web-browser-part-1/
#Based on https://epicchasgamer.com/2016/12/11/python-gtk-and-webkit-creating-a-web-browser-part-1/
#Based on https://epicchasgamer.com/2016/12/11/python-gtk-and-webkit-creating-a-web-browser-part-1/


#!/usr/bin/env python
import sys
from PySide2.QtCore import QUrl
from PySide2.QtWidgets import QApplication
from PySide2.QtWebEngineWidgets import QWebEngineView

root = QApplication(sys.argv)
webpage = QWebEngineView()
webpage.load(QUrl("https://google.com"))
webpage.show()

sys.exit(root.exec_())

