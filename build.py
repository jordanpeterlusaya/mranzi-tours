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
        "image": "stone-town-doors.jpg",
        "alt": "A carved wooden door in a Stone Town lane",
        "summary": "UNESCO Stone Town in the morning, then a working spice farm in the island’s green heart.",
        "body": [
            "Stone Town is a UNESCO World Heritage Site — coral-stone lanes, carved doors and a mix of Swahili, Arab, Indian and European history within walking distance of the seafront.",
            "The afternoon continues inland to a spice farm, where cloves, cinnamon, vanilla and other crops that earned Zanzibar the name Spice Island are seen, smelled and tasted as they grow.",
        ],
        "highlights": [
            "UNESCO Stone Town walking tour",
            "Carved doors, seafront and historic landmarks",
            "Spice farm with cloves, cinnamon and tropical fruit",
        ],
    },
    {
        "slug": "spice-tour",
        "title": "Spice Tour",
        "cat": "flavours",
        "cat_label": "Flavours & Lifestyle",
        "image": "spice-cloves.jpg",
        "alt": "Clove buds on a spice farm in Zanzibar",
        "summary": "Walk a working farm of cloves, cinnamon, vanilla and tropical fruit — Zanzibar as the Spice Island.",
        "body": [
            "Central Zanzibar’s farms still grow the crops that made the island’s trading fortune: cloves, cinnamon, nutmeg, vanilla, cardamom, pepper and more beneath coconut palms.",
            "A local guide leads you through the plantation to touch, smell and taste spices and seasonal fruit, and to see how they are used in cooking and daily life.",
        ],
        "highlights": [
            "Cloves, cinnamon, vanilla and tropical fruit",
            "Hands-on tasting in a working plantation",
            "The story of Zanzibar as the Spice Island",
        ],
    },
    {
        "slug": "prison-island",
        "title": "Prison Island Tour",
        "cat": "ocean",
        "cat_label": "Ocean & Islands",
        "image": "lux-coast-estate.webp",
        "alt": "A coastal island estate above turquoise water",
        "summary": "Changuu Island: Aldabra giant tortoises, historic ruins and a short boat ride from Stone Town.",
        "body": [
            "Prison Island — also called Changuu — sits a short boat ride northwest of Stone Town. The prison complex was completed in the 1890s but never held prisoners; it later became a yellow-fever quarantine station for ships arriving in East Africa.",
            "Today the island is best known for its sanctuary of Aldabra giant tortoises, descendants of animals gifted from the Seychelles in 1919. The visit usually leaves time for the sanctuary, a walk through the historic buildings, and the clear water around the shore.",
        ],
        "highlights": [
            "Boat crossing from Stone Town to Changuu Island",
            "Aldabra giant tortoise sanctuary",
            "Historic prison and quarantine buildings",
        ],
    },
    {
        "slug": "jozani-forest",
        "title": "Jozani Forest",
        "cat": "nature",
        "cat_label": "Wildlife & Nature",
        "image": "jozani-forest.webp",
        "alt": "Red colobus monkey in Jozani Forest",
        "summary": "Jozani Chwaka Bay National Park and the endemic Zanzibar red colobus.",
        "body": [
            "Jozani is Zanzibar’s principal protected forest and part of Jozani Chwaka Bay National Park — groundwater forest, coastal woodland and mangrove boardwalks in one reserve.",
            "It is the best place to look for the Zanzibar red colobus, a rare monkey found only on this island. Guides walk the trails at a quiet pace so the trees, birds and troops of colobus remain the focus.",
        ],
        "highlights": [
            "Jozani Chwaka Bay National Park",
            "Endemic Zanzibar red colobus",
            "Forest trails and mangrove boardwalk",
        ],
    },
    {
        "slug": "stone-town-tour",
        "title": "Stone Town Tour",
        "cat": "heritage",
        "cat_label": "Heritage & Culture",
        "image": "stonetown.webp",
        "alt": "A colourful lane in historic Stone Town",
        "summary": "A guided walk through UNESCO Stone Town: fort, cathedral, markets and carved doors.",
        "body": [
            "Stone Town is the historic heart of Zanzibar City and a UNESCO World Heritage Site since 2000 — one of the best-preserved Swahili trading towns on the East African coast.",
            "The walk typically takes in the Old Fort, the Anglican Cathedral and former slave market site, Forodhani Gardens on the seafront, Darajani Market and the famous carved Zanzibar doors that still mark the lanes.",
        ],
        "highlights": [
            "UNESCO World Heritage lanes",
            "Old Fort, Anglican Cathedral and Forodhani",
            "Carved doors and Darajani Market",
        ],
    },
    {
        "slug": "stone-town-prison-island",
        "title": "Stone Town + Prison Island",
        "cat": "heritage",
        "cat_label": "Heritage & Culture",
        "image": "island-resort-aerial.jpg",
        "alt": "An island resort ringed by turquoise reef",
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
        "alt": "Zanzibar red colobus among forest leaves",
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
        "image": "reef-snorkel.jpg",
        "alt": "Snorkellers above a coral reef in clear water",
        "summary": "A day under sail in the Menai Bay Conservation Area: reefs, sandbank, lagoon and seafood.",
        "body": [
            "Safari Blue is the classic full-day dhow excursion into the Menai Bay Conservation Area on Zanzibar’s south-west coast, usually boarding near Fumba.",
            "The day typically combines guided snorkelling on shallow reefs, a stop on a tidal sandbank, time in a warm mangrove lagoon, and a Swahili seafood lunch. Spinner and bottlenose dolphins live in the bay; sightings are common but never guaranteed.",
        ],
        "highlights": [
            "Traditional wooden dhow in Menai Bay",
            "Guided snorkelling and sandbank stop",
            "Mangrove lagoon and seafood lunch",
        ],
    },
    {
        "slug": "stone-town-lunch",
        "title": "Stone Town Tour with Lunch",
        "cat": "heritage",
        "cat_label": "Heritage & Culture",
        "image": "lux-chefs.webp",
        "alt": "Chefs preparing a Swahili lunch outdoors",
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
        "image": "signature-the-rock.webp",
        "alt": "The Rock restaurant on a coral outcrop",
        "summary": "The Rock restaurant on its coral outcrop, with time for the east-coast tide and views.",
        "body": [
            "The Rock sits on a coral rock off Michamvi on Zanzibar’s east coast — a restaurant reached on foot at low tide or by boat when the water rises.",
            "The visit is arranged around the tide: time for the approach, the coastal views and a meal at this well-known landmark rather than a hurried photograph stop.",
        ],
        "highlights": [
            "The Rock on its tidal coral outcrop",
            "East-coast views and coral formations",
            "Timing arranged around the tide",
        ],
    },
    {
        "slug": "butterfly-jozani",
        "title": "Butterfly Centre + Jozani Forest",
        "cat": "nature",
        "cat_label": "Wildlife & Nature",
        "image": "lux-butterflies.webp",
        "alt": "Orange butterflies in a tropical garden sanctuary",
        "summary": "A full day pairing the Zanzibar Butterfly Centre with Jozani Forest.",
        "body": [
            "The Zanzibar Butterfly Centre is a community garden a few minutes from Jozani, where native butterflies fly in a netted enclosure and local farmers rear pupae as an income from keeping forest standing.",
            "The same day continues into Jozani Chwaka Bay National Park for the red colobus, forest trails and mangrove boardwalk — a clear half-to-full day of the island’s land wildlife.",
        ],
        "highlights": [
            "Full day",
            "Zanzibar Butterfly Centre community project",
            "Jozani Forest and red colobus",
        ],
    },
    {
        "slug": "butterfly-jozani-spice",
        "title": "Butterfly Centre, Jozani Forest + Spice Tour",
        "cat": "flavours",
        "cat_label": "Flavours & Lifestyle",
        "image": "lux-butterfly-centre.webp",
        "alt": "Butterflies among leaves at the Butterfly Centre",
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
        "image": "the-rock.webp",
        "alt": "The Rock restaurant standing in the sea",
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
        "image": "lux-stone-town-aerial.webp",
        "alt": "Aerial view of Stone Town beside turquoise water",
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
        "image": "lux-dhow-sail.webp",
        "alt": "A traditional dhow under full sail",
        "summary": "A private full day on a wooden dhow in Menai Bay: sailing, snorkelling, lagoon and lunch.",
        "body": [
            "This private arrangement keeps the spirit of Safari Blue — Menai Bay under sail — with a boat set aside for your party rather than a shared departure.",
            "Expect snorkelling over coral, a sandbank when the tide allows, time in the mangrove lagoon and a seafood lunch arranged with the crew. Dolphin sightings depend on the animals that day.",
        ],
        "highlights": [
            "Full day on a private dhow",
            "Snorkelling, sandbank and mangrove lagoon",
            "Seafood lunch with your party",
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
        "image": "combo-znz-shore-hd.jpg",
        "alt": "White sand and clear shallows on the Zanzibar coast",
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
        "alt": "Forodhani night market in Stone Town",
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
        "image": "lux-lighthouse-island.webp",
        "alt": "A green island with a lighthouse in clear water",
        "summary": "A privately protected island of reef sanctuary, forest and carefully managed wildlife.",
        "body": [
            "Chumbe Island Coral Park is a privately managed nature reserve off Zanzibar’s west coast, known for one of the region’s most carefully protected reef sanctuaries and a forest reserve ashore.",
            "Visits are limited and guided, with time for the reef, the forest trails and the island’s quiet wildlife at the pace the reserve allows.",
        ],
        "highlights": [
            "Privately protected coral reef sanctuary",
            "Forest reserve and island wildlife",
            "Guided visit with limited numbers",
        ],
    },
    {
        "slug": "spice-cooking",
        "title": "Spice Tour + Swahili Cooking Lesson",
        "cat": "flavours",
        "cat_label": "Flavours & Lifestyle",
        "image": "private-chef.webp",
        "alt": "A plated seafood meal",
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
        "image": "lux-coast-bay.webp",
        "alt": "Turquoise bay and palm coastline",
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
        "image": "combo-znz-aerial-hd.jpg",
        "alt": "Aerial view of the Zanzibar coastline",
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
        "image": "clear-kayak.jpg",
        "alt": "A clear kayak on luminous turquoise water",
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
        "summary": "Snorkel the protected reef around Mnemba Atoll, with turtles and clear water.",
        "body": [
            "Mnemba is a small private island ringed by a marine conservation area off the north-east coast. Boats reach the reef from beaches such as Matemwe; the island itself is closed to casual landing.",
            "In the water the draw is coral gardens, tropical fish and, often, green turtles. A sandbank stop is arranged when the tide and conditions allow.",
        ],
        "highlights": [
            "Mnemba Atoll marine reserve",
            "Reef snorkelling with tropical fish and turtles",
            "Sandbank stop when the tide allows",
        ],
    },
    {
        "slug": "mnemba-aquarium-kendwa",
        "title": "Mnemba, Aquarium + Kendwa Beach",
        "cat": "ocean",
        "cat_label": "Ocean & Islands",
        "image": "salaam-turtles.jpg",
        "alt": "Sea turtles in clear turquoise water",
        "summary": "A full north-coast day: Mnemba reef, the Nungwi turtle aquarium and Kendwa Beach.",
        "body": [
            "The morning is on the water at Mnemba Atoll for snorkelling over coral in clear, shallow water.",
            "On shore near Nungwi, the natural aquarium — a tidal coral pool — cares for rescued sea turtles you can observe up close. The afternoon settles on Kendwa Beach, known for soft sand and swimming that stays easy through the tide.",
        ],
        "highlights": [
            "Full day",
            "Mnemba Atoll snorkelling",
            "Nungwi turtle aquarium and Kendwa Beach",
        ],
    },
    {
        "slug": "stone-town-spice-prison",
        "title": "Stone Town, Spice Tour + Prison Island",
        "cat": "heritage",
        "cat_label": "Heritage & Culture",
        "image": "sandbank-hd.jpg",
        "alt": "Clear turquoise water approaching Prison Island",
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
for tour in TOURS:
    source = " ".join(tour["body"] + tour["highlights"]).lower()
    if "full day" in source or "full-day" in source:
        tour["duration"] = "Full day"


def meta_line(tour):
    parts = []
    if tour.get("duration"):
        parts.append(e(tour["duration"]))
    if tour.get("price"):
        parts.append(e(tour["price"]))
    if not parts:
        return ""
    return f'<p class="pkg-meta">{" · ".join(parts)}</p>'


WA_ICON = (
    '<svg class="wa-icon" viewBox="0 0 24 24" aria-hidden="true" focusable="false">'
    '<path fill="currentColor" d="M12.04 2C6.58 2 2.15 6.4 2.15 11.83c0 1.74.46 3.44 1.34 4.94L2 22l5.39-1.4a10 10 0 0 0 4.65 1.18h.01c5.46 0 9.89-4.4 9.89-9.83C21.94 6.4 17.5 2 12.04 2zm5.76 14.05c-.24.68-1.4 1.3-1.94 1.38-.5.07-1.12.1-1.81-.11-.41-.13-.95-.31-1.64-.61-2.88-1.25-4.76-4.15-4.9-4.34-.14-.2-1.16-1.54-1.16-2.94s.73-2.08 1-2.37c.24-.28.64-.41 1.02-.41.12 0 .23 0 .33.01.3.01.44.03.64.5.24.57.81 1.97.88 2.11.07.14.12.31.02.49-.09.18-.14.29-.27.45-.14.16-.29.35-.41.47-.14.13-.28.28-.12.54.16.26.7 1.16 1.51 1.88 1.04.92 1.91 1.21 2.18 1.35.27.13.43.11.59-.07.16-.18.68-.79.86-1.06.18-.27.36-.22.6-.13.24.09 1.54.73 1.8.86.27.13.44.2.51.31.06.11.06.64-.18 1.32z"/>'
    "</svg>"
)


def experience_options(selected=""):
    choices = ["A private journey", "A private safari, to discuss", "A coastal stay, to discuss"]
    choices += [tour["title"] for tour in TOURS]
    options = []
    for choice in choices:
        selected_attr = " selected" if choice == selected else ""
        options.append(f"<option{selected_attr}>{e(choice)}</option>")
    return "".join(options)


def book_button(label, experience="", classes="btn btn-wa"):
    return (
        f'<button type="button" class="{classes}" data-book data-experience="{e(experience)}">'
        f"{WA_ICON}{e(label)}</button>"
    )


def booking_fields(selected=""):
    return f"""
      <label class="field"><span>Name</span><input name="name" required autocomplete="name"></label>
      <label class="field"><span>Experience</span><select name="experience" required>{experience_options(selected)}</select></label>
      <label class="field"><span>Dates</span><input name="dates" required placeholder="Arrival and departure"></label>
      <label class="field"><span>Group size</span><input name="group" required inputmode="numeric" placeholder="Number of guests"></label>
      <label class="field"><span>Pickup</span><input name="pickup" required placeholder="Hotel or area in Zanzibar"></label>
      <label class="field"><span>Note</span><textarea name="note" placeholder="Pace, interests, anything we should know"></textarea></label>
      <button class="btn btn-wa" type="submit">{WA_ICON}Book on WhatsApp</button>
      <p class="form-note">WhatsApp opens only after these details are filled in. We confirm availability in the chat. Nothing is paid on this page.</p>"""


def booking_form(selected=""):
    return f'<form class="booking-form" data-enquiry data-phone="{PHONE}">{booking_fields(selected)}</form>'


DIMS = {
    "lux-butterfly-centre.webp": (1600, 2000),
    "lux-coast-estate.webp": (1600, 2000),
    "lux-coast-bay.webp": (1600, 2000),
    "lux-lighthouse-island.webp": (1600, 2000),
    "lux-chefs.webp": (1600, 2000),
    "lux-dhow-sail.webp": (1600, 2000),
    "lux-stone-town-aerial.webp": (1600, 2000),
    "lux-butterflies.webp": (1600, 2000),
    "spice-cloves.jpg": (1920, 1280),
    "signature-the-rock.webp": (900, 1200),
    "sandbank-hd.jpg": (1920, 1440),
    "salaam-turtles.jpg": (1024, 1024),
    "reef-snorkel.jpg": (1024, 768),
    "pemba.webp": (354, 670),
    "island-resort-aerial.jpg": (1024, 1024),
    "combo-znz-shore-hd.jpg": (1920, 1280),
    "combo-znz-palms-hd.jpg": (1920, 1280),
    "combo-znz-island-hd.jpg": (1920, 1439),
    "combo-znz-aerial-hd.jpg": (1920, 1078),
    "clear-kayak.jpg": (559, 1037),
    "chef-luxury.jpg": (1800, 2700),
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
    "blue-lagoon.webp": (1280, 960),
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
    "stone-town-doors.jpg": (830, 830),
    "private-chef.webp": (1280, 853),
    "prison-island.webp": (1280, 353),
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
        {book_button("WhatsApp", "A private journey", "btn btn-wa nav-wa")}
      </nav>
    </div>
  </header>"""


# Official profile URLs when available. Empty = fall back to WhatsApp contact.
SOCIAL_INSTAGRAM = ""
SOCIAL_FACEBOOK = ""


def social_links(prefix=""):
    share = e(SITE + "/")
    ig = SOCIAL_INSTAGRAM or wa(GENERAL)
    fb = SOCIAL_FACEBOOK or f"https://www.facebook.com/sharer/sharer.php?u={share}"
    base = f"{prefix}assets/social"
    return f"""
      <div class="social" aria-label="Social links">
        <a class="social-link" href="{e(wa(GENERAL))}" target="_blank" rel="noopener">
          <img src="{base}/whatsapp.svg" alt="" width="22" height="22" decoding="async">
          <span>WhatsApp</span>
        </a>
        <a class="social-link" href="{e(ig)}" target="_blank" rel="noopener">
          <img src="{base}/instagram.svg" alt="" width="22" height="22" decoding="async">
          <span>Instagram</span>
        </a>
        <a class="social-link" href="{e(fb)}" target="_blank" rel="noopener">
          <img src="{base}/facebook.svg" alt="" width="22" height="22" decoding="async">
          <span>Facebook</span>
        </a>
        <a class="social-link" href="mailto:{EMAIL}">
          <img src="{base}/email.svg" alt="" width="22" height="22" decoding="async">
          <span>Email</span>
        </a>
      </div>"""




def footer(prefix, experience=""):
    return f"""
  <footer class="site-footer">
    <div class="wrap foot-grid">
      <div class="foot-brand">
        <h2>Mranzi</h2>
        <p>Private experiences across Zanzibar and Tanzania, arranged at your pace.</p>
        {social_links(prefix)}
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
          <li><button type="button" class="foot-wa" data-book data-experience="{e(experience or "A private journey")}">{WA_ICON}WhatsApp {PHONE_DISPLAY}</button></li>
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
  <button type="button" class="dock" data-book data-experience="{e(experience)}">{WA_ICON}Book on WhatsApp</button>
  <dialog class="booking" data-booking>
    <form class="booking-form" data-enquiry data-phone="{PHONE}">
      <div class="booking-head">
        <p class="eyebrow">Book</p>
        <button class="booking-close" type="button" data-booking-close>Close</button>
      </div>
      <h2>Your details</h2>
      {booking_fields(experience)}
    </form>
  </dialog>
  <script src="{prefix}js/site.js"></script>"""


def document(title, description, path, image, depth, current, main, schema="", enquire=None):
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
{footer(prefix, enquire or "")}
</body>
</html>
"""


def img(name, alt, prefix, lazy=True):
    loading = 'loading="lazy"' if lazy else 'loading="eager"'
    return f'<img src="{prefix}assets/{name}" alt="{e(alt)}" {dims(name)} {loading} decoding="async">'


def home():
    schema = """<script type="application/ld+json">
  {"@context":"https://schema.org","@type":"TravelAgency","name":"Mranzi Tours & Safaris","url":"https://mranzitours.co.tz/","email":"info@mranzitours.co.tz","telephone":"+255777466868","address":{"@type":"PostalAddress","addressLocality":"Zanzibar","addressCountry":"TZ"},"areaServed":["Zanzibar","Tanzania"]}
  </script>"""
    packages = []
    for tour in TOURS:
        packages.append(f"""
        <article class="pkg" data-cat="{tour['cat']}">
          <a class="pkg-media" href="experiences/{tour['slug']}.html">{img(tour['image'], tour['alt'], "")}</a>
          <div class="pkg-copy">
            <p class="eyebrow">{e(tour['cat_label'])}</p>
            <h3><a href="experiences/{tour['slug']}.html">{e(tour['title'])}</a></h3>
            <p>{e(tour['summary'])}</p>
            {meta_line(tour)}
            <div class="pkg-actions">
              <a class="text-link" href="experiences/{tour['slug']}.html">View details</a>
              {book_button("Book", tour["title"])}
            </div>
          </div>
        </article>""")
    main = f"""
  <main id="main">
    <section class="hero" aria-label="Introduction">
      <video class="hero-media" autoplay muted loop playsinline poster="assets/hero-poster.webp" width="720" height="1280">
        <source src="assets/video/hero.mp4" type="video/mp4">
      </video>
      <div class="hero-shade"></div>
      <div class="wrap hero-content">
        <ul class="hero-trust" aria-label="Guest review platforms">
          <li>
            <img src="assets/trust/badge-tripadvisor.svg" alt="Tripadvisor" width="64" height="64">
            <span>Tripadvisor</span>
          </li>
          <li>
            <img src="assets/trust/badge-google.svg" alt="Google Reviews" width="64" height="64">
            <span>Google Reviews</span>
          </li>
          <li>
            <img src="assets/trust/badge-trustpilot.svg" alt="Trustpilot" width="64" height="64">
            <span>Trustpilot</span>
          </li>
        </ul>
        <div class="hero-copy">
          <h1>Discover.<br>Experience.</h1>
          <p class="lede">Private journeys across Zanzibar and Tanzania.</p>
          <a class="btn btn-ivory" href="#experiences">Explore Experiences</a>
        </div>
      </div>
    </section>
    <section class="section" id="experiences">
      <div class="wrap">
        <div class="section-head">
          <p class="eyebrow">The collection</p>
          <h2>Experiences</h2>
        </div>
        <div class="filters" data-filters>
          <button type="button" data-filter="all" aria-pressed="true">All</button>
          <button type="button" data-filter="heritage">Heritage</button>
          <button type="button" data-filter="nature">Nature</button>
          <button type="button" data-filter="ocean">Ocean</button>
          <button type="button" data-filter="flavours">Flavours</button>
        </div>
        <div class="pkg-list">
          {''.join(packages)}
        </div>
      </div>
    </section>
  </main>"""
    return document(
        "Mranzi Tours & Safaris | Private Zanzibar & Tanzania",
        "Private Zanzibar experiences with Mranzi Tours & Safaris. View each journey and enquire on WhatsApp.",
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
            {meta_line(tour)}
            <div class="pkg-actions">
              <a class="text-link" href="{tour['slug']}.html">View details</a>
              {book_button("Book", tour["title"])}
            </div>
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
    main = f"""
  <main id="main">
    <header class="page-hero">
      {img(tour['image'], tour['alt'], "../", lazy=False)}
      <div class="shade"></div>
      <div class="wrap">
        <p class="crumbs"><a href="index.html">Experiences</a> · {e(tour['cat_label'])}</p>
        <h1>{e(tour['title'])}</h1>
        {meta_line(tour)}
      </div>
    </header>
    <section class="section" style="padding-top:0">
      <div class="wrap exp-layout">
        <div class="exp-copy">
          <p class="lede">{e(tour['summary'])}</p>
          {paragraphs}
        </div>
        <aside class="exp-aside">
          <p class="eyebrow">Book</p>
          {booking_form(tour["title"])}
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
        enquire=tour["title"],
    )


def destinations():
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
          {book_button("Discuss a private safari", "A private safari, to discuss", "btn btn-wa")}
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
          {book_button("Ask about a stay", "A coastal stay, to discuss", "btn btn-wa")}
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
            <li><button type="button" class="foot-wa" data-book data-experience="A private journey">{WA_ICON}WhatsApp {PHONE_DISPLAY}</button></li>
            <li><a href="tel:{PHONE}">Call {PHONE_DISPLAY}</a></li>
            <li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
            <li>Zanzibar, Tanzania · mranzitours.co.tz</li>
          </ul>
        </div>
        {booking_form("A private journey")}
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
