
import sqlite3
from sqlite3 import Error
import PySimpleGUI as sg
import os
import sys
from datetime import datetime


my_db_file = 'C:/Users/imlay/OneDrive/Documents/my-CRM-AppData.db'
# my_db_file = ''

lightblue = '#b9def4'  # color used by PySimpleGUIdef __init__(self, logfile, table='LogEntries'):
mediumblue = '#d2d2df'  # color used by PySimpleGUI
mediumblue2 = '#534aea'  # color used by PySimpleGUI
mediumgreen = '#66b3b3'  # color used by PySimpleGUI
mediumgreen2 = '#00aaaa'  # color used by PySimpleGUI

class ContactTable:
    def __init__(self, connection, datatable):
        '''

        :param connection:
        :param datatable:
        '''
        self.conn = connection
        self.datatable = datatable
    pass

    def createrow(self, sqlstring, rowdata):
        '''

        :param sqlstring:
        :param rowdata:
        :return: True if successful  else False
        '''
        pass

    def readrows(self,sqlstring, manyrows=False):
        '''

        :param sqlstring:
        :param manyrows: return all matching rows if True else return 1 row
        :return: list containing 1 or more rows
        '''
        pass

    def updaterow(self, sqlstring, rowdata):
        '''

        :param sqlstring:
        :param rowdata:
        :return: True if successful else False
        '''
        pass

    def deleterow(self,sqlstring):
        '''

        :param sqlstring:
        :return: True if successful else False
        '''
        pass

def tableexists(datafile, datatable):
    if os.path.isfile(datafile):
        try:
            conn = sqlite3.connect(datafile)

            sql2 = "SELECT name FROM sqlite_master WHERE type = 'table' AND name LIKE '%s' ;" % tablename

            # print('sql2 => ', sql2)
            curr = conn.cursor()
            curr.execute(sql2)

            thetablename = curr.fetchall()

            if len(thetablename)==0:
                return False
            else:
                return True
        except Error as e:
            print(e)
            sg.Popup('Could not connect to the database', keep_on_top=True)
            return False
    else:
        sg.Popup('Database file does not exist - it will be created')
        return False

def validatedatafile(datafile):
    if os.path.isfile(datafile):
        # sg.Popup('datafile exist')
        return True
    else:
        sg.Popup('Database file does not exist')
        return False


def setmessage(message, window):
    '''
    :param window:
    :param message:
    :return:
    '''
    window.FindElement('_MESSAGEAREA_').Update(message)
    window.Refresh()


def db_connection(db_file):
    '''

    :param db_file:
    :return: connection if successful else return None
    '''
    try:
        conn = sqlite3.connect(db_file)
        print("sqlite3 version=", sqlite3.version)
        return conn
    except Error as e:
        print('Error: ', e)
        return None


def fillscreen(window, companiid=0, contactid=0):
    '''

    :param window:
    :param companiid=0: zero means return the first company (for startup and following deletions)
    :param contactid=0: zero means return the first contact (for startup and following deletions)
    :return:
    '''
    pass

def getactionitemrow(window):
    '''

    :param window:
    :return:
    '''
    pass

def getcompanyrow(window):
    pass

def getcontactrow(window):
    pass

def getcontactlogrow(window):
    pass


def main():
    '''

    :return:
    '''

    if validatedatafile(my_db_file):
        conn = db_connection(my_db_file)
    else:
        sg.Popup('db file does not exist')


    if conn  is not None:
        try:
            actionitemlist = ContactTable(conn,'ActionItemList')
            company = ContactTable(conn, 'Company')
            contact = ContactTable(conn, 'Contact')
            contactlog = ContactTable(conn, 'ContactLog')
        except:
            sg.Popup('FAILED to instantiate the tables')
            sys.exit(1)

    # PySimpleGUI form layout
    mainscreencolumn1 = []

    tab2column1_layout = [[sg.Text('Contact Details', background_color='#d2d2df', justification='center', size=(25, 1))],
            [sg.Text('Name', justification='right', size=(20,1)), sg.InputText(key='_CONTACTNAME_')],
            [sg.Text('Email', justification='right', size=(20, 1)), sg.InputText(key='_EMAIL_')],
            [sg.Text('Phone Number', justification='right', size=(20, 1)), sg.InputText(key='_PHONE_')],
            [sg.Text('Company', justification='right', size=(20, 1)), sg.InputText(key='_COMPANYNAME_')],
            [sg.Button('Edit', key='_EDITBUTTON_', disabled=True), sg.Button('New', key='_NEWBUTTON_', disabled=False)]]

    tab2column2_layout = [[sg.Text('Contact Details', background_color='#d2d2df', justification='center', size=(25, 1))],
            [sg.Text('Name', justification='right', size=(20,1)), sg.InputText(key='_CONTACTNAME_')],
            [sg.Text('Email', justification='right', size=(20, 1)), sg.InputText(key='_EMAIL_')],
            [sg.Text('Phone Number', justification='right', size=(20, 1)), sg.InputText(key='_PHONE_')],
            [sg.Text('Company', justification='right', size=(20, 1)), sg.InputText(key='_COMPANYNAME_')],
            [sg.Button('Edit', key='_EDITBUTTON_', disabled=True), sg.Button('New', key='_NEWBUTTON_', disabled=False)]]

    tab3column1_layout = [[sg.Text('Contact Details', background_color='#d2d2df', justification='center', size=(25, 1))],
            [sg.Text('Name', justification='right', size=(20,1)), sg.InputText(key='_CONTACTNAME_')],
            [sg.Text('Email', justification='right', size=(20, 1)), sg.InputText(key='_EMAIL_')],
            [sg.Text('Phone Number', justification='right', size=(20, 1)), sg.InputText(key='_PHONE_')],
            [sg.Text('Company', justification='right', size=(20, 1)), sg.InputText(key='_COMPANYNAME_')],
            [sg.Button('Edit', key='_EDITBUTTON_', disabled=True), sg.Button('New', key='_NEWBUTTON_', disabled=False)]]

    tab2_layout = [[sg.Column(tab2column1_layout, background_color=mediumgreen),
                    sg.Column(tab2column2_layout, background_color=mediumgreen)]]

    tab1_layout = [[sg.T('This is inside tab 1')], [sg.In(key='in')]]

    tab3_layout = [[sg.Column(tab3column1_layout, background_color=mediumgreen)]]

    mainscreenlayout = [[sg.TabGroup([[sg.Tab('Company', tab1_layout, tooltip='tip'),
                                       sg.Tab('Contact', tab2_layout),
                                       sg.Tab('Action Items',tab3_layout)]],
            tooltip='TIP2')],
            [sg.Button('Read'),
            sg.Button('New Log Entry', key='_NEW_'),
            sg.Button('Save New', key='_ADDNEW_', disabled=True),
            sg.Button('Save Changes', key='_SAVECHANGES_'),
            sg.Button('Preview Table', key='_PREVIEWTABLE_'),
            sg.Button('Delete Log Entry', key='_DELETELOGENTRY_')],
            [sg.Text('Message Area', size=(134, 1), key='_MESSAGEAREA_', background_color='white')],
            [sg.Text('fileinfo', key='_FILEINFO_', size=(134, 1), justification='center',
            background_color='white'), sg.Exit()]
            ]

    # ########################################
    # initialize main screen window
    sg.SetOptions(element_padding=(2, 2))
    window = sg.Window('Project Log App', default_element_size=(15, 1), background_color=mediumgreen2).Layout(
            mainscreenlayout)
    window.Finalize()
    # window.Refresh()

    while True:  # Event Loop
        event, values = window.Read()
        if event is None or event=="Exit":
            sys.exit(1)




# ##########################################
# execute the main function
if __name__=="__main__":
    # execute only if run as a script
    main()