Jäsenyys
########
:date: 2015-10-07 18:01
:tags: info
:title: Jäsenyys
:category: info
:slug: jasenyys
:authors: Jarkko Saltiola

Hacklab Jyväskylän kerhotilan vuokra katetaan kuukausittaisista jäsenmaksuista. Jäsenmaksu on jaettu kahteen luokkaan.

Normaali jäsenmaksu on 10€/kk, joka oikeuttaa käyntiin kerhoilloissa ja tavaroiden säilyttämiseen Hacklabilla. Harrastetilalle on mahdollista saada myös oma avain jolla sisään pääsee koska tahansa. Avaimellisen jäsenyyden hinta on 20€/kk. 

Kerhoiltoihin voi vapaasti tulla tutustumaan jos jäsenyys kiinnostaa. Varsinaiset jäsenhakemukset pyydetään lähettämään `hallitukselle <yhteystiedot.html>`_ sähköpostilla tai allaolevalla lomakkeella:

.. raw:: html

    <form action="https://formspree.io/hacklab-jkl-hallitus@googlegroups.com" method="POST" class="join" autocomplete="on">
    <input type="hidden" name="_subject" value="Jyväskylän Hacklabin jäsenhakemus" />
    <input type="hidden" name="_next" value="http://jyvaskyla.hacklab.fi/pages/member_thanks.html" />
    <input type="hidden" name="languages" id="language" />
    <div>
    <label for="name">Nimi:</label>
    <input type="text" id="name" name="name" required autocomplete="name">
    </div><div>
    <label for="email">Sähköposti:</label>
    <input type="email" id="email" name="email" required autocomplete="email">
    </div><div>
    <label for="city">Kotikunta:</label>
    <input type="text" id="city" name="city" required autocomplete="address-level2" value="Jyväskylä">
    </div><div>
    <label for="irc">IRC-nimimerkki (jos on):</label>
    <input type="text" name="irc" id="irc" autocomplete="nickname">
    </div><div>
    <input type="radio" value="normal" name="membership" id="normal" accesskey="P" checked="checked"/>
    <label for="normal">Perusjäsenyys 10€/kk</label>
    </div><div>
    <input type="radio" value="key" name="membership" id="key" accesskey="A" />
    <label for="key">Avainjäsenyys 20€/kk</label>
    </div>
    <input id="liity" type="submit" value="Liity jäseneksi">
    </form> 
    <script type="text/javascript">document.getElementById("language").value = navigator.languages;</script>
