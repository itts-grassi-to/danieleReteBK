# ## CREATO DA ORTU prof. DANIELE
# ## daniele.ortu@itisgrassi.edu.it
import os
import gi
import ast

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

from pg1 import Pg1
from pg2_3 import Pg23


CURRDIR = os.path.dirname(os.path.abspath(__file__))
PATH_CONF = os.path.join(CURRDIR, 'danieleReteBK.conf')
GLADE = os.path.join(CURRDIR, 'mainConfig.glade')

class Eventi:
    def on_click_nuovo(self, button):
        mc.salvaPG1()
        print(mc._bks)
        dialog = Gtk.MessageDialog(
            transient_for=None,
            flags=0,
            message_type=Gtk.MessageType.INFO,
            buttons=Gtk.ButtonsType.CLOSE,
            text="Salvato generale"
        )
        dialog.run()
        dialog.destroy()
    def on_click_rd_origine_loc(self, rd):
        print("click origine")
        mc.pg2.on_rd_click()
    def on_click_rd_destinazione_loc(self, rd):
        print("Click destinazione")
        mc.pg3.on_rd_click()
    def on_currdir_changed(self,widget):
       print(mc.pg2.getBtLocPathText())
    def on_click_annulla(self, button):
        pass

class MainConfig(Pg1):
    def __init__(self, builder):
        self.__builder = builder
        with open(PATH_CONF, "r") as f:
            self.__bks = ast.literal_eval(f.read())
            f.close()
        self.__builder.add_from_file(GLADE)
        Pg1.__init__(self, builder, "pr", self.__bks)
        self.pg2 = Pg23(2, builder, "pr", self.__bks)
        self.pg3 = Pg23(3, builder, "pr", self.__bks)

    def getWin(self):
        return self.__builder.get_object('MainWinConfig')


builder = Gtk.Builder()
mc = MainConfig(builder)
builder.connect_signals(Eventi())
# pg1 = Pg1("pr", builder, bks)

window = mc.getWin()


window.set_title("GIGI")
# window.set_icon_from_file(ICON)
window.connect("destroy", Gtk.main_quit)
window.show_all()

Gtk.main()