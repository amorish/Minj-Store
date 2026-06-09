import re

cards_html = """      <a href="past%20work/2025%20vasundhara/buisinessCard.png" target="_blank" class="port-card stg" style="text-decoration:none; color:inherit; display:block;">
        <div class="port-thumb">
          <img src="past%20work/2025%20vasundhara/buisinessCard.png" alt="Business Card" loading="lazy" style="object-fit: cover; object-position: center;">
          <span class="port-chip" data-i18n="p1.chip">Business Card</span>
        </div>
        <div class="port-info">
          <div class="port-client">Vasundhara</div>
          <div class="port-title" data-i18n="p1.t">Vasundhara Business Card</div>
        </div>
      </a>

      <a href="past%20work/2025%20vasundhara/TitleBanner.svg" target="_blank" class="port-card stg" style="text-decoration:none; color:inherit; display:block;">
        <div class="port-thumb">
          <img src="past%20work/2025%20vasundhara/TitleBanner.svg" alt="Title Banner" loading="lazy" style="object-fit: cover; object-position: center;">
          <span class="port-chip" data-i18n="p2.chip">Banner</span>
        </div>
        <div class="port-info">
          <div class="port-client">Vasundhara</div>
          <div class="port-title" data-i18n="p2.t">Vasundhara Title Banner</div>
        </div>
      </a>

      <a href="past%20work/2025%20Pragati/pragati%20poster.png" target="_blank" class="port-card stg" style="text-decoration:none; color:inherit; display:block;">
        <div class="port-thumb">
          <img src="past%20work/2025%20Pragati/pragati%20poster.png" alt="Poster" loading="lazy" style="object-fit: cover; object-position: center top;">
          <span class="port-chip" data-i18n="p3.chip">Poster</span>
        </div>
        <div class="port-info">
          <div class="port-client">Pragati</div>
          <div class="port-title" data-i18n="p3.t">Pragati Event Poster</div>
        </div>
      </a>

      <a href="past%20work/2025%20side%20project/irpe%20logo%20design.png" target="_blank" class="port-card stg" style="text-decoration:none; color:inherit; display:block;">
        <div class="port-thumb">
          <img src="past%20work/2025%20side%20project/irpe%20logo%20design.png" alt="Logo Design" loading="lazy" style="object-fit: cover; object-position: center;">
          <span class="port-chip" data-i18n="p4.chip">Logo</span>
        </div>
        <div class="port-info">
          <div class="port-client">IRPE</div>
          <div class="port-title" data-i18n="p4.t">IRPE Logo Design</div>
        </div>
      </a>

      <a href="past%20work/2024%20st%20george/output/ST%20GEORGE%20HIGH%20SCHOOL%20class%206%20math%20question%20paper.png" target="_blank" class="port-card stg" style="text-decoration:none; color:inherit; display:block;">
        <div class="port-thumb">
          <img src="past%20work/2024%20st%20george/output/ST%20GEORGE%20HIGH%20SCHOOL%20class%206%20math%20question%20paper.png" alt="Question Paper" loading="lazy" style="object-fit: cover; object-position: center top;">
          <span class="port-chip" data-i18n="p5.chip">Academic</span>
        </div>
        <div class="port-info">
          <div class="port-client">St George High School</div>
          <div class="port-title" data-i18n="p5.t">Class 6 Math Question Paper</div>
        </div>
      </a>

      <a href="past%20work/2024%20st%20george/output/ST%20GEORGE%20HIGH%20SCHOOL%20class%207%20math%20question%20paper.png" target="_blank" class="port-card stg" style="text-decoration:none; color:inherit; display:block;">
        <div class="port-thumb">
          <img src="past%20work/2024%20st%20george/output/ST%20GEORGE%20HIGH%20SCHOOL%20class%207%20math%20question%20paper.png" alt="Question Paper" loading="lazy" style="object-fit: cover; object-position: center top;">
          <span class="port-chip" data-i18n="p6.chip">Academic</span>
        </div>
        <div class="port-info">
          <div class="port-client">St George High School</div>
          <div class="port-title" data-i18n="p6.t">Class 7 Math Question Paper</div>
        </div>
      </a>

      <a href="past%20work/MAHI%20FURNITURE.png" target="_blank" class="port-card stg" style="text-decoration:none; color:inherit; display:block;">
        <div class="port-thumb">
          <img src="past%20work/MAHI%20FURNITURE.png" alt="Quotation" loading="lazy" style="object-fit: cover; object-position: center top;">
          <span class="port-chip" data-i18n="p7.chip">Quotation</span>
        </div>
        <div class="port-info">
          <div class="port-client">Mahi Furniture</div>
          <div class="port-title" data-i18n="p7.t">Mahi Furniture Quotation</div>
        </div>
      </a>

      <a href="past%20work/shok%20bhoj%20nimantran%20card.png" target="_blank" class="port-card stg" style="text-decoration:none; color:inherit; display:block;">
        <div class="port-thumb">
          <img src="past%20work/shok%20bhoj%20nimantran%20card.png" alt="Invitation Card" loading="lazy" style="object-fit: cover; object-position: center top;">
          <span class="port-chip" data-i18n="p8.chip">Invitation Card</span>
        </div>
        <div class="port-info">
          <div class="port-client">Local Client</div>
          <div class="port-title" data-i18n="p8.t">Shok Bhoj Nimantran Card</div>
        </div>
      </a>

      <a href="past%20work/2026%20cineq/cineqLogoDarkmode.png" target="_blank" class="port-card stg" style="text-decoration:none; color:inherit; display:block;">
        <div class="port-thumb">
          <img src="past%20work/2026%20cineq/cineqLogoDarkmode.png" alt="Cineq Logo" loading="lazy" style="object-fit: cover; object-position: center; background: #000;">
          <span class="port-chip" data-i18n="p9.chip">Logo</span>
        </div>
        <div class="port-info">
          <div class="port-client">Cineq</div>
          <div class="port-title" data-i18n="p9.t">Cineq Brand Logo</div>
        </div>
      </a>

      <a href="past%20work/ID%20card/IDCard%20mockup.png" target="_blank" class="port-card stg" style="text-decoration:none; color:inherit; display:block;">
        <div class="port-thumb">
          <img src="past%20work/ID%20card/IDCard%20mockup.png" alt="ID Card" loading="lazy" style="object-fit: cover; object-position: center;">
          <span class="port-chip" data-i18n="p10.chip">ID Card</span>
        </div>
        <div class="port-info">
          <div class="port-client">School/Office</div>
          <div class="port-title" data-i18n="p10.t">Identity Card Design</div>
        </div>
      </a>"""

with open('portfolio.html', 'r', encoding='utf-8') as f:
    content = f.read()

# I need to replace everything from <div class="port-grid" id="port-grid"> up to the end of the 10th card, which ends right before </div></div></section>
start_idx = content.find('<div class="port-grid" id="port-grid">')
if start_idx != -1:
    # Find the end of the grid
    # It is right before <!-- PROCESS --> or </section>
    end_idx = content.find('    </div>\n  </div>\n</section>\n\n<!-- PROCESS -->')
    if end_idx != -1:
        prefix = content[:start_idx + len('<div class="port-grid" id="port-grid">\n\n')]
        suffix = content[end_idx:]
        new_content = prefix + cards_html + "\n" + suffix
        
        with open('portfolio.html', 'w', encoding='utf-8') as f:
            f.write(new_content)
        print("Restored and updated cards!")
    else:
        print("End idx not found")
else:
    print("Start idx not found")

