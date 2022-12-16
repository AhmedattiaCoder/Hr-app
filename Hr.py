from PyQt5 import QtWidgets,QtCore,QtGui
import sys
import hr_design
from PyQt5.QtGui import QPixmap,QIcon
from PyQt5.QtWidgets import QTableWidgetItem
from itertools import zip_longest
from datetime import *
import webbrowser





def users11():
    def users5():
        Time2=datetime.now()
        users10=users00.currentItem()
        with open("Time1","a") as save_time1:
            save_time1.write(users10.text()+'\n')
            save_time1.write("%s %s"%(Time2.month,Time2.day)+'\n')
            save_time1.close()
        m11=QtWidgets.QMessageBox.about(d6,'Hr app','تم تسجيل غياب بنجاح ل '+users10.text())
    d6=QtWidgets.QDialog(program)
    d6.setFixedHeight(600)
    d6.setFixedWidth(600)
    d6.setStyleSheet(hr_design.d0)
    d6.setWindowTitle('تسجيل غياب')
    users00=QtWidgets.QListWidget(d6)
    users00.resize(580,580)
    users00.move(10,1)
    users00.setStyleSheet(hr_design.i0)
    users0=[]
    with open('users','r') as read_users1:
        users0=read_users1.read().rstrip('\n').split('\n')
        read_users1.close()
    number10=0
    for read_users3 in users0:
        users00.insertItem(0,users0[int(number10)])
        number10+=1
    users00.clicked.connect(users5)
    d6.show()

def users1():
    def users4():
        Time1=datetime.now()
        users0=users3.currentItem()
        with open("Time","a") as save_time:
            save_time.write(users0.text()+'\n')
            save_time.write("%s %s"%(Time1.month,Time1.day)+'\n')
            save_time.close()
        m10=QtWidgets.QMessageBox.about(d5,'Hr app','تم تسجيل حضور بنجاح ل '+users0.text())
    d5=QtWidgets.QDialog(program)
    d5.setFixedHeight(600)
    d5.setFixedWidth(600)
    d5.setStyleSheet(hr_design.d0)
    d5.setWindowTitle('تسجيل حضور')
    users3=QtWidgets.QListWidget(d5)
    users3.resize(580,580)
    users3.move(10,1)
    users3.setStyleSheet(hr_design.i0)
    users2=[]
    with open('users','r') as read_users:
        users2=read_users.read().rstrip('\n').split('\n')
        read_users.close()
    number9=0
    for read_users2 in users2:
        users3.insertItem(0,users2[int(number9)])
        number9+=1
    users3.clicked.connect(users4)
    d5.show()
def username():
    def save_username():
        username1=e7.text()
        password1=e2.text()
        with open('username','w') as file5:
            file5.write(username1+'\n')
            file5.write(password1+'\n')
        m9=QtWidgets.QMessageBox.about(d3,'Hr app','تم تغيير اسم المستخدم بنجاح')
    d3=QtWidgets.QDialog(program)
    d3.setStyleSheet(hr_design.d00)
    d3.setWindowTitle('تغيير اسم المستخدم الحالي')
    d3.setFixedHeight(150)
    d3.setFixedWidth(300)
    e7=QtWidgets.QLineEdit(d3)
    e7.resize(200,30)
    e7.move(60,30)
    e7.setStyleSheet(hr_design.e00)
    e7.setPlaceholderText('اسم المستخدم الجديد')
    e7.show()
    b12=QtWidgets.QPushButton('تغيير الاسم',d3)
    b12.setStyleSheet(hr_design.buttons4)
    b12.move(80,80)
    b12.resize(150,30)
    b12.clicked.connect(save_username)
    b12.show()
    d3.show()
def password0():
    def save_password():
        username2=e1.text()
        password3=e2.text()
        password4=e8.text()
        password5=e9.text()
        if password3==password4:
            with open("username",'w') as file6:
                file6.write(username2+'\n')
                file6.write(password5+'\n')
            m10=QtWidgets.QMessageBox.about(d4,'Hr app','تم تغيير كلمة المرور بنجاح')
        else:
            m8=QtWidgets.QMessageBox.warning(d4,'Hr app','كلمة المرور خطأ')
    d4=QtWidgets.QDialog(program)
    d4.setStyleSheet(hr_design.d00)
    d4.setWindowTitle('تغيير اسم المستخدم الحالي')
    d4.setFixedHeight(200)
    d4.setFixedWidth(300)
    e8=QtWidgets.QLineEdit(d4)
    e8.resize(200,30)
    e8.move(60,30)
    e8.setStyleSheet(hr_design.e00)
    e8.setPlaceholderText('كلمة المرور القديمه')
    e8.setEchoMode(QtWidgets.QLineEdit.Password)
    e8.show()
    e9=QtWidgets.QLineEdit(d4)
    e9.resize(200,30)
    e9.move(60,90)
    e9.setStyleSheet(hr_design.e00)
    e9.setPlaceholderText("كلمة المرور الجديدة")
    e9.setEchoMode(QtWidgets.QLineEdit.Password)
    e9.show()
    b13=QtWidgets.QPushButton('تغيير كلمة المرور',d4)
    b13.setStyleSheet(hr_design.buttons4)
    b13.move(120,150)
    b13.resize(150,30)
    b13.clicked.connect(save_password)
    b13.show()
    d4.show()
def web():
    webbrowser.open('Hr_web\\Hr.html')
def x():
    m1=QtWidgets.QMessageBox.question(program,'Hr app','هل تريد الخروج؟')
    if m1==QtWidgets.QMessageBox.Yes:
        exit()
def program2():
    def s1():
        def show1():
            names1=l0.currentItem()
            m2=QtWidgets.QMessageBox.about(d1,'Hr app','اسم الموظف هو '+names1.text())
        d1=QtWidgets.QDialog(program)
        d1.setFixedHeight(600)
        d1.setFixedWidth(600)
        d1.setStyleSheet(hr_design.d0)
        d1.setWindowTitle('قائمه الموظفين')
        l0=QtWidgets.QListWidget(d1)
        l0.resize(580,580)
        l0.move(10,1)
        list1=[]
        try:
            with open('data','r') as f3:
                list1=f3.read().rstrip('\n').split('\n')
                number00=0
                for file0 in list1:
                    l0.insertItem(1,str(list1[int(number00)]))
                    number00+=1
        except Exception as r:
            m3=QtWidgets.QMessageBox.warning(d1,'Hr app','حدث خطأ حاول مره اخري')
            print(r)
        l0.clicked.connect(show1)
        l0.show()
        l0.setStyleSheet(hr_design.i0)
        d1.show()
    def save():
        def save1():
            name1=e3.text()
            number=e4.text()
            number2=e5.text()
            number3=e6.text()
            with open('data','a') as file1:
                file1.write(name1+'\n')
                file1.write(number+'\n')
                file1.write(number2+'\n')
                file1.write(number3+'\n')
            with open('users','a') as file9:
                file9.write(name1+'\n')
                file9.close()
            m2=QtWidgets.QMessageBox.about(program,'Hr app','تم اضافه الموظف بنجاح')
        d2=QtWidgets.QDialog(program)
        d2.setFixedHeight(170)
        d2.setFixedWidth(450)
        d2.setStyleSheet(hr_design.d0)
        d2.setWindowTitle('موظف جديد')
        e3=QtWidgets.QLineEdit(d2)
        e3.resize(200,30)
        e3.move(240,30)
        e3.setStyleSheet(hr_design.e0)
        e3.setPlaceholderText('اسم الموظف')
        e3.show()
        e4=QtWidgets.QLineEdit(d2)
        e4.resize(200,30)
        e4.move(240,70)
        e4.setStyleSheet(hr_design.e0)
        e4.setPlaceholderText('رقم التيلفون')
        e4.show()
        e5=QtWidgets.QLineEdit(d2)
        e5.resize(200,30)
        e5.move(20,30)
        e5.setStyleSheet(hr_design.e0)
        e5.setPlaceholderText('الرقم القومي')
        e5.show()
        e6=QtWidgets.QLineEdit(d2)
        e6.resize(200,30)
        e6.move(20,70)
        e6.setStyleSheet(hr_design.e0)
        e6.setPlaceholderText('الرقم التأميني')
        e6.show()
        b11=QtWidgets.QPushButton('اضافه الموظف',d2)
        b11.setStyleSheet(hr_design.buttons3)
        b11.move(140,130)
        b11.resize(200,30)
        b11.clicked.connect(save1)
        b11.show()
        d2.show()
    name=e1.text()
    password=e2.text()
    list2=[]
    def Money():
        def screen():
            t1.hide()
            b000.hide()
            l3.show()
            l4.show()
            l5.show()
            b3.show()
            b4.show()
            b5.show()
            b6.show()
            b7.show()
            b8.show()
            b9.show()
            b10.show()
        l3.hide()
        l4.hide()
        l5.hide()
        b3.hide()
        b4.hide()
        b5.hide()
        b6.hide()
        b7.hide()
        b8.hide()
        b9.hide()
        b10.hide()
        t1=QtWidgets.QTableWidget(program)
        t1.setColumnCount(2)
        t1.setRowCount(30)
        t1.resize(1310,590)
        t1.move(30,1)
        t1.setStyleSheet(hr_design.t)
        t1.show()
        list4=[]
        with open("Time",'r') as readfile:
            list4=readfile.read().rstrip('\n').split('\n')
        list5=[]
        with open("Time",'r') as readfile1:
            list5=readfile1.read().rstrip('\n').split('\n')
        calc=1
        calc1=0
        calc2=1
        try:
            for names000 in list4:
                t1.setItem(calc,0,QTableWidgetItem(list4[calc1]))
                calc+=1
                calc1+=2 
            calc=0                     
        except:
            pass
        try:
            for names0000 in list4:
                t1.setItem(calc2,1,QTableWidgetItem(list4[calc2]))
                calc2+=2
                calc+=1  
        except:
            pass
        t1.setItem(0,0, QTableWidgetItem("اسم الموظف"))
        t1.setItem(0,1, QTableWidgetItem('الحضور'))
        b000=QtWidgets.QPushButton('رجوع',program)
        b000.setStyleSheet(hr_design.buttons2)
        b000.move(50,650)
        b000.resize(150,40)
        b000.setIconSize(QtCore.QSize(50,50))
        b000.clicked.connect(screen)
        b000.show()
    with open('username','r') as f6:
        list2=f6.read().rstrip('\n').split('\n')
    if name==list2[0] and password==list2[1] or name=='' and password=='' :
        l1.hide()
        e1.hide()
        e2.hide()
        b1.hide()
        l2.hide()
        program.setStyleSheet(hr_design.window2)
        l3=QtWidgets.QLabel(program)
        l3.move(1,1)
        l3.resize(1399,100)
        l3.setStyleSheet(hr_design.ll)
        l3.show()
        l4=QtWidgets.QLabel('الصفحة الرئيسية',program)
        l4.move(550,1)
        l4.resize(250,100)
        l4.setStyleSheet(hr_design.lll)
        l4.show()
        list3=[]
        with open('username','r') as f7:
            list3=f7.read().rstrip('\n').split('\n')
        l5=QtWidgets.QLabel('اسم المستخدم :'+list3[0],program)
        l5.move(670,150)
        l5.resize(500,100)
        l5.setStyleSheet(hr_design.lll)
        l5.show()
        b3=QtWidgets.QPushButton('موظف جديد',program)
        b3.setStyleSheet(hr_design.buttons2)
        b3.move(100,350)
        b3.resize(200,50)
        b3.setIcon(QIcon('icons\\user3.png'))
        b3.setIconSize(QtCore.QSize(50,50))
        b3.clicked.connect(save)
        b3.show()
        b4=QtWidgets.QPushButton('تسجيل غياب',program)
        b4.setStyleSheet(hr_design.buttons2)
        b4.move(100,450)
        b4.resize(200,50)
        b4.setIcon(QIcon('icons\\user2.png'))
        b4.setIconSize(QtCore.QSize(50,50))
        b4.clicked.connect(users11)
        b4.show()
        b5=QtWidgets.QPushButton('تسجيل حضور',program)
        b5.setStyleSheet(hr_design.buttons2)
        b5.move(600,450)
        b5.resize(200,50)
        b5.setIcon(QIcon('icons\\true.png'))
        b5.setIconSize(QtCore.QSize(40,40))
        b5.clicked.connect(users1)
        b5.show()
        b6=QtWidgets.QPushButton('قائمه الموظفين',program)
        b6.setStyleSheet(hr_design.buttons2)
        b6.move(350,350)
        b6.resize(200,50)
        b6.setIcon(QIcon('icons\\list.png'))
        b6.setIconSize(QtCore.QSize(40,40))
        b6.clicked.connect(s1)
        b6.show()
        b7=QtWidgets.QPushButton('المرتبات',program)
        b7.setStyleSheet(hr_design.buttons2)
        b7.move(350,450)
        b7.resize(200,50)
        b7.setIcon(QIcon('icons\\money.png'))
        b7.setIconSize(QtCore.QSize(50,50))
        b7.clicked.connect(Money)
        b7.show()
        b8=QtWidgets.QPushButton('مساعده',program)
        b8.setStyleSheet(hr_design.buttons2)
        b8.move(600,350)
        b8.clicked.connect(web)
        b8.resize(200,50)
        b8.setIcon(QIcon('icons\\help.png'))
        b8.setIconSize(QtCore.QSize(40,40))
        b8.show()
        b9=QtWidgets.QPushButton('تغيير الاسم',program)
        b9.setStyleSheet(hr_design.buttons2)
        b9.move(850,350)
        b9.clicked.connect(username)
        b9.resize(200,50)
        b9.setIcon(QIcon('icons\\name.png'))
        b9.setIconSize(QtCore.QSize(40,40))
        b9.show()
        b10=QtWidgets.QPushButton('تغيير كلمه المرور',program)
        b10.setStyleSheet(hr_design.buttons2)
        b10.move(850,450)
        b10.clicked.connect(password0)
        b10.setIcon(QIcon('icons\\password.png'))
        b10.setIconSize(QtCore.QSize(40,40))
        b10.resize(200,50)
        b10.show()
    else:
        l2.setText('حاول مره اخري')
app=QtWidgets.QApplication(sys.argv)
program=QtWidgets.QMainWindow()
program.setWindowTitle('Hr app')
program.setStyleSheet(hr_design.window)
program.resize(800,600)
program.setWindowIcon(QIcon("icons\\settings.ico"))
l1=QtWidgets.QLabel(program)
i1=QPixmap('icons\\user1.png').scaled(150,150)
l1.setPixmap(i1)
l1.setStyleSheet(hr_design.i)
l1.resize(200,200)
l1.move(610,1)
l2=QtWidgets.QLabel(program)
l2.resize(200,70)
l2.move(600,380)
l2.setStyleSheet(hr_design.l)
l2.show()
e1=QtWidgets.QLineEdit(program)
e1.move(600,300)
e1.resize(200,40)
e1.setStyleSheet(hr_design.e)
e1.setPlaceholderText('اسم المستخدم')
e2=QtWidgets.QLineEdit(program)
e2.move(600,350)
e2.resize(200,40)
e2.setEchoMode(QtWidgets.QLineEdit.Password)
e2.setStyleSheet(hr_design.e)
e2.setPlaceholderText('كلمه المرور')
b1=QtWidgets.QPushButton('تسجيل دخول',program)
b1.resize(200,40)
b1.move(600,450)
b1.clicked.connect(program2)
b1.setStyleSheet(hr_design.buttons)
b2=QtWidgets.QPushButton('خروج',program)
b2.resize(100,40)
b2.move(1260,650)
b2.setStyleSheet(hr_design.buttons1)
b2.clicked.connect(x)
program.showMaximized()
app.exec_()