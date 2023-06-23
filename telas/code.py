from PyQt5 import QtWidgets, uic, QtMultimedia
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QLineEdit
import img


def mudarTl(anterior, proxima):
        anterior.close()
        proxima.show()

class art_scape:
    def __init__(self):
        app = QtWidgets.QApplication([])

        
        
        self.tl_telaUm = uic.loadUi("./telas/telaUm.ui")
        self.tl_TUQuadroBilhete = uic.loadUi("./telas/TUQuadroBilhete.ui")
        self.tl_TUBilhete = uic.loadUi("./telas/TUBilhete.ui")
        self.tl_TUEscultura = uic.loadUi("./telas/TUEscultura.ui")
        self.tl_TUPintura = uic.loadUi("./telas/TUPintura.ui")

        self.tl_td = uic.loadUi("./telas/TD.ui")
        self.tl_TDBilheteRosa = uic.loadUi("./telas/TDBilheteRosa.ui")
        self.tl_TDFrase = uic.loadUi("./telas/TDFrase.ui")
        self.tl_TDOlhos = uic.loadUi("./telas/TDOlhos.ui")
        self.tl_TDSombra = uic.loadUi("./telas/TDSombra.ui")
        self.tl_TDTintas = uic.loadUi("./telas/TDTintas.ui")

        self.tl_T3 = uic.loadUi("./telas/T3.ui")
        self.tl_T3BilheteCaixa = uic.loadUi("./telas/T3BilheteCaixa.ui")
        self.tl_T3Caixa = uic.loadUi("./telas/T3Caixa.ui")
        self.tl_T3Calendario = uic.loadUi("./telas/T3Calendario.ui")
        self.tl_T3Nivel = uic.loadUi("./telas/T3Nivel.ui")
        self.tl_T3Quadro = uic.loadUi("./telas/T3Quadro.ui")
        self.tl_T3RGB = uic.loadUi("./telas/T3RGB.ui")
        self.tl_T3Saida = uic.loadUi("./telas/T3Saida.ui")
    
        self.senha = uic.loadUi("./telas/senha.ui")
        self.final = uic.loadUi("./telas/final.ui")
        self.tl_erou = uic.loadUi("./telas/erou.ui")

        self.tl_telaUm.quadroBilhete.clicked.connect(lambda: mudarTl(self.tl_telaUm, self.tl_TUQuadroBilhete))
        self.tl_telaUm.escultura.clicked.connect(lambda: mudarTl(self.tl_telaUm, self.tl_TUEscultura))
        self.tl_TUEscultura.volta.clicked.connect(lambda:mudarTl(self.tl_TUEscultura, self.tl_telaUm))
        self.tl_TUQuadroBilhete.bilheteAmarelo.clicked.connect(lambda: mudarTl(self.tl_TUQuadroBilhete, self.tl_TUBilhete))
        self.tl_TUQuadroBilhete.volta.clicked.connect(lambda: mudarTl(self.tl_TUQuadroBilhete, self.tl_telaUm))
        self.tl_TUBilhete.volta.clicked.connect(lambda: mudarTl(self.tl_TUBilhete, self.tl_TUQuadroBilhete))
        self.tl_telaUm.pintura.clicked.connect(lambda: mudarTl(self.tl_telaUm, self.tl_TUPintura))
        self.tl_TUPintura.volta.clicked.connect(lambda: mudarTl(self.tl_TUPintura, self.tl_telaUm))

        self.tl_telaUm.show()


        self.tl_telaUm.direita.clicked.connect(lambda: mudarTl(self.tl_telaUm, self.tl_td))    #PERAS, SOMBRA, TINTAS, OLHOS, DIREITA, ESQUERDA
        self.tl_td.esquerda.clicked.connect(lambda: mudarTl(self.tl_td, self.tl_telaUm))
        self.tl_td.peras.clicked.connect(lambda:mudarTl(self.tl_td, self.tl_TDBilheteRosa))
        self.tl_TDBilheteRosa.volta.clicked.connect(lambda: mudarTl(self.tl_TDBilheteRosa, self.tl_td))
        self.tl_TDBilheteRosa.frase.clicked.connect(lambda: mudarTl(self.tl_TDBilheteRosa, self.tl_TDFrase))
        self.tl_TDFrase.volta.clicked.connect(lambda: mudarTl(self.tl_TDFrase, self.tl_TDBilheteRosa))
        self.tl_td.olhos.clicked.connect(lambda: mudarTl(self.tl_td, self.tl_TDOlhos))
        self.tl_TDOlhos.volta.clicked.connect(lambda: mudarTl(self.tl_TDOlhos, self.tl_td))
        self.tl_td.sombra.clicked.connect(lambda: mudarTl(self.tl_td, self.tl_TDSombra))
        self.tl_TDSombra.volta.clicked.connect(lambda: mudarTl(self.tl_TDSombra, self.tl_td))
        self.tl_td.tintas.clicked.connect(lambda: mudarTl(self.tl_td, self.tl_TDTintas))
        self.tl_TDTintas.volta.clicked.connect(lambda: mudarTl(self.tl_TDTintas, self.tl_td))


        self.tl_td.direita.clicked.connect(lambda: mudarTl(self.tl_td, self.tl_T3))  #nivel, quadro
        self.tl_T3.nivel.clicked.connect(lambda: mudarTl(self.tl_T3, self.tl_T3Nivel))
        self.tl_T3Nivel.volta.clicked.connect(lambda: mudarTl(self.tl_T3Nivel, self.tl_T3))
        self.tl_T3.quadro.clicked.connect(lambda: mudarTl(self.tl_T3, self.tl_T3Quadro))
        self.tl_T3Quadro.volta.clicked.connect(lambda: mudarTl(self.tl_T3Quadro, self.tl_T3))
        self.tl_T3Quadro.caixaA.clicked.connect(lambda: mudarTl(self.tl_T3Quadro, self.tl_T3Caixa))
        self.tl_T3Caixa.volta.clicked.connect(lambda: mudarTl(self.tl_T3Caixa, self.tl_T3Quadro))
        self.tl_T3Quadro.calendario.clicked.connect(lambda: mudarTl(self.tl_T3Quadro, self.tl_T3Calendario))
        self.tl_T3Calendario.volta.clicked.connect(lambda: mudarTl(self.tl_T3Calendario, self.tl_T3Quadro))
        self.tl_T3.esquerda.clicked.connect(lambda:mudarTl(self.tl_T3, self.tl_td))


        self.tl_T3.direita.clicked.connect(lambda: mudarTl(self.tl_T3, self.tl_T3Saida))
        self.tl_T3Saida.esquerda.clicked.connect(lambda: mudarTl(self.tl_T3Saida, self.tl_T3))
        self.tl_T3Saida.bilheteCaixa.clicked.connect(lambda: mudarTl(self.tl_T3Saida, self.tl_T3BilheteCaixa))
        self.tl_T3BilheteCaixa.volta.clicked.connect(lambda: mudarTl(self.tl_T3BilheteCaixa, self.tl_T3Saida))
        self.tl_T3Saida.rgb.clicked.connect(lambda: mudarTl(self.tl_T3Saida, self.tl_T3RGB))
        self.tl_T3RGB.volta.clicked.connect(lambda: mudarTl(self.tl_T3RGB, self.tl_T3Saida))
        self.tl_T3Saida.portaSaida.clicked.connect(lambda: mudarTl(self.tl_T3Saida, self.senha))
        self.senha.validar.clicked.connect(self.validar_senha)
        self.senha.volta.clicked.connect(lambda: mudarTl(self.senha, self.tl_T3Saida))
        self.final.sim.clicked.connect(lambda: mudarTl(self.final, self.tl_telaUm))
        self.final.nao.clicked.connect(self.final.close)
        self.tl_erou.volta.clicked.connect(lambda: mudarTl(self.tl_erou, self.senha))
        app.exec()
        
    def validar_senha(self):
             senhaP = self.senha.lineEdit.text()
             if senhaP == '2955':
                self.senha.close()
                self.final.show()
                self.senha.lineEdit.clear()

             else:
                  self.senha.lineEdit.clear()
                  self.senha.close()
                  self.tl_erou.show()


        



if __name__ == '__main__':
    jogo = art_scape()