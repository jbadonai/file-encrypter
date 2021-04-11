from ui import locker2
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QBasicTimer, Qt
from PyQt5.QtGui import QColor
from cryptography.fernet import Fernet
import os
import  time
import threading


class DragAndDropTextbox(QLineEdit):
    """ This creates a textbox that can accept and process drag and dropped files and folders
           it processed dropped files and folders into a list of file and folders
           output is a list.
       """

    def __init__(self, parent):
        super(DragAndDropTextbox, self).__init__(parent)
        # initialize the text box to accept drag and drop. and set place holder
        self.setAcceptDrops(True)
        self.setPlaceholderText("Drop file here to encrypt/decrypt.")
        self.setAlignment(Qt.AlignHCenter)

    def dragEnterEvent(self, e):
        # check if what is dragged into the text box has a url then accept or reject if not
        if e.mimeData().hasUrls():
            e.accept()
        else:
            e.reject()

    def dropEvent(self, e):
        # get what was dropped as text
        ans = e.mimeData().text()

        #   remove empty spaces at the end of the string by strip method
        #   split the result by newline character
        ans = str(ans).strip().split("\n")

        # create a new list object that will hold the files and folders as a list
        newans = []

        # loop through the string and append the value to the new List that is holding the file and folder
        for x in ans:
            newans.append(str(x)[8:])

        # display the formated list of files and folders dropped to user in the same text box.
        self.setText(str(newans))




class LockerWindow(QMainWindow, locker2.Ui_MainWindow):
    def __init__(self):
        super(LockerWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("JBAdonai File and Folder Locker")
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)

        # create a new text box for drag and drop functionality
        self.inputText = DragAndDropTextbox(self.frame)

        # assign and set timer properties
        self.timer = QBasicTimer()
        self.timer.start(200, self)

        # set variable for password
        self.password = None    # stores user password used to encrypt a file
        self.key = None # stores key used to encrypt file based on users password supplied.

        # set buffer
        self.buffer = 1024 * 1024   # set constant buffer used in encrypting file

        # attached buttons to functions
        self.buttonStart.clicked.connect(self.start_encrypt_decrypt)
        self.buttonClose.clicked.connect(self.exit)
        self.buttonMinimize.clicked.connect(self.minimize)
        self.buttonAbout.clicked.connect(self.about)

        self.message = "Info"   # stores message that informs user what is happening in the program
        self.completed = True  # hold control to check if all running task is completed.

        # progress bar
        self.pbCurrent = 0  # stores current progress bar value
        self.pbTotal = 0    # stores the total value that represents 100% in the progress bar

        self.busy = False   # controls work in progress on a single file
        self.fileList = []  # holds the list of files to be encrypted/decrpted

        self.statusUpdatetrigger = False

        self.inputText.textChanged.connect(self.addListToView)

    def about(self):
        try:
            info = '''Jbadonai Ventures Ltd. 
            \njbadonaiventures@yahoo.com \n+234-809-944-4076,  +234-802-222-4284 \ncopyright 2021.  
            '''

            QMessageBox.information(self, "Jbadonai Ventures", info)

        except Exception as e:
            print(e)

    def closeEvent(self, a0):
        if self.completed is False:
            ans = QMessageBox.question(self, "Exit", "Current Task is yet to be completed. Are you sure you want to exit")
            if ans == QMessageBox.Yes:
                pass
            else:
                a0.ignore()


    def addListToView(self):
        try:
            if self.inputText.text() != "":
                if self.listView.topLevelItemCount() > 0:
                    self.listView.clear()
                mylist = eval(self.inputText.text())
                item = QTreeWidgetItem()
                item.setText(0, "FILE NAME")
                item.setText(1, "STATUS")
                item.setText(2, "FILE LOCATION")
                item.setTextAlignment(0,0)
                item.setTextAlignment(1,0)
                item.setTextAlignment(2,0)
                self.listView.setHeaderItem(item)
                self.listView.setColumnWidth(0, 300)

                for l in mylist:
                    if os.path.isdir(l) is False:
                        item1 = QTreeWidgetItem()
                        item1.setText(0, os.path.split(l)[1].strip())
                        item1.setText(1, "pending...")
                        item1.setText(2, l)
                        self.listView.addTopLevelItem(item1)
                    else:
                        for root, dirs, files in os.walk(l):
                            for file in files:
                                item2 = QTreeWidgetItem()
                                item2.setText(0, file)
                                item2.setText(1, "pending...")
                                item2.setText(2, os.path.abspath(os.path.join(root, file)))
                                self.listView.addTopLevelItem(item2)

                # self.fileList = eval(self.inputText.text())
                # print(f"flist: {self.fileList}")

                self.fileList.clear()
                total = self.listView.topLevelItemCount()
                for counter in range(total):
                    self.fileList.append(self.listView.topLevelItem(counter).text(2))

                self.inputText.setText("")

        except Exception as e:
            print(e)

    def set_status(self, current_item, message, colour='White'):
        try:
            total = self.listView.topLevelItemCount()
            found = None
            i = QTreeWidgetItem()
            for x in range(total):
                item = self.listView.topLevelItem(x)
                # print(current_item, ">>>>>", item.text(0))
                if str(current_item).__contains__(item.text(0)):
                    found = x

                    i.setText(0, item.text(0))
                    i.setText(1, message)
                    i.setForeground(1, QColor(colour))
                    i.setText(2, current_item)
                    break


            if found is not None:
                self.listView.setCurrentItem(self.listView.topLevelItem(found))

                self.listView.takeTopLevelItem(found)
                self.listView.insertTopLevelItem(found, i)


            else:
                print("found is none")

            time.sleep(0.1)
            # print("\t[Set Status] Setting Status Succesful")

        except Exception as e:
            print("set status:", e)

    def set_status2(self, current_item, message, colour='White'):
        self.currentItem = current_item
        self.currentMessage = message
        self.currentColour = colour
        self.statusUpdatetrigger = True

    def exit(self):
        self.close()

    def minimize(self):
        self.setWindowState(Qt.WindowMinimized)

    def set_password(self):
        try:
            ''' COMPLETED '''
            # get a password from input dialog box
            ans, ok = QInputDialog.getText(self, "Password", "Set Encrypting/Decrypting Password\n"
                                                             "Password is required to encrypt or decrypt file. \n",
                                           text='password' )

            # if OK is pressed from the dialog box
            if ok:
                # check if value is supplied.
                if ans != "":
                    # if value is supplied set the password to the value supplied
                    self.password = ans
                else:
                    # if no value is supplied set the password to none
                    self.password = 'password'

            # if CANCEL is pressed from the dialog box
            else:
                # if cancel is pressed se the the password to none
                self.password = None
        except Exception as e:
            print(f"An Error Occurred in 'set_password': {e}")

    def convert(self, size):
        # print("Raw size:", size)
        for s in ['bytes', 'kb', 'mb', 'gb']:
            if size <= 1024:
                # print(f"{size} {s}")
                return f"{size} {s}"
                # break;
            else:
                ans = round((size / 1024), 2)
                size = ans

    def generate_key_from_password(self, password_provided):
        try:
            import base64
            import os
            from cryptography.hazmat.backends import default_backend
            from cryptography.hazmat.primitives import hashes
            from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

            # password_provided = "password"  # This is input in the form of a string
            password = password_provided.encode()  # Convert to type bytes
            # salt = os.urandom(16)  # CHANGE THIS - recommend using a key from os.urandom(16), must be of type bytes
            salt = b'jbadonaiventures'  # CHANGE THIS - recommend using a key from os.urandom(16), must be of type bytes
            kdf = PBKDF2HMAC(
                algorithm=hashes.SHA256(),
                length=32,
                salt=salt,
                iterations=100000,
                backend=default_backend()
            )

            key = base64.urlsafe_b64encode(kdf.derive(password))  # Can only use kdf once

            return key
        except Exception as e:
            print(f"Error Occurred in 'generate_key_from_password' : {e}")

    def timerEvent(self, *args, **kwargs):
        try:
            # position the drag and drop text over the original textbox with no drag and rop function.
            self.inputText.setGeometry(self.textInput.geometry())

            # message centre. always display message
            self.labelInfo.setText(self.message)

            if self.busy is False and self.completed is True:
                self.message = "All Task completed"


            # Progress bar.
            try:
                value = round((self.pbCurrent / self.pbTotal) * 100)
                self.progressBar.setValue(value)
            except Exception as e:
                self.progressBar.setValue(0)
                # print(e)
                pass

            # update list view on the fly when it's triggered.
            if self.statusUpdatetrigger:
                try:
                    found = 0
                    total = self.listView.topLevelItemCount()
                    itemList = []
                    for x in range(total):
                        item = self.listView.topLevelItem(x)
                        if str(self.currentItem).__contains__(item.text(0)):
                            found = x
                            i = QTreeWidgetItem()
                            i.setText(0, item.text(0))
                            i.setText(1, self.currentMessage)
                            i.setForeground(1, QColor(self.currentColour))
                            i.setText(2, self.currentItem)
                            itemList.append(i)
                        else:
                            itemList.append(item)

                    total = self.listView.topLevelItemCount()

                    print(f"total: {total}")
                    for x in range(total):
                        self.listView.takeTopLevelItem(0)

                    try:
                        for i in itemList:
                            one = i.text(0)
                            two = i.text(1)
                            three = i.text(2)

                            items = QTreeWidgetItem()
                            items.setText(0, one)
                            items.setText(1, two)
                            items.setText(2, three)
                            items.setForeground(1, i.foreground(1))
                            self.listView.addTopLevelItem(items)

                        self.listView.setCurrentItem(self.listView.topLevelItem(found))
                    except Exception as e:
                        print(e)

                    # time.sleep(0.1)
                    self.statusUpdatetrigger = False

                except Exception as e:
                    print("error occurred at set status:", e)

        except Exception as e:
            print(f"Error Occurred in 'timerEvent': {e}")

    def start_encrypt_decrypt(self):

        def start():
            try:
                self.completed = False

                # get the list of files to encrypt:
                list = self.fileList # evaluate the string to list
                # start encrypting/decrypting them one after the other.
                for l in list:
                    # a loop to wait for one file to be completed before starting the other.
                    while True:
                        if self.busy is False:
                            self.busy = True
                            break
                        time.sleep(1)

                    # Decide if file need encrypting or decrypting
                    if str(l).__contains__('_jblck'):
                        self.decrypt(l, self.key)
                    else:
                        # check file size to reject any file size greater than 1gb
                        filesize = os.stat(l).st_size
                        size = self.convert(filesize)
                        sizeData = size.split(" ")

                        if sizeData[1] == 'gb':
                            if float(sizeData[0]) > 1:
                                self.message = f"Sorry! File size greater than 1g is not supported for now"
                                # print(f"File size greater than 1G not supported.")
                            else:
                                self.encrypt(l, self.key)
                        if sizeData[1] in ['bytes', 'kb', 'mb']:
                            self.encrypt(l, self.key)

                while True:
                    # print("checking if completed...")
                    if self.busy is False:
                        # print("completed")
                        self.completed = True
                        break
                    time.sleep(1)


            except Exception as e:
                self.completed = True
                print(f"Error occured in 'start-encrypt-decrypt': \n {e}")
        # this checks if encryption/decryption is not in progress and act accordingly
        if self.completed is True:
            # this conidtion test if no file was specified before asking the programm to start encryting/decrypting.
            if self.listView.topLevelItemCount() > 0:
                # set the password. user to set the password to be used in encrypting the file
                self.set_password()

                # set the encrypting key base on the password provided by user above
                if self.password is not None:
                    # set the encrypting key base on the password supplied
                    self.key = self.generate_key_from_password(self.password)
                    time.sleep(1)

                    t = threading.Thread(target=start)
                    t.daemon = True
                    t.start()

                else:
                    # if user did not use any password. set the default password to 'password'
                    # self.key = self.generate_key_from_password("password")
                    self.message = "Operation canceled by user"
                    QMessageBox.information(self, "jbAdonai Ventures - Canceled.", "Operation Canceled by user")
            else:
                QMessageBox.critical(self, "jbAdonai Ventures - No data", "No file to encrypt, Please drag and drop file you want to encrypt/decrypt into the provided space, and then try again.")
        else:
            self.message = "Please wait for current task to be completed."
            QMessageBox.information(self, "jbAdonai Ventures - Busy", "Please wait for current task(s) to be completed.")

    def encrypt(self, filename, key):
        def start():
            try:
                self.set_status2(filename, 'Encrypting...!', colour='yellow')
                time.sleep(0.2)
                self.busy = True
                # read the files in bits with buffer (fixed size) and add the bits to list
                byteList = []

                # stores the encrypted bytes before writing to file
                encList = []

                # open the file and read as bytes using the buffer
                print("Loading file as byte into list")
                self.message = "Loading files into memory. Please wait..."
                counter = 0
                # set progress bar data
                totalsize = os.stat(filename).st_size
                self.pbTotal = totalsize
                self.pbCurrent = 0
                try:
                    with open(filename, 'rb') as f:
                        # read the first buffer
                        buffer = f.read(self.buffer)
                        self.pbCurrent += len(buffer)
                        # continue reading buffer until there is none left
                        while len(buffer) > 0:
                            counter += 1
                            # print(counter, ":", len(buffer), len(byteList))
                            byteList.append(buffer)
                            buffer = f.read(self.buffer)
                            self.pbCurrent += len(buffer)
                except Exception as e:
                    print(f"Error while loading data: \n {e}")
                    raise Exception
                self.pbCurrent = self.pbTotal
                # Encrypt the buffer list and store it in encrypted byte list
                # set the encrypting key first

                print("encrypting the bytes...")
                self.message = "Encrypting the loaded file. Please wait..."
                f = Fernet(key)

                # setting progress bar values for encrypting
                self.pbTotal = len(byteList)
                self.pbCurrent = 0
                counters = 0
                # using while loop to remove used data from a list to save memory
                while len(byteList) > 0:
                    counters += 1
                    b = byteList[0]
                    enc = f.encrypt(b)
                    encList.append(enc)
                    byteList.pop(0)
                    self.pbCurrent = counters

                self.pbCurrent = self.pbTotal


                # change the filename for the ecyrypted file
                file = os.path.splitext(filename)
                fname = file[0]
                extension = file[1]
                fname = f"{fname}_jblck{extension}"

                print("Writing the encrypted data")
                self.message = "Writing encrypted data to file. Please wait..."
                # write the encrypted data in encList to file

                # setting progress bar values for encrypting
                self.pbTotal = len(encList)
                self.pbCurrent = 0
                with open(fname, 'a') as e:
                    for index, data in enumerate(encList):
                        decoded = f"{data.decode()}\n"
                        e.write(decoded)
                        self.pbCurrent = index

                self.pbCurrent = self.pbTotal
                self.set_status2(filename, 'COMPLETED!', colour='light green')
                time.sleep(0.2)
                print("encrypting completed")
                self.message = "Current file encrypted Successfully!"
                print("_______________________________________")

                # self.run_function(self.set_status, False, filename, "Completed", 'light green')

                try:
                    os.remove(filename)
                except Exception as e:
                    print(e)
                    raise Exception

                # clean up memory usage
                encList.clear()
                byteList.clear()

                self.busy = False
                time.sleep(0.2)
                if self.completed:
                    print(" I was here:::")
                    self.message = "All tasks completed."

            except Exception as e:
                self.busy = False
                print(f"An Error occurred in 'encrypt': {e}")

        t = threading.Thread(target=start)
        t.daemon = True
        t.start()

    def decrypt(self, filename, key):
        def start():
            try:
                self.set_status2(filename, 'Decrypting...!', colour='yellow')
                time.sleep(0.2)
                decryptionError = False
                self.busy = True
                # retrieve data and store them enclist
                encList = []

                # list in bytes i.e not ecrypted ready to write mode
                byteList = []


                # Open encrypted file not as byte (bytes was decoded to string and \n added when saving)
                self.message = "Loading file to decrypt into memory. Please wait..."

                self.pbTotal = os.stat(filename).st_size
                self.pbCurrent = 0
                with open(filename, 'r') as f:
                    while True:
                        # continue reading until end of line
                        data = f.readline()
                        self.pbCurrent += len(data.encode())
                        if not data:
                            break
                        else:
                            # if not end of line add each line to encrypted data list (which was decoded)
                            encList.append(data)
                self.pbCurrent = self.pbTotal

                # decrypt the data
                # set the decrypting key
                f = Fernet(key)

                # scan through the encrypted list, convert each to byte from string (encode it because it was decoded during saving)
                # decrypt

                self.pbTotal = len(encList)
                self.pbCurrent = 0
                counters = 0

                self.message = "Decrypting file. Please wait..."
                while len(encList) > 0:
                    counters += 1
                    e = encList[0]
                    try:
                        d = f.decrypt(e.encode())
                    except Exception as e:
                        decryptionError = True
                        raise Exception
                    byteList.append(d)

                    # update progress bar
                    self.pbCurrent = counters

                    # free memory
                    encList.pop(0)


                self.pbCurrent = self.pbTotal
                # change the filename for the ecyrypted file
                file = os.path.splitext(filename)
                fname = file[0]
                extension = file[1]
                fname = fname.replace("_jblck", "")
                fname = f"{fname}{extension}"

                # write the decrypted data to file
                self.message = 'Writing decrypted data to file. Please wait...'

                self.pbTotal = len(byteList)
                self.pbCurrent = 0

                with open(fname, 'wb') as dec:
                    for index, x in enumerate(byteList):
                        # write the decrypted data to file
                        dec.write(x)
                        # update progress bar
                        self.pbCurrent = index
                self.pbCurrent = self.pbTotal
                self.set_status2(filename, 'COMPLETED', colour='light green')
                time.sleep(0.2)
                print("decrypting completed")
                print("-----------------------------------------------------------")
                self.message = "Current file Decrypted successfully!"


                # self.run_function(self.set_status,False, filename, "Completed",'light green')

                try:
                    os.remove(filename)
                except Exception as e:
                    print(e)
                    raise Exception

                # free memory
                encList.clear()
                byteList.clear()

                self.busy = False
                if self.completed:
                    self.message = "All tasks completed."


            except Exception as e:
                self.busy = False
                if decryptionError:
                    self.set_status2(filename, 'ERROR!', colour='orange')
                    self.message = "Unable to decrypt. Make sure to use right password and try again."
                else:
                    self.message= "An unknown error occurred."
                print(f"An Error occurred in 'decrypt': {e}")

        t = threading.Thread(target=start)
        t.daemon = True
        t.start()

    def keyPressEvent(self, e):
        pass
        # **********************************
        # try:
        #     if e.key() == int(Qt.Key_Enter) - 1:
        #         self.login()
        # except Exception as e:
        #     QMessageBox.critical(self, "Login Error", f"An Error Occured. Please see the details below:\n {e}")

    def mousePressEvent(self, e):
        self.mousedown = True
        self.posX = e.x()
        self.posY = e.y()

    def mouseMoveEvent(self, e):
        try:
            dx = e.x() - self.posX
            dy = e.y() - self.posY

            left = self.pos().x() + dx
            top = self.pos().y() + dy

            self.move(left, top)

        except Exception as e:
            print(e)

    def run_function(self, functionName, join = False, *args):
        t = threading.Thread(target=functionName, args=args)
        t.daemon = True
        t.start()


if __name__ == '__main__':
    app = QApplication([])
    app.setStyle('fusion')

    win = LockerWindow()
    win.show()

    app.exec()
