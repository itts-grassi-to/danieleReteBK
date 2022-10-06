# ## CREATO DA ORTU prof. DANIELE
# ## daniele.ortu@itisgrassi.edu.it
import os
import gi
import ast

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

from pg1 import Pg1


CURRDIR = os.path.dirname(os.path.abspath(__file__))
PATH_CONF = os.path.join(CURRDIR, 'danieleReteBK.conf')

class Eventi:
    def on_click_nuovo(self, button):
        bks = pg1.getBKS()
        dialog = Gtk.MessageDialog(
            transient_for=None,
            flags=0,
            message_type=Gtk.MessageType.INFO,
            buttons=Gtk.ButtonsType.CLOSE,
            text="Salvato generale"
        )
        dialog.run()
        dialog.destroy()

    def on_click_annulla(self, button):
        pass

class MainConfig:
    def __init__(self, builder):
        self.__builder=builder
        GLADE = os.path.join(CURRDIR, 'mainConfig.glade')
        self.__builder.add_from_file(GLADE)
        self.__builder.connect_signals(Eventi())
    def getWin(self):
        return self.__builder.get_object('MainWinConfig')

with open(PATH_CONF, "r") as f:
    bks = d = ast.literal_eval(f.read())
    f.close()
builder = Gtk.Builder()
mc=MainConfig(builder)

pg1 = Pg1("pr", builder, bks)

window =mc.getWin()


window.set_title("GIGI")
# window.set_icon_from_file(ICON)
window.connect("destroy", Gtk.main_quit)
window.show_all()

Gtk.main()