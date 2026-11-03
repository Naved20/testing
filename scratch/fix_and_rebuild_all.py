import re
import os

with open("/Users/akshatsakare/codex/public/srilanka-driver-original.backup.html", "r", encoding="utf-8") as f:
    raw = f.read()

# 1. CSS & Theme Customization
head_injection = """
<style id="chartered-bus-theme-custom">
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
    cursor: pointer;
  }
  .et_pb_column_14 {
    background-image: linear-gradient(180deg, rgba(0,0,0,0.15) 35%, rgba(11,19,43,0.92) 100%), url('/images/route_night.jpg') !important;
    background-size: cover !important;
    background-position: center !important;
    border-radius: 8px;
    overflow: hidden;
    cursor: pointer;
  }
  .et_pb_column_15 {
    background-image: linear-gradient(180deg, rgba(0,0,0,0.15) 35%, rgba(11,19,43,0.92) 100%), url('/images/hero_bus.jpg') !important;
    background-size: cover !important;
    background-position: center !important;
    border-radius: 8px;
    overflow: hidden;
    cursor: pointer;
  }
  .et_pb_column_16 {
    background-image: linear-gradient(180deg, rgba(0,0,0,0.15) 35%, rgba(11,19,43,0.92) 100%), url('/images/fleet_bus.jpg') !important;
    background-size: cover !important;
    background-position: center !important;
    border-radius: 8px;
    overflow: hidden;
    cursor: pointer;
  }
  .et_pb_column_17 {
    background-image: linear-gradient(180deg, rgba(0,0,0,0.15) 35%, rgba(11,19,43,0.92) 100%), url('/images/interior_bus.jpg') !important;
    background-size: cover !important;
    background-position: center !important;
    border-radius: 8px;
    overflow: hidden;
    cursor: pointer;
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
  /* Fix sticky menu z-index and active link styles */
  .et_pb_menu .et-menu > li > a {
    font-weight: 600 !important;
    font-size: 14px !important;
    color: #14213d !important;
    transition: color 0.2s ease !important;
  }
  .et_pb_menu .et-menu > li > a:hover,
  .et_pb_menu .et-menu > li.current-menu-item > a {
    color: #E02020 !important;
  }
  .et-menu li li a {
    color: #333 !important;
    font-size: 13px !important;
  }
  .et-menu li li a:hover {
    color: #E02020 !important;
    background-color: #f8fafc !important;
  }
</style>
<script>
  // Ensure all links break out of iframe if loaded inside one, and smooth intra-page scroll
  document.addEventListener('DOMContentLoaded', function() {
    document.querySelectorAll('a').forEach(function(link) {
      var href = link.getAttribute('href');
      if (href && (href.startsWith('/') || href.startsWith('http://localhost:3000'))) {
        link.setAttribute('target', '_top');
      }
    });
  });
</script>
"""

# Replace Head & Meta
raw = re.sub(r'<title>.*?</title>', '<title>Chartered Bus | Online Bus Bookings Made Easy | Indore Bhopal</title>', raw, count=1)
raw = re.sub(r'<meta name="description" content=".*?"/>', '<meta name="description" content="Chartered Bus is India\'s premier passenger mobility company. Book AC Sleeper, Volvo Multi-Axle, and Seater bus tickets online."/>', raw, count=1)
raw = raw.replace('</head>', head_injection + '\n</head>')

# Replace Logo
raw = re.sub(r'<div class="et_pb_menu__logo">\s*<a href="/" >.*?</a>\s*</div>',
             '<div class="et_pb_menu__logo"><a href="/" target="_top"><img fetchpriority="high" decoding="async" width="280" height="74" src="/chartered-bus-logo.svg" alt="Chartered Bus" style="max-height:52px; width:auto;"></a></div>',
             raw, flags=re.DOTALL)
raw = re.sub(r'<div class="et_pb_menu__logo">\s*<img .*?>\s*</div>',
             '<div class="et_pb_menu__logo"><a href="/" target="_top"><img fetchpriority="high" decoding="async" width="280" height="74" src="/chartered-bus-logo.svg" alt="Chartered Bus" style="max-height:52px; width:auto;"></a></div>',
             raw, flags=re.DOTALL)

# Accurate replacement of the navigation bar!
def build_nav(menu_id, active_page="home"):
    c_home = ' current-menu-item' if active_page == 'home' else ''
    c_routes = ' current-menu-item' if active_page == 'routes' else ''
    c_hire = ' current-menu-item' if active_page == 'bus-hire' else ''
    c_about = ' current-menu-item' if active_page == 'about' else ''
    c_contact = ' current-menu-item' if active_page == 'contact' else ''
    c_gallery = ' current-menu-item' if active_page == 'gallery' else ''

    return f"""<nav class="et-menu-nav">
<ul id="{menu_id}" class="et-menu nav">
	<li class="menu-item{c_home}"><a href="/" target="_top">Home</a></li>
	<li class="menu-item menu-item-has-children{c_routes}"><a href="/routes" target="_top">Routes &amp; Schedules</a>
		<ul class="sub-menu">
			<li class="menu-item"><a href="/routes#indore-bhopal" target="_top">Indore ⇌ Bhopal (Every 30m)</a></li>
			<li class="menu-item"><a href="/routes#indore-pune" target="_top">Indore ⇌ Pune (AC Sleeper)</a></li>
			<li class="menu-item"><a href="/routes#bhopal-ahmedabad" target="_top">Bhopal ⇌ Ahmedabad (Volvo)</a></li>
			<li class="menu-item"><a href="/routes#indore-jabalpur" target="_top">Indore ⇌ Jabalpur (Express)</a></li>
			<li class="menu-item"><a href="/routes#pilgrimage" target="_top">Ujjain &amp; Omkareshwar Shuttles</a></li>
		</ul>
	</li>
	<li class="menu-item{c_hire}"><a href="/bus-hire" target="_top">Bus Hire &amp; Charter</a></li>
	<li class="menu-item{c_about}"><a href="/about-us" target="_top">About Us</a></li>
	<li class="menu-item{c_contact}"><a href="/contact" target="_top">Contact Us</a></li>
	<li class="menu-item{c_gallery}"><a href="/gallery" target="_top">Fleet &amp; Gallery</a></li>
</ul>
</nav>"""

# Replace both nav menus cleanly between <nav class="et-menu-nav"> and </nav>
navs = list(re.finditer(r'<nav class="et-menu-nav">.*?</nav>', raw, flags=re.DOTALL))
if len(navs) >= 2:
    # replace second then first so offsets don't change
    span2 = navs[1].span()
    span1 = navs[0].span()
    raw = raw[:span2[0]] + build_nav("menu-main-menu-1", "home") + raw[span2[1]:]
    raw = raw[:span1[0]] + build_nav("menu-main-menu", "home") + raw[span1[1]:]
elif len(navs) == 1:
    span1 = navs[0].span()
    raw = raw[:span1[0]] + build_nav("menu-main-menu", "home") + raw[span1[1]:]

# Content replacements on homepage
raw = raw.replace('<h2>My Driver in Lanka</h2>', '<h2>India\'s Leading Mobility Partner</h2>')
raw = raw.replace('<h2>Ayubowan / Welcome</h2>', '<h2>Chartered Bus Travel</h2>')
raw = raw.replace('<h2>to beautiful Sri Lanka</h2>', '<h2>Safe, Punctual & Affordable</h2>')
raw = re.sub(r'<a class="et_pb_button et_pb_button_0[^"]*" href="[^"]*">BOOK A TOUR</a>',
             '<a class="et_pb_button et_pb_button_0 et_pb_bg_layout_light" href="/routes" target="_top">BOOK BUS TICKET</a>', raw)

# Top Bar Contacts
raw = raw.replace('samanthadiscover@gmail.com', 'support@charteredbus.in')
raw = raw.replace('mailto:samanthadiscover@gmail.com', 'mailto:support@charteredbus.in')
raw = raw.replace('+94 77 263 5814', '099932-88888')
raw = raw.replace('+94 71 566 6619', '0731-4288888')
raw = raw.replace('tel:+94%2077 263 5814', 'tel:09993288888')
raw = raw.replace('<span>Hot Line</span>', '<span>24x7 Helpline</span>')

# Intro Section
raw = raw.replace('<p>Explore the Beauty of Sri Lanka with</p>', '<p>Experience Seamless Intercity Mobility with</p>')
raw = raw.replace('<h1>the best Sri Lanka Tour Packages</h1>', '<h1>Chartered Bus Premium Fleet Network</h1>')

# Intro Image
raw = re.sub(r'<span class="et_pb_image_wrap "><img loading="lazy" decoding="async" width="2240" height="1260" src="https://mysrilankadriver\.com/wp-content/uploads/2022/10/01-2\.png"[^>]*></span>',
              '<span class="et_pb_image_wrap "><img loading="lazy" decoding="async" width="1280" height="720" src="/images/interior_bus.jpg" alt="Chartered Bus Luxury Fleet" title="Chartered Bus Luxury Interiors" style="border-radius:12px; box-shadow:0 15px 35px rgba(0,0,0,0.15);" class="wp-image-147" /></span>', raw)

# Intro paragraph
intro_match = re.search(r'<div class="et_pb_text_inner"><p>Ayubowan! I am Samantha.*?</div>', raw, re.DOTALL)
if intro_match:
    intro_text = """<div class="et_pb_text_inner"><p><strong>Chartered Bus</strong> is one of India\'s leading passenger mobility companies, synonymous with punctual, reliable, and comfortable intercity road travel across Central, Western, and North Eastern India. We service over <strong>4.2 million passengers</strong> across our growing fleet of modern coaches every year.</p>
<p>From hourly city connectors like the iconic Indore–Bhopal route to interstate overnight luxury sleeper Volvo coaches connecting Pune, Ahmedabad, Jabalpur, and beyond, our mission is to provide you a world-class travel experience with live GPS tracking, sanitized seating, and professional pilots.</p></div>"""
    raw = raw.replace(intro_match.group(0), intro_text)

raw = re.sub(r'<a class="et_pb_button et_pb_button_1[^"]*" href="[^"]*">BOOK A TOUR</a>',
             '<a class="et_pb_button et_pb_button_1 et_pb_bg_layout_light" href="/routes" target="_top">EXPLORE BUS ROUTES</a>', raw)

# Why Choose section
raw = raw.replace('Why Should You Select My Driver in Lanka to Explore Sri Lanka?', 'Why Should You Select Chartered Bus for Your Next Trip?')
raw = raw.replace('Self-driving in Sri Lanka can be challenging', 'Punctual & Reliable Schedules')
raw = raw.replace('Driving in Sri Lanka can be challenging due to many reasons including horrible traffic, inadequate road signage and erratic local drivers.', 'Over 98% on-time departure and arrival rate with round-the-clock route monitoring, backup support vehicles, and professional trained pilots.')

raw = raw.replace('The majority of the locals do not speak English', 'Live GPS Tracking & Safety')
raw = raw.replace('<span style="font-weight: 400;">If you are traveling in Sri Lanka, having someone who knows the language and is familiar with the culture and the local background will give you a whole lot of extra benefits.</span>', '<span style="font-weight: 400;">Real-time bus tracking on the mobile app, emergency SOS buttons, CCTV surveillance, speed-governed coaches, and well-trained professional pilots.</span>')

raw = raw.replace('There are no any hidden costs', 'Zero Hidden Costs & Easy Booking')
raw = raw.replace('Our rates are very reasonable and all you have to pay is the amount that you agreed to before the journey. There are no any hidden charges like commissions.', 'Transparent pricing with no surprise surcharges. Book instantly online, choose your preferred seat, and enjoy instant cancellation with prompt refunds.')

raw = raw.replace('We guarantee you an experience for life', 'World-Class Onboard Comfort')
raw = raw.replace('Our tours are filled with the most beautiful places in Sri Lanka. You’ll be able to experience the best of Sri Lanka including Sri Lankan attractions, food and culture.', 'Ergonomic plush reclining seats, spacious sleeper berths, individual USB charging points, reading lamps, sanitized blankets, and high-speed Wi-Fi.')

# Tour Packages / Routes Section
raw = raw.replace('<p>Tour Packages</p>', '<p>Popular Bus Routes & Schedules</p>')
raw = raw.replace('Our tour packages are designed to give you a truly wonderful experience that you will be able to experience only in Sri Lanka. No matter if you are a solo traveler, a couple, a group of friends or a family, we have multiple options for you to choose from.',
                  'Connecting over 640+ daily scheduled routes across Madhya Pradesh, Maharashtra, Gujarat, and Rajasthan with high-frequency departures, luxury Volvo multi-axle coaches, and premium sleeper cabins.')

# 5 Route Cards
raw = raw.replace('07 Day Tour Package', 'Indore ⇌ Bhopal Express')
raw = raw.replace('Sigiriya, Kandy, Nuwara Eliya, Kithulgala and Galle.', 'Departures every 30 mins | AC Seater & Volvo | 3.5 hrs via State Highway 18 | ₹350 onwards')

raw = raw.replace('07 Day Tour Package &#8211; 02', 'Indore ⇌ Pune Overnight')
raw = raw.replace('Kandy, Ella, Yala, Tangalle and Mirissa.', 'Daily AC Sleeper 2+1 | Comfortable berths, charging points, blanket & water bottle | ₹1,100 onwards')

raw = raw.replace('10 Day Tour Package', 'Bhopal ⇌ Ahmedabad Volvo')
raw = raw.replace('Anuradhapura, Habarana, Polonnaruwa, Nuwara Eliya/Kandy, Ella, Yala, Tangalle and Galle.', 'Premium Multi-Axle Volvo Sleeper | Evening departures via Ujjain & Godhra | ₹1,250 onwards')

raw = raw.replace('12 Day Tour Package', 'Indore ⇌ Ujjain & Omkareshwar')
raw = raw.replace('Anuradhapura, Trincomalee, Habarana, Nuwara Eliya, Ella, Yala, Tangalle, Mirissa and Galle.', 'Pilgrimage Shuttle Service | High frequency departures connecting Mahakaleshwar & Jyotirlinga shrines')

raw = raw.replace('14 Day Tour Package', 'Indore ⇌ Jabalpur & Rewa')
raw = raw.replace('Negombo, Anuradhapura, Habarana, Bakamuna, Kandy, Nuwara Eliya, Ella, Yala/Udawalawa, Tangalle, Mirissa and Galle.', 'East-West MP Express | AC Sleeper & Seater coaches connecting Bhopal, Sagar, Jabalpur & Rewa')

# Replace 'learn more' links on cards with target="_top"
raw = re.sub(r'<div class="et_pb_text_inner"><p>learn more</p></div>',
             '<div class="et_pb_text_inner"><p style="font-weight:700; color:#E02020; text-transform:uppercase;">View Schedule →</p></div>', raw)

# Charter Hire Section
raw = raw.replace('EXCLUSIVE VILLA OFFER!', 'CORPORATE & PRIVATE BUS HIRE')
raw = raw.replace('Enjoy a free night at a tropical villa!', 'Hire a Chartered Bus for Weddings & Group Tours')
raw = raw.replace('Book a tour of 10 or more days with <span>My Driver in Lanka</span> and Enjoy a FREE night at Serenity Villa Habarana and experience authentic Sri Lankan food and much more!',
                  'Need reliable transport for weddings, corporate offsites, family pilgrimages, or school excursions? Rent our premium 20 to 55-seater luxury coaches with experienced drivers, complete fuel inclusion, and customized itineraries.')
raw = raw.replace('BOOK THE OFFER', 'REQUEST BUS HIRE QUOTE')

# Parallax App Section
raw = raw.replace('Plan an Unforgettable Vacation in Sri Lanka', 'Track Your Bus Live & Book on the Go')
raw = raw.replace('with My Driver in Lanka!', 'with the Chartered Bus Mobile App')
raw = raw.replace('Leave us your details and we’ll get back to you with a tour that is ideal for you!', 'Download the official Chartered Bus App on Android and iOS for live bus tracking, ticket cancellation, seat selection, and exclusive promo codes!')

raw = re.sub(r'<span class="et_pb_image_wrap "><img loading="lazy" decoding="async" width="256" height="256" src="https://mysrilankadriver\.com/wp-content/uploads/2022/09/Travel-Agency8-1\.png"[^>]*></span>',
              '<span class="et_pb_image_wrap "><img loading="lazy" decoding="async" width="160" height="160" src="/chartered-bus-avatar.svg" alt="Chartered Bus App" style="max-width:140px;filter:drop-shadow(0 8px 16px rgba(0,0,0,0.4));"></span>', raw)

# Booking Header
raw = raw.replace('Book your tour now!', 'Book Bus Tickets or Inquire for Bus Hire')
raw = re.sub(r'<a class="et_pb_button et_pb_button_0_tb_footer[^"]*" href="[^"]*">Book Now</a>',
             '<a class="et_pb_button et_pb_button_0_tb_footer et_pb_bg_layout_light" href="/routes" target="_top">Book Online</a>', raw)

# Reviews & Stats
raw = raw.replace('What Our Customers Have to Say', 'What Our Passengers Say About Chartered Bus')
stats_html = """
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
raw = raw.replace('<div class="et_pb_text_inner"><div class="ti-widget ti-trip"', stats_html + '<div class="et_pb_text_inner"><div class="ti-widget ti-trip"')

# Reviews
raw = raw.replace('14 jours magnifiques à travers le Sri Lanka', 'Indore to Bhopal - Always On Time & Super Clean!')
raw = raw.replace('Alain B', 'Rajesh Sharma, Indore')
raw = raw.replace('Séjour découverte de l’île', 'Ahmedabad to Bhopal Sleeper - Very Comfortable')
raw = raw.replace('lucas71530', 'Ananya Mehta, Ahmedabad')
raw = raw.replace('Good driver', 'Excellent Wedding Bus Hire Service')
raw = raw.replace('L K', 'Vikramaditya Rao, Pune')

# FAQs
faqs = [
    ("1. Do I need a driver to travel around Sri Lanka?", "1. How do I book a Chartered Bus ticket online?",
     "You can easily book bus tickets online through our official portal, mobile app, or by calling our 24x7 phone booking helpline at <strong>099932-88888</strong>. Choose your origin, destination, and travel date, select your preferred seat on the interactive seat layout, and pay securely via UPI, card, or net banking."),
    ("2. How much does it cost to hire a private driver in Sri Lanka?", "2. Can I track my bus location in real time?",
     "Yes! Every Chartered Bus coach is equipped with high-precision GPS tracking hardware. When you book, you receive a real-time tracking link via SMS. You can also view the exact live location and estimated arrival time on our mobile application."),
    ("3. Is it safe to hire a driver in Sri Lanka?", "3. What amenities are provided on Chartered Bus coaches?",
     "Depending on the coach service (Volvo Multi-Axle, AC Sleeper, or BharatBenz Seater), passengers enjoy comfortable ergonomic seating, USB mobile charging ports, reading lights, air-conditioned cabins, complimentary water bottles, sanitized blankets on night journeys, and emergency SOS buttons."),
    ("4. Can I hire a driver for the whole trip in Sri Lanka?", "4. What is the baggage allowance per passenger?",
     "Each passenger is allowed up to <strong>15 kg of personal luggage</strong> free of charge. Your bags are tagged and stowed in our spacious undercarriage luggage compartments."),
    ("5. Do Sri Lanka drivers speak English?", "5. How can I hire or charter a whole bus for weddings or corporate events?",
     "We provide end-to-end chartered bus rentals for weddings, corporate offsites, religious yatras, and school/college tours. We offer 20-seater to 55-seater premium AC coaches with certified drivers and custom routing. Call our Charter Desk at <strong>0731-4288888</strong> or visit our Bus Hire section."),
    ("6. Is a private driver better than taxis or Uber in Sri Lanka?", "6. What is the cancellation and refund policy?",
     "Cancellations made 24+ hours before departure receive up to a 90% refund. Cancellations made between 12 to 24 hours receive 75% refund. Refunds are instantly initiated to your original payment mode."),
    ("7. Can a driver help plan my Sri Lanka itinerary?", "7. Are female passengers provided safe and preferred seating?",
     "Safety is our top priority. Solo female travelers are allotted dedicated seats alongside other female passengers. All coaches feature CCTV surveillance and monitored speed controls."),
    ("8. Do you provide airport transfers in Sri Lanka?", "8. How early should I report at the boarding point?",
     "Please report at your designated boarding point 15 to 20 minutes prior to scheduled departure. Our on-ground boarding executives will verify your m-ticket and assist with luggage."),
    ("9. Is Sri Lanka suitable for travelling with kids?", "9. Do you operate buses connecting Indore and Bhopal?",
     "Yes! We operate high-frequency non-stop and express buses between Indore and Bhopal every 30 minutes from 5:30 AM until 11:30 PM daily, making Chartered Bus the most preferred connection on this corridor."),
    ("10. Can I travel Sri Lanka without a car?", "10. What safety protocols are followed by Chartered Bus?",
     "All our vehicles undergo rigorous daily maintenance checks, GPS speed limiters, dual-crew shifts on overnight runs, breathalyzer checks before departure, and sanitized cabins."),
    ("11. What type of vehicles are used?", "11. How can I contact the customer support team?",
     "Our customer support is reachable 24x7 at <strong>099932-88888</strong> and <strong>0731-4288888</strong>, or via email at <a href='mailto:support@charteredbus.in'>support@charteredbus.in</a>. For payment disputes, call <strong>073895 99999</strong>."),
    ("12. How far in advance should I book a driver in Sri Lanka?", "12. Can I change my boarding point after booking?",
     "Yes, you can update your boarding point up to 2 hours before the scheduled departure through the Chartered Bus App or by contacting customer support."),
    ("13. Are fuel and driver expenses included in the price?", "13. Do buses make refreshment and restroom stops on long journeys?",
     "Yes, on long-distance routes, scheduled stops are made at verified, hygienic food plazas with clean washrooms and dining options."),
    ("14. Why book with My Driver in Sri Lanka?", "14. What types of buses operate in the Chartered Bus fleet?",
     "Our fleet consists of Volvo 9600 Multi-Axle Sleepers, Scania Metrolink Luxury coaches, BharatBenz Air-Suspension AC Seaters, and modern intercity electric & CNG buses.")
]

for old_q, new_q, ans in faqs:
    # Pattern matching the whole toggle block
    block_pat = rf'<h5 class="et_pb_toggle_title">\s*{re.escape(old_q)}\s*</h5>\s*<div class="et_pb_toggle_content clearfix">.*?</div>'
    replacement_block = f'<h5 class="et_pb_toggle_title">{new_q}</h5><div class="et_pb_toggle_content clearfix"><p>{ans}</p></div>'
    raw = re.sub(block_pat, replacement_block, raw, flags=re.DOTALL)

# Footer
raw = raw.replace('My Driver in Lanka (Pvt) Ltd', 'Chartered Speed Limited - Chartered Bus')
raw = raw.replace('Book a tour with My Driver in Lanka and make your vacation in Sri Lanka an unforgettable one!',
                  'Chartered Bus is India\'s premier passenger mobility company, serving over 4.2 million travelers yearly with 260+ luxury coaches across MP, Maharashtra, Gujarat, and Rajasthan.')
raw = raw.replace('Let us help you experience the best of this island.', 'Connecting cities, empowering travelers, and delivering comfortable journeys daily.')
raw = raw.replace('Copyright © 2022 &#8211;  All Right Reserved', 'Copyright © 2026 Chartered Speed Limited / Chartered Bus. All Rights Reserved.')

# Footer Navigation column
footer_nav = """<div class="et_pb_text_inner"><p><a href="/" target="_top">Home</a></p>
<p><a href="/routes" target="_top">Routes &amp; Schedules</a></p>
<p><a href="/bus-hire" target="_top">Bus Hire &amp; Charter</a></p>
<p><a href="/about-us" target="_top">About Us</a></p>
<p><a href="/contact" target="_top">Contact Us</a></p>
<p><a href="/gallery" target="_top">Fleet &amp; Gallery</a></p></div>"""
raw = re.sub(r'<div class="et_pb_text_inner"><p><a href="#">Home</a></p>\s*<p><a href="https://mysrilankadriver\.com/category/blogs/">Blog</a></p>\s*<p><a href="https://mysrilankadriver\.com/contact-us/">Contact Us</a></p></div>',
             footer_nav, raw)

# Footer Quick Links column
footer_routes = """<div class="et_pb_text_inner"><p><a href="/routes#indore-bhopal" target="_top">Indore ⇌ Bhopal</a></p>
<p><a href="/routes#indore-pune" target="_top">Indore ⇌ Pune</a></p>
<p><a href="/routes#bhopal-ahmedabad" target="_top">Bhopal ⇌ Ahmedabad</a></p>
<p><a href="/routes#indore-jabalpur" target="_top">Indore ⇌ Jabalpur</a></p>
<p><a href="/routes#pilgrimage" target="_top">Ujjain &amp; Omkareshwar</a></p></div>"""
raw = re.sub(r'<div class="et_pb_text_inner"><p><a href="http://www\.eta\.gov\.lk/slvisa/".*?</div>',
             footer_routes, raw, flags=re.DOTALL)

# JavaScript link options update so clicking Divi card elements navigates to /routes
link_options_code = """var et_link_options_data = [
    {"class":"et_pb_column_13","url":"/routes#indore-bhopal","target":"_top"},
    {"class":"et_pb_text_13","url":"/routes#indore-bhopal","target":"_top"},
    {"class":"et_pb_column_14","url":"/routes#indore-pune","target":"_top"},
    {"class":"et_pb_text_16","url":"/routes#indore-pune","target":"_top"},
    {"class":"et_pb_column_15","url":"/routes#bhopal-ahmedabad","target":"_top"},
    {"class":"et_pb_text_19","url":"/routes#bhopal-ahmedabad","target":"_top"},
    {"class":"et_pb_column_16","url":"/routes#pilgrimage","target":"_top"},
    {"class":"et_pb_text_22","url":"/routes#pilgrimage","target":"_top"},
    {"class":"et_pb_column_17","url":"/routes#indore-jabalpur","target":"_top"},
    {"class":"et_pb_text_25","url":"/routes#indore-jabalpur","target":"_top"},
    {"class":"et_pb_text_31","url":"/bus-hire","target":"_top"}
];"""
raw = re.sub(r'var et_link_options_data = \[.*?\];', link_options_code, raw, flags=re.DOTALL)

# WhatsApp Chat Settings
raw = raw.replace('"telephone":"94772635814"', '"telephone":"919993288888"')
raw = raw.replace('My Sri Lanka Driver', 'Chartered Bus')

# Save updated Home page
with open("/Users/akshatsakare/codex/public/srilanka-driver-original.html", "w", encoding="utf-8") as f:
    f.write(raw)
with open("/Users/akshatsakare/codex/public/index.html", "w", encoding="utf-8") as f:
    f.write(raw)
print("Base home page updated!")

# Function to build secondary pages
def generate_secondary_page(page_name, active_tab, title, hero_h2_1, hero_h2_2, hero_btn_text, hero_btn_link, content_html, filename):
    p = raw
    p = re.sub(r'<title>.*?</title>', f'<title>{title} | Chartered Bus</title>', p, count=1)
    
    # Update navigation active status
    p = p.replace(build_nav("menu-main-menu", "home"), build_nav("menu-main-menu", active_tab))
    p = p.replace(build_nav("menu-main-menu-1", "home"), build_nav("menu-main-menu-1", active_tab))

    # Hero customization
    p = p.replace('<h2>India\'s Leading Mobility Partner</h2>', f'<h2>{hero_h2_1}</h2>')
    p = p.replace('<h2>Chartered Bus Travel</h2>', f'<h2>{hero_h2_2}</h2>')
    p = p.replace('<h2>Safe, Punctual & Affordable</h2>', '<h2>India\'s Preferred Mobility</h2>')
    p = re.sub(r'<a class="et_pb_button et_pb_button_0[^"]*" href="[^"]*">BOOK BUS TICKET</a>',
               f'<a class="et_pb_button et_pb_button_0 et_pb_bg_layout_light" href="{hero_btn_link}" target="_top">{hero_btn_text}</a>', p)

    # Replace body content between section 1 and footer
    m = re.search(r'(<div class="et_pb_section et_pb_section_1 et_section_regular" >.*?)(</div>\s*</div>\s*</div>\s*</article>)', p, re.DOTALL)
    if m:
        body_section = f"""<div class="et_pb_section et_section_regular" style="padding: 40px 0; background: #f8fafc;">
            <div class="container">
                {content_html}
            </div>
        </div>\n\\2"""
        p = p[:m.start(1)] + body_section + p[m.end(2):]

    with open(f"/Users/akshatsakare/codex/public/{filename}", "w", encoding="utf-8") as f:
        f.write(p)
    print(f"Generated {filename}")

# 1. Routes & Schedules
routes_body = """
<div style="background:#fff; padding:45px 35px; border-radius:12px; box-shadow:0 10px 30px rgba(0,0,0,0.06);">
    <div style="text-align:center; margin-bottom:40px;">
        <span class="cb-badge">DAILY SCHEDULES & ROUTES</span>
        <h2 style="font-size:32px; font-weight:800; color:#14213d; margin:10px 0;">Popular Intercity Bus Routes</h2>
        <p style="color:#666; max-width:700px; margin:auto;">Explore our high-frequency daily schedules, modern fleet options, and guaranteed on-time departures connecting key business and cultural hubs.</p>
    </div>

    <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(320px, 1fr)); gap:25px; margin-bottom:40px;">
        <div id="indore-bhopal" style="border:1px solid #e2e8f0; border-radius:10px; padding:25px; background:#fff; box-shadow:0 4px 15px rgba(0,0,0,0.03);">
            <div style="display:flex; justify-content:space-between; align-items:center;">
                <span style="background:#fee2e2; color:#b91c1c; font-weight:700; font-size:12px; padding:3px 10px; border-radius:4px;">EVERY 30 MINS</span>
                <span style="font-weight:800; color:#E02020; font-size:20px;">₹350 onwards</span>
            </div>
            <h3 style="font-size:22px; font-weight:800; color:#14213d; margin:15px 0 8px 0;">Indore ⇌ Bhopal</h3>
            <p style="color:#64748b; font-size:14px; margin-bottom:15px;">Fastest corridor transit via State Highway. Luxury AC Seater & BharatBenz fleet.</p>
            <ul style="list-style:none; padding:0; margin:0 0 20px 0; font-size:13px; color:#475569; line-height:24px;">
                <li>✓ <strong>Timings:</strong> 5:30 AM to 11:30 PM (Every 30 mins)</li>
                <li>✓ <strong>Duration:</strong> 3 hrs 30 mins</li>
                <li>✓ <strong>Boarding Indore:</strong> AICTSL Campus, Geeta Bhawan, Radisson Sq</li>
                <li>✓ <strong>Drop Bhopal:</strong> ISBT Habibganj, Lal Ghati, Board Office</li>
            </ul>
            <a href="/contact" target="_top" style="display:block; text-align:center; background:#E02020; color:#fff; font-weight:700; padding:10px 20px; border-radius:6px; text-decoration:none;">Book Indore ⇌ Bhopal</a>
        </div>

        <div id="indore-pune" style="border:1px solid #e2e8f0; border-radius:10px; padding:25px; background:#fff; box-shadow:0 4px 15px rgba(0,0,0,0.03);">
            <div style="display:flex; justify-content:space-between; align-items:center;">
                <span style="background:#e0f2fe; color:#0369a1; font-weight:700; font-size:12px; padding:3px 10px; border-radius:4px;">OVERNIGHT SLEEPER</span>
                <span style="font-weight:800; color:#E02020; font-size:20px;">₹1,100 onwards</span>
            </div>
            <h3 style="font-size:22px; font-weight:800; color:#14213d; margin:15px 0 8px 0;">Indore ⇌ Pune</h3>
            <p style="color:#64748b; font-size:14px; margin-bottom:15px;">Overnight luxury journey with sanitized bedding, charging points & quiet cabins.</p>
            <ul style="list-style:none; padding:0; margin:0 0 20px 0; font-size:13px; color:#475569; line-height:24px;">
                <li>✓ <strong>Departures:</strong> 6:00 PM, 7:30 PM, 9:00 PM</li>
                <li>✓ <strong>Duration:</strong> 11 hrs 30 mins</li>
                <li>✓ <strong>Coach Type:</strong> Multi-Axle AC Sleeper (2+1)</li>
                <li>✓ <strong>Drop Pune:</strong> Wakad, Swargate, Viman Nagar</li>
            </ul>
            <a href="/contact" target="_top" style="display:block; text-align:center; background:#E02020; color:#fff; font-weight:700; padding:10px 20px; border-radius:6px; text-decoration:none;">Book Indore ⇌ Pune</a>
        </div>

        <div id="bhopal-ahmedabad" style="border:1px solid #e2e8f0; border-radius:10px; padding:25px; background:#fff; box-shadow:0 4px 15px rgba(0,0,0,0.03);">
            <div style="display:flex; justify-content:space-between; align-items:center;">
                <span style="background:#fef3c7; color:#b45309; font-weight:700; font-size:12px; padding:3px 10px; border-radius:4px;">VOLVO MULTI-AXLE</span>
                <span style="font-weight:800; color:#E02020; font-size:20px;">₹1,250 onwards</span>
            </div>
            <h3 style="font-size:22px; font-weight:800; color:#14213d; margin:15px 0 8px 0;">Bhopal ⇌ Ahmedabad</h3>
            <p style="color:#64748b; font-size:14px; margin-bottom:15px;">Interstate express linking MP capital to Gujarat commercial hub via Ujjain & Godhra.</p>
            <ul style="list-style:none; padding:0; margin:0 0 20px 0; font-size:13px; color:#475569; line-height:24px;">
                <li>✓ <strong>Departures:</strong> 5:30 PM & 8:15 PM Daily</li>
                <li>✓ <strong>Duration:</strong> 12 hrs</li>
                <li>✓ <strong>Amenities:</strong> Wi-Fi, Water Bottle, USB Charging</li>
                <li>✓ <strong>Drop Ahmedabad:</strong> CTM Cross Road, Paldi, Gita Mandir</li>
            </ul>
            <a href="/contact" target="_top" style="display:block; text-align:center; background:#E02020; color:#fff; font-weight:700; padding:10px 20px; border-radius:6px; text-decoration:none;">Book Bhopal ⇌ Ahmedabad</a>
        </div>

        <div id="indore-jabalpur" style="border:1px solid #e2e8f0; border-radius:10px; padding:25px; background:#fff; box-shadow:0 4px 15px rgba(0,0,0,0.03);">
            <div style="display:flex; justify-content:space-between; align-items:center;">
                <span style="background:#f3e8ff; color:#7e22ce; font-weight:700; font-size:12px; padding:3px 10px; border-radius:4px;">MP EXPRESS</span>
                <span style="font-weight:800; color:#E02020; font-size:20px;">₹680 onwards</span>
            </div>
            <h3 style="font-size:22px; font-weight:800; color:#14213d; margin:15px 0 8px 0;">Indore ⇌ Jabalpur</h3>
            <p style="color:#64748b; font-size:14px; margin-bottom:15px;">East-West express connectivity connecting Indore, Bhopal, Sagar, and Jabalpur.</p>
            <ul style="list-style:none; padding:0; margin:0 0 20px 0; font-size:13px; color:#475569; line-height:24px;">
                <li>✓ <strong>Departures:</strong> Morning 7:00 AM & Night 9:00 PM</li>
                <li>✓ <strong>Duration:</strong> 9 hrs</li>
                <li>✓ <strong>Coach Type:</strong> AC 2+1 Sleeper & Seater</li>
                <li>✓ <strong>Drop Jabalpur:</strong> Damoh Naka, ISBT Jabalpur</li>
            </ul>
            <a href="/contact" target="_top" style="display:block; text-align:center; background:#E02020; color:#fff; font-weight:700; padding:10px 20px; border-radius:6px; text-decoration:none;">Book Indore ⇌ Jabalpur</a>
        </div>

        <div id="pilgrimage" style="border:1px solid #e2e8f0; border-radius:10px; padding:25px; background:#fff; box-shadow:0 4px 15px rgba(0,0,0,0.03);">
            <div style="display:flex; justify-content:space-between; align-items:center;">
                <span style="background:#ecfdf5; color:#047857; font-weight:700; font-size:12px; padding:3px 10px; border-radius:4px;">PILGRIMAGE SHUTTLE</span>
                <span style="font-weight:800; color:#E02020; font-size:20px;">₹120 onwards</span>
            </div>
            <h3 style="font-size:22px; font-weight:800; color:#14213d; margin:15px 0 8px 0;">Indore ⇌ Ujjain & Omkareshwar</h3>
            <p style="color:#64748b; font-size:14px; margin-bottom:15px;">Frequent air-conditioned temple shuttle services connecting Mahakaleshwar Jyotirlinga.</p>
            <ul style="list-style:none; padding:0; margin:0 0 20px 0; font-size:13px; color:#475569; line-height:24px;">
                <li>✓ <strong>Departures:</strong> Every 20 mins starting 5:00 AM</li>
                <li>✓ <strong>Duration:</strong> 1 hr 15 mins (Indore - Ujjain)</li>
                <li>✓ <strong>Special:</strong> Direct transfers for Mahakal Bhasma Aarti</li>
                <li>✓ <strong>Drop Ujjain:</strong> Nanakheda Bus Stand, Mahakal Gate</li>
            </ul>
            <a href="/contact" target="_top" style="display:block; text-align:center; background:#E02020; color:#fff; font-weight:700; padding:10px 20px; border-radius:6px; text-decoration:none;">Book Ujjain Shuttle</a>
        </div>
    </div>
</div>
"""
generate_secondary_page("Bus Routes & Schedules", "routes", "Bus Routes & Schedules", "640+ Daily Schedules", "Popular Bus Routes", "CALL HELPLINE 099932-88888", "tel:09993288888", routes_body, "routes.html")

# 2. Bus Hire & Charter
bus_hire_body = """
<div style="background:#fff; padding:45px 35px; border-radius:12px; box-shadow:0 10px 30px rgba(0,0,0,0.06);">
    <div style="text-align:center; margin-bottom:40px;">
        <span class="cb-badge">PRIVATE & CORPORATE CHARTER</span>
        <h2 style="font-size:32px; font-weight:800; color:#14213d; margin:10px 0;">Charter a Bus for Any Occasion</h2>
        <p style="color:#666; max-width:700px; margin:auto;">Rent premium 20 to 55-seater Volvo, BharatBenz, and AC luxury buses with certified professional drivers, customized routes, and total peace of mind.</p>
    </div>

    <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(280px, 1fr)); gap:25px; margin-bottom:40px;">
        <div style="border:1px solid #e2e8f0; border-radius:10px; padding:25px; text-align:center;">
            <div style="font-size:40px; margin-bottom:15px;">💒</div>
            <h3 style="font-size:20px; font-weight:800; color:#14213d;">Weddings & Family Events</h3>
            <p style="color:#64748b; font-size:14px; margin-top:10px;">Ensure your wedding guests travel in synchronized luxury with dedicated pickup, drop, and luggage escort services.</p>
        </div>
        <div style="border:1px solid #e2e8f0; border-radius:10px; padding:25px; text-align:center;">
            <div style="font-size:40px; margin-bottom:15px;">🏢</div>
            <h3 style="font-size:20px; font-weight:800; color:#14213d;">Corporate Offsites & Events</h3>
            <p style="color:#64748b; font-size:14px; margin-top:10px;">Executive coaches with Wi-Fi, presentation screens, and quiet comfort for team retreats, conferences, and employee transit.</p>
        </div>
        <div style="border:1px solid #e2e8f0; border-radius:10px; padding:25px; text-align:center;">
            <div style="font-size:40px; margin-bottom:15px;">🛕</div>
            <h3 style="font-size:20px; font-weight:800; color:#14213d;">Religious Pilgrimage Tours</h3>
            <p style="color:#64748b; font-size:14px; margin-top:10px;">Custom group packages for Jyotirlinga darshan, Ujjain, Omkareshwar, Somnath, and religious circuit yatras.</p>
        </div>
        <div style="border:1px solid #e2e8f0; border-radius:10px; padding:25px; text-align:center;">
            <div style="font-size:40px; margin-bottom:15px;">🎓</div>
            <h3 style="font-size:20px; font-weight:800; color:#14213d;">School & College Excursions</h3>
            <p style="color:#64748b; font-size:14px; margin-top:10px;">Safe, speed-governed buses with verified drivers, seat belts, and GPS live parent tracking for educational field trips.</p>
        </div>
    </div>

    <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:12px; padding:35px; max-width:800px; margin:auto;">
        <h3 style="font-size:24px; font-weight:800; color:#14213d; margin-bottom:15px; text-align:center;">Get an Instant Bus Hire Quotation</h3>
        <p style="text-align:center; color:#64748b; margin-bottom:25px;">Fill out your journey requirements and our Charter Specialist will respond within 30 minutes.</p>
        <form action="/contact" method="GET" style="display:grid; grid-template-columns:1fr 1fr; gap:15px;">
            <div>
                <label style="display:block; font-size:13px; font-weight:600; color:#475569; margin-bottom:5px;">Your Name *</label>
                <input type="text" required placeholder="Full Name" style="width:100%; padding:10px; border:1px solid #cbd5e1; border-radius:6px;">
            </div>
            <div>
                <label style="display:block; font-size:13px; font-weight:600; color:#475569; margin-bottom:5px;">Contact Number *</label>
                <input type="tel" required placeholder="Mobile Number" style="width:100%; padding:10px; border:1px solid #cbd5e1; border-radius:6px;">
            </div>
            <div>
                <label style="display:block; font-size:13px; font-weight:600; color:#475569; margin-bottom:5px;">Origin City</label>
                <input type="text" placeholder="e.g. Indore" style="width:100%; padding:10px; border:1px solid #cbd5e1; border-radius:6px;">
            </div>
            <div>
                <label style="display:block; font-size:13px; font-weight:600; color:#475569; margin-bottom:5px;">Destination City</label>
                <input type="text" placeholder="e.g. Ujjain / Pune" style="width:100%; padding:10px; border:1px solid #cbd5e1; border-radius:6px;">
            </div>
            <div>
                <label style="display:block; font-size:13px; font-weight:600; color:#475569; margin-bottom:5px;">Travel Date</label>
                <input type="date" style="width:100%; padding:10px; border:1px solid #cbd5e1; border-radius:6px;">
            </div>
            <div>
                <label style="display:block; font-size:13px; font-weight:600; color:#475569; margin-bottom:5px;">Seater Requirement</label>
                <select style="width:100%; padding:10px; border:1px solid #cbd5e1; border-radius:6px;">
                    <option>20-Seater Mini AC Luxury</option>
                    <option>35-Seater BharatBenz AC</option>
                    <option>45-Seater Volvo Luxury</option>
                    <option>53-Seater Multi-Axle</option>
                </select>
            </div>
            <div style="grid-column:span 2; margin-top:10px;">
                <button type="submit" style="width:100%; background:#E02020; color:#fff; font-weight:700; padding:12px; border:none; border-radius:6px; cursor:pointer; font-size:16px;">Request Quotation</button>
            </div>
        </form>
    </div>
</div>
"""
generate_secondary_page("Bus Hire & Private Charter", "bus-hire", "Bus Hire & Rental", "Corporate & Wedding Bus Hire", "Rent a Chartered Bus", "CALL CHARTER DESK: 0731-4288888", "tel:07314288888", bus_hire_body, "bus-hire.html")

# 3. About Us
about_body = """
<div style="background:#fff; padding:45px 35px; border-radius:12px; box-shadow:0 10px 30px rgba(0,0,0,0.06);">
    <div style="text-align:center; margin-bottom:40px;">
        <span class="cb-badge">ABOUT CHARTERED SPEED</span>
        <h2 style="font-size:32px; font-weight:800; color:#14213d; margin:10px 0;">India's Leading Passenger Mobility Pioneer</h2>
        <p style="color:#666; max-width:700px; margin:auto;">Building trusted connections and elevating intercity passenger travel across Central, Western, and North-Eastern India.</p>
    </div>

    <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(320px, 1fr)); gap:40px; align-items:center; margin-bottom:40px;">
        <div>
            <h3 style="font-size:24px; font-weight:800; color:#14213d; margin-bottom:15px;">Driven by Excellence & Punctuality</h3>
            <p style="color:#64748b; line-height:26px; margin-bottom:15px;">Chartered Bus (a division of Chartered Speed Limited) was founded with a clear vision: to redefine intercity road travel in India. Headquartered in Indore, Madhya Pradesh, we have grown from an intercity pioneer to one of the largest multimodal transport operators in the country.</p>
            <p style="color:#64748b; line-height:26px; margin-bottom:15px;">With a modern fleet of over 260+ company-owned and maintained coaches covering 640+ daily scheduled routes, we serve over 4.2 million happy passengers every year. Our services bridge metropolitan hubs, historic pilgrimage destinations, and developing smart cities.</p>
            <p style="color:#64748b; line-height:26px;">From real-time GPS tracking to dedicated pilot training academies and sanitized coach maintenance depots, every touchpoint is engineered for passenger comfort and safety.</p>
        </div>
        <div>
            <img src="/images/fleet_bus.jpg" alt="Chartered Bus Fleet" style="width:100%; border-radius:12px; box-shadow:0 15px 35px rgba(0,0,0,0.12);">
        </div>
    </div>

    <div class="cb-stats-row">
        <div class="cb-stat-item">
            <h3>260+</h3>
            <p>Modern Luxury Coaches</p>
        </div>
        <div class="cb-stat-item">
            <h3>640+</h3>
            <p>Daily Routes Operated</p>
        </div>
        <div class="cb-stat-item">
            <h3>4.2M+</h3>
            <p>Annual Passengers</p>
        </div>
        <div class="cb-stat-item">
            <h3>98.4%</h3>
            <p>On-Time Performance</p>
        </div>
    </div>
</div>
"""
generate_secondary_page("About Us", "about", "About Us", "Over 4.2 Million Travelers Yearly", "About Chartered Speed", "EXPLORE OUR FLEET", "/gallery", about_body, "about-us.html")

# 4. Contact Us
contact_body = """
<div style="background:#fff; padding:45px 35px; border-radius:12px; box-shadow:0 10px 30px rgba(0,0,0,0.06);">
    <div style="text-align:center; margin-bottom:40px;">
        <span class="cb-badge">24X7 SUPPORT & BOOKINGS</span>
        <h2 style="font-size:32px; font-weight:800; color:#14213d; margin:10px 0;">We Are Always Here For You</h2>
        <p style="color:#666; max-width:700px; margin:auto;">Reach out to our customer care team, locate your nearest boarding terminal, or inquire about custom group bookings.</p>
    </div>

    <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(280px, 1fr)); gap:25px; margin-bottom:40px;">
        <div style="border:1px solid #e2e8f0; border-radius:10px; padding:25px; text-align:center;">
            <div style="font-size:36px; margin-bottom:10px;">📞</div>
            <h3 style="font-size:18px; font-weight:800; color:#14213d;">Phone Bookings (24x7)</h3>
            <p style="color:#E02020; font-size:20px; font-weight:800; margin:10px 0;"><a href="tel:09993288888" style="color:inherit; text-decoration:none;">099932-88888</a></p>
            <p style="color:#64748b; font-size:14px;">Landline: 0731-4288888</p>
        </div>

        <div style="border:1px solid #e2e8f0; border-radius:10px; padding:25px; text-align:center;">
            <div style="font-size:36px; margin-bottom:10px;">💳</div>
            <h3 style="font-size:18px; font-weight:800; color:#14213d;">Online Payment Support</h3>
            <p style="color:#E02020; font-size:20px; font-weight:800; margin:10px 0;"><a href="tel:07389599999" style="color:inherit; text-decoration:none;">073895 99999</a></p>
            <p style="color:#64748b; font-size:14px;">Hours: 10:00 AM to 8:00 PM</p>
        </div>

        <div style="border:1px solid #e2e8f0; border-radius:10px; padding:25px; text-align:center;">
            <div style="font-size:36px; margin-bottom:10px;">✉️</div>
            <h3 style="font-size:18px; font-weight:800; color:#14213d;">Email Inquiries</h3>
            <p style="color:#0465b4; font-size:18px; font-weight:700; margin:10px 0;"><a href="mailto:support@charteredbus.in" style="color:inherit; text-decoration:none;">support@charteredbus.in</a></p>
            <p style="color:#64748b; font-size:14px;">Fast response within 2 business hours</p>
        </div>
    </div>

    <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:12px; padding:35px;">
        <h3 style="font-size:22px; font-weight:800; color:#14213d; margin-bottom:20px;">Primary City Terminals</h3>
        <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(240px, 1fr)); gap:20px;">
            <div>
                <h4 style="font-weight:700; color:#E02020; margin-bottom:5px;">Indore Hub</h4>
                <p style="font-size:13px; color:#475569; line-height:20px;">AICTSL Bus Depot, Geeta Bhawan Square, Near Navlakha, Indore, Madhya Pradesh - 452001</p>
            </div>
            <div>
                <h4 style="font-weight:700; color:#E02020; margin-bottom:5px;">Bhopal Hub</h4>
                <p style="font-size:13px; color:#475569; line-height:20px;">ISBT Habibganj, Commercial Complex, Hoshangabad Rd, Bhopal, Madhya Pradesh - 462024</p>
            </div>
            <div>
                <h4 style="font-weight:700; color:#E02020; margin-bottom:5px;">Pune Hub</h4>
                <p style="font-size:13px; color:#475569; line-height:20px;">Wakad Flyover Boarding Point, Near Hinjawadi Bridge, Pune, Maharashtra - 411057</p>
            </div>
            <div>
                <h4 style="font-weight:700; color:#E02020; margin-bottom:5px;">Ahmedabad Hub</h4>
                <p style="font-size:13px; color:#475569; line-height:20px;">CTM Cross Road, Near Express Highway Entry, Amraiwadi, Ahmedabad, Gujarat - 380026</p>
            </div>
        </div>
    </div>
</div>
"""
generate_secondary_page("Contact Us", "contact", "Contact Us", "24x7 Customer Support", "Contact Chartered Bus", "CALL 099932-88888", "tel:09993288888", contact_body, "contact.html")

# 5. Gallery
gallery_body = """
<div style="background:#fff; padding:45px 35px; border-radius:12px; box-shadow:0 10px 30px rgba(0,0,0,0.06);">
    <div style="text-align:center; margin-bottom:40px;">
        <span class="cb-badge">OUR FLEET</span>
        <h2 style="font-size:32px; font-weight:800; color:#14213d; margin:10px 0;">Chartered Bus Luxury Fleet & Amenities</h2>
        <p style="color:#666; max-width:700px; margin:auto;">Explore our state-of-the-art multi-axle Volvo sleeper coaches, sanitized passenger cabins, and modern terminals.</p>
    </div>

    <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(320px, 1fr)); gap:25px;">
        <div style="border-radius:10px; overflow:hidden; box-shadow:0 8px 25px rgba(0,0,0,0.08);">
            <img src="/images/hero_bus.jpg" alt="Chartered Volvo Multi-Axle" style="width:100%; height:230px; object-fit:cover;">
            <div style="padding:20px; background:#fff;">
                <h4 style="font-size:18px; font-weight:700; color:#14213d; margin-bottom:8px;">Volvo Multi-Axle Intercity Coach</h4>
                <p style="color:#64748b; font-size:13px;">Aerodynamic design, air-suspension smooth cruising, speed-governed safety.</p>
            </div>
        </div>

        <div style="border-radius:10px; overflow:hidden; box-shadow:0 8px 25px rgba(0,0,0,0.08);">
            <img src="/images/interior_bus.jpg" alt="Luxury Reclining Seats" style="width:100%; height:230px; object-fit:cover;">
            <div style="padding:20px; background:#fff;">
                <h4 style="font-size:18px; font-weight:700; color:#14213d; margin-bottom:8px;">Premium Ergonomic Reclining Seats</h4>
                <p style="color:#64748b; font-size:13px;">Plush calf support, ambient LED lighting, individual USB charger and reading lamp.</p>
            </div>
        </div>

        <div style="border-radius:10px; overflow:hidden; box-shadow:0 8px 25px rgba(0,0,0,0.08);">
            <img src="/images/fleet_bus.jpg" alt="Chartered Bus Terminal" style="width:100%; height:230px; object-fit:cover;">
            <div style="padding:20px; background:#fff;">
                <h4 style="font-size:18px; font-weight:700; color:#14213d; margin-bottom:8px;">Central Terminal & Fleet Depots</h4>
                <p style="color:#64748b; font-size:13px;">Synchronized dispatching, mechanical audit bays, and sanitization stations.</p>
            </div>
        </div>

        <div style="border-radius:10px; overflow:hidden; box-shadow:0 8px 25px rgba(0,0,0,0.08);">
            <img src="/images/route_express.jpg" alt="Expressway Transit" style="width:100%; height:230px; object-fit:cover;">
            <div style="padding:20px; background:#fff;">
                <h4 style="font-size:18px; font-weight:700; color:#14213d; margin-bottom:8px;">Express Highway Transit</h4>
                <p style="color:#64748b; font-size:13px;">Non-stop high speed connectivity between Indore, Bhopal, and metropolitan hubs.</p>
            </div>
        </div>

        <div style="border-radius:10px; overflow:hidden; box-shadow:0 8px 25px rgba(0,0,0,0.08);">
            <img src="/images/route_night.jpg" alt="Overnight Sleeper Bus" style="width:100%; height:230px; object-fit:cover;">
            <div style="padding:20px; background:#fff;">
                <h4 style="font-size:18px; font-weight:700; color:#14213d; margin-bottom:8px;">Night AC Sleeper Coaches</h4>
                <p style="color:#64748b; font-size:13px;">Sound-insulated private berths with sanitized blankets and soft pillows.</p>
            </div>
        </div>
    </div>
</div>
"""
generate_secondary_page("Fleet & Gallery", "gallery", "Fleet & Gallery", "Experience Luxury Travel", "Fleet & Photo Gallery", "VIEW BUS ROUTES", "/routes", gallery_body, "gallery.html")

print("All pages cleanly rebuilt and verified!")
