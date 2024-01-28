class CursistenRegister:

    def __init__(self, voornaam, achternaam, adres, e_mail):
        self._voornaam= voornaam
        self._achternaam= achternaam
        self._adres= adres
        self._e_mail= e_mail

    def wasmachine (self):
        print('Welkom ' + (self._voornaam) )
        print('We hebben u bericht goed ontvangen op de naam ' + (self._achternaam) )
        print('We gaan langskomen voor u wasmachine te repareren op ' + (self._adres) )
        print('U krijgt binnen de 24 uur een e mail waarop u de de datum en het uur terug vindt op' + (self._e_mail) )
        print('We komen zo snel mogelijk. mvg' )

bericht = CursistenRegister('heidi', 'helmhout', 'heiken 91 te brecht', 'heidi.@gmail.com')
bericht.wasmachine()