# ## CREATO DA ORTU prof. DANIELE
# ## daniele.ortu@itisgrassi.edu.it

import ast
import gi
import os
import socket


HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65432  # The port used by the server

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from dlgConfigurazione import DlgNuovo, DlgConf

STRUTTURA_CONFIGURAZIONE={
            'bks': {},
            'altro': {'mailFROM': '', 'mailTO': ''}
}
class GMain:
    def __init__(self, path_fconf, lst):
        self.path_fconf = path_fconf
        self.lstMain = lst
        if not os.path.isfile(path_fconf):
            with open(path_fconf, "w") as f:
                #print(str(STRUTTURA_CONFIGURAZIONE))
                f.write(str(STRUTTURA_CONFIGURAZIONE))
        self.__configurazione = self.get_impostazioni(self.path_fconf)
        self.__bks = self.__configurazione['bks']
        self.lst_chiavi=[]
        self.__attach_rows(lst)
    def invia(self, richi):

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))
            s.sendall(richi)
            #data = s.recv(1024)

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
        w = DlgConf(self, self.path_fconf)
        w.connect("destroy", Gtk.main_quit)
        w.set_modal(True)
        w.show_all()
        Gtk.main()
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