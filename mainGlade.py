# ## CREATO DA ORTU prof. DANIELE
# ## daniele.ortu@itisgrassi.edu.it

import gi
import os

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from gmain import GMain

CURRDIR = os.path.dirname(os.path.abspath(__file__))
GLADE = os.path.join(CURRDIR, 'mainGBK.glade')
PATH_CONF = os.path.join(CURRDIR, 'danieleReteBK.conf')


class Eventi:
    def __init__(self):
        pass
    def on_click_nuovo(self, button):
        gestione.on_nuovo_clicked(lstBKS)
    def on_click_modifica(self, button):
        gestione.on_modifica_clicked()
    def on_click_cancella(self, button):
        pass
    def on_showClick(self, button):
        #print("clicked")
        pop.popup()
    def lbl_click(self):
        print("clicked*************")
    def uba(self, button):
        print("clicked*************")

builder = Gtk.Builder()
builder.add_from_file(GLADE)
builder.connect_signals(Eventi())

window = builder.get_object('MainWin')
pop = builder.get_object('popover')
lstBKS = builder.get_object('lstBKS')
lblLed=builder.get_object('lblLed')
gestione = GMain(PATH_CONF, lstBKS, lblLed)

# window.set_icon_from_file(ICON)
window.connect("destroy", Gtk.main_quit)
window.show_all()

Gtk.main()
