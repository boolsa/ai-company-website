# Microve.ai

> **"We fit tools to your problems. We never fit your problems into tools."**

A static website for Microve.ai, a consulting business specializing in practical micro-automations for small-to-medium businesses.

## Core Philosophy

- **Diagnostic-First:** We start by listening and analyzing workflows, not pitching products. 
- **Custom Micro-Tools:** We build targeted fixes using rule-based automation, AI, or both. We don't sell monolithic "AI dreams."
- **Targeted Intervention:** We plug solutions directly into workflow bottlenecks without overhauling a company's entire operation.

## Overview

Microve.ai positions itself as the practical alternative to "AI fantasy" hype. The site communicates that the problem in businesses is not the people, but the processes—and offers surgical automation solutions that save time and increase revenue.

**Live Site:** [GitHub Repository](https://github.com/boolsa/ai-company-website) (private)

## Pages

- **`index.html`** - Homepage with StoryBrand messaging, workflow diagram, 4-step process, and competitive positioning
- **`what-we-do.html`** - Detailed service explanation with:
  - Hero SVG graphic showing human-machine-automation workflow
  - Three-way comparison: Generic LLMs vs Agentic Platforms vs Microve
  - [SYSTEMS] section explaining rule-based vs AI automation choice framework
  - Condensed [STAKES] section with visual stat (67%)
- **`calculator.html`** - Interactive cost calculator with "Cost of Waiting" feature showing weekly/monthly/quarterly losses
- **`contact.html`** - Lead capture form with validation and enhanced UX

## Design Philosophy

### Design System: Swiss Minimalism (inspired by dify.ai)

Clean, grid-based, highly legible design with minimal embellishment:
- **2px border radius** throughout (nearly sharp corners)
- **Generous whitespace** (120px+ section padding)
- **Tight typography tracking** (-0.02em) on headlines
- **Monospace section labels** [ELIMINATE], [PROCESS], [TRANSFORM], [COMPOUND], [ABOUT]

### Color Scheme: Grounded Professional + Coral Accent

A refined palette balancing trust with energy:

| Color | Hex | Usage |
|-------|-----|-------|
| **Deep Navy** | `#1E3A5F` | Logo, headings, dark sections, trust/competence |
| **Sage Green** | `#7A9E7E` | Completion states, growth accents, visual rest |
| **Soft Coral** | `#E07A5F` | Primary CTAs, statistics, highlights, action/energy |
| **Warm White** | `#FAF9F7` | Background - clean, no yellow tint |
| **Charcoal** | `#2D3436` | Primary text - professional, readable |
| **Stone** | `#636E72` | Secondary text - 12:1 contrast ratio (WCAG AAA) |

**Color Psychology:**
- Navy = Trust, stability, competence
- Sage = Growth, balance, approachability
- Coral = Energy, warmth, action (complementary to cool navy/sage)
- Usage ratio: 60% neutral / 30% navy+sage / 10% coral accents

### Typography

- **Headlines:** Inter (sans-serif) - modern, tight tracking (-0.02em)
- **Body:** Inter (sans-serif) - highly readable
- **Labels:** JetBrains Mono (monospace) - [ELIMINATE], [PROCESS], etc.
- **Contrast:** 12:1 ratio exceeds accessibility standards

### Key Features

1. **StoryBrand Framework** - A-grade implementation with:
   - Situation-based hero identification ("Your best people are drowning in busywork")
   - Specific founder story creating empathy ("We lost a $40K deal...")
   - Clear failure stakes (automation gap, cost of waiting)
   - Visual 4-step process plan

2. **Competitive Positioning** - Anti-hype messaging:
   - "The gap is widening" section creates authentic urgency
   - "Cost of Waiting" calculator shows tangible losses
   - Differentiation from both cheap freelancers and expensive agencies

3. **Accessibility (A-grade)**:
   - WCAG AAA contrast ratios
   - Mobile hamburger navigation with ARIA labels
   - Keyboard navigation support
   - Skip-to-content links
   - Focus-visible states

4. **UX Enhancements**:
   - Real-time form validation
   - Loading states on form submission
   - Smooth scroll behavior
   - Responsive SVG diagrams
   - Touch targets ≥44px

## Technical Details

- **Framework:** Pure HTML/CSS with Tailwind CSS via CDN
- **No Build Process:** Direct file editing, no compilation required
- **Assets:** Inline SVGs for diagrams (scalable, no external dependencies)
- **Responsive:** Mobile-first design with breakpoints at `md:` (768px)
- **Performance:** Minimal external dependencies (Tailwind CDN, Google Fonts)

## Recent Major Updates

### v5.0 - Diagnostic-First & Custom Micro-Tools Architecture

Complete messaging alignment reflecting the updated mission statement: "We fit tools to your problems. We never fit your problems into tools."

#### Sitewide Language Updates
- Replaced all binary "Rules vs AI" phrasing with a unified approach: "Custom micro-tools using rule-based automation, AI, or both."
- Shifted positioning away from general "AI adoption" toward solving the hype-vs-reality gap.

#### Homepage (`index.html`)
- **"Why it's urgent now" redesign:** Replaced generic AI urgency with a 4-card breakdown:
  1. *The hype* (Magic AI platforms)
  2. *The chatbot gap* (Surface-level LLM usage)
  3. *The platform trap* (Rigid no-code tools)
  4. *What actually works* (Custom micro-tools)
- Updated "How it works" timeline to reflect the micro-tools approach.
- Updated eyebrow text to: `CUSTOM WORKFLOW AUTOMATION · PRACTICAL A.I. IMPLEMENTATION · FLEXIBLE TOOLS`

#### What We Do (`what-we-do.html`)
- **Redesigned "Targeted Intervention" SVG Diagrams:** Threw out the linear "factory line" flowchart. Both desktop and mobile SVGs now depict a continuous client workflow with specific "bottlenecks" highlighted, showing Microve plugging targeted micro-tools directly into those broken spots.
- Removed outdated "compounding statement" to streamline the page flow.

#### Contact & About Pages
- **Trust Panel (`contact.html`):** Added a 2-column layout to house a "diagnostic-first" trust panel next to the form (We listen → We analyze → We build).
- **Operator Credibility (`about.html`):** Wove the diagnostic methodology into the founder story ("We diagnose before we build").

#### Blog Architecture
- Replaced the standalone `calculator.html` and `success.html` with a new `cases.html` and blog infrastructure.
- Updated blog excerpts and meta descriptions to match the "micro-tools" language.

### v4.0 - Navigation Overhaul + Background + AI Reality Messaging

#### Navigation (all pages)
Complete nav redesign across all 4 pages, based on award-winning frontend design patterns:

- **Logo** — Refined from `text-3xl` to `1.5rem`; `.ai` TLD now uses JetBrains Mono at `0.6875rem` with precise `top: -5px` baseline raise — intentional type detail, not a superscript accident
- **"Main" → "Home"** — Clearer, universally understood nav label
- **Scroll-aware nav** — Passive scroll listener adds navy-tinted shadow + border darkening at 12px scroll; nav compresses `py-4 → py-2.5` on scroll, all at `0.25s ease`
- **Active state** — Coral `#E07A5F` 2px underline bar via `::after` pseudo-element; hover animates `scaleX(0 → 1)` from left with directional micro-interaction
- **CTA button** — Upgraded from `rounded-sm` square corners to full pill (`border-radius: 9999px`); inline arrow SVG; rest shadow + hover lift `translateY(-1px)`
- **Hamburger → X morph** — Three `<span>` lines morphing to X via CSS transforms; no JS class toggling for animation
- **Mobile menu** — Smooth slide-in via `max-height` + `opacity` transition (`cubic-bezier(0.4, 0, 0.2, 1)`); active item gets coral left border
- **Accessibility** — `aria-controls`, `role="region"`, Escape key closes menu and returns focus, click-outside closes menu

#### Background (all pages)
- Replaced flat `#FAF9F7` cream background with a **dot grid pattern** — navy dots (`rgba(30,58,95,0.18)`) at 1.5px radius, 28px spacing
- Removed `bg-cream` Tailwind class from all `<body>` tags (was overriding custom CSS); added `!important` guards
- Applied consistently across `index.html`, `what-we-do.html`, `calculator.html`, `contact.html`

#### What We Do Page — AI Reality Check Section
New [REALITY CHECK] section added above [COMPARE], with contrarian AI hype messaging:

- **Headline:** "Most AI Projects Fail. Here's Why Ours Don't."
- Body copy directly addresses the AI hype problem — companies spending recklessly without understanding what AI actually does
- Real example: $12K integration vs $150K AI model — same bottleneck, radically different cost
- Pull quote callout box: *"The real advantage isn't artificial intelligence — it's intelligent decisions about where to deploy it."*
- 3 differentiation cards: Diagnostic before deployment / Custom-built not configured / Surgical not scattered

#### What We Do Page — Header reorder
- "What we do" heading + subtext moved **above** the SVG workflow diagram (was below it)
- Diagram now appears after the framing copy, as supporting evidence rather than leading content

### v3.1 - What We Do Page Enhancement
- Added hero SVG graphic showing automation workflow (human → process → output)
- New [COMPARE] section with three-way comparison:
  - Generic LLMs (ChatGPT, Claude) — manual prompting, no workflow integration
  - Agentic Platforms (LangChain, AutoGPT) — complex configuration, overkill for SMBs
  - Microve.ai — zero configuration, custom-built, runs automatically
- Rewrote [SYSTEMS] section explaining rule-based vs AI automation:
  - Visual equation showing Rules + AI = Measurable Results
  - Clear criteria for choosing each approach
  - Focus on business outcomes (cost savings, productivity, revenue)
- Condensed [STAKES] section from 65 lines to 20 lines:
  - Single stat visualization (67% of employees quit due to repetitive tasks)
  - Punchy headline: "Chained to busywork, talent walks"
  - Streamlined to core message with single CTA

### v3.0 - Swiss Design System (dify.ai inspired)
- Switched to Inter font family (removed Playfair Display serif)
- Added JetBrains Mono for bracketed section labels
- Implemented 2px border radius (rounded-sm) for Swiss minimalism
- Added bracketed section labels [ELIMINATE], [PROCESS], [TRANSFORM], [COMPOUND], [ABOUT]
- Increased section spacing to 120px+ (py-32)
- Added tight tracking (-0.02em) on headlines
- Increased hero typography to 72px
- Removed statistics block (unsubstantiated claims)
- Increased logo size (text-3xl)

### v2.5 - Coral Accent Addition
- Added Soft Coral (#E07A5F) as third accent color
- Primary CTAs now use coral instead of navy
- Statistics and highlights use coral for energy
- Text highlights use coral underline (rgba(224, 122, 95, 0.25))
- Maintains navy for headings, logo, and dark sections

### v2.0 - Grounded Professional
- Changed from terracotta to Deep Navy (#1E3A5F)
- Updated sage to #7A9E7E
- Changed background to Warm White (#FAF9F7)
- Improved text contrast to 12:1 ratio (WCAG AAA)

### v1.5 - UX/UI Overhaul
- Added mobile hamburger navigation
- Implemented real-time form validation
- Added "Cost of Waiting" calculator feature
- Improved keyboard accessibility
- Added smooth scroll and focus states

### v1.0 - Initial Launch
- 4-page static site
- StoryBrand framework implementation
- Basic responsive design
- Contact form with validation

## Development

### To Modify Colors
Edit the Tailwind config in each HTML file:
```javascript
tailwind.config = {
  theme: {
    extend: {
      colors: {
        navy: '#1E3A5F',
        sage: '#7A9E7E',
        coral: '#E07A5F',
        cream: '#FAF9F7',
        charcoal: '#2D3436',
        stone: '#636E72'
      }
    }
  }
}
```

### File Structure
```
microve-ai/
├── index.html          # Homepage
├── what-we-do.html     # Services & Workflow diagram
├── cases.html          # Case studies
├── pricing.html        # Pricing
├── blog.html           # Blog index
├── blog-*.html         # Individual blog posts
├── about.html          # About/Founder story
├── contact.html        # Contact form
└── README.md           # This file
```

## Navigation Structure

**Desktop & Mobile:**
- Home → Homepage
- What We Do → Services explanation
- Cases → Case studies
- Blog → Insights & methodology
- About → Founder credibility
- Book a Call → Contact form

## Notes

- This is a lightweight static build requiring no framework or build process
- All navigation links are relative
- SVG diagrams are inline for performance and scalability
- No external assets beyond Tailwind CDN and Google Fonts
- Site is optimized for small-to-medium business owners as the target audience
- No client testimonials, use cases, or unsubstantiated metrics

## Target Audience

Small-to-medium businesses (5-50 employees) that:
- Need custom automation solutions
- Cannot afford full-time tech teams or agency markups
- Want senior-level implementation without enterprise overhead
- Are tired of watching talent leak into busywork

## License

Private repository - All rights reserved © 2026 Microve.ai
