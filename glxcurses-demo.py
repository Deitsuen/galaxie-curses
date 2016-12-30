#!/usr/bin/env python
# -*- coding: utf-8 -*-
import GLXCurses
import sys
import curses
import logging

from random import randint

# It script it publish under GNU GENERAL PUBLIC LICENSE
# http://www.gnu.org/licenses/gpl-3.0.en.html
# Author: Jérôme ORNECH alias "Tuux" <tuxa@rtnp.org> all rights reserved
__author__ = 'Tuux'

if __name__ == '__main__':
    logging.basicConfig(filename='/tmp/galaxie-curses.log',
                        level=logging.DEBUG,
                        format='%(asctime)s, %(levelname)s, %(message)s')
    logging.info('Started glxcurses-demo')


    # Create the main Application
    app = GLXCurses.Application()
    app.set_name('Galaxie-Curse Demo')

    # Create a Menu
    menu = GLXCurses.MenuModel()
    menu.app_info_label = app.get_name()

    # Create a Window
    win1 = GLXCurses.Window()
    # win_main.set_title('My super Window 1')

    # Create a Window
    frame_for_progressbar = GLXCurses.Frame()
    frame_for_progressbar.set_label('Progress Bar Widget')
    frame_for_progressbar.override_background_color('CYAN')

    # Create a Window
    frame_for_labels = GLXCurses.Frame()
    frame_for_labels.set_label('Label Widget')

    # Create a Label
    label1 = GLXCurses.Label()
    #qlabel1.set_justify('RIGHT')
    label1.set_text('RED WITH BACKGROUND GREEN')
    label1.override_color('RED')
    #label1.override_background_color('GREEN')
    label1.set_line_wrap_mode('WRAP_CHAR')
    label1.set_text('How does it work?\n'
                    '   Well, the reduce\n'
                    '* A Quick Guide to GPLv3\n'
                    '* Why Upgrade to GPLv3\n'
                    '* Frequently Asked Questions about the GNU licenses\n'
                    '* How to use GNU licenses for your own software\n'
                    '* Translations of the GPL\n'
                    '* The GPL in other formats: plain text, Texinfo, LaTeX, standalone HTML, ODF, Docbook v4 or v5, Markdown, and RTF\n'
                    '* GPLv3 logos to use with your project\n'
                    '* Old versions of the GNU GPL\n'
                    '* What to do if you see a possible GPL violation\n'
                    )


    label2 = GLXCurses.Label()
    #label2.set_justify('CENTER')
    label2.set_text('How does it work?\n'
                    '   Well, the reduce\n'
                    '* A Quick Guide to GPLv3\n'
                    '* Why Upgrade to GPLv3\n'
                    '* Frequently Asked Questions about the GNU licenses\n'
                    '* How to use GNU licenses for your own software\n'
                    '* Translations of the GPL\n'
                    '* The GPL in other formats: plain text, Texinfo, LaTeX, standalone HTML, ODF, Docbook v4 or v5, Markdown, and RTF\n'
                    '* GPLv3 logos to use with your project\n'
                    '* Old versions of the GNU GPL\n'
                    '* What to do if you see a possible GPL violation\n'
                    )
    label2.override_color('YELLOW')
    label2.set_line_wrap(True)
    label2.set_max_width_chars(-1)

    label3 = GLXCurses.Label()
    label3.set_alignment(0.5, 1.0)
    #label3.set_justify('RIGHT')
    label3.set_text_with_mnemonic('CY_AN WITH BACKGROUND NORMAL')
    label3.override_color('CYAN')
    label3.set_single_line_mode(1)
    label3.set_max_width_chars(10)

    progressbar1 = GLXCurses.ProgressBar()
    progressbar1.set_spacing(0)
    progressbar1.set_value(randint(0, 100))
    value = '{0:}{1:}'.format(progressbar1.get_value(), '%')
    progressbar1.set_text(value)
    progressbar1.set_show_text(1)
    progressbar1.set_position_type('BOTTOM')
    progressbar1.set_justify('CENTER')
    progressbar1.set_orientation('VERTICAL')
    progressbar1.set_inverted(0)

    progressbar2 = GLXCurses.ProgressBar()
    progressbar2.set_spacing(0)
    progressbar2.set_value(randint(0, 100))
    value = '{0:}{1:}'.format(progressbar2.get_value(), '%')
    progressbar2.set_text(value)
    progressbar2.set_show_text(1)
    progressbar2.set_position_type('CENTER')
    progressbar2.set_justify('CENTER')
    progressbar2.set_orientation('VERTICAL')
    progressbar2.set_inverted(0)

    progressbar3 = GLXCurses.ProgressBar()
    progressbar3.set_spacing(0)
    progressbar3.set_value(randint(0, 100))
    value = '{0:}{1:}'.format(progressbar3.get_value(), '%')
    progressbar3.set_text(value)
    progressbar3.set_show_text(1)
    progressbar3.set_position_type('TOP')
    progressbar3.set_justify('CENTER')
    progressbar3.set_orientation('VERTICAL')
    progressbar3.set_inverted(0)

    progressbar4 = GLXCurses.ProgressBar()
    progressbar4.set_spacing(0)
    progressbar4.set_value(randint(0, 100))
    value = '{0:}{1:}'.format(progressbar4.get_value(), '%')
    progressbar4.set_text(value)
    progressbar4.set_show_text(1)
    progressbar4.set_position_type('TOP')
    progressbar4.set_justify('CENTER')
    progressbar4.set_orientation('VERTICAL')
    progressbar4.set_inverted(1)

    progressbar5 = GLXCurses.ProgressBar()
    progressbar5.set_spacing(0)
    progressbar5.set_value(randint(0, 100))
    value = '{0:}{1:}'.format(progressbar5.get_value(), '%')
    progressbar5.set_text(value)
    progressbar5.set_show_text(1)
    progressbar5.set_position_type('CENTER')
    progressbar5.set_justify('CENTER')
    progressbar5.set_orientation('VERTICAL')
    progressbar5.set_inverted(1)

    progressbar6 = GLXCurses.ProgressBar()
    progressbar6.set_spacing(0)
    progressbar6.set_value(randint(0, 100))
    value = '{0:}{1:}'.format(progressbar6.get_value(), '%')
    progressbar6.set_text(value)
    progressbar6.set_show_text(1)
    progressbar6.set_position_type('BOTTOM')
    progressbar6.set_justify('CENTER')
    progressbar6.set_orientation('VERTICAL')
    progressbar6.set_inverted(1)

    progressbar7 = GLXCurses.ProgressBar()
    progressbar7.set_spacing(0)
    progressbar7.set_value(randint(0, 100))
    value = '{0:}{1:}'.format(progressbar7.get_value(), '%')
    progressbar7.set_text(value)
    progressbar7.set_show_text(1)
    progressbar7.set_position_type('CENTER')
    progressbar7.set_justify('CENTER')
    progressbar7.set_orientation('HORIZONTAL')
    progressbar7.set_inverted(0)

    progressbar8 = GLXCurses.ProgressBar()
    progressbar8.set_spacing(0)
    progressbar8.set_value(randint(0, 100))
    value = '{0:}{1:}'.format(progressbar8.get_value(), '%')
    progressbar8.set_text(value)
    progressbar8.set_show_text(1)
    progressbar8.set_position_type('CENTER')
    progressbar8.set_justify('CENTER')
    progressbar8.set_orientation('HORIZONTAL')
    progressbar8.set_inverted(0)

    progressbar9 = GLXCurses.ProgressBar()
    progressbar9.set_spacing(0)
    progressbar9.set_value(randint(0, 100))
    value = '{0:}{1:}'.format(progressbar9.get_value(), '%')
    progressbar9.set_text(value)
    progressbar9.set_show_text(1)
    progressbar9.set_position_type('CENTER')
    progressbar9.set_justify('CENTER')
    progressbar9.set_orientation('HORIZONTAL')
    progressbar9.set_inverted(0)

    progressbar10 = GLXCurses.ProgressBar()
    pgb_handler = GLXCurses.ProgressBarHandler(progressbar10)

    progressbar10.set_spacing(0)
    progressbar10.set_value(0)
    value = '{0:}{1:}'.format(progressbar10.get_value(), '%')
    progressbar10.set_text(value)
    progressbar10.set_show_text(1)
    progressbar10.set_position_type('CENTER')
    progressbar10.set_justify('CENTER')
    progressbar10.set_orientation('HORIZONTAL')
    progressbar10.set_inverted(1)

    progressbar11 = GLXCurses.ProgressBar()
    progressbar11.set_spacing(0)
    progressbar11.set_value(randint(0, 100))
    value = '{0:}{1:}'.format(progressbar11.get_value(), '%')
    progressbar11.set_text(value)
    progressbar11.set_show_text(1)
    progressbar11.set_position_type('CENTER')
    progressbar11.set_justify('CENTER')
    progressbar11.set_orientation('HORIZONTAL')
    progressbar11.set_inverted(1)

    progressbar12 = GLXCurses.ProgressBar()
    progressbar12.set_spacing(0)
    progressbar12.set_value(randint(0, 100))
    value = '{0:}{1:}'.format(progressbar12.get_value(), '%')
    progressbar12.set_text(value)
    progressbar12.set_show_text(1)
    progressbar12.set_position_type('CENTER')
    progressbar12.set_justify('left')
    progressbar12.set_orientation('HORIZONTAL')
    progressbar12.set_inverted(1)

    # Creat Button
    Button1 = GLXCurses.Button()
    Button1.set_application(app)
    Button1.set_text('INCREASE')
    Button1.set_name('increase_button')

    Button2 = GLXCurses.Button()
    Button2.set_application(app)
    Button2.set_text('DECREASE')
    Button2.set_name('decrease_button')

    Button3 = GLXCurses.Button()
    Button3.set_application(app)
    Button3.set_text('Quit')
    Button3.set_name('quit_button')

    vbox_button = GLXCurses.VBox()
    vbox_button.pack_end(Button1)
    vbox_button.pack_end(Button2)
    vbox_button.pack_end(Button3)

    RadioButton1 = GLXCurses.RadioButton()
    RadioButton1.set_application(app)
    RadioButton1.set_text('RadioButton1')

    RadioButton2 = GLXCurses.RadioButton()
    RadioButton2.set_application(app)
    RadioButton2.set_text('RadioButton2')

    RadioButton3 = GLXCurses.RadioButton()
    RadioButton3.set_application(app)
    RadioButton3.set_text('RadioButton3')

    vbox_radio_button = GLXCurses.VBox()
    vbox_radio_button.pack_end(RadioButton1)
    vbox_radio_button.pack_end(RadioButton2)
    vbox_radio_button.pack_end(RadioButton3)

    CheckButton1 = GLXCurses.CheckButton()
    CheckButton1.set_application(app)
    CheckButton1.set_text('CheckButton1')

    CheckButton2 = GLXCurses.CheckButton()
    CheckButton2.set_application(app)
    CheckButton2.set_text('CheckButton2')

    CheckButton3 = GLXCurses.CheckButton()
    CheckButton3.set_application(app)
    CheckButton3.set_text('CheckButton3')

    vbox_check_button = GLXCurses.VBox()
    vbox_check_button.pack_end(CheckButton1)
    vbox_check_button.pack_end(CheckButton2)
    vbox_check_button.pack_end(CheckButton3)

    frame_for_button = GLXCurses.Frame()
    frame_for_button.set_label('Button')
    frame_for_button.add(vbox_button)

    frame_for_radio_button = GLXCurses.Frame()
    frame_for_radio_button.set_label('RadioButton')
    frame_for_radio_button.add(vbox_radio_button)

    frame_for_check_button = GLXCurses.Frame()
    frame_for_check_button.set_label('CheckButton')
    frame_for_check_button.add(vbox_check_button)

    hbox_buttons = GLXCurses.HBox()
    hbox_buttons.pack_end(frame_for_button)
    hbox_buttons.pack_end(frame_for_radio_button)
    hbox_buttons.pack_end(frame_for_check_button)

    HSepartor = GLXCurses.HSeparator()
    HSepartor.set_spacing(0)
    # VSepartor.set_position_type('center')
    # Creat two Vertical Box contener
    vbox1 = GLXCurses.VBox()
    vbox1.pack_end(hbox_buttons)
    vbox1.pack_end(frame_for_progressbar)
    vbox1.pack_end(frame_for_labels)

    hbox_label = GLXCurses.HBox()
    hbox_label.pack_end(label1)
    hbox_label.pack_end(label2)
    hbox_label.pack_end(label3)
    frame_for_labels.add(hbox_label)

    # Creat a new Horizontal Box contener
    hbox = GLXCurses.HBox()
    hbox.pack_end(vbox1)
    # hbox.add(vbox2)

    hbox_progress_widgets = GLXCurses.HBox()
    hbox_progress_widgets.set_spacing(1)
    hbox_progress = GLXCurses.HBox()
    vbox_progress = GLXCurses.VBox()

    hbox_progress_widgets.pack_end(vbox_progress)
    hbox_progress_widgets.pack_end(hbox_progress)

    hbox_progress.pack_end(progressbar1)
    hbox_progress.pack_end(progressbar2)
    hbox_progress.pack_end(progressbar3)
    hbox_progress.pack_end(progressbar4)
    hbox_progress.pack_end(progressbar5)
    hbox_progress.pack_end(progressbar6)

    vbox_progress.pack_end(progressbar7)
    vbox_progress.pack_end(progressbar8)
    vbox_progress.pack_end(progressbar9)
    vbox_progress.pack_end(progressbar10)
    vbox_progress.pack_end(progressbar11)
    vbox_progress.pack_end(progressbar12)

    frame_for_progressbar.add(hbox_progress_widgets)

    # hbox.set_spacing(0)
    # hbox.pack_end(win_for_progressbar)
    # hbox.pack_end(win6)

    win1.add(hbox)

    # Creat a Status Bar
    toolbar = GLXCurses.Toolbar()
    toolbar.button_list = [
        'Help',
        'Normal',
        'Active',
        'Prelight',
        'Selected',
        'Insensitive',
        '',
        '',
        'Menu',
        'Quit'
    ]
    statusbar = GLXCurses.Statusbar()
    # Add Everything inside the Application
    app.add_menubar(menu)
    app.add_window(win1)
    app.add_statusbar(statusbar)
    app.add_toolbar(toolbar)

    def on_resize(self, event_signal, event_args = []):
        message_text = ''
        message_text += 'Screen Size:'
        message_text += str(app.get_parent_size())
        message_text += ' '

        # Status Bar Demo
        progressbar1.set_value(randint(0, 100))
        value = '{0:}{1:}'.format(progressbar1.get_value(), '%')
        progressbar1.set_text(value)

        progressbar2.set_value(randint(0, 100))
        value = '{0:}{1:}'.format(progressbar2.get_value(), '%')
        progressbar2.set_text(value)

        progressbar3.set_value(randint(0, 100))
        value = '{0:}{1:}'.format(progressbar3.get_value(), '%')
        progressbar3.set_text(value)

        progressbar4.set_value(randint(0, 100))
        value = '{0:}{1:}'.format(progressbar4.get_value(), '%')
        progressbar4.set_text(value)

        progressbar5.set_value(randint(0, 100))
        value = '{0:}{1:}'.format(progressbar5.get_value(), '%')
        progressbar5.set_text(value)

        progressbar6.set_value(randint(0, 100))
        value = '{0:}{1:}'.format(progressbar6.get_value(), '%')
        progressbar6.set_text(value)

        progressbar7.set_value(randint(0, 100))
        value = '{0:}{1:}'.format(progressbar7.get_value(), '%')
        progressbar7.set_text(value)

        progressbar8.set_value(randint(0, 100))
        value = '{0:}{1:}'.format(progressbar8.get_value(), '%')
        progressbar8.set_text(value)

        progressbar9.set_value(randint(0, 100))
        value = '{0:}{1:}'.format(progressbar9.get_value(), '%')
        progressbar9.set_text(value)

        # progressbar10.set_value(randint(0, 100))
        # value = '{0:}{1:}'.format(progressbar10.get_value(), '%')
        # progressbar10.set_text(value)

        progressbar11.set_value(randint(0, 100))
        value = '{0:}{1:}'.format(progressbar11.get_value(), '%')
        progressbar11.set_text(value)

        progressbar12.set_value(randint(0, 100))
        value = '{0:}{1:}'.format(progressbar12.get_value(), '%')
        progressbar12.set_text(value)

        #app.refresh()

    def on_destroy():
        logging.debug('==> onDestroy')
        statusbar.push('A Incredible Emiter thing')

    def handleUpButtonClicked():
        logging.debug('handleUpButtonClicked')
        current = progressbar10.get_value()
        progressbar10.set_value(current+1)
        value = '{0:}{1:}'.format(progressbar10.get_value(), '%')
        progressbar10.set_text(value)

    def handlekeys(input_event):
        logging.debug('handleKeys '+str(input_event))
        if input_event == curses.KEY_F5:
            app.set_is_focus(Button1.id)
        elif input_event == curses.KEY_F6:
            Button1.set_sensitive(not Button1.get_sensitive())

    def on_click(self, event_signal, event_args = []):
        if event_args[1] == Button1.get_widget_id():
            current = progressbar9.get_value()
            progressbar9.set_value(current+1)
            value = '{0:}{1:}'.format(progressbar9.get_value(), '%')
            progressbar9.set_text(value)
            statusbar.push('Increase progress bar to value: ' + value)

        if event_args[1] == Button2.get_widget_id():
            current = progressbar9.get_value()
            progressbar9.set_value(current-1)
            value = '{0:}{1:}'.format(progressbar9.get_value(), '%')
            progressbar9.set_text(value)
            statusbar.push('Decrease progress bar to value: ' + value)

        if event_args[1] == Button3.get_widget_id():
            statusbar.push('Stopping every operation\'s')
            app.stop()

    app.connect('RESIZE', on_resize)
    app.connect('BUTTON_CLICKED', on_click)

    # Main loop
    app.start()

    # THE END
    sys.exit(0)
