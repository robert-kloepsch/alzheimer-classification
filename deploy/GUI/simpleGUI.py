# to create APP type: cxfreeze -c "name_of_app.py" --target-dir dist
# navigate to dist folder and type: ./"name_of_app"

import sys
import tensorflow as tf
from PIL import Image
import numpy as np

#from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import (
                            QApplication
                            , QFileDialog
                            , QWidget
                            , QPushButton
                            , QVBoxLayout
                            , QLabel
                            , QMessageBox
                            
)

from PyQt6.QtGui import (
                        QPixmap
)

from PyQt6.QtCore import (
                        Qt
)


class App(QWidget):

    def __init__(self):
        super().__init__()
        self.setFixedSize(300, 350)

        layout = QVBoxLayout()

        self.button1 = QPushButton("Select Tensorflow Model")
        self.button1.clicked.connect(self.getModel)
        layout.addWidget(self.button1)
                
        self.button1 = QPushButton("Select Image")
        self.button1.clicked.connect(self.openFileAndPredict)
        layout.addWidget(self.button1)

        self.picture = QLabel("Please Select an Image")
        self.picture.setAlignment(Qt.AlignmentFlag.AlignCenter) 
        layout.addWidget(self.picture)

        self.prediction = QLabel("")
        self.prediction.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.prediction)

        self.button2 = QPushButton("Close")
        self.button2.clicked.connect(QApplication.instance().quit)
        layout.addWidget(self.button2)

        self.setLayout(layout)
        self.setWindowTitle("Alzheimer's Early Detection")

        self.model = 0

    # massagebox if no model is selected
    def showDialog(self):
        self.msgBox = QMessageBox()
        self.msgBox.setIcon(QMessageBox.Icon.Information)
        self.msgBox.setText("Please first select a Model to load")
        self.msgBox.setWindowTitle("No Model")
        self.msgBox.setStandardButtons(QMessageBox.StandardButton.Ok)
        
        returnValue = self.msgBox.exec()
        if returnValue == QMessageBox.StandardButton.Ok:
            print('OK clicked')
    
    

    #main function - load image
    def openFileAndPredict(self):
        
        if self.model == 0:
            self.showDialog()
            return

        filename, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*)")
        
        # makes pop up -cancel- NOT result in error
        if filename == "":
            return

        self.picture.setPixmap(QPixmap(filename))
        
        #load image and predict
        image = self.load_image(filename)
        pred = self.predict(image, self.model)
        
        #generate output in widget
        self.prediction.setText(self.interpret_pred(pred))

        
    #secondary function - load model
    def getModel(self):
        filename, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*.h5)")

        if filename == "":
            return

        # makes pop up -cancel- NOT result in error
        self.model = load_model(filename)

        return self.model

    #load image function
    def load_image(self, filename):
        
        image = Image.open(filename)
        image = image.convert("RGB")                    #to keep three channels
        image = np.array(image)
        image = image[np.newaxis,:,:,:]

        return image

    #predict function
    def predict(self, image_array, model):

        pred = model.predict(image_array)
    
        return pred

    #interpret prediction output function
    def interpret_pred(self, prediction):
        pred = np.argmax(prediction[0])
        proba = prediction[0][pred]*100
        if pred == 0:
            output="-Healthy-"+"\n"+"Certaintly: "+str(proba)[:6]+"%"
            return str(output)
        if pred == 1:
            output="-Very Mild AD- indications"+"\n"+"Certaintly: "+str(proba)[:6]+"%"
            return str(output)
        if pred == 2:
            output="-Mild AD- indications"+"\n"+"Certaintly: "+str(proba)[:6]+"%"
            return str(output)


#load the model
def load_model(path_to_model):
        model = tf.keras.models.load_model(path_to_model)
        return model

def main():
    app = QApplication([])
    app.setStyle('macos')
    window = App()
    window.show()
    app.exec()

# Create window object
if __name__ == "__main__":
    main()

