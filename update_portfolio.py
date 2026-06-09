import re

def process():
    with open('portfolio.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Update Trusted Logos
    trusted_logos_old = '''    <div class="trusted-logos">
      <div class="trusted-logo"><i data-lucide="shield-check"></i><span>Sharma Medicals</span></div>
      <div class="trusted-logo"><i data-lucide="utensils"></i><span>New Raj Dhaba</span></div>
      <div class="trusted-logo"><i data-lucide="graduation-cap"></i><span>Sunrise Coaching</span></div>
      <div class="trusted-logo"><i data-lucide="shopping-bag"></i><span>Anjali Boutique</span></div>
    </div>'''
    trusted_logos_new = '''    <div class="trusted-logos">
      <div class="trusted-logo"><img src="worked%20with%20brand%20institute%20logos/vasundhara%20logo.svg" alt="Vasundhara" style="height:24px;"><span>Vasundhara</span></div>
      <div class="trusted-logo"><img src="worked%20with%20brand%20institute%20logos/pragati%20logo.png" alt="Pragati" style="height:24px;"><span>Pragati</span></div>
      <div class="trusted-logo"><i data-lucide="graduation-cap"></i><span>St George High School</span></div>
    </div>'''
    content = content.replace(trusted_logos_old, trusted_logos_new)

    # 2. Update Portfolio HTML
    port_html_old = '''      <div class="port-card stg">
        <div class="port-thumb">
          <img src="https://images.unsplash.com/photo-1634942537034-2531766767d1?w=600&auto=format&fit=crop&q=80" alt="Brand identity design" loading="lazy">
          <span class="port-chip" data-i18n="p1.chip">Logo + Card</span>
        </div>
        <div class="port-info">
          <div class="port-client">Sharma Medicals</div>
          <div class="port-title" data-i18n="p1.t">Logo (Text + Icon) + Visiting Card</div>
        </div>
      </div>

      <div class="port-card stg">
        <div class="port-thumb">
          <img src="https://images.unsplash.com/photo-1547592180-85f173990554?w=600&auto=format&fit=crop&q=80" alt="Banner design" loading="lazy">
          <span class="port-chip" data-i18n="p2.chip">Banner</span>
        </div>
        <div class="port-info">
          <div class="port-client">New Raj Dhaba</div>
          <div class="port-title" data-i18n="p2.t">Flex Banner (With Photos) + Festival Post</div>
        </div>
      </div>

      <div class="port-card stg">
        <div class="port-thumb">
          <img src="https://images.unsplash.com/photo-1513542789411-b6a5d4f31634?w=600&auto=format&fit=crop&q=80" alt="Academic design" loading="lazy">
          <span class="port-chip" data-i18n="p3.chip">Academic</span>
        </div>
        <div class="port-info">
          <div class="port-client">Sunrise Coaching Centre</div>
          <div class="port-title" data-i18n="p3.t">Question Paper (Formatted) + Certificate</div>
        </div>
      </div>

      <div class="port-card stg">
        <div class="port-thumb">
          <img src="https://images.unsplash.com/photo-1611162617213-7d7a39e9b1d7?w=600&auto=format&fit=crop&q=80" alt="Social media design" loading="lazy">
          <span class="port-chip" data-i18n="p4.chip">Social Media</span>
        </div>
        <div class="port-info">
          <div class="port-client">Anjali Boutique</div>
          <div class="port-title" data-i18n="p4.t">Festival Post Pack (Set of 5)</div>
        </div>
      </div>

      <div class="port-card stg">
        <div class="port-thumb">
          <img src="https://images.unsplash.com/photo-1467232004584-a241de8bcf5d?w=600&auto=format&fit=crop&q=80" alt="Website design" loading="lazy">
          <span class="port-chip" data-i18n="p5.chip">Website</span>
        </div>
        <div class="port-info">
          <div class="port-client">Dr. Chakraborty Clinic</div>
          <div class="port-title" data-i18n="p5.t">Website - Tier 2 (3 Pages)</div>
        </div>
      </div>

      <div class="port-card stg">
        <div class="port-thumb">
          <img src="https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=600&auto=format&fit=crop&q=80" alt="Google Maps listing" loading="lazy">
          <span class="port-chip" data-i18n="p6.chip">Google Maps</span>
        </div>
        <div class="port-info">
          <div class="port-client">Kalyan Electricals</div>
          <div class="port-title" data-i18n="p6.t">Google Map Listing + Visiting Card</div>
        </div>
      </div>'''

    port_html_new = '''      <div class="port-card stg">
        <div class="port-thumb">
          <img src="past%20work/2025%20vasundhara/buisinessCard.png" alt="Business Card" loading="lazy" style="object-fit: cover; object-position: center;">
          <span class="port-chip" data-i18n="p1.chip">Business Card</span>
        </div>
        <div class="port-info">
          <div class="port-client">Vasundhara</div>
          <div class="port-title" data-i18n="p1.t">Vasundhara Business Card</div>
        </div>
      </div>

      <div class="port-card stg">
        <div class="port-thumb">
          <img src="past%20work/2025%20vasundhara/TitleBanner.svg" alt="Title Banner" loading="lazy" style="object-fit: cover; object-position: center;">
          <span class="port-chip" data-i18n="p2.chip">Banner</span>
        </div>
        <div class="port-info">
          <div class="port-client">Vasundhara</div>
          <div class="port-title" data-i18n="p2.t">Vasundhara Title Banner</div>
        </div>
      </div>

      <div class="port-card stg">
        <div class="port-thumb">
          <img src="past%20work/2025%20Pragati/pragati%20poster.png" alt="Poster" loading="lazy" style="object-fit: cover; object-position: center top;">
          <span class="port-chip" data-i18n="p3.chip">Poster</span>
        </div>
        <div class="port-info">
          <div class="port-client">Pragati</div>
          <div class="port-title" data-i18n="p3.t">Pragati Event Poster</div>
        </div>
      </div>

      <div class="port-card stg">
        <div class="port-thumb">
          <img src="past%20work/2025%20side%20project/irpe%20logo%20design.png" alt="Logo Design" loading="lazy" style="object-fit: cover; object-position: center;">
          <span class="port-chip" data-i18n="p4.chip">Logo</span>
        </div>
        <div class="port-info">
          <div class="port-client">IRPE</div>
          <div class="port-title" data-i18n="p4.t">IRPE Logo Design</div>
        </div>
      </div>

      <div class="port-card stg">
        <div class="port-thumb">
          <img src="past%20work/2024%20st%20george/output/ST%20GEORGE%20HIGH%20SCHOOL%20class%206%20math%20question%20paper.png" alt="Question Paper" loading="lazy" style="object-fit: cover; object-position: center top;">
          <span class="port-chip" data-i18n="p5.chip">Academic</span>
        </div>
        <div class="port-info">
          <div class="port-client">St George High School</div>
          <div class="port-title" data-i18n="p5.t">Class 6 Math Question Paper</div>
        </div>
      </div>

      <div class="port-card stg">
        <div class="port-thumb">
          <img src="past%20work/2024%20st%20george/output/ST%20GEORGE%20HIGH%20SCHOOL%20class%207%20math%20question%20paper.png" alt="Question Paper" loading="lazy" style="object-fit: cover; object-position: center top;">
          <span class="port-chip" data-i18n="p6.chip">Academic</span>
        </div>
        <div class="port-info">
          <div class="port-client">St George High School</div>
          <div class="port-title" data-i18n="p6.t">Class 7 Math Question Paper</div>
        </div>
      </div>'''
    
    content = content.replace(port_html_old, port_html_new)
    
    # 3. Update 'port.note':'Mock projects - real design, fictional clients' to 'Real clients, real design.'
    content = content.replace("'port.note':'Mock projects - real design, fictional clients'", "'port.note':'Recent Projects'")
    content = content.replace("'port.note':'प्रायोगिक प्रोजेक्ट्स - असली डिज़ाइन, काल्पनिक ग्राहक'", "'port.note':'हाल के प्रोजेक्ट्स'")
    content = content.replace("'port.note':'নমুনা প্রজেক্ট - আসল ডিজাইন, কাল্পনিক গ্রাহক'", "'port.note':'সাম্প্রতিক প্রজেক্ট'")

    # 4. Update Translations
    # English
    en_old = """  'p1.chip':'Logo + Card','p1.t':'Logo (Text + Icon) + Visiting Card',
  'p2.chip':'Banner','p2.t':'Flex Banner (With Photos) + Festival Post',
  'p3.chip':'Academic','p3.t':'Question Paper (Formatted) + Certificate',
  'p4.chip':'Social Media','p4.t':'Festival Post Pack (Set of 5)',
  'p5.chip':'Website','p5.t':'Website - Tier 2 (3 Pages)',
  'p6.chip':'Google Maps','p6.t':'Google Map Listing + Visiting Card',"""
    en_new = """  'p1.chip':'Business Card','p1.t':'Vasundhara Business Card',
  'p2.chip':'Banner','p2.t':'Vasundhara Title Banner',
  'p3.chip':'Poster','p3.t':'Pragati Event Poster',
  'p4.chip':'Logo','p4.t':'IRPE Logo Design',
  'p5.chip':'Academic','p5.t':'Class 6 Math Question Paper',
  'p6.chip':'Academic','p6.t':'Class 7 Math Question Paper',"""
    content = content.replace(en_old, en_new)

    # Hindi
    hi_old = """  'p1.chip':'लोगो + कार्ड','p1.t':'लोगो (टेक्स्ट + आइकन) + विजिटिंग कार्ड',
  'p2.chip':'बैनर','p2.t':'फ्लेक्स बैनर (फ़ोटो के साथ) + त्योहार पोस्ट',
  'p3.chip':'अकादमिक','p3.t':'प्रश्न पत्र (फॉर्मेटेड) + प्रमाण पत्र',
  'p4.chip':'सोशल मीडिया','p4.t':'त्योहार पोस्ट पैक (5 का सेट)',
  'p5.chip':'वेबसाइट','p5.t':'वेबसाइट - टियर 2 (3 पेज)',
  'p6.chip':'गूगल मैप्स','p6.t':'गूगल मैप लिस्टिंग + विजिटिंग कार्ड',"""
    hi_new = """  'p1.chip':'विजिटिंग कार्ड','p1.t':'वसुंधरा विजिटिंग कार्ड',
  'p2.chip':'बैनर','p2.t':'वसुंधरा बैनर',
  'p3.chip':'पोस्टर','p3.t':'प्रगति इवेंट पोस्टर',
  'p4.chip':'लोगो','p4.t':'आईआरपीई (IRPE) लोगो डिज़ाइन',
  'p5.chip':'अकादमिक','p5.t':'कक्षा 6 गणित प्रश्न पत्र',
  'p6.chip':'अकादमिक','p6.t':'कक्षा 7 गणित प्रश्न पत्र',"""
    content = content.replace(hi_old, hi_new)

    # Bengali
    bn_old = """  'p1.chip':'লোগো + কার্ড','p1.t':'লোগো (টেক্সট + আইকন) + ভিজিটিং কার্ড',
  'p2.chip':'ব্যানার','p2.t':'ফ্লেক্স ব্যানার (ছবি সহ) + উৎসবের পোস্ট',
  'p3.chip':'অ্যাকাডেমিক','p3.t':'প্রশ্নপত্র (ফরম্যাটেড) + শংসাপত্র',
  'p4.chip':'সোশ্যাল মিডিয়া','p4.t':'উৎসবের পোস্ট প্যাক (৫-এর সেট)',
  'p5.chip':'ওয়েবসাইট','p5.t':'ওয়েবসাইট - টায়ার ২ (৩ পেজ)',
  'p6.chip':'গুগল ম্যাপস','p6.t':'গুগল ম্যাপ লিস্টিং + ভিজিটিং কার্ড',"""
    bn_new = """  'p1.chip':'ভিজিটিং কার্ড','p1.t':'বসুন্ধরা ভিজিটিং কার্ড',
  'p2.chip':'ব্যানার','p2.t':'বসুন্ধরা ব্যানার',
  'p3.chip':'পোস্টার','p3.t':'প্রগতি ইভেন্ট পোস্টার',
  'p4.chip':'লোগো','p4.t':'IRPE লোগো ডিজাইন',
  'p5.chip':'অ্যাকাডেমিক','p5.t':'ষষ্ঠ শ্রেণীর গণিত প্রশ্নপত্র',
  'p6.chip':'অ্যাকাডেমিক','p6.t':'সপ্তম শ্রেণীর গণিত প্রশ্নপত্র',"""
    content = content.replace(bn_old, bn_new)

    with open('portfolio.html', 'w', encoding='utf-8') as f:
        f.write(content)

process()
