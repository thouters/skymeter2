.. vim:ft=rst:spell:spelllang=en,nl

==========
 Skymeter
==========

:author: Thomas Langewouters
:description: A program that polls the download/upload meters webpage of a Belgacom Skynet account.

What is Skymeter?
-----------------

Skymeter is a utility targeted at Belgacom [#]_ customers.  
Belgacom has a very restrictive policy towards the amount of data its customers
can download with its broadband internet service.

Skymeter polls the meter webpage of the Belgacom 'Self care' [#]_ website 
and presents the useful information to the user.

.. Note::

    This program is only useful to Belgians.  Since half of the country
    speaks dutch, I wrote the rest of this page in Dutch.  Sorry to the French
    speaking part of the target audience.  The code comments are in English so
    you should still be able to figure out how to operate Skymeter.  Please
    submit or provide a French or English translation of this page if you feel 
    it necessary.

.. [#] A Belgian Internet Service Provider
.. [#] What an odd name!

Wat is Skymeter?
----------------

.. figure:: img/Skymeter/tkskymeter.png
   :align: center

   Tkskymeter 2.1.0 schermafdruk


Skymeter is een programma dat Skynet klanten toelaat de meterstand van hun
internet abonnement te bekijken.  Het haalt de informatie van de Skynet 
'self care' website en toont vervolgens het enige interessante deel van de 
pagina als enkele lijnen tekst in een terminalvenster of grafisch.

Waarom
------

Als Skynet klant valt het regelmatig voor dat er tegen het einde van de maand
een melding in mijn mailbox land die ik liever niet zie.  
Een boodschap die aankondigt dat ter huize het verstrekte download volume bijna
overschreden is.  Om de goede vrede te bewaren check ik in die periode 
regelmatig de volumemeter op de Skynet website.  Dit voorkomt een situatie
waarin pa, ma of broer het in de vroege uren van het weekend nodig acht 
om me te wekken en te klagen over de trage verbinding.

Aangezien dit redelijk veel muisklikken vereist (dat is met de meeste 
handelingen op websites nu eenmaal zo), kwam het idee in me op om het
`telemeter programma`_ (waarmee Telenet klanten hun volume kunnen controleren)
, aan te passen zodat het met de Skynet website overweg kan.

.. _`telemeter programma`: http://www.telemeter.be

Telemeter bleek in de programmeertaal C geschreven te zijn, maar een dergelijk
programma in C schrijven leek me nogal overkill.  

Skymeter 1 & 2
--------------

Oorspronkelijk heb ik Skymeter in PERL geschreven, maar toen ik de taal
Python ontdekte, stelde ik vast dat Skymeter veel beknopter en eleganter 
geschreven kon worden in Python, deze heeft namelijk standaard http 
functionaliteit aan boord heeft (met SSL support).

Ik heb de Skymeter die in python geschreven is Skymeter 2.0 gedoopt.
Skymeter 1 blijft beschikbaar, maar ondertussen is Skymeter 2 beter
ontwikkeld en heeft deze het minst ruwe kanten.

Screenshots
-----------

.. raw:: html
	
	<table style="border: 0px;">
	<tr><td align="center"><a href="img/Skymeter/screenshot-1.1.8.png">
	<img border="0" src="img/Skymeter/thumb/screenshot-1.1.8.png" alt="thumb"/>
	</a>
	<br/>
	<font size="1" color="grey">screenshot-1.1.8.png</font>
	</td><td align="center"><a href="img/Skymeter/screenshot-1.2.1.png">
	<img border="0" src="img/Skymeter/thumb/screenshot-1.2.1.png" alt="thumb"/>
	</a>
	<br/>
	<font size="1" color="grey">screenshot-1.2.1.png</font>
	</td><td align="center"><a href="img/Skymeter/screenshot1.png">
	<img border="0" src="img/Skymeter/thumb/screenshot1.png" alt="thumb"/>
	</a>
	<br/>
	<font size="1" color="grey">screenshot1.png</font>
	</td></tr></table>

.. raw:: html

	<table style="border: 0px;">
	<tr><td align="center"><a href="img/Skymeter/lintkskymeter.png">
	<img border="0" src="img/Skymeter/thumb/lintkskymeter.png" alt="thumb"/>
	</a>
	<br/>
	<font size="1" color="grey">lintkskymeter.png</font>
	</td><td align="center"><a href="img/Skymeter/wintkskymeter.png">
	<img border="0" src="img/Skymeter/thumb/wintkskymeter.png" alt="thumb"/>
	</a>
	<br/>
	<font size="1" color="grey">wintkskymeter.png</font>
	</td><td align="center"><a href="img/Skymeter/winxptkskymeter.png">
	<img border="0" src="img/Skymeter/thumb/winxptkskymeter.png" alt="thumb"/>
	</a>
	<br/>
	<font size="1" color="grey">winxptkskymeter.png</font>
	</td></tr></table>


Configuratie
------------

Skymeter dient de username en het paswoord van je Skynet abonnement te weten,
deze informatie dient in het configuratiebestand te worden geplaatst.
	
Dit bestand moet de naam ``.skymeterrc`` te hebben, en zich in de home folder
van de gebruiker te bevinden die Skymeter wil gebruiken.
Het bestand dient deze twee lijnen te bevatten ::

	user jegebruikersnaam
	pass jewachtwoord

Dit wijst zichzelf uit.

Het is aangeraden dit bestand onleesbaar te maken voor andere gebruikers
van uw computer: ``chmod go-rwx ~/.skymeterrc``

Skymeter 2
----------

Om de achter de huidige stand van de volumemeter te polsen, moet je gewoon het
commando ``skymeter`` uitvoeren.

:: 

	thomas@whirlpool thomas $ skymeter
        Volume meters for xxxxxxxx on Mon, xx Jul 2008 14:19:51
        BasicMeter: 33%: 8 GB 311 MB of 25 GB

Er is een grafische interface met de naam ``tkskymeter``.


Broken by design...
-------------------

Skymeter gebruikt reguliere expressies op de HTML pagina van
de volumemeter webpagina om achter de informatie te komen.
Telkens dat Skynet de constructie van de betreffende zinnen
met de meterstand wijzigt, dient de patroonherkenning die gebruikt
wordt om de nuttige informatie te achterhalen dus onbruikbaar,
en is Skymeter aan onderhoud toe.

Aangezien ik soms gedurende lange periodes Skymeter niet zelf gebruik,
kan het een hele tijd duren voor dat ik merk dat de regex aan
liefde toe is.  Het valt dus af en toe voor dat Skymeter onbruikbaar is,
en een nieuwe release op zich laat wachten.

Als u zelf verstand heeft van PERL en/of reguliere expressies,  stel ik patches
erg op prijs.  Ook kan u helpen door bij Skynet te lobbyen en ze aan te sporen
de meterstand in XML(-RPC) aan te bieden.

Ten slotte...
-------------

Ik geef de code ook vrij (onder de GPL), zodat u het script kan bestuderen,
aanpassen en uitbreiden naar uw wensen. (Wel zou ik het heel fijn vinden dat
bugs gemeld worden, net als verbeteringen die u hebt aangebracht en u graag
meeverspreid wilt zien in de code die ik op mijn site aanbied.)

Ik zou graag alle mensen willen bedanken die me patches hebben gemaild, en me
raad gegeven hebben bij het schrijven van Skymeter.  (zie het bestand met de
naam THANKS in de tarball)

Gebruik Skymeter 1
-------------------

.. caution::

   Het is aangeraden Skymeter 2 te gebruiken, deze instructies voor de
   oude versie blijven hier als referentie.

Sporadisch gebruik
==================

Om de achter de huidige stand van de volumemeter te polsen, moet je gewoon het
commando ``skymeter`` uitvoeren.

:: 

	thomas@whirlpool thomas $ skymeter
	Aanvraag... Inloggen... Parsen... Ok!
	Basisvolume [1.19 / 10] 
	Lopende volumepack: [3.71 / 5]

Automatisch
===========

In GNU/Linux worden elke keer een PPP(gebruikt bij ADSL) verbinding tot stand
komt de scripts in ``/etc/ppp/ip-up.d/`` uitgevoerd.  Hier kun je bijvoorbeeld
een script zoals het volgende plaatsen: ::

	#!/bin/bash
	/usr/local/bin/skymeter --put /var/www/index.html

Dit zorgt er voor dat Skymeter de informatie over de volumemeter
(wel als text file!) schrijft naar ``/var/www/index.html``.
Dat kan eventueel door een webserver (met als *documentroot* ``/var/www/``)
gedeeld worden over het LAN.  Zo kan de hele familie de meterstand
snel raadplegen.

Het argument ``--put`` zorgt er voor dat een bestand wordt aangemaakt dat er 
als volgt uitziet: ::

	Basisvolume: 0.34 / 10
	Volumepack: 3.71 / 5

Het bestand kan dus gemakkelijk door zelfgeschreven scripts verwerkt worden.

Dependencies
============

* curl: Skymeter maakt gebruik van de stand alone versie van curl,
  een curl binary met SSL support is nodig.
* PERL: Skymeter heeft de PERL interpreter nodig, deze is op de
  meeste Linux systemen standaard aanwezig.
	
Verwanten
---------

.. _`telemeter`: http://www.telemeter.be
.. _`SkyMonitor`: http://n00.be/widgets/

* `SkyMonitor`_, De Mac OSX-incarnatie van Skymeter.  
  Een must-have voor Mac gebruikers.
* `telemeter`_, Voor Telenet klanten.

