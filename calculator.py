from PyQt5 import QtWidgets
from interface import Ui_MainWindow
"Tasarımımızı kullanabilmek için PyQt5 kütüphanemizden özellikleri içeri aktardık. Bunu oluşturduğumuz dosya içinde yaptık."

class Interface(QtWidgets.QMainWindow, Ui_MainWindow):
    "Verilen değişkenin sebebi girilen sayıları hafıza tutulma amacıyla"
    firstNumber = None
    lastNumber = False

    "QtWidgets içinden QMainWindowu alarak ve interface dosyamızdaki Ui_MainWindow'un özelliklerini dahil ettik."
    def __init__(self):
        "super ile üst sınıfın özelliklerini almasını sağladım."
        super().__init__()
        "nesnemizi setupUi ile nesnemizin kendisini yolladık"
        self.setupUi(self)
        "show komutu ile nesnemizi çağırdığımızda görünmesini sağladık"
        self.show()

        "Rakam butonlarının etkileşimini sağlamak"
        self.pushButton_0.clicked.connect(self.printing_numbers)
        self.pushButton_1.clicked.connect(self.printing_numbers)
        self.pushButton_2.clicked.connect(self.printing_numbers)
        self.pushButton_3.clicked.connect(self.printing_numbers)
        self.pushButton_4.clicked.connect(self.printing_numbers)
        self.pushButton_5.clicked.connect(self.printing_numbers)  # clicked = tıklama olduğunda connect ile sinyali fonksiyonumuza gönderesi
        self.pushButton_6.clicked.connect(self.printing_numbers)
        self.pushButton_7.clicked.connect(self.printing_numbers)
        self.pushButton_8.clicked.connect(self.printing_numbers)
        self.pushButton_9.clicked.connect(self.printing_numbers)

        "Nokta Butonunun Etkileşimini Sağlamak"
        self.pushButton_dot.clicked.connect(self.decimal)

        "Sembollerin Etkileşimini sağlamak"
        self.pushButton_plus.clicked.connect(self.operations)
        self.pushButton_subtraction.clicked.connect(self.operations)
        self.pushButton_slash.clicked.connect(self.operations)
        self.pushButton_multiplication.clicked.connect(self.operations)

        self.pushButton_plus.setCheckable(True)
        self.pushButton_subtraction.setCheckable(True) 
        self.pushButton_slash.setCheckable(True)
        self.pushButton_multiplication.setCheckable(True)

        "İşaret Butonu Etkileşimi"
        self.pushButton_clear_plasOrNegative.clicked.connect(self.negative)

        "Eşittir Butonu Etkileşimi"
        self.pushButton_result.clicked.connect(self.result)
        self.pushButton_result.setCheckable(True)

        "Temizleme Butonu Etkileşimi"
        self.pushButton_clear.clicked.connect(self.clear)

    "Her hangi bir rakama basıldığında çalışacak olan fonksiyon"
    def printing_numbers(self):
        btn = self.sender() #Hangi butona tıkladığını bilmek adına

        "Ekrandaki değere sayı ekleyebilmemiz ve işlemi devam ettirebilmemiz için ikinci sayı ve eşittir butonu kontrolü sağladık"
        if ((self.lastNumber) and (self.pushButton_result.isChecked())):
            self.label.setText(format(float(btn.text()), '.15g'))
            self.lastNumber = True #ikinci sayılar girilebilmesi için
            self.pushButton_result.setChecked(False) #tekrar işlem yapılabilir hala geçirebilmek içinm

        elif ((self.pushButton_plus.isChecked() or self.pushButton_subtraction.isChecked() 
            or self.pushButton_multiplication.isChecked() or self.pushButton_slash.isChecked()) and (not self.lastNumber)):
            
            self.label.setText(format(float(btn.text()),'.15g'))
            self.lastNumber = True

        else:
            if(('.' in self.label.text() and btn.text() == "0")):
                self.label.setText(format(float(self.label.text() + btn.text()),'.15'))
            else : 
                self.label.setText(format(float(self.label.text() + btn.text()),'.15g'))
                

    "Nokta butonu için kullanılan fonksiyon"
    def decimal(self):
        self.label.setText(self.label.text() + '.') #bitmedi

    "Sayıyı negatif yaparken çalışacak fonksiyon"
    def negative(self):
        btn = self.sender()

        value = float(self.label.text())
        btn.text()=="+/-"
        value = value * -1


        self.label.setText(format(value, '.15g'))

    "Sembollerimizin fonksiyonu"
    def operations(self):
        btn = self.sender()
        self.firstNumber = float(self.label.text())
        btn.setChecked(True)

    "Eşittir butonu"
    def result(self):
        lastNumber = float(self.label.text())

        """Eşittir butonuna işaretlerimizin görevini verme sebebimiz hesap makinesinde
        girilen değerlerin ve belirtilen butonların görevini ekrana yansıtmasıdır."""

        if self.pushButton_plus.isChecked():
            newValue = self.firstNumber + lastNumber
            self.label.setText(format(newValue, '.15g'))
            self.pushButton_plus.setChecked(False)

        elif self.pushButton_subtraction.isChecked():
            newValue = self.firstNumber - lastNumber
            self.label.setText(format(newValue, '.15g'))
            self.pushButton_subtraction.setChecked(False)
        
        elif self.pushButton_slash.isChecked():
            newValue = self.firstNumber / lastNumber
            self.label.setText(format(newValue, '.15g'))
            self.pushButton_slash.setChecked(False)

        elif self.pushButton_multiplication.isChecked():
            newValue = self.firstNumber * lastNumber
            self.label.setText(format(newValue, '.15g'))
            self.pushButton_multiplication.setChecked(False)    
        
        self.firstNumber = newValue

    "Temizleme butonu"
    def clear(self):
        self.firstNumber = 0
        self.lastNumber = False
        self.label.setText("0")
        "Bir önceki işlemden hiçbir detayın kalmaması için yaptık"
        self.pushButton_plus.setChecked(False)
        self.pushButton_multiplication.setChecked(False)
        self.pushButton_slash.setChecked(False)
        self.pushButton_subtraction.setChecked(False)
        self.pushButton_result.setChecked(False)
