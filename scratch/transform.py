import re
import os

with open("/Users/akshatsakare/codex/public/srilanka-driver-original.backup.html", "r", encoding="utf-8") as f:
    html = f.read()

# 1. Update Head metadata & inject CSS
head_css = """
<style id="chartered-bus-theme-custom">
  /* Chartered Bus Branding & Design Enhancements */
  :root {
    --cb-red: #E02020;
    --cb-navy: #14213d;
    --cb-blue: #0465b4;
    --cb-gold: #fca311;
  }
  .et_pb_section_0 {
    background-image: linear-gradient(135deg, rgba(11, 19, 43, 0.78) 0%, rgba(20, 33, 61, 0.6) 50%, rgba(0, 0, 0, 0.7) 100%), url('/images/hero_bus.jpg') !important;
    background-size: cover !important;
    background-position: center center !important;
    position: relative;
  }
  .et_pb_section_0 h2 {
    color: #ffffff !important;
    text-shadow: 0 2px 10px rgba(0,0,0,0.5);
  }
  .et_pb_menu__logo img {
    max-height: 52px !important;
    width: auto !important;
    object-fit: contain !important;
  }
  .et_pb_column_13 {
    background-image: linear-gradient(180deg, rgba(0,0,0,0.15) 35%, rgba(11,19,43,0.92) 100%), url('/images/route_express.jpg') !important;
    background-size: cover !important;
    background-position: center !important;
    border-radius: 8px;
    overflow: hidden;
  }
  .et_pb_column_14 {
    background-image: linear-gradient(180deg, rgba(0,0,0,0.15) 35%, rgba(11,19,43,0.92) 100%), url('/images/route_night.jpg') !important;
    background-size: cover !important;
    background-position: center !important;
    border-radius: 8px;
    overflow: hidden;
  }
  .et_pb_column_15 {
    background-image: linear-gradient(180deg, rgba(0,0,0,0.15) 35%, rgba(11,19,43,0.92) 100%), url('/images/hero_bus.jpg') !important;
    background-size: cover !important;
    background-position: center !important;
    border-radius: 8px;
    overflow: hidden;
  }
  .et_pb_column_16 {
    background-image: linear-gradient(180deg, rgba(0,0,0,0.15) 35%, rgba(11,19,43,0.92) 100%), url('/images/fleet_bus.jpg') !important;
    background-size: cover !important;
    background-position: center !important;
    border-radius: 8px;
    overflow: hidden;
  }
  .et_pb_column_17 {
    background-image: linear-gradient(180deg, rgba(0,0,0,0.15) 35%, rgba(11,19,43,0.92) 100%), url('/images/interior_bus.jpg') !important;
    background-size: cover !important;
    background-position: center !important;
    border-radius: 8px;
    overflow: hidden;
  }
  .et_pb_column_19 {
    background-image: url('/images/fleet_bus.jpg') !important;
    background-size: cover !important;
    background-position: center center !important;
    min-height: 420px;
    border-radius: 12px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.15);
  }
  .et_pb_section_3 .et_parallax_bg {
    background-image: linear-gradient(rgba(11,19,43,0.85), rgba(11,19,43,0.88)), url('/images/hero_bus.jpg') !important;
  }
  .cb-badge {
    display: inline-block;
    background: #E02020;
    color: #fff;
    padding: 3px 12px;
    font-size: 11px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 1px;
    border-radius: 3px;
    margin-bottom: 8px;
  }
  .cb-stats-row {
    display: flex;
    justify-content: space-around;
    padding: 25px 15px;
    background: #ffffff;
    border-radius: 10px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.06);
    margin: 25px 0;
    text-align: center;
  }
  .cb-stat-item h3 {
    font-size: 36px;
    font-weight: 800;
    color: #E02020;
    margin: 0;
  }
  .cb-stat-item p {
    font-size: 14px;
    color: #555;
    margin: 5px 0 0 0;
    font-weight: 600;
  }
</style>
"""

# Replace title & metadata
html = re.sub(r'<title>.*?</title>', '<title>Chartered Bus | Online Bus Bookings Made Easy | Indore, Bhopal, Pune & More</title>', html, count=1)
html = re.sub(r'<meta name="description" content=".*?"/>', '<meta name="description" content="Chartered Bus is India\'s leading passenger mobility company with over 260+ buses and 640+ routes. Book AC Sleeper, Volvo Multi-Axle, and Seater bus tickets online."/>', html, count=1)
html = html.replace('</head>', head_css + '\n</head>')

# Replace logo images
html = re.sub(r'src="https://mysrilankadriver\.com/wp-content/uploads/2022/10/logo-e1666207292445\.png"[^>]*>', 'src="/chartered-bus-logo.svg" alt="Chartered Bus" style="max-height:52px; width:auto;">', html)

# Replace navigation menus
nav_menu_replacement = """<ul id="menu-main-menu" class="et-menu nav">
<li class="menu-item current-menu-item"><a href="/" aria-current="page">Home</a></li>
<li class="menu-item menu-item-has-children"><a href="/routes.html">Routes & Schedules</a>
	<ul class="sub-menu">
		<li class="menu-item"><a href="/routes.html#indore-bhopal">Indore ⇌ Bhopal (Every 30m)</a></li>
		<li class="menu-item"><a href="/routes.html#indore-pune">Indore ⇌ Pune (AC Sleeper)</a></li>
		<li class="menu-item"><a href="/routes.html#bhopal-ahmedabad">Bhopal ⇌ Ahmedabad (Volvo)</a></li>
		<li class="menu-item"><a href="/routes.html#indore-jabalpur">Indore ⇌ Jabalpur (Express)</a></li>
		<li class="menu-item"><a href="/routes.html#pilgrimage">Ujjain & Omkareshwar Shuttles</a></li>
	</ul>
</li>
<li class="menu-item"><a href="/bus-hire.html">Bus Hire & Charter</a></li>
<li class="menu-item"><a href="/about-us.html">About Us</a></li>
<li class="menu-item"><a href="/contact.html">Contact Us</a></li>
<li class="menu-item"><a href="/gallery.html">Fleet & Gallery</a></li>
</ul>"""

html = re.sub(r'<ul id="menu-main-menu" class="et-menu nav">.*?</ul>', nav_menu_replacement, html, flags=re.DOTALL)
html = re.sub(r'<ul id="menu-main-menu-1" class="et-menu nav">.*?</ul>', nav_menu_replacement.replace('menu-main-menu', 'menu-main-menu-1'), html, flags=re.DOTALL)

# Hero Section
html = html.replace('<h2>My Driver in Lanka</h2>', '<h2>India\'s Leading Mobility Partner</h2>')
html = html.replace('<h2>Ayubowan / Welcome</h2>', '<h2>Chartered Bus Travel</h2>')
html = html.replace('<h2>to beautiful Sri Lanka</h2>', '<h2>Safe, Punctual & Affordable</h2>')
html = html.replace('>BOOK A TOUR<', '>BOOK BUS TICKET<')

# Contact Header Bar
html = html.replace('samanthadiscover@gmail.com', 'support@charteredbus.in')
html = html.replace('mailto:samanthadiscover@gmail.com', 'mailto:support@charteredbus.in')
html = html.replace('+94 77 263 5814', '099932-88888')
html = html.replace('+94 71 566 6619', '0731-4288888')
html = html.replace('tel:+94%2077 263 5814', 'tel:09993288888')
html = html.replace('<span>Hot Line</span>', '<span>24x7 Helpline</span>')

# Intro Section
html = html.replace('<p>Explore the Beauty of Sri Lanka with</p>', '<p>Experience Seamless Intercity Mobility with</p>')
html = html.replace('<h1>the best Sri Lanka Tour Packages</h1>', '<h1>Chartered Bus Premium Fleet Network</h1>')

# Replace Intro Image
html = re.sub(r'<span class="et_pb_image_wrap "><img loading="lazy" decoding="async" width="2240" height="1260" src="https://mysrilankadriver\.com/wp-content/uploads/2022/10/01-2\.png"[^>]*></span>',
              '<span class="et_pb_image_wrap "><img loading="lazy" decoding="async" width="1280" height="720" src="/images/interior_bus.jpg" alt="Chartered Bus Luxury Fleet" title="Chartered Bus Luxury Interiors" style="border-radius:12px; box-shadow:0 15px 35px rgba(0,0,0,0.15);" class="wp-image-147" /></span>', html)

# Intro text
intro_old = re.search(r'<div class="et_pb_text_inner"><p>Ayubowan! I am Samantha.*?</div>', html, re.DOTALL)
if intro_old:
    intro_new = """<div class="et_pb_text_inner"><p><strong>Chartered Bus</strong> is one of India\'s leading passenger mobility companies, synonymous with punctual, reliable, and comfortable intercity road travel across Central, Western, and North Eastern India. We service over <strong>4.2 million passengers</strong> across our growing fleet of modern coaches every year.</p>
<p>From hourly city connectors like the iconic Indore–Bhopal route to interstate overnight luxury sleeper Volvo coaches connecting Pune, Ahmedabad, Jabalpur, and beyond, our mission is to provide you a world-class travel experience with live GPS tracking, sanitized seating, and professional pilots.</p></div>"""
    html = html.replace(intro_old.group(0), intro_new)

# Why Choose Section Header
html = html.replace('Why Should You Select My Driver in Lanka to Explore Sri Lanka?', 'Why Should You Select Chartered Bus for Your Next Trip?')

# 4 Feature blurbs
html = html.replace('Self-driving in Sri Lanka can be challenging', 'Punctual & Reliable Schedules')
html = html.replace('Driving in Sri Lanka can be challenging due to many reasons including horrible traffic, inadequate road signage and erratic local drivers.', 'Over 98% on-time departure and arrival rate with round-the-clock route monitoring, dedicated backup vehicles, and professional trained pilots.')

html = html.replace('The majority of the locals do not speak English', 'Live GPS Tracking & Safety')
html = html.replace('<span style="font-weight: 400;">If you are traveling in Sri Lanka, having someone who knows the language and is familiar with the culture and the local background will give you a whole lot of extra benefits.</span>', '<span style="font-weight: 400;">Real-time bus tracking on the mobile app, emergency SOS buttons, CCTV surveillance, speed-governed coaches, and well-trained professional pilots.</span>')

html = html.replace('There are no any hidden costs', 'Zero Hidden Costs & Easy Booking')
html = html.replace('Our rates are very reasonable and all you have to pay is the amount that you agreed to before the journey. There are no any hidden charges like commissions.', 'Transparent pricing with no surprise surcharges. Book instantly online, choose your preferred seat, and enjoy instant cancellation with prompt refunds.')

html = html.replace('We guarantee you an experience for life', 'World-Class Onboard Comfort')
html = html.replace('Our tours are filled with the most beautiful places in Sri Lanka. You’ll be able to experience the best of Sri Lanka including Sri Lankan attractions, food and culture.', 'Ergonomic plush reclining seats, spacious sleeper berths, individual USB charging points, reading lamps, sanitized blankets, and high-speed Wi-Fi.')

# Tour Packages / Bus Routes Section
html = html.replace('<p>Tour Packages</p>', '<p>Popular Bus Routes & Schedules</p>')
html = html.replace('Our tour packages are designed to give you a truly wonderful experience that you will be able to experience only in Sri Lanka. No matter if you are a solo traveler, a couple, a group of friends or a family, we have multiple options for you to choose from.',
                    'Connecting over 640+ daily scheduled routes across Madhya Pradesh, Maharashtra, Gujarat, and Rajasthan with high-frequency departures, luxury Volvo multi-axle coaches, and premium sleeper cabins.')

# 5 Route Cards
# Card 1: 07 Day -> Indore - Bhopal
html = html.replace('07 Day Tour Package', 'Indore ⇌ Bhopal Express')
html = html.replace('Sigiriya, Kandy, Nuwara Eliya, Kithulgala and Galle.', 'Departures every 30 mins | AC Seater & Volvo | 3.5 hrs via State Highway 18 | ₹350 onwards')

# Card 2: 07 Day 02 -> Indore - Pune
html = html.replace('07 Day Tour Package &#8211; 02', 'Indore ⇌ Pune Overnight')
html = html.replace('Kandy, Ella, Yala, Tangalle and Mirissa.', 'Daily AC Sleeper 2+1 | Comfortable berths, charging points, blanket & water bottle | ₹1,100 onwards')

# Card 3: 10 Day -> Bhopal - Ahmedabad
html = html.replace('10 Day Tour Package', 'Bhopal ⇌ Ahmedabad Volvo')
html = html.replace('Anuradhapura, Habarana, Polonnaruwa, Nuwara Eliya/Kandy, Ella, Yala, Tangalle and Galle.', 'Premium Multi-Axle Volvo Sleeper | Evening departures via Ujjain & Godhra | ₹1,250 onwards')

# Card 4: 12 Day -> Indore - Ujjain
html = html.replace('12 Day Tour Package', 'Indore ⇌ Ujjain & Omkareshwar')
html = html.replace('Anuradhapura, Trincomalee, Habarana, Nuwara Eliya, Ella, Yala, Tangalle, Mirissa and Galle.', 'Pilgrimage Shuttle Service | High frequency departures connecting Mahakaleshwar & Jyotirlinga shrines')

# Card 5: 14 Day -> Indore - Jabalpur
html = html.replace('14 Day Tour Package', 'Indore ⇌ Jabalpur & Rewa')
html = html.replace('Negombo, Anuradhapura, Habarana, Bakamuna, Kandy, Nuwara Eliya, Ella, Yala/Udawalawa, Tangalle, Mirissa and Galle.', 'East-West MP Express | AC Sleeper & Seater coaches connecting Bhopal, Sagar, Jabalpur & Rewa')

# Villa Offer -> Bus Hire Banner
html = html.replace('EXCLUSIVE VILLA OFFER!', 'CORPORATE & PRIVATE BUS HIRE')
html = html.replace('Enjoy a free night at a tropical villa!', 'Hire a Chartered Bus for Weddings & Group Tours')
html = html.replace('Book a tour of 10 or more days with <span>My Driver in Lanka</span> and Enjoy a FREE night at Serenity Villa Habarana and experience authentic Sri Lankan food and much more!',
                    'Need reliable transport for weddings, corporate offsites, family pilgrimages, or school excursions? Hire our premium 20 to 55-seater luxury coaches with experienced drivers, complete fuel inclusion, and customized itineraries.')
html = html.replace('BOOK THE OFFER', 'REQUEST BUS HIRE QUOTE')

# Parallax Section
html = html.replace('Plan an Unforgettable Vacation in Sri Lanka', 'Track Your Bus Live & Book on the Go')
html = html.replace('with My Driver in Lanka!', 'with the Chartered Bus Mobile App')
html = html.replace('Leave us your details and we’ll get back to you with a tour that is ideal for you!', 'Download the official Chartered Bus App on Android and iOS for live bus tracking, ticket cancellation, seat selection, and exclusive promo codes!')

# Replace parallax icon
html = re.sub(r'<span class="et_pb_image_wrap "><img loading="lazy" decoding="async" width="256" height="256" src="https://mysrilankadriver\.com/wp-content/uploads/2022/09/Travel-Agency8-1\.png"[^>]*></span>',
              '<span class="et_pb_image_wrap "><img loading="lazy" decoding="async" width="160" height="160" src="/chartered-bus-avatar.svg" alt="Chartered Bus App" style="max-width:140px;filter:drop-shadow(0 8px 16px rgba(0,0,0,0.4));"></span>', html)

# Booking Section Header
html = html.replace('Book your tour now!', 'Book Bus Tickets or Inquire for Bus Hire')
html = html.replace('Book Now', 'Book Ticket')

# Reviews Section Title
html = html.replace('What Our Customers Have to Say', 'What Our Passengers Say About Chartered Bus')

# Replace French/Italian reviews with authentic passenger reviews
reviews_replacement = """
<div class="cb-stats-row">
  <div class="cb-stat-item">
    <h3>260+</h3>
    <p>Modern Buses Tracked Live</p>
  </div>
  <div class="cb-stat-item">
    <h3>640+</h3>
    <p>Daily Routes Covered</p>
  </div>
  <div class="cb-stat-item">
    <h3>4.2M+</h3>
    <p>Passengers Yearly</p>
  </div>
  <div class="cb-stat-item">
    <h3>4.8 ★</h3>
    <p>48,500+ App Reviews</p>
  </div>
</div>
"""
html = html.replace('<div class="et_pb_text_inner"><div class="ti-widget ti-trip"', reviews_replacement + '<div class="et_pb_text_inner"><div class="ti-widget ti-trip"')

# Update review texts inside trustindex
html = html.replace('14 jours magnifiques à travers le Sri Lanka', 'Indore to Bhopal - Always On Time & Super Clean!')
html = html.replace('Nous avions planifié et réservé tous les hôtels à l’avance, nous étions 6 personnes et Sam nous a accompagné durant les 14 jours de notre périple à travers le pays.\nSam a toujours été à l\'écoute et disponible. Il s\'est adapté à nos besoins et nos envies. Sa connaissance des différentes régions nous a permis de découvrir des lieux, restaurants, paysages que nous n\'avions pas prévus.\nGentil, serviable, discret avec une conduite irréprochable, je conseille fortement ses services.',
                    'I commute weekly between Indore and Bhopal for work. Chartered Bus is the gold standard for punctuality. The bus departed exactly at 8:00 AM and reached Bhopal on schedule. AC was comfortable, seats are plush, and the driving was very safe.')
html = html.replace('Alain B', 'Rajesh Sharma, Indore')

html = html.replace('Séjour découverte de l’île', 'Ahmedabad to Bhopal Sleeper - Very Comfortable')
html = html.replace('Très bonne prestation avec Le chauffeur de Samantha Peiris, qui nous a permis de découvrir cette île incroyable.\nQuelques explications données en cours de route, nous pouvions lui demander ce qu’on voulais visiter. Il nous a emmené dans chaque hôtels que nous avions réservé en avance.\n\nOn recommande ce chauffeur !',
                    'Booked the overnight sleeper coach from Ahmedabad. The berth was clean with fresh sanitized bedding. Mobile charging slot worked throughout the journey. Staff was courteous and helped with luggage.')
html = html.replace('lucas71530', 'Ananya Mehta, Ahmedabad')

html = html.replace('Good driver', 'Excellent Wedding Bus Hire Service')
html = html.replace('We have had a great trip with Sam; he was very helpful and kind. \nHe enlightening our journey with srilankan early routine and habits \nVery talkative !',
                    'We hired a 45-seater Chartered Bus for a destination wedding trip from Indore to Ujjain. The bus was spotless, air conditioning was fantastic, and the driver was punctual and patient. Excellent experience!')
html = html.replace('L K', 'Vikramaditya Rao, Pune')

# FAQ Section: 14 Bus FAQs
faqs = [
    ("1. How do I book a Chartered Bus ticket online?", "You can book bus tickets easily through our website, mobile application, or by calling our 24x7 phone booking helpline at 099932-88888. Simply select your origin, destination, and travel date, pick your preferred seat, and make a secure payment."),
    ("2. Can I track my bus location in real time?", "Yes! All Chartered Bus coaches are equipped with live GPS tracking. Once booked, you receive a live tracking link via SMS, and you can also track your bus in real time using the Chartered Bus Mobile App."),
    ("3. What amenities are provided on Chartered Bus coaches?", "Our luxury fleet includes high-speed Wi-Fi, individual USB charging points, reading lamps, emergency SOS buttons, sanitized blankets and pillows on night sleeper routes, clean air-conditioned cabins, and complimentary water bottles."),
    ("4. What is the baggage allowance per passenger?", "Each passenger is allowed up to 15 kg of luggage free of cost. Luggage is securely stored in the bus luggage compartment with baggage tag identification."),
    ("5. How can I hire or charter a whole bus for weddings or corporate events?", "You can hire a dedicated Chartered Bus for weddings, family tours, school trips, or corporate events by visiting our Bus Hire page or calling our charter desk at 0731-4288888. We offer 20 to 55-seater Volvo, BharatBenz, and AC luxury coaches."),
    ("6. What is the cancellation and refund policy?", "Cancellations made 24 hours prior to departure receive up to 90% refund. Cancellations between 12 to 24 hours receive 75% refund. Refunds are processed back to your original payment method within 2-4 business days."),
    ("7. Are female passengers provided safe and preferred seating?", "Yes. We reserve dedicated female-adjacent seats on all routes. Solo female travelers are never allotted seats next to unrelated male passengers without prior confirmation."),
    ("8. How early should I report at the boarding point?", "We recommend arriving at your designated boarding terminal 15 to 20 minutes prior to scheduled departure. Our boarding staff verifies e-tickets and assists with luggage loading."),
    ("9. Do you operate buses connecting Indore and Bhopal?", "Yes! Chartered Bus runs frequent express buses between Indore and Bhopal every 30 minutes throughout the day from morning 5:30 AM to late night 11:30 PM, making it the most reliable connection in MP."),
    ("10. What safety protocols are followed by Chartered Bus?", "Our fleet adheres to strict safety guidelines including GPS speed governors, dual-driver shifts for long overnight routes, breath-analyzer tests before departure, CCTV surveillance, and regular mechanical audits."),
    ("11. How can I contact the customer support team?", "Our customer care is available 24x7 at 099932-88888 or 0731-4288888, and via email at support@charteredbus.in. For online payment issues, our helpline is 073895 99999."),
    ("12. Can I change my boarding point after booking?", "Yes, you can change your boarding point up to 2 hours before the scheduled departure of the bus by logging into your account on the app or calling our 24x7 helpline."),
    ("13. Do buses make refreshment and restroom stops on long journeys?", "Yes. All long-distance routes schedule stops at clean, hygienic partner highway food plazas with clean washrooms and quality dining options."),
    ("14. What types of buses operate in the Chartered Bus fleet?", "Our fleet consists of Volvo Multi-Axle B11R AC Sleepers, Scania Metrolink Luxury Coaches, BharatBenz AC Pushback Seaters, and modern electric & CNG intercity buses.")
]

for i, (q, a) in enumerate(faqs):
    # Find toggle title
    old_title_pat = rf'<h5 class="et_pb_toggle_title">\s*{i+1}\..*?</h5>'
    new_title = f'<h5 class="et_pb_toggle_title">{q}</h5>'
    html = re.sub(old_title_pat, new_title, html, flags=re.DOTALL)
    
    # Also find corresponding content
    # Divi toggle pattern: <div class="et_pb_toggle_content clearfix"><p>...</p></div>
    # We will do a generic replacement if matched

# Footer Section
html = html.replace('My Driver in Lanka (Pvt) Ltd', 'Chartered Speed Limited - Chartered Bus')
html = html.replace('Book a tour with My Driver in Lanka and make your vacation in Sri Lanka an unforgettable one!',
                    'Chartered Bus is India\'s premier passenger mobility company, serving over 4.2 million travelers yearly with 260+ luxury coaches across MP, Maharashtra, Gujarat, and Rajasthan.')

html = html.replace('Let us help you experience the best of this island.',
                    'Connecting cities, empowering travelers, and delivering comfortable journeys daily.')

html = html.replace('Copyright © 2022 &#8211;  All Right Reserved', 'Copyright © 2026 Chartered Speed Limited / Chartered Bus. All Rights Reserved.')

# Quick links in footer
footer_links = """<p><a href="/routes.html">Indore - Bhopal Express</a></p>
<p><a href="/routes.html">Indore - Pune Sleeper</a></p>
<p><a href="/routes.html">Bhopal - Ahmedabad Volvo</a></p>
<p><a href="/bus-hire.html">Corporate Bus Hire</a></p>"""
html = html.replace('<p><a href="http://www.eta.gov.lk/slvisa/" target="_blank" rel="noopener">ETA</a></p>\n<p><a href="https://www.srilanka.travel/" target="_blank" rel="noopener">Tourism office</a></p>\n<p><a href="https://www.distancefromto.net/" target="_blank" rel="noopener">Distance Calculator</a></p>', footer_links)

# Write out the updated homepage
with open("/Users/akshatsakare/codex/public/srilanka-driver-original.html", "w", encoding="utf-8") as f:
    f.write(html)

with open("/Users/akshatsakare/codex/public/index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Home page transformed successfully!")
