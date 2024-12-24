from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
from PyQt5.QtCore import QTimer, QDate
from PyQt5.QtWidgets import QGraphicsOpacityEffect

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(908, 603)
        MainWindow.setFixedSize(908, 603)

        self.statusBar().setVisible(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setEnabled(True)
        self.label.setGeometry(QtCore.QRect(0, 0, 911, 605))

        self.label.setAutoFillBackground(True)
        self.label.setStyleSheet("background-image: url(); opacity: 500;")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("japan-background-digital-art.jpg"))
        self.label.setScaledContents(True)
        self.label.setIndent(1)
        self.label.setObjectName("label")
        self.opacity_effect = QGraphicsOpacityEffect()
        self.opacity_effect.setOpacity(0.9)
        self.label.setGraphicsEffect(self.opacity_effect)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(100, 70, 151, 141))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("pomodro-removebg1.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(40, 0, 291, 71))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(30, 10, 255);")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(80, 220, 221, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(255, 0, 0);")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(110, 280, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(0, 255, 0);")
        self.label_5.setObjectName("label_5")
        
        # Timer Widgets
        self.timer_label = QtWidgets.QLabel(self.centralwidget)
        self.timer_label.setGeometry(QtCore.QRect(120, 330, 111, 71))
        self.timer_label.setStyleSheet("font-size: 28px; font-weight: bold; text-align: center; color: rgb(255, 170, 127);")
        self.timer_label.setAlignment(QtCore.Qt.AlignCenter)
        self.timer_label.setObjectName("timer_label")

        self.start_button = QtWidgets.QPushButton("Start", self.centralwidget)
        self.start_button.setGeometry(QtCore.QRect(60, 420, 100, 30))
        self.start_button.setStyleSheet("""
            border: 0;
            color: rgba(4,40,70,255);
            font-size: 35px;
        """)

        self.reset_button = QtWidgets.QPushButton("Reset", self.centralwidget)
        self.reset_button.setGeometry(QtCore.QRect(170, 420, 100, 30))
        self.reset_button.setStyleSheet("""
            border: 0;
            color: rgba(4,40,70,255);
            font-size: 35px;
        """)



        self.daily_usage_label = QtWidgets.QLabel(self.centralwidget)
        self.daily_usage_label.setGeometry(QtCore.QRect(30, 470, 300, 30))
        self.daily_usage_label.setStyleSheet("font-size: 22px; font-weight: bold; text-align: center; color:rgb(255, 10, 55);")
        self.daily_usage_label.setAlignment(QtCore.Qt.AlignCenter)

        # Task Tracker Widgets
        self.task_input = QtWidgets.QLineEdit(self.centralwidget)
        self.task_input.setGeometry(QtCore.QRect(580, 220, 250, 30))
        self.task_input.setPlaceholderText("Enter a task or study topic...")
        self.task_input.setStyleSheet("""
            border: 0;
            border-radius: 10px;
        """)

        self.add_task_button = QtWidgets.QPushButton("Add Task", self.centralwidget)
        self.add_task_button.setGeometry(QtCore.QRect(650, 270, 120, 30))
        self.add_task_button.setStyleSheet("""
            border: 0;
            color: rgba(254,167,174,255);
            font-size: 28px;
        """)
        self.task_list = QtWidgets.QListWidget(self.centralwidget)
        self.task_list.setGeometry(QtCore.QRect(580, 320, 250, 200))
        self.task_list.setStyleSheet("""
            border: 0;
            border-radius: 10px;
                    """)
        #  self.task_list.setStyleSheet("""
        #     border: 0;
        #     border-radius: 10px;
        #     background:transparent;
        # """)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 908, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Pomodoro Timer"))
        self.label_3.setText(_translate("MainWindow", "Pomodoro Technique"))
        self.label_4.setText(_translate("MainWindow", "25 min working"))
        self.label_5.setText(_translate("MainWindow", "5 min rest"))
        self.timer_label.setText("25:00")
        self.daily_usage_label.setText("Time spent today: 00:00")

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Database setup
        self.conn = sqlite3.connect("pomodoro.db")
        self.create_tables()

        # Timer settings
        self.work_time = 25 * 60
        self.break_time = 5 * 60
        self.current_time = self.work_time
        self.is_work_session = True
        self.timer_running = False
        self.today_date = QDate.currentDate().toString("yyyy-MM-dd")
        self.daily_usage = self.get_daily_usage()

        # Connect buttons
        self.start_button.clicked.connect(self.start_timer)
        self.reset_button.clicked.connect(self.reset_timer)
        self.add_task_button.clicked.connect(self.add_task)

        # Load tasks
        self.load_tasks()

        # Timer
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_timer)

    def create_tables(self):
        cursor = self.conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                date TEXT,
                task TEXT
            )
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS usage (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                date TEXT,
                time_spent INTEGER
            )
        """)
        self.conn.commit()

    def get_daily_usage(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT time_spent FROM usage WHERE date = ? ORDER BY time_spent DESC LIMIT 1", (self.today_date,))
        result = cursor.fetchone()
        return result[0] if result else 0

    def start_timer(self):
        if self.timer_running:
            self.timer.stop()
            self.start_button.setText("Start")
        else:
            self.timer.start(1000)
            self.start_button.setText("Pause")
        self.timer_running = not self.timer_running

    def update_timer(self):
        if self.current_time > 0:
            self.current_time -= 1
            self.timer_label.setText(self.format_time(self.current_time))
        else:
            self.timer.stop()
            self.timer_running = False
            self.start_button.setText("Start")
            self.switch_session()
        if self.is_work_session:
            self.daily_usage += 1
            self.daily_usage_label.setText(f"Time spent today: {self.format_time(self.daily_usage)}")
            self.save_daily_usage()

    def switch_session(self):
        self.is_work_session = not self.is_work_session
        self.current_time = self.work_time if self.is_work_session else self.break_time
        session_type = "Work" if self.is_work_session else "Break"
        self.timer_label.setText(f"{session_type} Time!")

    def reset_timer(self):
        self.timer.stop()
        self.timer_running = False
        self.start_button.setText("Start")
        self.is_work_session = True
        self.current_time = self.work_time
        self.timer_label.setText(self.format_time(self.current_time))

    def save_task(self, task):
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO tasks (date, task) VALUES (?, ?)", (self.today_date, task))
        self.conn.commit()

    def load_tasks(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT task FROM tasks WHERE date = ?", (self.today_date,))
        tasks = cursor.fetchall()
        for task in tasks:
            self.task_list.addItem(task[0])

    def save_daily_usage(self):
        cursor = self.conn.cursor()
        cursor.execute("INSERT OR REPLACE INTO usage (date, time_spent) VALUES (?, ?)", (self.today_date, self.daily_usage))
        self.conn.commit()

    def add_task(self):
        task = self.task_input.text().strip()
        if task:
            self.task_list.addItem(f"{self.today_date}: {task}")
            self.task_input.clear()
            self.save_task(task)

    def format_time(self, seconds):
        minutes = seconds // 60
        seconds = seconds % 60
        return f"{minutes:02}:{seconds:02}"

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindowApp = MainWindow()
    MainWindowApp.show()
    sys.exit(app.exec_())
