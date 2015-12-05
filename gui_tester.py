import sys
from PyQt4 import QtCore, QtGui, uic
import mnist_loader
import network
import image_parser
import numpy as np
import mnist
import drawer

filename = 'form.ui'

Ui_MainWindow, QtBaseClass = uic.loadUiType(filename)


class MyApp(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.trainButton.clicked.connect(self.trainButtonAction)
        self.loadParamButton.clicked.connect(self.loadData)
        self.saveParamButton.clicked.connect(self.saveData)
        self.testDigitButton.clicked.connect(self.testDigit)
        self.showDigitButton.clicked.connect(self.showDigit)
        self.psDigitTest.clicked.connect(self.testPsDigit)
        self.drawButton.clicked.connect(self.drawDigitAndTest)

        self.training_data, self.validation_data, self.test_data = mnist_loader.load_data_wrapper()
        self.net = network.Network([784, 30, 10])
        self.textEdit.append('Network created.')

    def testDigit(self):
        image_number = int(self.digitNumberEdit.text())
        x = np.argmax(self.net.feedforward(self.test_data[image_number][0]))
        y = self.test_data[image_number][1]
        self.textEdit.append('Network thinks the photo number {0} is {1},'
                             ' right answer is {2}'.format(image_number, x, y))

    def drawDigitAndTest(self):
        drawer.launch()
        user_image = image_parser.load_image(img_name='custom_img.png')
        pr_array = self.net.feedforward(user_image)
        self.textEdit.append('Your drawn digit is considered to be {0}'.format(np.argmax(pr_array)))

    def testPsDigit(self):
        user_image = image_parser.load_image(img_name='image2.png')
        pr_array = self.net.feedforward(user_image)
        self.textEdit.append('Drawn digit in Adobe Photoshop is considered to be {0}'.format(np.argmax(pr_array)))

    def showDigit(self):
        image_number = int(self.digitNumberEdit.text())
        mnist.plot_mnist_digit(np.reshape(self.test_data[image_number][0], (-1, 28)))

    def loadData(self):
        self.textEdit.append('Started loading...')
        self.net.load_parameters()
        self.textEdit.append('Weight and bias parameters loaded.')

    def saveData(self):
        self.textEdit.append('Started saving...')
        self.net.save_parameters()
        self.textEdit.append('Weight and bias parameters saved.')

    def trainButtonAction(self):
        self.textEdit.append('Training started...')
        log_str = self.net.sgd(self.training_data, 1, 10, 3.0, test_data=self.test_data)
        self.textEdit.append(log_str)
        self.textEdit.append('Network has passed training in {0} epochs.'.format(1))


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
