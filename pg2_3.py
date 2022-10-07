# ## CREATO DA ORTU prof. DANIELE
# ## daniele.ortu@itisgrassi.edu.it

class Pg23:
    def __init__(self,  npg, builder, ch, bks):
        # print(bks)
        self.__bk = bks['bks'][ch]
        if npg == 1:
            # print(bks)
            self.__rdLoc = builder.get_object('rdOrigineLoc')
            self.__txtLocPath = builder.get_object('txtOrigineLoc')
            self.__btLoc = builder.get_object('btOrigineLoc')

            self.__rdRem = builder.get_object('rdOrigineRem')
            self.__txtHost = builder.get_object('txtOrigineHost')
            self.__txtUtente = builder.get_object('txtOrigineUtente')
            self.__txtRemPath = builder.get_object('txtOrigineRemPath')

            self.__caricaCampi("dirDA")
            print("campi caricati ", self.__rdRem.get_active() )
    def __caricaCampi(self, who):
        if self.__bk[who]['remoto']:
            self.__rdRem.set_active(False)
            i = self.__bk[who]['da'].find("@")
            if i != -1:
                self.__txtUtente.set_text(self.__bk[who]['da'][:i])
                ii = self.__bk[who]['da'].find(":")
                if ii != -1:
                    self.txtHost.set_text(self.__bk[who]['da'][i + 1:ii])
                    self.txtRemPath.set_text(self.__bk[who]['da'][ii + 1:])
        else:
            self.__rdLoc.set_active(False)
            self.__txtLocPath.set_text(self.__bk[who]['da'])
    def on_rd_toggled(self, rd, name):
        if rd.get_active():
            self.__btLocPath.set_sensitive(True)
            self.__txtHost.set_editable(False)
            self.__txtUtente.set_editable(False)
            self.__txtRemPath.set_editable(False)
        else:
            self.__btLocPath.set_sensitive(False)
            self.__txtHost.set_editable(True)
            self.__txtUtente.set_editable(True)
            self.__txtRemPath.set_editable(True)
