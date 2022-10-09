# ## CREATO DA ORTU prof. DANIELE
# ## daniele.ortu@itisgrassi.edu.it

import gi
import os
import ast
import segnali

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

CURRDIR = os.path.dirname(os.path.abspath(__file__))
GLADE = os.path.join(CURRDIR, 'mainGBK.glade')
PATH_CONF = os.path.join(CURRDIR, 'danieleReteBK.conf')

STRUTTURA_CONFIGURAZIONE={
            'bks': {},
            'altro': {'mailFROM': '', 'mailTO': ''}
}
SPAZI="    "

class Eventi:
    def __init__(self):
        pass
    def on_click_nuovo(self, button):
        gestione.on_nuovo_clicked(lstBKS)
    def on_click_modifica(self, button):
        #gestione.on_modifica_clicked()
        if not self.lstMain.get_selected_row():
            dialog = Gtk.MessageDialog(
                transient_for=None,
                flags=0,
                message_type=Gtk.MessageType.ERROR,
                buttons=Gtk.ButtonsType.CLOSE,
                text="Seleziona il backup da modificare",
            )
            dialog.run()
            dialog.destroy()
            return
        builder = Gtk.Builder()
        mc = MainConfig("pr", builder)
        builder.connect_signals(Eventi())
        window = mc.getWin()
        window.set_title("Modifica ")
        # window.set_icon_from_file(ICON)
        window.connect("destroy", Gtk.main_quit)
        window.show_all()

        Gtk.main()
    def on_click_cancella(self, button):
        pass
    def on_showClick(self, button):
        #print("clicked")
        pop.popup()
    def lbl_click(self):
        print("clicked*************")
    def uba(self, button):
        print("clicked*************")

class GMain:
    def __init__(self, path_fconf, lst, lblLed):
        self.path_fconf = path_fconf
        self.lstMain = lst
        self.__lblLed=lblLed
        if not os.path.isfile(path_fconf):
            with open(path_fconf, "w") as f:
                #print(str(STRUTTURA_CONFIGURAZIONE))
                f.write(str(STRUTTURA_CONFIGURAZIONE))
        self.__configurazione = self.get_impostazioni(self.path_fconf)
        self.__bks = self.__configurazione['bks']
        self.lst_chiavi = []
        self.__attach_rows(lst)
        self.__setLed()
    def __setLed(self):
        if self.invia(segnali.IS_ATTIVO) == segnali.OK:
            self.__lblLed.set_markup("<span background='green'><big>    </big></span>")
        else:
            self.__lblLed.set_markup("<span background='red'><big>    </big></span>")
    def invia(self, richi):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((HOST, PORT))
                s.sendall(richi)
                data = s.recv(1024)
                return data
        except:
            return segnali.NOK
        # print(f"Received {data!r}")
    def on_cancella_clicked(self):
        self.__invia(b"Hello, world")
    def on_modifica_clicked(self):
        if not self.lstMain.get_selected_row():
            dialog = Gtk.MessageDialog(
                transient_for=None,
                flags=0,
                message_type=Gtk.MessageType.ERROR,
                buttons=Gtk.ButtonsType.CLOSE,
                text="Seleziona il backup da modificare",
            )
            dialog.run()
            dialog.destroy()
            return
        #ch = lst_chiavi[lstMain.get_selected_row().get_index()]
        #w = MainConfig(self, ch, builder)
        #w.connect("destroy", Gtk.main_quit)
        #w.set_modal(True)
        #w.show_all()
        #Gtk.main()
    def on_nuovo_clicked(self, lst):
        # print("NUOVO")
        w = DlgNuovo(self, self.path_fconf)
        w.connect("destroy", Gtk.main_quit)
        w.set_modal(True)
        w.show_all()
        Gtk.main()
        self.__bks = self.get_impostazioni(self.path_fconf)['bks']
        # lst.add(self.__attach_row(self.lst_chiavi.pop()))
    def get_impostazioni(self, f):
        with open(f, "r") as data:
            d = ast.literal_eval(data.read())
            data.close()
            return d
    def __attach_rows(self, lst):
        # print("Backup: " + str(self.bks['bks']))
        for chiave in self.__bks:
            lst.add(self.__attach_row(chiave))
    def __attach_row(self, ch):
        row = Gtk.ListBoxRow()
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        row.add(hbox)
        bk = self.__bks[ch]
        label = Gtk.Label(label=bk['titolo'], xalign=0)
        label.set_property("width-request", 450)
        hbox.pack_start(label, False, True, 0)

        check = Gtk.CheckButton(label=ch)
        check.set_active(bk['attivo'])
        check.connect("toggled", self.__on_toggled_ck)
        hbox.pack_start(check, False, True, 0)

        self.lst_chiavi.append(ch)
        # hbox.pack_start(check, False, True, 0)

        return row
    def __on_toggled_ck(self, ck):
        ch = ck.get_label()
        self.__bks[ch]['attivo'] = ck.get_active()
        with open(self.path_fconf, "w") as data:
            data.write(str(self.__configurazione))
            data.close()
    def test(self):
        print("prova**************************")

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
