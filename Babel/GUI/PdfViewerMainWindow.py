# -*- coding: utf-8 -*-

####################################################################################################
# 
# Babel - A Bibliography Manager 
# Copyright (C) Salvaire Fabrice 2013 
# 
####################################################################################################

####################################################################################################

import codecs

from PyQt4 import QtCore, QtGui

####################################################################################################

from Babel.GUI.MainWindowBase import MainWindowBase
from Babel.GUI.Widgets.GrowingTextBrowser import GrowingTextBrowser
from Babel.GUI.Widgets.RowLayoutManager import RowLayoutManager
from Babel.Pdf.PdfDocument import PdfDocument

####################################################################################################

class PdfViewerMainWindow(MainWindowBase):

    ##############################################

    def __init__(self, pdf_path=None, parent=None):

        super(PdfViewerMainWindow, self).__init__(title='Babel PDF Viewer', parent=parent)

        self._init_ui()
        if pdf_path is not None:
            self.open_pdf(pdf_path)

    ##############################################

    def open_pdf(self, path):

        self._pdf_document = PdfDocument(path)
        for page in (self._info_page,
                     self._image_page,
                     self._text_page,
                     ):
            page.open_pdf()

    ##############################################
    
    def _create_actions(self):

        self._show_info_action = \
            QtGui.QAction('Info',
                          self,
                          toolTip='Info',
                          checkable=True,
                          triggered=lambda: self._set_current_widget(self._info_page),
                          )

        self._show_image_action = \
            QtGui.QAction('Image',
                          self,
                          toolTip='Image',
                          checkable=True,
                          triggered=lambda: self._set_current_widget(self._image_page),
                          )

        self._show_text_action = \
            QtGui.QAction('Text',
                          self,
                          toolTip='Text',
                          checkable=True,
                          triggered=lambda: self._set_current_widget(self._text_page),
                          )

        self._action_group = QtGui.QActionGroup(self)
        for action in (self._show_info_action,
                       self._show_image_action,
                       self._show_text_action,
                       ):
            self._action_group.addAction(action)

    ##############################################
    
    def _create_toolbar(self):

        self._show_info_action.setChecked(True)
        self._tool_bar = self.addToolBar('Tools')
        for action in (self._show_info_action,
                       self._show_image_action,
                       self._show_text_action,
                       ):
            self._tool_bar.addAction(action)

    ##############################################

    def init_menu(self):

        super(PdfViewerMainWindow, self).init_menu()

    ##############################################

    def _init_ui(self):

        self._stacked_widget = QtGui.QStackedWidget(self)
        self.setCentralWidget(self._stacked_widget)
        self._info_page = InfoPage(self)
        self._image_page = ImagePage(self)
        self._text_page = TextPage(self)
        for page in (self._info_page,
                     self._image_page,
                     self._text_page,
                     ):
            self._stacked_widget.addWidget(page)
        self.statusBar()
        self._create_actions()
        self._create_toolbar()

        self._translate_ui()

    ##############################################

    def _translate_ui(self):

        pass

    ##############################################

    def _set_current_widget(self, widget):

        self._stacked_widget.setCurrentWidget(widget)

####################################################################################################

class InfoPage(QtGui.QWidget):

    ##############################################

    def __init__(self, main_window):

        super(InfoPage, self).__init__()
        
        self._main_window = main_window
        self._init_ui()

    ##############################################

    def _init_ui(self):

        self._widgets = {}

        vertical_layout = QtGui.QVBoxLayout(self)

        grid_layout = QtGui.QGridLayout()
        row_layout_manager = RowLayoutManager(grid_layout)
        vertical_layout.addLayout(grid_layout)
        application = QtGui.QApplication.instance()
        palette = QtGui.QPalette(application.palette())
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        for key, title in (
            ('path', u'Path'),
            ('number_of_pages', u'Number of pages'),
            ('Title', u'Title'),
            ('Subject', u'Subject'),
            ('Author', u'Author'),
            ('Creator', u'Creator'),
            ('Producer', u'Producer'),
            ('CreationDate', u'Creation Date'),
            ('ModDate', u'Modification Date'),
            ):
            label = QtGui.QLabel(self)
            label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
            label.setText(title + u':')
            line_edit = QtGui.QLineEdit(self)
            self._widgets[key] = line_edit
            # line_edit.setPalette(palette)
            # line_edit.setFrame(False)
            line_edit.setReadOnly(True)
            label.setBuddy(line_edit)
            row_layout_manager.add_row((label, line_edit))

        label = QtGui.QLabel(self)
        label.setText(u'XML Metadata:')
        self._text_browser = QtGui.QTextBrowser(self)
        size_policy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        self._text_browser.setSizePolicy(size_policy)
        label.setBuddy(self._text_browser)
        vertical_layout.addWidget(label)
        vertical_layout.addWidget(self._text_browser)

        # spacer_item = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        # vertical_layout.addItem(spacer_item)

    ##############################################

    def open_pdf(self):

        pdf_document = self._main_window._pdf_document
        pdf_metadata = pdf_document.metadata
        key_value_pairs = [('path', pdf_document.path),
                           ('number_of_pages', pdf_document.number_of_pages),
                           ]
        for key in ('Title', 'Subject', 'Author', 'Creator', 'Producer', 'CreationDate', 'ModDate'):
            key_value_pairs.append((key, pdf_metadata[key]))
        for key, value in key_value_pairs:
            self._widgets[key].setText(str(value))
            # unicode(value, encoding=codecs.utf_8_encode))
        self._text_browser.setPlainText(pdf_metadata.metadata)

####################################################################################################

class ImagePage(QtGui.QScrollArea):

    ##############################################

    def __init__(self, main_window):

        super(ImagePage, self).__init__()
        
        self._main_window = main_window
        self._init_ui()

    ##############################################

    def _init_ui(self):

        # self._scroll_area = QtGui.QScrollArea(self)
        self.setWidgetResizable(True)
        self._pixmap_label = QtGui.QLabel()
        self.setWidget(self._pixmap_label)

    ##############################################

    def open_pdf(self):

        pdf_document = self._main_window._pdf_document
        np_array = pdf_document[0].to_pixmap()
        height, width = np_array.shape[:2]
        image = QtGui.QImage(np_array.data, width, height, QtGui.QImage.Format_ARGB32)
        self._pixmap_label.setPixmap(QtGui.QPixmap.fromImage(image))

####################################################################################################

class TextPage(QtGui.QScrollArea):

    ##############################################

    def __init__(self, main_window):

        super(TextPage, self).__init__()
        
        self._main_window = main_window
        self._init_ui()

    ##############################################

    def _init_ui(self):

        # self._scroll_area = QtGui.QScrollArea(self)
        # self._scroll_area.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.setWidgetResizable(True)

        self._container_widget = QtGui.QWidget()
        self._vertical_layout = QtGui.QVBoxLayout(self._container_widget) # Set container_widget layout
        self.setWidget(self._container_widget)

        spacer_item = QtGui.QSpacerItem(0, 0, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self._vertical_layout.addItem(spacer_item)

    ##############################################

    def open_pdf(self):

        pdf_document = self._main_window._pdf_document
        text_page = pdf_document[0].to_text()
        for block_text in text_page.block_iterator():
            self._append_block(block_text)

    ##############################################
            
    def _append_block(self, block_text):

        horizontal_layout = QtGui.QHBoxLayout()
        combo_box = QtGui.QComboBox(self._container_widget)
        for item in ('Text', 'Title', 'Authors', 'Abstract', 'Refrences'):
            combo_box.addItem(item)
        text_browser = GrowingTextBrowser(self._container_widget)
        text_browser.setPlainText(block_text)
        horizontal_layout.addWidget(combo_box, 0, QtCore.Qt.AlignTop)
        horizontal_layout.addWidget(text_browser, 0, QtCore.Qt.AlignTop)
        self._vertical_layout.addLayout(horizontal_layout)
            
####################################################################################################
#
# End
#
####################################################################################################