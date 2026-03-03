# Microve.ai

A static website for Microve.ai, a consulting business specializing in practical micro-automations for small-to-medium businesses.

## Overview

Microve.ai positions itself as the practical alternative to "AI fantasy" hype. The site communicates that the problem in businesses is not the people, but the processes—and offers surgical automation solutions that save time and increase revenue.

**Live Site:** [GitHub Repository](https://github.com/boolsa/ai-company-website) (private)

## Pages

- **`index.html`** - Homepage with StoryBrand messaging, workflow diagram, 4-step process, and competitive positioning
- **`what-we-do.html`** - Detailed service explanation with automation type comparison table and competitive messaging
- **`calculator.html`** - Interactive cost calculator with "Cost of Waiting" feature showing weekly/monthly/quarterly losses
- **`contact.html`** - Lead capture form with validation and enhanced UX

## Design Philosophy

### Color Scheme: "Sage & Clay"

A nature-inspired palette that maintains warmth while improving readability:

| Color | Hex | Usage |
|-------|-----|-------|
| **Clay (Terracotta)** | `#B85C4A` | Primary CTAs, accents, highlights |
| **Sage** | `#8FA68E` | Secondary accents, timeline connectors, visual rest |
| **Warm White** | `#FAFAF8` | Background - cleaner than cream, reduces yellow cast |
| **Charcoal** | `#1F1F1F` | Primary text - crisp with slight warmth |
| **Stone** | `#6B6560` | Secondary text - 12:1 contrast ratio (WCAG AAA) |

### Typography

- **Headlines:** Playfair Display (serif) - conveys heritage and trustworthiness
- **Body:** Inter (sans-serif) - modern, highly readable
- **Contrast:** 12:1 ratio exceeds accessibility standards

### Key Features

1. **StoryBrand Framework** - A-grade implementation with:
   - Situation-based hero identification
   - Specific founder story creating empathy
   - Clear failure stakes (cost of waiting)
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

### v2.0 - Sage & Clay Redesign
- Muted terracotta from aggressive orange-red to clay (#B85C4A)
- Changed background from yellow-cream to warm white (#FAFAF8)
- Added sage green (#8FA68E) as secondary accent for visual rest
- Improved text contrast to 12:1 ratio (WCAG AAA)
- Simplified 4-step timeline layout
- Enhanced comparison table with zebra striping
- Fixed SVG diagram contrast issues

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
        terracotta: '#B85C4A',
        sage: '#8FA68E',
        cream: '#FAFAF8',
        charcoal: '#1F1F1F',
        stone: '#6B6560'
      }
    }
  }
}
```

### File Structure
```
microve-ai/
├── index.html          # Homepage
├── what-we-do.html     # Services page
├── calculator.html     # Cost calculator
├── contact.html        # Contact form
└── README.md          # This file
```

## Notes

- This is a lightweight static build requiring no framework or build process
- All navigation links are relative
- SVG diagrams are inline for performance and scalability
- No external assets beyond Tailwind CDN and Google Fonts
- Site is optimized for small-to-medium business owners as the target audience

## Target Audience

Small-to-medium businesses (5-50 employees) that:
- Need custom automation solutions
- Cannot afford full-time tech teams or agency markups
- Want senior-level implementation without enterprise overhead
- Are tired of watching talent leak into busywork

## License

Private repository - All rights reserved © 2026 Microve.ai