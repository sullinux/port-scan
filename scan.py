import sys
import time
import socket
from PySide2 import *
from qt_material import *
from ui_portscan import *
# list = {
#             "20": "File Transfer Protocol (FTP) Data Transfer",
#             "21": "File Transfer Protocol (FTP) Command Control",
#             "22": "Secure Shell (SSH)",
#             "23": "Telnet - Remote login service, unencrypted text messages",
#             "25": "Simple Mail Transfer Protocol (SMTP) E-mail Routing",
#             "53": "Domain Name System (DNS) service",
#             "80": "Hypertext Transfer Protocol (HTTP) used in World Wide Web",
#             "110": "Post Office Protocol (POP3) used by e-mail clients to retrieve e-mail from a server",
#             "119": "Network News Transfer Protocol (NNTP)",
#             "123": "Network Time Protocol (NTP)",
#             "143": "Internet Message Access Protocol (IMAP) Management of Digital Mail",
#             "161": "Simple Network Management Protocol (SNMP)",
#             "194": "Internet Relay Chat (IRC)",
#             "443": "HTTP Secure (HTTPS) HTTP over TLS/SSL",
# }

class PostScan(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()
        self.btn()

    def btn(self):
        self.ui.btn_scan.clicked.connect(self.get_target)

    def get_target(self):
        self.ui.textBrowser.clear()
        self.ui.btn_scan.setEnabled(False)
        self.ui.maximum.setEnabled(False)
        self.ui.minimum.setEnabled(False)
        self.ui.lineEdit.setEnabled(False)
        self.ui.textBrowser.clear()
        target = self.ui.lineEdit.text().lower().strip()
        mimimum = self.ui.minimum.text()
        maximum = self.ui.maximum.text()
        ports = []
        openPorts = []
        portslist = [21,25,22,23,80,443,53]
        print(f'Scanning Running From Port - {mimimum} To {maximum} Port Please Wait ...')
        if mimimum > maximum:
            self.show_info("Minimum is bigger than maximum. Please check the values.","Port Scan")
            return
        self.ui.progressBar.setMinimum(int(mimimum))
        self.ui.progressBar.setMaximum(int(maximum))
        for i in range(int(mimimum),int(maximum)+1):
            ports.append(i)
        QApplication.processEvents()
        while True:
            time.sleep(0.05)
            self.ui.textBrowser.append(f'Port Scanning By Sullinux.com Feel Free to visit us ... \n')
            self.ui.textBrowser.append(f'Scanning Running From Port - {mimimum} To {maximum} Port Please Wait ... \n')
            self.statusBar().showMessage("Scanning running")
            for port in ports:

                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(1)
                if not sock.connect_ex((target, port)):
                    print(f'{port} is open')
                    # if port in portslist_info: ### searching in portlist

                    if port == 21:
                        self.ui.textBrowser.append(f'port {port} File Transfer Protocol (FTP) Data Transfer \n')
                    if port == 25:
                        self.ui.textBrowser.append(f'port {port} Simple Mail Transfer Protocol (SMTP) E-mail Routing \n')
                    if port == 80:
                        self.ui.textBrowser.append(f'port {port} Hypertext Transfer Protocol (HTTP) used in World Wide Web \n')
                    if port == 443:
                        self.ui.textBrowser.append(f'port {port} HTTP Secure (HTTPS) HTTP over TLS/SSL \n')
                    if port == 53:
                        self.ui.textBrowser.append(f'port {port} Domain Name System (DNS) service \n')
                    if port not in portslist:
                        self.ui.textBrowser.append(f'port {port} Is Open - unknown  \n')

                    else:
                        pass

                    # self.ui.textBrowser.append(f'port {port} Is Open - unknown  \n')
                    self.statusBar().showMessage(f'{port} is open')
                    self.statusBar().showMessage("Scanning running")
                else:
                    # openPorts.append(port)
                    # print("Port %s is close" % port)
                    # sock.close()
                    pass
                sock.close()
                value = port
                self.ui.progressBar.setValue(value)
                QApplication.processEvents()
            self.ui.btn_scan.setEnabled(True)
            self.ui.maximum.setEnabled(True)
            self.ui.minimum.setEnabled(True)
            self.ui.lineEdit.setEnabled(True)
            self.ui.textBrowser.append(f'Scanning finished')
            self.statusBar().showMessage("Scanning finished")
            self.show_info("Scanning finished.","Port Scan")
            break



    def show_info(self,e,title):
        msgBox = QMessageBox()
        msgBox.setWindowTitle(title)
        msgBox.setText(str(e))
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.exec_()




def main():
    app = QApplication(sys.argv)
    apply_stylesheet(app, theme='dark_yellow.xml')
    window = PostScan()
    window.show()
    app.exec_()
if __name__ == '__main__':
    main()
