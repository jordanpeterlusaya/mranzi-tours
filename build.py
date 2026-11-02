#!/usr/bin/env python3
"""Generate the Mranzi Tours & Safaris site from the brochure experiences."""

from html import escape
from pathlib import Path
from urllib.parse import quote

ROOT = Path(__file__).resolve().parent
PHONE = "255777466868"
PHONE_DISPLAY = "+255 777 466 868"
EMAIL = "info@mranzitours.co.tz"
SITE = "https://mranzitours.co.tz"

GENERAL = (
    "Hello Mranzi Tours & Safaris, I would like to plan a private journey "
    "in Zanzibar and Tanzania."
)


def e(value):
    return escape(str(value), quote=True)


def wa(text):
    return f"https://wa.me/{PHONE}?text={quote(text)}"


def tour_wa(title):
    return wa(
        f"Hello Mranzi Tours & Safaris, I would like to enquire about {title}. "
        "Please let me know availability for my dates and group size."
    )


TOURS = [
    {
        "slug": "stone-town-spice",
        "title": "Stone Town + Spice Tour",
        "cat": "heritage",
        "cat_label": "Heritage & Culture",
        "image": "stonetown.webp",
        "alt": "Stone Town lanes and carved wooden architecture",
        "summary": "A walk through Stone Town’s architectural lanes, followed by an afternoon on a local spice farm.",
        "body": [
            "The morning moves through the winding streets of Stone Town, with time for the architectural character of the old city and the layers of history held in its houses and courtyards.",
            "In the afternoon the journey continues to a local spice farm, where the island’s plants and the way they are cultivated are part of the visit.",
        ],
        "highlights": [
            "Stone Town’s winding streets and architecture",
            "Afternoon visit to a local spice farm",
        ],
    },
    {
        "slug": "spice-tour",
        "title": "Spice Tour",
        "cat": "flavours",
        "cat_label": "Flavours & Lifestyle",
        "image": "spice-farm.webp",
        "alt": "Fresh tropical fruit opened by hand on a spice farm",
        "summary": "Aromatic spices, herbs, coconut and tropical fruit, seen where they are grown.",
        "body": [
            "Zanzibar’s spice farms hold an abundance of aromatic spices, herbs and tropical fruit. This visit is about the plants themselves: how they are cultivated, and how coconut sits alongside the cloves, cinnamon and other crops of the island.",
        ],
        "highlights": [
            "Aromatic spices, herbs and tropical fruits",
            "Cultivation of spice plants, including coconut",
        ],
    },
    {
        "slug": "prison-island",
        "title": "Prison Island Tour",
        "cat": "ocean",
        "cat_label": "Ocean & Islands",
        "image": "sandbank-prison-island.webp",
        "alt": "Shallow turquoise water near Prison Island",
        "summary": "The former prison and quarantine hospital, and the giant tortoises that now live on the island.",
        "body": [
            "Prison Island has served as a prison and later as a quarantine hospital. Today it is known for that history and for its tortoise sanctuary.",
            "The visit gives time to learn the story of the island, see the giant tortoises, and be on the water between Stone Town and the island.",
        ],
        "highlights": [
            "Historic prison, later a quarantine hospital",
            "Tortoise sanctuary and giant tortoises",
        ],
    },
    {
        "slug": "jozani-forest",
        "title": "Jozani Forest",
        "cat": "nature",
        "cat_label": "Wildlife & Nature",
        "image": "jozani-forest.webp",
        "alt": "Red colobus monkey in Jozani Forest",
        "summary": "Jozani’s forest paths and the rare Zanzibar red colobus.",
        "body": [
            "Jozani Forest is home to a variety of wildlife, including the Zanzibar red colobus, a rare and endangered monkey found only here.",
            "The visit is a walk in the forest, with time for the trees, the wildlife and the character of this protected corner of the island.",
        ],
        "highlights": [
            "Zanzibar red colobus",
            "Forest wildlife and endemic habitat",
        ],
    },
    {
        "slug": "stone-town-tour",
        "title": "Stone Town Tour",
        "cat": "heritage",
        "cat_label": "Heritage & Culture",
        "image": "forodhani.webp",
        "alt": "Seafront and historic buildings of Stone Town",
        "summary": "Historic landmarks of Stone Town, including the Anglican Cathedral.",
        "body": [
            "Stone Town carries the influence of many cultures. The walk visits important historic landmarks, including the Anglican Cathedral, and moves through the lanes that still shape daily life in the old city.",
        ],
        "highlights": [
            "Anglican Cathedral and historic landmarks",
            "The layered cultures of Stone Town",
        ],
    },
    {
        "slug": "stone-town-prison-island",
        "title": "Stone Town + Prison Island",
        "cat": "heritage",
        "cat_label": "Heritage & Culture",
        "image": "combo-zanzibar-shore.webp",
        "alt": "Zanzibar shoreline near the historic town",
        "summary": "Stone Town’s narrow streets and coloured houses, paired with Prison Island.",
        "body": [
            "Stone Town is one of the most fascinating cities in Africa: a maze of narrow streets and coloured houses, with a rich history and culture.",
            "This combination continues from the town to Prison Island, so the day holds both the old city and the island’s tortoises and history.",
        ],
        "highlights": [
            "Narrow streets and coloured houses of Stone Town",
            "Prison Island’s history and tortoises",
        ],
    },
    {
        "slug": "stone-town-jozani",
        "title": "Stone Town + Jozani Forest",
        "cat": "nature",
        "cat_label": "Wildlife & Nature",
        "image": "jozani.webp",
        "alt": "Forest canopy in Jozani",
        "summary": "A thorough Stone Town walk, then the forest in the afternoon.",
        "body": [
            "The day begins with a comprehensive walk through Stone Town: its viewpoints, landmarks and narrow streets.",
            "In the afternoon the journey moves on to Jozani Forest and the wildlife of the interior.",
        ],
        "highlights": [
            "Stone Town viewpoints and narrow streets",
            "Afternoon in Jozani Forest",
        ],
    },
    {
        "slug": "stone-town-sunset-cruise",
        "title": "Stone Town + Sunset Cruise",
        "cat": "ocean",
        "cat_label": "Ocean & Islands",
        "image": "sunset-dhow.jpg",
        "alt": "Traditional dhow on the water at sunset",
        "summary": "The west coast town, then a sunset cruise on the water.",
        "body": [
            "The day is rooted on the west coast of Zanzibar. Stone Town’s narrow streets hold a blend of cultures and architectural influence.",
            "The visit closes on the water with a sunset cruise, as the town gives way to the Indian Ocean.",
        ],
        "highlights": [
            "West-coast Stone Town",
            "Sunset cruise",
        ],
    },
    {
        "slug": "safari-blue",
        "title": "Safari Blue",
        "cat": "ocean",
        "cat_label": "Ocean & Islands",
        "image": "nakupenda-island.webp",
        "alt": "White sandbank in turquoise water",
        "summary": "Menai Bay by boat: reefs, dolphins and a seafood lunch.",
        "body": [
            "Safari Blue spends the day among the islands of the Menai Bay Conservation Area.",
            "There is time to snorkel on Zanzibar’s coral reefs, watch for dolphins, and sit down to a seafood lunch.",
        ],
        "highlights": [
            "Menai Bay Conservation Area",
            "Snorkelling, dolphins and a seafood lunch",
        ],
    },
    {
        "slug": "stone-town-lunch",
        "title": "Stone Town Tour with Lunch",
        "cat": "heritage",
        "cat_label": "Heritage & Culture",
        "image": "stonetown.webp",
        "alt": "Historic Stone Town",
        "summary": "The landmarks of Stone Town, with lunch included.",
        "body": [
            "This Stone Town walk includes the Anglican Cathedral, the slave markets, the Palace of the Sultans, Tippu Tip’s House, the Arabic Fort, Forodhani Park and the carved Zanzibar doors.",
            "Lunch is part of the day, so the visit has a slower, seated pause in the old city.",
        ],
        "highlights": [
            "Anglican Cathedral, slave markets and the Palace of the Sultans",
            "Arabic Fort, Forodhani Park and Zanzibar doors",
            "Lunch included",
        ],
    },
    {
        "slug": "the-rock",
        "title": "The Rock",
        "cat": "ocean",
        "cat_label": "Ocean & Islands",
        "image": "the-rock.webp",
        "alt": "The Rock restaurant standing in the sea",
        "summary": "The Rock, the coral around it, and a long look at the coast.",
        "body": [
            "A visit to The Rock is a pause on the east coast: the restaurant on its tidal rock, the coral formations around it, and wide views of the sea.",
            "It is arranged as time for the place itself, rather than a hurried stop between other sights.",
        ],
        "highlights": [
            "Visit to The Rock",
            "Coral formations and coastal views",
        ],
    },
    {
        "slug": "butterfly-jozani",
        "title": "Butterfly Centre + Jozani Forest",
        "cat": "nature",
        "cat_label": "Wildlife & Nature",
        "image": "jozani-forest.webp",
        "alt": "Colobus monkey among the trees of Jozani",
        "summary": "A full day between the Butterfly Centre and Jozani Forest.",
        "body": [
            "This full-day excursion pairs the Zanzibar Butterfly Centre, a garden housing a diverse array of butterflies, with Jozani Forest, a national park of plant and animal life.",
        ],
        "highlights": [
            "Full day",
            "Zanzibar Butterfly Centre",
            "Jozani Forest",
        ],
    },
    {
        "slug": "butterfly-jozani-spice",
        "title": "Butterfly Centre, Jozani Forest + Spice Tour",
        "cat": "flavours",
        "cat_label": "Flavours & Lifestyle",
        "image": "spice-farm.webp",
        "alt": "Hands holding freshly opened tropical fruit",
        "summary": "Butterflies, the forest, and a spice farm in one day.",
        "body": [
            "The day brings together the Butterfly Centre, Jozani Forest and a spice tour.",
            "Jozani is an expansive national park of about 44 square kilometres, with rare butterflies and forest wildlife alongside the spice plants of the island.",
        ],
        "highlights": [
            "Butterfly Centre",
            "Jozani Forest",
            "Spice tour",
        ],
    },
    {
        "slug": "butterfly-jozani-rock",
        "title": "Butterfly Centre, Jozani Forest + The Rock",
        "cat": "nature",
        "cat_label": "Wildlife & Nature",
        "image": "the-rock-restaurant.webp",
        "alt": "The Rock restaurant at the edge of the tide",
        "summary": "Forest and butterflies inland, then The Rock on the coast.",
        "body": [
            "The inland half of the day is the Butterfly Centre and Jozani Forest, home to rare butterflies and a wide stretch of protected forest.",
            "The day then reaches the coast at The Rock.",
        ],
        "highlights": [
            "Butterfly Centre and Jozani Forest",
            "The Rock",
        ],
    },
    {
        "slug": "butterfly-jozani-stone-town",
        "title": "Butterfly Centre, Jozani Forest + Stone Town",
        "cat": "heritage",
        "cat_label": "Heritage & Culture",
        "image": "stonetown.webp",
        "alt": "A lane in historic Stone Town",
        "summary": "Butterflies, Jozani, and a Stone Town walking tour.",
        "body": [
            "The day includes the Zanzibar Butterfly Centre, Jozani Forest and a Stone Town walking tour.",
            "Each part offers something distinct: the garden, the forest, and the historic town.",
        ],
        "highlights": [
            "Zanzibar Butterfly Centre",
            "Jozani Forest",
            "Stone Town walking tour",
        ],
    },
    {
        "slug": "safari-blue-private-dhow",
        "title": "Safari Blue Private Dhow",
        "cat": "ocean",
        "cat_label": "Ocean & Islands",
        "image": "combo-zanzibar-dhow.webp",
        "alt": "Traditional dhow in the shallows of Menai Bay",
        "summary": "A full day on a private dhow in Menai Bay: sailing, snorkelling, dolphins and lunch.",
        "body": [
            "Safari Blue is a full-day excursion in the Menai Bay Conservation Area, a marine sanctuary off the coast of Zanzibar.",
            "On a private dhow the day combines sailing, snorkelling, dolphin watching and a seafood lunch.",
        ],
        "highlights": [
            "Full day on a private dhow",
            "Sailing, snorkelling and dolphin watching",
            "Seafood lunch",
        ],
    },
    {
        "slug": "jozani-village",
        "title": "Jozani Forest + Village Tour",
        "cat": "nature",
        "cat_label": "Wildlife & Nature",
        "image": "village-tour.jpg",
        "alt": "A village street and local produce in Zanzibar",
        "summary": "Forest wildlife and a village visit on the same day.",
        "body": [
            "The day joins Jozani Forest with a village visit, pairing the protected forest with everyday cultural life nearby.",
        ],
        "highlights": [
            "Jozani Forest",
            "Village visit",
        ],
    },
    {
        "slug": "seaweed-centre",
        "title": "Seaweed Centre Tour",
        "cat": "flavours",
        "cat_label": "Flavours & Lifestyle",
        "image": "combo-zanzibar-shore.webp",
        "alt": "Shallow coastal water along a Zanzibar shore",
        "summary": "A visit with women seaweed farmers and the community work around the farms.",
        "body": [
            "The Seaweed Centre works with women seaweed farmers to improve daily life and to support activities that benefit the wider community.",
            "On the tour you visit the farms and learn how seaweed is grown and used along this coast.",
        ],
        "highlights": [
            "Women seaweed farmers",
            "Community livelihood along the coast",
        ],
    },
    {
        "slug": "kizimkazi-village",
        "title": "Guided Walking Tour of Kizimkazi Village",
        "cat": "heritage",
        "cat_label": "Heritage & Culture",
        "image": "dolphins-zanzibar.webp",
        "alt": "Dolphins in clear water off Zanzibar",
        "summary": "Kizimkazi’s 12th-century mosque and a village known for dolphin watching.",
        "body": [
            "The walk through Kizimkazi includes the 12th-century Kizimkazi Mosque, one of the oldest on the island.",
            "The village is also a well-known point for dolphin watching on the south coast.",
        ],
        "highlights": [
            "12th-century Kizimkazi Mosque",
            "A village known for dolphin watching",
        ],
    },
    {
        "slug": "stone-town-voodoo-evening",
        "title": "Stone Town Voodoo Evening Tour",
        "cat": "heritage",
        "cat_label": "Heritage & Culture",
        "image": "forodhani.webp",
        "alt": "Stone Town in the warm light of late day",
        "summary": "An evening walk through Stone Town’s spiritual heritage.",
        "body": [
            "The Stone Town Voodoo Evening Tour is an after-dark walk through sites connected with the town’s spiritual and haunted heritage.",
        ],
        "highlights": [
            "Evening departure",
            "Sites linked to Stone Town’s spiritual heritage",
        ],
    },
    {
        "slug": "chumbe-island",
        "title": "Chumbe Island Tour",
        "cat": "ocean",
        "cat_label": "Ocean & Islands",
        "image": "combo-zanzibar-island.webp",
        "alt": "A small green island in clear Indian Ocean water",
        "summary": "A private nature reserve of coral reef, forest and wildlife.",
        "body": [
            "Chumbe Island is a privately owned nature reserve off the coast of Zanzibar, with a coral reef, a forest reserve and a variety of wildlife.",
            "The visit is time on the island’s reef and forest, at the pace the reserve allows.",
        ],
        "highlights": [
            "Private nature reserve",
            "Coral reef, forest and wildlife",
        ],
    },
    {
        "slug": "spice-cooking",
        "title": "Spice Tour + Swahili Cooking Lesson",
        "cat": "flavours",
        "cat_label": "Flavours & Lifestyle",
        "image": "village-tour.jpg",
        "alt": "Local produce at a Zanzibar market",
        "summary": "From the spice farm to the market, then into a Swahili kitchen.",
        "body": [
            "The visit begins on a spice farm, with the ingredients used in Swahili cooking.",
            "It continues at a local market and into a cooking lesson, so the spices are tasted in a meal rather than only seen in the field.",
        ],
        "highlights": [
            "Spice farm",
            "Local market",
            "Swahili cooking lesson",
        ],
    },
    {
        "slug": "jambiani-cultural",
        "title": "Jambiani Village Cultural Tour",
        "cat": "heritage",
        "cat_label": "Heritage & Culture",
        "image": "combo-zanzibar-palms.webp",
        "alt": "Palm-lined beach on the Zanzibar coast",
        "summary": "Everyday Swahili life in Jambiani village.",
        "body": [
            "Jambiani is known for its cultural heritage along the east coast. The visit is a chance to experience the Swahili way of life in the village, with the people who live there.",
        ],
        "highlights": [
            "Jambiani village",
            "Swahili coastal life",
        ],
    },
    {
        "slug": "tumbatu-cultural",
        "title": "Tumbatu Cultural Tour",
        "cat": "heritage",
        "cat_label": "Heritage & Culture",
        "image": "blue-lagoon.webp",
        "alt": "Calm coastal water and a traditional boat",
        "summary": "The distinct culture of Tumbatu. A written permit is required.",
        "body": [
            "Tumbatu has a distinct and comparatively isolated community. This cultural visit is about that place and the people who live there.",
            "A written permit is required, including for visitors from elsewhere in Zanzibar. Ask us to arrange it with the booking.",
        ],
        "highlights": [
            "Tumbatu’s cultural life",
            "Written permit required",
        ],
    },
    {
        "slug": "prison-island-sandbank-bbq",
        "title": "Prison Island + Sandbank with BBQ",
        "cat": "ocean",
        "cat_label": "Ocean & Islands",
        "image": "nakupenda-island.webp",
        "alt": "A sandbank picnic setting in shallow turquoise water",
        "summary": "Prison Island’s 1893 history, then a sandbank barbecue.",
        "body": [
            "Prison Island’s prison dates to 1893 and later served as a quarantine hospital. The visit includes the remains of that history and the tortoises.",
            "The day also stops on a sandbank for a barbecue.",
        ],
        "highlights": [
            "Prison dating from 1893, later a quarantine hospital",
            "Sandbank barbecue",
        ],
    },
    {
        "slug": "mnemba",
        "title": "Mnemba Tour",
        "cat": "ocean",
        "cat_label": "Ocean & Islands",
        "image": "mnemba-island.webp",
        "alt": "Mnemba Island ringed by turquoise reef",
        "summary": "The reef at Mnemba, with turtles, fish and a sandbank stop.",
        "body": [
            "Mnemba’s reef holds tropical fish, sea turtles and clear water over coral.",
            "The day includes a snack on a sandbank and time to take in the atoll.",
        ],
        "highlights": [
            "Mnemba reef, tropical fish and sea turtles",
            "Sandbank stop",
        ],
    },
    {
        "slug": "mnemba-aquarium-kendwa",
        "title": "Mnemba, Aquarium + Kendwa Beach",
        "cat": "ocean",
        "cat_label": "Ocean & Islands",
        "image": "nungwi-kendwa.webp",
        "alt": "Palm beach at Kendwa on Zanzibar’s north coast",
        "summary": "A full day: Mnemba Atoll, the Nungwi aquarium and Kendwa Beach.",
        "body": [
            "This full-day tour is built around the waters of Mnemba Island Atoll.",
            "It includes a visit to the aquarium in Nungwi and time on Kendwa Beach.",
        ],
        "highlights": [
            "Full day",
            "Mnemba Island Atoll",
            "Nungwi aquarium and Kendwa Beach",
        ],
    },
    {
        "slug": "stone-town-spice-prison",
        "title": "Stone Town, Spice Tour + Prison Island",
        "cat": "heritage",
        "cat_label": "Heritage & Culture",
        "image": "combo-zanzibar-palms.webp",
        "alt": "Coastal palms on Zanzibar",
        "summary": "Historic Stone Town, a spice farm and Prison Island in one arrangement.",
        "body": [
            "This combination brings together the historic city of Stone Town, a spice tour and Prison Island.",
            "It suits guests who want the town, the farms and the water in a single private plan.",
        ],
        "highlights": [
            "Historic Stone Town",
            "Spice tour",
            "Prison Island",
        ],
    },
]

DIMS = {
    "stonetown.webp": (1280, 720),
    "spice-farm.webp": (1280, 960),
    "sandbank-prison-island.webp": (1280, 853),
    "jozani-forest.webp": (1280, 960),
    "forodhani.webp": (1280, 960),
    "combo-zanzibar-shore.webp": (1280, 853),
    "jozani.webp": (1200, 1200),
    "sunset-dhow.jpg": (830, 564),
    "nakupenda-island.webp": (1280, 960),
    "stone-town.webp": (1280, 449),
    "the-rock.webp": (1280, 795),
    "the-rock-restaurant.webp": (1280, 720),
    "private-yacht.webp": (1280, 853),
    "village-tour.jpg": (830, 553),
    "dolphins-zanzibar.webp": (1024, 683),
    "combo-zanzibar-island.webp": (1280, 853),
    "combo-zanzibar-palms.webp": (1280, 853),
    "blue-lagoon.webp": (1280, 853),
    "mnemba-island.webp": (1280, 960),
    "nungwi-kendwa.webp": (1280, 960),
    "combo-zanzibar-aerial.webp": (1280, 853),
    "combo-zanzibar-dhow.webp": (1280, 853),
    "safari-giraffes-kilimanjaro.webp": (1024, 770),
    "tz-lion.webp": (1280, 853),
    "tz-tarangire-elephants.webp": (1280, 853),
    "safari-acacia-sunset.webp": (1024, 681),
    "luxury-villa.webp": (1280, 853),
    "zanzibar-overwater-resort.webp": (1024, 1024),
    "hero-zanzibar-luxury.webp": (1280, 720),
    "charity-community.webp": (1200, 900),
    "yacht-charter.webp": (1280, 960),
    "mnemba.webp": (1280, 961),
}


def dims(name):
    w, h = DIMS.get(name, (1280, 853))
    return f'width="{w}" height="{h}"'


NAV = [
    ("experiences", "Experiences", "experiences/index.html"),
    ("destinations", "Destinations", "destinations.html"),
    ("about", "About", "about.html"),
    ("contact", "Contact", "contact.html"),
]


def header(prefix, current):
    links = []
    for key, label, href in NAV:
        current_attr = ' aria-current="page"' if key == current else ""
        links.append(f'<a href="{prefix}{href}"{current_attr}>{label}</a>')
    book = e(wa(GENERAL))
    return f"""
  <a class="skip" href="#main">Skip to content</a>
  <header class="site-header" data-header>
    <div class="wrap header-bar">
      <a class="brand" href="{prefix}index.html">
        <span class="brand-name">Mranzi</span>
        <span class="brand-sub">Tours &amp; Safaris</span>
      </a>
      <button class="nav-toggle" type="button" data-nav-toggle aria-expanded="false" aria-controls="nav" aria-label="Open menu"><span></span><span></span><span></span></button>
      <nav class="nav" id="nav" data-nav>
        {''.join(links)}
        <a class="btn btn-book" href="{book}">Book your journey</a>
      </nav>
    </div>
  </header>"""


def footer(prefix):
    return f"""
  <footer class="site-footer">
    <div class="wrap foot-grid">
      <div class="foot-brand">
        <h2>Mranzi</h2>
        <p>Private experiences across Zanzibar and Tanzania, arranged at your pace.</p>
      </div>
      <div>
        <h3>Experiences</h3>
        <ul>
          <li><a href="{prefix}experiences/index.html?cat=heritage">Heritage &amp; culture</a></li>
          <li><a href="{prefix}experiences/index.html?cat=nature">Wildlife &amp; nature</a></li>
          <li><a href="{prefix}experiences/index.html?cat=ocean">Ocean &amp; islands</a></li>
          <li><a href="{prefix}experiences/index.html?cat=flavours">Flavours &amp; lifestyle</a></li>
        </ul>
      </div>
      <div>
        <h3>Visit</h3>
        <ul>
          <li><a href="{prefix}destinations.html">Zanzibar &amp; Tanzania</a></li>
          <li><a href="{prefix}about.html">About</a></li>
          <li><a href="{prefix}contact.html">Contact</a></li>
          <li><a href="{prefix}contact.html#enquire">Plan a journey</a></li>
        </ul>
      </div>
      <div>
        <h3>Contact</h3>
        <ul>
          <li><a href="{e(wa(GENERAL))}">WhatsApp {PHONE_DISPLAY}</a></li>
          <li><a href="tel:{PHONE}">Call {PHONE_DISPLAY}</a></li>
          <li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
          <li>Zanzibar, Tanzania</li>
        </ul>
      </div>
    </div>
    <div class="wrap">
      <p class="copy">© <span id="year">2026</span> Mranzi Tours &amp; Safaris. Zanzibar, Tanzania.</p>
    </div>
  </footer>
  <a class="wa-float" href="{e(wa(GENERAL))}">WhatsApp</a>
  <script src="{prefix}js/site.js"></script>"""


def document(title, description, path, image, depth, current, main, schema=""):
    prefix = "../" * depth
    canonical = SITE + path
    og = f"{SITE}/assets/{image}"
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{e(title)}</title>
  <meta name="description" content="{e(description)}">
  <link rel="canonical" href="{canonical}">
  <meta name="theme-color" content="#F7F4ED">
  <meta property="og:type" content="website">
  <meta property="og:site_name" content="Mranzi Tours &amp; Safaris">
  <meta property="og:title" content="{e(title)}">
  <meta property="og:description" content="{e(description)}">
  <meta property="og:url" content="{canonical}">
  <meta property="og:image" content="{og}">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{e(title)}">
  <meta name="twitter:description" content="{e(description)}">
  <meta name="twitter:image" content="{og}">
  <link rel="icon" href="{prefix}favicon.svg" type="image/svg+xml">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,500;0,600;1,500&family=Manrope:wght@400;500;600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="{prefix}css/styles.css">
  {schema}
</head>
<body>
{header(prefix, current)}
{main}
{footer(prefix)}
</body>
</html>
"""


def img(name, alt, prefix, lazy=True):
    loading = 'loading="lazy"' if lazy else 'loading="eager"'
    return f'<img src="{prefix}assets/{name}" alt="{e(alt)}" {dims(name)} {loading} decoding="async">'


def home():
    book = e(wa(GENERAL))
    schema = """<script type="application/ld+json">
  {"@context":"https://schema.org","@type":"TravelAgency","name":"Mranzi Tours & Safaris","url":"https://mranzitours.co.tz/","email":"info@mranzitours.co.tz","telephone":"+255777466868","address":{"@type":"PostalAddress","addressLocality":"Zanzibar","addressCountry":"TZ"},"areaServed":["Zanzibar","Tanzania"]}
  </script>"""
    experiences = [
        ("sig-a", "combo-zanzibar-aerial.webp", "Aerial view of Zanzibar’s turquoise coast", "Zanzibar Island Experiences", "Stone Town, spice farms, Prison Island and Jozani, taken singly or composed together.", "experiences/index.html"),
        ("sig-b", "combo-zanzibar-dhow.webp", "Traditional dhow in shallow turquoise water", "Private Boat Excursions", "Dhow sailing, Safari Blue, Mnemba and sandbank days on the Indian Ocean.", "experiences/index.html?cat=ocean"),
        ("sig-c", "safari-giraffes-kilimanjaro.webp", "Giraffes on a Tanzanian plain with Kilimanjaro beyond", "Safari Adventures", "Mainland wildlife, arranged privately around your dates.", "destinations.html#safari"),
        ("sig-d", "nakupenda-island.webp", "White sandbank in clear shallow water", "Beach & Coastal Escapes", "Kendwa, Nungwi, The Rock and quiet sandbanks.", "experiences/the-rock.html"),
        ("sig-e", "stonetown.webp", "Historic Stone Town", "Cultural Experiences", "Villages, Swahili cooking, seaweed farming and the living heritage of the coast.", "experiences/index.html?cat=heritage"),
        ("sig-f", "luxury-villa.webp", "A quiet luxury villa beside tropical planting", "Coastal Stays", "Villas and quiet coastal stays, matched to the journey and confirmed with us directly.", "destinations.html#stays"),
    ]
    cards = []
    for cls, image, alt, title, text, href in experiences:
        cards.append(f"""
        <a class="sig {cls}" href="{href}">
          {img(image, alt, "", lazy=cls != "sig-a")}
          <span class="sig-shade"></span>
          <span class="sig-copy">
            <h3>{title}</h3>
            <p>{text}</p>
            <span class="text-link">Discover experience</span>
          </span>
        </a>""")
    main = f"""
  <main id="main">
    <section class="hero" aria-label="Introduction">
      <video class="hero-media" autoplay muted loop playsinline poster="assets/hero-poster.webp">
        <source src="assets/video/hero.mp4" type="video/mp4">
      </video>
      <div class="hero-shade"></div>
      <div class="wrap hero-content">
        <p class="eyebrow">Tanzania &amp; Zanzibar · Private experiences</p>
        <h1>Discover Africa.<br>Experience the Extraordinary.</h1>
        <p class="lede">Exceptional journeys, thoughtfully curated across the breathtaking landscapes and timeless beauty of Zanzibar and Tanzania.</p>
        <div class="hero-actions">
          <a class="btn btn-ivory" href="experiences/index.html">Explore our experiences</a>
          <a class="btn" href="{book}">Plan your journey</a>
        </div>
      </div>
    </section>

    <section class="section intro">
      <div class="wrap intro-grid reveal">
        <h2>More Than a Journey. A World of Experiences.</h2>
        <div>
          <p class="lede">From the winding heritage lanes of Stone Town to fragrant spice farms and turquoise marine escapes, Zanzibar invites you to slow down, explore and connect.</p>
          <p class="lede" style="margin-top:1rem">Mranzi Tours &amp; Safaris arranges private experiences around that invitation. One excursion, or several composed into a journey. You tell us what draws you, your dates and the size of your group. We shape the day around it.</p>
        </div>
      </div>
    </section>

    <section class="section" style="padding-top:0">
      <div class="wrap">
        <div class="section-head reveal">
          <p class="eyebrow">Signature experiences</p>
          <h2>The island, met properly.</h2>
        </div>
        <div class="sig-grid reveal">
          {''.join(cards)}
        </div>
      </div>
    </section>

    <section class="section" id="destination">
      <div class="wrap">
        <div class="section-head reveal">
          <p class="eyebrow">The destination</p>
          <h2>Zanzibar and the country beyond it.</h2>
        </div>
        <div class="dest-layout reveal">
          <figure class="dest-main">
            <div class="frame">{img("mnemba-island.webp", "Mnemba Island surrounded by reef", "")}</div>
            <figcaption>
              <h3>Turquoise water</h3>
              <p>Reefs, sandbanks and the long colour of the Indian Ocean, from Mnemba to Menai Bay.</p>
            </figcaption>
          </figure>
          <div class="dest-stack">
            <figure>
              <div class="frame">{img("nakupenda-island.webp", "White sandbank in shallow water", "")}</div>
              <figcaption>
                <h3>White sand</h3>
                <p>Sandbanks and quiet beaches, reached by boat and left to the tide.</p>
              </figcaption>
            </figure>
            <figure>
              <div class="frame">{img("combo-zanzibar-dhow.webp", "Traditional dhow under sail", "")}</div>
              <figcaption>
                <h3>Dhows</h3>
                <p>Traditional boats on Menai Bay and along the west coast, including sunset hours.</p>
              </figcaption>
            </figure>
          </div>
        </div>
        <div class="dest-row reveal">
          <figure>
            <div class="frame">{img("stonetown.webp", "Stone Town’s historic streets", "")}</div>
            <figcaption>
              <h3>Stone Town</h3>
              <p>A UNESCO World Heritage city of carved doors, courtyards and narrow lanes.</p>
            </figcaption>
          </figure>
          <figure>
            <div class="frame">{img("tz-lion.webp", "Lion in golden grass", "")}</div>
            <figcaption>
              <h3>Wildlife</h3>
              <p>Jozani’s red colobus on the island, and the great animals of the mainland when a safari is part of the plan.</p>
            </figcaption>
          </figure>
          <figure>
            <div class="frame">{img("safari-acacia-sunset.webp", "Acacia trees at sunset on the savanna", "")}</div>
            <figcaption>
              <h3>Safari country</h3>
              <p>Open landscapes beyond the island, discussed privately and arranged to your dates.</p>
            </figcaption>
          </figure>
        </div>
      </div>
    </section>

    <section class="section sand bespoke">
      <div class="wrap bespoke-grid reveal">
        <h2>Your Journey. Your Pace. Your Africa.</h2>
        <div>
          <p class="lede">Every journey can be tailored to what you want to see, how you like to spend the hours, and the size of your party. A single private excursion. A combination of heritage, forest and ocean. Or a longer plan that includes the mainland.</p>
          <p class="lede" style="margin-top:1rem">Tell us the dates, where you are staying, and what the days should feel like. We confirm the arrangement with you directly.</p>
          <a class="btn btn-solid" style="margin-top:1.6rem" href="{book}">Create your private journey</a>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="wrap">
        <div class="section-head reveal">
          <p class="eyebrow">Discover the difference</p>
          <h2>Hospitality, kept personal.</h2>
        </div>
        <div class="diff-list reveal">
          <article class="diff-item"><span>01</span><h3>Private guides</h3><p>Days led for your group, with room to linger where the place asks for it.</p></article>
          <article class="diff-item"><span>02</span><h3>Curated experiences</h3><p>A considered collection of island excursions, from Stone Town to the reefs, rather than a crowded menu.</p></article>
          <article class="diff-item"><span>03</span><h3>Personal hospitality</h3><p>Dates, pickup and group size discussed with you before the day begins.</p></article>
          <article class="diff-item"><span>04</span><h3>Local connections</h3><p>Spice farms, villages, seaweed farmers and the communities who keep these places alive.</p></article>
          <article class="diff-item"><span>05</span><h3>Seamless planning</h3><p>One conversation on WhatsApp covers the excursion, the combination, or the wider journey.</p></article>
        </div>
      </div>
    </section>

    <section class="section sand purpose">
      <div class="wrap purpose-grid reveal">
        <div class="purpose-media">{img("charity-community.webp", "Children studying in a community classroom", "")}</div>
        <div>
          <p class="eyebrow">Giving back</p>
          <h2>Travel With Purpose.</h2>
          <p class="stat">40%</p>
          <p class="lede">Forty percent of tour revenue is contributed to charitable initiatives in the local Zanzibar community. The journeys are for our guests. A meaningful share of them stays with the island that makes them possible.</p>
        </div>
      </div>
    </section>

    <section class="finale">
      {img("hero-zanzibar-luxury.webp", "Turquoise Zanzibar coast", "", lazy=False)}
      <div class="shade"></div>
      <div class="wrap finale-copy">
        <p class="eyebrow">Begin</p>
        <h2>Your African Story Begins Here.</h2>
        <p class="lede">Let us create an extraordinary journey worth remembering.</p>
        <div class="finale-actions">
          <a class="btn btn-ivory" href="{book}">Plan your journey</a>
        </div>
      </div>
    </section>
  </main>"""
    return document(
        "Mranzi Tours & Safaris | Private Zanzibar & Tanzania",
        "Private Zanzibar experiences and tailored Tanzania journeys with Mranzi Tours & Safaris. Enquire on WhatsApp.",
        "/",
        "hero-zanzibar-luxury.webp",
        0,
        "home",
        main,
        schema,
    )


def catalog():
    rows = []
    for index, tour in enumerate(TOURS):
        flip = " is-flip" if index % 2 else ""
        rows.append(f"""
        <article class="exp-row{flip}" data-cat="{tour['cat']}">
          <a class="frame" href="{tour['slug']}.html">{img(tour['image'], tour['alt'], "../")}</a>
          <div>
            <p class="eyebrow">{e(tour['cat_label'])}</p>
            <h2><a href="{tour['slug']}.html">{e(tour['title'])}</a></h2>
            <p>{e(tour['summary'])}</p>
            <a class="text-link" href="{tour['slug']}.html">Discover experience</a>
          </div>
        </article>""")
    main = f"""
  <main id="main">
    <header class="page-hero">
      {img("combo-zanzibar-dhow.webp", "Dhow on the Indian Ocean", "../", lazy=False)}
      <div class="shade"></div>
      <div class="wrap">
        <p class="eyebrow">Zanzibar</p>
        <h1>Experiences</h1>
        <p class="lede">Curated excursions and memorable island moments. Choose one, or ask us to combine several.</p>
      </div>
    </header>
    <section class="section">
      <div class="wrap">
        <div class="filters" data-filters>
          <button type="button" data-filter="all" aria-pressed="true">All</button>
          <button type="button" data-filter="heritage">Heritage &amp; culture</button>
          <button type="button" data-filter="nature">Wildlife &amp; nature</button>
          <button type="button" data-filter="ocean">Ocean &amp; islands</button>
          <button type="button" data-filter="flavours">Flavours &amp; lifestyle</button>
        </div>
        <p class="empty-note" data-empty>Nothing in this collection yet.</p>
        {''.join(rows)}
      </div>
    </section>
  </main>"""
    return document(
        "Zanzibar Experiences | Mranzi Tours & Safaris",
        "Stone Town, spice farms, Jozani, Safari Blue, Mnemba, Prison Island and private dhow days with Mranzi Tours & Safaris.",
        "/experiences/",
        "combo-zanzibar-dhow.webp",
        1,
        "experiences",
        main,
    )


def detail(tour, index):
    paragraphs = "".join(f"<p>{e(p)}</p>" for p in tour["body"])
    highlights = "".join(f"<li>{e(item)}</li>" for item in tour["highlights"])
    related = [TOURS[i % len(TOURS)] for i in range(index + 1, index + 4)]
    related_html = []
    for item in related:
        related_html.append(f"""
          <a href="{item['slug']}.html">
            <div class="frame">{img(item['image'], item['alt'], "../")}</div>
            <h3>{e(item['title'])}</h3>
          </a>""")
    link = e(tour_wa(tour["title"]))
    main = f"""
  <main id="main">
    <header class="page-hero">
      {img(tour['image'], tour['alt'], "../", lazy=False)}
      <div class="shade"></div>
      <div class="wrap">
        <p class="crumbs"><a href="index.html">Experiences</a> · {e(tour['cat_label'])}</p>
        <h1>{e(tour['title'])}</h1>
      </div>
    </header>
    <section class="section" style="padding-top:0">
      <div class="wrap exp-layout">
        <div class="exp-copy">
          <p class="lede">{e(tour['summary'])}</p>
          {paragraphs}
        </div>
        <aside class="exp-aside">
          <p class="eyebrow">Enquire</p>
          <p>Tell us your dates, pickup point and group size. We confirm the arrangement on WhatsApp. Rates are not listed here; they are agreed for your party.</p>
          <a class="btn btn-solid" href="{link}">Enquire on WhatsApp</a>
          <ul class="aside-contact">
            <li><a href="tel:{PHONE}">{PHONE_DISPLAY}</a></li>
            <li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
          </ul>
          <ul class="highlights">{highlights}</ul>
        </aside>
      </div>
    </section>
    <section class="section related" style="padding-top:0">
      <div class="wrap">
        <p class="eyebrow">Continue</p>
        <h2 style="font-size:clamp(2.4rem,4vw,3.6rem);margin-bottom:1.5rem">Further experiences</h2>
        <div class="related-grid">{''.join(related_html)}</div>
      </div>
    </section>
  </main>"""
    return document(
        f"{tour['title']} | Mranzi Tours & Safaris",
        tour["summary"],
        f"/experiences/{tour['slug']}.html",
        tour["image"],
        1,
        "experiences",
        main,
    )


def destinations():
    book = e(wa("Hello Mranzi Tours & Safaris, I would like to discuss a private safari in Tanzania alongside time in Zanzibar."))
    stay = e(wa("Hello Mranzi Tours & Safaris, I would like to discuss a coastal stay as part of my journey."))
    main = f"""
  <main id="main">
    <header class="page-hero">
      {img("combo-zanzibar-aerial.webp", "Aerial view of the Zanzibar coast", "", lazy=False)}
      <div class="shade"></div>
      <div class="wrap">
        <p class="eyebrow">Zanzibar · Tanzania</p>
        <h1>The destination</h1>
        <p class="lede">Turquoise water, Stone Town, dhows and, when you want it, the wildlife country of the mainland.</p>
      </div>
    </header>
    <section class="section">
      <div class="wrap dest-layout">
        <figure class="dest-main">
          <div class="frame">{img("combo-zanzibar-shore.webp", "White sand and clear shallows", "")}</div>
          <figcaption><h3>The coast</h3><p>North-coast beaches such as Kendwa and Nungwi, east-coast tides around The Rock, and sandbanks reached by boat.</p></figcaption>
        </figure>
        <div class="dest-stack">
          <figure>
            <div class="frame">{img("stonetown.webp", "Stone Town architecture", "")}</div>
            <figcaption><h3>Stone Town</h3><p>UNESCO lanes, carved doors, the Anglican Cathedral, the Old Fort and the seafront at Forodhani.</p></figcaption>
          </figure>
          <figure>
            <div class="frame">{img("jozani-forest.webp", "Red colobus in Jozani Forest", "")}</div>
            <figcaption><h3>Jozani</h3><p>The island’s forest reserve and the Zanzibar red colobus.</p></figcaption>
          </figure>
        </div>
      </div>
    </section>
    <section class="section sand" id="safari">
      <div class="wrap bespoke-grid">
        <div>
          <p class="eyebrow">Safari</p>
          <h2>The mainland, when the journey asks for it.</h2>
        </div>
        <div>
          <p class="lede">Mranzi is based in the island experiences of this collection. A private safari on the Tanzanian mainland can be discussed as part of a wider journey: your dates, your pace, and the wildlife you hope to meet.</p>
          <p class="lede" style="margin-top:1rem">We do not publish set safari prices here. The plan is agreed with you on WhatsApp.</p>
          <a class="btn btn-solid" style="margin-top:1.5rem" href="{book}">Discuss a private safari</a>
        </div>
      </div>
      <div class="wrap dest-row" style="margin-top:2.5rem">
        <figure><div class="frame">{img("tz-tarangire-elephants.webp", "Elephants in Tarangire country", "")}</div></figure>
        <figure><div class="frame">{img("tz-lion.webp", "Lion in the grass", "")}</div></figure>
        <figure><div class="frame">{img("safari-giraffes-kilimanjaro.webp", "Giraffes with Kilimanjaro in the distance", "")}</div></figure>
      </div>
    </section>
    <section class="section" id="stays">
      <div class="wrap purpose-grid">
        <div class="purpose-media">{img("zanzibar-overwater-resort.webp", "A coastal stay above clear water", "")}</div>
        <div>
          <p class="eyebrow">Stays</p>
          <h2>Where the days begin and end.</h2>
          <p class="lede">Coastal villas and quiet beach stays can be discussed with the excursions, so the base suits the pace of the journey. We confirm what is available for your dates rather than listing rooms or rates on this site.</p>
          <a class="btn" style="margin-top:1.5rem" href="{stay}">Ask about a stay</a>
        </div>
      </div>
    </section>
  </main>"""
    return document(
        "Zanzibar & Tanzania | Mranzi Tours & Safaris",
        "Stone Town, the Indian Ocean, Jozani Forest and privately arranged Tanzania safaris with Mranzi Tours & Safaris.",
        "/destinations.html",
        "combo-zanzibar-aerial.webp",
        0,
        "destinations",
        main,
    )


def about():
    main = f"""
  <main id="main">
    <header class="page-hero">
      {img("luxury-villa.webp", "Quiet tropical stay in Zanzibar", "", lazy=False)}
      <div class="shade"></div>
      <div class="wrap">
        <p class="eyebrow">Mranzi Tours &amp; Safaris</p>
        <h1>The island is calling.</h1>
        <p class="lede">Culture, nature and ocean. Beautiful days, and the kind of memories that stay.</p>
      </div>
    </header>
    <section class="section">
      <div class="wrap intro-grid">
        <h2>A collection, not a crowd.</h2>
        <div>
          <p class="lede">From Stone Town to the spice farms and the marine parks, this collection brings together remarkable excursions and flexible combinations for different ways of travelling.</p>
          <p class="lede" style="margin-top:1rem">We are Mranzi Tours &amp; Safaris, in Zanzibar. The experiences on this site are the ones in our collection. If you want a single day or a sequence of them, we plan it with you.</p>
        </div>
      </div>
      <div class="wrap guide">
        <article>
          <p class="eyebrow">01</p>
          <h3>Private experiences</h3>
          <p>A more personal pace, and arrangements that can flex around your group.</p>
        </article>
        <article>
          <p class="eyebrow">02</p>
          <h3>Combined excursions</h3>
          <p>Heritage, nature and ocean highlights brought into one journey.</p>
        </article>
        <article>
          <p class="eyebrow">03</p>
          <h3>Travel planning</h3>
          <p>Timing, pickup points and the details that belong to a particular tour.</p>
        </article>
        <article>
          <p class="eyebrow">04</p>
          <h3>With the island</h3>
          <p>Forty percent of tour revenue is contributed to charitable initiatives in the local Zanzibar community.</p>
        </article>
      </div>
    </section>
  </main>"""
    return document(
        "About | Mranzi Tours & Safaris",
        "Mranzi Tours & Safaris arranges private Zanzibar experiences and tailored journeys. Enquire on WhatsApp.",
        "/about.html",
        "luxury-villa.webp",
        0,
        "about",
        main,
    )


def contact():
    options = ['<option>A private journey</option>', '<option>A private safari, to discuss</option>', '<option>A coastal stay, to discuss</option>']
    for tour in TOURS:
        options.append(f"<option>{e(tour['title'])}</option>")
    main = f"""
  <main id="main">
    <header class="page-hero">
      {img("sunset-dhow.jpg", "Traditional dhow at sunset", "", lazy=False)}
      <div class="shade"></div>
      <div class="wrap">
        <p class="eyebrow">Let’s connect</p>
        <h1>Plan the journey.</h1>
        <p class="lede">Your next adventure starts with a conversation. Send the details on WhatsApp and we will reply there.</p>
      </div>
    </header>
    <section class="section" id="enquire">
      <div class="wrap contact-grid">
        <div>
          <p class="eyebrow">Enquiry</p>
          <h2 style="font-size:clamp(2.8rem,4vw,4.2rem)">Tell us the dates, and what you hope to see.</h2>
          <ul class="contact-list">
            <li><a href="{e(wa(GENERAL))}">WhatsApp {PHONE_DISPLAY}</a></li>
            <li><a href="tel:{PHONE}">Call {PHONE_DISPLAY}</a></li>
            <li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
            <li>Zanzibar, Tanzania · mranzitours.co.tz</li>
          </ul>
        </div>
        <form data-enquiry data-phone="{PHONE}">
          <label class="field"><span>Name</span><input name="name" required autocomplete="name"></label>
          <label class="field"><span>Experience</span><select name="experience">{''.join(options)}</select></label>
          <label class="field"><span>Dates</span><input name="dates" placeholder="Arrival and departure"></label>
          <label class="field"><span>Group size</span><input name="group" inputmode="numeric" placeholder="Number of guests"></label>
          <label class="field"><span>Note</span><textarea name="note" placeholder="Hotel area, interests, pace"></textarea></label>
          <button class="btn btn-solid" type="submit">Send on WhatsApp</button>
          <p class="form-note">This opens WhatsApp with your note. We confirm availability and the rate in the chat. Nothing is paid on this page.</p>
        </form>
      </div>
    </section>
  </main>"""
    return document(
        "Plan Your Journey | Mranzi Tours & Safaris",
        "Contact Mranzi Tours & Safaris on WhatsApp +255 777 466 868 or info@mranzitours.co.tz.",
        "/contact.html",
        "sunset-dhow.jpg",
        0,
        "contact",
        main,
    )


def missing():
    main = """
  <main id="main">
    <header class="page-hero">
      <img src="assets/hero-zanzibar-luxury.webp" alt="" width="1280" height="720" decoding="async">
      <div class="shade"></div>
      <div class="wrap">
        <p class="eyebrow">404</p>
        <h1>This page has drifted.</h1>
        <p class="lede">The experience you asked for is not on this site.</p>
        <a class="btn btn-ivory" style="margin-top:1.4rem" href="index.html">Return home</a>
      </div>
    </header>
  </main>"""
    return document(
        "Page not found | Mranzi Tours & Safaris",
        "The page you requested is not available.",
        "/404.html",
        "hero-zanzibar-luxury.webp",
        0,
        "",
        main,
    )


def write(path, html):
    dest = ROOT / path
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(html, encoding="utf-8")
    print(path)


def main():
    write("index.html", home())
    write("experiences/index.html", catalog())
    for index, tour in enumerate(TOURS):
        write(f"experiences/{tour['slug']}.html", detail(tour, index))
    write("destinations.html", destinations())
    write("about.html", about())
    write("contact.html", contact())
    write("404.html", missing())
    urls = ["/", "/experiences/", "/destinations.html", "/about.html", "/contact.html"]
    urls += [f"/experiences/{tour['slug']}.html" for tour in TOURS]
    body = "\n".join(f"  <url><loc>{SITE}{url}</loc></url>" for url in urls)
    write("sitemap.xml", f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{body}
</urlset>
""")
    write("robots.txt", f"User-agent: *\nAllow: /\nSitemap: {SITE}/sitemap.xml\n")
    print(f"{len(TOURS)} experiences")


if __name__ == "__main__":
    main()
