
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
mediumgreen2 = '#00aaaa'  # color used by PySimpleGUIs



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

        try:
            curr = self.conn.cursor()
            # print('curr creation succeeded')
            # print('sqlstring =>', sqlstring)
            curr.execute(sqlstring, rowdata)
            # commit the changes
            self.conn.commit()
            # print('curr.execute succeeded')
            return True
        except Error as e:
            print(e)
            print('createrow FAILED(', rowdata, ')')
            return False

    def readrows(self,sqlstring,sqlvaluelist=None):
        '''

        :param sqlstring:
        :param sqlvaluelist: values to be inserted into the sqlstring when the cursor is executed
        :return: list containing 1 or more rows or None
        '''

        try:
            curr = self.conn.cursor()
            # print('curr creation succeeded')
            if sqlvaluelist is None:
                curr.execute(sqlstring)
            else:
                # print('cur.execute =>', sqlstring, sqlvaluelist)
                curr.execute(sqlstring, str(sqlvaluelist))

            # print('curr.execute succeeded')
            therecords = curr.fetchall()
            # print('therecords => ', therecords)
            return therecords
        except Error as e:
            print(e)
            return None

    def updaterow(self, sqlstring, rowdata):
        '''

        :param sqlstring:
        :param rowdata:
        :return: True if successful else False
        '''

        try:
            curr = self.conn.cursor()
            # print('curr creation succeeded')
            # print('sqlstring =>', sqlstring)
            curr.execute(sqlstring, rowdata)
            # commit the changes
            self.conn.commit()
            # print('curr.execute succeeded')
            return True
        except Error as e:
            print(e)
            print('updatelogentry FAILED(', rowdata, ')')
            return False

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

def fillcompanylistbox(table, window):
    '''

    :return: True/False
    '''
    sqlstr = 'SELECT CompanyName, ID FROM Company order by CompanyName;'

    companyboxlist = table.readrows(sqlstr)
    companynumber = companyboxlist[0][1]
    # print('currentcompany =>', companynumber)
    # print('companyboxlist =>', companyboxlist)
    window.FindElement('_COMPANYLISTBOX_').Update(companyboxlist)
    return companynumber


def fillcontactlistbox(table,window, currentcompany):
    '''

    :param table:
    :param window:
    :param currentcompany:
    :return:
    '''
    sqlstr = 'SELECT ContactName, ID FROM Contact where CompanyID = ? order by ContactName;'

    contactboxlist = table.readrows(sqlstr, currentcompany)
    contactnumber = contactboxlist[0][1]
    # print('contactnumber', contactnumber)
    # print('contactboxlist =>', contactboxlist)
    window.FindElement('_CONTACTLISTBOX_').Update(contactboxlist)
    return contactnumber
    

def getactionitemrow(window):

    '''
    :param window:
    :return:
    '''
    pass

def getcompanyrow(window):
    '''

    :param window:
    :return: list of values representing a row in the company table
    '''
    companyrow = []
    return companyrow


def fillcontactrow(table, contactnumber, window):
    '''

    :param table:
    :param contactnumber:
    :param window:
    :return: True/False
    '''
    sqlstring = 'SELECT * from Contact WHERE ID = ? ;'
    contactrow = table.readrows(sqlstring, contactnumber)

    window.FindElement('_CONTACTNUMBER_').Update(contactrow[0][0])
    window.FindElement('_CONTACTNAME_').Update(contactrow[0][1])
    window.FindElement('_CONTACTLASTNAME_').Update(contactrow[0][2])
    window.FindElement('_CONTACTFIRSTNAME_').Update(contactrow[0][3])
    window.FindElement('_CONTACTJOBTITLE_').Update(contactrow[0][4])
    window.FindElement('_CONTACTCOMPANY_').Update(contactrow[0][5])
    window.FindElement('_WORKPHONE_').Update(contactrow[0][6])
    window.FindElement('_CELLPHONE_').Update(contactrow[0][7])
    window.FindElement('_CONTACTWORKEMAIL_').Update(contactrow[0][8])
    window.FindElement('_CONTACTPERSONALEMAIL_').Update(contactrow[0][9])
    window.FindElement('_CONTACTPICTURE_').Update(contactrow[0][11])
    window.FindElement('_CONTACTLASTUPDATED_').Update(contactrow[0][12])
    window.FindElement('_CONTACTNOTES_').Update(contactrow[0][10])
    window.Refresh()
    return contactnumber

def fillcompanyrow(table, companynumber, window):
    '''

    :param table:
    :param companynumber:
    :param window:
    :return:
    '''
    sqlstring = 'SELECT * from Company WHERE ID = ? ;'
    contactrow = table.readrows(sqlstring, companynumber)

    window.FindElement('_COMPANYNUMBER_').Update(contactrow[0][0])
    window.FindElement('_COMPANYNAME_').Update(contactrow[0][1])
    window.FindElement('_WEBADDRESS_').Update(contactrow[0][2])
    window.FindElement('_STREETADDRESS1_').Update(contactrow[0][3])
    window.FindElement('_STREETADDRESS2_').Update(contactrow[0][4])
    window.FindElement('_CITY_').Update(contactrow[0][5])
    window.FindElement('_STATE_').Update(contactrow[0][6])
    window.FindElement('_ZIPCODE_').Update(contactrow[0][7])
    window.FindElement('_NOTES_').Update(contactrow[0][8])
    window.FindElement('_PHONE_').Update(contactrow[0][9])

    return companynumber


def getcontactlogrow(window):
    pass


def main():
    '''

    :return:
    '''
    actionitemlistbox = []
    contactlistbox = []
    companylistbox = []
    contactloglistbox = []

    sql_add_actionitem = ''
    sql_update_actionitem = ''
    sql_read_actionitem = ''

    sql_add_company = ''
    sql_update_company = ''
    sql_read_company = ''

    sql_add_contact = ''
    sql_update_contact = ''
    sql_read_contact = ''

    sql_add_contactlog = ''
    sql_update_contactlog = ''
    sql_read_contactlog = ''


    if validatedatafile(my_db_file):
        conn = db_connection(my_db_file)
        fileinfo = my_db_file
    else:
        conn = None
        sg.Popup('db file %s does not exist', my_db_file)


    if conn is not None:
        try:
            theactionitemlist = ContactTable(conn,'ActionItemList')
            thecompany = ContactTable(conn, 'Company')
            thecontact = ContactTable(conn, 'Contact')
            thecontactlog = ContactTable(conn, 'ContactLog')
        except:
            sg.Popup('FAILED to instantiate the tables')
            sys.exit(1)

    # PySimpleGUI screen layout

    contacttabcol1_layout = [[sg.Listbox(contactlistbox, size=(40, 15), key='_CONTACTLISTBOX_', enable_events=True)],
                             [sg.In(key='_CONTACTNUMBER_', size=(4, 1)),
                              sg.Button('New Contact', key='_NEWCONTACT_'),
                              sg.Button('Save Contact', key='_SAVECONTACT_')]
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
                              sg.Multiline(key='_CONTACTNOTES_', size=(40, 10))]
                             ]

    actionitemlisttabcol1_layout = [[sg.Listbox(actionitemlistbox, size=(40, 15), key='_ACTIONITEMLISTBOX_')],
                                    [sg.In(key='_ACTIONITEMNUMBER_', size=(4, 1)),
                                     sg.Button('New Action Item', key='_NEWACTIONITEM_'),
                                     sg.Button('Save Action Item', key='_SAVEACTIONITEM_')]
                             ]

    actionitemlisttabcol2_layout = [[sg.T('Company', size=(25, 1)), sg.In(key='_ACTIONITEMLISTCOMPANYNAME_', size=(40, 1))],
                        [sg.T('Created', size=(25, 1)), sg.In(key='_ACTIONITEMLISTCREATED_', size=(40, 1))],
                         [sg.T('Due Date', size=(25, 1)), sg.In(key='ACTIONITEMLISTDUEDATE', size=(40, 1))],
                         [sg.T('Status', size=(25, 1)), sg.In(key='_ACTIONITEMLISTSTATUS_', size=(40, 1))],
                         [sg.T('Status Date', size=(25, 1)), sg.In(key='_ACTIONITEMLISTSTATUSDATE_', size=(40, 1))],
                        [sg.T('Action Item', size=(10, 1)),
                        sg.Multiline(key='_ACTIONITEMLISTACTIONITEM_', size=(55, 10))],
                        [sg.T('Notes', size=(10, 1)), sg.Multiline(key='_ACTIONITEMLISTNOTES_', size=(55, 10))]
                         ]

    contactlogtabcol1_layout = [[sg.Listbox(contactloglistbox, size=(40, 15), key='_CONTACTLOGLISTBOX_')],
                             [sg.In(key='_CONTACTLOGNUMBER_', size=(4, 1)),
                              sg.Button('New Contact Log Item', key='_NEWCONTACTLOGITETM_'),
                               sg.Button('Save Log Item', key='_SAVECONTACTLOG_')]
                             ]

    contactlogtabcol2_layout = [[sg.T('Company', size=(25, 1)), sg.In(key='_ACTIONITEMLISTCOMPANYNAME_', size=(40, 1))],
                        [sg.T('Company', size=(25, 1)), sg.In(key='_CONTACTLOGCOMPANY_', size=(40, 1))],
                         [sg.T('Contact', size=(25, 1)), sg.In(key='_CONTACTLOGCONTACT_', size=(40, 1))],
                         [sg.T('Date/Time', size=(25, 1)), sg.In(key='_CONTACTLOGDATETIME_', size=(40, 1))],
                         [sg.T('Purpose', size=(25, 1)), sg.In(key='_CONTACTLOGPURPOSE_', size=(40, 1))],
                        [sg.T('Outcome', size=(10, 1)), sg.In(key='_CONTACTLOGOUTCOME_', size=(55, 10))],
                        [sg.T('Follow Up', size=(10, 1)), sg.Multiline(key='_CONTACTLOGFOLLOWUP_', size=(55, 10))]
                         ]

    contacttab_layout = [[sg.Column(contacttabcol1_layout, background_color=mediumgreen),
                    sg.Column(contacttabcol2_layout, background_color=mediumgreen)]
                    ]

    companytabcol1_layout = [[sg.Listbox(companylistbox, size=(40, 15), key='_COMPANYLISTBOX_', enable_events=True)],
                             [sg.In(key='_COMPANYNUMBER_', size=(4, 1)),
                                sg.Button('New Company', key='_NEWCOMPANY_'),
                                sg.Button('Save Company', key='_SAVECOMPANY_')]
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

    actionitemtab_layout = [[sg.Column(actionitemlisttabcol1_layout, background_color=mediumgreen),
                             sg.Column(actionitemlisttabcol2_layout, background_color=mediumgreen)]]

    contactlogtab_layout = [[sg.Column(contactlogtabcol1_layout, background_color=mediumgreen),
                             sg.Column(contactlogtabcol2_layout, background_color=mediumgreen)]]

    mainscreenlayout = [[sg.TabGroup([[sg.Tab('Company Info', companytab_layout, tooltip='tip', background_color=mediumgreen),
                            sg.Tab('Contacts', contacttab_layout, background_color=mediumgreen),
                            sg.Tab('Action Items',actionitemtab_layout, background_color=mediumgreen),
                            sg.Tab('Contact Log',contactlogtab_layout, background_color=mediumgreen)]],
            tooltip='Tab Group')],
                        [sg.Text('Message Area', size=(110, 1), key='_MESSAGEAREA_', background_color='white')],
                        [sg.Text(fileinfo, key='_FILEINFO_', size=(110, 1), justification='center',
                                background_color='lightblue'), sg.Exit()],
            ]

    # ########################################
    # initialize main screen window
    sg.SetOptions(element_padding=(2, 2))
    window = sg.Window('Contact Manager App', default_element_size=(15, 1), background_color=mediumgreen2).Layout(
            mainscreenlayout)
    window.Finalize()
    # window.Refresh()
    fillscreen(window,0,0)  # fill all the fields based on the first company and the first contact in that company
    currentcompany = fillcompanylistbox(thecompany, window)
    currentcontact = fillcontactlistbox(thecontact, window, currentcompany)
    fillcompanyrow(thecompany,currentcompany,window)
    fillcontactrow(thecontact,currentcontact,window)

    while True:  # Event Loop
        event, values = window.Read()
        if event is None or event == "Exit":
            break
        elif event == '_NEWCOMPANY_':
            sg.Popup('_NEWCOMPANY_')
            if company.createrow(sql_add_company, getcompanyrow(window)):
                setmessage('New company added', window)
        elif event == '_SAVECOMPANY_':
            sg.Popup('_SAVECOMPANY_')
            if company.updaterow(sql_update_actionitem, getcompanyrow(window)):
                setmessage('Company info saved', window)
        elif event == '_COMPANYLISTBOX_':
            # sg.Popup('_COMPANYLISTBOX_', values['_COMPANYLISTBOX_'][0][1])

            currentcompany = values['_COMPANYLISTBOX_'][0][1]
            fillcompanyrow(thecompany, currentcompany, window)
            currentcontact = fillcontactlistbox(thecontact, window, currentcompany)
            currentcontact = fillcontactrow(thecontact, values['_CONTACTLISTBOX_'][0][1], window)


            fillscreen(window,values['_COMPANYLISTBOX_'],values['_CONTACTLISTBOX_'])

        elif event == '_NEWCONTACT_':
            sg.Popup('_NEWCONTACT_')
            if thecontact.createrow(sql_add_contact, getcontactrow(window)):
                setmessage('New contact added', window)
        elif event=='_SAVECONTACT_':
            sg.Popup('_SAVECONTACT_')
            if thecontact.updaterow(sql_update_contact, getcontactrow(window)):
                setmessage('Contact info saved', window)
        elif event == '_CONTACTLISTBOX_':
            # sg.Popup('_CONTACTLISTBOX_', values['_CONTACTLISTBOX_'][0][1])
            # fillscreen(window,values['_COMPANYLISTBOX_'],values['_CONTACTLISTBOX_'])

            currentcontact = fillcontactrow(thecontact, values['_CONTACTLISTBOX_'][0][1],window)


        elif event == '_NEWACTIONITEM_':
            sg.Popup('_NEWACTIONITEM_')

        elif event == '_SAVEACTIONITEM_':
            sg.Popup('_SAVEACTIONITEM_')

        elif event == '_NEWCONTACTLOGITETM_':
            sg.Popup('_NEWCONTACTLOGITETM_')

        elif event=='_SAVECONTACTLOG_':
            sg.Popup('_SAVECONTACTLOG_')

# ##########################################
# execute the main function
if __name__=="__main__":
    # execute only if run as a script
    main()