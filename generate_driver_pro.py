#!/usr/bin/env python3
"""
Complete Flagship ParkSpot Driver UI Generator.
Implements the Industry Standard Mobile Application UX Flow Architecture:
  1. STAGE 01: Standard Launch, Onboarding & Auth Suite (12 Screens)
     - App Launch / Native Splash
     - Onboarding 1: Find & Compare Parking
     - Onboarding 2: Guaranteed Bay Reservation
     - Onboarding 3: Contactless Ingress & Exit
     - Welcome / Auth Gateway
     - Login Screen (Email/Phone, Password + Eye Toggle, Forgot Password, Biometrics)
     - Register Screen (Full Name, Phone +91, Email, Password + Strength Meter, Terms Checkbox)
     - Forgot Password Step 1: Request Code
     - Forgot Password Step 2: Verify 6-Digit OTP
     - Forgot Password Step 3: Set New Password
     - Terms of Service (Dedicated Full Screen)
     - Privacy Policy & DPDP Notice (Dedicated Full Screen)
  2. STAGE 02: Flagship Home Screen & Standard 5-Tab Navigation Suite (5 Screens)
     - Tab 1: Home Screen (Location Selector, Search HUD, Categories, Live Active Banner, Nearby Carousel)
     - Tab 2: Bookings Screen (Active Ticket Countdown, Upcoming, Completed History)
     - Tab 3: Garage Screen (HSRP Plates, EV Profile, FASTag NETC Status)
     - Tab 4: Wallet Screen (₹840 Balance Card, Monthly Pass, UPI AutoPay, Ledger)
     - Tab 5: Profile Screen (Verified Driver Header, Account Settings, DPDP Privacy Desk, Logout)
  3. STAGE 03: Vehicle Passport, HSRP Plates & Garage Management (4 Screens)
  4. STAGE 04: Map Discovery & Search HUD (4 Screens)
  5. STAGE 05: Facility Telemetry & 2D Blueprint Deck Bay Selector (4 Screens)
  6. STAGE 06: Statutory Quote & Secure 1-Tap UPI Checkout (8 Screens - ₹76.70 Invariant)
  7. STAGE 07: Ingress Wayfinding & Live Gate Clearance (4 Screens)
  8. STAGE 08: Active Dwell Session, EV Fast Charging & Exit Invoice (6 Screens)
  9. STAGE 09: Incident Recovery, SOS Support & DPDP Data Rights (6 Screens)

Produces docs/figma-mockups/flow-driver.html (53 Screens Total).
"""
import os
from pathlib import Path

OUT_DIR = Path("/Users/maheshgiri/Documents/Projects/Parking/docs/figma-mockups")

def build_driver_page():
    # Asset references
    ASSETS = {
        "facility": "assets/parkspot-facility-hero.jpg",
        "garage": "assets/parkspot-garage-b2.jpg",
        "garage_stock": "assets/garage-hero.jpg",
        "levels": "assets/parking-levels.jpg",
        "map": "assets/parkspot-map-base.jpg",
        "car": "assets/car-detail.jpg",
        "plate": "assets/parkspot-hsrp-plate.jpg",
        "qr": "assets/qr-pass.png",
        "city": "assets/city-street.jpg",
        "night": "assets/night-city.jpg",
        "desk": "assets/desk.jpg",
        "sign": "assets/parking-sign.jpg",
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

    # Industry Standard 5-Tab Navigation Bar
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

    def phone(sid, title, inner, bg="var(--canvas)"):
        return f"""
        <article class="phone-frame-wrapper">
          <header class="screen-meta">
            <span class="screen-id">{sid}</span>
            <span class="screen-name">{title}</span>
          </header>
          <div class="phone" style="background:{bg};">
            <div class="phone-viewport">{inner}</div>
            <div class="home-indicator"></div>
          </div>
        </article>"""

    def phase_divider(phase_num, title, desc, screen_range):
        return f"""
        <div class="phase-divider">
          <div class="phase-badge">STAGE 0{phase_num}</div>
          <div class="phase-info">
            <h2 class="phase-title">{title}</h2>
            <p class="phase-desc">{desc}</p>
          </div>
          <div class="phase-range">{screen_range}</div>
        </div>"""

    sections = []

    # ═══════════════════════════════════════════════════════════════════════════
    # STAGE 01: STANDARD LAUNCH, ONBOARDINGS, AUTH SUITE & POLICIES (12 SCREENS)
    # ═══════════════════════════════════════════════════════════════════════════
    p1 = []

    # STD-01: App Launch / Native Splash
    p1.append(phone("STD-01", "App Launch / Splash", f"""
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
    """, bg="#0B1C30"))

    # STD-02: Onboarding 1 - Real-Time Discovery
    p1.append(phone("STD-02", "Onboarding: Discover", f"""
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
    """))

    # STD-03: Onboarding 2 - Guaranteed Bay Reservation
    p1.append(phone("STD-03", "Onboarding: Reserve", f"""
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
    """))

    # STD-04: Onboarding 3 - Contactless Ingress & Exit
    p1.append(phone("STD-04", "Onboarding: Ingress", f"""
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
    """))

    # STD-05: Welcome / Auth Gateway
    p1.append(phone("STD-05", "Welcome & Gateway", f"""
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
    """, bg="#0B1C30"))

    # STD-06: Standard Login Screen
    p1.append(phone("STD-06", "Login Screen", f"""
      {status_bar()}
      {nav_header("Sign In", "Welcome Back")}
      <div class="screen-body space-y-4">
        <div>
          <h2 class="text-xl font-bold text-on-surface">Welcome Back</h2>
          <p class="text-xs text-secondary mt-0.5">Sign in to manage your garage, bookings, and FastTag passes.</p>
        </div>

        <div class="card p-4 space-y-3.5">
          <div>
            <label class="input-label" for="login-identifier">EMAIL OR MOBILE NUMBER</label>
            <div class="input-field">
              {icon("mail", size=18, extra_style="color:#565E74;")}
              <input id="login-identifier" name="login_identifier" type="text" value="mahesh.giri@example.com" readonly/>
            </div>
          </div>

          <div>
            <div class="flex items-center justify-between mb-1">
              <label class="input-label mb-0" for="login-password">PASSWORD</label>
              <span class="text-[11px] font-bold text-[#00685F] cursor-pointer">Forgot Password?</span>
            </div>
            <div class="input-field">
              {icon("lock", size=18, extra_style="color:#565E74;")}
              <input id="login-password" name="login_password" type="password" value="••••••••••••" style="letter-spacing:2px;" readonly/>
              <button type="button" class="eye-toggle-btn" aria-label="Toggle password visibility">
                {icon("visibility", size=18, extra_style="color:#565E74;")}
              </button>
            </div>
          </div>

          <div class="flex items-center justify-between pt-1">
            <label class="flex items-center gap-2 cursor-pointer">
              <input type="checkbox" id="remember-me-chk" checked class="accent-[#00685F] w-4 h-4 rounded"/>
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
        {btn("Log In", "primary", icon_name="login", btn_id="btn-login-submit")}
        <div class="text-center mt-3 text-xs text-secondary">
          Don't have an account? <strong class="text-[#00685F] cursor-pointer">Sign Up</strong>
        </div>
      </div>
    """))

    # STD-07: Standard Register Screen
    p1.append(phone("STD-07", "Register / Sign Up", f"""
      {status_bar()}
      {nav_header("Create Account", "Driver Registration")}
      <div class="screen-body space-y-3">
        <div>
          <h2 class="text-xl font-bold text-on-surface">Create Account</h2>
          <p class="text-xs text-secondary mt-0.5">Experience guaranteed urban parking in 240+ facilities.</p>
        </div>

        <div class="card p-3.5 space-y-2.5">
          <div>
            <label class="input-label" for="reg-fullname">FULL LEGAL NAME</label>
            <div class="input-field">
              {icon("person", size=18, extra_style="color:#565E74;")}
              <input id="reg-fullname" name="reg_fullname" type="text" value="Mahesh Giri" readonly/>
            </div>
          </div>

          <div>
            <label class="input-label" for="reg-phone">MOBILE PHONE NUMBER</label>
            <div class="phone-input-row">
              <div class="phone-prefix">
                <span class="flag-icon">🇮🇳</span>
                <span>+91</span>
              </div>
              <input id="reg-phone" name="reg_phone" class="phone-text-input" type="text" value="98765 43210" readonly/>
            </div>
          </div>

          <div>
            <label class="input-label" for="reg-email">EMAIL ADDRESS (FOR GST TAX INVOICES)</label>
            <div class="input-field">
              {icon("mail", size=18, extra_style="color:#565E74;")}
              <input id="reg-email" name="reg_email" type="email" value="mahesh.giri@example.com" readonly/>
            </div>
          </div>

          <div>
            <label class="input-label" for="reg-password">SET SECURE PASSWORD</label>
            <div class="input-field">
              {icon("lock", size=18, extra_style="color:#565E74;")}
              <input id="reg-password" name="reg_password" type="password" value="••••••••••••" style="letter-spacing:2px;" readonly/>
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
            <input type="checkbox" id="reg-consent-chk" checked class="accent-[#00685F] w-4 h-4 rounded mt-0.5"/>
            <div class="text-[11px] text-secondary leading-normal">
              I agree to the <strong class="text-[#00685F]">Terms of Service</strong> and acknowledge the <strong class="text-[#00685F]">DPDP Privacy Policy</strong> for FASTag &amp; HSRP plate processing.
            </div>
          </label>
        </div>
      </div>
      <div class="sticky-footer">
        {btn("Create Driver Account", "primary", icon_name="person_add", btn_id="btn-register-submit")}
        <div class="text-center mt-2.5 text-xs text-secondary">
          Already registered? <strong class="text-[#00685F] cursor-pointer">Log In</strong>
        </div>
      </div>
    """))

    # STD-08: Forgot Password - Step 1: Request Code
    p1.append(phone("STD-08", "Forgot Password: Step 1", f"""
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
            <label class="input-label" for="fp-identifier">REGISTERED EMAIL OR MOBILE</label>
            <div class="input-field">
              {icon("contact_mail", size=18, extra_style="color:#565E74;")}
              <input id="fp-identifier" name="fp_identifier" type="text" value="mahesh.giri@example.com" readonly/>
            </div>
          </div>

          <div class="legal-trust-banner">
            {icon("verified_user", size=15, extra_style="color:#00685F;flex-shrink:0;")}
            <p>Verification link will expire in 10 minutes to protect your account and garage access.</p>
          </div>
        </div>
      </div>
      <div class="sticky-footer">
        {btn("Send 6-Digit Code", "primary", icon_name="send", btn_id="btn-fp-send")}
        <div class="text-center mt-3 text-xs text-secondary">
          Remember password? <strong class="text-[#00685F] cursor-pointer">Back to Log In</strong>
        </div>
      </div>
    """))

    # STD-09: Forgot Password - Step 2: Verify OTP
    p1.append(phone("STD-09", "Forgot Password: Step 2", f"""
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
        {btn("Verify & Continue", "primary", icon_name="check", btn_id="btn-fp-verify")}
      </div>
    """))

    # STD-10: Forgot Password - Step 3: Set New Password
    p1.append(phone("STD-10", "Forgot Password: Step 3", f"""
      {status_bar()}
      {nav_header("Set New Password", "Secure Your Account")}
      <div class="screen-body space-y-3.5">
        <div>
          <h2 class="text-xl font-bold text-on-surface">Set New Password</h2>
          <p class="text-xs text-secondary mt-0.5">Your new password must be distinct from previously used credentials.</p>
        </div>

        <div class="card p-4 space-y-3">
          <div>
            <label class="input-label" for="new-password">NEW PASSWORD</label>
            <div class="input-field">
              {icon("lock", size=18, extra_style="color:#565E74;")}
              <input id="new-password" name="new_password" type="password" value="••••••••••••" style="letter-spacing:2px;" readonly/>
              <button type="button" class="eye-toggle-btn" aria-label="Toggle password visibility">
                {icon("visibility", size=18, extra_style="color:#565E74;")}
              </button>
            </div>
          </div>

          <div>
            <label class="input-label" for="confirm-password">CONFIRM NEW PASSWORD</label>
            <div class="input-field">
              {icon("check_circle", size=18, extra_style="color:#006947;")}
              <input id="confirm-password" name="confirm_password" type="password" value="••••••••••••" style="letter-spacing:2px;" readonly/>
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
        {btn("Update Password & Log In", "primary", icon_name="task_alt", btn_id="btn-fp-finish")}
      </div>
    """))

    # STD-11: Full Terms of Service Screen
    p1.append(phone("STD-11", "Terms of Service", f"""
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
    """))

    # STD-12: Full Privacy Policy & DPDP Notice Screen
    p1.append(phone("STD-12", "Privacy Policy & DPDP", f"""
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
    """))

    sections.append(phase_divider(1, "Standard Launch, Onboarding & Auth Journey", "Industry-standard mobile UX architecture: Splash, 3-step carousel, Welcome Gateway, Login, Register, 3-step Forgot Password, and DPDP Legal Terms.", "STD-01 → STD-12 (12 Screens)"))
    sections.append(f'<div class="screens-horizontal-row">{"".join(p1)}</div>')

    # ═══════════════════════════════════════════════════════════════════════════
    # STAGE 02: FLAGSHIP 5-TAB NAVIGATION SUITE (5 SCREENS)
    # ═══════════════════════════════════════════════════════════════════════════
    p2 = []

    # TAB-01: Tab 1 - Flagship Home Screen (Home Active)
    p2.append(phone("TAB-01", "Tab 1: Home (Flagship)", f"""
      {status_bar()}
      <!-- Home App Bar with Location Selector -->
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
          <input id="home-search-input" name="home_search" type="text" placeholder="Search destination, mall, metro station..." value="" readonly/>
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

        <!-- Recommended Nearby Facilities Carousel -->
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
    """))

    # TAB-02: Tab 2 - Flagship Bookings Screen (Bookings Active)
    p2.append(phone("TAB-02", "Tab 2: Bookings (Flagship)", f"""
      {status_bar()}
      {nav_header("My Bookings", "Active & Past Reservations", back=False, right_icon="history")}
      <div class="screen-body space-y-3">
        <!-- Segmented Control -->
        <div class="segmented-control">
          <div class="seg-btn active">Active (1)</div>
          <div class="seg-btn">Upcoming (1)</div>
          <div class="seg-btn">Past (14)</div>
        </div>

        <!-- Active Booking Ticket Card -->
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

        <!-- Upcoming Reservation -->
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
    """))

    # TAB-03: Tab 3 - Flagship Garage Screen (Garage Active)
    p2.append(phone("TAB-03", "Tab 3: Garage (Flagship)", f"""
      {status_bar()}
      {nav_header("Vehicle Garage", "Linked HSRP Passports & FASTag", back=False, right_icon="add")}
      <div class="screen-body space-y-3">
        <!-- Vehicle 1: Tata Nexon EV (Default) -->
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

        <!-- Vehicle 2: Activa -->
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
    """))

    # TAB-04: Tab 4 - Flagship Wallet Screen (Wallet Active)
    p2.append(phone("TAB-04", "Tab 4: Wallet (Flagship)", f"""
      {status_bar()}
      {nav_header("ParkSpot Wallet", "Cash, Passes & AutoPay", back=False, right_icon="qr_code")}
      <div class="screen-body space-y-3.5">
        <!-- Wallet Balance Card -->
        <div class="wallet-balance-card">
          <div class="text-[10px] text-slate-300 font-bold uppercase tracking-wider">AVAILABLE BALANCE</div>
          <div class="text-2xl font-bold font-mono mt-1 text-white">₹840.00</div>
          <p class="text-[11px] text-slate-200 mt-0.5">Instant refunds &amp; contactless barrier tolls</p>
          <div class="flex gap-2 mt-3.5">
            <button class="pro-btn sm bg-white text-[#0B1C30] font-bold" type="button">+ Add Funds</button>
            <button class="pro-btn sm bg-white/10 text-white border border-white/20" type="button">Refund / Withdraw</button>
          </div>
        </div>

        <!-- Monthly Pass Card -->
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

        <!-- UPI AutoPay Pre-Auth Status -->
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

        <!-- Recent Ledger -->
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
    """))

    # TAB-05: Tab 5 - Flagship Profile Screen (Profile Active)
    p2.append(phone("TAB-05", "Tab 5: Profile (Flagship)", f"""
      {status_bar()}
      {nav_header("Driver Profile", "Account & Preferences", back=False, right_icon="settings")}
      <div class="screen-body space-y-3.5">
        <!-- Profile Header Card -->
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

        <!-- Settings Links Groups -->
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
              <div class="icon-circle teal">{icon("support_agent", size=18)}</div>
              <span class="text-xs font-bold text-on-surface">Emergency Gate Intercom &amp; Help</span>
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

        <div class="text-center text-[10px] text-secondary">
          ParkSpot v5.0.2 (Build 2026.10) • ISO/IEC 27001 Certified
        </div>
      </div>
      {tabbar("Profile")}
    """))

    sections.append(phase_divider(2, "Flagship Home Screen & Standard 5-Tab Navigation Suite", "The 5 primary destinations of the ParkSpot driver app: Home, Bookings, Garage, Wallet, and Profile — all sharing the unified 5-tab bottom navigation bar.", "TAB-01 → TAB-05 (5 Screens)"))
    sections.append(f'<div class="screens-horizontal-row">{"".join(p2)}</div>')

    # ═══════════════════════════════════════════════════════════════════════════
    # STAGE 03: VEHICLE PASSPORT, HSRP PLATES & GARAGE HUB (4 SCREENS)
    # ═══════════════════════════════════════════════════════════════════════════
    p3 = []

    # DRV-18E: Garage Empty State
    p3.append(phone("DRV-18E", "Garage Empty State", f"""
      {status_bar()}
      {nav_header("My Vehicle Garage", "0 Vehicles Registered")}
      <div class="screen-body flex flex-col items-center justify-center text-center p-6">
        <div class="empty-graphic-circle">
          {icon("directions_car", size=36, extra_style="color:#00685F;")}
        </div>
        <h3 class="text-base font-bold text-on-surface mt-4">No Vehicles Added Yet</h3>
        <p class="text-xs text-secondary mt-1 max-w-[260px]">Add your primary vehicle to enable 1-tap bay booking, FASTag gate ingress, and EV charging.</p>
        
        <div class="sample-plate-preview mt-6">
          <div class="text-[9px] text-secondary font-bold uppercase tracking-wider mb-1">Standard Indian HSRP Format</div>
          {hsrp_badge("KA 01 AB 0000")}
        </div>
      </div>
      <div class="sticky-footer">
        {btn("Add Your First Vehicle", "primary", icon_name="add")}
      </div>
      {tabbar("Garage")}
    """))

    # DRV-18A: Add Vehicle Sheet
    p3.append(phone("DRV-18A", "Add Vehicle Sheet", f"""
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
          <label class="input-label" for="add-plate-input">HSRP NUMBER PLATE</label>
          <div class="input-field">
            {icon("pin", size=18, extra_style="color:#565E74;")}
            <input id="add-plate-input" name="add_plate" type="text" value="KA 01 MJ 8821" style="font-family:'Share Tech Mono', monospace; font-size:16px; font-weight:700;" readonly/>
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
    """))

    # DRV-18F: Vehicle Class Selector
    p3.append(phone("DRV-18F", "Class Selector Detail", f"""
      {status_bar()}
      {nav_header("Select Vehicle Class", "Tariff & Dimension Matching")}
      <div class="screen-body space-y-2.5">
        <p class="text-xs text-secondary px-1">Tariff category and garage ramp clearance are strictly determined by vehicle classification.</p>
        
        <div class="card p-3 border-2 border-[#00685F] bg-[#00685F]/[0.02] flex items-center justify-between">
          <div class="flex items-center gap-3">
            <div class="icon-circle teal">{icon("directions_car", size=20)}</div>
            <div>
              <div class="font-bold text-xs text-on-surface">Standard Passenger Car (Sedan/Hatch)</div>
              <div class="text-[10px] text-secondary">Length &lt; 4.5m • Width &lt; 1.8m • Standard Bay</div>
            </div>
          </div>
          {icon("radio_button_checked", size=18, extra_style="color:#00685F;")}
        </div>

        <div class="card p-3 flex items-center justify-between">
          <div class="flex items-center gap-3">
            <div class="icon-circle slate">{icon("airport_shuttle", size=20)}</div>
            <div>
              <div class="font-bold text-xs text-on-surface">Compact SUV / Crossover</div>
              <div class="text-[10px] text-secondary">Height up to 1.75m • Requires standard bay clearance</div>
            </div>
          </div>
          {icon("radio_button_unchecked", size=18, extra_style="color:#565E74;")}
        </div>

        <div class="card p-3 flex items-center justify-between">
          <div class="flex items-center gap-3">
            <div class="icon-circle slate">{icon("two_wheeler", size=20)}</div>
            <div>
              <div class="font-bold text-xs text-on-surface">Motorcycle / Scooter (2W)</div>
              <div class="text-[10px] text-secondary">Dedicated 2W bay • ₹15/hr base tariff</div>
            </div>
          </div>
          {icon("radio_button_unchecked", size=18, extra_style="color:#565E74;")}
        </div>
      </div>
      <div class="sticky-footer">
        {btn("Confirm Class Selection", "primary")}
      </div>
      {tabbar("Garage")}
    """))

    # DRV-18V: Compatibility & Clearance Check
    p3.append(phone("DRV-18V", "Clearance Telemetry", f"""
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
    """))

    sections.append(phase_divider(3, "Vehicle Passport, HSRP Plates & Garage Management", "Physical HSRP plate rendering, 6 vehicle class selectors, FASTag linking, and vertical clearance verification.", "DRV-18E → DRV-18V (4 Screens)"))
    sections.append(f'<div class="screens-horizontal-row">{"".join(p3)}</div>')

    # ═══════════════════════════════════════════════════════════════════════════
    # STAGE 04: MAP DISCOVERY & SEARCH HUD (4 SCREENS)
    # ═══════════════════════════════════════════════════════════════════════════
    p4 = []

    # DRV-01M: Map-First Discovery
    p4.append(phone("DRV-01M", "Vector Transit Map", f"""
      <div style="flex:1;position:relative;background:#E2E8F0;overflow:hidden;">
        <img class="img-cover" src="{ASSETS['map']}" alt="City Map Base"/>
        {status_bar()}

        <!-- Top Floating Search HUD -->
        <div style="position:absolute;top:54px;left:16px;right:16px;z-index:20;">
          <div class="search-hud-bar">
            {icon("search", size=20, extra_style="color:#00685F;")}
            <input id="map-search-field" name="map_search" type="text" value="Forum South Mall, Bengaluru" readonly/>
            <button type="button" class="filter-tune-btn" aria-label="Open Filters">{icon("tune", size=16)}</button>
          </div>
        </div>

        <!-- Floating Map Pin Marker -->
        <div style="position:absolute;top:40%;left:52%;transform:translate(-50%,-100%);z-index:20;cursor:pointer;">
          <div class="map-pin-bubble active">
            <span class="font-bold">₹60</span>
            <span class="text-[9px]">• 42 free</span>
          </div>
          <div class="map-pin-stem"></div>
        </div>

        <!-- Bottom Sheet Card Preview -->
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
    """))

    # DRV-01S: Search HUD & Autocomplete
    p4.append(phone("DRV-01S", "Search HUD & Recents", f"""
      {status_bar()}
      <div class="p-3 border-b border-slate-200">
        <div class="search-hud-bar">
          {icon("search", size=20, extra_style="color:#00685F;")}
          <input id="search-hud-input" name="search_hud" type="text" value="Forum South" readonly/>
          {icon("close", size=18, extra_style="color:#565E74;cursor:pointer;")}
        </div>
      </div>
      <div class="screen-body space-y-3">
        <div class="text-[10px] text-secondary font-bold uppercase tracking-wider">MATCHING DESTINATIONS</div>

        <div class="card p-3 space-y-2 divide-y divide-slate-100">
          <div class="pt-1 flex items-start gap-2.5 cursor-pointer">
            <div class="icon-circle teal">{icon("local_parking", size=16)}</div>
            <div class="flex-1 min-w-0">
              <div class="font-bold text-xs text-on-surface">Forum South Mall MLCP</div>
              <div class="text-[11px] text-secondary">Kanakapura Road, Konanakunte • 0.4 km</div>
            </div>
            <span class="badge-chip ok">42 Free</span>
          </div>

          <div class="pt-2 flex items-start gap-2.5 cursor-pointer">
            <div class="icon-circle slate">{icon("store", size=16)}</div>
            <div class="flex-1 min-w-0">
              <div class="font-bold text-xs text-on-surface">Forum Rex Walk Parking</div>
              <div class="text-[11px] text-secondary">Brigade Road, Ashok Nagar • 6.2 km</div>
            </div>
            <span class="badge-chip warn">8 Free</span>
          </div>
        </div>

        <div class="text-[10px] text-secondary font-bold uppercase tracking-wider pt-2">RECENT SEARCHES</div>
        <div class="flex flex-wrap gap-1.5">
          <div class="badge-chip slate">{icon("history", size=12)} MG Road Metro</div>
          <div class="badge-chip slate">{icon("history", size=12)} Kempegowda T2</div>
          <div class="badge-chip slate">{icon("history", size=12)} Indiranagar 100ft</div>
        </div>
      </div>
      {tabbar("Home")}
    """))

    # DRV-12: Contextual Filters Drawer
    p4.append(phone("DRV-12", "Contextual Filters", f"""
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

        <div>
          <label class="input-label">SORT RESULTS BY</label>
          <div class="space-y-1.5 text-xs">
            <div class="card p-2.5 flex items-center justify-between border-[#00685F] border">
              <span class="font-bold text-on-surface">Distance (Nearest First)</span>
              {icon("radio_button_checked", size=16, extra_style="color:#00685F;")}
            </div>
            <div class="card p-2.5 flex items-center justify-between">
              <span class="text-secondary">Lowest Tariff First</span>
              {icon("radio_button_unchecked", size=16, extra_style="color:#565E74;")}
            </div>
          </div>
        </div>
      </div>
      <div class="sticky-footer">
        {btn("Apply Filters (18 Facilities)", "primary", icon_name="check")}
      </div>
      {tabbar("Home")}
    """))

    # DRV-01L: Facility List View
    p4.append(phone("DRV-01L", "Facility List View", f"""
      {status_bar()}
      {nav_header("Nearby Parking (24)", "Sorted by Distance", right_icon="map")}
      <div class="screen-body space-y-2.5">
        <!-- Item 1 -->
        <div class="card p-3 border-2 border-[#00685F]">
          <div class="flex items-center justify-between mb-1">
            <div class="flex items-center gap-1.5">
              <span class="font-bold text-xs text-on-surface">Forum South Mall MLCP</span>
              <span class="badge-chip ok">42 Free</span>
            </div>
            <span class="font-bold text-xs text-[#00685F]">₹60/hr</span>
          </div>
          <p class="text-[11px] text-secondary">0.4 km away • 2.1m clearance • 60kW DC EV Ready</p>
          <div class="flex items-center justify-between mt-2 pt-1.5 border-t border-slate-100">
            <span class="text-[10px] text-[#006947] font-semibold">{icon("verified", size=12)} Advance Bay Lock</span>
            <button class="pro-btn primary sm" type="button">Select</button>
          </div>
        </div>

        <!-- Item 2 -->
        <div class="card p-3">
          <div class="flex items-center justify-between mb-1">
            <div class="flex items-center gap-1.5">
              <span class="font-bold text-xs text-on-surface">Metro Central MLCP</span>
              <span class="badge-chip ok">85 Free</span>
            </div>
            <span class="font-bold text-xs text-[#00685F]">₹40/hr</span>
          </div>
          <p class="text-[11px] text-secondary">0.8 km away • Direct Skywalk to Metro Station</p>
          <div class="flex items-center justify-between mt-2 pt-1.5 border-t border-slate-100">
            <span class="text-[10px] text-secondary font-semibold">Floating Facility Entry</span>
            <button class="pro-btn secondary sm" type="button">Details</button>
          </div>
        </div>
      </div>
      {tabbar("Home")}
    """))

    sections.append(phase_divider(4, "Map Discovery & Search HUD", "Interactive vector transit map, search HUD with vehicle chip switcher, contextual filtering, and high-density list results.", "DRV-01M → DRV-01L (4 Screens)"))
    sections.append(f'<div class="screens-horizontal-row">{"".join(p4)}</div>')

    # ═══════════════════════════════════════════════════════════════════════════
    # STAGE 05: FACILITY TELEMETRY & 2D BLUEPRINT DECK BAY SELECTOR (4 SCREENS)
    # ═══════════════════════════════════════════════════════════════════════════
    p5 = []

    # DRV-02: Facility Telemetry Hero
    p5.append(phone("DRV-02", "Facility Telemetry", f"""
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
    """))

    # DRV-02P: Product Selector (Advance vs Floating)
    p5.append(phone("DRV-02P", "Product Selector", f"""
      {status_bar()}
      {nav_header("Reservation Type", "Select Admission Guarantee")}
      <div class="screen-body space-y-3">
        <!-- Advance Guaranteed -->
        <div class="card p-4 border-2 border-[#00685F] bg-[#00685F]/[0.02] space-y-2">
          <div class="flex items-center justify-between">
            <span class="badge-chip teal">100% Guaranteed</span>
            <span class="font-bold text-sm text-[#00685F]">₹60.00/hr</span>
          </div>
          <h3 class="font-bold text-sm text-on-surface">Advance Dedicated Bay (B2)</h3>
          <p class="text-xs text-secondary leading-relaxed">
            Specific bay locked for your vehicle plate. 15-minute arrival hold guarantee. Zero wait time.
          </p>
          <div class="text-[11px] text-[#006947] font-semibold flex items-center gap-1 pt-1">
            {icon("verified", size=14)} Backed by SLA goodwill compensation
          </div>
        </div>

        <!-- Floating Entry -->
        <div class="card p-4 space-y-2">
          <div class="flex items-center justify-between">
            <span class="badge-chip slate">Floating Flex</span>
            <span class="font-bold text-sm text-on-surface">₹40.00/hr</span>
          </div>
          <h3 class="font-bold text-sm text-on-surface">Facility Admission Pass</h3>
          <p class="text-xs text-secondary leading-relaxed">
            General entry into the garage. Drive into any open stall on arrival without specific bay reservation.
          </p>
        </div>
      </div>
      <div class="sticky-footer">
        {btn("Continue with Advance Bay B2", "primary")}
      </div>
    """))

    # DRV-02A: Zone Capacity Picker
    p5.append(phone("DRV-02A", "Zone Capacity Picker", f"""
      {status_bar()}
      {nav_header("Deck B2 Zones", "Ultrasonic Sensor Telemetry")}
      <div class="screen-body space-y-3">
        <p class="text-xs text-secondary">Ultrasonic sensors update occupancy every 3 seconds.</p>
        
        <div class="card p-3.5 border-2 border-[#00685F] space-y-2">
          <div class="flex items-center justify-between">
            <span class="font-bold text-xs text-on-surface">Sector 2B (Near Lift Lobby C)</span>
            <span class="badge-chip ok">14 Bays Free</span>
          </div>
          <div class="w-full bg-slate-200 h-2 rounded-full overflow-hidden">
            <div class="bg-[#00685F] h-full w-2/5"></div>
          </div>
          <div class="text-[11px] text-secondary">Recommended: Fastest pedestrian exit to mall atrium.</div>
        </div>

        <div class="card p-3.5 space-y-2">
          <div class="flex items-center justify-between">
            <span class="font-bold text-xs text-on-surface">Sector 2E (EV Charging Hub)</span>
            <span class="badge-chip teal">6 Fast Bays Free</span>
          </div>
          <div class="w-full bg-slate-200 h-2 rounded-full overflow-hidden">
            <div class="bg-[#00685F] h-full w-3/4"></div>
          </div>
          <div class="text-[11px] text-secondary">Equipped with 60kW Dual Gun DC Fast Chargers.</div>
        </div>
      </div>
      <div class="sticky-footer">
        {btn("Open Interactive Blueprint", "primary", icon_name="view_quilt")}
      </div>
    """))

    # DRV-02B: Interactive Blueprint Deck Bay Selector (B2)
    p5.append(phone("DRV-02B", "Deck Bay Blueprint (B2)", f"""
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

        <!-- Blueprint Grid -->
        <div class="blueprint-grid-canvas">
          <div class="bay-cell taken">B2-11</div>
          <div class="bay-cell taken">B2-12</div>
          <div class="bay-cell free">B2-13</div>
          <div class="bay-cell selected">B2-14</div>
          <div class="bay-cell free">B2-15</div>
          <div class="bay-cell taken">B2-16</div>
        </div>

        <!-- Selected Bay Card -->
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
    """))

    sections.append(phase_divider(5, "Facility Telemetry & 2D Blueprint Deck Bay Selector", "Real-time ultrasonic capacity meter, advance vs floating model choice, and interactive 2D blueprint deck bay selector.", "DRV-02 → DRV-02B (4 Screens)"))
    sections.append(f'<div class="screens-horizontal-row">{"".join(p5)}</div>')

    # ═══════════════════════════════════════════════════════════════════════════
    # STAGE 06: STATUTORY QUOTE & SECURE 1-TAP UPI CHECKOUT (8 SCREENS)
    # Master Spec v3.0 Invariant: ₹60 + ₹5 + ₹5.85 CGST + ₹5.85 SGST = ₹76.70
    # ═══════════════════════════════════════════════════════════════════════════
    p6 = []

    # DRV-03: Statutory Payable Quote
    p6.append(phone("DRV-03", "Statutory Quote (₹76.70)", f"""
      {status_bar()}
      {nav_header("Booking Summary", "Statutory Tariff Quote")}
      <div class="screen-body space-y-3 text-xs">
        <div class="card p-3.5">
          <div class="font-bold text-sm text-on-surface">Forum South Mall MLCP • Bay B2-14</div>
          <p class="text-secondary mt-0.5">Tata Nexon EV Max • KA 01 MJ 8821</p>
          <div class="badge-chip teal mt-2">1 Hour Lease • 15-min arrival hold</div>
        </div>

        <!-- Master Spec Invariant Breakdown -->
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
    """))

    # DRV-03F: Floating Session Quote
    p6.append(phone("DRV-03F", "Floating Session Quote", f"""
      {status_bar()}
      {nav_header("Floating Admission", "Pay-As-You-Dwell")}
      <div class="screen-body space-y-3 text-xs">
        <div class="card p-3.5">
          <div class="font-bold text-sm text-on-surface">Metro Central Hub MLCP</div>
          <p class="text-secondary mt-0.5">Floating Facility Entry • Any Open Bay</p>
        </div>
        <div class="card p-3.5 space-y-2">
          <div class="font-bold text-on-surface">Pre-Authorization Hold</div>
          <p class="text-secondary">₹100 pre-auth hold placed on UPI. Only actual dwell time billed at ₹40/hr + GST upon exit.</p>
        </div>
      </div>
      <div class="sticky-footer">
        {btn("Authorize ₹100 Hold", "primary")}
      </div>
    """))

    # DRV-04: 1-Tap UPI Payment Sheet
    p6.append(phone("DRV-04", "1-Tap UPI Checkout", f"""
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

          <div class="p-3 flex items-center justify-between cursor-pointer">
            <span class="font-bold text-sm text-on-surface">Paytm UPI / Wallet</span>
            {icon("radio_button_unchecked", size=18, extra_style="color:#565E74;")}
          </div>
        </div>
      </div>
      <div class="sticky-footer">
        {btn("Pay ₹76.70 with GPay", "primary", icon_name="lock")}
      </div>
    """))

    # DRV-04P: Payment Pending Webhook
    p6.append(phone("DRV-04P", "Payment Processing", f"""
      {status_bar()}
      <div class="screen-body flex flex-col items-center justify-center text-center p-6 space-y-3">
        <div class="splash-spinner mb-2"></div>
        <h3 class="text-base font-bold text-on-surface">Awaiting UPI Confirmation</h3>
        <p class="text-xs text-secondary max-w-[260px]">Please approve the ₹76.70 request in your Google Pay app within 02:45.</p>
        <span class="badge-chip teal">NPCI Tokenized Gateway</span>
      </div>
    """))

    # DRV-04X: Payment Failed Retry
    p6.append(phone("DRV-04X", "Payment Failed Retry", f"""
      {status_bar()}
      {nav_header("Payment Declined", "Bank Timeout")}
      <div class="screen-body space-y-3 text-center p-4">
        <div class="w-12 h-12 rounded-full bg-red-100 text-rose-700 flex items-center justify-center mx-auto">
          {icon("cancel", size=28)}
        </div>
        <h3 class="font-bold text-base text-rose-950">Payment Unsuccessful</h3>
        <p class="text-xs text-secondary">Bank server did not respond in time. Bay B2-14 lease hold is reserved for another 04:18 minutes.</p>
      </div>
      <div class="sticky-footer">
        {btn("Retry with PhonePe or Other UPI", "primary", icon_name="refresh")}
      </div>
    """))

    # DRV-04E: Lease Expired State
    p6.append(phone("DRV-04E", "Lease Expired State", f"""
      {status_bar()}
      {nav_header("Reservation Expired", "15-Minute Timeout")}
      <div class="screen-body space-y-3 text-center p-4">
        <div class="w-12 h-12 rounded-full bg-amber-100 text-amber-700 flex items-center justify-center mx-auto">
          {icon("timer_off", size=28)}
        </div>
        <h3 class="font-bold text-base text-amber-950">Bay Hold Released</h3>
        <p class="text-xs text-secondary">Bay B2-14 hold timed out after 15 minutes. Select a new bay on Deck B2.</p>
      </div>
      <div class="sticky-footer">
        {btn("Select New Bay on Map", "primary", icon_name="refresh")}
      </div>
    """))

    # DRV-04F: UPI OTM Pre-Auth Mandate
    p6.append(phone("DRV-04F", "UPI OTM Pre-Auth", f"""
      {status_bar()}
      {nav_header("One-Time Mandate", "NPCI UPI AutoPay")}
      <div class="screen-body space-y-3 text-xs">
        <div class="card p-3.5 space-y-2">
          <div class="font-bold text-on-surface">Auto-Overstay Settlement Consent</div>
          <p class="text-secondary">Authorizes automated settlement if you choose to park beyond the initial 1-hour booking.</p>
        </div>
      </div>
      <div class="sticky-footer">
        {btn("Authorize Mandate", "primary")}
      </div>
    """))

    # DRV-04T: Mandate Top-Up Warning
    p6.append(phone("DRV-04T", "Mandate Top-Up Alert", f"""
      {status_bar()}
      {nav_header("Mandate Threshold", "Balance Low")}
      <div class="screen-body space-y-3 text-xs">
        <div class="card p-3.5">
          <div class="font-bold text-on-surface">UPI Mandate Cap Reached</div>
          <p class="text-secondary">Approve top-up to avoid gate exit delays.</p>
        </div>
      </div>
      <div class="sticky-footer">
        {btn("Top Up Mandate", "primary")}
      </div>
    """))

    sections.append(phase_divider(6, "Statutory Quote & Secure 1-Tap UPI Checkout", "Strict Master Spec v3.0 financial invariants (₹76.70 quote), lease hold countdown, GPay/PhonePe selection, and OTM mandates.", "DRV-03 → DRV-04T (8 Screens)"))
    sections.append(f'<div class="screens-horizontal-row">{"".join(p6)}</div>')

    # ═══════════════════════════════════════════════════════════════════════════
    # STAGE 07: INGRESS WAYFINDING & LIVE GATE CLEARANCE (4 SCREENS)
    # ═══════════════════════════════════════════════════════════════════════════
    p7 = []

    # DRV-05: Dynamic Digital Pass
    p7.append(phone("DRV-05", "Dynamic Digital Pass", f"""
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
    """))

    # DRV-05N: Ramp HUD Wayfinding
    p7.append(phone("DRV-05N", "Ingress Wayfinding HUD", f"""
      {status_bar(True)}
      <div class="screen-body p-4 space-y-3 bg-[#0B1C30] text-white">
        <div class="card p-4 bg-slate-900 border border-slate-700 text-center space-y-2">
          {icon("arrow_downward", size=36, extra_style="color:#89F5E7;")}
          <h3 class="text-lg font-bold text-white">Descend Ramp to Deck B2</h3>
          <p class="text-xs text-slate-300">Maintain &lt; 15 km/h • Take second left towards Sector 2B</p>
        </div>
        <div class="card p-3 bg-slate-800 border border-slate-700 flex justify-between text-xs">
          <span>Target Bay:</span>
          <span class="font-bold text-teal-container">STALL B2-14</span>
        </div>
      </div>
      <div class="sticky-footer" style="background:#0B1C30;border-color:rgba(255,255,255,0.1);">
        {btn("Arrived at Stall B2-14", "primary", icon_name="task_alt")}
      </div>
    """, bg="#0B1C30"))

    # DRV-05B: Barrier Gate Clearance
    p7.append(phone("DRV-05B", "Barrier Gate Handshake", f"""
      {status_bar()}
      {nav_header("Boom Barrier Auto-Lift", "FASTag Handshake < 1.2s")}
      <div class="screen-body space-y-4 text-center p-4">
        <div class="w-16 h-16 rounded-full bg-emerald-100 text-[#006947] flex items-center justify-center mx-auto">
          {icon("check_circle", size=36)}
        </div>
        <h3 class="text-lg font-bold text-emerald-950">Barrier Raising</h3>
        <p class="text-xs text-secondary">FASTag NETC EPC recognized. Drive forward to B2 ramp.</p>
      </div>
    """))

    # DRV-05O: Offline Dynamic Pass
    p7.append(phone("DRV-05O", "Offline Dynamic Pass", f"""
      {status_bar()}
      {nav_header("Cellar Offline Mode", "Cryptographic PassKit")}
      <div class="screen-body space-y-3 text-center">
        <div class="card p-4 space-y-2">
          <span class="badge-chip navy">NO INTERNET REQUIRED</span>
          <p class="text-xs text-secondary">Stored local cryptographic key confirms reservation at offline cellar gate reader.</p>
        </div>
      </div>
    """))

    sections.append(phase_divider(7, "Ingress Wayfinding & Live Gate Clearance", "PassKit digital pass, live turn-by-turn ramp HUD, FASTag ANPR boom barrier clearance, and cellar offline mode.", "DRV-05 → DRV-05O (4 Screens)"))
    sections.append(f'<div class="screens-horizontal-row">{"".join(p7)}</div>')

    # ═══════════════════════════════════════════════════════════════════════════
    # STAGE 08: ACTIVE DWELL SESSION, EXTENSION & EXIT (6 SCREENS)
    # ═══════════════════════════════════════════════════════════════════════════
    p8 = []

    # DRV-06: Active Parking Session
    p8.append(phone("DRV-06", "Active Parking Session", f"""
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
    """))

    # DRV-27: EV Fast Charging
    p8.append(phone("DRV-27", "EV Fast Charging", f"""
      {status_bar()}
      {nav_header("EV Fast Charging", "60kW DC Dual Gun")}
      <div class="screen-body space-y-3 text-center">
        <div class="card p-4 space-y-2">
          <div class="text-2xl font-bold text-[#00685F]">68% Charged</div>
          <p class="text-xs text-secondary">Delivering 54.2 kW • +38 km added</p>
        </div>
      </div>
    """))

    # DRV-07: Extend Parking Sheet
    p8.append(phone("DRV-07", "Extend Parking Sheet", f"""
      {status_bar()}
      {nav_header("Extend Parking", "Bay B2-14 Availability")}
      <div class="screen-body space-y-3 text-xs">
        <div class="card p-3.5 space-y-2">
          <div class="font-bold text-on-surface">Select Extension Duration</div>
          <div class="grid-3 gap-2">
            <button class="pro-btn secondary sm">+30 Min</button>
            <button class="pro-btn primary sm">+1 Hour</button>
            <button class="pro-btn secondary sm">+2 Hours</button>
          </div>
        </div>
      </div>
      <div class="sticky-footer">
        {btn("Confirm & Pay Extension", "primary")}
      </div>
    """))

    # DRV-07X: Extension Conflict
    p8.append(phone("DRV-07X", "Extension Conflict", f"""
      {status_bar()}
      {nav_header("Bay Reserved", "Conflict Resolved")}
      <div class="screen-body space-y-3 text-xs">
        <div class="card p-3.5 bg-amber-50 border border-amber-200">
          <div class="font-bold text-amber-950">Bay B2-14 Reserved by Next Driver</div>
          <p class="text-amber-800 mt-1">You may extend into adjacent Bay B2-15 without leaving the garage.</p>
        </div>
      </div>
    """))

    # DRV-08: Overstay Warning
    p8.append(phone("DRV-08", "Overstay Warning", f"""
      {status_bar()}
      {nav_header("T-15m Warning", "Session Ending Soon")}
      <div class="screen-body space-y-3 text-xs text-center p-4">
        <div class="icon-circle warn mx-auto">{icon("alarm", size=24)}</div>
        <h3 class="font-bold text-sm text-on-surface">15 Minutes Remaining</h3>
        <p class="text-secondary">Return to vehicle or extend your booking to avoid overstay penalty.</p>
      </div>
    """))

    # DRV-09: Statutory Tax Invoice
    p8.append(phone("DRV-09", "Session Tax Invoice", f"""
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
    """))

    sections.append(phase_divider(8, "Active Dwell Session, Extension & Exit", "Live elapsed dwell ring, 60kW DC EV charging telemetry, slot extension conflict resolution, and statutory GST tax invoices.", "DRV-06 → DRV-09 (6 Screens)"))
    sections.append(f'<div class="screens-horizontal-row">{"".join(p8)}</div>')

    # ═══════════════════════════════════════════════════════════════════════════
    # STAGE 09: INCIDENT RECOVERY, SOS & DPDP DATA RIGHTS (6 SCREENS)
    # ═══════════════════════════════════════════════════════════════════════════
    p9 = []

    # DRV-19: SOS Bay Occupied
    p9.append(phone("DRV-19", "SOS Bay Occupied", f"""
      {status_bar()}
      {nav_header("SOS • Bay Occupied", "Guaranteed Bay SLA")}
      <div class="screen-body space-y-3 text-xs">
        <div class="card p-3.5 bg-red-50 border border-red-200">
          <div class="badge-chip danger mb-1">{icon("report_problem", size=13)} Priority Dispute</div>
          <div class="font-bold text-sm text-red-950">Is Someone Parked in Bay B2-14?</div>
          <p class="text-red-800 mt-1">Our Guaranteed Bay SLA will instantly reassign you to an adjacent vacant stall without penalty.</p>
        </div>
      </div>
      <div class="sticky-footer">
        {btn("Submit SOS & Auto-Reassign Bay", "primary", icon_name="bolt")}
      </div>
    """))

    # DRV-19R: SOS Reassigned Bay
    p9.append(phone("DRV-19R", "SOS Reassigned Bay", f"""
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
    """))

    # DRV-22: Cancel & Refund
    p9.append(phone("DRV-22", "Cancel & Refund", f"""
      {status_bar()}
      {nav_header("Cancel Reservation", "Published Refund Policy")}
      <div class="screen-body space-y-3 text-xs">
        <div class="card p-3.5 space-y-2">
          <div class="font-bold text-on-surface pb-1 border-b border-slate-100">Statutory Refund Computation</div>
          <div class="flex justify-between text-secondary"><span>Refund Tier:</span><span class="text-[#006947] font-bold">100% Tariff Refund</span></div>
          <div class="flex justify-between text-secondary"><span>Platform Fee:</span><span class="text-secondary font-mono">₹5.00 non-refundable</span></div>
          <div class="flex justify-between text-sm font-bold text-on-surface pt-2 border-t border-slate-200">
            <span>Refund Amount to UPI:</span>
            <span class="font-mono text-[#00685F]">₹71.70</span>
          </div>
        </div>
      </div>
      <div class="sticky-footer flex gap-2">
        {btn("Keep Reservation", "secondary", extra="flex:1;")}
        {btn("Confirm Cancellation", "primary", extra="flex:1.5;", icon_name="cancel")}
      </div>
    """))

    # DRV-24D: DPDP Rights Desk
    p9.append(phone("DRV-24D", "DPDP Rights Desk", f"""
      {status_bar()}
      {nav_header("DPDP Privacy Desk", "Data Subject Rights")}
      <div class="screen-body space-y-3 text-xs">
        <div class="card p-3.5 space-y-2">
          <div class="font-bold text-on-surface">Your Data Rights under DPDP Act 2023</div>
          <p class="text-secondary">Request full transcript of linked vehicle plate hashes, gate timestamps, or request data purge.</p>
        </div>
      </div>
      <div class="sticky-footer">
        {btn("Download Personal Data Archive", "primary", icon_name="download")}
      </div>
    """))

    # DRV-30: Payment Methods Hub
    p9.append(phone("DRV-30", "Payment Methods Hub", f"""
      {status_bar()}
      {nav_header("Payment Methods", "Saved Cards & UPI")}
      <div class="screen-body space-y-3 text-xs">
        <div class="card p-3.5 flex justify-between items-center">
          <span class="font-bold text-on-surface">Google Pay UPI (Active)</span>
          <span class="badge-chip ok">Default</span>
        </div>
      </div>
      <div class="sticky-footer">
        {btn("Add New UPI VPA", "primary", icon_name="add")}
      </div>
    """))

    # DRV-31: 24/7 Gate Emergency Support
    p9.append(phone("DRV-31", "Gate Emergency Support", f"""
      {status_bar()}
      {nav_header("Emergency Support", "24/7 Gate Intercom")}
      <div class="screen-body space-y-3 text-center p-4">
        <div class="icon-circle teal mx-auto">{icon("support_agent", size=28)}</div>
        <h3 class="font-bold text-sm text-on-surface">Need Immediate Barrier Clearance?</h3>
        <p class="text-xs text-secondary">Connect directly to the on-site MLCP control room.</p>
      </div>
      <div class="sticky-footer">
        {btn("Call Garage Intercom", "primary", icon_name="call")}
      </div>
    """))

    sections.append(phase_divider(9, "Incident Recovery, SOS Support & DPDP Data Rights", "SOS bay occupied resolution, SLA goodwill credit, 1-tap refund computation, monthly pass, and DPDP data rights.", "DRV-19 → DRV-31 (6 Screens)"))
    sections.append(f'<div class="screens-horizontal-row">{"".join(p9)}</div>')

    # Complete Document Assembly
    body_content = "\n".join(sections)

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8"/>
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>ParkSpot Driver App — Complete Flagship UI Flow</title>
  <link rel="preconnect" href="https://fonts.googleapis.com"/>
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin/>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=JetBrains+Mono:wght@500;700&family=Share+Tech+Mono&display=swap" rel="stylesheet"/>
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200" />
  <link rel="stylesheet" href="styles.css"/>
  <style>
    /* Premium Stitch & Mobile Architecture Additions */
    :root {{
      --teal: #00685F;
      --teal-bright: #0D9488;
      --teal-container: #89F5E7;
      --navy: #0B1C30;
      --canvas: #F8F9FF;
      --surface: #FFFFFF;
      --secondary: #565E74;
      --border: #E2E8F0;
    }}
    
    body {{
      background: #070B14;
      color: #0B1C30;
      margin: 0;
      padding: 0;
      font-family: 'Plus Jakarta Sans', system-ui, sans-serif;
    }}
    
    .driver-flow-canvas {{
      max-width: 100%;
      padding: 40px 48px 120px;
      overflow-x: hidden;
    }}
    
    .canvas-hero {{
      margin-bottom: 32px;
      padding-bottom: 24px;
      border-bottom: 1px solid rgba(255,255,255,0.08);
    }}
    .canvas-title {{
      font-family: 'Plus Jakarta Sans', sans-serif;
      font-size: 32px;
      font-weight: 800;
      color: #FFFFFF;
      margin: 0 0 8px;
    }}
    .canvas-sub {{
      color: #94A3B8;
      font-size: 14px;
      line-height: 1.5;
      max-width: 820px;
      margin: 0;
    }}

    /* Phase Divider Header */
    .phase-divider {{
      display: flex;
      align-items: center;
      gap: 16px;
      padding: 24px 0 14px;
      border-top: 1px solid rgba(255,255,255,0.08);
      margin-top: 40px;
    }}
    .phase-badge {{
      background: rgba(0,104,95,0.25);
      border: 1px solid #00685F;
      color: #89F5E7;
      font-size: 11px;
      font-weight: 800;
      letter-spacing: 0.08em;
      padding: 4px 10px;
      border-radius: 999px;
      white-space: nowrap;
    }}
    .phase-info h2 {{
      font-family: 'Plus Jakarta Sans', sans-serif;
      font-size: 18px;
      font-weight: 700;
      color: #FFFFFF;
      margin: 0;
    }}
    .phase-info p {{
      color: #94A3B8;
      font-size: 12px;
      margin: 2px 0 0;
    }}
    .phase-range {{
      margin-left: auto;
      font-family: 'JetBrains Mono', monospace;
      font-size: 11px;
      color: #64748B;
      font-weight: 600;
      white-space: nowrap;
    }}

    /* Horizontal Screen Track */
    .screens-horizontal-row {{
      display: flex;
      gap: 28px;
      overflow-x: auto;
      padding: 16px 0 28px;
      align-items: flex-start;
      scrollbar-width: thin;
      scrollbar-color: #334155 #0B1C30;
    }}
    
    .phone-frame-wrapper {{
      flex: 0 0 auto;
      display: flex;
      flex-direction: column;
    }}
    .screen-meta {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 10px;
      padding: 0 4px;
    }}
    .screen-id {{
      color: #89F5E7;
      font-family: 'JetBrains Mono', monospace;
      font-size: 11px;
      font-weight: 700;
    }}
    .screen-name {{
      color: #E2E8F0;
      font-size: 12px;
      font-weight: 600;
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
    .tab-item.active span {{
      color: #00685F;
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
    .pro-btn.primary:hover {{ background: #005049; }}
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
      margin: 8px 12px;
      border: 1px solid #E2E8F0;
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

    /* Auth Gateway Styling */
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
  </style>
</head>
<body>
  <main class="driver-flow-canvas">
    <header class="canvas-hero">
      <div class="badge-chip teal mb-2">Google Stitch "Urban Mobility &amp; Transit" Design System</div>
      <h1 class="canvas-title">ParkSpot Driver App — Complete UI Flow</h1>
      <p class="canvas-sub">
        Industry-standard 53-screen mobile UX architecture. Features native Launch Screen, 3-Step Onboarding Walkthrough, 
        Welcome Auth Gateway, Sign-In, Register with DPDP Consents, 3-Step Forgot Password, Dedicated Terms of Service &amp; Privacy Policy, 
        Flagship 5-Tab Bottom Navigation Suite (Home, Bookings, Garage, Wallet, Profile), 
        Interactive 2D B2 Blueprint Deck Bay Selector, Master Spec v3.0 Statutory Quote (₹76.70 Invariant), 
        and FASTag &amp; Cryptographic QR Gate Clearance.
      </p>
    </header>

    {body_content}
  </main>
</body>
</html>"""

    (OUT_DIR / "flow-driver.html").write_text(html, encoding="utf-8")
    print("Successfully built flagship flow-driver.html with 53 screens and 5-tab bottom navigation!")

if __name__ == "__main__":
    build_driver_page()
