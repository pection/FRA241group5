from PyQt4 import QtCore, QtGui
from Realtime_S_First import Ui_Form
import time
import sys
from Realtime_S_Question import Ui_MainWindowVote
from Realtime_S_Ask import Ui_MainWindowQuestion
import time
from Realtime_Server import Databaze
import time
import signal
a=0
class HumanoidMainWindow(QtGui.QMainWindow,Ui_Form):


    ClassID = 241
    StuID = None
    Click_table = 0
    lastdatetime = ''


    def __init__(self, parent=None,Username = None,Cls=None):
        super(HumanoidMainWindow, self).__init__(parent)
        self.StuID = Username
        self.ClassID = Cls
        #get username and class
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.Action()
        self.click_table = Databaze(server='10.61.3.223',username='2016FRA241G5',password='SzTGde9E9AxVaNXA',database='2016FRA241G5')

    def Action(self):
        QtCore.QObject.connect(self.ui.kaojai, QtCore.SIGNAL("clicked()"), self.GetdataTrue)
        QtCore.QObject.connect(self.ui.maikaojai,QtCore.SIGNAL("clicked()"), self.GetdataFalse)
        QtCore.QObject.connect(self.ui.vote, QtCore.SIGNAL("clicked()"), self.VoteTrue)
        QtCore.QObject.connect(self.ui.question, QtCore.SIGNAL("clicked()"), self.Question)

    def GetdataFalse(self):
        print "click! confuse"
        self.TF(0)

    def TF(self,TF):
        click_id = self.click_table.SELECT_MAX(table="Click Table",column="Click ID")[0][0]
        datetime = time.asctime( time.localtime(time.time())) #Tue Nov 08 12:41:18 2016
        datetime = datetime[20:24]+"-"+str(self.click_table.monthToNum(datetime[4:7]))+"-"+datetime[8:10]+" "+datetime[11:19]

        if click_id is None:
            click_id  = 0
        else:
            click_id += 1
        if self.lastdatetime == '':
            ck = True
            print "first"
        else:
            if datetime[:-3] != self.lastdatetime[:-3]:
                ck = True
                print "add"
            else:
                ck = False
                print "NOOO"
        if ck:
            self.click_table.ADD(table='Click Table',column=['Click ID','Class ID','Student ID','status','time'],value=[str(click_id),str(self.ClassID),str(self.StuID),TF,datetime])
            self.lastdatetime = datetime

    def GetdataTrue(self):
        print "click! understand"
        self.TF(1)

    def VoteTrue(self):
        WindowVote = 0
        WindowVote = Votewindow(Username = self.StuID,Cls = self.ClassID)
        WindowVote.show()



    def Question(self):
        Windowquestion.show()



class Votewindow(QtGui.QMainWindow,Ui_MainWindowVote):
    id = []
    ques_table = 0
    alis = 0
    ClassID = None


    def __init__(self, parent=None,Username = None,Cls = None):
        super(Votewindow, self).__init__(parent)
        self.ui = Ui_MainWindowVote(Username,Cls)
        self.ClassID = Cls
        self.ques_table = 0
        self.ques_table = Databaze(server='10.61.3.223',username='2016FRA241G5',password='SzTGde9E9AxVaNXA',database='2016FRA241G5',use_unicode=True)
        alis = self.ques_table.SQL("SELECT"+""+" `Question ID`, `Question` FROM `Question Table` WHERE (`Class ID` ="+str(self.ClassID)+") AND (`seen` <1) ORDER BY `Time` DESC LIMIT 4")

        self.id = []
        for i in range(0,len(alis)):
            self.id.append(alis[i][0])
        self.ui.setupUi(self,alis)
        self.ActionVote()




    def ActionVote(self):
        print self.id , "IDIDIDIDIDI"
        QtCore.QObject.connect(self.ui.Vote1, QtCore.SIGNAL("clicked()"),lambda: self.GetVoteQuestion(self.id[0]))
        QtCore.QObject.connect(self.ui.Vote2, QtCore.SIGNAL("clicked()"),lambda: self.GetVoteQuestion(self.id[1]))
        QtCore.QObject.connect(self.ui.Vote3, QtCore.SIGNAL("clicked()"),lambda: self.GetVoteQuestion(self.id[2]))
        QtCore.QObject.connect(self.ui.Vote4, QtCore.SIGNAL("clicked()"),lambda: self.GetVoteQuestion(self.id[3]))

    def GetVoteQuestion(self,index):
        f = open("vote.txt","r")
        votetxt = f.read()
        f.close()
        f = open("vote.txt","w")
        votetxt = votetxt.split(',')
        txt = []
        for a in votetxt:
            if a != '':
                txt.append(int(a))
        votetxt = txt
        txt = ""
        ck = False
        if index not in votetxt:
            i = self.ques_table.SELECT(select='Vote',table='Question Table',column='Question ID',IS=index)[0][0]
            self.ques_table.CHANGE(table = 'Question Table',column=['Vote'],to=[i+1],where=['Question ID',index])
            ck = True
        else:
            print "you have vote all ready"
        for a in votetxt:
            txt += (str(a)+",")
        if ck:
            txt += str(index)
        else:
            txt = txt[:-1]
        f.write(txt)
        f.close()



    def GetVoteQuestion1(self):
        print "DATA QUESTION1 +1"


    def GetVoteQuestion2(self):
        print "DATA QUESTION2 +1"


    def GetVoteQuestion3(self):
        print "DATA QUESTION3 +1"


    def GetVoteQuestion4(self):
        print "DATA QUESTION4 +1"


class Questionwindow(QtGui.QMainWindow,Ui_MainWindowQuestion):
    def __init__(self, parent=None,Username = None,Cls =None):
        super(Questionwindow, self).__init__(parent)
        self.ui = Ui_MainWindowQuestion()
        self.ui.setupUi(self,Username = Username,Cls = Cls)
        self.ActionQuestion()
    def ActionQuestion(self):
        QtCore.QObject.connect(self.ui.Sendbutton, QtCore.SIGNAL("clicked()"), self.Send)

    def Send(self):
        print "sent"
        self.close()



def login(Username=None,Subject=None):

    Date = str(time.asctime(time.localtime(time.time())))
    Day = Date[:3]
    Time = Date[11:13]

    login_table = Databaze(server='10.61.3.223',username='2016FRA241G5',password='SzTGde9E9AxVaNXA',database='2016FRA241G5')
    re = login_table.SELECT(table="Student Profile",select="Student ID",column="Student ID",IS= Username)
    if int(str(Username)[-2:]) >= 40:
        sec = "B"
    else:
        sec = "A"
    if len(re) == 0:
        login_table.ADD(table="Student Profile",column=["Student ID","Section","Login (amount)","Mini Quiz (amount)","Question ask (amount)","Correct (amount)","Answer (amount)"],value=[Username,sec,0,0,0,0,0])
    lis = login_table.SELECT(table="Subject",different=True,select="Code`,`Time",column="Day",IS='"'+Day+'"')

    if int(Time) < 13:
        search = 0
    else:
        search = 1
    for e in lis:
        if e[1] == search:

            return e[0]
    else:
        return None


if __name__ == "__main__":
    US = 58340500051
    if US is not None:
        try:
            cls = login(Username = US)[3:]
        except:
            cls = 100
        if cls != None:
            app = QtGui.QApplication(sys.argv)
            MainWindow = HumanoidMainWindow(Username = US,Cls=cls)
            WindowVote = Votewindow(Username = US,Cls=cls)
            Windowquestion = Questionwindow(Username = US,Cls =cls)
            MainWindow.show()
            sys.exit(app.exec_())
