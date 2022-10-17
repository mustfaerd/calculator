import sys
from PyQt5.QtWidgets import QApplication
"kütüphaneler içinden QApplicationu dahil ettik"
from calculator import Interface
"calculator dosyamızın içine Interfaceyi dahil ederek sınıfı çektik"

application = QApplication(sys.argv)
"sistem argümanlarımızı çağırdık"

calculator = Interface()
"değişkenimize Interface atadık"

sys.exit(application.exec())
"sys modülüne exit metodunu vererek program açıldığında kapanmaması için exec fonksiyonunu verdik"
