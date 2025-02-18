class P1:

    def __init__(self):
        self.deb_p1 = 0

    def debito_1(self, deb_p1=None):
        piu_1 = float(input('quanti soldi devi: '))
        self.deb_p1 = float(self.deb_p1 + piu_1)

    def dati_1(self, deb_p1=None):
        meno_1 = float(input('quanti soldi hai dato: '))
        self.deb_p1 = float(self.deb_p1 - meno_1)

    def mostra(self):
        print(self.deb_p1)


class P2:

    def __init__(self):
        self.deb_p2 = 0

    def debito_2(self, deb_p2=None):
        piu_2 = float(input('quanti soldi devi: '))
        self.deb_p2 = float(self.deb_p2 + piu_2)

    def dati_2(self, deb_p2=None):
        meno_2 = float(input('quanti soldi hai dato: '))
        self.deb_p2 = float(self.deb_p2 - meno_2)

    def mostra(self):
        print(self.deb_p2)

P1 = P1()
P2 = P2()


persona = input('chi sei: ').lower()

if persona == 'p2':
    azione = input('devi aggiungere o diminuire il tuo debito: ').lower()
    if azione == 'aggiungere':
        P2.debito_2()
    elif azione == 'diminuire':
        P2.dati_2()
    else:
        print('risposta non accettata')
    P2.mostra()

elif persona == 'p1':
    azione = input('devi aggiungere o diminuire il tuo debito: ').lower()
    if azione == 'aggiungere':
        P1.debito_1()
    elif azione == 'diminuire':
        P1.dati_1()
    else:
        print('risposta non accettata')
    P1.mostra()

else:
    print('risposta non accettata')
