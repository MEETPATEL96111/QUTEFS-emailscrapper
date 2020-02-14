import re
emailRegex = re.compile(r'''
#example :
#something-.+_@somedomain.com
(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])
''', re.VERBOSE)
        
#Extacting Emails


tex = '''
{"_id":"Sportsman Hotel","email":[""],"email0":["\"[]\""]}
{"_id":"Morningside Festival Association","email":["\"[\"morningsidestalls@gmail.com\""],"email0":["\"morningsidestalls@gmail.com\""]}
{"_id":"Slingshot","email":["\"[]\""],"email0":["\"[]\""]}
{"_id":"GenreCon.","email":[""],"email0":["\"[]\""]}
{"_id":"Johnny Ringo's Queensland","email":[""],"email0":["\"[]\""]}
{"_id":"Brisbane Writers Festival","email":["","\"[\"info@uplit.com.au\""],"email0":["\"[\"maryjane@website.com\"]\"","\"info@uplit.com.au\""]}
{"_id":"Stones Corner Hotel","email":[""],"email0":["\"[\"stones.corner.hotel@alhgroup.com.au\""]}
{"_id":"Alderley Arms Hotel","email":["\"[\"alderley.arms.hotel@alhgroup.com.au\""],"email0":["\"alderley.arms.hotel@alhgroup.com.au\""]}
{"_id":"McDonald's Queen Street","email":["\"[]\""],"email0":["\"[]\""]}
{"_id":"Jetts Fortitude Valley 24/7","email":["\"[]\""],"email0":["\"[]\""]}
{"_id":"Luxury Japan Travel","email":["\"[\"bookings@luxuryjapantravel.com\""],"email0":["\"bookings@luxuryjapantravel.com\""]}
{"_id":"South Bank's Christmas Village","email":["\"[]\""],"email0":[""]}
{"_id":"Science Of Fitness","email":[""],"email0":["\"[\"info@scienceoffitness.com.au\""]}
{"_id":"Blute's Bar","email":["\"[\"blutesbar@gmail.com\""],"email0":["\"jesse@thehappyhorsemen.com\""]}
{"_id":"Royal Queensland Show - Ekka","email":[""],"email0":["\"[\"enquiries@ekka.com.au\""]}
{"_id":"AwesomeX Karaoke Hire","email":[""],"email0":["\"[\"//8b4e078a51d04e0e9efdf470027f0ec1@sentry.wixpress.com\""]}
{"_id":"Brisbane Exhibition Grounds","email":[""],"email0":["\"[]\""]}
{"_id":"Sussan (Brisbane CBD)","email":["\"[\"//cdn.jsdelivr.net/npm/slick-carousel@1.8.1\""],"email0":["\"//cdn.jsdelivr.net/npm/slick-carousel@1.8.1\""]}
{"_id":"The Paddo","email":["\"[\"//cdn.jsdelivr.net/npm/bootstrap@4.1.1\""],"email0":["\"//cdn.jsdelivr.net/npm/magnific-popup@1.1.0\""]}
{"_id":"Strike Bowling Wintergarden","email":["\"[\"//unpkg.com/vue@2.4.3\""],"email0":["\"//unpkg.com/vee-validate@2.0.0-rc.17\"]\""]}
{"_id":"Indoz Festival","email":[""],"email0":[""]}
{"_id":"OMFGs Adult Lounge","email":["\"[]\""],"email0":["\"[\"fletcher@peabodytrading.com.au\""]}
{"_id":"Fate Fitness","email":[""],"email0":[""]}
{"_id":"Taiwan Festival","email":[""],"email0":["\"[\"info@taiwanfestival.com.au\""]}
{"_id":"Jetts Brisbane CBD","email":[""],"email0":["\"[]\""]}
{"_id":"F45 Training","email":[""],"email0":["\"[\"//cdn.jsdelivr.net/npm/slick-carousel@1.8.1\""]}
{"_id":"Brisbane Powerhouse","email":["\"[\"/favicon/favicon@2x.png\"]\""],"email0":["\"[\"/favicon/favicon@2x.png\"]\""]}
{"_id":"ZIMMERMANN","email":[""],"email0":["\"[\"info@zimmermannwear.com\""]}
{"_id":"Little Big House","email":["\"[\"littlebighouse@solotel.com.au\""],"email0":["\"littlebighouse@solotel.com.au\"]\""]}
{"_id":"Cue Wintergarden","email":["\"[]\""],"email0":["\"[]\""]}
{"_id":"Witchery Toombul","email":["\"[]\""],"email0":["\"[]\""]}
{"_id":"Big Fork Theatre","email":["\"[\"contact@bigforktheatre.com\""],"email0":["\"bigforktheatre@gmail.com\""]}
{"_id":"Slams Karaoke Jukebox Hire","email":["\"[]\""],"email0":["\"[]\""]}
{"_id":"Shadow Lounge","email":[""],"email0":["\"[]\""]}
{"_id":"Le Festival - Brisbane French Festival","email":["\"[\"info@lefestival.com.au\""],"email0":["\"info@lefestival.com.au\""]}
{"_id":"Jacaranda Gin Fest","email":["\"[\"impallari@gmail.com\""],"email0":["\"team@latofonts.com\""]}
{"_id":"Sportsgirl","email":["\"[]\""],"email0":["\"[]\""]}
{"_id":"South Bank Fitness Centre","email":["\"[]\""],"email0":["\"[\"example@yourdomain.com\"]\""]}
{"_id":"Fat Louies","email":[""],"email0":["\"[]\""]}
{"_id":"永乐汇KTV","email":[""],"email0":[""]}
{"_id":"The Milk Factory Kitchen & Bar","email":["\"[\"me@mywixsite.com\""],"email0":["\"//8b4e078a51d04e0e9efdf470027f0ec1@sentry.wixpress.com\""]}
{"_id":"Hungry Jack's Burgers Beak House","email":[""],"email0":["\"[\"/assets/images/pin@3x.png\"]\""]}
{"_id":"Sit Down Comedy Club","email":["\"[\"tellmemore@standup.com.au\""],"email0":["\"tellmemore@standup.com.au\"]\""]}
{"_id":"Digby's Menswear","email":[""],"email0":["\"[]\""]}
{"_id":"Anytime Fitness (Brisbane CBD)","email":["\"[]\""],"email0":["\"[]\""]}
{"_id":"Retro's Fortitude Valley","email":[""],"email0":["\"[\"//8b4e078a51d04e0e9efdf470027f0ec1@sentry.wixpress.com\""]}
{"_id":"Dymocks Brisbane","email":[""],"email0":["\"[\"brisbane@dymocks.com.au\""]}
{"_id":"Snap Fitness 24/7 Brisbane CBD","email":["\"[\"inquiries@snapfitness.com\""],"email0":["\"inquiries@snapfitness.com\""]}
{"_id":"Shaver Shop","email":[""],"email0":["\"[\"customerservice@shavershop.com.au\""]}
{"_id":"Albatross Tours","email":[""],"email0":["\"[]\""]}
{"_id":"The Beat Megaclub","email":["\"[\"info@thebeatmegaclub.com.au\"]\""],"email0":[""]}
{"_id":"Katies","email":[""],"email0":["\"[\"//cdn.jsdelivr.net/npm/slick-carousel@1.8.1\""]}
{"_id":"The Palace Karaoke and Lounge Bar","email":["\"[\"enquiries@thepalacelounge.com.au\"]\""],"email0":["\"[]\""]}
{"_id":"The Comedy Empire","email":["\"[]\""],"email0":["\"[\"username@example.com\""]}
{"_id":"Witchery Fortitude Valley","email":["\"[]\""],"email0":["\"[]\""]}
{"_id":"Hanwoori Restaurant","email":[""],"email0":["\"[]\""]}
{"_id":"DISSH","email":[""],"email0":["\"[]\""]}
{"_id":"F1rst Class Fitness","email":["\"[\"info@f1rstclassfitness.com.au\"","\"[\"info@f1rstclassfitness.com.au\""],"email0":["\"info@f1rstclassfitness.com.au\"]\"","\"info@f1rstclassfitness.com.au\"]\""]}
{"_id":"bounce fitness","email":["\"[]\""],"email0":["\"[]\""]}
{"_id":"Newmarket Hotel","email":["\"[\"newmarket.hotel@alhgroup.com.au\""],"email0":["\"newmarket.hotel@alhgroup.com.au\""]}
{"_id":"Contra Store","email":[""],"email0":["\"[]\""]}
{"_id":"Sky and Lotus","email":[""],"email0":["\"[]\""]}
{"_id":"URBBANA Brisbane","email":["\"[\"admin@urbbana.com.au\""],"email0":["\"admin@urbbana.com.au\""]}
{"_id":"Music City","email":[""],"email0":["\"[\"musiccity@tnaru.net\"]\""]}
{"_id":"Snap Fitness 24/7 Brisbane City","email":["\"[\"inquiries@snapfitness.com\""],"email0":["\"inquiries@snapfitness.com\""]}
{"_id":"Dizzy - Comedy Hypnotist","email":[""],"email0":["\"[]\""]}
{"_id":"BWS MacArthur Central","email":[""],"email0":[""]}
{"_id":"Cotton On","email":[""],"email0":["\"[]\""]}
{"_id":"Brisbane Comedy Festival","email":[""],"email0":["\"[\"/dist/images/logo/bcf@2x.png\""]}
{"_id":"Nest Nappies","email":["\"[\"info@nestnappies.com.au\""],"email0":["\"info@nestnappies.com.au\""]}
{"_id":"T.M.Lewin","email":["\"[\"customer.services@tmlewin.co.uk\"]\""],"email0":["\"[\"customer.services@tmlewin.co.uk\"]\""]}
{"_id":"Fitness First Brisbane CBD","email":["\"[]\""],"email0":["\"[]\""]}
{"_id":"Vinnies","email":[""],"email0":[""]}
{"_id":"Figure Fitness","email":[""],"email0":[""]}
{"_id":"Lost Bar and Nightclub","email":[""],"email0":["\"[]\""]}
{"_id":"colette by colette hayman - Queen Street","email":["\"[\"customercare@colette.com.au\""],"email0":["\"customercare@colette.com.au\""]}
{"_id":"Sunrover Tours","email":[""],"email0":["\"[\"tours@sunrover.com.au\""]}
{"_id":"Sunlit Sounds music festival","email":[""],"email0":["\"[]\""]}
{"_id":"BWS George Street","email":[""],"email0":[""]}
{"_id":"Noritor Bar and Restaurant","email":[""],"email0":[""]}
{"_id":"Callan Shirts & Callan Designs","email":[""],"email0":[""]}
{"_id":"Tree of Life (Brisbane)","email":["\"[\"customer@treeoflife.com.au\""],"email0":["\"customer@treeoflife.com.au\""]}
{"_id":"Izabel + Sebastian","email":["\"[]\""],"email0":["\"[]\""]}
{"_id":"Queensland Poetry Festival","email":["\"[\"info@queenslandpoetryfestival.com\""],"email0":["\"info@queenslandpoetryfestival.com\""]}
{"_id":"The Tivoli","email":["\"[\"nickcave@thebadseeds.com\""],"email0":["\"nickcave@thebadseeds.com\""]}
{"_id":"Smiggle","email":["\"[\"obile@0x.jpg\""],"email0":["\"esktop@1x.png\""]}
{"_id":"Calamvale Carnival","email":[""],"email0":[""]}
{"_id":"sass & bide queensplaza","email":["\"[\"customercare@sassandbide.com\""],"email0":["\"customercare@sassandbide.com\""]}
{"_id":"Australia the Gift","email":["\"[]\"","\"[]\""],"email0":["\"[]\"","\"[]\""]}
{"_id":"SHEIKE Wintergarden","email":["\"[]\""],"email0":["\"[]\""]}
{"_id":"InsideAsia Tours Australia Branch","email":[""],"email0":[""]}
{"_id":"Olympia Body Transformation Sanctuary","email":["\"[\"theteam@olympiatransformations.com.au\"]\""],"email0":["\"[\"theteam@olympiatransformations.com.au\"]\""]}
{"_id":"Ally Fashion (Brisbane CBD)","email":["\"[\"allyinfo@allyfashion.com\""],"email0":["\"allyinfo@allyfashion.com\""]}
{"_id":"Exhibition Street","email":[""],"email0":[""]}
{"_id":"Contrasts of Brisbane Walking Tour","email":[""],"email0":[""]}
{"_id":"Brisbane 4WD Day Tours","email":["\"[\"bookings@southerncrosstours.com.au\"]\""],"email0":["\"[]\""]}
{"_id":"Kangaroo Segway Tours","email":["\"[]\""],"email0":["\"[]\""]}
{"_id":"The Met","email":[""],"email0":["\"[\"functions@themet.com.au\""]}
{"_id":"MW Tours Pty Ltd","email":["\"[\"sales@mwtours.com.au\""],"email0":["\"sales@mwtours.com.au\""]}
{"_id":"Queensland Music Festival","email":["\"[\"//8b4e078a51d04e0e9efdf470027f0ec1@sentry.wixpress.com\""],"email0":["\"//static.parastorage.com/unpkg/core-js-bundle@3.2.1\""]}
{"_id":"Soleil Pool Bar","email":["\"[\"info@soleilpoolbar.com.au\""],"email0":["\"info@soleilpoolbar.com.au\"]\""]}
{"_id":"World Expeditions","email":[""],"email0":["\"[]\""]}
{"_id":"lululemon","email":["\"[\"gec@lululemon.com.au\""],"email0":["\"gec@lululemon.com.au\""]}
{"_id":"Ollie's Place Brisbane DFO","email":[""],"email0":["\"[\"info@olliesplace.com.au\""]}
{"_id":"Nyanda Cultural Tours","email":["\"[]\""],"email0":["\"[]\""]}
{"_id":"Italian Week","email":[""],"email0":[""]}
{"_id":"Brisbane Trike Tours","email":["\"[]\""],"email0":["\"[]\""]}
{"_id":"Furlani Fitness","email":["\"[\"//8b4e078a51d04e0e9efdf470027f0ec1@sentry.wixpress.com\""],"email0":["\"//static.parastorage.com/unpkg/core-js-bundle@3.2.1\""]}
{"_id":"The Reject Shop Queen St","email":["\"[]\""],"email0":["\"[]\""]}
{"_id":"Ghost Tours","email":["\"[]\""],"email0":["\"[]\""]}
{"_id":"Jimmy's On The Mall","email":["\"[\"jimmys@jimmysonthemall.com.au\""],"email0":["\"jimmys@jimmysonthemall.com.au\"]\""]}
{"_id":"Walk Brisbane","email":["\"[]\""],"email0":["\"[]\""]}
{"_id":"Botanica Real Food","email":["\"[\"alison@botanicarealfood.com.au\"]\"",""],"email0":["\"[]\"","\"[]\""]}
{"_id":"East West Food","email":[""],"email0":[""]}
{"_id":"Brisbane Sightseeing Tours - Urban Adventures","email":[""],"email0":[""]}
{"_id":"Buffalo Bar","email":["\"[\"//buffalobar.com.au/wp-content/uploads/2018/08/bb-footer-logo@2x.png\""],"email0":["\"info@buffalobar.com.au\""]}
{"_id":"Laruche","email":[""],"email0":["\"[]\""]}
{"_id":"Tattersall's Arcade","email":[""],"email0":["\"[\"ceo@tattersallsclub.com\""]}
{"_id":"GPO Hotel","email":["\"[]\""],"email0":["\"[]\""]}
{"_id":"Guest House Paradiso","email":["\"[]\""],"email0":["\"[]\""]}
{"_id":"Birdees","email":["\"[\"hello@birdees.com\""],"email0":["\"hello@birdees.com\""]}
{"_id":"Bubblebubs Modern Cloth Nappies","email":[""],"email0":["\"[\"cs@bubblebubs.com.au\""]}
{"_id":"Queensland Performing Arts Centre","email":[""],"email0":["\"[]\""]}
{"_id":"Drunken Monkey","email":[""],"email0":["\"[]\""]}
{"_id":"Alannah Hill - Broadway","email":[""],"email0":["\"[\"johndoe@domain.com\""]}
{"_id":"tookoonooka crater","email":[""],"email0":[""]}
{"_id":"Lennons Restaurant & Bar","email":[""],"email0":["\"[]\""]}
{"_id":"Brisbane Jazz Club","email":["\"[\"music@brisbanejazzclub.com.au\""],"email0":["\"music@brisbanejazzclub.com.au\""]}
{"_id":"George's Paragon Seafood Restaurant","email":[""],"email0":["\"[]\""]}
{"_id":"Mix Karaoke","email":[""],"email0":[""]}
{"_id":"Candy Club","email":["\"[\"functions@candyclub.com.au\""],"email0":["\"functions@candyclub.com.au\"]\""]}
{"_id":"Prohibition Brisbane","email":["\"[\"info@prohibitionbrisbane.com.au\""],"email0":["\"info@prohibitionbrisbane.com.au\""]}
{"_id":"Comedy Hypnotist Andy Vening","email":[""],"email0":["\"[\"//8b4e078a51d04e0e9efdf470027f0ec1@sentry.wixpress.com\""]}
{"_id":"X-Wing Australia Pty Ltd","email":["\"[\"sales@xwing.com.au\""],"email0":["\"sales@xwing.com.au\""]}
{"_id":"Press Club","email":["\"[]\""],"email0":[""]}
{"_id":"Anytime Fitness","email":["\"[]\""],"email0":["\"[]\""]}
{"_id":"FAMOUS","email":[""],"email0":["\"[\"//8b4e078a51d04e0e9efdf470027f0ec1@sentry.wixpress.com\""]}
{"_id":"Players Brisbane","email":[""],"email0":["\"[\"info@playersbris.com.au\""]}
{"_id":"The Victory Hotel","email":["\"[\"victory.hotel@alhgroup.com.au\""],"email0":["\"victory.hotel@alhgroup.com.au\""]}
{"_id":"AQUITAINE","email":["\"[\"enquiries@aquitainebrasserie.com.au\""],"email0":["\"enquiries@aquitainebrasserie.com.au\""]}
{"_id":"Roti Place","email":[""],"email0":["\"[]\""]}
{"_id":"The Brunswick Hotel","email":["\"[\"brunswick.hotel@alhgroup.com.au\""],"email0":["\"brunswick.hotel@alhgroup.com.au\""]}
{"_id":"Black Fire Restaurant Brisbane","email":["\"[\"bookings@blackfirebrisbane.com.au\""],"email0":["\"bookings@blackfirebrisbane.com.au\""]}
{"_id":"Stokehouse Q","email":["\"[\"info@stokehouseq.com.au\""],"email0":["\"info@stokehouseq.com.au\""]}
{"_id":"Donna Chang","email":["\"[]\""],"email0":["\"[]\""]}
{"_id":"Ally Fashion","email":["\"[\"allyinfo@allyfashion.com\""],"email0":["\"allyinfo@allyfashion.com\""]}
{"_id":"The Pool Terrace + Bar","email":[""],"email0":["\"[]\""]}
{"_id":"Grill'd Albert Street","email":["\"[\"/images/icons/footer-grilld-love@2x.png\"]\""],"email0":["\"[\"/images/icons/footer-grilld-love@2x.png\"]\""]}
{"_id":"Bacchus","email":["\"[\"info@bacchussouthbank.com.au\"]\""],"email0":["\"[]\""]}
{"_id":"Einbunpin Festival","email":["\"[\"ard@bcc.qld.gov.au\""],"email0":["\"ard@bcc.qld.gov.au\""]}
{"_id":"The Gresham Bar","email":[""],"email0":["\"[\"gatherings@thegresham.com.au\""]}
{"_id":"Super Whatnot","email":["\"[\"hello@superwhatnot.com\""],"email0":["\"hello@superwhatnot.com\"]\""]}
{"_id":"Verve Restaurant & Ciderhouse","email":["\"[\"//8b4e078a51d04e0e9efdf470027f0ec1@sentry.wixpress.com\""],"email0":["\"//static.parastorage.com/unpkg/core-js-bundle@3.2.1\""]}
{"_id":"Red Rooster","email":["\"[]\""],"email0":["\"[]\""]}
{"_id":"JPT Tour Group","email":[""],"email0":["\"[]\""]}
{"_id":"Twelfth Night Theatre","email":[""],"email0":["\"[\"twelfthnighttheatre@bigpond.com\"]\""]}
{"_id":"Mr. Bunz","email":[""],"email0":["\"[\"admin@mrbunz.com.au\"]\""]}
{"_id":"Public Quarter","email":["\"[]\""],"email0":["\"[]\""]}
{"_id":"Kadoya Japanese Restaurant","email":[""],"email0":["\"[\"robert@broofa.com\"]\""]}
{"_id":"Club XOXO","email":[""],"email0":[""]}
{"_id":"An Cafe Vietnamese Street Food","email":[""],"email0":["\"[\"//8b4e078a51d04e0e9efdf470027f0ec1@sentry.wixpress.com\""]}
{"_id":"Queensland Club","email":[""],"email0":["\"[]\""]}
{"_id":"Frequent Fitness","email":[""],"email0":[""]}
{"_id":"Kinn-Imm Thai Hawker Food","email":[""],"email0":["\"[\"kinnimm.queenplaza@gmail.com\"]\""]}
{"_id":"Audio Tours Australia: Brisbane","email":[""],"email0":[""]}
{"_id":"The Walnut Restaurant and Lounge Bar","email":["\"[]\""],"email0":["\"[]\""]}
{"_id":"Soul Origin","email":["\"[]\"","\"[\"myercentre@soulorigin.com.au\""],"email0":["\"[]\"","\"myercentre@soulorigin.com.au\""]}
{"_id":"Fraser Explorer Tours","email":[""],"email0":[""]}
{"_id":"charsmy Food & Bottle Shop","email":["\"[]\""],"email0":["\"[]\""]}
{"_id":"FunkGlam","email":[""],"email0":[""]}
{"_id":"The Lab","email":["\"[\"treasuryfunctions@star.com.au\""],"email0":["\"treasuryfunctions@star.com.au\"]\""]}
{"_id":"The Pancake Manor","email":["\"[\"//8b4e078a51d04e0e9efdf470027f0ec1@sentry.wixpress.com\""],"email0":["\"//static.parastorage.com/unpkg/core-js-bundle@3.2.1\""]}
{"_id":"Fat Noodle","email":["\"[\"hirnbeck@star.com.au\""],"email0":["\"ing@star.com.au\"]\""]}
{"_id":"Rock N Roll Kebab Pizza - Low Price Pizza","email":["http://www.rocknrollkebabpizza.com.au/"],"email0":["https://maps.google.com/?cid=405749267078995819"]}
{"_id":"Embassy Bar & Kitchen","email":["\"[\"info@embassyhotel.net.au\"]\""],"email0":["\"[]\""]}
{"_id":"LiveWire 24/7 Sports Bar","email":["\"[\"hirnbeck@star.com.au\""],"email0":["\"hirnbeck@star.com.au\""]}
{"_id":"TURQUOISE Kebab & Pizza","email":[""],"email0":["\"[]\""]}
{"_id":"Anywhere Festival","email":["\"[]\""],"email0":["\"[]\""]}
{"_id":"Lexington Queen","email":[""],"email0":[""]}
{"_id":"Beach House Bar & Grill CBD","email":["\"[]\""],"email0":["\"[]\""]}
{"_id":"Cross Country Tours","email":["\"[\"info@aaj.com.au\""],"email0":["\"info@aaj.com.au\""]}
{"_id":"Moo Moo The Wine Bar and Grill","email":[""],"email0":["\"[\"brisbane/wp-content/themes/moo-moo/static/img/logo-1@2x.png\""]}
{"_id":"Club Vixen - Gentleman's Bar and Lounge","email":[""],"email0":["\"[\"//8b4e078a51d04e0e9efdf470027f0ec1@sentry.wixpress.com\""]}
{"_id":"charber 29 Cruise Club","email":[""],"email0":["\"[\"club29fun@gmail.com\""]}
{"_id":"Treasury Casino and Hotel Brisbane","email":["\"[\"hirnbeck@star.com.au\""],"email0":["\"hirnbeck@star.com.au\""]}
{"_id":"Botanic Bar","email":["\"[\"pcanning@qutguild.com\""],"email0":["\"pcanning@qutguild.com\"]\""]}
{"_id":"Priceline Pharmacy King George Square","email":[""],"email0":[""]}
{"_id":"Fab Kebabs","email":[""],"email0":[""]}
{"_id":"Blackmarket Bar & Grill","email":["\"[\"//8b4e078a51d04e0e9efdf470027f0ec1@sentry.wixpress.com\""],"email0":["\"//static.parastorage.com/unpkg/core-js-bundle@3.2.1\""]}
{"_id":"QUT Gardens Point Fitness and Aquatic","email":[""],"email0":["\"[\"brisbane@ymca.org.au\"]\""]}
{"_id":"KG Bar","email":[""],"email0":["\"[\"8784-re2@accor.com\""]}
{"_id":"Irish Murphy's","email":[""],"email0":["\"[\"danielle@irishmurphys.com.au\""]}
{"_id":"st Fitness Professionals-Sports-Fitness-Coach-Personal-Strength-Training-School-Brisbane City","email":[""],"email0":[""]}
{"_id":"Bull Bar restaurant","email":["\"[]\""],"email0":["\"[]\""]}
{"_id":"Forever New","email":["\"[]\""],"email0":["\"[]\""]}
{"_id":"On The Go Tours","email":[""],"email0":["\"[\"aus-info@onthegotours.com\""]}
{"_id":"Walter's Steakhouse and Wine Bar","email":["\"[\"info@waltersbrisbane.com.au\"]\""],"email0":["\"[\"info@waltersbrisbane.com.au\"]\""]}
{"_id":"Down Under Bar & Grill","email":[""],"email0":[""]}
{"_id":"Tattersall's Club","email":["\"[\"admin@tattersallsclub.com\""],"email0":["\"cycling@tattersallsclub.com\""]}
{"_id":"Ryan's On The Park Bar and Restaurant","email":["\"[\"ain@star.com.au\"]\""],"email0":["\"[\"ain@star.com.au\"]\""]}
{"_id":"The Caxton Hotel","email":["\"[\"caxton@caxton.com.au\""],"email0":["\"//8b4e078a51d04e0e9efdf470027f0ec1@sentry.wixpress.com\""]}
{"_id":"The Pav Bar & Courtyard","email":["\"[\"reservations@spb.stamford.com.au\""],"email0":["\"reservations@spb.stamford.com.au\"]\""]}
'''

text ='''
['morningsidestalls@gmail.com', 'info@uplit.com.au', 'maryjane@website.com', 'stones.corner.hotel@alhgroup.com.au', 'alderley.arms.hotel@alhgroup.com.au', 'bookings@luxuryjapantravel.com', 'info@scienceoffitness.com.au', 'blutesbar@gmail.com', 'jesse@thehappyhorsemen.com', 'enquiries@ekka.com.au', 'fletcher@peabodytrading.com.au', 'info@taiwanfestival.com.au', 'info@zimmermannwear.com', 'littlebighouse@solotel.com.au', 'contact@bigforktheatre.com', 'bigforktheatre@gmail.com', 'info@lefestival.com.au', 'impallari@gmail.com', 'team@latofonts.com', 'example@yourdomain.com', 'me@mywixsite.com', 'tellmemore@standup.com.au', 'brisbane@dymocks.com.au', 'inquiries@snapfitness.com', 'customerservice@shavershop.com.au', 'info@thebeatmegaclub.com.au', 'enquiries@thepalacelounge.com.au', 'username@example.com', 'info@f1rstclassfitness.com.au', 'newmarket.hotel@alhgroup.com.au', 'admin@urbbana.com.au', 'musiccity@tnaru.net',, 'info@nestnappies.com.au', 'customer.services@tmlewin.co.uk', 'customercare@colette.com.au', 'tours@sunrover.com.au', 'customer@treeoflife.com.au', 'info@queenslandpoetryfestival.com', 'nickcave@thebadseeds.com', 'esktop@1x.png', 'customercare@sassandbide.com', 'theteam@olympiatransformations.com.au', 'allyinfo@allyfashion.com', 'bookings@southerncrosstours.com.au', 'functions@themet.com.au', 'sales@mwtours.com.au', 'info@soleilpoolbar.com.au', 'gec@lululemon.com.au', 'info@olliesplace.com.au', 'jimmys@jimmysonthemall.com.au', 'alison@botanicarealfood.com.au', 'info@buffalobar.com.au', 'ceo@tattersallsclub.com', 'hello@birdees.com', 'cs@bubblebubs.com.au', 'johndoe@domain.com', 'music@brisbanejazzclub.com.au', 'functions@candyclub.com.au', 'info@prohibitionbrisbane.com.au', 'sales@xwing.com.au', 'info@playersbris.com.au', 'victory.hotel@alhgroup.com.au', 'enquiries@aquitainebrasserie.com.au', 'brunswick.hotel@alhgroup.com.au', 'bookings@blackfirebrisbane.com.au', 'info@stokehouseq.com.au', 'info@bacchussouthbank.com.au', 'ard@bcc.qld.gov.au', 'gatherings@thegresham.com.au', 'hello@superwhatnot.com', 'twelfthnighttheatre@bigpond.com', 'admin@mrbunz.com.au', 'robert@broofa.com', 'kinnimm.queenplaza@gmail.com', 'myercentre@soulorigin.com.au', 'treasuryfunctions@star.com.au', 'hirnbeck@star.com.au', 'ing@star.com.au', 'info@embassyhotel.net.au', 'info@aaj.com.au', 'club29fun@gmail.com', 'pcanning@qutguild.com', 'brisbane@ymca.org.au', 'danielle@irishmurphys.com.au', 'aus-info@onthegotours.com', 'info@waltersbrisbane.com.au', 'admin@tattersallsclub.com', 'cycling@tattersallsclub.com', 'ain@star.com.au', 'caxton@caxton.com.au', 'reservations@spb.stamford.com.au']
'''

def extractEmailsFromUrlText(urlText):
    extractedEmail =  emailRegex.findall(urlText.replace('%20',''))
    extractedEmail =  emailRegex.findall(urlText.replace('\'',''))
    return extractedEmail
def removeDuplicates(chars):
    mail = []
    for char in range(len(chars)):
        if chars[char] not in mail:
                mail.append(chars[char])

    return mail
email = extractEmailsFromUrlText(text)
email = removeDuplicates(email)
print (email)



size=len(email)

print(size)