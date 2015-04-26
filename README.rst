<div class="document" id="skymeter">
<h1 class="title">Skymeter</h1>
<table class="docinfo" frame="void" rules="none">
<col class="docinfo-name" />
<col class="docinfo-content" />
<tbody valign="top">
<tr><th class="docinfo-name">Author:</th>
<td>Thomas Langewouters</td></tr>
<tr class="field"><th class="docinfo-name">description:</th><td class="field-body">A script to check your Skynet account's download/upload meters.</td>
</tr>
</tbody>
</table>
<!-- vim:ft=rst:spell:spelllang=en,nl -->
<div class="section">
<h1><a id="what-is-skymeter" name="what-is-skymeter">What is Skymeter?</a></h1>
<p>Skymeter is a utility targeted at Belgacom <a class="footnote-reference" href="#id3" id="id1" name="id1">[1]</a> customers.
Belgacom has a very restrictive policy towards the amount of data its customers
can download with its broadband internet service.</p>
<p>Skymeter polls the meter webpage of the Belgacom 'Self care' <a class="footnote-reference" href="#id4" id="id2" name="id2">[2]</a> website
and presents the useful information to the user.</p>
<div class="note">
<p class="first admonition-title">Note</p>
<p class="last">This program is only useful to Belgians.  Since half of the country
speaks dutch, I wrote the rest of this page in Dutch.  Sorry to the French
speaking part of the target audience.  The code comments are in English so
you should still be able to figure out how to operate Skymeter.  Please
submit or provide a French or English translation of this page if you feel
it necessary.</p>
</div>
<table class="docutils footnote" frame="void" id="id3" rules="none">
<colgroup><col class="label" /><col /></colgroup>
<tbody valign="top">
<tr><td class="label"><a class="fn-backref" href="#id1" name="id3">[1]</a></td><td>A Belgian Internet Service Provider</td></tr>
</tbody>
</table>
<table class="docutils footnote" frame="void" id="id4" rules="none">
<colgroup><col class="label" /><col /></colgroup>
<tbody valign="top">
<tr><td class="label"><a class="fn-backref" href="#id2" name="id4">[2]</a></td><td>What an odd name!</td></tr>
</tbody>
</table>
</div>
<div class="section">
<h1><a id="wat-is-skymeter" name="wat-is-skymeter">Wat is Skymeter?</a></h1>
<div align="center" class="figure">
<img alt="img/Skymeter/tkskymeter.png" src="img/Skymeter/tkskymeter.png" />
<p class="caption">Tkskymeter 2.1.0 schermafdruk</p>
</div>
<p>Skymeter is een programma dat Skynet klanten toelaat de meterstand van hun
internet abonnement te bekijken.  Het haalt de informatie van de Skynet
'self care' website en toont vervolgens het enige interessante deel van de
pagina als enkele lijnen tekst in een terminalvenster of grafisch.</p>
</div>
<div class="section">
<h1><a id="waarom" name="waarom">Waarom</a></h1>
<p>Als Skynet klant valt het regelmatig voor dat er tegen het einde van de maand
een melding in mijn mailbox land die ik liever niet zie.
Een boodschap die aankondigt dat ter huize het verstrekte download volume bijna
overschreden is.  Om de goede vrede te bewaren check ik in die periode
regelmatig de volumemeter op de Skynet website.  Dit voorkomt een situatie
waarin pa, ma of broer het in de vroege uren van het weekend nodig acht
om me te wekken en te klagen over de trage verbinding.</p>
<p>Aangezien dit redelijk veel muisklikken vereist (dat is met de meeste
handelingen op websites nu eenmaal zo), kwam het idee in me op om het
<a class="reference" href="http://www.telemeter.be">telemeter programma</a> (waarmee Telenet klanten hun volume kunnen controleren)
, aan te passen zodat het met de Skynet website overweg kan.</p>
<p>Telemeter bleek in de programmeertaal C geschreven te zijn, maar een dergelijk
programma in C schrijven leek me nogal overkill.</p>
</div>
<div class="section">
<h1><a id="skymeter-1-2" name="skymeter-1-2">Skymeter 1 &amp; 2</a></h1>
<p>Oorspronkelijk heb ik Skymeter in PERL geschreven, maar toen ik de taal
Python ontdekte, stelde ik vast dat Skymeter veel beknopter en eleganter
geschreven kon worden in Python, deze heeft namelijk standaard http
functionaliteit aan boord heeft (met SSL support).</p>
<p>Ik heb de Skymeter die in python geschreven is Skymeter 2.0 gedoopt.
Skymeter 1 blijft beschikbaar, maar ondertussen is Skymeter 2 beter
ontwikkeld en heeft deze het minst ruwe kanten.</p>
</div>
<div class="section">
<h1><a id="screenshots" name="screenshots">Screenshots</a></h1>
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
</td></tr></table><table style="border: 0px;">
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
</td></tr></table></div>
<div class="section">
<h1><a id="configuratie" name="configuratie">Configuratie</a></h1>
<p>Skymeter dient de username en het paswoord van je Skynet abonnement te weten,
deze informatie dient in het configuratiebestand te worden geplaatst.</p>
<p>Dit bestand moet de naam <tt class="docutils literal"><span class="pre">.skymeterrc</span></tt> te hebben, en zich in de home folder
van de gebruiker te bevinden die Skymeter wil gebruiken.
Het bestand dient deze twee lijnen te bevatten</p>
<pre class="literal-block">
user jegebruikersnaam
pass jewachtwoord
</pre>
<p>Dit wijst zichzelf uit.</p>
<p>Het is aangeraden dit bestand onleesbaar te maken voor andere gebruikers
van uw computer: <tt class="docutils literal"><span class="pre">chmod</span> <span class="pre">go-rwx</span> <span class="pre">~/.skymeterrc</span></tt></p>
</div>
<div class="section">
<h1><a id="skymeter-2" name="skymeter-2">Skymeter 2</a></h1>
<p>Om de achter de huidige stand van de volumemeter te polsen, moet je gewoon het
commando <tt class="docutils literal"><span class="pre">skymeter</span></tt> uitvoeren.</p>
<pre class="literal-block">
thomas&#64;whirlpool thomas $ skymeter
Volume meters for xxxxxxxx on Mon, xx Jul 2008 14:19:51
BasicMeter: 33%: 8 GB 311 MB of 25 GB
</pre>
<p>Er is een grafische interface met de naam <tt class="docutils literal"><span class="pre">tkskymeter</span></tt>.</p>
</div>
<div class="section">
<h1><a id="broken-by-design" name="broken-by-design">Broken by design...</a></h1>
<p>Skymeter gebruikt reguliere expressies op de HTML pagina van
de volumemeter webpagina om achter de informatie te komen.
Telkens dat Skynet de constructie van de betreffende zinnen
met de meterstand wijzigt, dient de patroonherkenning die gebruikt
wordt om de nuttige informatie te achterhalen dus onbruikbaar,
en is Skymeter aan onderhoud toe.</p>
<p>Aangezien ik soms gedurende lange periodes Skymeter niet zelf gebruik,
kan het een hele tijd duren voor dat ik merk dat de regex aan
liefde toe is.  Het valt dus af en toe voor dat Skymeter onbruikbaar is,
en een nieuwe release op zich laat wachten.</p>
<p>Als u zelf verstand heeft van PERL en/of reguliere expressies,  stel ik patches
erg op prijs.  Ook kan u helpen door bij Skynet te lobbyen en ze aan te sporen
de meterstand in XML(-RPC) aan te bieden.</p>
</div>
<div class="section">
<h1><a id="ten-slotte" name="ten-slotte">Ten slotte...</a></h1>
<p>Ik geef de code ook vrij (onder de GPL), zodat u het script kan bestuderen,
aanpassen en uitbreiden naar uw wensen. (Wel zou ik het heel fijn vinden dat
bugs gemeld worden, net als verbeteringen die u hebt aangebracht en u graag
meeverspreid wilt zien in de code die ik op mijn site aanbied.)</p>
<p>Ik zou graag alle mensen willen bedanken die me patches hebben gemaild, en me
raad gegeven hebben bij het schrijven van Skymeter.  (zie het bestand met de
naam THANKS in de tarball)</p>
</div>
<div class="section">
<h1><a id="gebruik-skymeter-1" name="gebruik-skymeter-1">Gebruik Skymeter 1</a></h1>
<div class="caution">
<p class="first admonition-title">Caution!</p>
<p class="last">Het is aangeraden Skymeter 2 te gebruiken, deze instructies voor de
oude versie blijven hier als referentie.</p>
</div>
<div class="section">
<h2><a id="sporadisch-gebruik" name="sporadisch-gebruik">Sporadisch gebruik</a></h2>
<p>Om de achter de huidige stand van de volumemeter te polsen, moet je gewoon het
commando <tt class="docutils literal"><span class="pre">skymeter</span></tt> uitvoeren.</p>
<pre class="literal-block">
thomas&#64;whirlpool thomas $ skymeter
Aanvraag... Inloggen... Parsen... Ok!
Basisvolume [1.19 / 10]
Lopende volumepack: [3.71 / 5]
</pre>
</div>
<div class="section">
<h2><a id="automatisch" name="automatisch">Automatisch</a></h2>
<p>In GNU/Linux worden elke keer een PPP(gebruikt bij ADSL) verbinding tot stand
komt de scripts in <tt class="docutils literal"><span class="pre">/etc/ppp/ip-up.d/</span></tt> uitgevoerd.  Hier kun je bijvoorbeeld
een script zoals het volgende plaatsen:</p>
<pre class="literal-block">
#!/bin/bash
/usr/local/bin/skymeter --put /var/www/index.html
</pre>
<p>Dit zorgt er voor dat Skymeter de informatie over de volumemeter
(wel als text file!) schrijft naar <tt class="docutils literal"><span class="pre">/var/www/index.html</span></tt>.
Dat kan eventueel door een webserver (met als <em>documentroot</em> <tt class="docutils literal"><span class="pre">/var/www/</span></tt>)
gedeeld worden over het LAN.  Zo kan de hele familie de meterstand
snel raadplegen.</p>
<p>Het argument <tt class="docutils literal"><span class="pre">--put</span></tt> zorgt er voor dat een bestand wordt aangemaakt dat er
als volgt uitziet:</p>
<pre class="literal-block">
Basisvolume: 0.34 / 10
Volumepack: 3.71 / 5
</pre>
<p>Het bestand kan dus gemakkelijk door zelfgeschreven scripts verwerkt worden.</p>
</div>
<div class="section">
<h2><a id="dependencies" name="dependencies">Dependencies</a></h2>
<ul class="simple">
<li>curl: Skymeter maakt gebruik van de stand alone versie van curl,
een curl binary met SSL support is nodig.</li>
<li>PERL: Skymeter heeft de PERL interpreter nodig, deze is op de
meeste Linux systemen standaard aanwezig.</li>
</ul>
</div>
</div>
<div class="section">
<h1><a id="verwanten" name="verwanten">Verwanten</a></h1>
<ul class="simple">
<li><a class="reference" href="http://n00.be/widgets/">SkyMonitor</a>, De Mac OSX-incarnatie van Skymeter.
Een must-have voor Mac gebruikers.</li>
<li><a class="reference" href="http://www.telemeter.be">telemeter</a>, Voor Telenet klanten.</li>
</ul>
</div>
</div>