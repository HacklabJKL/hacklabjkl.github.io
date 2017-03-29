Jäsenyys
########
:date: 2015-10-07 18:01
:tags: info
:title: Jäsenyys
:category: info
:slug: jasenyys
:authors: Jarkko Saltiola

Hacklab Jyväskylän kerhotilan vuokra katetaan kuukausittaisista jäsenmaksuista. Jäsenmaksu on jaettu kahteen luokkaan.

Normaali jäsenmaksu on 10€/kk, joka oikeuttaa käyntiin kerhoilloissa
ja tavaroiden säilyttämiseen Hacklabilla. Harrastetilalle on
mahdollista saada myös oma avain jolla sisään pääsee koska
tahansa. Avaimellisen jäsenyyden hinta on 20€/kk.

Voit hakea myös alennettua jäsenmaksua, jos taloudellinen tilanteesi
on heikko. Tällöin hinta on 5€/kk ensimmäisen 12 kuukauden ajan, jonka
jälkeen hinta on 10€/kk. Alennettu jäsenmaksuluokka oikeuttaa samoihin
etuihin kuin normaali jäsenyys. Hallituksen jäsenvastaava pyytää
tarvittaessa perustelut alennukselle.

Kerhoiltoihin voi vapaasti tulla tutustumaan jos jäsenyys kiinnostaa. Varsinaiset jäsenhakemukset pyydetään lähettämään `hallitukselle <yhteystiedot.html>`_ sähköpostilla tai allaolevalla lomakkeella:

.. raw:: html

    <form action="https://formspree.io/hacklab-jkl-hallitus@googlegroups.com" method="POST" class="join" autocomplete="on">
    <input type="hidden" id="subject" name="_subject" value="Jyväskylän Hacklabin jäsenhakemus" />
    <input type="hidden" name="_next" value="http://jyvaskyla.hacklab.fi/pages/member_thanks.html" />
    <input type="hidden" name="languages" id="language" />
    <div>
    <label class="leftlabel" for="name">Nimi:</label>
    <input type="text" id="name" name="name" required autocomplete="name">
    </div><div>
    <label class="leftlabel" for="email">Sähköposti:</label>
    <input type="email" id="email" name="email" required autocomplete="email">
    </div><div>
    <label class="leftlabel" for="city">Kotikunta:</label>
    <input type="text" id="city" name="city" required autocomplete="address-level2" value="Jyväskylä">
    </div><div>
    <label class="leftlabel" for="irc">IRC-nimimerkki (jos on):</label>
    <input type="text" name="irc" id="irc" autocomplete="nickname">
    </div>
    <div class="control-container">
        <div>
        <input type="radio" value="discount" name="membership" id="discount" accesskey="L" />
        <label for="discount">Alennettu jäsenyys 5€/kk</label>
        </div>
        <div>
        <input type="radio" value="normal" name="membership" id="normal" accesskey="P" checked="checked"/>
        <label for="normal">Perusjäsenyys 10€/kk</label>
        </div>
        <div>
        <input type="radio" value="key" name="membership" id="key" accesskey="A" />
        <label for="key">Avainjäsenyys 20€/kk</label>
        </div>
    </div>
    <div class="control-container" id="discount-motivation-div">
        <label for="discount-motivation" class="block">Perustelu alennetun jäsenmaksun
        hakemiselle:</label>
        <textarea id="discount-motivation" name="discount-motivation" maxlength="1000" cols="65" rows="10"></textarea>
    </div>
    <input id="liity" type="submit" value="Liity jäseneksi">
    </form>
    <script type="text/javascript">
        document.getElementById("language").value = navigator.languages;
        document.getElementById("name").onchange = function() {
            document.getElementById("subject").value = "Jyväskylän Hacklabin jäsenhakemus / "
                                                        + document.getElementById("name").value;
        }

        function showHideDiscountMotivation() {
            document.getElementById("discount-motivation-div").style.display =
                document.getElementById("discount").checked ? "block" : "none";
        }
        showHideDiscountMotivation();

        document.getElementsByName("membership").forEach(function(elem) {
            elem.addEventListener("change", showHideDiscountMotivation);
        });
    </script>
