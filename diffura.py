import sys
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(726, 571)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit_function = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_function.setGeometry(QtCore.QRect(30, 60, 601, 21))
        self.lineEdit_function.setText("")
        self.lineEdit_function.setObjectName("lineEdit_function")
        self.label_derivative_calculator = QtWidgets.QLabel(self.centralwidget)
        self.label_derivative_calculator.setGeometry(QtCore.QRect(30, 20, 171, 16))
        self.label_derivative_calculator.setObjectName("label_derivative_calculator")
        self.label_diffura_value = QtWidgets.QLabel(self.centralwidget)
        self.label_diffura_value.setGeometry(QtCore.QRect(30, 100, 991, 21))
        self.label_diffura_value.setText("")
        self.label_diffura_value.setObjectName("label_diffura_value")
        self.pushButton_calculate_derivative = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_calculate_derivative.setGeometry(QtCore.QRect(530, 130, 113, 32))
        self.pushButton_calculate_derivative.setObjectName("pushButton_calculate_derivative")
        self.pushButton_info = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_info.setGeometry(QtCore.QRect(630, 30, 51, 32))
        self.pushButton_info.setObjectName("pushButton_info")
        self.label_info = QtWidgets.QLabel(self.centralwidget)
        self.label_info.setGeometry(QtCore.QRect(30, 170, 661, 81))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_info.setFont(font)
        self.label_info.setObjectName("label_info")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_derivative_calculator.setText(_translate("MainWindow", "Калькулятор производной"))
        self.pushButton_calculate_derivative.setText(_translate("MainWindow", "Посчитать"))
        self.pushButton_info.setText(_translate("MainWindow", "info"))
        self.label_info.setText(_translate("MainWindow",
                                           "<html><head/><body><p>В качестве аргумента используйте x,</p><p> вместо корня n-ой степени используйте дробные степени</p></body></html>"))


class Difference(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.number_of_press = 0
        self.label_info.hide()
        self.pushButton_info.clicked.connect(self.press_inf)
        self.pushButton_calculate_derivative.clicked.connect(self.press_calculate)

    def press_inf(self):
        if self.number_of_press % 2 == 0:
            self.label_info.show()
        else:
            self.label_info.hide()
        self.number_of_press += 1

    def press_calculate(self):
        try:
            self.label_diffura_value.setText(derivative(self.lineEdit_function.text()))
        except:
            self.label_diffura_value.setText('🤡?')


def derivative_ymnogit(el1, oper, el2):
    el1, pr_or_not1, nach1 = el1[0], el1[1], el1[2]
    el2, pr_or_not2, nach2 = el2[0], el2[1], el2[2]
    if 'x' not in nach1 and 'x' not in nach2:
        return ['0', 1, f'{nach1} * {nach2}']
    else:
        if pr_or_not1 == 0:
            el1 = derivative_one_element(el1)
            el1, pr_or_not1, nach1 = el1[0], el1[1], el1[2]

        if pr_or_not2 == 0:
            el2 = derivative_one_element(el2)
            el2, pr_or_not2, nach2 = el2[0], el2[1], el2[2]

        if nach1 == '' or el2 == '':
            r1 = ''
        else:
            r1 = f'({nach1})*({el2})'
        if el1 == '' or nach2 == '':
            r2 = ''
        else:
            r2 = f'({el1})*({nach2})'
        if r1 == '':
            proiz = f'{r2}'
        elif r2 == '':
            proiz = f'{r1}'
        else:
            proiz = f'{r1} + {r2}'
        return [proiz, 1, f'({nach1}) * ({nach2})']


def derivative_delit(el1, oper, el2):
    el1, pr_or_not1, nach1 = el1[0], el1[1], el1[2]
    el2, pr_or_not2, nach2 = el2[0], el2[1], el2[2]
    if 'x' not in nach1 and 'x' not in nach2:
        return ['0', 1, f'{nach1} / {nach2}']
    else:
        if pr_or_not1 == 0:
            el1, pr_or_not1, nach1 = derivative_one_element(el1)

        if pr_or_not2 == 0:
            el2, pr_or_not2, nach2 = derivative_one_element(el2)

        if nach1 == '' or el2 == '':
            r2 = ''
        else:
            r2 = f'({nach1})*({el2})'
        if el1 == '' or nach2 == '':
            r1 = ''
        else:
            r1 = f'({el1})*({nach2})'
        if r1 == '':
            proiz = f'(-{r2})/({nach2})^2'
        elif r2 == '':
            proiz = f'({r1})/({nach2})^2'
        else:
            proiz = f'({r1} - {r2})/({nach2})^2'
        return [proiz, 1, f'({nach1}) / ({nach2})']


def derivative_one_element(el1):
    if 'x' not in el1:
        proiz = '0'
    elif 'x' in el1:
        pos_x = el1.find('x')
        virez_chislo = el1[:pos_x]
        if virez_chislo == '-' or virez_chislo == '(-':
            chislo = '(-1)'
        elif virez_chislo != '':
            chislo = virez_chislo
        else:
            chislo = '1'
        proiz = str(chislo)
    else:
        proiz = '0'

    if proiz[0] == '(' and proiz[-1] != ')':
        proiz += ')'
    return [proiz, 1, el1]


def derivative_ln(el1, tek_op, el2):
    el2, pr_or_not2, nach2 = el2[0], el2[1], el2[2]
    if pr_or_not2 == 0:
        el2 = derivative(el2)
    if el2 == '0':
        proiz = f'0'
    else:
        proiz = f'(({el2})/({nach2}))'
    return [proiz, 1, f'ln({nach2})']


def derivative_stepen(el1, oper, el2):
    el1, pr_or_not1, nach1 = el1[0], el1[1], el1[2]
    el2, pr_or_not2, nach2 = el2[0], el2[1], el2[2]

    if (pr_or_not2 == 1 and 'x' in nach2) or ('x' in el2):

        if pr_or_not2 == 0:
            el2, pr_or_not2, nach2 = derivative_one_element(el2)

        if pr_or_not1 == 0:
            el1, pr_or_not1, nach1 = derivative_one_element(el1)
        ln_nach1_proiz = derivative_ln("ln", "%", [el1, pr_or_not1, nach1])
        if ln_nach1_proiz[0] == '0':
            proiz = f'(({nach1})^({nach2})) * ({el2}) * ln({nach1})'
        else:
            proiz = f'(({nach1})^({nach2}))*(({el2}) * ln({nach1}) + {nach2} * ({ln_nach1_proiz[0]}))'
        return [proiz, 1, f'{nach1}^{nach2}']
    else:
        is_skobki = False
        if '(' in el2 and ')' in el2:
            el2 = el2[1:-1]
            is_skobki = True
        if el1 == '-x':
            el1 = '-1x'

        if pr_or_not1 == 1 and 'x' not in el2:
            chislo = int(el2)
            if 'x' not in el1:
                umn = chislo * int(el1)
                proiz = f'{umn}*({nach1})' if chislo - 1 == 1 else f'{umn}*({nach1})^{chislo - 1}'
            else:
                proiz = f'{chislo}*({nach1})*({el1})' if chislo - 1 == 1 else f'{chislo}*({nach1})^{chislo - 1}*({el1})'
        elif el1 == 'x':
            chislo = int(el2)
            if is_skobki:
                new_stepen = '' if int(el2) - 1 == 1 else f'^({int(el2) - 1})'
            else:
                new_stepen = '' if int(el2) - 1 == 1 else f'^{int(el2) - 1}'
            proiz = str(chislo) + 'x' + str(new_stepen)
        elif 'x' in el1:
            pos_x = el1.find('x')
            chislo = int(el1[:pos_x]) * int(el2)
            if is_skobki:
                new_stepen = '' if int(el2) - 1 == 1 else f'^({int(el2) - 1})'
            else:
                new_stepen = '' if int(el2) - 1 == 1 else f'^{int(el2) - 1}'
            proiz = str(chislo) + 'x' + str(new_stepen)
        else:
            proiz = '0'

        return [proiz, 1, f'{nach1}^{nach2}']


def derivative_trigon(el1, oper, el2):
    el1, pr_or_not1, nach1 = el1[0], el1[1], el1[2]
    el2, pr_or_not2, nach2 = el2[0], el2[1], el2[2]

    if pr_or_not2 == 0:
        el2, pr_or_not2, nach2 = derivative_one_element(el2)

    if el1 == 'sin':
        proiz = f'({el2})*cos({nach2})'
    elif el1 == 'cos':
        proiz = f'({el2})*(-sin({nach2}))'
    elif el1 == 'tg':
        proiz = f'({el2})*(sec({nach2})^2)'
    elif el1 == 'ctg':
        proiz = f'({el2})*(-(csc({nach2})^2))'
    elif el1 == 'sec':
        proiz = f'({el2})*(sec({nach2})*tg({nach2}))'
    elif el1 == 'csc':
        proiz = f'({el2})*(-csc({nach2})*ctg({nach2}))'
    elif el1 == 'sinh':
        proiz = f'({el2})*(cosh({nach2}))'
    elif el1 == 'cosh':
        proiz = f'({el2})*(sinh({nach2}))'
    elif el1 == 'tgh':
        proiz = f'({el2})*(csch({nach2})^2)'
    elif el1 == 'ctgh':
        proiz = f'({el2})*(-(sech({nach2})^2))'
    elif el1 == 'sech':
        proiz = f'({el2})*(-sech({nach2})*tgh({nach2}))'
    elif el1 == 'csch':
        proiz = f'({el2})*(-csch({nach2})*ctgh({nach2}))'
    elif el1 == 'arcsin':
        proiz = f'({el2})*(1/(1 - ({nach2})^2)^0.5)'
    elif el1 == 'arccos':
        proiz = f'({el2})*(-1/(1 - ({nach2})^2)^0.5)'
    elif el1 == 'arctg':
        proiz = f'({el2})*(1/(({nach2})^2 + 1))'
    elif el1 == 'arcctg':
        proiz = f'({el2})*(-1/(({nach2})^2 + 1))'
    elif el1 == 'arcsec':
        proiz = f'({el2})*(1/|{nach2}|*(({nach2})^2 - 1)^0.5)'
    elif el1 == 'arccsc':
        proiz = f'({el2})*(-1/|{nach2}|*(({nach2})^2 - 1)^0.5)'
    elif el1 == 'arcsinh':
        proiz = f'({el2})*(1/(({nach2})^2 + 1)^0.5)'
    elif el1 == 'arccosh':
        proiz = f'({el2})*(1/(({nach2} - 1)*({nach2} + 1))^0.5)'
    elif el1 == 'arctgh':
        proiz = f'({el2})*(1/(1 - ({nach2})^2))'
    elif el1 == 'arcctgh':
        proiz = f'({el2})*(1/(1 - ({nach2})^2))'
    elif el1 == 'arcsech':
        proiz = f'({el2})*(-1/{nach2}*(1 - ({nach2})^2)^0.5)'
    elif el1 == 'arccsch':
        proiz = f'({el2})*(-1/({nach2})*(1 + ({nach2})^-2)^0.5)'
    return [proiz, 1, f'{el1}({nach2})']


def derivative_log(el1, oper, el2):
    el1, pr_or_not1, nach1 = el1[0], el1[1], el1[2]
    el2, pr_or_not2, nach2 = el2[0], el2[1], el2[2]

    if pr_or_not2 == 0:
        el2 = derivative(el2)

    proiz = f'({el2})/(({nach2}) * ln({nach1[3:]}))'
    return [proiz, 1, f'{nach1}(nach2)']


def derivative_plus(el1, oper, el2):
    el1, pr_or_not1, nach1 = el1[0], el1[1], el1[2]
    el2, pr_or_not2, nach2 = el2[0], el2[1], el2[2]
    if pr_or_not1 == 0:
        proiz1, pr_or_not1, nach1 = derivative_one_element(el1)
    else:
        proiz1 = el1

    if pr_or_not2 == 0:
        proiz2, pr_or_not2, nach2 = derivative_one_element(el2)
    else:
        proiz2 = el2

    if proiz1 == "":
        return [proiz2, 1, f'{nach1} + {nach2}']
    elif proiz2 == "":
        return [proiz1, 1, f'{nach1} + {nach2}']
    else:
        return [str(proiz1) + ' + ' + str(proiz2), 1, f'{nach1} + {nach2}']


def derivative_minus(el1, oper, el2):
    el1, pr_or_not1, nach1 = el1[0], el1[1], el1[2]
    el2, pr_or_not2, nach2 = el2[0], el2[1], el2[2]
    if pr_or_not1 == 0:
        proiz1, pr_or_not1, nach1 = derivative_one_element(el1)
    else:
        proiz1 = el1

    if pr_or_not2 == 0:
        proiz2, pr_or_not2, nach2 = derivative_one_element(el2)
    else:
        proiz2 = el2

    if proiz1 == "":
        return [f'-{proiz2}', 1, f'{nach1} - {nach2}']
    elif proiz2 == "":
        return [proiz1, 1, f'{nach1} - {nach2}']
    else:
        return [str(proiz1) + ' - ' + str(proiz2), 1, f'{nach1} - {nach2}']


def make_tokens(func):
    function = func.replace(' ', '').replace(':', '/').replace('**', '^')
    tokeni = []
    t = 0
    i = 0
    while i < len(function):
        if function[i:i + 3] == 'log':
            if function[i + 3] == '(':
                k = 1
                for j in range(i + 4, len(function)):
                    if function[j] == '(':
                        k += 1
                    if function[j] == ')':
                        k -= 1
                    if k == 0:
                        tokeni.append(function[i:j + 1])
                        t = j + 1
                        i = j
                        break
        else:
            if function[i] == '-' or function[i] == '+' or function[i] == '*' or function[i] == '/' or function[
                i] == '^' or \
                    function[i] == '(' or function[i] == ')':
                if function[t:i] == "":
                    tokeni.append(function[i])
                else:
                    tokeni.append(function[t:i])
                    tokeni.append(function[i])
                t = i + 1
        i += 1
    if function[t:] != "":
        tokeni.append(''.join(function[t:]))
    if tokeni[0] == '-':
        tokeni.pop(0)
        tokeni[0] = f'-{tokeni[0]}'
    n = 0
    while n < len(tokeni):
        if tokeni[n] == '(' and tokeni[n + 1] == '-':
            tokeni[n + 2] = f'-{tokeni[n + 2]}'
            tokeni.pop(n + 1)
        else:
            n += 1
    return tokeni


def derivative(func):
    tokeni = make_tokens(func)

    prior = {'+': 0, '-': 0, '*': 1, '/': 1, '^': 2, '$': 2, '@': 2, '%': 2, '(': 3, ')': 3}
    elementi = []
    oper = []
    for tok in tokeni:
        if (tok != '(' and tok != ')' and tok != '+' and tok != '-' and
                tok != '*' and tok != '/' and tok != '^'):
            elementi.append([tok, 0, tok])
            if tok == 'sin' or tok == 'cos' or tok == 'tg' or tok == 'ctg' or tok == 'sec' or tok == 'csc' \
                    or tok == 'arcsin' or tok == 'arccos' or tok == 'arctg' or tok == 'arcctg' or tok == 'arcsec' \
                    or tok == 'arccsc' or tok == 'sinh' or tok == 'cosh' or tok == 'tgh' or tok == 'ctgh' \
                    or tok == 'sech' or tok == 'csch' or tok == 'arcsinh' or tok == 'arccosh' or tok == 'arctgh' \
                    or tok == 'arcctgh' or tok == 'arcsech' or tok == 'arccsch':
                oper.append('$')
            if 'log' in tok:
                oper.append('@')
            if 'ln' in tok:
                oper.append('%')
        else:
            if (oper != [] and prior[tok] > prior[oper[-1]]) or oper == [] or oper[-1] == '(':
                oper.append(tok)
            else:
                if oper[-1] == ')':
                    tek_op = oper.pop()
                    tek_op = oper.pop()
                    if tek_op == '(':
                        if '-' in elementi[-1][0]:
                            elementi[-1][0] = f'({elementi[-1][0]})'
                            elementi[-1][-1] = f'({elementi[-1][-1]})'
                        else:
                            elementi[-1][0] = f'{elementi[-1][0]}'
                            elementi[-1][-1] = f'{elementi[-1][-1]}'
                    while tek_op != '(':
                        el2 = elementi.pop()
                        el1 = elementi.pop()
                        if tek_op == '^':
                            rezult = derivative_stepen(el1, tek_op, el2)
                            elementi.append(rezult)
                        elif tek_op == '*':
                            rezult = derivative_ymnogit(el1, tek_op, el2)
                            elementi.append(rezult)
                        elif tek_op == '+':
                            rezult = derivative_plus(el1, tek_op, el2)
                            elementi.append(rezult)
                        elif tek_op == '-':
                            rezult = derivative_minus(el1, tek_op, el2)
                            elementi.append(rezult)
                        elif tek_op == '/':
                            rezult = derivative_delit(el1, tek_op, el2)
                            elementi.append(rezult)
                        elif tek_op == '$':
                            rezult = derivative_trigon(el1, tek_op, el2)
                            elementi.append(rezult)
                        elif tek_op == '@':
                            rezult = derivative_log(el1, tek_op, el2)
                            elementi.append(rezult)
                        elif tek_op == '%':
                            rezult = derivative_ln(el1, tek_op, el2)
                            elementi.append(rezult)
                        tek_op = oper.pop()
                while oper != [] and oper[-1] != '(' and prior[tok] <= prior[oper[-1]]:
                    el2 = elementi.pop()
                    el1 = elementi.pop()
                    tek_op = oper.pop()
                    if tek_op == '^':
                        rezult = derivative_stepen(el1, tek_op, el2)
                        elementi.append(rezult)
                    elif tek_op == '*':
                        rezult = derivative_ymnogit(el1, tek_op, el2)
                        elementi.append(rezult)
                    elif tek_op == '+':
                        rezult = derivative_plus(el1, tek_op, el2)
                        elementi.append(rezult)
                    elif tek_op == '-':
                        rezult = derivative_minus(el1, tek_op, el2)
                        elementi.append(rezult)
                    elif tek_op == '/':
                        rezult = derivative_delit(el1, tek_op, el2)
                        elementi.append(rezult)
                    elif tek_op == '$':
                        rezult = derivative_trigon(el1, tek_op, el2)
                        elementi.append(rezult)
                    elif tek_op == '@':
                        rezult = derivative_log(el1, tek_op, el2)
                        elementi.append(rezult)
                    elif tek_op == '%':
                        rezult = derivative_ln(el1, tek_op, el2)
                        elementi.append(rezult)
                oper.append(tok)
    if oper == []:
        el1 = elementi.pop()
        el1, pr_or_not1, nach1 = el1[0], el1[1], el1[2]
        if el1 == 'x':
            return '1'
        elif 'x' not in el1:
            return '0'
        else:
            pos_x = el1.find('x')
            return el1[:pos_x]
    elif oper[-1] == ')':
        tek_op = oper.pop()
        tek_op = oper.pop()
        if tek_op == '(':
            if '-' in elementi[-1][0]:
                elementi[-1][0] = f'({elementi[-1][0]})'
                elementi[-1][-1] = f'({elementi[-1][-1]})'
            else:
                elementi[-1][0] = f'{elementi[-1][0]}'
                elementi[-1][-1] = f'{elementi[-1][-1]}'

        while tek_op != '(':
            el2 = elementi.pop()
            el1 = elementi.pop()
            if tek_op == '^':
                rezult = derivative_stepen(el1, tek_op, el2)
                elementi.append(rezult)
            elif tek_op == '*':
                rezult = derivative_ymnogit(el1, tek_op, el2)
                elementi.append(rezult)
            elif tek_op == '+':
                rezult = derivative_plus(el1, tek_op, el2)
                elementi.append(rezult)
            elif tek_op == '-':
                rezult = derivative_minus(el1, tek_op, el2)
                elementi.append(rezult)
            elif tek_op == '/':
                rezult = derivative_delit(el1, tek_op, el2)
                elementi.append(rezult)
            elif tek_op == '$':
                rezult = derivative_trigon(el1, tek_op, el2)
                elementi.append(rezult)
            elif tek_op == '@':
                rezult = derivative_log(el1, tek_op, el2)
                elementi.append(rezult)
            elif tek_op == '%':
                rezult = derivative_ln(el1, tek_op, el2)
                elementi.append(rezult)

            tek_op = oper.pop()

    while oper != [] and oper[-1] != '(':
        el2 = elementi.pop()
        el1 = elementi.pop()
        tek_op = oper.pop()
        if tek_op == '^':
            rezult = derivative_stepen(el1, tek_op, el2)
            elementi.append(rezult)
        elif tek_op == '*':
            rezult = derivative_ymnogit(el1, tek_op, el2)
            elementi.append(rezult)
        elif tek_op == '+':
            rezult = derivative_plus(el1, tek_op, el2)
            elementi.append(rezult)
        elif tek_op == '-':
            rezult = derivative_minus(el1, tek_op, el2)
            elementi.append(rezult)
        elif tek_op == '/':
            rezult = derivative_delit(el1, tek_op, el2)
            elementi.append(rezult)
        elif tek_op == '$':
            rezult = derivative_trigon(el1, tek_op, el2)
            elementi.append(rezult)
        elif tek_op == '@':
            rezult = derivative_log(el1, tek_op, el2)
            elementi.append(rezult)
        elif tek_op == '%':
            rezult = derivative_ln(el1, tek_op, el2)
            elementi.append(rezult)
    if elementi[0][1] == 0:
        rezult = derivative_one_element(elementi[0][0])
        elementi.pop()
        elementi.append(rezult)
    return elementi[0][0]


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = Difference()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
