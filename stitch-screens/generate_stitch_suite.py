#!/usr/bin/env python3
"""
Generate the Complete Flagship Google Stitch Driver UI Design Suite & Flow Viewer.
Produces docs/figma-mockups/stitch-screens/index.html with:
  1. Complete Standard Mobile Lifecycle:
     - Stage 1: Launch & Onboardings (Splash, 3-step carousel: Find, Reserve, Contactless Ingress)
     - Stage 2: Auth Suite (Welcome Gateway, Login with eye toggle, Register with DPDP, 3-step Forgot Password, Terms & Privacy)
     - Stage 3: Flagship 5-Tab Bottom Navigation Suite (Home, Bookings, Garage, Wallet, Profile)
     - Stage 4: Vehicle Passport & Height Clearance Check (2.1m check, HSRP plates, FASTag)
     - Stage 5: Map Discovery & Search HUD (Vector transit map with live radar pins, search autocomplete, filters)
     - Stage 6: Facility Telemetry & 2D Blueprint Deck Bay Selector (Ultrasonic counters, B2 Blueprint, Bay B2-14)
     - Stage 7: Statutory Quote & Secure 1-Tap UPI Checkout (Master Spec ₹76.70 quote SAC 999113, UPI intent, AutoPay pre-auth)
     - Stage 8: Ingress Wayfinding & Gate Clearance (PassKit QR pass, Ramp HUD, FASTag <1.2s boom barrier auto-lift, offline pass)
     - Stage 9: Active Dwell Session, EV Fast Charging, Tax Invoice & SOS (Live dwell ring, 60kW EV telemetry, GST invoice, SOS bay reassignment)
  2. Dual-Mode Viewer:
     - Studio Wall Mode (Panoramic side-by-side gallery with zoom slider 65%/80%/100%)
     - Interactive Device Stage Mode (Focused 390×844 iPhone 16 Pro device with live screen scrubber & design dossier)
"""
import os
from pathlib import Path

OUT_DIR = Path("/Users/maheshgiri/Documents/Projects/Parking/docs/figma-mockups/stitch-screens")

def build_stitch_suite():
    # Asset paths relative to stitch-screens/
    ASSETS = {
        "facility": "../assets/parkspot-facility-hero.jpg",
        "garage": "../assets/parkspot-garage-b2.jpg",
        "garage_stock": "../assets/garage-hero.jpg",
        "levels": "../assets/parking-levels.jpg",
        "map": "../assets/parkspot-map-base.jpg",
        "car": "../assets/car-detail.jpg",
        "plate": "../assets/parkspot-hsrp-plate.jpg",
        "qr": "../assets/qr-pass.png",
        "city": "../assets/city-street.jpg",
        "night": "../assets/night-city.jpg",
        "desk": "../assets/desk.jpg",
    }

    def icon(name, fill=False, size=18, extra_style=""):
        fill_cls = "fill" if fill else ""
        return f'<span class="material-symbols-outlined {fill_cls}" style="font-size:{size}px;{extra_style}">{name}</span>'

    def status_bar(dark=False):
        c = "#FFFFFF" if dark else "#0B1C30"
        return f"""
        <header class="ios-status-bar" style="color:{c};">
          <span class="ios-time">9:41</span>
          <div class="dynamic-island"></div>
          <div class="ios-icons">
            {icon("signal_cellular_alt", size=15)}
            {icon("wifi", size=15)}
            {icon("battery_full", size=18)}
          </div>
        </header>"""

    def nav_header(title, sub="", right_icon=None, dark=False, back=True):
        c = "#FFFFFF" if dark else "#0B1C30"
        sub_c = "#94A3B8" if dark else "#565E74"
        bg = "rgba(11,28,48,0.92)" if dark else "rgba(255,255,255,0.92)"
        border_b = "1px solid rgba(255,255,255,0.08)" if dark else "1px solid #E2E8F0"
        back_btn = f'<button class="nav-btn" type="button" aria-label="Go back">{icon("arrow_back", size=18)}</button>' if back else '<div style="width:36px;"></div>'
        right_btn = f'<button class="nav-btn" type="button" aria-label="{right_icon or "action"}">{icon(right_icon, size=18)}</button>' if right_icon else '<div style="width:36px;"></div>'
        
        return f"""
        <nav class="nav-header" style="background:{bg};border-bottom:{border_b};color:{c};">
          {back_btn}
          <div class="nav-center">
            <h1 class="nav-title" style="color:{c};">{title}</h1>
            {f'<p class="nav-sub" style="color:{sub_c};">{sub}</p>' if sub else ''}
          </div>
          {right_btn}
        </nav>"""

    # Industry-Standard 5-Tab Navigation Bar
    def tabbar(active="Home"):
        tabs = [
            ("Home", "home"),
            ("Bookings", "confirmation_number"),
            ("Garage", "directions_car"),
            ("Wallet", "account_balance_wallet"),
            ("Profile", "person")
        ]
        items = []
        for t, ic in tabs:
            is_on = (t == active)
            cls = "active" if is_on else ""
            color = "#00685F" if is_on else "#565E74"
            items.append(f"""
            <div class="tab-item {cls}" style="color:{color};">
              {icon(ic, fill=is_on, size=21)}
              <span style="font-size:10px;font-weight:{'700' if is_on else '500'};margin-top:2px;">{t}</span>
            </div>""")
        return f'<footer class="bottom-tabbar">{"".join(items)}</footer>'

    def btn(label, kind="primary", extra="", icon_name=None, btn_id=None):
        ico_html = f'{icon(icon_name, size=18)} ' if icon_name else ""
        id_attr = f' id="{btn_id}"' if btn_id else ""
        return f'<button{id_attr} class="pro-btn {kind}" style="{extra}" type="button">{ico_html}<span>{label}</span></button>'

    def hsrp_badge(plate="KA 01 MJ 8821"):
        return f"""
        <div class="hsrp-plate-box">
          <div class="hsrp-flag">
            <div class="hsrp-chakra"></div>
            <span>IND</span>
          </div>
          <span class="hsrp-number">{plate}</span>
        </div>"""

    def onboarding_dots(step=1, total=3):
        dots = []
        for i in range(1, total + 1):
            if i == step:
                dots.append('<div class="carousel-dot active"></div>')
            else:
                dots.append('<div class="carousel-dot"></div>')
        return f'<div class="carousel-dots-row">{"".join(dots)}</div>'

    screens = []

    def add_screen(sid, title, stage_idx, stage_name, desc, inner_html, bg="#F8F9FF", iframe_link=None, dossier=None):
        screens.append({
            "id": sid,
            "title": title,
            "stage_idx": stage_idx,
            "stage_name": stage_name,
            "desc": desc,
            "html": inner_html,
            "bg": bg,
            "iframe_link": iframe_link,
            "dossier": dossier or {}
        })

    # ═══════════════════════════════════════════════════════════════════════════
    # STAGE 01: STANDARD LAUNCH & ONBOARDING (4 SCREENS)
    # ═══════════════════════════════════════════════════════════════════════════

    # STITCH-01: App Launch / Splash
    add_screen("STITCH-01", "App Launch & Splash", 1, "Launch & Onboarding",
        "Native branded launch screen with glowing teal ParkSpot glyph, tagline, and MoRTH/NPCI certification badge.",
        f"""
        <div class="hero-stage" style="flex:1;position:relative;background:#0B1C30;display:flex;flex-direction:column;justify-content:space-between;text-align:center;padding:0 24px 32px;">
          {status_bar(True)}
          <div style="flex:1;display:flex;flex-direction:column;align-items:center;justify-content:center;">
            <div class="splash-logo-container">
              <div class="splash-glow"></div>
              <div class="brand-pill large mb-4">
                <div class="brand-glyph">P</div>
                <div class="brand-text">Park<span>Spot</span></div>
              </div>
            </div>
            <p class="hero-tagline mt-2" style="color:#89F5E7;font-size:14px;font-weight:700;letter-spacing:0.04em;">
              Smart Urban Transit &amp; Guaranteed Parking
            </p>
            <p class="text-xs text-slate-400 max-w-[260px] mt-1">
              India's leading automated MLCP &amp; FASTag ingress mobility platform
            </p>
          </div>
          
          <div style="display:flex;flex-direction:column;align-items:center;gap:12px;">
            <div class="splash-spinner"></div>
            <div class="badge-chip navy border border-slate-700/60 text-[10px]">
              {icon("security", size=13, extra_style="color:#89F5E7;")} MoRTH &amp; NPCI NETC Certified
            </div>
          </div>
        </div>
        """, bg="#0B1C30", dossier={"intent": "Initial cold start & authentication state hydration", "spec": "Certifies MoRTH/NPCI compliance"})

    # STITCH-02: Onboarding 1 - Real-Time Discovery
    add_screen("STITCH-02", "Onboarding: Discover", 1, "Launch & Onboarding",
        "Step 1 of 3: Highlights real-time occupancy across 240+ facilities with upfront statutory pricing.",
        f"""
        {status_bar()}
        <div class="onboarding-top-bar">
          <span class="badge-chip teal">Step 1 of 3</span>
          <button type="button" class="skip-btn">Skip</button>
        </div>
        <div class="screen-body flex flex-col justify-between py-2">
          <div class="onboarding-hero-card">
            <img class="onboarding-img" src="{ASSETS['map']}" alt="City Parking Map"/>
            <div class="onboarding-overlay-card">
              <div class="flex items-center justify-between mb-1">
                <span class="font-bold text-xs text-on-surface">Forum South Mall MLCP</span>
                <span class="badge-chip ok">42 Bays Free</span>
              </div>
              <div class="flex items-center justify-between text-[11px] text-secondary">
                <span>0.4 km away • B2 Deck Live</span>
                <span class="font-bold text-[#00685F]">₹60/hr</span>
              </div>
            </div>
          </div>

          <div class="onboarding-content-block text-center px-4">
            <h2 class="text-xl font-bold text-on-surface mb-2">Find &amp; Compare Parking</h2>
            <p class="text-xs text-secondary leading-relaxed max-w-[280px] mx-auto">
              Discover real-time occupancy across 240+ verified multi-level garages, metro hubs, and curbside bays with transparent statutory tariffs.
            </p>
          </div>

          <div class="onboarding-footer px-2">
            {onboarding_dots(1, 3)}
            <div class="mt-5">
              {btn("Next • Bay Reservation", "primary", icon_name="arrow_forward")}
            </div>
          </div>
        </div>
        """, dossier={"intent": "User value education on live capacity & location discovery"})

    # STITCH-03: Onboarding 2 - Guaranteed Bay Reservation
    add_screen("STITCH-03", "Onboarding: Reserve", 1, "Launch & Onboarding",
        "Step 2 of 3: Explains 100% bay arrival certainty on interactive B2 architectural deck blueprints.",
        f"""
        {status_bar()}
        <div class="onboarding-top-bar">
          <span class="badge-chip teal">Step 2 of 3</span>
          <button type="button" class="skip-btn">Skip</button>
        </div>
        <div class="screen-body flex flex-col justify-between py-2">
          <div class="onboarding-hero-card">
            <img class="onboarding-img" src="{ASSETS['garage']}" alt="Reserved Parking Bay"/>
            <div class="onboarding-overlay-card">
              <div class="flex items-center justify-between mb-1">
                <span class="badge-chip ok">{icon("verified", size=13)} 100% Guaranteed Spot</span>
                <span class="badge-chip teal">Bay B2-14</span>
              </div>
              <div class="text-[11px] text-secondary">
                15-minute arrival lease hold secured before departure.
              </div>
            </div>
          </div>

          <div class="onboarding-content-block text-center px-4">
            <h2 class="text-xl font-bold text-on-surface mb-2">Guaranteed Bay Certainty</h2>
            <p class="text-xs text-secondary leading-relaxed max-w-[280px] mx-auto">
              Never circle busy streets again. Reserve your specific stall on our interactive architectural deck blueprints with EV fast charging support.
            </p>
          </div>

          <div class="onboarding-footer px-2">
            {onboarding_dots(2, 3)}
            <div class="mt-5">
              {btn("Next • Fast Ingress", "primary", icon_name="arrow_forward")}
            </div>
          </div>
        </div>
        """, dossier={"intent": "Arrival certainty value proposition & 15-minute lease hold"})

    # STITCH-04: Onboarding 3 - Contactless Ingress & Exit
    add_screen("STITCH-04", "Onboarding: Ingress", 1, "Launch & Onboarding",
        "Step 3 of 3: Showcases automated FASTag barrier lift and offline Ed25519 QR pass.",
        f"""
        {status_bar()}
        <div class="onboarding-top-bar">
          <span class="badge-chip teal">Step 3 of 3</span>
          <span class="text-xs text-secondary font-semibold">Complete</span>
        </div>
        <div class="screen-body flex flex-col justify-between py-2">
          <div class="onboarding-hero-card">
            <img class="onboarding-img" src="{ASSETS['city']}" alt="Contactless Gate Barrier"/>
            <div class="onboarding-overlay-card">
              <div class="flex items-center justify-between mb-1">
                <span class="font-bold text-xs text-on-surface">Contactless Boom Barrier</span>
                <span class="badge-chip ok">&lt; 1.2s Fast Lift</span>
              </div>
              <div class="flex items-center gap-2 text-[11px] text-secondary">
                <span class="text-[#006947] font-bold">{icon("toll", size=13)} FASTag ANPR</span>
                <span>•</span>
                <span class="text-[#00685F] font-bold">{icon("qr_code_2", size=13)} PassKit Offline QR</span>
              </div>
            </div>
          </div>

          <div class="onboarding-content-block text-center px-4">
            <h2 class="text-xl font-bold text-on-surface mb-2">Contactless Ingress &amp; Exit</h2>
            <p class="text-xs text-secondary leading-relaxed max-w-[280px] mx-auto">
              Drive right in without rolling down windows. Barriers auto-lift via FASTag or dynamic cryptographic QR pass, even in deep underground cellars.
            </p>
          </div>

          <div class="onboarding-footer px-2">
            {onboarding_dots(3, 3)}
            <div class="mt-5">
              {btn("Get Started Now", "primary", icon_name="check_circle")}
            </div>
          </div>
        </div>
        """, dossier={"intent": "Conversion to Auth Gateway & contactless gate technology"})

    # ═══════════════════════════════════════════════════════════════════════════
    # STAGE 02: AUTHENTICATION SUITE & LEGAL POLICIES (8 SCREENS)
    # ═══════════════════════════════════════════════════════════════════════════

    # STITCH-05: Welcome / Auth Gateway
    add_screen("STITCH-05", "Welcome & Gateway", 2, "Auth Suite",
        "Auth Gateway with primary Log In, secondary Register, Google & Apple OAuth, and DPDP legal footnote.",
        f"""
        <div class="hero-stage" style="flex:1;position:relative;background:#0B1C30;display:flex;flex-direction:column;justify-content:space-between;padding:24px 20px 32px;">
          <img class="img-cover" style="opacity:0.25;" src="{ASSETS['night']}" alt="City Night"/>
          <div class="hero-gradient-overlay"></div>
          {status_bar(True)}
          
          <div style="z-index:10;padding-top:20px;">
            <div class="brand-pill mb-3">
              <div class="brand-glyph">P</div>
              <div class="brand-text">Park<span>Spot</span></div>
            </div>
            <h2 class="hero-h1 text-2xl font-bold text-white leading-tight">
              Seamless parking for the modern driver.
            </h2>
            <p class="text-xs text-slate-300 mt-2 leading-relaxed">
              Join 120,000+ urban drivers saving 18 mins on every trip with guaranteed bay bookings and contactless gate passes.
            </p>
          </div>

          <div style="z-index:10;display:grid;gap:10px;">
            {btn("Log In to Account", "primary", icon_name="login")}
            {btn("Create New Account", "secondary", extra="background:rgba(255,255,255,0.08);color:#FFF;border-color:rgba(255,255,255,0.2);", icon_name="person_add")}
            
            <div class="auth-divider-row my-1">
              <div class="divider-line"></div>
              <span class="divider-text">OR CONTINUE WITH</span>
              <div class="divider-line"></div>
            </div>

            <div class="grid-2 gap-2">
              <button class="social-auth-btn" type="button">
                {icon("g_mobiledata", size=22, extra_style="color:#EA4335;")}
                <span>Google</span>
              </button>
              <button class="social-auth-btn" type="button">
                {icon("phone_iphone", size=18, extra_style="color:#000;")}
                <span>Apple</span>
              </button>
            </div>

            <p class="text-[10px] text-center text-slate-400 mt-2">
              By continuing, you agree to our <strong class="text-teal-container">Terms of Service</strong> &amp; <strong class="text-teal-container">Privacy Policy</strong> under DPDP Act 2023.
            </p>
          </div>
        </div>
        """, bg="#0B1C30", dossier={"intent": "Conversion gateway connecting returning and new drivers"})

    # STITCH-06: Standard Login Screen
    add_screen("STITCH-06", "Login Screen", 2, "Auth Suite",
        "Sign-in form with Email/Phone input, Password with eye icon visibility toggle, 'Forgot Password?' link, and Face ID biometrics.",
        f"""
        {status_bar()}
        {nav_header("Sign In", "Welcome Back")}
        <div class="screen-body space-y-4">
          <div>
            <h2 class="text-xl font-bold text-on-surface">Welcome Back</h2>
            <p class="text-xs text-secondary mt-0.5">Sign in to manage your garage, bookings, and FastTag passes.</p>
          </div>

          <div class="card p-4 space-y-3.5">
            <div>
              <label class="input-label" for="stitch-login-id">EMAIL OR MOBILE NUMBER</label>
              <div class="input-field">
                {icon("mail", size=18, extra_style="color:#565E74;")}
                <input id="stitch-login-id" name="stitch_login_id" type="text" value="mahesh.giri@example.com" readonly/>
              </div>
            </div>

            <div>
              <div class="flex items-center justify-between mb-1">
                <label class="input-label mb-0" for="stitch-login-pwd">PASSWORD</label>
                <span class="text-[11px] font-bold text-[#00685F] cursor-pointer">Forgot Password?</span>
              </div>
              <div class="input-field">
                {icon("lock", size=18, extra_style="color:#565E74;")}
                <input id="stitch-login-pwd" name="stitch_login_pwd" type="password" value="••••••••••••" style="letter-spacing:2px;" readonly/>
                <button type="button" class="eye-toggle-btn" aria-label="Toggle password visibility">
                  {icon("visibility", size=18, extra_style="color:#565E74;")}
                </button>
              </div>
            </div>

            <div class="flex items-center justify-between pt-1">
              <label class="flex items-center gap-2 cursor-pointer">
                <input type="checkbox" id="stitch-rem-chk" checked class="accent-[#00685F] w-4 h-4 rounded"/>
                <span class="text-xs text-secondary">Remember device</span>
              </label>
              <div class="flex items-center gap-1 text-xs font-semibold text-[#00685F] cursor-pointer">
                {icon("fingerprint", size=16)} Face ID
              </div>
            </div>
          </div>

          <div class="card p-3 bg-slate-50 border border-slate-200/60 flex items-center gap-2.5">
            <div class="icon-circle teal">{icon("sms", size=16)}</div>
            <div class="flex-1 min-w-0">
              <div class="text-xs font-bold text-on-surface">Prefer passwordless?</div>
              <div class="text-[11px] text-secondary">Sign in instantly via 6-digit WhatsApp/SMS OTP.</div>
            </div>
            <button class="pro-btn secondary sm" type="button">Use OTP</button>
          </div>
        </div>
        <div class="sticky-footer">
          {btn("Log In", "primary", icon_name="login")}
          <div class="text-center mt-3 text-xs text-secondary">
            Don't have an account? <strong class="text-[#00685F] cursor-pointer">Sign Up</strong>
          </div>
        </div>
        """, dossier={"intent": "Authenticate driver identity with password visibility toggle & biometrics"})

    # STITCH-07: Standard Register Screen
    add_screen("STITCH-07", "Register / Sign Up", 2, "Auth Suite",
        "Driver registration with Full Name, Phone (+91), GST-compliant Email, Password strength meter, and DPDP consent checkbox.",
        f"""
        {status_bar()}
        {nav_header("Create Account", "Driver Registration")}
        <div class="screen-body space-y-3">
          <div>
            <h2 class="text-xl font-bold text-on-surface">Create Account</h2>
            <p class="text-xs text-secondary mt-0.5">Experience guaranteed urban parking in 240+ facilities.</p>
          </div>

          <div class="card p-3.5 space-y-2.5">
            <div>
              <label class="input-label" for="stitch-reg-name">FULL LEGAL NAME</label>
              <div class="input-field">
                {icon("person", size=18, extra_style="color:#565E74;")}
                <input id="stitch-reg-name" name="stitch_reg_name" type="text" value="Mahesh Giri" readonly/>
              </div>
            </div>

            <div>
              <label class="input-label" for="stitch-reg-phone">MOBILE PHONE NUMBER</label>
              <div class="phone-input-row">
                <div class="phone-prefix">
                  <span class="flag-icon">🇮🇳</span>
                  <span>+91</span>
                </div>
                <input id="stitch-reg-phone" name="stitch_reg_phone" class="phone-text-input" type="text" value="98765 43210" readonly/>
              </div>
            </div>

            <div>
              <label class="input-label" for="stitch-reg-email">EMAIL ADDRESS (FOR GST TAX INVOICES)</label>
              <div class="input-field">
                {icon("mail", size=18, extra_style="color:#565E74;")}
                <input id="stitch-reg-email" name="stitch_reg_email" type="email" value="mahesh.giri@example.com" readonly/>
              </div>
            </div>

            <div>
              <label class="input-label" for="stitch-reg-pwd">SET SECURE PASSWORD</label>
              <div class="input-field">
                {icon("lock", size=18, extra_style="color:#565E74;")}
                <input id="stitch-reg-pwd" name="stitch_reg_pwd" type="password" value="••••••••••••" style="letter-spacing:2px;" readonly/>
                <button type="button" class="eye-toggle-btn" aria-label="Toggle password visibility">
                  {icon("visibility", size=18, extra_style="color:#565E74;")}
                </button>
              </div>
              <div class="strength-meter-bar mt-1.5">
                <div class="strength-segment active"></div>
                <div class="strength-segment active"></div>
                <div class="strength-segment active"></div>
                <div class="strength-segment"></div>
              </div>
              <div class="text-[10px] text-emerald-700 font-semibold mt-1">Strong password: 8+ chars, numbers &amp; symbols.</div>
            </div>
          </div>

          <div class="agreement-box active p-2.5">
            <label class="flex items-start gap-2.5 cursor-pointer">
              <input type="checkbox" id="stitch-reg-consent" checked class="accent-[#00685F] w-4 h-4 rounded mt-0.5"/>
              <div class="text-[11px] text-secondary leading-normal">
                I agree to the <strong class="text-[#00685F]">Terms of Service</strong> and acknowledge the <strong class="text-[#00685F]">DPDP Privacy Policy</strong> for FASTag &amp; HSRP plate processing.
              </div>
            </label>
          </div>
        </div>
        <div class="sticky-footer">
          {btn("Create Driver Account", "primary", icon_name="person_add")}
          <div class="text-center mt-2.5 text-xs text-secondary">
            Already registered? <strong class="text-[#00685F] cursor-pointer">Log In</strong>
          </div>
        </div>
        """, dossier={"intent": "New account onboarding adhering to DPDP Act 2023 consent mandate"})

    # STITCH-08: Forgot Password - Step 1
    add_screen("STITCH-08", "Forgot Password: Step 1", 2, "Auth Suite",
        "Account recovery request by registered email address or mobile phone number.",
        f"""
        {status_bar()}
        {nav_header("Forgot Password", "Account Recovery")}
        <div class="screen-body space-y-4">
          <div class="text-center py-2">
            <div class="w-14 h-14 rounded-2xl bg-teal-50 border border-teal-200 flex items-center justify-center mx-auto mb-3 text-[#00685F]">
              {icon("lock_reset", size=32)}
            </div>
            <h2 class="text-xl font-bold text-on-surface">Reset Password</h2>
            <p class="text-xs text-secondary mt-1 max-w-[280px] mx-auto">
              Enter the email address or phone registered with your ParkSpot account to receive a 6-digit OTP code.
            </p>
          </div>

          <div class="card p-4 space-y-3">
            <div>
              <label class="input-label" for="stitch-fp-id">REGISTERED EMAIL OR MOBILE</label>
              <div class="input-field">
                {icon("contact_mail", size=18, extra_style="color:#565E74;")}
                <input id="stitch-fp-id" name="stitch_fp_id" type="text" value="mahesh.giri@example.com" readonly/>
              </div>
            </div>

            <div class="legal-trust-banner">
              {icon("verified_user", size=15, extra_style="color:#00685F;flex-shrink:0;")}
              <p>Verification link will expire in 10 minutes to protect your account and garage access.</p>
            </div>
          </div>
        </div>
        <div class="sticky-footer">
          {btn("Send 6-Digit Code", "primary", icon_name="send")}
          <div class="text-center mt-3 text-xs text-secondary">
            Remember password? <strong class="text-[#00685F] cursor-pointer">Back to Log In</strong>
          </div>
        </div>
        """, dossier={"intent": "Initiate password reset via verified channel"})

    # STITCH-09: Forgot Password - Step 2 (Verify OTP)
    add_screen("STITCH-09", "Forgot Password: Step 2", 2, "Auth Suite",
        "6-digit cryptographic verification OTP input with 38-second resend timer and WhatsApp fallback.",
        f"""
        {status_bar()}
        {nav_header("Verify OTP Code", "mahesh.giri@example.com")}
        <div class="screen-body text-center space-y-4">
          <div>
            <div class="icon-circle teal mx-auto mb-2">{icon("mark_email_read", size=24)}</div>
            <h2 class="text-xl font-bold text-on-surface">Enter 6-Digit Code</h2>
            <p class="text-xs text-secondary mt-1">We sent an authentication code to <strong>mahesh***@example.com</strong></p>
          </div>

          <div class="card p-5">
            <div class="otp-boxes-row">
              <div class="otp-cell filled">4</div>
              <div class="otp-cell filled">8</div>
              <div class="otp-cell filled">2</div>
              <div class="otp-cell filled">1</div>
              <div class="otp-cell filled">9</div>
              <div class="otp-cell active">|</div>
            </div>

            <div class="resend-row mt-4">
              <span class="text-secondary text-xs">Resend code in <strong class="text-on-surface">0:38</strong></span>
              <span class="text-divider">•</span>
              <span class="whatsapp-link">{icon("chat", size=14)} WhatsApp fallback</span>
            </div>
          </div>

          <div class="card p-3 bg-slate-50 border border-slate-200/60 text-left text-xs text-secondary flex items-center gap-2">
            {icon("info", size=16, extra_style="color:#00685F;flex-shrink:0;")}
            <span>Check spam folder if code does not arrive within 30 seconds.</span>
          </div>
        </div>
        <div class="sticky-footer">
          {btn("Verify & Continue", "primary", icon_name="check")}
        </div>
        """, dossier={"intent": "Authenticate identity via time-based 6-digit OTP"})

    # STITCH-10: Forgot Password - Step 3 (Set New Password)
    add_screen("STITCH-10", "Forgot Password: Step 3", 2, "Auth Suite",
        "Enter new password and confirm password with 3 live validation checks and session security revocation.",
        f"""
        {status_bar()}
        {nav_header("Set New Password", "Secure Your Account")}
        <div class="screen-body space-y-3.5">
          <div>
            <h2 class="text-xl font-bold text-on-surface">Set New Password</h2>
            <p class="text-xs text-secondary mt-0.5">Your new password must be distinct from previously used credentials.</p>
          </div>

          <div class="card p-4 space-y-3">
            <div>
              <label class="input-label" for="stitch-new-pwd">NEW PASSWORD</label>
              <div class="input-field">
                {icon("lock", size=18, extra_style="color:#565E74;")}
                <input id="stitch-new-pwd" name="stitch_new_pwd" type="password" value="••••••••••••" style="letter-spacing:2px;" readonly/>
                <button type="button" class="eye-toggle-btn" aria-label="Toggle password visibility">
                  {icon("visibility", size=18, extra_style="color:#565E74;")}
                </button>
              </div>
            </div>

            <div>
              <label class="input-label" for="stitch-conf-pwd">CONFIRM NEW PASSWORD</label>
              <div class="input-field">
                {icon("check_circle", size=18, extra_style="color:#006947;")}
                <input id="stitch-conf-pwd" name="stitch_conf_pwd" type="password" value="••••••••••••" style="letter-spacing:2px;" readonly/>
              </div>
            </div>

            <div class="space-y-1.5 pt-1">
              <div class="flex items-center gap-1.5 text-xs text-emerald-800 font-semibold">
                {icon("check", size=14)} Minimum 8 characters
              </div>
              <div class="flex items-center gap-1.5 text-xs text-emerald-800 font-semibold">
                {icon("check", size=14)} Contains at least 1 number &amp; uppercase letter
              </div>
              <div class="flex items-center gap-1.5 text-xs text-emerald-800 font-semibold">
                {icon("check", size=14)} Passwords match
              </div>
            </div>
          </div>

          <div class="card p-3 bg-emerald-50 border border-emerald-200 text-xs text-emerald-950 flex items-center gap-2">
            {icon("shield", size=16, extra_style="color:#006947;flex-shrink:0;")}
            <span>All active sessions on older devices will be logged out securely.</span>
          </div>
        </div>
        <div class="sticky-footer">
          {btn("Update Password & Log In", "primary", icon_name="task_alt")}
        </div>
        """, dossier={"intent": "Finalize credential rotation and return to authenticated session"})

    # STITCH-11: Terms of Service
    add_screen("STITCH-11", "Terms of Service", 2, "Auth Suite",
        "Dedicated Master Service Agreement screen detailing 15-min arrival hold, SAC 999113 tariffs, and overstay rules.",
        f"""
        {status_bar()}
        {nav_header("Terms of Service", "Effective Date: Oct 24, 2026")}
        <div class="screen-body space-y-3.5 text-xs leading-relaxed text-secondary">
          <div class="badge-chip navy">ParkSpot Master Service Agreement v5.0</div>
          
          <div class="card p-3.5 space-y-2">
            <h3 class="font-bold text-sm text-on-surface">1. Scope &amp; Parking Leases</h3>
            <p>ParkSpot facilitates guaranteed bay leases between property operators and vehicle drivers. A confirmed reservation grants exclusive ingress rights for the allocated vehicle license plate (HSRP) during the active lease window.</p>
          </div>

          <div class="card p-3.5 space-y-2">
            <h3 class="font-bold text-sm text-on-surface">2. 15-Minute Guaranteed Arrival Hold</h3>
            <p>For Advance Bookings, your designated bay (e.g. B2-14) is locked exclusively. If arrival does not occur within 15 minutes of the start time, the bay hold converts to floating facility admission or cancellation per statutory SLA.</p>
          </div>

          <div class="card p-3.5 space-y-2">
            <h3 class="font-bold text-sm text-on-surface">3. Statutory Tariffs &amp; GST Invoicing</h3>
            <p>All quotes strictly follow SAC 999113 for Supporting Services in Transport: Base Parking Fee + ₹5 Platform Convenience Fee + 18% GST (9% CGST + 9% SGST). Formal tax invoices are issued immediately post-exit.</p>
          </div>

          <div class="card p-3.5 space-y-2">
            <h3 class="font-bold text-sm text-on-surface">4. Overstay Settlement &amp; AutoPay</h3>
            <p>Vehicles exceeding dwell duration without in-app extension are billed at standard rack rates via registered UPI AutoPay or FASTag NETC toll clearance upon barrier exit.</p>
          </div>

          <div class="card p-3.5 space-y-2">
            <h3 class="font-bold text-sm text-on-surface">5. Governing Law</h3>
            <p>Disputes are subject to the exclusive jurisdiction of the competent courts in Bengaluru, Karnataka, India.</p>
          </div>
        </div>
        <div class="sticky-footer">
          {btn("I Accept Terms of Service", "primary", icon_name="check")}
        </div>
        """, dossier={"intent": "Master Spec legal compliance & lease hold terms"})

    # STITCH-12: Privacy Policy & DPDP
    add_screen("STITCH-12", "Privacy Policy & DPDP", 2, "Auth Suite",
        "Dedicated Data Protection notice detailing SHA-256 HSRP plate tokenization, 30-day ANPR purge, and Data Principal rights.",
        f"""
        {status_bar()}
        {nav_header("Privacy & DPDP Notice", "Data Protection Act 2023")}
        <div class="screen-body space-y-3 text-xs leading-relaxed text-secondary">
          <div class="badge-chip teal">ISO/IEC 27001 &amp; DPDP 2023 Certified</div>

          <div class="card p-3.5 space-y-2">
            <h3 class="font-bold text-sm text-on-surface">1. Data Collected &amp; Purpose</h3>
            <p>ParkSpot collects vehicle HSRP license plate numbers, FASTag EPC tags, driver contact credentials, and telemetry at gate boom barriers solely for automated ingress clearance and statutory GST invoicing.</p>
          </div>

          <div class="card p-3.5 space-y-2">
            <h3 class="font-bold text-sm text-on-surface">2. Plate Hash Tokenization</h3>
            <p>License plate images captured by ANPR cameras are converted to cryptographic SHA-256 hashes within 60 seconds. Raw imagery is securely purged after 30 days pursuant to municipal smart-city mandates.</p>
          </div>

          <div class="card p-3.5 space-y-2">
            <h3 class="font-bold text-sm text-on-surface">3. Data Principal Rights</h3>
            <p>Under India's Digital Personal Data Protection Act 2023, you retain full rights to: (a) Access stored vehicle records, (b) Correct inaccuracies, (c) Request erasure of non-statutory dwell history, and (d) Nominate a representative.</p>
          </div>

          <div class="card p-3.5 space-y-2">
            <h3 class="font-bold text-sm text-on-surface">4. Grievance Redressal Officer</h3>
            <p>For inquiries or data erasure requests: <strong>dpo@parkspot.in</strong> • Officer: S. Ramachandran, Bengaluru, KA 560001.</p>
          </div>
        </div>
        <div class="sticky-footer">
          {btn("Acknowledge & Continue", "primary", icon_name="verified_user")}
        </div>
        """, dossier={"intent": "DPDP Act 2023 statutory privacy disclosures"})

    # ═══════════════════════════════════════════════════════════════════════════
    # STAGE 03: FLAGSHIP 5-TAB BOTTOM NAVIGATION SUITE (5 SCREENS)
    # ═══════════════════════════════════════════════════════════════════════════

    # STITCH-TAB1: Tab 1 - Home
    add_screen("STITCH-TAB1", "Tab 1: Home (Flagship)", 3, "Flagship 5-Tabs",
        "Primary landing screen: Current city selector, Search HUD, Quick category chips, Active session live card, and Recommended garages carousel.",
        f"""
        {status_bar()}
        <header class="home-app-bar">
          <div class="location-pill">
            {icon("location_on", fill=True, size=16, extra_style="color:#00685F;")}
            <div class="text-left">
              <div class="text-[9px] uppercase font-bold text-secondary">CURRENT CITY</div>
              <div class="font-bold text-xs text-on-surface flex items-center gap-1">
                Bengaluru • MG Road {icon("expand_more", size=14)}
              </div>
            </div>
          </div>
          <div class="flex items-center gap-2">
            <button type="button" class="icon-circle slate" aria-label="Notifications" style="position:relative;">
              {icon("notifications", size=18)}
              <span class="notification-badge-dot"></span>
            </button>
            <div class="avatar-circle">MG</div>
          </div>
        </header>

        <div class="screen-body space-y-3.5 pt-2">
          <!-- Search HUD -->
          <div class="search-hud-bar">
            {icon("search", size=20, extra_style="color:#00685F;")}
            <input id="stitch-home-search" name="stitch_home_search" type="text" placeholder="Search destination, mall, metro station..." value="" readonly/>
            <button type="button" class="filter-tune-btn" aria-label="Open Filters">
              {icon("tune", size=16)}
            </button>
          </div>

          <!-- Category Filter Chips -->
          <div class="category-chips-row">
            <div class="chip active">{icon("near_me", size=14)} Near Me (24)</div>
            <div class="chip">{icon("roofing", size=14)} Covered Deck</div>
            <div class="chip">{icon("electric_bolt", size=14)} EV Fast (60kW)</div>
            <div class="chip">{icon("airline_stops", size=14)} Valet</div>
            <div class="chip">{icon("flight", size=14)} Airport FASTag</div>
          </div>

          <!-- Live Active Booking Banner -->
          <div class="card p-3.5 border-2 border-[#00685F] bg-gradient-to-r from-teal-50 to-white">
            <div class="flex items-center justify-between mb-1.5">
              <span class="badge-chip ok">{icon("timer", size=13)} Active Session</span>
              <span class="badge-chip teal">Bay B2-14</span>
            </div>
            <div class="font-bold text-sm text-on-surface">Forum South Mall MLCP</div>
            <div class="flex items-center justify-between text-xs text-secondary mt-1">
              <span>Dwell: <strong>01:24:18 left</strong></span>
              <span class="font-bold text-[#00685F] cursor-pointer">View Pass &amp; QR →</span>
            </div>
          </div>

          <!-- Recommended Garages Carousel -->
          <div>
            <div class="flex items-center justify-between mb-2">
              <h3 class="font-bold text-sm text-on-surface">Recommended Garages</h3>
              <span class="text-xs font-bold text-[#00685F] cursor-pointer">View Map</span>
            </div>

            <div class="facility-mini-card mb-2">
              <img class="mini-card-thumb" src="{ASSETS['facility']}" alt="Forum South Mall"/>
              <div class="flex-1 min-w-0">
                <div class="flex items-center justify-between">
                  <h4 class="font-bold text-xs text-on-surface truncate">Forum South Mall Deck</h4>
                  <span class="badge-chip ok">42 Free</span>
                </div>
                <p class="text-[11px] text-secondary mt-0.5">0.4 km • B2 Blueprint Live • 2.1m clearance</p>
                <div class="flex items-center justify-between mt-1 pt-1 border-t border-slate-100">
                  <span class="font-bold text-xs text-[#00685F]">₹60/hr</span>
                  <button class="pro-btn primary sm" type="button">Book Bay</button>
                </div>
              </div>
            </div>

            <div class="facility-mini-card">
              <img class="mini-card-thumb" src="{ASSETS['garage_stock']}" alt="Brigade World Trade"/>
              <div class="flex-1 min-w-0">
                <div class="flex items-center justify-between">
                  <h4 class="font-bold text-xs text-on-surface truncate">Brigade World Trade Hub</h4>
                  <span class="badge-chip teal">18 Free</span>
                </div>
                <p class="text-[11px] text-secondary mt-0.5">1.2 km • 60kW DC Fast EV Chargers</p>
                <div class="flex items-center justify-between mt-1 pt-1 border-t border-slate-100">
                  <span class="font-bold text-xs text-[#00685F]">₹50/hr</span>
                  <button class="pro-btn secondary sm" type="button">Reserve</button>
                </div>
              </div>
            </div>
          </div>

          <!-- Quick Actions Grid -->
          <div class="grid-4 gap-2 text-center pt-1">
            <div class="quick-action-pill">
              <div class="action-icon-box">{icon("qr_code_scanner", size=20)}</div>
              <span>Scan QR</span>
            </div>
            <div class="quick-action-pill">
              <div class="action-icon-box">{icon("directions_car", size=20)}</div>
              <span>My Garage</span>
            </div>
            <div class="quick-action-pill">
              <div class="action-icon-box">{icon("credit_card", size=20)}</div>
              <span>Monthly Pass</span>
            </div>
            <div class="quick-action-pill">
              <div class="action-icon-box">{icon("support_agent", size=20)}</div>
              <span>SOS Help</span>
            </div>
          </div>
        </div>
        {tabbar("Home")}
        """, dossier={"intent": "Daily driver dashboard with search HUD and active dwell telemetry"})

    # STITCH-TAB2: Tab 2 - Bookings
    add_screen("STITCH-TAB2", "Tab 2: Bookings (Flagship)", 3, "Flagship 5-Tabs",
        "Segmented reservations hub (Active, Upcoming, History) with countdown timer and one-tap digital pass access.",
        f"""
        {status_bar()}
        {nav_header("My Bookings", "Active & Past Reservations", back=False, right_icon="history")}
        <div class="screen-body space-y-3">
          <div class="segmented-control">
            <div class="seg-btn active">Active (1)</div>
            <div class="seg-btn">Upcoming (1)</div>
            <div class="seg-btn">Past (14)</div>
          </div>

          <div class="card p-4 border-2 border-[#00685F] space-y-3">
            <div class="flex items-center justify-between">
              <span class="badge-chip ok">{icon("check_circle", size=13)} Ingress Active</span>
              <span class="badge-chip navy">Bay B2-14</span>
            </div>

            <div>
              <h3 class="font-bold text-base text-on-surface">Forum South Mall MLCP</h3>
              <p class="text-xs text-secondary">Basement Deck B2 • Sector 2B • Near Pillar C3</p>
            </div>

            {hsrp_badge("KA 01 MJ 8821")}

            <div class="dwell-mini-status p-3 bg-slate-50 rounded-xl flex items-center justify-between">
              <div>
                <div class="text-[10px] text-secondary font-bold uppercase">REMAINING LEASE</div>
                <div class="text-lg font-bold text-[#00685F] font-mono">01:24:18</div>
              </div>
              <button class="pro-btn primary sm" type="button">Show QR Pass</button>
            </div>

            <div class="flex gap-2">
              <button class="pro-btn secondary sm flex-1" type="button">{icon("near_me", size=14)} Bay Nav</button>
              <button class="pro-btn secondary sm flex-1" type="button">{icon("more_time", size=14)} Extend</button>
            </div>
          </div>

          <div class="card p-3.5 space-y-2">
            <div class="flex items-center justify-between">
              <span class="badge-chip navy">Tomorrow 09:30 AM</span>
              <span class="text-xs font-bold text-on-surface">2 Hours</span>
            </div>
            <h4 class="font-bold text-sm text-on-surface">Brigade World Trade Hub</h4>
            <p class="text-xs text-secondary">Reserved Bay A-08 • 60kW EV Fast Charger Plugged</p>
            <div class="flex items-center justify-between pt-1 border-t border-slate-100 text-xs">
              <span class="text-secondary font-mono">₹76.70 pre-authorized</span>
              <span class="font-bold text-[#00685F] cursor-pointer">Modify</span>
            </div>
          </div>
        </div>
        {tabbar("Bookings")}
        """, dossier={"intent": "Manage active parking sessions, upcoming holds, and past tax receipts"})

    # STITCH-TAB3: Tab 3 - Garage
    add_screen("STITCH-TAB3", "Tab 3: Garage (Flagship)", 3, "Flagship 5-Tabs",
        "Vehicle garage passport: HSRP number plates (KA 01 MJ 8821), Tata Nexon EV profile, and FASTag NETC linked status.",
        f"""
        {status_bar()}
        {nav_header("Vehicle Garage", "Linked HSRP Passports & FASTag", back=False, right_icon="add")}
        <div class="screen-body space-y-3">
          <div class="card p-4 border-2 border-[#00685F] bg-[#00685F]/[0.02] space-y-2.5">
            <div class="flex items-center justify-between">
              <div class="flex items-center gap-2">
                <span class="font-bold text-sm text-on-surface">Tata Nexon EV Max</span>
                <span class="badge-chip teal">Default</span>
              </div>
              <span class="badge-chip ok">{icon("electric_bolt", size=13)} EV Fast</span>
            </div>

            {hsrp_badge("KA 01 MJ 8821")}

            <div class="grid-3 gap-2 pt-2 border-t border-slate-100 text-center text-xs">
              <div class="bg-slate-50 p-2 rounded-lg">
                <div class="text-[9px] text-secondary font-bold">HEIGHT</div>
                <div class="font-bold text-on-surface mt-0.5">1.62m</div>
              </div>
              <div class="bg-slate-50 p-2 rounded-lg">
                <div class="text-[9px] text-secondary font-bold">FASTAG</div>
                <div class="font-bold text-[#006947] mt-0.5">NETC Linked</div>
              </div>
              <div class="bg-slate-50 p-2 rounded-lg">
                <div class="text-[9px] text-secondary font-bold">PORT</div>
                <div class="font-bold text-on-surface mt-0.5">CCS-2</div>
              </div>
            </div>
          </div>

          <div class="card p-3.5 space-y-2">
            <div class="flex items-center justify-between">
              <span class="font-bold text-sm text-on-surface">Honda Activa 6G</span>
              <span class="badge-chip slate">2-Wheeler</span>
            </div>
            {hsrp_badge("KA 05 EQ 2490")}
            <div class="flex items-center justify-between text-xs text-secondary pt-1 border-t border-slate-100">
              <span>Two-Wheeler Tariff Eligible</span>
              <span class="text-[#00685F] font-bold cursor-pointer">Set as Default</span>
            </div>
          </div>

          <div class="card p-3 bg-slate-50 border border-slate-200/60 flex items-center justify-between">
            <div class="flex items-center gap-2.5">
              <div class="icon-circle teal">{icon("toll", size=18)}</div>
              <div>
                <div class="text-xs font-bold text-on-surface">FASTag Auto-Billing</div>
                <div class="text-[10px] text-secondary">National Electronic Toll Collection</div>
              </div>
            </div>
            <div class="ios-switch on"></div>
          </div>
        </div>
        <div class="sticky-footer">
          {btn("Register Another Vehicle", "secondary", icon_name="add_circle")}
        </div>
        {tabbar("Garage")}
        """, dossier={"intent": "Manage linked vehicle passports and automated FASTag clearance"})

    # STITCH-TAB4: Tab 4 - Wallet
    add_screen("STITCH-TAB4", "Tab 4: Wallet (Flagship)", 3, "Flagship 5-Tabs",
        "Driver financial center: ₹840 available balance, Monthly Metro Pass card, UPI AutoPay status, and transaction ledger.",
        f"""
        {status_bar()}
        {nav_header("ParkSpot Wallet", "Cash, Passes & AutoPay", back=False, right_icon="qr_code")}
        <div class="screen-body space-y-3.5">
          <div class="wallet-balance-card">
            <div class="text-[10px] text-slate-300 font-bold uppercase tracking-wider">AVAILABLE BALANCE</div>
            <div class="text-2xl font-bold font-mono mt-1 text-white">₹840.00</div>
            <p class="text-[11px] text-slate-200 mt-0.5">Instant refunds &amp; contactless barrier tolls</p>
            <div class="flex gap-2 mt-3.5">
              <button class="pro-btn sm bg-white text-[#0B1C30] font-bold" type="button">+ Add Funds</button>
              <button class="pro-btn sm bg-white/10 text-white border border-white/20" type="button">Refund / Withdraw</button>
            </div>
          </div>

          <div class="monthly-pass-card">
            <div class="flex justify-between items-start">
              <div>
                <span class="badge-chip teal text-[9px] mb-1">ALL-ACCESS PASS</span>
                <h3 class="text-sm font-bold text-white">Bengaluru Metro Executive</h3>
                <p class="text-[11px] text-slate-300">Valid in 14 MLCP Transit Garages</p>
              </div>
              {icon("verified", size=22, extra_style="color:#89F5E7;")}
            </div>
            <div class="flex items-center justify-between text-xs mt-3 pt-2 border-t border-white/10 text-slate-300">
              <span>Expires: 15 Nov 2026</span>
              <span class="font-mono text-teal-container">22 Days Left</span>
            </div>
          </div>

          <div class="card p-3 flex items-center justify-between">
            <div class="flex items-center gap-2.5">
              <div class="icon-circle teal">{icon("autorenew", size=18)}</div>
              <div>
                <div class="text-xs font-bold text-on-surface">UPI AutoPay Active</div>
                <div class="text-[10px] text-secondary">Linked via PhonePe • Cap ₹500/day</div>
              </div>
            </div>
            <span class="badge-chip ok">Active</span>
          </div>

          <div>
            <div class="flex items-center justify-between mb-2">
              <h3 class="font-bold text-xs text-on-surface">Recent Transactions</h3>
              <span class="text-[11px] text-[#00685F] font-bold cursor-pointer">Full Ledger</span>
            </div>
            <div class="space-y-1.5 text-xs">
              <div class="card p-2.5 flex items-center justify-between">
                <div>
                  <div class="font-bold text-on-surface">Forum South Mall MLCP</div>
                  <div class="text-[10px] text-secondary">24 Oct 2026 • SAC 999113</div>
                </div>
                <div class="text-right">
                  <div class="font-bold text-rose-700">-₹76.70</div>
                  <div class="text-[10px] text-[#00685F] cursor-pointer">Tax Invoice</div>
                </div>
              </div>
              <div class="card p-2.5 flex items-center justify-between">
                <div>
                  <div class="font-bold text-on-surface">Auto-Topup (UPI PhonePe)</div>
                  <div class="text-[10px] text-secondary">20 Oct 2026 • Ref #UPI8892</div>
                </div>
                <div class="text-right">
                  <div class="font-bold text-emerald-700">+₹500.00</div>
                  <div class="text-[10px] text-secondary">Success</div>
                </div>
              </div>
            </div>
          </div>
        </div>
        {tabbar("Wallet")}
        """, dossier={"intent": "Wallet top-up, recurring passes, and pre-authorized overstay balance"})

    # STITCH-TAB5: Tab 5 - Profile
    add_screen("STITCH-TAB5", "Tab 5: Profile (Flagship)", 3, "Flagship 5-Tabs",
        "Driver account and governance: Monogram avatar, KYC verified badge, GSTIN details, and DPDP privacy desk.",
        f"""
        {status_bar()}
        {nav_header("Driver Profile", "Account & Preferences", back=False, right_icon="settings")}
        <div class="screen-body space-y-3.5">
          <div class="card p-4 flex items-center gap-3.5">
            <div class="w-14 h-14 rounded-2xl bg-gradient-to-br from-[#00685F] to-[#0B1C30] text-white flex items-center justify-center font-bold text-lg">
              MG
            </div>
            <div class="flex-1 min-w-0">
              <div class="flex items-center gap-1.5">
                <h3 class="font-bold text-sm text-on-surface">Mahesh Giri</h3>
                {icon("verified", size=16, extra_style="color:#00685F;")}
              </div>
              <p class="text-xs text-secondary mt-0.5">+91 98765 43210</p>
              <span class="badge-chip ok mt-1">KYC &amp; FASTag Verified</span>
            </div>
          </div>

          <div class="card overflow-hidden divide-y divide-slate-100">
            <div class="p-3 flex items-center justify-between cursor-pointer hover:bg-slate-50">
              <div class="flex items-center gap-2.5">
                <div class="icon-circle teal">{icon("directions_car", size=18)}</div>
                <span class="text-xs font-bold text-on-surface">My Vehicles &amp; HSRP Plates</span>
              </div>
              {icon("chevron_right", size=18, extra_style="color:#565E74;")}
            </div>

            <div class="p-3 flex items-center justify-between cursor-pointer hover:bg-slate-50">
              <div class="flex items-center gap-2.5">
                <div class="icon-circle teal">{icon("receipt_long", size=18)}</div>
                <span class="text-xs font-bold text-on-surface">GSTIN &amp; Tax Invoices</span>
              </div>
              {icon("chevron_right", size=18, extra_style="color:#565E74;")}
            </div>

            <div class="p-3 flex items-center justify-between cursor-pointer hover:bg-slate-50">
              <div class="flex items-center gap-2.5">
                <div class="icon-circle teal">{icon("language", size=18)}</div>
                <span class="text-xs font-bold text-on-surface">Language (English / हिन्दी / ಕನ್ನಡ)</span>
              </div>
              {icon("chevron_right", size=18, extra_style="color:#565E74;")}
            </div>

            <div class="p-3 flex items-center justify-between cursor-pointer hover:bg-slate-50">
              <div class="flex items-center gap-2.5">
                <div class="icon-circle teal">{icon("shield", size=18)}</div>
                <span class="text-xs font-bold text-on-surface">DPDP Privacy &amp; Data Rights Desk</span>
              </div>
              {icon("chevron_right", size=18, extra_style="color:#565E74;")}
            </div>

            <div class="p-3 flex items-center justify-between cursor-pointer hover:bg-slate-50">
              <div class="flex items-center gap-2.5">
                <div class="icon-circle danger">{icon("logout", size=18)}</div>
                <span class="text-xs font-bold text-rose-700">Log Out of ParkSpot</span>
              </div>
              {icon("chevron_right", size=18, extra_style="color:#BA1A1A;")}
            </div>
          </div>
        </div>
        {tabbar("Profile")}
        """, dossier={"intent": "User account settings, statutory GST compliance & data privacy controls"})

    # ═══════════════════════════════════════════════════════════════════════════
    # STAGE 04: VEHICLE PASSPORT & HEIGHT CLEARANCE (2 SCREENS)
    # ═══════════════════════════════════════════════════════════════════════════

    # STITCH-18: Add Vehicle Sheet
    add_screen("STITCH-18", "Add Vehicle Form", 4, "Vehicle & Garage",
        "Add vehicle form: 6 vehicle classes, HSRP plate input, EV toggle, and automated classification.",
        f"""
        {status_bar()}
        {nav_header("Add Vehicle", "Class & License Plate")}
        <div class="screen-body space-y-3.5">
          <div>
            <label class="input-label">VEHICLE CLASSIFICATION (6 CLASSES)</label>
            <div class="grid-3">
              <div class="class-card">{icon("pedal_bike", size=20)}<span>Cycle</span></div>
              <div class="class-card">{icon("two_wheeler", size=20)}<span>2W</span></div>
              <div class="class-card active">{icon("directions_car", size=20)}<span>Car</span></div>
              <div class="class-card">{icon("electric_rickshaw", size=20)}<span>Auto</span></div>
              <div class="class-card">{icon("airport_shuttle", size=20)}<span>SUV</span></div>
              <div class="class-card">{icon("local_shipping", size=20)}<span>Truck</span></div>
            </div>
          </div>
          
          <div>
            <label class="input-label" for="add-v-plate">HSRP NUMBER PLATE</label>
            <div class="input-field">
              {icon("pin", size=18, extra_style="color:#565E74;")}
              <input id="add-v-plate" name="add_v_plate" type="text" value="KA 01 MJ 8821" style="font-family:'Share Tech Mono', monospace; font-size:16px; font-weight:700;" readonly/>
            </div>
            <p class="text-[10px] text-secondary mt-1">Standard state code + RTO + series + 4 digits.</p>
          </div>
          
          <div class="card p-3 flex items-center justify-between">
            <div class="flex items-center gap-2.5">
              <div class="icon-circle teal">{icon("electric_bolt", size=18)}</div>
              <div>
                <div class="font-bold text-xs">Electric Vehicle (EV)</div>
                <div class="text-[10px] text-secondary">Enable EV Charging bay filters</div>
              </div>
            </div>
            <div class="ios-switch"></div>
          </div>
        </div>
        <div class="sticky-footer">
          {btn("Save Vehicle to Garage", "primary", icon_name="check")}
        </div>
        {tabbar("Garage")}
        """, dossier={"intent": "Register vehicle and bind HSRP license plate with VAHAN validation"})

    # STITCH-19: Height Clearance Telemetry
    add_screen("STITCH-19", "Clearance Telemetry", 4, "Vehicle & Garage",
        "Vehicle height check (1.62m vs 2.10m deck clearance) and ramp gradient verification before arrival.",
        f"""
        {status_bar()}
        {nav_header("Compatibility Check", "Forum South Mall Deck B2")}
        <div class="screen-body space-y-3">
          <div class="card p-4 text-center">
            <div class="w-12 h-12 rounded-full bg-emerald-100 text-[#006947] flex items-center justify-center mx-auto mb-2">
              {icon("verified", size=24)}
            </div>
            <h3 class="font-bold text-base text-emerald-950">100% Fit &amp; Clear</h3>
            <p class="text-xs text-emerald-800 mt-1">Tata Nexon EV Max is fully cleared for Level B2 subterranean ingress.</p>
          </div>

          <div class="card p-3.5 space-y-2.5 text-xs">
            <div class="flex justify-between items-center py-1 border-b border-slate-100">
              <span class="text-secondary">Vehicle Height:</span>
              <span class="font-bold text-on-surface">1.62 meters</span>
            </div>
            <div class="flex justify-between items-center py-1 border-b border-slate-100">
              <span class="text-secondary">Ramp Overhead Clearance:</span>
              <span class="font-bold text-[#006947]">2.10 meters (Safe +0.48m)</span>
            </div>
            <div class="flex justify-between items-center py-1 border-b border-slate-100">
              <span class="text-secondary">Turning Radius Required:</span>
              <span class="font-bold text-on-surface">5.1m (Deck ramp provides 6.4m)</span>
            </div>
            <div class="flex justify-between items-center py-1">
              <span class="text-secondary">FASTag Reader Compatibility:</span>
              <span class="font-bold text-[#006947]">NETC Compliant</span>
            </div>
          </div>
        </div>
        <div class="sticky-footer">
          {btn("Proceed to Bay Selection", "primary", icon_name="arrow_forward")}
        </div>
        {tabbar("Garage")}
        """, dossier={"intent": "Prevent in-garage height accidents and verify turning radius"})

    # ═══════════════════════════════════════════════════════════════════════════
    # STAGE 05: MAP DISCOVERY & SEARCH HUD (2 SCREENS)
    # ═══════════════════════════════════════════════════════════════════════════

    # STITCH-20: Vector Transit Map (Existing screen-1-map-explore)
    add_screen("STITCH-20", "Vector Transit Map", 5, "Map & Search HUD",
        "Interactive vector transit basemap with live radar pulse pins, 5-tab bottom navigation, and facility preview card.",
        f"""
        <div style="flex:1;position:relative;background:#E2E8F0;overflow:hidden;">
          <img class="img-cover" src="{ASSETS['map']}" alt="City Map Base"/>
          {status_bar()}

          <div style="position:absolute;top:54px;left:16px;right:16px;z-index:20;">
            <div class="search-hud-bar">
              {icon("search", size=20, extra_style="color:#00685F;")}
              <input id="map-explore-input" name="map_explore" type="text" value="Forum South Mall, Bengaluru" readonly/>
              <button type="button" class="filter-tune-btn" aria-label="Open Filters">{icon("tune", size=16)}</button>
            </div>
          </div>

          <div style="position:absolute;top:40%;left:52%;transform:translate(-50%,-100%);z-index:20;cursor:pointer;">
            <div class="map-pin-bubble active">
              <span class="font-bold">₹60</span>
              <span class="text-[9px]">• 42 free</span>
            </div>
            <div class="map-pin-stem"></div>
          </div>

          <div style="position:absolute;bottom:72px;left:12px;right:12px;z-index:20;">
            <div class="card p-3.5 shadow-xl border-2 border-[#00685F] bg-white">
              <div class="flex items-center justify-between mb-1">
                <span class="badge-chip ok">42 Bays Free</span>
                <span class="badge-chip teal">Level B2 Live</span>
              </div>
              <div class="font-bold text-sm text-on-surface">Forum South Mall MLCP</div>
              <div class="flex items-center justify-between text-xs text-secondary mt-1">
                <span>0.4 km away • 2.1m clearance</span>
                <span class="font-bold text-[#00685F]">₹60/hr</span>
              </div>
              <div class="mt-2.5">
                {btn("Select & View B2 Blueprint", "primary", icon_name="map")}
              </div>
            </div>
          </div>

          {tabbar("Home")}
        </div>
        """, iframe_link="screen-1-map-explore.html", dossier={"intent": "Cartographic map discovery with real-time occupancy radar markers"})

    # STITCH-21: Contextual Filters
    add_screen("STITCH-21", "Contextual Filters", 5, "Map & Search HUD",
        "Filter facilities by amenities: Covered deck, 60kW DC EV fast chargers, disabled access, and price range.",
        f"""
        {status_bar()}
        {nav_header("Filter Garages", "Reset All", right_icon="restart_alt")}
        <div class="screen-body space-y-4">
          <div>
            <label class="input-label">GARAGE AMENITIES</label>
            <div class="grid-2 gap-2">
              <div class="selection-pill active">
                {icon("roofing", size=16)}
                <span>Covered Deck</span>
                {icon("check", size=14, extra_style="color:#00685F;margin-left:auto;")}
              </div>
              <div class="selection-pill active">
                {icon("electric_bolt", size=16)}
                <span>EV Fast (60kW)</span>
                {icon("check", size=14, extra_style="color:#00685F;margin-left:auto;")}
              </div>
              <div class="selection-pill">
                {icon("accessible", size=16)}
                <span>Disabled Stall</span>
              </div>
              <div class="selection-pill">
                {icon("toll", size=16)}
                <span>FASTag Ingress</span>
              </div>
            </div>
          </div>

          <div>
            <label class="input-label">MAXIMUM HOURLY RATE (₹)</label>
            <div class="card p-3">
              <div class="flex justify-between text-xs font-bold mb-2">
                <span>Up to ₹80/hr</span>
                <span class="text-[#00685F]">₹60/hr selected</span>
              </div>
              <div class="w-full bg-slate-200 h-2 rounded-full overflow-hidden">
                <div class="bg-[#00685F] h-full w-3/4"></div>
              </div>
            </div>
          </div>
        </div>
        <div class="sticky-footer">
          {btn("Apply Filters (18 Facilities)", "primary", icon_name="check")}
        </div>
        {tabbar("Home")}
        """, dossier={"intent": "Filter facilities to narrow down guaranteed parking options"})

    # ═══════════════════════════════════════════════════════════════════════════
    # STAGE 06: FACILITY TELEMETRY & B2 BLUEPRINT (2 SCREENS)
    # ═══════════════════════════════════════════════════════════════════════════

    # STITCH-22: Facility Detail Hero (screen-2-facility-detail)
    add_screen("STITCH-22", "Facility Telemetry", 6, "Facility & B2 Blueprint",
        "Live ultrasonic slot counters, height clearance (2.1m), amenities, and Deck B2 zone selector.",
        f"""
        {status_bar()}
        <div class="hero-stage" style="height:180px;position:relative;">
          <img class="img-cover" src="{ASSETS['facility']}" alt="Forum South Mall"/>
          <div class="hero-gradient-overlay"></div>
          <div style="position:absolute;top:10px;left:12px;z-index:20;">
            <button class="nav-btn" type="button" aria-label="Go back">{icon("arrow_back", size=18)}</button>
          </div>
          <div style="position:absolute;bottom:12px;left:16px;right:16px;z-index:20;color:#FFF;">
            <span class="badge-chip teal mb-1">MLCP Smart Facility</span>
            <h2 class="text-base font-bold text-white">Forum South Mall MLCP</h2>
            <p class="text-[11px] text-slate-200">Kanakapura Road, Konanakunte, Bengaluru</p>
          </div>
        </div>
        <div class="screen-body space-y-3 pt-3">
          <div class="card p-3 grid-3 text-center text-xs">
            <div>
              <div class="text-[10px] text-secondary font-bold">TOTAL CAPACITY</div>
              <div class="font-bold text-sm text-on-surface mt-0.5">240 Bays</div>
            </div>
            <div>
              <div class="text-[10px] text-secondary font-bold">CLEARANCE</div>
              <div class="font-bold text-sm text-[#006947] mt-0.5">2.10m Max</div>
            </div>
            <div>
              <div class="text-[10px] text-secondary font-bold">BASE TARIFF</div>
              <div class="font-bold text-sm text-[#00685F] mt-0.5">₹60/hr</div>
            </div>
          </div>

          <div class="card p-3.5 space-y-2">
            <div class="font-bold text-xs text-on-surface">Available Decks &amp; Zones</div>
            <div class="space-y-1.5 text-xs">
              <div class="p-2 bg-slate-50 rounded-lg flex items-center justify-between border border-[#00685F]">
                <span class="font-bold text-on-surface">Deck B2 (Underground Basement)</span>
                <span class="badge-chip ok">42 Bays Free</span>
              </div>
              <div class="p-2 bg-slate-50 rounded-lg flex items-center justify-between">
                <span class="text-secondary">Deck B1 (Valet &amp; High-Clearance)</span>
                <span class="badge-chip warn">8 Bays Free</span>
              </div>
            </div>
          </div>
        </div>
        <div class="sticky-footer">
          {btn("Select Level B2 Deck Bay", "primary", icon_name="grid_view")}
        </div>
        """, iframe_link="screen-2-facility-detail.html", dossier={"intent": "Inspect facility capacity, clearance limits, and live sensor freshness"})

    # STITCH-23: Interactive B2 Blueprint (screen-3-deck-selector)
    add_screen("STITCH-23", "Deck B2 Blueprint", 6, "Facility & B2 Blueprint",
        "2D architectural blueprint deck selector: Bay B2-14 locked with 60kW EV charging indicator.",
        f"""
        {status_bar()}
        {nav_header("Deck B2 Blueprint", "Bay Selection", right_icon="info")}
        <div class="screen-body space-y-2.5">
          <div class="flex items-center justify-between text-xs px-1">
            <span class="font-bold text-on-surface">Sector 2B Grid</span>
            <div class="flex gap-2">
              <span class="flex items-center gap-1 text-[10px] text-secondary"><span class="w-2.5 h-2.5 rounded bg-emerald-500"></span> Free</span>
              <span class="flex items-center gap-1 text-[10px] text-secondary"><span class="w-2.5 h-2.5 rounded bg-slate-400"></span> Taken</span>
              <span class="flex items-center gap-1 text-[10px] text-secondary"><span class="w-2.5 h-2.5 rounded bg-[#00685F]"></span> Selected</span>
            </div>
          </div>

          <div class="blueprint-grid-canvas">
            <div class="bay-cell taken">B2-11</div>
            <div class="bay-cell taken">B2-12</div>
            <div class="bay-cell free">B2-13</div>
            <div class="bay-cell selected">B2-14</div>
            <div class="bay-cell free">B2-15</div>
            <div class="bay-cell taken">B2-16</div>
          </div>

          <div class="card p-3.5 border-2 border-[#00685F] bg-teal-50/40">
            <div class="flex items-center justify-between mb-1">
              <div class="flex items-center gap-1.5">
                <span class="badge-chip teal">Selected Bay B2-14</span>
                <span class="badge-chip ok">EV 60kW</span>
              </div>
              <span class="font-bold text-xs text-[#00685F]">₹60/hr</span>
            </div>
            <p class="text-[11px] text-secondary">Extra wide stall (2.8m) • 12m from Lift Lobby C.</p>
          </div>
        </div>
        <div class="sticky-footer">
          {btn("Lock Bay B2-14 • Proceed", "primary", icon_name="lock")}
        </div>
        """, iframe_link="screen-3-deck-selector.html", dossier={"intent": "Select specific bay with 100% arrival certainty"})

    # ═══════════════════════════════════════════════════════════════════════════
    # STAGE 07: STATUTORY QUOTE & 1-TAP UPI (2 SCREENS)
    # ═══════════════════════════════════════════════════════════════════════════

    # STITCH-24: Statutory Quote (₹76.70) (screen-4-checkout-quote)
    add_screen("STITCH-24", "Statutory Quote (₹76.70)", 7, "Quote ₹76.70 & UPI",
        "Strict Master Spec v3.0 financial invariant breakdown under GST SAC 999113: ₹60 + ₹5 + ₹5.85 + ₹5.85 = ₹76.70.",
        f"""
        {status_bar()}
        {nav_header("Booking Summary", "Statutory Tariff Quote")}
        <div class="screen-body space-y-3 text-xs">
          <div class="card p-3.5">
            <div class="font-bold text-sm text-on-surface">Forum South Mall MLCP • Bay B2-14</div>
            <p class="text-secondary mt-0.5">Tata Nexon EV Max • KA 01 MJ 8821</p>
            <div class="badge-chip teal mt-2">1 Hour Lease • 15-min arrival hold</div>
          </div>

          <div class="card p-3.5 space-y-2">
            <div class="font-bold text-on-surface pb-1 border-b border-slate-100">Itemized Tax Breakdown (SAC 999113)</div>
            <div class="flex justify-between text-secondary">
              <span>Base Parking Fee (1 Hr):</span>
              <span class="font-mono text-on-surface font-semibold">₹60.00</span>
            </div>
            <div class="flex justify-between text-secondary">
              <span>Platform Convenience Fee:</span>
              <span class="font-mono text-on-surface font-semibold">₹5.00</span>
            </div>
            <div class="flex justify-between text-secondary">
              <span>CGST (9.0% on ₹65.00):</span>
              <span class="font-mono text-on-surface font-semibold">₹5.85</span>
            </div>
            <div class="flex justify-between text-secondary">
              <span>SGST (9.0% on ₹65.00):</span>
              <span class="font-mono text-on-surface font-semibold">₹5.85</span>
            </div>
            <div class="flex justify-between text-sm font-bold text-on-surface pt-2 border-t border-slate-200">
              <span>Total Payable Amount:</span>
              <span class="font-mono text-[#00685F] text-base">₹76.70</span>
            </div>
          </div>
        </div>
        <div class="sticky-footer">
          {btn("Proceed to 1-Tap UPI (₹76.70)", "primary", icon_name="lock")}
        </div>
        """, iframe_link="screen-4-checkout-quote.html", dossier={"intent": "Itemized tax invoice preview prior to checkout", "invariant": "₹60 base + ₹5 fee + ₹5.85 CGST + ₹5.85 SGST = ₹76.70 SAC 999113"})

    # STITCH-25: 1-Tap UPI Checkout
    add_screen("STITCH-25", "1-Tap UPI Checkout", 7, "Quote ₹76.70 & UPI",
        "UPI payment selector: Google Pay, PhonePe, Paytm, and AutoPay pre-authorization consent.",
        f"""
        {status_bar()}
        {nav_header("Select Payment", "Pay ₹76.70")}
        <div class="screen-body space-y-3 text-xs">
          <div class="card p-3.5 flex justify-between items-center bg-teal-50 border border-teal-200">
            <div>
              <div class="text-[10px] text-teal-800 font-bold uppercase">TOTAL PAYABLE</div>
              <div class="font-mono text-xl font-bold text-[#00685F]">₹76.70</div>
            </div>
            <span class="badge-chip ok">GST SAC 999113</span>
          </div>

          <div class="card overflow-hidden divide-y divide-slate-100">
            <div class="p-3 flex items-center justify-between cursor-pointer border-[#00685F] border">
              <div class="flex items-center gap-2.5">
                <span class="font-bold text-sm text-on-surface">Google Pay UPI</span>
                <span class="badge-chip teal">Fastest</span>
              </div>
              {icon("radio_button_checked", size=18, extra_style="color:#00685F;")}
            </div>

            <div class="p-3 flex items-center justify-between cursor-pointer">
              <span class="font-bold text-sm text-on-surface">PhonePe UPI</span>
              {icon("radio_button_unchecked", size=18, extra_style="color:#565E74;")}
            </div>
          </div>
        </div>
        <div class="sticky-footer">
          {btn("Pay ₹76.70 with GPay", "primary", icon_name="lock")}
        </div>
        """, dossier={"intent": "Single-tap payment checkout via NPCI UPI ecosystem"})

    # ═══════════════════════════════════════════════════════════════════════════
    # STAGE 08: INGRESS & ACTIVE DWELL (3 SCREENS)
    # ═══════════════════════════════════════════════════════════════════════════

    # STITCH-26: Dynamic PassKit Pass (screen-5-active-pass)
    add_screen("STITCH-26", "Dynamic QR Gate Pass", 8, "Ingress & Active Dwell",
        "Active digital pass: Cryptographic Ed25519 single-use QR nonce, HSRP plate badge, and 15-min countdown.",
        f"""
        {status_bar()}
        {nav_header("Active Gate Pass", "Forum South Mall Deck B2")}
        <div class="screen-body space-y-3 text-center">
          <div class="card p-4 space-y-3 border-2 border-[#00685F]">
            <div class="flex items-center justify-between">
              <span class="badge-chip ok">ACTIVE INGRESS PASS</span>
              <span class="badge-chip navy">Bay B2-14</span>
            </div>

            <div class="qr-box p-3 bg-white border border-slate-200 rounded-xl inline-block mx-auto">
              <img class="w-36 h-36 mx-auto" src="{ASSETS['qr']}" alt="Cryptographic QR Pass"/>
            </div>

            <div class="text-xs text-secondary font-mono">PASS-ED25519-88192</div>
            {hsrp_badge("KA 01 MJ 8821")}
          </div>
        </div>
        <div class="sticky-footer">
          {btn("Start Turn-by-Turn Wayfinding", "primary", icon_name="navigation")}
        </div>
        """, iframe_link="screen-5-active-pass.html", dossier={"intent": "Digital boarding pass for gate barrier ingress"})

    # STITCH-27: Barrier Gate Auto-Lift (screen-6-barrier-clearance)
    add_screen("STITCH-27", "Barrier Gate Clearance", 8, "Ingress & Active Dwell",
        "FASTag ANPR boom barrier clearance (<1.2s handshake) and turn-by-turn ramp HUD to Deck B2.",
        f"""
        {status_bar()}
        {nav_header("Boom Barrier Auto-Lift", "FASTag Handshake < 1.2s")}
        <div class="screen-body space-y-4 text-center p-4">
          <div class="w-16 h-16 rounded-full bg-emerald-100 text-[#006947] flex items-center justify-center mx-auto">
            {icon("check_circle", size=36)}
          </div>
          <h3 class="text-lg font-bold text-emerald-950">Barrier Raising</h3>
          <p class="text-xs text-secondary">FASTag NETC EPC recognized. Drive forward to B2 ramp.</p>
        </div>
        """, iframe_link="screen-6-barrier-clearance.html", dossier={"intent": "Barrier gate clearance event confirmation"})

    # STITCH-28: Active Dwell Session Ring
    add_screen("STITCH-28", "Active Dwell Session", 8, "Ingress & Active Dwell",
        "Real-time dwell timer ring (01:24:18 left), accumulated tariff, 60kW EV charging status, and one-tap extension.",
        f"""
        {status_bar()}
        {nav_header("Live Session", "Forum South Mall B2-14")}
        <div class="screen-body space-y-3 text-center">
          <div class="card p-4 space-y-3">
            <div class="dwell-countdown-ring mx-auto">
              <span class="text-xs text-secondary font-bold">REMAINING</span>
              <span class="text-2xl font-bold text-on-surface font-mono">01:24:18</span>
              <span class="text-[10px] text-teal-800 font-semibold">Ends 16:30 IST</span>
            </div>
            <div class="text-xs text-secondary">Bay B2-14 • Sector 2B</div>
          </div>
        </div>
        <div class="sticky-footer flex gap-2">
          {btn("Extend Time", "secondary", extra="flex:1;", icon_name="more_time")}
          {btn("End & Exit Gate", "primary", extra="flex:1.2;", icon_name="door_open")}
        </div>
        """, dossier={"intent": "Dwell session tracking with overstay prevention controls"})

    # ═══════════════════════════════════════════════════════════════════════════
    # STAGE 09: TAX INVOICING & INCIDENT RECOVERY (2 SCREENS)
    # ═══════════════════════════════════════════════════════════════════════════

    # STITCH-29: Statutory GST Tax Invoice
    add_screen("STITCH-29", "Session Tax Invoice", 9, "Tax Invoice & SOS",
        "Statutory GST Tax Invoice #PS-2026-88192 under SAC 999113: ₹76.70 breakdown with GSTIN and download link.",
        f"""
        {status_bar()}
        {nav_header("Tax Invoice", "SAC 999113 • #PS-2026-88192")}
        <div class="screen-body space-y-3 text-xs">
          <div class="card p-4 space-y-2">
            <div class="flex justify-between font-bold border-b pb-1">
              <span>Total Paid (UPI):</span>
              <span class="font-mono text-[#00685F]">₹76.70</span>
            </div>
            <div class="text-[11px] text-secondary">
              GSTIN: 29AABCP1928K1Z5<br/>
              Base: ₹60.00 • Fee: ₹5.00<br/>
              CGST: ₹5.85 • SGST: ₹5.85
            </div>
          </div>
        </div>
        <div class="sticky-footer">
          {btn("Download GST Invoice PDF", "primary", icon_name="download")}
        </div>
        """, dossier={"intent": "Statutory GST invoice generation and corporate expense download"})

    # STITCH-30: SOS Bay Occupied Resolution
    add_screen("STITCH-30", "SOS Bay Occupied SLA", 9, "Tax Invoice & SOS",
        "Dispute resolver: Instant automated stall reallocation to Bay B2-15 plus ₹100 SLA goodwill wallet credit.",
        f"""
        {status_bar()}
        {nav_header("SLA Resolved", "Reassigned to Bay B2-15")}
        <div class="screen-body space-y-3 text-center">
          <div class="card p-4 bg-emerald-50 border border-emerald-200">
            <h4 class="font-bold text-base text-emerald-950">New Bay: STALL B2-15</h4>
            <p class="text-xs text-emerald-800 mt-1">Adjacent stall allocated in Sector 2B. Gate credential updated automatically.</p>
          </div>
          <div class="card p-3.5 text-left text-xs">
            <div class="font-bold text-on-surface">SLA Goodwill Compensation</div>
            <p class="text-secondary mt-0.5">₹100 goodwill credit added to your ParkSpot wallet for the inconvenience.</p>
          </div>
        </div>
        <div class="sticky-footer">
          {btn("Navigate to Bay B2-15", "primary", icon_name="near_me")}
        </div>
        """, dossier={"intent": "Incident recovery and SLA compensation for seamless driver trust"})


    # --- STAGE 10: FLOATING DRIVE-IN & METERED DWELL (3 SCREENS) ---
    add_screen("STITCH-31", "Drive-In Ingress Alert", 10, "Floating Drive-In",
        "Unannounced drive-in detection: ANPR camera detects plate at Gate 2 Lane 01 and opens floating session.",
        f"""
        {status_bar()}
        {nav_header("Ingress Detected", "Gate 2 • Lane 01")}
        <div class="screen-body space-y-3">
          <div class="card p-3.5 bg-teal-50 border border-teal-200 flex items-center justify-between">
            <div class="flex items-center gap-2">
              <div class="w-2.5 h-2.5 rounded-full bg-emerald-500 animate-pulse"></div>
              <span class="font-bold text-xs text-teal-950">FASTag Boom Barrier Lifted</span>
            </div>
            <span class="badge-chip ok">&lt; 1.1s Handshake</span>
          </div>

          <div class="card p-4 space-y-3">
            <div class="text-[10px] font-bold text-secondary uppercase">IDENTIFIED VEHICLE</div>
            <div class="flex items-center justify-between">
              <div>
                <div class="font-bold text-base text-on-surface">Tata Nexon EV</div>
                <div class="text-xs text-secondary font-mono">KA 01 MJ 8821</div>
              </div>
              <span class="badge-chip teal">FASTag NETC Active</span>
            </div>
            
            <div class="pt-2 border-t border-slate-100 flex items-center justify-between text-xs text-secondary">
              <span>Entry Timestamp:</span>
              <span class="font-bold text-on-surface">Today, 10:42 AM</span>
            </div>
            <div class="flex items-center justify-between text-xs text-secondary">
              <span>Applicable Rack Tariff:</span>
              <span class="font-bold text-[#00685F]">₹60/1st hr + ₹30/subsequent 30m</span>
            </div>
          </div>

          <div class="card p-3.5 bg-slate-50 border border-slate-200/60 text-xs space-y-1.5">
            <div class="font-bold text-on-surface flex items-center gap-1.5">
              <span class="material-symbols-outlined text-[16px] text-teal-600">navigation</span> Assigned Floating Zones
            </div>
            <p class="text-secondary leading-relaxed">
              Proceed down the ramp to <strong>Deck B1 (Valet &amp; Floating)</strong> or <strong>Deck B2 (Underground)</strong>. Park in any stall with a green ceiling sensor.
            </p>
          </div>
        </div>
        <div class="sticky-footer">
          {btn("Open Live Metered Session", "primary", icon_name="timer")}
        </div>
        """, dossier={"intent": "Spec §4.2 Pay-as-you-go floating ingress without prior reservation", "spec": "FASTag ANPR Auto-Clearance"})

    add_screen("STITCH-32", "Live Metered Session HUD", 10, "Floating Drive-In",
        "Live running dwell meter: Duration ticker, real-time tariff accumulation, and pre-payment exit voucher.",
        f"""
        {status_bar()}
        {nav_header("Live Session Meter", "Forum South Mall MLCP")}
        <div class="screen-body space-y-3.5 text-center">
          <div class="card p-5">
            <div class="text-[10px] font-bold text-secondary uppercase tracking-wider">ACTIVE DWELL TIME</div>
            <div class="meter-ticker my-1">01:14:22</div>
            <div class="text-xs text-secondary">Entry: 10:42 AM • Gate 2 (Lane 01)</div>

            <div class="mt-4 pt-3 border-t border-slate-100 text-left space-y-2 text-xs">
              <div class="flex justify-between text-secondary">
                <span>Base 1st Hour:</span>
                <span class="font-bold text-on-surface">₹60.00</span>
              </div>
              <div class="flex justify-between text-secondary">
                <span>Subsequent 30m Block (Partially Used):</span>
                <span class="font-bold text-on-surface">₹30.00</span>
              </div>
              <div class="flex justify-between text-secondary">
                <span>Convenience Platform Fee:</span>
                <span class="font-bold text-on-surface">₹5.00</span>
              </div>
              <div class="flex justify-between text-secondary">
                <span>GST (18% SAC 999113):</span>
                <span class="font-bold text-on-surface">₹17.10</span>
              </div>
              <div class="flex justify-between text-sm font-bold text-on-surface pt-2 border-t border-slate-200">
                <span>Current Payable Amount:</span>
                <span class="font-mono text-[#00685F] text-base">₹112.10</span>
              </div>
            </div>
          </div>

          <div class="card p-3 bg-amber-50 border border-amber-200 text-left text-xs text-amber-950 flex items-start gap-2">
            <span class="material-symbols-outlined text-[16px] text-amber-600 shrink-0 mt-0.5">tips_and_updates</span>
            <p>Pay now before walking to your car to get <strong>15 minutes free exit grace</strong> at the boom barrier.</p>
          </div>
        </div>
        <div class="sticky-footer">
          {btn("Pay ₹112.10 & Get Exit Pass", "primary", icon_name="check_circle")}
        </div>
        """, dossier={"intent": "Transparent live billing ticker preventing exit barrier delay", "spec": "SAC 999113 Metered Tariff"})

    add_screen("STITCH-33", "FASTag Auto-Debit Exit", 10, "Floating Drive-In",
        "Contactless barrier exit: NETC FASTag clearance (<1.2s), automated fee deduction, and GST receipt.",
        f"""
        {status_bar()}
        {nav_header("Exit Clearance", "Boom Barrier Lifted")}
        <div class="screen-body space-y-3.5 text-center">
          <div class="w-16 h-16 rounded-full bg-emerald-50 border-2 border-emerald-400 text-[#006947] flex items-center justify-center mx-auto mb-1">
            <span class="material-symbols-outlined text-[36px]">toll</span>
          </div>
          
          <div>
            <h2 class="text-xl font-bold text-on-surface">Exit Cleared via FASTag</h2>
            <p class="text-xs text-secondary mt-0.5">Gate 4 (Lane 02 Exit) • Boom barrier raised in 1.18s</p>
          </div>

          <div class="card p-4 text-left space-y-2.5 text-xs">
            <div class="flex justify-between pb-2 border-b border-slate-100">
              <span class="text-secondary">Total Dwell Duration:</span>
              <span class="font-bold text-on-surface">1 hr 48 min</span>
            </div>
            <div class="flex justify-between">
              <span class="text-secondary">Vehicle HSRP:</span>
              <span class="font-mono font-bold text-on-surface">KA 01 MJ 8821</span>
            </div>
            <div class="flex justify-between">
              <span class="text-secondary">Payment Method:</span>
              <span class="font-bold text-[#00685F]">ICICI Bank FASTag Auto-Debit</span>
            </div>
            <div class="flex justify-between">
              <span class="text-secondary">NPCI Reference ID:</span>
              <span class="font-mono text-slate-500">NETC-2026-9948210385</span>
            </div>
            <div class="flex justify-between pt-2 border-t border-slate-200 text-sm font-bold text-on-surface">
              <span>Total Deducted:</span>
              <span class="font-mono text-[#00685F]">₹141.60</span>
            </div>
          </div>

          <div class="badge-chip ok py-2 px-3 text-xs w-full justify-center">
            <span class="material-symbols-outlined text-[15px]">verified</span> Formal GST Tax Invoice Sent to Email
          </div>
        </div>
        <div class="sticky-footer">
          {btn("Done • Return to Home", "primary", icon_name="home")}
        </div>
        """, dossier={"intent": "Frictionless barrier lift without roll-down window interaction", "spec": "NPCI NETC FASTag Clearing"})

    # --- STAGE 11: EXTENSION & CONFLICT MANAGEMENT (3 SCREENS) ---
    add_screen("STITCH-34", "Session Extension Sheet", 11, "Extension & Conflict",
        "Self-service duration extension: Real-time bay occupancy check, duration chips, and 1-tap quote recalculation.",
        f"""
        {status_bar()}
        {nav_header("Extend Parking", "Bay B2-14")}
        <div class="screen-body space-y-3.5">
          <div class="card p-3.5 bg-teal-50 border border-teal-200 flex items-center justify-between text-xs">
            <div>
              <div class="font-bold text-teal-950">Current Expiry: 12:30 PM</div>
              <div class="text-teal-800 text-[11px] mt-0.5">01:24:18 remaining in active lease</div>
            </div>
            <span class="badge-chip ok">Bay Available</span>
          </div>

          <div>
            <label class="input-label">SELECT ADDITIONAL EXTENSION</label>
            <div class="grid-3 gap-2">
              <div class="class-card">
                <span class="text-xs font-bold">+30 Mins</span>
                <span class="text-[10px] text-secondary">until 01:00 PM</span>
                <span class="font-bold text-[#00685F] mt-1">₹35.40</span>
              </div>
              <div class="class-card active">
                <span class="text-xs font-bold">+1 Hour</span>
                <span class="text-[10px] text-[#00685F]">until 01:30 PM</span>
                <span class="font-bold text-[#00685F] mt-1">₹70.80</span>
              </div>
              <div class="class-card">
                <span class="text-xs font-bold">+2 Hours</span>
                <span class="text-[10px] text-secondary">until 02:30 PM</span>
                <span class="font-bold text-[#00685F] mt-1">₹141.60</span>
              </div>
            </div>
          </div>

          <div class="card p-3.5 space-y-2 text-xs">
            <div class="font-bold text-on-surface pb-1 border-b border-slate-100">Extension Price Breakdown</div>
            <div class="flex justify-between text-secondary">
              <span>Additional 1-Hr Base:</span>
              <span class="font-mono text-on-surface">₹60.00</span>
            </div>
            <div class="flex justify-between text-secondary">
              <span>CGST (9%) + SGST (9%):</span>
              <span class="font-mono text-on-surface">₹10.80</span>
            </div>
            <div class="flex justify-between font-bold text-sm text-on-surface pt-2 border-t border-slate-200">
              <span>Total to Pay:</span>
              <span class="font-mono text-[#00685F]">₹70.80</span>
            </div>
          </div>
        </div>
        <div class="sticky-footer">
          {btn("1-Tap Pay & Extend (+1 Hr)", "primary", icon_name="update")}
        </div>
        """, dossier={"intent": "Spec §4.4 Driver-initiated parking lease extension", "spec": "Dynamic Availability Validation"})

    add_screen("STITCH-35", "Extension Conflict & Relocate", 11, "Extension & Conflict",
        "Incoming reservation conflict: Bay B2-14 booked by incoming driver; automated relocation to Deck B1 Floating Zone.",
        f"""
        {status_bar()}
        {nav_header("Extension Notice", "Bay Conflict Detected")}
        <div class="screen-body space-y-3.5">
          <div class="card p-4 bg-amber-50 border border-amber-200">
            <div class="badge-chip warn mb-2">
              <span class="material-symbols-outlined text-[13px]">warning</span> Bay Reserved by Incoming Driver
            </div>
            <div class="font-bold text-sm text-amber-950">Extension Denied for Bay B2-14</div>
            <p class="text-xs text-amber-900 mt-1 leading-relaxed">
              Another driver holds a confirmed reservation for <strong>Bay B2-14 starting at 01:30 PM</strong>. Under our Guaranteed Bay SLA, this stall cannot be extended.
            </p>
          </div>

          <div class="card p-4 space-y-2.5 text-xs">
            <div class="font-bold text-sm text-on-surface">Automated Resolution Options</div>
            
            <div class="p-3 bg-teal-50/70 border border-teal-300 rounded-xl cursor-pointer">
              <div class="flex items-center justify-between mb-1">
                <span class="font-bold text-teal-950">Option 1: Relocate to Deck B1 (Floating)</span>
                <span class="badge-chip ok">18 Bays Free</span>
              </div>
              <p class="text-teal-800 text-[11px] leading-relaxed">
                Move your car to any vacant stall on Level B1 before 01:15 PM and continue parking for as long as you need.
              </p>
            </div>

            <div class="p-3 bg-slate-50 border border-slate-200 rounded-xl cursor-pointer">
              <div class="flex items-center justify-between mb-1">
                <span class="font-bold text-on-surface">Option 2: Depart by 12:30 PM</span>
                <span class="text-slate-500 font-mono text-[11px]">No Extra Charge</span>
              </div>
              <p class="text-secondary text-[11px] leading-relaxed">
                Exit before your original scheduled lease end. No relocation required.
              </p>
            </div>
          </div>
        </div>
        <div class="sticky-footer">
          {btn("Accept Relocation to Deck B1", "primary", icon_name="swap_horiz")}
        </div>
        """, dossier={"intent": "Spec §4.4 Fair allocation preventing bay hoarding over advance reservations", "spec": "Guaranteed Bay SLA Priority"})

    add_screen("STITCH-36", "Overstay Escalation Notice", 11, "Extension & Conflict",
        "Overstay penalty matrix: Active overstay counter, escalating surge tariffs, and wheel-clamp policy notice.",
        f"""
        {status_bar()}
        {nav_header("Lease Expired", "Active Overstay Alert")}
        <div class="screen-body space-y-3.5">
          <div class="card p-4 bg-red-50 border border-red-200 text-center">
            <div class="badge-chip danger mx-auto mb-2">
              <span class="material-symbols-outlined text-[13px]">alarm</span> OVERSTAY IN PROGRESS
            </div>
            <div class="text-2xl font-bold font-mono text-red-950">+00:24:18</div>
            <p class="text-xs text-red-800 mt-1">Lease for Bay B2-14 expired at 12:30 PM</p>
          </div>

          <div class="card p-4 space-y-2.5 text-xs">
            <div class="font-bold text-on-surface pb-1 border-b border-slate-100">Overstay Tariff Computation</div>
            <div class="flex justify-between text-secondary">
              <span>15-Min Grace Period:</span>
              <span class="text-red-700 font-bold">Elapsed (12:45 PM)</span>
            </div>
            <div class="flex justify-between text-secondary">
              <span>Standard Rack Tariff:</span>
              <span class="font-mono text-on-surface">₹60.00 / hr</span>
            </div>
            <div class="flex justify-between text-secondary">
              <span>Overstay Surcharge (+50%):</span>
              <span class="font-mono text-amber-700 font-bold">+₹30.00 / hr</span>
            </div>
            <div class="flex justify-between pt-2 border-t border-slate-200 text-sm font-bold text-on-surface">
              <span>Accumulated Overstay Fee:</span>
              <span class="font-mono text-red-600">₹45.00</span>
            </div>
          </div>

          <div class="card p-3 bg-slate-50 border border-slate-200/80 text-[11px] text-secondary leading-relaxed">
            <strong class="text-on-surface">Facility Bylaw Rule 14:</strong> Vehicles exceeding 2 hours overstay without an authorized extension are subject to wheel clamping by the attendant.
          </div>
        </div>
        <div class="sticky-footer">
          {btn("Settle Overstay & Prepare Exit", "primary", icon_name="exit_to_app")}
        </div>
        """, dossier={"intent": "Spec §4.10 Enforce turnover discipline while maintaining transparent legal statutory rates", "spec": "Rack Rate + Surge Penalty"})

    # --- STAGE 12: EV FAST CHARGING TELEMETRY (4 SCREENS) ---
    add_screen("STITCH-37", "EV Fast Charger Handshake", 12, "EV Fast Charging",
        "EV Bay B2-14 integration: Delta 60kW DC fast charger, CCS2 dual-gun cable lock, and target limit selector.",
        f"""
        {status_bar()}
        {nav_header("EV Fast Charger", "Bay B2-14 • Delta 60kW DC")}
        <div class="screen-body space-y-3.5">
          <div class="card p-4 text-center">
            <div class="w-14 h-14 rounded-2xl bg-teal-50 border border-teal-200 text-[#00685F] flex items-center justify-center mx-auto mb-2">
              <span class="material-symbols-outlined text-[32px]">ev_station</span>
            </div>
            <h3 class="text-base font-bold text-on-surface">Delta 60kW DC Fast Charger</h3>
            <p class="text-xs text-secondary mt-0.5">Station ID: <code class="font-mono text-slate-700">CHG-DELTA-B2-01</code></p>
            
            <div class="badge-chip ok mt-2">
              <span class="material-symbols-outlined text-[13px]">lock</span> CCS2 Gun Locked &amp; Communicating
            </div>
          </div>

          <div class="card p-4 space-y-3 text-xs">
            <div class="flex justify-between items-center pb-2 border-b border-slate-100">
              <span class="text-secondary">Vehicle Battery (Tata Nexon EV):</span>
              <span class="font-bold text-on-surface font-mono">Current: 34%</span>
            </div>
            <div class="flex justify-between items-center">
              <span class="text-secondary">Electricity Tariff:</span>
              <span class="font-bold text-[#00685F] font-mono">₹18.00 / kWh (+18% GST)</span>
            </div>
            
            <div>
              <label class="input-label mb-1.5">SET CHARGING TARGET</label>
              <div class="grid-2 gap-2">
                <div class="class-card active">
                  <span class="text-xs font-bold">80% Fast Target</span>
                  <span class="text-[10px] text-[#00685F]">~22 mins • Protects Battery</span>
                </div>
                <div class="class-card">
                  <span class="text-xs font-bold">100% Full Top-up</span>
                  <span class="text-[10px] text-secondary">~45 mins • Trickles at end</span>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div class="sticky-footer">
          {btn("Authorize & Start Fast Charging", "primary", icon_name="bolt")}
        </div>
        """, dossier={"intent": "Spec §4.7 Tier 4 EV Charging initiation with automated CCS2 lock detection", "spec": "SAC 998714 Power Tariff"})

    add_screen("STITCH-38", "Live 60kW Charging Telemetry", 12, "EV Fast Charging",
        "Live charging telemetry: Real-time battery SoC circular gauge (58%), kW power flow, and kWh tariff counter.",
        f"""
        {status_bar()}
        {nav_header("Charging in Progress", "Delta 60kW Fast DC")}
        <div class="screen-body space-y-3.5 text-center">
          <div class="card p-5">
            <div class="battery-circle mx-auto mb-2">
              <span class="text-2xl font-bold font-mono text-[#00685F]">58%</span>
              <span class="text-[10px] text-secondary font-bold">+24% ADDED</span>
            </div>
            
            <div class="text-xs font-bold text-on-surface">Tata Nexon EV • 40.5 kWh Pack</div>
            <div class="text-[11px] text-secondary mt-0.5">Est. 12 mins remaining until 80% cutoff</div>

            <div class="grid-3 gap-2 mt-4 pt-3 border-t border-slate-100 text-left">
              <div class="p-2 bg-slate-50 rounded-xl">
                <div class="text-[9px] text-secondary font-bold">POWER FLOW</div>
                <div class="font-mono font-bold text-xs text-on-surface mt-0.5">58.4 kW</div>
              </div>
              <div class="p-2 bg-slate-50 rounded-xl">
                <div class="text-[9px] text-secondary font-bold">DELIVERED</div>
                <div class="font-mono font-bold text-xs text-on-surface mt-0.5">14.2 kWh</div>
              </div>
              <div class="p-2 bg-slate-50 rounded-xl">
                <div class="text-[9px] text-secondary font-bold">CHARGE COST</div>
                <div class="font-mono font-bold text-xs text-[#00685F] mt-0.5">₹255.60</div>
              </div>
            </div>
          </div>

          <div class="card p-3 bg-teal-50 border border-teal-200 text-left text-xs text-teal-950 flex items-center gap-2">
            <span class="material-symbols-outlined text-[16px] text-teal-600 shrink-0">electric_bolt</span>
            <span>Auto-stop armed at 80% to protect vehicle lithium pack and avoid idle charges.</span>
          </div>
        </div>
        <div class="sticky-footer">
          {btn("Stop Charging Session", "secondary", icon_name="stop_circle")}
        </div>
        """, dossier={"intent": "Spec §4.7 Real-time power telemetry and safety threshold monitoring", "spec": "Live MQTT Telemetry Stream"})

    add_screen("STITCH-39", "Charging Complete & Idle Fee", 12, "EV Fast Charging",
        "Charging cutoff alert: Target 80% reached, 15-minute unplug grace timer, and ₹5/min idle penalty policy.",
        f"""
        {status_bar()}
        {nav_header("Charging Complete", "Target 80% Reached")}
        <div class="screen-body space-y-3.5 text-center">
          <div class="w-16 h-16 rounded-full bg-emerald-50 border-2 border-emerald-400 text-[#006947] flex items-center justify-center mx-auto mb-1">
            <span class="material-symbols-outlined text-[36px]">battery_charging_full</span>
          </div>
          
          <div>
            <h2 class="text-xl font-bold text-on-surface">Battery Ready: 80% Charged</h2>
            <p class="text-xs text-secondary mt-0.5">+18.4 kWh delivered in 21 mins 40 secs</p>
          </div>

          <div class="card p-4 bg-amber-50 border border-amber-200 text-left space-y-2">
            <div class="badge-chip warn">
              <span class="material-symbols-outlined text-[13px]">schedule</span> 15-MINUTE GRACE PERIOD
            </div>
            <div class="font-bold text-sm text-amber-950">Please Move Vehicle to Open Bay</div>
            <p class="text-xs text-amber-900 leading-relaxed">
              To ensure EV chargers are available for other drivers, a <strong>₹5.00/min idle fee</strong> applies if your vehicle remains connected to this charger after <strong>11:15 AM (14 mins left)</strong>.
            </p>
          </div>

          <div class="card p-3.5 text-left text-xs space-y-1.5">
            <div class="flex justify-between">
              <span class="text-secondary">Energy Consumed:</span>
              <span class="font-bold text-on-surface">18.4 kWh @ ₹18/kWh</span>
            </div>
            <div class="flex justify-between">
              <span class="text-secondary">Energy Total:</span>
              <span class="font-mono font-bold text-on-surface">₹331.20</span>
            </div>
          </div>
        </div>
        <div class="sticky-footer">
          {btn("I am Returning to Unplug Vehicle", "primary", icon_name="directions_walk")}
        </div>
        """, dossier={"intent": "Charger turnover management preventing stall squatting", "spec": "Idle Fee Enforcement"})

    add_screen("STITCH-40", "Combined Parking + EV Invoice", 12, "EV Fast Charging",
        "Unified statutory tax invoice: Itemized parking lease (SAC 999113) plus electricity charging (SAC 998714).",
        f"""
        {status_bar()}
        {nav_header("Unified Tax Invoice", "Invoice #PS-EV-2026-904")}
        <div class="screen-body space-y-3 text-xs">
          <div class="badge-chip teal mx-auto">GST Dual-SAC Statutory Invoice</div>

          <div class="card p-4 space-y-2.5">
            <div class="flex justify-between pb-2 border-b border-slate-100">
              <div>
                <div class="font-bold text-sm text-on-surface">Forum South Mall MLCP</div>
                <div class="text-[10px] text-secondary">GSTIN: 29AABCP1928K1Z5</div>
              </div>
              <span class="badge-chip ok">Paid via UPI</span>
            </div>

            <div class="space-y-2 pt-1">
              <div class="p-2 bg-slate-50 rounded-lg">
                <div class="flex justify-between font-bold text-on-surface">
                  <span>1. Parking Dwell (2 Hrs)</span>
                  <span class="font-mono">₹120.00</span>
                </div>
                <div class="text-[10px] text-secondary">SAC 999113 • Bay B2-14 • Platform Fee: ₹5.00</div>
              </div>

              <div class="p-2 bg-slate-50 rounded-lg">
                <div class="flex justify-between font-bold text-on-surface">
                  <span>2. EV Fast Charge (18.4 kWh)</span>
                  <span class="font-mono">₹331.20</span>
                </div>
                <div class="text-[10px] text-secondary">SAC 998714 • Delta 60kW DC Station</div>
              </div>

              <div class="flex justify-between text-secondary pt-1">
                <span>CGST (9%):</span>
                <span class="font-mono text-on-surface">₹41.06</span>
              </div>
              <div class="flex justify-between text-secondary">
                <span>SGST (9%):</span>
                <span class="font-mono text-on-surface">₹41.06</span>
              </div>
              <div class="flex justify-between pt-2 border-t border-slate-200 text-sm font-bold text-on-surface">
                <span>Grand Total:</span>
                <span class="font-mono text-[#00685F] text-base">₹538.32</span>
              </div>
            </div>
          </div>
        </div>
        <div class="sticky-footer">
          {btn("Download Unified GST PDF", "primary", icon_name="download")}
        </div>
        """, dossier={"intent": "Dual-SAC statutory invoice meeting Indian GST B2B/B2C compliance", "spec": "SAC 999113 + SAC 998714 Unified"})

    # --- STAGE 13: PASS & OFFLINE CELLAR (3 SCREENS) ---
    add_screen("STITCH-41", "Monthly Commuter Pass Catalog", 13, "Pass & Offline Cellar",
        "Commuter passes: Dedicated Assigned Bay, Floating Flexi Pass, and Metro Commuter Park-and-Ride plans.",
        f"""
        {status_bar()}
        {nav_header("Monthly Passes", "Bengaluru South MLCP Hub")}
        <div class="screen-body space-y-3">
          <div>
            <h2 class="text-xl font-bold text-on-surface">Commuter Season Passes</h2>
            <p class="text-xs text-secondary mt-0.5">Save up to 48% with automated monthly passes.</p>
          </div>

          <div class="space-y-2.5">
            <div class="card p-3.5 border-2 border-[#00685F] bg-teal-50/40 space-y-1.5 cursor-pointer">
              <div class="flex items-center justify-between">
                <span class="font-bold text-sm text-teal-950">Floating Flexi Pass</span>
                <span class="badge-chip teal">Most Popular</span>
              </div>
              <p class="text-xs text-secondary">Guaranteed admission to any open bay on Deck B1/B2. Mon–Sat, 8 AM – 9 PM.</p>
              <div class="flex items-center justify-between pt-2 border-t border-teal-100">
                <span class="text-xs text-secondary">Unlimited Lifts</span>
                <span class="font-mono font-bold text-sm text-[#00685F]">₹2,800 / mo</span>
              </div>
            </div>

            <div class="card p-3.5 space-y-1.5 cursor-pointer">
              <div class="flex items-center justify-between">
                <span class="font-bold text-sm text-on-surface">Dedicated Reserved Stall</span>
                <span class="badge-chip navy">24/7 Access</span>
              </div>
              <p class="text-xs text-secondary">Your personalized bay with nameplate lock. Level B2 stall with trickle EV charger.</p>
              <div class="flex items-center justify-between pt-2 border-t border-slate-100">
                <span class="text-xs text-secondary">Permanent Allocation</span>
                <span class="font-mono font-bold text-sm text-on-surface">₹4,200 / mo</span>
              </div>
            </div>
          </div>
        </div>
        <div class="sticky-footer">
          {btn("Select Floating Flexi (₹2,800)", "primary", icon_name="check")}
        </div>
        """, dossier={"intent": "Spec §4.14 Recurring commuter subscription options", "spec": "Monthly Pass Tier Model"})

    add_screen("STITCH-42", "UPI AutoPay e-Mandate", 13, "Pass & Offline Cellar",
        "NPCI UPI AutoPay recurring mandate: ₹2,800/mo limit, Google Pay/PhonePe authorization, and pre-debit SMS consent.",
        f"""
        {status_bar()}
        {nav_header("Setup AutoPay", "NPCI UPI e-Mandate")}
        <div class="screen-body space-y-3.5">
          <div class="card p-4 text-center">
            <div class="w-14 h-14 rounded-2xl bg-teal-50 border border-teal-200 text-[#00685F] flex items-center justify-center mx-auto mb-2">
              <span class="material-symbols-outlined text-[32px]">autorenew</span>
            </div>
            <h3 class="text-base font-bold text-on-surface">NPCI UPI AutoPay Mandate</h3>
            <p class="text-xs text-secondary mt-0.5">Recurring Monthly Pass Subscription</p>
          </div>

          <div class="card p-4 space-y-2.5 text-xs">
            <div class="flex justify-between pb-2 border-b border-slate-100">
              <span class="text-secondary">Merchant:</span>
              <span class="font-bold text-on-surface">ParkSpot Mobility Pvt Ltd</span>
            </div>
            <div class="flex justify-between">
              <span class="text-secondary">Max Debit Amount:</span>
              <span class="font-mono font-bold text-on-surface">₹2,800.00 / month</span>
            </div>
            <div class="flex justify-between">
              <span class="text-secondary">Billing Cycle:</span>
              <span class="font-bold text-on-surface">1st of Every Month</span>
            </div>
            <div class="flex justify-between">
              <span class="text-secondary">Mandate Validity:</span>
              <span class="font-bold text-on-surface">Nov 2026 – Oct 2027 (12 Mos)</span>
            </div>
            <div class="flex justify-between pt-2 border-t border-slate-100">
              <span class="text-secondary">Debiting UPI VPA:</span>
              <span class="font-mono text-slate-700">mahesh.giri@okhdfcbank</span>
            </div>
          </div>

          <div class="legal-trust-banner">
            <span class="material-symbols-outlined text-[15px] text-[#00685F] shrink-0">verified_user</span>
            <p>Mandate pre-notification SMS sent 24 hours prior to each billing. Cancel or pause anytime in 1 tap from profile.</p>
          </div>
        </div>
        <div class="sticky-footer">
          {btn("Authorize Mandate via UPI PIN", "primary", icon_name="lock")}
        </div>
        """, dossier={"intent": "Spec §4.14 NPCI recurring mandate authorization", "spec": "UPI AutoPay e-Mandate"})

    add_screen("STITCH-43", "Basement Offline Grace Pass", 13, "Pass & Offline Cellar",
        "Subterranean offline pass: 0-bar cellular fallback, rotating cryptographic TOTP nonce, and BLE beacon ping.",
        f"""
        {status_bar()}
        {nav_header("Offline Gate Pass", "Subterranean Deck B3")}
        <div class="screen-body space-y-3.5 text-center">
          <div class="card p-3 bg-slate-900 text-white flex items-center justify-between text-xs">
            <div class="flex items-center gap-2">
              <span class="material-symbols-outlined text-[16px] text-amber-400">cloud_off</span>
              <span>Cellular Network Unavailable (Deck B3)</span>
            </div>
            <span class="badge-chip warn text-[10px]">Offline Mode</span>
          </div>

          <div class="card p-4 space-y-3">
            <div class="text-[10px] font-bold text-secondary uppercase">PRE-CACHED PASSKIT QR NONCE</div>
            
            <div class="w-44 h-44 bg-white p-2 border-2 border-slate-900 rounded-2xl mx-auto flex items-center justify-center shadow-md">
              <img src="../assets/qr-pass.png" alt="Offline Dynamic QR" class="w-full h-full object-contain"/>
            </div>

            <div class="flex items-center justify-center gap-2 text-xs font-mono text-[#00685F]">
              <span class="material-symbols-outlined text-[16px] animate-spin">refresh</span>
              <span>TOTP Nonce expires in: 04:32</span>
            </div>

            <div class="p-2.5 bg-slate-50 border border-slate-200/60 rounded-xl text-left text-xs space-y-1">
              <div class="flex items-center gap-1.5 text-secondary">
                <span class="material-symbols-outlined text-[15px] text-teal-600">bluetooth</span> BLE Proximity Beacon Active (-64 dBm)
              </div>
              <div class="text-[11px] text-secondary">Signed with cloud Ed25519 key prior to descent. Boom barrier scanner will verify offline.</div>
            </div>
          </div>
        </div>
        <div class="sticky-footer">
          {btn("Present to Gate Scanner", "primary", icon_name="qr_code_scanner")}
        </div>
        """, dossier={"intent": "Spec §1.2 Axioms of Ground Chaos: Cellar connectivity failure tolerance", "spec": "Offline Asymmetric Ed25519 Nonce"})

    # --- STAGE 14: PHYSICAL VMS & THERMAL PRINT (2 SCREENS) ---
    add_screen("EDGE-01", "Driveway LED VMS Totem", 14, "Physical VMS & Print",
        "Outdoor Variable Message Sign (VMS): High-contrast outdoor LED totem showing live bay reservation & height clearance.",
        f"""
        {status_bar(dark=True)}
        <div class="hero-stage" style="flex:1;background:#050505;padding:16px 16px 28px;display:flex;flex-direction:column;justify-content:space-between;">
          <div>
            <div class="flex items-center justify-between text-[11px] text-slate-400 mb-3 px-1">
              <span>GATEWAY DRIVEWAY DISPLAY</span>
              <span class="badge-chip ok text-[10px]">LED MATRIX LIVE</span>
            </div>

            <div class="vms-board space-y-3">
              <div class="border-b border-slate-800 pb-2">
                <div class="text-[10px] text-slate-500 uppercase tracking-widest font-mono">PARKSPOT SMART MOBILITY VMS</div>
                <div class="vms-green text-sm font-bold tracking-wider mt-1">WELCOME TATA NEXON</div>
                <div class="vms-green text-base font-bold font-mono tracking-widest">KA 01 MJ 8821</div>
              </div>

              <div class="border-b border-slate-800 pb-2 space-y-1">
                <div class="text-[10px] text-slate-500 uppercase tracking-widest font-mono">CONFIRMED ASSIGNMENT</div>
                <div class="vms-amber text-lg font-bold tracking-wider">RESERVED: BAY B2-14</div>
                <div class="vms-cyan text-xs font-mono">&gt;&gt;&gt; PROCEED TO ENTRY LANE 2 &gt;&gt;&gt;</div>
              </div>

              <div class="flex justify-between items-center text-xs font-mono pt-1">
                <div class="vms-green font-bold">DECK B2: 42 FREE</div>
                <div class="vms-red font-bold">MAX HT: 2.10M</div>
              </div>
            </div>
          </div>

          <div class="card p-3 bg-slate-900 border border-slate-800 text-xs text-slate-300 space-y-1">
            <div class="font-bold text-white flex items-center gap-1.5">
              <span class="material-symbols-outlined text-[15px] text-teal-400">display_settings</span> Hardware Specifications
            </div>
            <p class="text-[11px] text-slate-400 leading-relaxed">
              Daktronics P10 Ultra-Bright Dual-Color LED Matrix • Direct Modbus/RS485 feed from Lane 01 ANPR Camera.
            </p>
          </div>
        </div>
        <div class="sticky-footer" style="background:#0F172A;border-color:#1E293B;">
          <div class="text-center text-xs text-slate-400">Hardware Telemetry Stream • Latency &lt; 380ms</div>
        </div>
        """, bg="#050505", dossier={"intent": "Physical-digital edge interface for real-time driver arrival guidance", "spec": "IP65 P10 RGB LED Signage"})

    add_screen("EDGE-02", "58mm Thermal Printed Ticket", 14, "Physical VMS & Print",
        "Attendant physical printout: 58mm thermal receipt for non-smartphone walk-ins with exit clearance QR.",
        f"""
        {status_bar()}
        <nav class="nav-header" style="background:rgba(255,255,255,0.92);border-bottom:1px solid #E2E8F0;color:#0B1C30;">
          <button class="nav-btn" type="button"><span class="material-symbols-outlined" style="font-size:18px;">arrow_back</span></button>
          <div class="nav-center">
            <h1 class="nav-title">Thermal Paper Ticket</h1>
            <p class="nav-sub">Attendant POS Printout</p>
          </div>
          <div style="width:36px;"></div>
        </nav>
        <div class="screen-body space-y-3 py-3" style="background:#E2E8F0;">
          <div class="thermal-ticket">
            <div class="text-center border-b border-dashed border-slate-400 pb-3 mb-3">
              <div class="font-bold text-sm tracking-widest">PARKSPOT SMART MOBILITY</div>
              <div class="text-xs font-semibold mt-0.5">FORUM SOUTH MALL MLCP</div>
              <div class="text-[10px] text-slate-600 mt-0.5">Gate 02 • Lane 01 • POS-04</div>
            </div>

            <div class="space-y-1.5 text-xs font-mono">
              <div class="flex justify-between">
                <span>TICKET:</span>
                <span class="font-bold">#TK-2026-1024-8841</span>
              </div>
              <div class="flex justify-between">
                <span>VEHICLE:</span>
                <span class="font-bold">KA 01 MJ 8821</span>
              </div>
              <div class="flex justify-between">
                <span>CLASS:</span>
                <span>SUV / 4-WHEELER</span>
              </div>
              <div class="flex justify-between">
                <span>ENTRY:</span>
                <span>24-OCT-2026 10:42:15</span>
              </div>
              <div class="flex justify-between">
                <span>TARIFF:</span>
                <span>₹60/1ST HR + ₹30/30M</span>
              </div>
              <div class="flex justify-between">
                <span>SAC CODE:</span>
                <span>999113 (GST 18%)</span>
              </div>
            </div>

            <div class="my-4 text-center border-t border-b border-dashed border-slate-400 py-3">
              <img src="../assets/qr-pass.png" alt="Exit Barcode" class="w-32 h-32 mx-auto object-contain filter contrast-125"/>
              <div class="text-[10px] font-mono mt-1 text-slate-600">SCAN AT EXIT BARRIER</div>
            </div>

            <div class="text-center text-[10px] text-slate-600 space-y-0.5">
              <div>PLEASE KEEP TICKET SAFE • DO NOT FOLD</div>
              <div class="font-bold">LOST TICKET SURCHARGE: ₹300.00</div>
              <div>GSTIN: 29AABCP1928K1Z5 • HELPLINE: 1800-PARK-SPOT</div>
            </div>
          </div>
        </div>
        <div class="sticky-footer">
          {btn("Print Duplicate Ticket", "primary", icon_name="print")}
        </div>
        """, bg="#E2E8F0", dossier={"intent": "Physical paper fallback for drivers without mobile devices", "spec": "58mm ESC/POS Thermal Print"})

    # Build Stage Filter Pills
    stages = [
        ("All", "All Screens (45)"),
        ("1", "1. Launch & Onboard (4)"),
        ("2", "2. Auth Suite (8)"),
        ("3", "3. Flagship 5-Tabs (5)"),
        ("4", "4. Vehicle & Garage (2)"),
        ("5", "5. Map & Search HUD (2)"),
        ("6", "6. Facility & B2 Deck (2)"),
        ("7", "7. Quote ₹76.70 & UPI (2)"),
        ("8", "8. Ingress & Active Dwell (3)"),
        ("9", "9. Tax Invoice & SOS (2)"),
        ("10", "10. Floating Drive-In (3)"),
        ("11", "11. Extension & Conflict (3)"),
        ("12", "12. EV Fast Charging (4)"),
        ("13", "13. Pass & Offline Cellar (3)"),
        ("14", "14. Physical VMS & Print (2)"),
    ]

    pills_html = []
    for s_id, s_lbl in stages:
        active_cls = "bg-teal-600 text-white font-bold" if s_id == "All" else "bg-slate-800/80 text-slate-300 hover:text-white"
        pills_html.append(f"""
        <button type="button" onclick="filterByStage('{s_id}', this)" class="stage-pill-btn px-3 py-1.5 rounded-lg text-xs font-semibold border border-slate-700/80 shrink-0 transition-all {active_cls}">
          {s_lbl}
        </button>""")

    # Build Grid Cards HTML
    grid_cards_html = []
    for idx, sc in enumerate(screens):
        iframe_tag = f'<a href="{sc["iframe_link"]}" target="_blank" class="text-[11px] text-teal-400 hover:underline flex items-center gap-0.5">Standalone {icon("open_in_new", size=13)}</a>' if sc["iframe_link"] else ''
        grid_cards_html.append(f"""
        <article class="screen-grid-item" data-stage="{sc['stage_idx']}" data-search="{sc['id'].lower()} {sc['title'].lower()} {sc['stage_name'].lower()}">
          <header class="flex items-center justify-between px-1 mb-2">
            <span class="text-xs font-bold text-teal-400 flex items-center gap-1.5">
              <span class="w-2 h-2 rounded-full bg-teal-400"></span>
              <span class="font-mono">{sc['id']}</span>
            </span>
            <div class="flex items-center gap-2">
              <span class="text-[10px] text-slate-400 font-semibold">{sc['stage_name']}</span>
              {iframe_tag}
            </div>
          </header>

          <div class="phone-frame-container" onclick="openInStage({idx})">
            <div class="phone" style="background:{sc['bg']};">
              <div class="phone-viewport">{sc['html']}</div>
              <div class="home-indicator"></div>
            </div>
          </div>

          <footer class="mt-2 text-center p-2 rounded-xl bg-slate-900/80 border border-slate-800">
            <h3 class="text-xs font-bold text-white truncate">{sc['title']}</h3>
            <p class="text-[11px] text-slate-400 mt-0.5 line-clamp-1">{sc['desc']}</p>
          </footer>
        </article>""")

    # Build Jump Dropdown Options
    jump_options = []
    for idx, sc in enumerate(screens):
        jump_options.append(f'<option value="{idx}">{sc["id"]} — {sc["title"]} ({sc["stage_name"]})</option>')

    # Complete HTML Document
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8"/>
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>ParkSpot Driver UI Suite — Google Stitch Design System (Complete Flow)</title>
  <link rel="preconnect" href="https://fonts.googleapis.com"/>
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin/>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Plus+Jakarta+Sans:wght@500;600;700;800&family=JetBrains+Mono:wght@500;700&family=Share+Tech+Mono&display=swap" rel="stylesheet"/>
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200" />
  <script src="https://cdn.tailwindcss.com"></script>
  <style>
    /* Google Stitch Urban Mobility & Smart Transit Theme Tokens */
    :root {{
      --primary: #00685F;
      --primary-container: #89F5E7;
      --on-primary: #FFFFFF;
      --on-primary-container: #00201D;
      --surface: #F8F9FF;
      --on-surface: #0B1C30;
      --secondary: #565E74;
      --surface-container: #E5EEFF;
      --teal: #00685F;
      --navy: #0B1C30;
    }}

    body {{
      background: #070B14;
      color: #E2E8F0;
      font-family: 'Plus Jakarta Sans', 'Inter', system-ui, sans-serif;
      margin: 0;
      padding: 0;
    }}

    /* Device Bezel (iPhone 14 / 16 Pro Canvas: 390x844) */
    .phone {{
      width: 390px;
      height: 844px;
      border-radius: 44px;
      overflow: hidden;
      position: relative;
      box-shadow: 0 25px 60px -15px rgba(0, 0, 0, 0.7), 0 0 0 1px rgba(255, 255, 255, 0.1);
      display: flex;
      flex-direction: column;
      border: 6px solid #1E293B;
      flex-shrink: 0;
    }}
    .phone-viewport {{
      position: absolute;
      inset: 0;
      display: flex;
      flex-direction: column;
      overflow: hidden;
    }}
    .screen-body {{
      flex: 1;
      overflow-y: auto;
      padding: 16px;
    }}
    .home-indicator {{
      position: absolute;
      bottom: 8px;
      left: 50%;
      transform: translateX(-50%);
      width: 134px;
      height: 4px;
      background: rgba(11,28,48,0.4);
      border-radius: 999px;
      z-index: 50;
      pointer-events: none;
    }}

    /* iOS Status Bar */
    .ios-status-bar {{
      height: 44px;
      padding: 8px 24px 0;
      display: flex;
      align-items: center;
      justify-content: space-between;
      font-family: 'Plus Jakarta Sans', sans-serif;
      font-weight: 700;
      font-size: 14px;
      z-index: 40;
      flex-shrink: 0;
    }}
    .dynamic-island {{
      width: 90px;
      height: 22px;
      background: #000000;
      border-radius: 20px;
    }}
    .ios-icons {{
      display: flex;
      align-items: center;
      gap: 4px;
    }}

    /* Navigation Bar */
    .nav-header {{
      height: 52px;
      padding: 0 12px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      backdrop-filter: blur(16px);
      z-index: 30;
      flex-shrink: 0;
    }}
    .nav-btn {{
      width: 36px;
      height: 36px;
      border-radius: 12px;
      background: #EFF4FF;
      border: 0;
      color: #0B1C30;
      display: grid;
      place-items: center;
      cursor: pointer;
    }}
    .nav-center {{
      text-align: center;
      flex: 1;
      min-width: 0;
      padding: 0 8px;
    }}
    .nav-title {{
      font-family: 'Plus Jakarta Sans', sans-serif;
      font-size: 15px;
      font-weight: 700;
      line-height: 1.2;
      margin: 0;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
    }}
    .nav-sub {{
      font-size: 10px;
      line-height: 1.2;
      margin: 1px 0 0;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
    }}

    /* Standard 5-Tab Bottom Navigation Bar */
    .bottom-tabbar {{
      height: 64px;
      background: #FFFFFF;
      border-top: 1px solid #E2E8F0;
      display: flex;
      justify-content: space-around;
      align-items: center;
      padding-bottom: 8px;
      z-index: 30;
      flex-shrink: 0;
    }}
    .tab-item {{
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      flex: 1;
    }}

    /* Buttons */
    .pro-btn {{
      height: 48px;
      border-radius: 14px;
      border: 0;
      font-family: 'Plus Jakarta Sans', sans-serif;
      font-size: 13.5px;
      font-weight: 700;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 8px;
      cursor: pointer;
      transition: all 0.15s ease;
      width: 100%;
    }}
    .pro-btn.primary {{
      background: #00685F;
      color: #FFFFFF;
      box-shadow: 0 4px 12px rgba(0,104,95,0.25);
    }}
    .pro-btn.secondary {{
      background: #FFFFFF;
      color: #0B1C30;
      border: 1.5px solid #E2E8F0;
    }}
    .pro-btn.sm {{
      height: 34px;
      font-size: 11px;
      border-radius: 10px;
      padding: 0 12px;
      width: auto;
    }}

    /* Cards */
    .card {{
      background: #FFFFFF;
      border: 1px solid #E2E8F0;
      border-radius: 18px;
      box-shadow: 0 2px 8px rgba(11,28,48,0.03);
    }}

    /* Badges & Chips */
    .badge-chip {{
      display: inline-flex;
      align-items: center;
      gap: 4px;
      font-size: 10px;
      font-weight: 700;
      padding: 3px 8px;
      border-radius: 6px;
      text-transform: uppercase;
      letter-spacing: 0.04em;
    }}
    .badge-chip.teal {{ background: #CCFBF1; color: #00685F; }}
    .badge-chip.ok {{ background: #DCFCE7; color: #006947; }}
    .badge-chip.warn {{ background: #FFFBEB; color: #B45309; }}
    .badge-chip.danger {{ background: #FFDAD6; color: #BA1A1A; }}
    .badge-chip.navy {{ background: #0B1C30; color: #FFFFFF; }}
    .badge-chip.slate {{ background: #EFF4FF; color: #565E74; }}

    /* Indian HSRP License Plate */
    .hsrp-plate-box {{
      background: #FFFFFF;
      border: 2px solid #000000;
      border-radius: 5px;
      padding: 2px 8px;
      display: inline-flex;
      align-items: center;
      gap: 8px;
      box-shadow: 0 1px 3px rgba(0,0,0,0.1);
    }}
    .hsrp-flag {{
      display: flex;
      flex-direction: column;
      align-items: center;
      padding-right: 6px;
      border-right: 1px solid #CBD5E1;
      line-height: 1;
    }}
    .hsrp-chakra {{
      width: 7px;
      height: 7px;
      border: 1px solid #1E40AF;
      border-radius: 50%;
      margin-bottom: 2px;
      background: #2563EB;
    }}
    .hsrp-flag span {{
      font-size: 7px;
      font-weight: 900;
      color: #1E3A8A;
      letter-spacing: -0.05em;
    }}
    .hsrp-number {{
      font-family: 'Share Tech Mono', monospace;
      font-size: 15px;
      font-weight: 700;
      color: #000000;
      letter-spacing: 0.12em;
      white-space: nowrap;
    }}

    /* Form & Input Elements */
    .input-label {{
      font-size: 10px;
      font-weight: 700;
      color: #565E74;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      display: block;
      margin-bottom: 4px;
    }}
    .input-field {{
      height: 46px;
      background: #FFFFFF;
      border: 1.5px solid #E2E8F0;
      border-radius: 12px;
      padding: 0 12px;
      display: flex;
      align-items: center;
      gap: 10px;
    }}
    .input-field input {{
      border: 0;
      outline: 0;
      background: transparent;
      width: 100%;
      font-family: 'Plus Jakarta Sans', sans-serif;
      font-size: 13px;
      font-weight: 600;
      color: #0B1C30;
    }}
    .eye-toggle-btn {{
      background: none;
      border: 0;
      cursor: pointer;
      display: grid;
      place-items: center;
      padding: 4px;
    }}

    .phone-input-row {{
      display: flex;
      gap: 8px;
    }}
    .phone-prefix {{
      height: 46px;
      background: #EFF4FF;
      border: 1.5px solid #E2E8F0;
      border-radius: 12px;
      padding: 0 10px;
      display: flex;
      align-items: center;
      gap: 6px;
      font-weight: 700;
      font-size: 13px;
      color: #0B1C30;
      flex-shrink: 0;
    }}
    .phone-text-input {{
      flex: 1;
      height: 46px;
      background: #FFFFFF;
      border: 1.5px solid #E2E8F0;
      border-radius: 12px;
      padding: 0 12px;
      font-family: 'Plus Jakarta Sans', sans-serif;
      font-size: 14px;
      font-weight: 600;
      color: #0B1C30;
      outline: none;
    }}

    /* OTP Cells */
    .otp-boxes-row {{
      display: flex;
      justify-content: center;
      gap: 8px;
    }}
    .otp-cell {{
      width: 44px;
      height: 52px;
      border-radius: 12px;
      border: 2px solid #CBD5E1;
      background: #FFFFFF;
      font-family: 'Share Tech Mono', monospace;
      font-size: 22px;
      font-weight: 700;
      display: flex;
      align-items: center;
      justify-content: center;
      color: #0B1C30;
    }}
    .otp-cell.filled {{
      border-color: #00685F;
      background: #F0FDFA;
    }}
    .otp-cell.active {{
      border-color: #00685F;
      box-shadow: 0 0 0 3px rgba(0,104,95,0.2);
    }}

    /* Password Strength Bar */
    .strength-meter-bar {{
      display: flex;
      gap: 4px;
      height: 4px;
    }}
    .strength-segment {{
      flex: 1;
      border-radius: 2px;
      background: #E2E8F0;
    }}
    .strength-segment.active {{
      background: #10B981;
    }}

    /* Onboarding Styling */
    .onboarding-top-bar {{
      padding: 8px 16px;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }}
    .skip-btn {{
      background: none;
      border: 0;
      font-size: 12px;
      font-weight: 700;
      color: #565E74;
      cursor: pointer;
    }}
    .onboarding-hero-card {{
      position: relative;
      height: 380px;
      border-radius: 24px;
      overflow: hidden;
      margin: 8px 12px 16px;
      border: 1px solid #E2E8F0;
      flex-shrink: 0;
    }}
    .onboarding-img {{
      width: 100%;
      height: 100%;
      object-fit: cover;
    }}
    .onboarding-overlay-card {{
      position: absolute;
      bottom: 12px;
      left: 12px;
      right: 12px;
      background: rgba(255,255,255,0.95);
      backdrop-filter: blur(8px);
      padding: 12px;
      border-radius: 16px;
      box-shadow: 0 10px 25px rgba(0,0,0,0.1);
    }}
    .carousel-dots-row {{
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 6px;
    }}
    .carousel-dot {{
      width: 8px;
      height: 8px;
      border-radius: 50%;
      background: #CBD5E1;
      transition: all 0.2s ease;
    }}
    .carousel-dot.active {{
      width: 24px;
      border-radius: 999px;
      background: #00685F;
    }}

    /* Auth Gateway */
    .auth-divider-row {{
      display: flex;
      align-items: center;
      gap: 12px;
    }}
    .divider-line {{
      flex: 1;
      height: 1px;
      background: rgba(255,255,255,0.15);
    }}
    .divider-text {{
      font-size: 9px;
      letter-spacing: 0.08em;
      color: #94A3B8;
      font-weight: 700;
    }}
    .social-auth-btn {{
      height: 44px;
      border-radius: 12px;
      background: #FFFFFF;
      border: 0;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 6px;
      font-weight: 700;
      font-size: 12px;
      color: #0B1C30;
      cursor: pointer;
    }}

    /* Home Screen App Bar */
    .home-app-bar {{
      padding: 8px 16px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      border-bottom: 1px solid #E2E8F0;
    }}
    .location-pill {{
      display: flex;
      align-items: center;
      gap: 8px;
    }}
    .avatar-circle {{
      width: 34px;
      height: 34px;
      border-radius: 50%;
      background: linear-gradient(135deg, #00685F, #0B1C30);
      color: #FFF;
      font-weight: 700;
      font-size: 11px;
      display: grid;
      place-items: center;
    }}
    .notification-badge-dot {{
      position: absolute;
      top: 6px;
      right: 6px;
      width: 7px;
      height: 7px;
      border-radius: 50%;
      background: #BA1A1A;
      border: 1.5px solid #FFF;
    }}

    /* Search HUD Bar */
    .search-hud-bar {{
      height: 46px;
      background: #FFFFFF;
      border: 1.5px solid #E2E8F0;
      border-radius: 14px;
      padding: 0 12px;
      display: flex;
      align-items: center;
      gap: 10px;
      box-shadow: 0 2px 6px rgba(11,28,48,0.03);
    }}
    .search-hud-bar input {{
      border: 0;
      outline: 0;
      background: transparent;
      width: 100%;
      font-family: 'Plus Jakarta Sans', sans-serif;
      font-size: 12.5px;
      font-weight: 600;
      color: #0B1C30;
    }}
    .filter-tune-btn {{
      width: 30px;
      height: 30px;
      border-radius: 8px;
      background: #EFF4FF;
      border: 0;
      color: #00685F;
      display: grid;
      place-items: center;
      cursor: pointer;
    }}

    /* Category Chips */
    .category-chips-row {{
      display: flex;
      gap: 6px;
      overflow-x: auto;
      padding-bottom: 4px;
      scrollbar-width: none;
    }}
    .chip {{
      display: inline-flex;
      align-items: center;
      gap: 4px;
      padding: 6px 12px;
      border-radius: 999px;
      background: #FFFFFF;
      border: 1px solid #E2E8F0;
      font-size: 11px;
      font-weight: 600;
      color: #565E74;
      white-space: nowrap;
      cursor: pointer;
    }}
    .chip.active {{
      background: #00685F;
      color: #FFFFFF;
      border-color: #00685F;
    }}

    /* Facility Mini Card */
    .facility-mini-card {{
      background: #FFFFFF;
      border: 1px solid #E2E8F0;
      border-radius: 14px;
      padding: 10px;
      display: flex;
      gap: 10px;
      align-items: center;
    }}
    .mini-card-thumb {{
      width: 68px;
      height: 68px;
      border-radius: 10px;
      object-fit: cover;
    }}

    /* Quick Actions */
    .quick-action-pill {{
      display: flex;
      flex-direction: column;
      align-items: center;
      cursor: pointer;
    }}
    .action-icon-box {{
      width: 44px;
      height: 44px;
      border-radius: 14px;
      background: #EFF4FF;
      color: #00685F;
      display: grid;
      place-items: center;
      margin-bottom: 4px;
    }}
    .quick-action-pill span {{
      font-size: 10px;
      font-weight: 600;
      color: #565E74;
    }}

    /* Segmented Control */
    .segmented-control {{
      display: flex;
      background: #EFF4FF;
      padding: 3px;
      border-radius: 12px;
    }}
    .seg-btn {{
      flex: 1;
      padding: 6px 0;
      text-align: center;
      font-size: 11px;
      font-weight: 600;
      color: #565E74;
      border-radius: 9px;
      cursor: pointer;
    }}
    .seg-btn.active {{
      background: #FFFFFF;
      color: #00685F;
      font-weight: 700;
      box-shadow: 0 2px 4px rgba(0,0,0,0.06);
    }}

    /* Brand Glyphs & Logo */
    .brand-pill {{
      display: inline-flex;
      align-items: center;
      gap: 10px;
      background: rgba(255,255,255,0.08);
      border: 1px solid rgba(255,255,255,0.15);
      border-radius: 999px;
      padding: 6px 16px 6px 6px;
      backdrop-filter: blur(10px);
    }}
    .brand-pill.large {{
      padding: 8px 24px 8px 8px;
    }}
    .brand-glyph {{
      width: 32px;
      height: 32px;
      border-radius: 50%;
      background: #00685F;
      color: #89F5E7;
      font-family: 'Plus Jakarta Sans', sans-serif;
      font-weight: 800;
      font-size: 16px;
      display: grid;
      place-items: center;
    }}
    .brand-pill.large .brand-glyph {{
      width: 44px;
      height: 44px;
      font-size: 22px;
    }}
    .brand-text {{
      font-family: 'Plus Jakarta Sans', sans-serif;
      font-weight: 800;
      font-size: 16px;
      color: #FFFFFF;
      letter-spacing: -0.02em;
    }}
    .brand-pill.large .brand-text {{
      font-size: 22px;
    }}
    .brand-text span {{
      color: #89F5E7;
    }}

    /* Blueprint Grid */
    .blueprint-grid-canvas {{
      background: #0B1C30;
      border-radius: 16px;
      padding: 16px;
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 10px;
    }}
    .bay-cell {{
      height: 60px;
      border-radius: 10px;
      display: flex;
      align-items: center;
      justify-content: center;
      font-family: 'JetBrains Mono', monospace;
      font-weight: 700;
      font-size: 12px;
      cursor: pointer;
    }}
    .bay-cell.taken {{
      background: rgba(255,255,255,0.06);
      color: #64748B;
      border: 1px dashed rgba(255,255,255,0.15);
    }}
    .bay-cell.free {{
      background: rgba(16,185,129,0.15);
      color: #34D399;
      border: 1.5px solid #10B981;
    }}
    .bay-cell.selected {{
      background: #00685F;
      color: #89F5E7;
      border: 2px solid #89F5E7;
      box-shadow: 0 0 12px rgba(137,245,231,0.4);
    }}

    /* Monthly Pass Card */
    .monthly-pass-card {{
      background: linear-gradient(135deg, #0B1C30 0%, #1E293B 100%);
      border: 1.5px solid rgba(255,255,255,0.15);
      border-radius: 20px;
      padding: 20px;
      color: #FFFFFF;
      box-shadow: 0 16px 32px rgba(0,0,0,0.3);
    }}
    
    /* Wallet Balance Card */
    .wallet-balance-card {{
      background: linear-gradient(135deg, #00685F 0%, #0B1C30 100%);
      border-radius: 20px;
      padding: 20px;
      color: #FFFFFF;
      box-shadow: 0 10px 24px rgba(0,104,95,0.25);
    }}

    /* Dwell Ring */
    .dwell-countdown-ring {{
      width: 140px;
      height: 140px;
      border-radius: 50%;
      border: 8px solid #EFF4FF;
      border-top-color: #00685F;
      border-right-color: #00685F;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
    }}

    /* Sticky Footer */
    .sticky-footer {{
      margin-top: auto;
      padding: 12px 16px 28px;
      background: #FFFFFF;
      border-top: 1px solid #E2E8F0;
      z-index: 30;
      flex-shrink: 0;
    }}

    /* Utilities */
    .img-cover {{
      width: 100%;
      height: 100%;
      object-fit: cover;
    }}
    .hero-gradient-overlay {{
      position: absolute;
      inset: 0;
      background: linear-gradient(180deg, rgba(11,28,48,0.3) 0%, rgba(11,28,48,0.92) 100%);
    }}
    .icon-circle {{
      width: 34px;
      height: 34px;
      border-radius: 50%;
      display: grid;
      place-items: center;
      flex-shrink: 0;
    }}
    .icon-circle.teal {{ background: #CCFBF1; color: #00685F; }}
    .icon-circle.slate {{ background: #EFF4FF; color: #565E74; }}
    .icon-circle.danger {{ background: #FFDAD6; color: #BA1A1A; }}
    .icon-circle.warn {{ background: #FFFBEB; color: #B45309; }}

    .grid-2 {{ display: grid; grid-template-columns: repeat(2, 1fr); }}
    .grid-3 {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 8px; }}
    .grid-4 {{ display: grid; grid-template-columns: repeat(4, 1fr); }}
    .flex {{ display: flex; }}
    .flex-col {{ display: flex; flex-direction: column; }}
    .flex-1 {{ flex: 1; }}
    .items-center {{ align-items: center; }}
    .items-start {{ align-items: flex-start; }}
    .justify-center {{ justify-content: center; }}
    .justify-between {{ justify-content: space-between; }}
    .text-center {{ text-align: center; }}
    .text-left {{ text-align: left; }}
    .text-right {{ text-align: right; }}
    .mx-auto {{ margin-left: auto; margin-right: auto; }}
    .my-1 {{ margin-top: 4px; margin-bottom: 4px; }}
    .my-2 {{ margin-top: 8px; margin-bottom: 8px; }}
    .mb-1 {{ margin-bottom: 4px; }}
    .mb-2 {{ margin-bottom: 8px; }}
    .mb-3 {{ margin-bottom: 12px; }}
    .mb-4 {{ margin-bottom: 16px; }}
    .mt-0-5 {{ margin-top: 2px; }}
    .mt-1 {{ margin-top: 4px; }}
    .mt-2 {{ margin-top: 8px; }}
    .mt-3 {{ margin-top: 12px; }}
    .mt-4 {{ margin-top: 16px; }}
    .mt-5 {{ margin-top: 20px; }}
    .p-1 {{ padding: 4px; }}
    .p-2 {{ padding: 8px; }}
    .p-2-5 {{ padding: 10px; }}
    .p-3 {{ padding: 12px; }}
    .p-3-5 {{ padding: 14px; }}
    .p-4 {{ padding: 16px; }}
    .p-5 {{ padding: 20px; }}
    .p-6 {{ padding: 24px; }}
    .py-1 {{ padding-top: 4px; padding-bottom: 4px; }}
    .py-2 {{ padding-top: 8px; padding-bottom: 8px; }}
    .px-1 {{ padding-left: 4px; padding-right: 4px; }}
    .px-2 {{ padding-left: 8px; padding-right: 8px; }}
    .px-4 {{ padding-left: 16px; padding-right: 16px; }}
    .pt-1 {{ padding-top: 4px; }}
    .pt-2 {{ padding-top: 8px; }}
    .pt-3 {{ padding-top: 12px; }}
    .pb-1 {{ padding-bottom: 4px; }}
    .min-w-0 {{ min-width: 0; }}
    .truncate {{ white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }}
    .space-y-1 > * + * {{ margin-top: 4px; }}
    .space-y-1-5 > * + * {{ margin-top: 6px; }}
    .space-y-2 > * + * {{ margin-top: 8px; }}
    .space-y-2-5 > * + * {{ margin-top: 10px; }}
    .space-y-3 > * + * {{ margin-top: 12px; }}
    .space-y-3-5 > * + * {{ margin-top: 14px; }}
    .space-y-4 > * + * {{ margin-top: 16px; }}
    .leading-relaxed {{ line-height: 1.6; }}
    .leading-tight {{ line-height: 1.25; }}
    .leading-normal {{ line-height: 1.5; }}
    .font-mono {{ font-family: 'JetBrains Mono', monospace; }}
    .font-bold {{ font-weight: 700; }}
    .font-semibold {{ font-weight: 600; }}
    .text-xs {{ font-size: 12px; }}
    .text-sm {{ font-size: 13.5px; }}
    .text-base {{ font-size: 15px; }}
    .text-lg {{ font-size: 17px; }}
    .text-xl {{ font-size: 20px; }}
    .text-2xl {{ font-size: 24px; }}
    .text-secondary {{ color: #565E74; }}
    .text-on-surface {{ color: #0B1C30; }}
    .text-white {{ color: #FFFFFF; }}
    .gap-1 {{ gap: 4px; }}
    .gap-1-5 {{ gap: 6px; }}
    .gap-2 {{ gap: 8px; }}
    .gap-2-5 {{ gap: 10px; }}
    .gap-3 {{ gap: 12px; }}
    .gap-3-5 {{ gap: 14px; }}

    .ios-switch {{
      width: 44px;
      height: 24px;
      background: #CBD5E1;
      border-radius: 999px;
      position: relative;
      cursor: pointer;
    }}
    .ios-switch::after {{
      content: "";
      position: absolute;
      top: 2px;
      left: 2px;
      width: 20px;
      height: 20px;
      background: #FFF;
      border-radius: 50%;
      transition: all 0.2s;
    }}
    .ios-switch.on {{
      background: #00685F;
    }}
    .ios-switch.on::after {{
      left: 22px;
    }}

    .selection-pill {{
      height: 42px;
      border-radius: 12px;
      background: #FFFFFF;
      border: 1.5px solid #E2E8F0;
      padding: 0 12px;
      display: flex;
      align-items: center;
      gap: 8px;
      font-size: 12px;
      font-weight: 600;
      color: #0B1C30;
      cursor: pointer;
    }}
    .selection-pill.active {{
      border-color: #00685F;
      background: #F0FDFA;
      color: #00685F;
    }}

    .class-card {{
      background: #FFFFFF;
      border: 1.5px solid #E2E8F0;
      border-radius: 12px;
      padding: 10px 4px;
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 4px;
      font-size: 11px;
      font-weight: 700;
      color: #565E74;
      cursor: pointer;
    }}
    .class-card.active {{
      border-color: #00685F;
      background: #F0FDFA;
      color: #00685F;
    }}

    .splash-spinner {{
      width: 32px;
      height: 32px;
      border: 3px solid rgba(137,245,231,0.2);
      border-top-color: #89F5E7;
      border-radius: 50%;
      animation: spin 1s linear infinite;
    }}
    @keyframes spin {{
      to {{ transform: rotate(360deg); }}
    }}

    .legal-trust-banner {{
      background: #F0FDFA;
      border: 1px solid #CCFBF1;
      border-radius: 12px;
      padding: 10px;
      display: flex;
      align-items: flex-start;
      gap: 8px;
      font-size: 11px;
      line-height: 1.4;
      color: #005049;
    }}

    .agreement-box {{
      background: #FFFFFF;
      border: 1.5px solid #E2E8F0;
      border-radius: 14px;
      padding: 12px;
    }}
    .agreement-box.active {{
      border-color: #00685F;
      background: #F0FDFA;
    }}


    /* Additional Styles for Unseen Screens */
    .meter-ticker {{
      font-family: 'Share Tech Mono', 'JetBrains Mono', monospace;
      font-size: 36px;
      font-weight: 700;
      color: #00685F;
      letter-spacing: 2px;
      text-shadow: 0 0 16px rgba(0,104,95,0.25);
    }}
    .battery-circle {{
      width: 130px;
      height: 130px;
      border-radius: 50%;
      border: 9px solid #CCFBF1;
      border-top-color: #00685F;
      border-right-color: #00685F;
      border-bottom-color: #00685F;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
    }}
    .vms-board {{
      background: #050505;
      border: 4px solid #1E293B;
      border-radius: 14px;
      padding: 14px 12px;
      font-family: 'Share Tech Mono', monospace;
      color: #22C55E;
      box-shadow: inset 0 0 20px rgba(0,0,0,0.9), 0 10px 25px rgba(0,0,0,0.7);
      position: relative;
      overflow: hidden;
    }}
    .vms-amber {{ color: #F59E0B; text-shadow: 0 0 8px rgba(245,158,11,0.6); }}
    .vms-green {{ color: #10B981; text-shadow: 0 0 8px rgba(16,185,129,0.6); }}
    .vms-cyan  {{ color: #06B6D4; text-shadow: 0 0 8px rgba(6,182,212,0.6); }}
    .vms-red   {{ color: #EF4444; text-shadow: 0 0 8px rgba(239,68,68,0.6); }}

    .thermal-ticket {{
      background: #FFFEF9;
      color: #1E293B;
      font-family: 'JetBrains Mono', 'Courier New', monospace;
      border: 1px dashed #CBD5E1;
      border-radius: 6px;
      padding: 18px 14px;
      box-shadow: 0 8px 20px -4px rgba(0,0,0,0.12);
      position: relative;
    }}

    /* Studio Wall Grid & Device Scaling */
    .studio-wall-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(390px, 1fr));
      gap: 32px;
      justify-items: center;
      padding: 24px 0 60px;
    }}
    .phone-frame-container {{
      cursor: pointer;
      transition: transform 0.2s ease, box-shadow 0.2s ease;
    }}
    .phone-frame-container:hover {{
      transform: translateY(-4px);
    }}

    /* Zoom levels */
    .zoom-100 .phone {{ transform: scale(1); transform-origin: top center; }}
    .zoom-80 .phone {{ transform: scale(0.8); transform-origin: top center; }}
    .zoom-80 .phone-frame-container {{ height: 690px; }}
    .zoom-65 .phone {{ transform: scale(0.65); transform-origin: top center; }}
    .zoom-65 .phone-frame-container {{ height: 565px; }}

    /* Material Symbols */
    .material-symbols-outlined {{
      font-variation-settings: 'FILL' 0, 'wght' 500, 'GRAD' 0, 'opsz' 20;
      display: inline-block;
      vertical-align: middle;
      line-height: 1;
    }}
    .material-symbols-outlined.fill {{
      font-variation-settings: 'FILL' 1, 'wght' 500, 'GRAD' 0, 'opsz' 20;
    }}
  </style>
</head>
<body class="min-h-screen">

  <!-- Top Global Sticky Header -->
  <header class="sticky top-0 z-50 bg-[#0B1220]/95 backdrop-blur-md border-b border-slate-800 px-6 py-3.5 flex flex-wrap items-center justify-between gap-4">
    <div class="flex items-center gap-3.5">
      <div class="w-10 h-10 rounded-xl bg-gradient-to-tr from-[#00685F] to-[#10B981] flex items-center justify-center text-white font-bold text-lg shadow-lg shadow-teal-500/20">
        P
      </div>
      <div>
        <div class="flex items-center gap-2">
          <h1 class="text-base font-bold text-white tracking-tight">ParkSpot Driver UI Suite</h1>
          <span class="px-2 py-0.5 rounded-full text-[10px] font-bold uppercase tracking-wider bg-teal-500/10 text-teal-400 border border-teal-500/20">Google Stitch MCP</span>
          <span class="px-2 py-0.5 rounded-full text-[10px] font-bold uppercase tracking-wider bg-indigo-500/10 text-indigo-400 border border-indigo-500/20">Complete 45-Screen Master Flow</span>
        </div>
        <p class="text-xs text-slate-400 mt-0.5">Project <code class="font-mono text-slate-300">15000274080821385749</code> • Launch → 3-Step Onboarding → Auth &amp; Forgot Password → Flagship 5-Tabs → B2 Bay &amp; Quote ₹76.70 → Floating Meter, EV 60kW, Overstay &amp; Physical VMS</p>
      </div>
    </div>

    <!-- Controls: Search, View Mode & Zoom -->
    <div class="flex items-center gap-3">
      <!-- Search Input -->
      <div class="relative w-48 sm:w-64">
        <span class="absolute left-3 top-2.5 text-slate-400 material-symbols-outlined text-[16px]">search</span>
        <input id="screenSearchInput" oninput="handleSearch(this.value)" type="text" placeholder="Search screen by title/ID..." class="w-full bg-slate-900 border border-slate-700/80 rounded-lg pl-8 pr-3 py-1.5 text-xs text-white placeholder-slate-500 focus:outline-none focus:border-teal-500"/>
      </div>

      <!-- Zoom Toggle (Studio Wall) -->
      <div id="zoomControls" class="flex items-center bg-slate-900 rounded-lg border border-slate-800 p-0.5 text-xs">
        <button type="button" onclick="setZoom('65')" id="zoom65Btn" class="px-2.5 py-1 rounded text-slate-400 hover:text-white">65%</button>
        <button type="button" onclick="setZoom('80')" id="zoom80Btn" class="px-2.5 py-1 rounded bg-teal-600 text-white font-bold">80%</button>
        <button type="button" onclick="setZoom('100')" id="zoom100Btn" class="px-2.5 py-1 rounded text-slate-400 hover:text-white">100%</button>
      </div>

      <!-- Mode Selector -->
      <div class="flex items-center bg-slate-900 rounded-lg border border-slate-800 p-0.5 text-xs">
        <button id="viewWallBtn" type="button" onclick="setViewMode('wall')" class="px-3 py-1.5 rounded-md font-semibold bg-teal-600 text-white shadow-sm flex items-center gap-1.5">
          <span class="material-symbols-outlined text-[15px]">view_quilt</span> Studio Wall
        </button>
        <button id="viewStageBtn" type="button" onclick="setViewMode('stage')" class="px-3 py-1.5 rounded-md font-semibold text-slate-400 hover:text-white flex items-center gap-1.5">
          <span class="material-symbols-outlined text-[15px]">smartphone</span> Stage Focus
        </button>
      </div>

      <!-- Full 53-Screen Master Flow Link -->
      <a href="../flow-driver.html" class="px-3 py-1.5 rounded-lg text-xs font-semibold bg-slate-800 hover:bg-slate-700 text-teal-300 hover:text-teal-200 border border-slate-700 flex items-center gap-1">
        <span>Full 53 Screens</span>
        <span class="material-symbols-outlined text-[14px]">arrow_forward</span>
      </a>
    </div>
  </header>

  <!-- Stage Filter Navigation Bar -->
  <nav class="border-b border-slate-800/80 bg-slate-950/70 px-6 py-2.5 overflow-x-auto flex items-center gap-2 text-xs no-scrollbar">
    <span class="text-slate-500 font-bold uppercase text-[10px] tracking-wider shrink-0 mr-1 flex items-center gap-1">
      <span class="material-symbols-outlined text-[14px]">route</span> JOURNEY:
    </span>
    {"".join(pills_html)}
  </nav>

  <!-- Main View Container -->
  <main class="px-6 py-6 max-w-full">

    <!-- STUDIO WALL VIEW (Default Panoramic Gallery) -->
    <section id="wallView" class="zoom-80">
      <div id="gridContainer" class="studio-wall-grid">
        {"".join(grid_cards_html)}
      </div>
    </section>

    <!-- INTERACTIVE DEVICE STAGE VIEW -->
    <section id="stageView" class="hidden flex flex-col items-center justify-center py-4">
      <!-- Stage Nav Controls -->
      <div class="flex flex-wrap items-center justify-between gap-4 w-full max-w-5xl mb-6 bg-slate-900/90 p-3.5 rounded-2xl border border-slate-800">
        <div class="flex items-center gap-2">
          <button type="button" onclick="prevStageScreen()" class="px-3.5 py-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-white text-xs font-bold flex items-center gap-1 transition-all">
            <span class="material-symbols-outlined text-[16px]">arrow_back</span> Prev
          </button>
          <button type="button" onclick="nextStageScreen()" class="px-3.5 py-2 rounded-xl bg-teal-600 hover:bg-teal-500 text-white text-xs font-bold flex items-center gap-1 transition-all">
            Next <span class="material-symbols-outlined text-[16px]">arrow_forward</span>
          </button>
        </div>

        <!-- Jump Dropdown -->
        <div class="flex items-center gap-2">
          <span class="text-xs text-slate-400 font-semibold">Jump to:</span>
          <select id="stageJumpSelect" onchange="openInStage(this.value)" class="bg-slate-950 border border-slate-700 text-white text-xs rounded-lg px-3 py-2 font-medium focus:outline-none focus:border-teal-500">
            {"".join(jump_options)}
          </select>
        </div>

        <div class="text-xs font-mono text-teal-400" id="stageCounter">Screen 1 of {len(screens)}</div>
      </div>

      <!-- Device & Spec Dossier Layout -->
      <div class="flex flex-col lg:flex-row items-center lg:items-start justify-center gap-10 w-full max-w-5xl">
        <!-- Centerpiece Phone Frame -->
        <div class="flex flex-col items-center">
          <div id="stagePhoneContainer" class="phone">
            <!-- Dynamic Injection -->
            <div id="stageViewport" class="phone-viewport"></div>
            <div class="home-indicator"></div>
          </div>
        </div>

        <!-- Accompanying Screen Dossier Card -->
        <div class="w-full lg:w-96 flex flex-col gap-4">
          <div class="card p-5 bg-slate-900 border border-slate-800 text-white">
            <div class="flex items-center justify-between mb-2">
              <span id="dossierId" class="font-mono text-sm font-bold text-teal-400">STITCH-01</span>
              <span id="dossierStage" class="badge-chip teal">Launch &amp; Onboarding</span>
            </div>
            <h2 id="dossierTitle" class="text-lg font-bold text-white mb-1.5">App Launch &amp; Splash</h2>
            <p id="dossierDesc" class="text-xs text-slate-300 leading-relaxed">
              Native branded launch screen with glowing teal ParkSpot glyph, tagline, and MoRTH/NPCI certification badge.
            </p>

            <div class="mt-4 pt-3 border-t border-slate-800 space-y-2 text-xs">
              <div class="flex justify-between">
                <span class="text-slate-400">UX Intent:</span>
                <span id="dossierIntent" class="text-slate-200 font-medium text-right">Initial cold start</span>
              </div>
              <div class="flex justify-between">
                <span class="text-slate-400">Master Spec Invariant:</span>
                <span id="dossierSpec" class="text-teal-400 font-mono text-right font-bold">SAC 999113</span>
              </div>
            </div>

            <div id="dossierStandaloneBtn" class="mt-4 pt-3 border-t border-slate-800">
              <!-- Standalone link if applicable -->
            </div>
          </div>

          <!-- Quick Navigation Tip -->
          <div class="card p-4 bg-slate-900/60 border border-slate-800 text-xs text-slate-400 space-y-1.5">
            <div class="font-bold text-slate-300 flex items-center gap-1.5">
              <span class="material-symbols-outlined text-[16px] text-teal-400">keyboard</span> Keyboard Navigation
            </div>
            <p>Use <kbd class="px-1.5 py-0.5 rounded bg-slate-800 text-slate-300 font-mono text-[10px]">←</kbd> and <kbd class="px-1.5 py-0.5 rounded bg-slate-800 text-slate-300 font-mono text-[10px]">→</kbd> keys to step through the entire driver journey.</p>
          </div>
        </div>
      </div>
    </section>

  </main>

  <!-- Screens JavaScript Data & Controller -->
  <script>
    const screensData = {str(screens).replace("None", "null").replace("True", "true").replace("False", "false")};
    let currentStageIndex = 0;
    let currentStageFilter = "All";

    function setViewMode(mode) {{
      const wallView = document.getElementById('wallView');
      const stageView = document.getElementById('stageView');
      const viewWallBtn = document.getElementById('viewWallBtn');
      const viewStageBtn = document.getElementById('viewStageBtn');
      const zoomControls = document.getElementById('zoomControls');

      if (mode === 'wall') {{
        wallView.classList.remove('hidden');
        stageView.classList.add('hidden');
        zoomControls.classList.remove('hidden');
        viewWallBtn.className = "px-3 py-1.5 rounded-md font-semibold bg-teal-600 text-white shadow-sm flex items-center gap-1.5";
        viewStageBtn.className = "px-3 py-1.5 rounded-md font-semibold text-slate-400 hover:text-white flex items-center gap-1.5";
      }} else {{
        wallView.classList.add('hidden');
        stageView.classList.remove('hidden');
        zoomControls.classList.add('hidden');
        viewWallBtn.className = "px-3 py-1.5 rounded-md font-semibold text-slate-400 hover:text-white flex items-center gap-1.5";
        viewStageBtn.className = "px-3 py-1.5 rounded-md font-semibold bg-teal-600 text-white shadow-sm flex items-center gap-1.5";
        renderStage();
      }}
    }}

    function setZoom(level) {{
      const wall = document.getElementById('wallView');
      wall.className = `zoom-${{level}}`;
      document.getElementById('zoom65Btn').className = level === '65' ? "px-2.5 py-1 rounded bg-teal-600 text-white font-bold" : "px-2.5 py-1 rounded text-slate-400 hover:text-white";
      document.getElementById('zoom80Btn').className = level === '80' ? "px-2.5 py-1 rounded bg-teal-600 text-white font-bold" : "px-2.5 py-1 rounded text-slate-400 hover:text-white";
      document.getElementById('zoom100Btn').className = level === '100' ? "px-2.5 py-1 rounded bg-teal-600 text-white font-bold" : "px-2.5 py-1 rounded text-slate-400 hover:text-white";
    }}

    function filterByStage(stageId, btnEl) {{
      currentStageFilter = stageId;
      document.querySelectorAll('.stage-pill-btn').forEach(b => {{
        b.className = "stage-pill-btn px-3 py-1.5 rounded-lg text-xs font-semibold border border-slate-700/80 shrink-0 transition-all bg-slate-800/80 text-slate-300 hover:text-white";
      }});
      btnEl.className = "stage-pill-btn px-3 py-1.5 rounded-lg text-xs font-semibold border border-slate-700/80 shrink-0 transition-all bg-teal-600 text-white font-bold";

      const items = document.querySelectorAll('.screen-grid-item');
      items.forEach(item => {{
        const itemStage = item.getAttribute('data-stage');
        if (stageId === 'All' || itemStage === stageId) {{
          item.classList.remove('hidden');
        }} else {{
          item.classList.add('hidden');
        }}
      }});
    }}

    function handleSearch(q) {{
      const term = q.trim().toLowerCase();
      const items = document.querySelectorAll('.screen-grid-item');
      items.forEach(item => {{
        const searchData = item.getAttribute('data-search') || '';
        if (!term || searchData.includes(term)) {{
          item.classList.remove('hidden');
        }} else {{
          item.classList.add('hidden');
        }}
      }});
    }}

    function openInStage(idx) {{
      currentStageIndex = parseInt(idx, 10);
      setViewMode('stage');
      renderStage();
    }}

    function prevStageScreen() {{
      if (currentStageIndex > 0) {{
        currentStageIndex--;
        renderStage();
      }}
    }}

    function nextStageScreen() {{
      if (currentStageIndex < screensData.length - 1) {{
        currentStageIndex++;
        renderStage();
      }}
    }}

    function renderStage() {{
      const sc = screensData[currentStageIndex];
      const viewport = document.getElementById('stageViewport');
      const phoneContainer = document.getElementById('stagePhoneContainer');
      
      phoneContainer.style.background = sc.bg || "#F8F9FF";
      viewport.innerHTML = sc.html;

      // Update Dossier
      document.getElementById('dossierId').textContent = sc.id;
      document.getElementById('dossierStage').textContent = sc.stage_name;
      document.getElementById('dossierTitle').textContent = sc.title;
      document.getElementById('dossierDesc').textContent = sc.desc;
      document.getElementById('dossierIntent').textContent = sc.dossier?.intent || "Primary user interaction checkpoint";
      document.getElementById('dossierSpec').textContent = sc.dossier?.invariant || sc.dossier?.spec || "Google Stitch M3 Verified";

      const standBtn = document.getElementById('dossierStandaloneBtn');
      if (sc.iframe_link) {{
        standBtn.innerHTML = `<a href="${{sc.iframe_link}}" target="_blank" class="w-full pro-btn secondary sm flex items-center justify-center gap-1.5"><span class="material-symbols-outlined text-[15px]">open_in_new</span> Open Standalone Screen View</a>`;
      }} else {{
        standBtn.innerHTML = '';
      }}

      // Dropdown & Counter
      document.getElementById('stageJumpSelect').value = currentStageIndex;
      document.getElementById('stageCounter').textContent = `Screen ${{currentStageIndex + 1}} of ${{screensData.length}}`;
    }}

    // Keyboard Arrow Navigation
    window.addEventListener('keydown', (e) => {{
      const stageView = document.getElementById('stageView');
      if (!stageView.classList.contains('hidden')) {{
        if (e.key === 'ArrowLeft') prevStageScreen();
        if (e.key === 'ArrowRight') nextStageScreen();
      }}
    }});
  </script>
</body>
</html>"""

    (OUT_DIR / "index.html").write_text(html, encoding="utf-8")
    print(f"Successfully generated Google Stitch Suite viewer at {OUT_DIR / 'index.html'} with {len(screens)} screens!")

if __name__ == "__main__":
    build_stitch_suite()
