# galaxie-curses
Galaxie ncurses API, is a hight level API for ncuses library. The target is Dialog Windows for Print, Browser File, Color selection, like GTK or QT Dialog.
That API is use for Galaxie Applications.

Frist show the exemple file: glxcurses-demo.py

##ProgressBar

ProgressBar — A widget which indicates progress visually

###Functions
    def set_text(self, text):
    
    def get_text(self):
        return self.text

    def set_value(self, percent=0):
        if self.value >= 0:
            self.value = percent
        else:
            self.value = 0

    def get_value(self):
        if self.value >= 0:
            return self.value
        else:
            self.value = 0
            return self.value

    def set_show_text(self, show_text_int):
        self.show_text = show_text_int

    def get_show_text(self):
        return self.show_text

    # Justification: LEFT, RIGHT, CENTER
    def set_justify(self, justification):
        self.justification = justification

    def get_justify(self):
        return self.justification

    # Orientation: HORIZONTAL, VERTICAL
    def set_orientation(self, orientation):
        self.orientation = orientation

    def get_orientation(self):
        return self.orientation

    # PositionType: CENTER, TOP, BOTTOM
    def set_position_type(self, position_type):
        self.position_type = position_type

    def get_position_type(self):
    return self.position_type
