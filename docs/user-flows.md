# User Flows & Operational State Workflows — SmartPark India

This document defines the authoritative state machine and user journeys across all four roles: **Driver**, **Field Attendant**, **Facility Operator**, and **Platform Super Admin**.

---

## 1. Driver Flow: Discovery to Confirmed Booking

1. **App Launch & Authentication:**
   * Driver opens the app (`AUTH-01`).
   * Phone number entry with `+91` validation (`AUTH-02`).
   * Automated SMS OTP read and HMAC session establishment (`AUTH-03`).
   * Multi-vehicle garage profile setup with HSRP number plate and vehicle class selection (`AUTH-04`, `DRV-18`).

2. **Destination & Vehicle Discovery (`DRV-01`):**
   * Geolocation permission requested with graceful manual address fallback.
   * Commuter selects target destination (e.g., "Connaught Place", "Cyber City") or drops a pin on the interactive map.
   * Selects active vehicle category from 6 classes: **Cycle**, **Two-Wheeler**, **Car**, **Auto-Rickshaw**, **Van/SUV**, **Heavy Truck**.
   * Results feed renders verified facility cards with distance, starting price, and **Availability Freshness Pill** (`Updated by operator 2m ago`).

3. **Advanced Filtering (`DRV-12`):**
   * Driver opens filter modal to specify strict ramp clearance (`> 2.0m`), distance radius slider (`500m - 15km`), covered/underground basement preference, EV 60kW charging, and "Operator-Verified Live (< 10m)" confidence filter.

4. **Facility Detail & Multi-Level Bay Selection (`DRV-02`, `DRV-02B`):**
   * Driver inspects facility hours, overhead height clearance, and ingress ramp directions.
   * Enters **Interactive Multi-Level Deck Blueprint (`DRV-02B`)** to select floor (`Basement B2`) and pick an available bay (`B2-19`) near Elevator Core B.

5. **Atomic Inventory Hold & Quote (`DRV-03`):**
   * Driver confirms duration window (e.g., 2 Hours).
   * Backend database locks Bay B2-19 under a serializable transaction with an atomic 10-minute hold (`expires_at = now() + interval '10m'`).
   * Quote summary displays base tariff + incremental hours + municipal fee + 18% CGST/SGST tax breakdown.

6. **UPI Escrow Checkout (`DRV-04`):**
   * Real-time 5:00 countdown timer displayed during payment session.
   * Driver pays via UPI Intent (Google Pay, PhonePe, Paytm, CRED) or custom VPA.
   * Payment webhook verifies cryptographic provider signature and promotes hold to confirmed booking.

7. **Digital Pass Delivery (`DRV-05`):**
   * Confirmed booking screen issues dynamic RS256-signed QR code.
   * Screen provides 100% brightness trigger, anti-screenshot pulsating watermark, and turn-by-turn navigation deep link to the facility entrance ramp.

---

## 2. Driver Flow: Arrival, Ingress, Active Session & Exit

1. **Ingress & Ramp Verification:**
   * Driver arrives at facility ingress gate and presents digital QR pass (`DRV-05`).
   * Attendant scans QR using optical POS scanner (`ATT-10`, `ATT-11`).
   * Server validates cryptographically signed token, time window, vehicle plate, and marks ingress event. Barrier lifts.

2. **Active Session & Live Bay Tracker (`DRV-06`):**
   * In-app session timer starts with live elapsed duration display.
   * Displays bay navigation reminder (`Bay B2-19, Pillar 10 near Lift Lobby B`).

3. **Session Extension (`DRV-07`):**
   * Driver taps 1-touch extension (`+30m`, `+1hr`, `+2hr`).
   * Server re-verifies bay availability, calculates incremental tariff with GST, and charges via UPI.

4. **Overstay Alert & Pre-Clearance (`DRV-08`):**
   * If driver exceeds duration, an urgent amber/red alert is triggered.
   * Surcharge breakdown is calculated; driver can settle dues in-app prior to exit to prevent gate congestion.

5. **Exit Clearance & Statutory Tax Invoice (`DRV-09`):**
   * Attendant scans exit QR (`ATT-12`), verifying zero dues. Exit barrier lifts.
   * Driver receives GSTR-1 compliant digital tax invoice with CGST/SGST breakdown and PDF/WhatsApp export.

6. **Cancellation & Automated Refund Pipeline (`DRV-22`):**
   * Driver cancels booking before arrival window.
   * Policy engine calculates tier refund (> 1 hr = 100% base + GST refund).
   * Live 4-step NPCI UPI refund pipeline initiates instant ARN reversal to driver's bank account in < 5 minutes.

---

## 3. Field Attendant Flow: Gate Operations & POS Terminal

1. **Shift Login & Terminal Pin (`OPR-01`):**
   * Attendant signs in with biometric/credential PIN on rugged Android POS (Sunmi V2).
   * Terminal binds to designated lane (`DLF CyberCity Radial Gate 2 · Lane 02`).

2. **Optical Scan & Barrier Lift (`ATT-10`, `ATT-11`):**
   * Sub-300ms optical scanning of driver QR pass.
   * POS renders vehicle plate, category, and bay ID.
   * Attendant confirms ingress; terminal fires barrier relay trigger.

3. **Spot Walk-In Ingestion (`ATT-16`):**
   * For unbooked vehicles arriving at the gate, attendant enters category and plate number.
   * System decrements available capacity and prints thermal paper slip with entrance barcode.

4. **Offline Cryptographic Fallback (`ATT-13`):**
   * When network is unavailable, POS falls back to local public-key verification of driver's signed JWT token.
   * Ingress records are queued in local encrypted SQLite and synced upon network restoration.

5. **Shift Close & Cash Reconciliation (`ATT-05`):**
   * At shift end, attendant enters counted physical currency denominations (₹500, ₹200, ₹100, ₹50, ₹20).
   * System verifies parity against recorded walk-in slip dues with **Zero Cash Discrepancy** badge.
   * Thermal handover slip is printed and signed over to the incoming shift supervisor.

---

## 4. Facility Operator Flow: Onboarding, Capacity & Revenue SaaS

1. **Operator Onboarding & KYC (`OPR-01`):**
   * Business entity registration with PAN, Trade License, and municipal lease agreement.
   * Escrow bank account verification for daily automated settlement disbursements.

2. **Facility Creation & Geofence Pinning (`OPR-02`):**
   * Satellite polygon boundary drawing.
   * Distinct pinning of public street entrance vs basement ingress ramp coordinates.

3. **Deck & Capacity Configuration (`OPR-03`):**
   * Multi-level floor setup (B1, B2, Level 1, Terrace).
   * Quota distribution across 6 vehicle classes and hourly tariff schedules.

4. **Operations Monitoring (`OPR-14`, `OPR-15`):**
   * Real-time facility occupancy dashboard (84.6% live gauge).
   * Manual bay blocking for maintenance with mandatory audit reason logging.

5. **Daily Settlements & Tax Reporting (`OPR-17`):**
   * Reconciliation of app pre-bookings, FASTag toll, and on-site cash collections.
   * Automated GSTR-1 tax export and municipal royalty share calculation.

---

## 5. Super Admin Flow: Operations & Real-Time Fraud Watchdog

1. **National Operations & Fraud Stream (`ADM-01`):**
   * Real-time monitoring across Delhi NCR, Mumbai, Bengaluru, and national grid.
   * Heatmap visualization of facility occupancy synced every 3.2s.
   * Automated incident watchdog flags duplicate plate entries, attendant manual barrier override spikes, and webhook delays.

2. **Operator & Concession KYC Desk (`ADM-02`):**
   * Legal review and verification of operator documentation and municipal concession leases.

3. **Facility Geofence & Ramp Geometry Audit (`ADM-03`):**
   * Satellite audit of ingress ramps, turning radii, and road deceleration buffers prior to listing activation.
