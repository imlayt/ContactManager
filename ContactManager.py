
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


def fillscreen(window, companyid=0, contactid=0):
    '''

    :param window:
    :param companyid=0: zero means return the first company (for startup and following deletions)
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

    contactlist = []
    companylist = []
    contactloglist = []


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

    contacttabcol1_layout = [[sg.Listbox(contactlist, size=(40, 15))],
                             [sg.Button('New Contact', key='_NEWCONTACT_')]
                             ]

    contacttabcol2_layout = [[sg.Text('Contact Details', background_color='#d2d2df', justification='center', size=(60, 1))],
                             [sg.Text('Name', justification='right', size=(20,1)), sg.InputText(key='_CONTACTNAME_', size=(40, 1))],
                             [sg.Text('Last Name', justification='right', size=(20, 1)), sg.InputText(key='_CONTACTLASTNAME_', size=(40, 1))],
                             [sg.Text('First Name', justification='right', size=(20, 1)), sg.InputText(key='_CONTACTFIRSTNAME_', size=(40, 1))],
                             [sg.Text('Job Title', justification='right', size=(20, 1)), sg.InputText(key='_CONTACTJOBTITLE_', size=(40, 1))],
                             [sg.Text('Company', justification='right', size=(20, 1)), sg.InputText(key='_CONTACTCOMPANY_', size=(40, 1))],
                             [sg.Text('Work Phone', justification='right', size=(20, 1)), sg.InputText(key='_WORKPHONE_', size=(40, 1))],
                             [sg.Text('Cell Phone', justification='right', size=(20, 1)), sg.InputText(key='_CELLPHONE_', size=(40, 1))],
                             [sg.Text('Work Email', justification='right', size=(20, 1)), sg.InputText(key='_CONTACTWORKEMAIL_', size=(40, 1))],
                             [sg.Text('Personal Email', justification='right', size=(20, 1)), sg.InputText(key='_CONTACTPERSONALEMAIL_', size=(40, 1))],
                             [sg.Text('Picture', justification='right', size=(20, 1)), sg.InputText(key='_CONTACTPICTURE_', size=(40, 1))],
                             [sg.Text('Last Updated', justification='right', size=(20, 1)), sg.InputText(key='_CONTACTLASTUPDATED_', size=(40, 1))],
                             [sg.Text('Notes', justification='right', size=(20, 1)),
                              sg.Multiline(key='_CONTACTNOTES_', size=(40, 10))],
                             ]

    Actionitemlisttabcol1_layout = [[sg.Listbox(contactlist, size=(40, 15))],
                             [sg.Button('New Action Item', key='_NEWACTIONITEM_')]
                             ]

    Actionitemlisttabcol2_layout = [[sg.T('Company', size=(25, 1)), sg.In(key='_ACTIONITEMLISTCOMPANYNAME_', size=(40, 1))],
                        [sg.T('Created', size=(25, 1)), sg.In(key='_ACTIONITEMLISTCREATED_', size=(40, 1))],
                         [sg.T('Due Date', size=(25, 1)), sg.In(key='ACTIONITEMLISTDUEDATE', size=(40, 1))],
                         [sg.T('Status', size=(25, 1)), sg.In(key='_ACTIONITEMLISTSTATUS_', size=(40, 1))],
                         [sg.T('Status Date', size=(25, 1)), sg.In(key='_ACTIONITEMLISTSTATUSDATE_', size=(40, 1))],
                        [sg.T('Action Item', size=(10, 1)),
                        sg.Multiline(key='_ACTIONITEMLISTACTIONITEM_', size=(55, 10))],
                        [sg.T('Notes', size=(10, 1)), sg.Multiline(key='_ACTIONITEMLISTNOTES_', size=(55, 10))],
                         ]

    contactlogtabcol1_layout = [[sg.Listbox(contactloglist, size=(40, 15))],
                             [sg.Button('New Contact Log Item', key='_NEWCONTACTLOGITETM_')]
                             ]

    contactlogtabcol2_layout = [[sg.T('Company', size=(25, 1)), sg.In(key='_ACTIONITEMLISTCOMPANYNAME_', size=(40, 1))],
                        [sg.T('Company', size=(25, 1)), sg.In(key='_CONTACTLOGCOMPANY_', size=(40, 1))],
                         [sg.T('Contact', size=(25, 1)), sg.In(key='_CONTACTLOGCONTACT_', size=(40, 1))],
                         [sg.T('Date/Time', size=(25, 1)), sg.In(key='_CONTACTLOGDATETIME_', size=(40, 1))],
                         [sg.T('Purpose', size=(25, 1)), sg.In(key='_CONTACTLOGPURPOSE_', size=(40, 1))],
                        [sg.T('Outcome', size=(10, 1)), sg.In(key='_CONTACTLOGOUTCOME_', size=(55, 10))],
                        [sg.T('Follow Up', size=(10, 1)), sg.Multiline(key='_CONTACTLOGFOLLOWUP_', size=(55, 10))],
                         ]

    contacttab_layout = [[sg.Column(contacttabcol1_layout, background_color=mediumgreen),
                    sg.Column(contacttabcol2_layout, background_color=mediumgreen)]
                    ]

    companytabcol1_layout = [[sg.Listbox(companylist, size=(40, 15))],
                             [sg.Button('New Company', key='_NEWCOMPANY_')]
                             ]

    companytabcol2_layout = [[sg.T('Company', size=(25, 1)), sg.In(key='_COMPANYNAME_', size=(40, 1))],
                        [sg.T('Website', size=(25, 1)), sg.In(key='_WEBADDRESS_', size=(40, 1))],
                         [sg.T('Phone', size=(25, 1)), sg.In(key='_PHONE_', size=(40, 1))],
                         [sg.T('Street Address 1', size=(25, 1)), sg.In(key='_STREETADDRESS1_', size=(40, 1))],
                         [sg.T('Street Address 2', size=(25, 1)), sg.In(key='_STREETADDRESS2_', size=(40, 1))],
                         [sg.T('City', size=(25, 1)), sg.In(key='_CITY_', size=(40, 1))],
                         [sg.T('State', size=(25, 1)), sg.In(key='_STATE_', size=(40, 1))],
                         [sg.T('ZIP Code', size=(25, 1)), sg.In(key='_ZIPCODE_', size=(40, 1))],
                         [sg.T('Notes', size=(25, 1)), sg.Multiline(key='_NOTES_', size=(40, 5))]
                         ]

    companytab_layout = [[sg.Column(companytabcol1_layout, background_color=mediumgreen),
                          sg.Column(companytabcol2_layout, background_color=mediumgreen)]]

    actionitemtab_layout = [[sg.Column(Actionitemlisttabcol1_layout, background_color=mediumgreen),
                             sg.Column(Actionitemlisttabcol2_layout, background_color=mediumgreen)]]

    contactlogtab_layout = [[sg.Column(contactlogtabcol1_layout, background_color=mediumgreen),
                             sg.Column(contactlogtabcol2_layout, background_color=mediumgreen)]]

    mainscreenlayout = [[sg.Button('Read'),
            sg.Button('New Log Entry', key='_NEW_'),
            sg.Button('Save New', key='_ADDNEW_', disabled=True),
            sg.Button('Save Changes', key='_SAVECHANGES_'),
            sg.Button('Preview Table', key='_PREVIEWTABLE_'),
            sg.Button('Delete Log Entry', key='_DELETELOGENTRY_')],
            [sg.TabGroup([[sg.Tab('Company Info', companytab_layout, tooltip='tip', background_color=mediumgreen),
                                       sg.Tab('Contacts', contacttab_layout, background_color=mediumgreen),
                                       sg.Tab('Action Items',actionitemtab_layout, background_color=mediumgreen),
                                       sg.Tab('Contact Log',contactlogtab_layout, background_color=mediumgreen)]],
            tooltip='Tab Group')],
                        [sg.Text('Message Area', size=(134, 1), key='_MESSAGEAREA_', background_color='white')],
                        [sg.Text('fileinfo', key='_FILEINFO_', size=(134, 1), justification='center',
                                background_color='white'), sg.Exit()],
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
        if event is None or event == "Exit":
            sys.exit(1)




# ##########################################
# execute the main function
if __name__=="__main__":
    # execute only if run as a script
    main()