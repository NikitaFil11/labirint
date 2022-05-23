from PyQt5.QtCore import Qt
from PyQt5.QtWiedgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QMassageBox, QRadioBatton

app = QApplication([])
main_win = QWidget()

main_win.setWindowTitle('Определитель победителя')
main_win.move(900,70)
main_win.size(400,200)
main_win.show()

question = QLabel('Сколько деток учится у нас в группе?')
ans1 = QRadioBatton('4')
ans2 = QRadioBatton('6')
ans3 = QRadioBatton('9')
ans4 = QRadioBatton('7')
lineH1 = QHBoxLayout
lineH2 = QHBoxLayout
lineH3 = QHBoxLayout
lineH1.setwidget(question, alignment = Qt.AlignCenter)
lineH2.setWidget(ans1, alignment = Qt.AlignCenter)
lineH2.setWidget(ans2, alignment = Qt.AlignCenter)
lineH3.setWidget(ans3, alignment = Qt.AlignCenter)
lineH3.setWidget(ans4, alignment = Qt.AlignCenter)
lineV1 = QVBoxLayout
lineV1.setLayout(lineH1)
lineV1.setLayout(lineH2)
lineV1.setLayout(lineH3)
main_win.setLayout(lineV1)





main_win.show()
app.exec_()