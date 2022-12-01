########################################################################
# COMPONENT:
#    MESSAGES
# Author:
#    Br. Helfrich, Kyle Mueller, Paul Anderson
# Summary: 
#    This class stores the notion of a collection of messages
########################################################################

import control, message

##################################################
# MESSAGES
# The collection of high-tech messages
##################################################
class Messages:

    ##################################################
    # MESSAGES CONSTRUCTOR
    # Read a file to fill the messages
    ##################################################
    def __init__(self, filename):
        self._messages = []
        self._read_messages(filename)

    ##################################################
    # MESSAGES :: DISPLAY
    # Display the list of messages
    ################################################## 
    def display(self, subject_level):
        for m in self._messages:
            if control.securityConditionRead(m._control_level, subject_level):
                m.display_properties()

    ##################################################
    # MESSAGES :: SHOW
    # Show a single message
    ################################################## 
    def show(self, id, subject_level):
        for m in self._messages:
            if m.get_id() == id:
                if control.securityConditionRead(m._control_level, subject_level):
                    m.display_text()
                    return True
                else:
                    print("403: Access Denied.")
        return False

    ##################################################
    # MESSAGES :: UPDATE
    # Update a single message
    ################################################## 
    def update(self, id, text, subject_level):
        for m in self._messages:
            if m.get_id() == id:
                if control.securityConditionWrite(m._control_level, subject_level):
                    m.update_text(text)
                else:
                    print("403: Access Denied.")

    ##################################################
    # MESSAGES :: REMOVE
    # Remove a single message
    ################################################## 
    def remove(self, id, subject_level):
        for m in self._messages:
            if m.get_id() == id:
                if control.securityConditionWrite(m._control_level, subject_level):
                    m.clear()
                else:
                    print("403: Access Denied.")

    ##################################################
    # MESSAGES :: ADD
    # Add a new message
    ################################################## 
    def add(self, text, author, date, subject_level):
        m = message.Message(text, author, date, subject_level)
        if control.securityConditionWrite(m._control_level, subject_level):
            self._messages.append(m)
        else:
            print("403: Access Denied.")

    ##################################################
    # MESSAGES :: READ MESSAGES
    # Read messages from a file
    ################################################## 
    def _read_messages(self, filename):
        try:
            with open(filename, "r") as f:
                for line in f:
                    text_control, author, date, text = line.split('|')
                    self.add(text.rstrip('\r\n'), author, date, text_control)

        except FileNotFoundError:
            print(f"ERROR! Unable to open file \"{filename}\"")
            return
