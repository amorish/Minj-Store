import re

def main():
    with open('portfolio.html', 'r', encoding='utf-8') as f:
        html = f.read()
        
    port_grid_start = html.find('<div class="port-grid" id="port-grid">')
    port_grid_end = html.find('</div>\n  </div>\n</section>\n\n<!-- FEEDBACK -->')
    if port_grid_end == -1:
        port_grid_end = html.find('</div>\n  </div>\n</section>\n\n<!-- CONTACT -->')
    if port_grid_end == -1:
        # Fallback
        port_grid_end = html.find('</section>', port_grid_start) - 16
        
    prefix = html[:port_grid_start + len('<div class="port-grid" id="port-grid">') + 1]
    suffix = html[port_grid_end:]
    
    new_cards = """
      <!-- 1. IRPE Logo -->
      <a href="past%20work/2025%20side%20project/irpe%20logo%20design.pdf" target="_blank" class="port-card stg" style="text-decoration:none; color:inherit; display:block;">
        <div class="port-thumb">
          <img src="past%20work/2025%20side%20project/irpe%20logo%20design.png" alt="Logo Design" loading="lazy" style="object-fit: cover; object-position: center;">
          <span class="port-chip">Logo</span>
        </div>
        <div class="port-info">
          <div class="port-client">IRPE</div>
          <div class="port-title">IRPE Logo Design</div>
        </div>
      </a>

      <!-- 2. Vasundhara Branding -->
      <a href="past%20work/2025%20vasundhara/buisinessCard.png" target="_blank" class="port-card stg" style="text-decoration:none; color:inherit; display:block;">
        <div class="port-thumb">
          <img src="past%20work/2025%20vasundhara/buisinessCard.png" alt="Business Card" loading="lazy" style="object-fit: cover; object-position: center;">
          <span class="port-chip">Business Card</span>
        </div>
        <div class="port-info">
          <div class="port-client">Vasundhara</div>
          <div class="port-title">Vasundhara Business Card</div>
        </div>
      </a>

      <a href="past%20work/2025%20vasundhara/TitleBanner.svg" target="_blank" class="port-card stg" style="text-decoration:none; color:inherit; display:block;">
        <div class="port-thumb">
          <img src="past%20work/2025%20vasundhara/TitleBanner.svg" alt="Title Banner" loading="lazy" style="object-fit: cover; object-position: center;">
          <span class="port-chip">Banner</span>
        </div>
        <div class="port-info">
          <div class="port-client">Vasundhara</div>
          <div class="port-title">Vasundhara Title Banner</div>
        </div>
      </a>

      <!-- 3. Pragati Poster (and PDF) -->
      <a href="past%20work/2025%20Pragati/PRAGATI_STUDY_CENTRE%20Admission_Form%20-%20(clean).pdf" target="_blank" class="port-card stg" style="text-decoration:none; color:inherit; display:block;">
        <div class="port-thumb">
          <img src="past%20work/2025%20Pragati/pragati%20poster.png" alt="Poster" loading="lazy" style="object-fit: cover; object-position: center top;">
          <span class="port-chip">Poster / Form</span>
        </div>
        <div class="port-info">
          <div class="port-client">Pragati</div>
          <div class="port-title">Pragati Admission Form & Poster</div>
        </div>
      </a>

      <!-- 4. Cineq Logo -->
      <a href="past%20work/2026%20cineq/cineqLogoDarkmode.png" target="_blank" class="port-card stg" style="text-decoration:none; color:inherit; display:block;">
        <div class="port-thumb">
          <img src="past%20work/2026%20cineq/cineqLogoDarkmode.png" alt="Cineq Logo" loading="lazy" style="object-fit: cover; object-position: center; background: #000;">
          <span class="port-chip">Logo</span>
        </div>
        <div class="port-info">
          <div class="port-client">Cineq</div>
          <div class="port-title">Cineq Darkmode Logo</div>
        </div>
      </a>

      <!-- 5. St George High School (Combined) -->
      <div class="port-card stg" style="display:block;">
        <a href="past%20work/2024%20st%20george/output/ST%20GEORGE%20HIGH%20SCHOOL%20class%206%20math%20question%20paper.pdf" target="_blank" style="text-decoration:none; color:inherit; display:block;">
          <div class="port-thumb">
            <img src="past%20work/2024%20st%20george/output/ST%20GEORGE%20HIGH%20SCHOOL%20class%206%20math%20question%20paper.png" alt="Question Paper" loading="lazy" style="object-fit: cover; object-position: center top;">
            <span class="port-chip">Academic</span>
          </div>
        </a>
        <div class="port-info">
          <div class="port-client">St George High School</div>
          <div class="port-title" style="margin-bottom: 10px;">Math Question Papers</div>
          <div style="display: flex; gap: 15px;">
             <a href="past%20work/2024%20st%20george/output/ST%20GEORGE%20HIGH%20SCHOOL%20class%206%20math%20question%20paper.pdf" target="_blank" style="color: #F5A623; text-decoration: none; font-size: 0.9rem; font-weight: 600;">📄 Class 6 PDF</a>
             <a href="past%20work/2024%20st%20george/output/ST%20GEORGE%20HIGH%20SCHOOL%20class%207%20math%20question%20paper.pdf" target="_blank" style="color: #F5A623; text-decoration: none; font-size: 0.9rem; font-weight: 600;">📄 Class 7 PDF</a>
          </div>
        </div>
      </div>

      <!-- 6. Mahi Furniture Quotation -->
      <a href="past%20work/MAHI%20FURNITURE.png" target="_blank" class="port-card stg" style="text-decoration:none; color:inherit; display:block;">
        <div class="port-thumb">
          <img src="past%20work/MAHI%20FURNITURE.png" alt="Quotation" loading="lazy" style="object-fit: cover; object-position: center top;">
          <span class="port-chip">Quotation</span>
        </div>
        <div class="port-info">
          <div class="port-client">Mahi Furniture</div>
          <div class="port-title">Mahi Furniture Quotation</div>
        </div>
      </a>

      <!-- 7. Shok Bhoj Nimantran Card -->
      <a href="past%20work/shok%20bhoj%20nimantran%20card.png" target="_blank" class="port-card stg" style="text-decoration:none; color:inherit; display:block;">
        <div class="port-thumb">
          <img src="past%20work/shok%20bhoj%20nimantran%20card.png" alt="Invitation Card" loading="lazy" style="object-fit: cover; object-position: center top;">
          <span class="port-chip">Invitation Card</span>
        </div>
        <div class="port-info">
          <div class="port-client">Local Client</div>
          <div class="port-title">Shok Bhoj Nimantran Card</div>
        </div>
      </a>
"""
    
    with open('portfolio.html', 'w', encoding='utf-8') as f:
        f.write(prefix + new_cards + suffix)

if __name__ == '__main__':
    main()
