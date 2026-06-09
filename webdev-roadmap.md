# Web Dev Roadmap 2026
### Goal: Build portfolio sites + local business websites (Tier 1 & 2)
### Start: After August IBPS SO exam
### Daily time: 1.5 hrs weekdays · 3 hrs Saturday · Sunday off

---

## What This Roadmap Is NOT

This is not a full-stack roadmap. No React. No Node. No databases.
This is the exact minimum to build good-looking, fast, client-ready websites
with smooth animations — and nothing more.

Skip everything not on this list.

---

## Overview

| Phase | Topic | Duration | Weeks |
|-------|-------|----------|-------|
| 1 | HTML Modern | 1 week | Week 1 |
| 2 | CSS Modern | 2 weeks | Week 2–3 |
| 3 | JavaScript Essentials | 2 weeks | Week 4–5 |
| 4 | GSAP + Animations | 1 week | Week 6 |
| 5 | Windsurf + Vibe Coding | 1 week | Week 7 |
| 6 | Build 3 Real Projects | 3 weeks | Week 8–10 |

**Total: 10 weeks. September to mid-November.**

---

## Phase 1 — HTML Modern
### Duration: 1 week · ~10 hours

**What changed recently:**
Old HTML tutorials teach `<div>` for everything.
Modern HTML has semantic elements that improve SEO and accessibility.

**What to learn:**

- Semantic structure: `<header>`, `<main>`, `<section>`, `<article>`, `<footer>`, `<nav>`
- Text: headings hierarchy, `<p>`, `<span>`, `<strong>`, `<em>`
- Links and images: `<a>`, `<img>` with `srcset` for responsive images
- Forms: `<input>` types, `<label>`, `<button>`, `<select>`, `<textarea>`
- New elements: `<dialog>` (modals without JS), `<details>/<summary>` (accordion)
- Popover API: `popover` attribute — native tooltip/modal without JS
- `<picture>` element for modern image formats (WebP, AVIF)
- Meta tags for SEO: title, description, Open Graph

**What to skip:**
- Tables (not for layout)
- `<iframe>` deep dive
- Canvas/SVG internals
- Deprecated tags (`<font>`, `<center>`, `<marquee>`)

**Resource:**
- Kevin Powell — "HTML for beginners" playlist (3–4 videos)
- MDN HTML basics: developer.mozilla.org/en-US/docs/Learn/HTML

**Build after this phase:**
A plain unstyled 3-page website structure. No CSS yet.
Just semantic HTML. Home + Services + Contact.

---

## Phase 2 — CSS Modern
### Duration: 2 weeks · ~20 hours

**This is the most important phase. Spend the most time here.**

### Week 2A — Layout & Basics

**What to learn:**
- Box model: margin, padding, border, box-sizing
- Display: block, inline, inline-block, none
- Flexbox: flex-direction, justify-content, align-items, gap, flex-wrap
- CSS Grid: grid-template-columns, grid-template-rows, grid-area, gap
- Subgrid: `subgrid` value for nested grids
- Positioning: relative, absolute, fixed, sticky
- Units: px, rem, em, %, vw, vh, svh (new — for mobile)
- CSS Variables (Custom Properties): `--color-accent: #F5A623`
- CSS Nesting: native, no SCSS needed anymore

```css
/* Old way — needed SCSS */
.card { color: red; }
.card .title { font-size: 2rem; }

/* Modern way — native CSS nesting */
.card {
  color: red;
  .title { font-size: 2rem; }
}
```

### Week 2B — Modern Selectors & Responsive

**What to learn:**
- `:has()` selector — select parent based on child (game changer)

```css
/* Apply style to nav IF it contains an open dropdown */
nav:has(.dropdown.open) { background: black; }
```

- `:is()`, `:where()`, `:not()` — cleaner selectors
- Container Queries — responsive based on parent size, not screen size

```css
@container (min-width: 400px) {
  .card { flex-direction: row; }
}
```

- `@layer` — control CSS specificity
- Media queries (still needed): `@media (max-width: 768px)`
- `clamp()` for fluid typography: `font-size: clamp(1rem, 2.5vw, 2rem)`
- Transitions: `transition: all 0.3s ease`
- Transform: `translate`, `scale`, `rotate`
- CSS animations: `@keyframes`, `animation`
- `text-wrap: balance` — automatic balanced headlines (new)
- Scroll Snap: `scroll-snap-type`
- Backdrop filter: `backdrop-filter: blur(12px)` — for glassmorphism

**What to skip:**
- SASS/SCSS — CSS nesting replaced it
- Bootstrap/Tailwind — learn vanilla CSS first
- Float-based layouts — dead, never use

**Resource:**
- Kevin Powell YouTube — ENTIRE channel is what you need
  - "Learn CSS Grid" (1 hour)
  - "Learn Flexbox" (30 min)
  - ":has() is incredible" video
  - "Container Queries" video
  - "CSS Nesting" video
- web.dev/learn/css — Google's free CSS course, modern

**Build after this phase:**
Style the 3-page site from Phase 1.
Make it look professional. Mobile responsive.
Use CSS variables for colors. Use Grid for layout.

---

## Phase 3 — JavaScript Essentials
### Duration: 2 weeks · ~20 hours

**Important:** You don't need deep JS for Tier 1–2 websites.
You need just enough to make interactive things work
and to understand GSAP code.

### Week 4 — Core JS

**What to learn:**
- Variables: `const`, `let` (never `var`)
- Data types: string, number, boolean, array, object, null, undefined
- Functions: regular + arrow functions
- Template literals: `` `Hello ${name}` ``
- Array methods: `.map()`, `.filter()`, `.forEach()`
- Objects: creation, accessing properties, destructuring
- Conditionals: `if/else`, ternary operator
- Loops: `for`, `forEach`
- Modules: `import`/`export`

### Week 5 — DOM + Browser APIs

**What to learn:**
- DOM selection: `querySelector`, `querySelectorAll`
- DOM manipulation: `textContent`, `innerHTML`, `classList`
- Events: `addEventListener`, click, scroll, resize, input
- `classList` methods: `.add()`, `.remove()`, `.toggle()`, `.contains()`
- Intersection Observer — detect when elements enter viewport

```javascript
// Show element when it enters the screen
const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('visible');
    }
  });
});

document.querySelectorAll('.animate').forEach(el => observer.observe(el));
```

- Fetch API basics: load JSON data
- `localStorage` basics: save simple data
- Form handling: prevent default, get input values

**What to skip:**
- Async/await deep dive
- Promises advanced patterns
- Object-oriented JS / classes
- TypeScript
- Node.js
- Any framework (React, Vue, Svelte)

**Resource:**
- javascript.info — best free JS reference, no fluff
  Read: Fundamentals → Objects → Arrays → DOM → Events
  (Don't read the whole thing — just these chapters)
- Kevin Powell also has JS videos for CSS-focused devs

**Build after this phase:**
Add a hamburger menu (mobile nav toggle),
a scroll-to-top button,
and a simple contact form that validates before submit.

---

## Phase 4 — GSAP + Animations
### Duration: 1 week · ~10 hours

**This is the fun part. This is what makes sites look premium.**

**What to learn:**

### Core GSAP
```javascript
// Basic: animate from state to state
gsap.to(".hero-title", { opacity: 1, y: 0, duration: 1, ease: "power3.out" });

// fromTo: define start AND end
gsap.fromTo(".card",
  { opacity: 0, y: 60 },
  { opacity: 1, y: 0, duration: 0.8 }
);

// Timeline: sequence multiple animations
const tl = gsap.timeline();
tl.from(".nav", { y: -100, duration: 0.5 })
  .from(".hero-title", { opacity: 0, y: 40, duration: 0.8 }, "-=0.2")
  .from(".hero-subtitle", { opacity: 0, y: 20, duration: 0.6 }, "-=0.4");
```

### ScrollTrigger (most important plugin)
```javascript
gsap.registerPlugin(ScrollTrigger);

gsap.from(".section-title", {
  scrollTrigger: {
    trigger: ".section-title",
    start: "top 80%",
    toggleActions: "play none none reverse"
  },
  opacity: 0,
  y: 50,
  duration: 0.8
});
```

### Stagger (animate multiple elements in sequence)
```javascript
gsap.from(".service-card", {
  scrollTrigger: ".services-grid",
  opacity: 0,
  y: 40,
  duration: 0.6,
  stagger: 0.15   // 0.15 second gap between each card
});
```

**What to skip:**
- DrawSVG plugin (paid)
- Morph plugin (paid)
- Physics plugins
- Three.js integration (too complex now)

**The only eases you need:**
- `power3.out` — snappy deceleration (most used)
- `power2.inOut` — smooth both ends
- `elastic.out(1, 0.5)` — bouncy
- `none` — linear, for looping animations

**Resource:**
- gsap.com/get-started — official, well-written
- GreenSock YouTube channel:
  - "ScrollTrigger for beginners"
  - "GSAP Timeline basics"
- GSAP CodePen demos — copy, break, understand

**Performance rule:**
Only animate `transform` and `opacity`.
Never animate `width`, `height`, `top`, `left`, `margin`, `padding`.
Those cause reflow and stutter on budget phones.
GSAP uses transform by default — you're safe.

**Build after this phase:**
Rebuild your portfolio page with:
- Hero text fade-in on load (timeline)
- Service cards stagger-in on scroll
- Smooth section reveals throughout

---

## Phase 5 — Windsurf + Vibe Coding
### Duration: 1 week · ~8 hours

**This is how you 10x your output without 10x the time.**

### Setup
1. Download Windsurf: codeium.com/windsurf
2. Install Live Server extension (local preview)
3. Set up a project folder structure:

```
my-portfolio/
├── index.html
├── css/
│   └── style.css
├── js/
│   └── main.js
└── assets/
    └── images/
```

### How to prompt Windsurf effectively

**Bad prompt:**
> "Make a website"

**Good prompt:**
> "Create a hero section with dark background (#0D0D0D), a headline that
> says 'Design & Web Services', a subheadline, and a WhatsApp CTA button.
> Use Poppins font from Google Fonts. Add a GSAP fade-in animation from
> below on page load. Mobile responsive."

**Rules for prompting:**
- Always specify exact colors
- Always mention the font
- Specify mobile responsive every time
- Reference existing code: "In the style.css I already have..."
- Ask for one section at a time, not the whole page

### When AI code breaks
Ask: *"This code gives [error message]. Here is the full code: [paste]. Fix it."*
Don't rewrite from scratch. Fix what exists.

### What to read in AI-generated code
You don't need to understand every line. You need to understand:
- What selector is being targeted
- What property is being changed
- What value it's being changed to

Everything else GSAP and the browser handles.

**Build after this phase:**
Rebuild a section from scratch using only Windsurf prompts.
Compare the time vs writing manually.
Find the balance: what to write yourself vs what to prompt.

---

## Phase 6 — Build 3 Real Projects
### Duration: 3 weeks · ~40 hours

**This is where learning becomes skill.
Build real things. Don't build tutorials.**

### Project 1 — Your Portfolio Site (Week 8)
Everything you've learned, applied to your own portfolio.

Must have:
- Hero with GSAP timeline animation
- Services section with ScrollTrigger stagger
- Portfolio grid with hover effects
- About section
- WhatsApp contact button (floating + inline)
- Mobile responsive
- Fast load (no heavy libraries except GSAP)

Deploy on: **Netlify** (drag and drop the folder, free)

### Project 2 — Local Business Site Tier 1 (Week 9)
Pick a real or fictional local business.
Build a 1-page landing site.

Must have:
- Business name + services
- Google Maps embed
- WhatsApp CTA
- GSAP scroll reveals
- Mobile first design

### Project 3 — Local Business Site Tier 2 (Week 10)
3-page site with a contact form.

Must have:
- Home + Services + Contact pages
- Contact form using Formspree (free, no backend needed)
- Photo gallery (CSS grid + lightbox)
- GSAP animations throughout
- SEO meta tags
- Fast loading images (WebP format, compressed)

---

## Tools You Need (All Free)

| Tool | Purpose | Link |
|------|---------|------|
| Windsurf | AI code editor | codeium.com/windsurf |
| VS Code | Code editor backup | code.visualstudio.com |
| Chrome DevTools | Debug, inspect | Built into Chrome |
| Netlify | Free hosting | netlify.com |
| Formspree | Contact forms | formspree.io |
| Squoosh | Compress images | squoosh.app |
| Google Fonts | Free fonts | fonts.google.com |
| GSAP CDN | Animations | cdnjs.cloudflare.com |
| Coolors | Color palettes | coolors.co |
| unDraw | Free illustrations | undraw.co |

---

## What to Skip Completely (For Now)

| Technology | Why Skip |
|-----------|---------|
| React / Vue / Svelte | Overkill for Tier 1–2 sites |
| Node.js / Express | No backend needed yet |
| TypeScript | Adds complexity, zero benefit now |
| SASS / SCSS | CSS nesting replaced it |
| Bootstrap / Tailwind | Learn vanilla CSS first |
| Webpack / Vite | Not needed for plain HTML sites |
| PHP / WordPress | Later, if clients need it |
| Databases | Not in scope |

---

## Weekly Schedule (Post-August)

**Weekdays (1.5 hours):**
- 45 min: watch / read learning resource
- 45 min: code what you just learned

**Saturday (3 hours):**
- Build session — no tutorials, only building
- If stuck: ask Windsurf, then understand the answer

**Sunday:**
- Rest. Seriously.

---

## Progress Checkpoints

After Week 1: Can write proper semantic HTML from memory
After Week 3: Can build a responsive layout without Googling flexbox
After Week 5: Can add click events and scroll animations with vanilla JS
After Week 6: Can make a page feel alive with GSAP ScrollTrigger
After Week 7: Can prompt Windsurf to build a full section in 10 minutes
After Week 10: Can deliver a Tier 1 site in 1 weekend, Tier 2 in 2 weekends

---

## The One Rule

**Never spend more than 20 minutes stuck on something.**

After 20 minutes: ask Windsurf.
After Windsurf answers: understand why it works.
Move on.

Time is the only thing you don't have enough of.
Don't waste it on Stack Overflow rabbit holes.

---

*Start date: Day after IBPS SO Prelims — September 2026*
*End date: Mid-November 2026*
*Outcome: Fully capable of delivering client work, earning pocket money, and building a real portfolio*
