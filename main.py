from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import *

app = QApplication([])
window = QWidget()
window.resize(500, 500)
window.setWindowTitle("Питання та відповіді")


text = QLabel("Хто такий Т. Шевченко?")
an1_lbl = QRadioButton("Письменник")
an2_lbl = QRadioButton("Футболіст")
an3_lbl = QRadioButton("Президент")
an4_lbl = QRadioButton("Програміст")


question = QLabel("Який зараз рік?")
bvj1_nb = QRadioButton("2225")
bvj2_nb = QRadioButton("2025")
bvj3_nb = QRadioButton("Поганий")
bvj4_nb = QRadioButton("Новий")


main_line = QVBoxLayout()
main_line.addWidget(text, alignment=Qt.AlignmentFlag.AlignHCenter)


h1 = QHBoxLayout()
h1.addWidget(an1_lbl, alignment=Qt.AlignmentFlag.AlignHCenter)
h1.addWidget(an2_lbl, alignment=Qt.AlignmentFlag.AlignHCenter)

h2 = QHBoxLayout()
h2.addWidget(an3_lbl, alignment=Qt.AlignmentFlag.AlignHCenter)
h2.addWidget(an4_lbl, alignment=Qt.AlignmentFlag.AlignHCenter)

main_line.addLayout(h1)
main_line.addLayout(h2)


main_line.addWidget(question, alignment=Qt.AlignmentFlag.AlignHCenter)


a1 = QHBoxLayout()
a1.addWidget(bvj1_nb, alignment=Qt.AlignmentFlag.AlignHCenter)
a1.addWidget(bvj2_nb, alignment=Qt.AlignmentFlag.AlignHCenter)

a2 = QHBoxLayout()
a2.addWidget(bvj3_nb, alignment=Qt.AlignmentFlag.AlignHCenter)
a2.addWidget(bvj4_nb, alignment=Qt.AlignmentFlag.AlignHCenter)

main_line.addLayout(a1)
main_line.addLayout(a2)


def win_func():
    msg = QMessageBox()
    msg.setText("Ви перемогли!!")
    msg.setWindowTitle("ПЕРЕМОГА!!")
    msg.exec()


an1_lbl.clicked.connect(win_func)
bvj2_nb.clicked.connect(win_func)


window.setLayout(main_line)
window.show()
app.exec()
