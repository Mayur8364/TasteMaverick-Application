import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont, QPixmap, QMovie
from PyQt5.QtCore import Qt
from Backend import store_and_recommend

class TasteMaverickApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Taste Maverick")
        self.setGeometry(100, 100, 800, 700)
        self.setStyleSheet("background-color: #001f3f;")

        main_layout = QVBoxLayout()

        top_bar = self.create_top_bar()
        main_layout.addWidget(top_bar)

        main_content = self.create_main_content()
        main_layout.addLayout(main_content)

        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

    def create_top_bar(self):
        top_bar_layout = QHBoxLayout()

        logo_label = QLabel()
        logo_pixmap = QPixmap("E:\\maverick\\WhatsApp Image 2024-11-20 at 7.01.41 PM.jpeg")
        logo_label.setPixmap(logo_pixmap.scaled(300, 300, Qt.KeepAspectRatio))
        logo_label.setAlignment(Qt.AlignLeft)
        top_bar_layout.addWidget(logo_label)

        title_label = QLabel("TASTE - MAVERIC :- BY TEAM INFINITY")
        title_label.setFont(QFont("Algerian", 30, QFont.Bold))
        title_label.setStyleSheet("color: #FFD700;")
        title_label.setAlignment(Qt.AlignCenter)
        top_bar_layout.addWidget(title_label)
        top_bar_layout.addStretch()

        menu_button = QPushButton("...")
        menu_button.setStyleSheet("background-color: #003366; color: white; font-size: 14px;")
        menu_button.setFixedSize(40, 30)

        menu = QMenu(self)
        history_action = QAction("History", self)
        menu_action = QAction("Menu", self)
        database_action = QAction("Database", self)
        menu.addAction(history_action)
        menu.addAction(menu_action)
        menu.addAction(database_action)

        menu_button.setMenu(menu)
        top_bar_layout.addWidget(menu_button)

        top_bar_widget = QWidget()
        top_bar_widget.setLayout(top_bar_layout)
        return top_bar_widget
        # ... (no changes)

    def create_main_content(self):
        main_layout = QHBoxLayout()

        left_layout = QVBoxLayout()
        left_layout.setContentsMargins(50, 20, 50, 20)

        fields = ["Name", "Age", "Weight", "Height", "Gender", "Mobile No.", "Mood"]
        self.inputs = {}

        for field in fields:
            label = QLabel(field)
            label.setStyleSheet("color: white; font-size: 14px;")
            input_field = QLineEdit()
            input_field.setStyleSheet("background-color: white; color: black;")
            left_layout.addWidget(label)
            left_layout.addWidget(input_field)
            self.inputs[field] = input_field

        submit_button = QPushButton("Submit")
        submit_button.setStyleSheet("background-color: #003366; color: white; font-size: 14px;")
        submit_button.setFixedSize(100, 30)
        submit_button.clicked.connect(self.submit_form)  # Connect submit button to submit_form method
        left_layout.addWidget(submit_button)

        gui_label = QLabel("GUI")
        gui_label.setStyleSheet("color: white; font-size: 20px; border: 2px dashed white; padding: 20px;")
        gui_movie = QMovie("E:\\maverick\\G.U.I Material-20241120T132939Z-001\\G.U.I Material\\VoiceReg\\Siri_1.gif")
        gui_label.setMovie(gui_movie)
        gui_movie.start()
        gui_label.setAlignment(Qt.AlignCenter)
        gui_label.setFixedSize(600, 400)

        main_layout.addLayout(left_layout)
        main_layout.addWidget(gui_label)

        return main_layout

    def submit_form(self):
        # Collect data from inputs
        data = {
            "name": self.inputs["Name"].text(),
            "age": self.inputs["Age"].text(),
            "weight": self.inputs["Weight"].text(),
            "height": self.inputs["Height"].text(),
            "gender": self.inputs["Gender"].text(),
            "mobile_no": self.inputs["Mobile No."].text(),
            "mood": self.inputs["Mood"].text()
        }

        # Validate fields
        if not all(data.values()):
            QMessageBox.warning(self, "Error", "Please fill out all fields!")
            return

        # Call backend function to store data and recommend a dish
        recommendation = store_and_recommend(data)

        # Show the recommended dish
        QMessageBox.information(self, "Recommended Dish", f"Dish: {recommendation}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TasteMaverickApp()
    window.show()
    sys.exit(app.exec_())