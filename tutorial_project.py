import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg  # Needed so font style and size can be changed


# Define the MainWindow class
class MainWindow(qtw.QWidget):

    # Define an init method
    def __init__(self):

        # Inherit from the base class
        super().__init__()

        # Set the window title
        self.setWindowTitle('Kevin\'s PyQt5 Program')

        # Set up the layout (QV = vertical layout; QH = Horizontal layout)
        self.setLayout(qtw.QVBoxLayout())


# Create a label for the entry box
        test_label1 = qtw.QLabel('Hello unnamed person!!')

        # Change the font style and size
        test_label1.setFont(qtg.QFont('Helvetica', 18))

        # Display the label
        self.layout().addWidget(test_label1)


# Create an entry box
        test_entry = qtw.QLineEdit()

        # Define a name for the object
        test_entry.setObjectName('name_field')

        # setText is what text is in the entry box when the app loads
        test_entry.setText('')

        # Display the entry box
        self.layout().addWidget(test_entry)


# Create a button for the entry box
        test_button1 = qtw.QPushButton('Click Here', clicked=lambda: press_it_entry())

        # Display the button
        self.layout().addWidget(test_button1)


# Create a label for the text box
        test_label2 = qtw.QLabel('Write a little about yourself!!')

        # Change the font style and size
        test_label2.setFont(qtg.QFont('Helvetica', 12))

        # Display the label
        self.layout().addWidget(test_label2)


# Create a text box
        test_textbox = qtw.QTextEdit(self,
#            plainText="> ", # Text that stays in the textbox and does not disapear
            html='<h1>H1 Text</h1>', # This changes plainText to the chars between
                                     # the tags for all text entered in the textbox
            acceptRichText=False, # To Allow rich text to be entered
            lineWrapMode=qtw.QTextEdit.FixedColumnWidth, # For fixed columns
            lineWrapColumnOrWidth=50, # Set the width of the test across each row
            placeholderText='Type Something Here...', # Set placeholder text
            readOnly=False, # False by default(This line can be omitted if false).
            # If set to True the user will not be able to type in the text box
        )


        # Display the entry box
        self.layout().addWidget(test_textbox)


# Create a button for the text box
        test_button2 = qtw.QPushButton('Click Here', clicked=lambda: press_it_textbox())

        # Display the button
        self.layout().addWidget(test_button2)


# Create a label for the combo box
        test_label3 = qtw.QLabel('')

        # Change the font style and size
        test_label3.setFont(qtg.QFont('Helvetica', 12))

        # Display the label
        self.layout().addWidget(test_label3)


# Create a combo box
        test_combo = qtw.QComboBox(
            self,
            editable=True,
#            insertPolicy=qtw.QComboBox.InsertAtBottom#, # Adds item to the bottom of the list
            insertPolicy = qtw.QComboBox.InsertAtTop # Adds item to the top of the list
        )

        # Add items to combo box .addItem('item text', 'item data'(optional))
        test_combo.addItem('First Item', 'dataItem1')
        test_combo.addItem('Second Item', 'dataItem2')
        test_combo.addItem('Third Item', 'dataItem3')
        test_combo.addItem('Fourth Item', 'dataItem4')
        test_combo.addItem('Fifth Item', 'dataItem5')

        combo_list = ['First Combo List Item',
                      'Second Combo List Item',
                      'Third Combo List Item',
                      'Fourth Combo List Item',
                      'Fifth Combo List Item'
                      ]

        # Add items to combo box .addItems(list_of_items)
        test_combo.addItems(combo_list)

        # Insert Items into the combo box .insertItem(position to insert the
        # item, 'item text')
        test_combo.insertItem(10, 'First Inserted Item')

        # Insert Items into the combo box .insertItems(position to insert the
        # list of items, list_of_items)
        test_combo.insertItems(11,
                               [
                                   'First Inserted Array Item',
                                   'Second Inserted Array Item',
                                   'Third Inserted Array Item'])

        # Display combo box
        self.layout().addWidget(test_combo)


# Create a button for the combo box
        test_button3 = qtw.QPushButton('Click Here', clicked=lambda: press_it_combo())

        # Display the button
        self.layout().addWidget(test_button3)


# Create a label for the spin box
        test_label4 = qtw.QLabel('')

        # Change the font style and size
        test_label4.setFont(qtg.QFont('Helvetica', 12))

        # Display the label
        self.layout().addWidget(test_label4)


# Create a spin box
        # For use with integer spin box value
        test_spin = qtw.QSpinBox(

        # For use with double/float spin box values
#        test_spin=qtw.QDoubleSpinBox(
                self,
            value = 50, # The default value
            minimum = 18, # The min value
            maximum = 120, # The max value
            singleStep = 1#, # The number of steps between each value when using the up/down arrows
#            prefix = 'pre ', # Add a prefix to the value displayed in the spinbox
#            suffix = ' suf' # Add a prefix to the value displayed in the spinbox
        )

        # Display the spinbox
        self.layout().addWidget(test_spin)


# Create a button for the spin box
        test_button4 = qtw.QPushButton('Click Here', clicked=lambda: press_it_spin())

        # Display the button
        self.layout().addWidget(test_button4)


        # Display the window
        self.show()

# Define the function to determine what happens when the button for the entry box is clicked
        def press_it_entry():

            # Set the label text equal to the text that was entered into the entry box
            test_label1.setText(f'Hello {test_entry.text()[0].upper()}' +
                                f'{test_entry.text()[1:].lower()}!!')

            # Delete the text that was entered in the entry box since it is no longer needed
            test_entry.setText('')

# Define the function to determine what happens when the button for the entry box is clicked
        def press_it_textbox():

            # Set the label text equal to the text that was entered into the entry box
            test_label2.setText(test_textbox.toPlainText())

            # Set the text that is displayed in the textbox after the button is pressed
            test_textbox.setPlainText('Thank you for submitting your text.')

            # Delete the text that was entered in the entry box since it is no longer needed
#            test_textbox.setText('')

# Define the function to determine what happens when the button for the combo box is clicked
        def press_it_combo():

            # Set the label text equal to the text that was selected from the box
            test_label3.setText(f'You picked {test_combo.currentText()}!!')

            # Other options are:
            # Set the label text equal to the item data that was selected from the combo box
#            test_label2.setText(f'You picked {test_combo.currentData()}!!')

            # Set the label text equal to the index of the combo box item that was selected
#            test_label2.setText(f'You picked {test_combo.currentIndex()}!!')

# Define the function to determine what happens when the button for the combo box is clicked
        def press_it_spin():

            # Set the label text equal to the text that was selected from the box
            test_label4.setText(f'You picked {test_spin.value()}!!')


app = qtw.QApplication([])
mw = MainWindow()

app.exec_()
