# ## CREATO DA ORTU prof. DANIELE
# ## daniele.ortu@itisgrassi.edu.it

class Pg1:
    def __init__(self, ch, builder, bks):
        # print(bks)
        self._bks = bks
        self.__bk = bks['bks'][ch]
        self.__altro = bks['altro']
        self.__txtOra = builder.get_object('txtOra')
        self.__txtOra.set_text(self.__bk['cron']['ora'])
        self.__txtMin = builder.get_object('txtMin')
        self.__txtMin.set_text(self.__bk['cron']['minuto'])
        self.__txtGio = builder.get_object('txtGio')
        self.__txtGio.set_text(self.__bk['cron']['giorno'])
        self.__txtMese = builder.get_object('txtMese')
        self.__txtMese.set_text(self.__bk['cron']['mese'])
        # Giorno settimana
        self.__ckLun = builder.get_object('ckLun')
        self.__ckLun.set_active(1 in self.__bk['cron']['settimana'])
        self.__ckMar = builder.get_object('ckMar')
        self.__ckMar.set_active(2 in self.__bk['cron']['settimana'])
        self.__ckMer = builder.get_object('ckMer')
        self.__ckMer.set_active(3 in self.__bk['cron']['settimana'])
        self.__ckGio = builder.get_object('ckGio')
        self.__ckGio.set_active(4 in self.__bk['cron']['settimana'])
        self.__ckVen = builder.get_object('ckVen')
        self.__ckVen.set_active(5 in self.__bk['cron']['settimana'])
        self.__ckSab = builder.get_object('ckSab')
        self.__ckSab.set_active(6 in self.__bk['cron']['settimana'])
        self.__ckDom = builder.get_object('ckDom')
        self.__ckDom.set_active(7 in self.__bk['cron']['settimana'])
        # email
        self.__txtMailFROM = builder.get_object('txtMailFROM')
        self.__txtMailFROM.set_text(self.__altro['mailFROM'])
        self.__txtMailTO = builder.get_object('txtMailTO')
        self.__txtMailTO.set_text(self.__altro['mailTO'])

    def __salva_cron(self):
        self.__bk['cron']['minuto'] = self.txtMin.get_text()
        self.__bk['cron']['ora'] = self.txtOra.get_text()
        self.__bk['cron']['giorno'] = self.txtGio.get_text()
        self.__bk['cron']['mese'] = self.txtMese.get_text()
        self.__bk['cron']['settimana'] = []
        if self.chDom.get_active():
            self.__bk['cron']['settimana'].append(0)
        if self.chLun.get_active():
            self.__bk['cron']['settimana'].append(1)
        if self.chMar.get_active():
            self.__bk['cron']['settimana'].append(2)
        if self.chMer.get_active():
            self.__bk['cron']['settimana'].append(3)
        if self.chGio.get_active():
            self.__bk['cron']['settimana'].append(4)
        if self.chVen.get_active():
            self.__bk['cron']['settimana'].append(5)
        if self.chSab.get_active():
            self.__bk['cron']['settimana'].append(6)
    def __salva_altro(self):
        self.bks['altro']['mailFROM'] = self.txtMailFrom.get_text()
        self.bks['altro']['mailTO'] = self.txtMailTO.get_text()

    def __is_active(self, giorno):
        if self.__bk['cron']['settimana'] == '*':
            return True
        return giorno in self.__bk['cron']['settimana']

    def getBKS(self):
        self.__salva_cron()
        self.__salva_altro()
        return self.bks