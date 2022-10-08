# ## CREATO DA ORTU prof. DANIELE
# ## daniele.ortu@itisgrassi.edu.it

class Pg23:
    def __init__(self,  npg, builder, ch, bks):
        # print(bks)
        self.__bk = bks['bks'][ch]
        if npg == 2:
            # print(bks)
            self.__rdLoc = builder.get_object('rdOrigineLoc')
            self.__txtLocPath = builder.get_object('txtOrigineLocPath')
            self.__btLocPath = builder.get_object('btOrigineLocPath')

            self.__rdRem = builder.get_object('rdOrigineRem')
            self.__txtHost = builder.get_object('txtOrigineHost')
            self.__txtUtente = builder.get_object('txtOrigineUtente')
            self.__txtRemPath = builder.get_object('txtOrigineRemPath')

            self.__caricaCampi("dirDA")
        else:
            self.__rdLoc = builder.get_object('rdDestinazioneLoc')
            self.__txtLocPath = builder.get_object('txtDestinazioneLocPath')
            self.__btLocPath = builder.get_object('btDestinazioneLocPath')

            self.__rdRem = builder.get_object('rdDestinazioneRem')
            self.__txtHost = builder.get_object('txtDestinazioneHost')
            self.__txtUtente = builder.get_object('txtDestinazioneUtente')
            self.__txtRemPath = builder.get_object('txtDestinazioneRemPath')

            self.on_rd_click()
            # print("campi caricati ", self.__rdRem.get_active() )
    def getBtLocPathText(self):
        return self.__btLocPath.get_filename()
    def __caricaCampi(self, who):
        self.__txtLocPath.set_editable(False)
        if self.__bk[who]['remoto']:
            self.__rdRem.set_active(True)
            i = self.__bk[who]['da'].find("@")
            if i != -1:
                self.__txtUtente.set_text(self.__bk[who]['da'][:i])
                ii = self.__bk[who]['da'].find(":")
                if ii != -1:
                    self.txtHost.set_text(self.__bk[who]['da'][i + 1:ii])
                    self.txtRemPath.set_text(self.__bk[who]['da'][ii + 1:])
        else:
            self.__rdLoc.set_active(True)
            self.__txtLocPath.set_text(self.__bk[who]['da'])



    def on_rd_click(self):
        if self.__rdLoc.get_active():
            self.__btLocPath.set_sensitive(True)
            self.__txtHost.set_editable(False)
            self.__txtUtente.set_editable(False)
            self.__txtRemPath.set_editable(False)
        else:
            self.__btLocPath.set_sensitive(False)
            self.__txtHost.set_editable(True)
            self.__txtUtente.set_editable(True)
            self.__txtRemPath.set_editable(True)
