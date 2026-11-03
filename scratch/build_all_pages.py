import re
import os

with open("/Users/akshatsakare/codex/public/srilanka-driver-original.html", "r", encoding="utf-8") as f:
    base_html = f.read()

# Replace all FAQ answers accurately
faq_pairs = [
    ("1. How do I book a Chartered Bus ticket online?",
     "You can easily book bus tickets online through our official portal, mobile app, or by calling our 24x7 phone booking helpline at <strong>099932-88888</strong>. Choose your origin, destination, and travel date, select your preferred seat on the interactive seat layout, and pay securely via UPI, credit/debit card, or net banking."),
    ("2. Can I track my bus location in real time?",
     "Yes! Every Chartered Bus coach is equipped with high-precision GPS tracking hardware. When you book, you receive a real-time tracking link via SMS. You can also view the exact live location and estimated arrival time on our mobile application."),
    ("3. What amenities are provided on Chartered Bus coaches?",
     "Depending on the coach service (Volvo Multi-Axle, AC Sleeper, or BharatBenz Seater), passengers enjoy comfortable ergonomic seating, USB mobile charging ports, reading lights, air-conditioned cabins, complimentary water bottles, sanitized blankets on night journeys, and emergency SOS buttons."),
    ("4. What is the baggage allowance per passenger?",
     "Each passenger is allowed up to <strong>15 kg of personal luggage</strong> free of charge. Your bags are tagged and stowed in our spacious undercarriage luggage compartments."),
    ("5. How can I hire or charter a whole bus for weddings or corporate events?",
     "We provide end-to-end chartered bus rentals for weddings, corporate offsites, religious yatras, and school/college tours. We offer 20-seater to 55-seater premium AC coaches with certified drivers and custom routing. Call our Charter Desk at <strong>0731-4288888</strong> or visit our Bus Hire section."),
    ("6. What is the cancellation and refund policy?",
     "Cancellations made 24+ hours before departure receive up to a 90% refund. Cancellations made between 12 to 24 hours receive 75% refund. Refunds are instantly initiated to your original payment mode."),
    ("7. Are female passengers provided safe and preferred seating?",
     "Safety is our top priority. Solo female travelers are allotted dedicated seats alongside other female passengers. All coaches feature CCTV surveillance and monitored speed controls."),
    ("8. How early should I report at the boarding point?",
     "Please report at your designated boarding point 15 to 20 minutes prior to scheduled departure. Our on-ground boarding executives will verify your m-ticket and assist with luggage."),
    ("9. Do you operate buses connecting Indore and Bhopal?",
     "Yes! We operate high-frequency non-stop and express buses between Indore and Bhopal every 30 minutes from 5:30 AM until 11:30 PM daily, making Chartered Bus the most preferred connection on this corridor."),
    ("10. What safety protocols are followed by Chartered Bus?",
     "All our vehicles undergo rigorous daily maintenance checks, GPS speed limiters, dual-crew shifts on overnight runs, breathalyzer checks before departure, and sanitized cabins."),
    ("11. How can I contact the customer support team?",
     "Our customer support is reachable 24x7 at <strong>099932-88888</strong> and <strong>0731-4288888</strong>, or via email at <a href='mailto:support@charteredbus.in'>support@charteredbus.in</a>. For payment disputes, call <strong>073895 99999</strong>."),
    ("12. Can I change my boarding point after booking?",
     "Yes, you can update your boarding point up to 2 hours before the scheduled departure through the Chartered Bus App or by contacting customer support."),
    ("13. Do buses make refreshment and restroom stops on long journeys?",
     "Yes, on long-distance routes, scheduled stops are made at verified, hygienic food plazas with clean washrooms and dining options."),
    ("14. What types of buses operate in the Chartered Bus fleet?",
     "Our fleet consists of Volvo 9600 Multi-Axle Sleepers, Scania Metrolink Luxury coaches, BharatBenz Air-Suspension AC Seaters, and modern intercity electric & CNG buses.")
]

for q, a in faq_pairs:
    pat = rf'(<h5 class="et_pb_toggle_title">\s*{re.escape(q)}\s*</h5>\s*<div class="et_pb_toggle_content clearfix">).*?(</div>)'
    rep = rf'\g<1><p>{a}</p>\g<2>'
    base_html = re.sub(pat, rep, base_html, flags=re.DOTALL)

with open("/Users/akshatsakare/codex/public/srilanka-driver-original.html", "w", encoding="utf-8") as f:
    f.write(base_html)

with open("/Users/akshatsakare/codex/public/index.html", "w", encoding="utf-8") as f:
    f.write(base_html)

print("Home page FAQs updated!")

# Function to create a subpage using the same header, footer, CSS, and layout structure
def make_page(page_title, page_heading, hero_sub, content_html, out_filename):
    p = base_html
    # Update title
    p = re.sub(r'<title>.*?</title>', f'<title>{page_title} | Chartered Bus</title>', p, count=1)
    
    # Update hero section
    p = p.replace('<h2>India\'s Leading Mobility Partner</h2>', f'<h2>{hero_sub}</h2>')
    p = p.replace('<h2>Chartered Bus Travel</h2>', f'<h2>{page_heading}</h2>')
    p = p.replace('<h2>Safe, Punctual & Affordable</h2>', '<h2>India\'s Most Trusted Fleet</h2>')
    
    # We replace the main content area (between header and footer)
    # The main content begins with `<div class="entry-content">` and ends before `</article>`
    # Specifically, replace Section 1 through Section 4 with content_html while keeping Section 0 (hero) or replacing Section 1-4
    m = re.search(r'(<div class="et_pb_section et_pb_section_1 et_section_regular" >.*?)(</div>\s*</div>\s*</div>\s*</article>)', p, re.DOTALL)
    if m:
        new_body = f"""<div class="et_pb_section et_section_regular" style="padding: 50px 0; background: #f8fafc;">
            <div class="container">
                {content_html}
            </div>
        </div>\n\\2"""
        p = p[:m.start(1)] + new_body + p[m.end(2):]
    
    with open(f"/Users/akshatsakare/codex/public/{out_filename}", "w", encoding="utf-8") as f:
        f.write(p)
    print(f"Created {out_filename}!")

# 1. Routes & Schedules Page
routes_content = """
<div style="background:#fff; padding:40px; border-radius:12px; box-shadow:0 10px 30px rgba(0,0,0,0.06);">
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
                <li>✓ <strong>Timings:</strong> 5:30 AM to 11:30 PM (Hourly & Half-Hourly)</li>
                <li>✓ <strong>Duration:</strong> 3 hrs 30 mins</li>
                <li>✓ <strong>Boarding Indore:</strong> AICTSL Campus, Geeta Bhawan, Radisson Sq</li>
                <li>✓ <strong>Drop Bhopal:</strong> ISBT Habibganj, Lal Ghati, Board Office</li>
            </ul>
            <a href="/#wpforms-723" style="display:block; text-align:center; background:#E02020; color:#fff; font-weight:700; padding:10px 20px; border-radius:6px; text-decoration:none;">Book Indore ⇌ Bhopal</a>
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
            <a href="/#wpforms-723" style="display:block; text-align:center; background:#E02020; color:#fff; font-weight:700; padding:10px 20px; border-radius:6px; text-decoration:none;">Book Indore ⇌ Pune</a>
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
            <a href="/#wpforms-723" style="display:block; text-align:center; background:#E02020; color:#fff; font-weight:700; padding:10px 20px; border-radius:6px; text-decoration:none;">Book Bhopal ⇌ Ahmedabad</a>
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
            <a href="/#wpforms-723" style="display:block; text-align:center; background:#E02020; color:#fff; font-weight:700; padding:10px 20px; border-radius:6px; text-decoration:none;">Book Indore ⇌ Jabalpur</a>
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
            <a href="/#wpforms-723" style="display:block; text-align:center; background:#E02020; color:#fff; font-weight:700; padding:10px 20px; border-radius:6px; text-decoration:none;">Book Ujjain Shuttle</a>
        </div>
    </div>
</div>
"""
make_page("Bus Routes & Schedules", "Routes & Schedules", "Explore 640+ Daily Routes", routes_content, "routes.html")

# 2. Bus Hire & Charter Page
bus_hire_content = """
<div style="background:#fff; padding:40px; border-radius:12px; box-shadow:0 10px 30px rgba(0,0,0,0.06);">
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
        <form action="/#wpforms-723" method="GET" style="display:grid; grid-template-columns:1fr 1fr; gap:15px;">
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
make_page("Bus Hire & Private Charter", "Bus Hire & Rental", "Corporate, Wedding & Group Charters", bus_hire_content, "bus-hire.html")

# 3. About Us Page
about_content = """
<div style="background:#fff; padding:40px; border-radius:12px; box-shadow:0 10px 30px rgba(0,0,0,0.06);">
    <div style="text-align:center; margin-bottom:40px;">
        <span class="cb-badge">ABOUT CHARTERED SPEED</span>
        <h2 style="font-size:32px; font-weight:800; color:#14213d; margin:10px 0;">India's Leading Passenger Mobility Pioneer</h2>
        <p style="color:#666; max-width:700px; margin:auto;">Building trusted connections and elevating intercity passenger travel across Central, Western, and North-Eastern India.</p>
    </div>

    <div style="display:grid; grid-template-columns:1fr 1fr; gap:40px; align-items:center; margin-bottom:40px;">
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
make_page("About Us", "About Chartered Bus", "Pioneering Indian Mobility", about_content, "about-us.html")

# 4. Contact Us Page
contact_content = """
<div style="background:#fff; padding:40px; border-radius:12px; box-shadow:0 10px 30px rgba(0,0,0,0.06);">
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
make_page("Contact Us", "Contact & Support", "24x7 Customer Helpline", contact_content, "contact.html")

# 5. Fleet & Gallery Page
gallery_content = """
<div style="background:#fff; padding:40px; border-radius:12px; box-shadow:0 10px 30px rgba(0,0,0,0.06);">
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
make_page("Fleet & Gallery", "Fleet & Gallery", "Experience Luxury Travel", gallery_content, "gallery.html")

print("All multiple pages generated successfully!")
