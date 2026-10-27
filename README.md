# ParkSpot UI/UX Design Module

> **Production-grade design system, 45-screen Google Stitch M3 interactive suite, multi-persona flows, design iterations, and live prototypes for ParkSpot Smart Parking Platform.**

---

## 🌟 Overview

The `ui_design` module is a self-contained, framework-agnostic design system and UI codebase that defines the complete frontend experience for ParkSpot. It unifies all design assets, interactive mockups, persona workflows, and visual specifications in one standard directory.

---

## 📂 Directory Structure

```
ui_design/
├── index.html                   # Master Design Hub (Launchpad for all screens & flows)
├── server.js                    # Zero-dependency Node.js HTTP preview server
├── serve_mockups.py             # Portable Python 3 HTTP preview server
├── package.json                 # NPM scripts and project configuration
├── styles.css                   # Master design system styles and CSS variables
├── .gitignore                   # Standard ignore rules
│
├── stitch-screens/              # Google Stitch M3 Interactive Suite (45 Screens)
│   ├── index.html               # Dual-Mode Studio Wall & Stage Focus Viewer
│   ├── screen-1-map-explore.html
│   ├── screen-2-facility-detail.html
│   ├── screen-3-deck-selector.html
│   ├── screen-4-checkout-quote.html
│   ├── screen-5-active-pass.html
│   ├── screen-6-barrier-clearance.html
│   ├── generate_stitch_suite.py
│   └── update_suite_with_unseen_screens.py
│
├── prototype/                   # Unified Interactive Web Prototype
│   └── index.html               # Tailwind CSS-powered interactive app prototype
│
├── flows/ & Root Flows          # Full Persona Flow Visualizers (103+ Screens)
│   ├── flow-driver.html         # Driver App Complete Lifecycle (53 Screens)
│   ├── flow-operator.html       # Operator SaaS Multi-Level Console (21 Screens)
│   ├── flow-attendant.html      # Attendant Handheld POS Scanner (16 Screens)
│   ├── flow-admin.html          # City Platform Admin Command Center (13 Screens)
│   ├── premium-showcase.html    # Flagship Photo-Led Screens
│   ├── drv-01-explore.html      # Driver Stage 1: Explore & Discovery
│   ├── drv-02b-bay.html         # Driver Stage 2: Deck B2 Bay Selector
│   ├── drv-04-checkout.html     # Driver Stage 4: Transparent Quote (₹76.70)
│   ├── drv-05-pass.html         # Driver Stage 5: Active Pass & QR Handshake
│   ├── opr-14-liveboard.html    # Operator Live Board
│   ├── att-10-scanner.html      # Attendant Fast Scanner
│   └── adm-01-command.html      # Admin City Command
│
├── iterations/                  # Design Explorations & Aesthetic Variants
│   ├── index.html               # Iterations comparison gallery
│   ├── iteration-*.html         # 13 Aesthetic Styles (Cyber HUD, Luxe, Transit, HSRP, etc.)
│   └── generate_iterations.py   # Iteration generator script
│
├── assets/                      # Production Visual Media & Typography
│   ├── parkspot-facility-hero.jpg
│   ├── parkspot-garage-b2.jpg
│   ├── parkspot-map-base.jpg
│   ├── parkspot-hsrp-plate.jpg
│   ├── qr-pass.png
│   ├── garage-hero.jpg
│   ├── city-street.jpg
│   ├── night-city.jpg
│   ├── parking-levels.jpg
│   ├── desk.jpg
│   └── fonts/                   # DejaVu Sans & Mono font family
│
└── docs/                        # Design System Guidelines & Acceptance Matrix
    ├── MASTER_UI_WORKFLOW_AND_DESIGN_SYSTEM.md # Tokens, Material 3 specs, colors
    ├── design.md                # UI architecture & responsive layouts
    ├── user-flows.md            # End-to-end customer & staff journeys
    └── QA_TEST_MATRIX.md        # Visual QA checklist & financial invariant rules
```

---

## 🚀 Quick Start (Running Locally)

This module includes built-in static servers that require zero external dependencies.

### Option 1: Using Node.js (Recommended)
```bash
# Run using Node.js directly
node server.js

# Or via npm
npm start
```
Open **`http://localhost:8765/`** in your browser.

### Option 2: Using Python 3
```bash
python3 serve_mockups.py
```

### Option 3: Using any static server (e.g. npx http-server)
```bash
npx -y http-server . -p 8765 --cors -c-1
```

---

## 📱 Google Stitch Driver Suite (45 Screens)

Located at `stitch-screens/index.html`, this suite implements all **14 lifecycle stages** of the driver experience on an accurate 390×844 iOS viewport canvas with Dynamic Island, Status Bar, and Home Indicator:

1. **Stage 01: Floating Ingress & App Launch** (`STITCH-31`, `STITCH-01`)
2. **Stage 02: Onboarding & Value Proposition** (`STITCH-02`, `STITCH-03`, `STITCH-04`)
3. **Stage 03: Authentication & Identity Suite** (`STITCH-05`, `STITCH-06`, `STITCH-07`, `STITCH-08`)
4. **Stage 04: Legal, DPDP Consent & Terms** (`STITCH-09`, `STITCH-10`)
5. **Stage 05: Discovery & Facility Detail** (`STITCH-11`, `STITCH-12`)
6. **Stage 06: Deck B2 Selection & Real-Time Bay Assignment** (`STITCH-13`, `STITCH-14`)
7. **Stage 07: Transparent Checkout Quote (₹76.70 SAC 999113)** (`STITCH-15`, `STITCH-16`, `STITCH-17`)
8. **Stage 08: Active Digital Pass & QR Barrier Handshake** (`STITCH-18`, `STITCH-19`, `STITCH-20`)
9. **Stage 09: Live Parking Session & Meter Ticker** (`STITCH-32`, `STITCH-33`, `STITCH-34`)
10. **Stage 10: In-Session Exceptions & Conflict Relocation** (`STITCH-35`, `STITCH-36`)
11. **Stage 11: EV Charging Hub & 60kW Telemetry** (`STITCH-37`, `STITCH-38`, `STITCH-39`)
12. **Stage 12: Exit Barrier Clear & Dual-SAC Invoice** (`STITCH-21`, `STITCH-40`)
13. **Stage 13: Commuter Pass Catalog & UPI AutoPay Mandate** (`STITCH-41`, `STITCH-42`, `STITCH-43`)
14. **Stage 14: Hardware Edge Touchpoints** (`EDGE-01` Driveway VMS Totem, `EDGE-02` 58mm Thermal Ticket)

---

## 🎨 Master Design System Standards

### Primary Color Palette
- **Brand Teal / Primary**: `#00685F` (Light: `#89F5E7`, Surface Container: `#004D46`)
- **Accent Emerald**: `#10B981` (Bay available / EV charging active)
- **Warning Amber**: `#F59E0B` (Grace period countdown / Overstay threshold)
- **Error Rose**: `#EF4444` (Unauthorized spot / Barrier halt)
- **Deep Slate / Dark Mode**: `#070B14`, `#0F172A`, `#1E293B`

### Financial Invariant (Enforced across all checkout screens)
- **Base Rate**: ₹60.00
- **Convenience / Platform Fee**: ₹5.00
- **CGST (9%)**: ₹5.85
- **SGST (9%)**: ₹5.85
- **Total Payable**: **₹76.70** (SAC Code: `999113`)

---

## 🤝 Integration Guide

- **Flutter / React Native**: Use screen dimensions 390×844 as the base viewport ratio (390dp width, 844dp height). All typography scales adhere to Material 3 standard tokens (`title-large`, `headline-medium`, `body-small`).
- **Web Applications**: Responsive breakpoints set at `640px` (mobile), `768px` (tablet), `1024px` (desktop liveboards).
- **Icons**: Standard Google Material Symbols Outlined (`https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined`).

---

## 📄 License & Attribution

Designed and maintained for **ParkSpot Smart Parking Platform** by **ByteWeave System**. All rights reserved.
