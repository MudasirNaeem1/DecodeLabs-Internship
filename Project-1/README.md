# DecodeLabs - Full Stack Internship Platform
### Project 1: Responsive Frontend Interface · Batch 2026

---

## Overview

DecodeLabs is a structured full-stack internship platform that trains developers through sequential, industry-grade projects. This repository contains **Project 1** - a fully responsive, multi-page frontend interface built with pure HTML5, CSS3, and vanilla JavaScript. No frameworks. No libraries. Just fundamentals done right.

---

## Project Structure

```
decodelabs/
├── index.html       # All pages (SPA via JS routing)
├── style.css        # Complete stylesheet
├── main.js          # Page router, interactions, animations
└── logo.svg         # Brand logo (white + cyan SVG)
```

---

## Pages

| Page | ID | Description |
|---|---|---|
| Home | `#home` | Hero, features, toolkit, CTA |
| About | `#about` | Story, standards, three pillars |
| Courses | `#courses` | All 4 project tracks + dashboard |
| Projects | `#projects` | Active P1 + locked P2–P4 |
| Contact | `#contact` | Contact info + message form |

---

## Tech Stack

- **HTML5** - Semantic landmarks, ARIA roles, accessible markup
- **CSS3** - CSS Grid, Flexbox, `clamp()` fluid typography, CSS variables, `backdrop-filter`
- **JavaScript (ES6)** - DOM routing, IntersectionObserver scroll reveal, counter animation
- **Fonts** - Quantico (headings) + DM Sans (body) via Google Fonts

---

## Features

- Single-page routing - no page reloads, smooth fade transitions
- Mobile-first responsive layout - works from 320px to 4K
- Hamburger menu with animated ✕ toggle on mobile
- Scroll reveal animations on cards and sections
- Animated stat counters (500+, 12, 98%) on hero load
- Form focus states with glow ring
- Toast notification system
- Backend modal for locked features
- ESC key closes modal
- Footer link hover slide animation

---

## Getting Started

**Option 1 - VS Code Live Server**
1. Open the project folder in VS Code
2. Right-click `index.html` → `Open with Live Server`
3. Opens at `http://127.0.0.1:5500`

**Option 2 - Direct browser**
1. Double-click `index.html`
2. Opens locally in your default browser

> No build step, no npm install, no dependencies - just open and run.

---

## Design System

| Token | Value |
|---|---|
| Primary (Mocha) | `#A5856E` |
| Mocha Dark | `#7A5C44` |
| Accent (Blue) | `#A0D4E0` |
| Dark | `#2A1F17` |
| Background | `#FDFCFA` |
| Grey Surface | `#F2F0EA` |
| Heading Font | Quantico 700, uppercase |
| Body Font | DM Sans 400/500 |
| Border Radius | `14px` |

---

## Internship Roadmap

```
P1 - Responsive Frontend   ✅ Active
P2 - Backend APIs          🔒 Unlocks after P1
P3 - React SPA             🔒 Unlocks after P2
P4 - Full Stack Deploy     🔒 Unlocks after P3
```

---

## Submission Checklist

- [ ] All 5 pages render correctly on mobile and desktop
- [ ] No horizontal scroll on any viewport
- [ ] Hamburger menu works on mobile
- [ ] All buttons and nav links navigate correctly
- [ ] Form inputs have visible focus states
- [ ] Images (logo) load without broken icon
- [ ] Lighthouse score — Performance ≥ 90, Accessibility ≥ 90

---

## Contact

**DecodeLabs**
decodelabs.tech@gmail.com
www.decodelabs.tech
Greater Lucknow, India

---

*Built as part of the DecodeLabs Batch 2026 Internship Program.*
