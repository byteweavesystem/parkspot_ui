#!/usr/bin/env python3
"""Generate complete ParkSpot UI mockup HTML for every Must/Should screen in design.md."""
from pathlib import Path

OUT = Path(__file__).parent

ASSETS = {
  "facility": "assets/parkspot-facility-hero.jpg",
  "garage": "assets/parkspot-garage-b2.jpg",
  "garage_stock": "assets/garage-hero.jpg",
  "levels": "assets/parking-levels.jpg",
  "map": "assets/parkspot-map-base.jpg",
  "map_aerial": "assets/map-aerial.jpg",
  "car": "assets/car-detail.jpg",
  "plate": "assets/parkspot-hsrp-plate.jpg",
  "qr": "assets/qr-pass.png",
  "city": "assets/city-street.jpg",
  "night": "assets/night-city.jpg",
  "desk": "assets/desk.jpg",
  "sign": "assets/parking-sign.jpg",
}

SHELL_CSS = """
.flow-page { padding: 48px 32px 80px; }
.flow-page h1 { color:#fff; font-size:32px; font-weight:800; margin-bottom:8px; }
.flow-page .sub { color:#94A3B8; margin-bottom:28px; max-width:640px; }
.row { display:flex; gap:32px; overflow-x:auto; padding-bottom:24px; align-items:flex-start; }
.shot { flex:0 0 auto; }
.shot .sid { color:#5EEAD4; font-size:12px; font-weight:700; letter-spacing:.04em; margin-bottom:8px; }
.shot .stitle { color:#E2E8F0; font-size:14px; font-weight:600; margin-bottom:12px; }
.phone-inner { position:absolute; inset:0; display:flex; flex-direction:column; }
.pad { padding:16px; }
.pad-x { padding-left:16px; padding-right:16px; }
.grow { flex:1; overflow:auto; }
.sticky-bottom { margin-top:auto; padding:16px; padding-bottom:28px; background:#fff; border-top:1px solid var(--border); }
.nav-top { display:flex; align-items:center; gap:12px; padding:8px 16px 12px; background:#fff; }
.back { width:36px; height:36px; border-radius:12px; background:var(--muted); display:grid; place-items:center; font-weight:800; flex-shrink:0; }
.row-between { display:flex; justify-content:space-between; align-items:center; gap:8px; }
.list-item { padding:14px 0; border-bottom:1px solid var(--border); }
.input { height:52px; border-radius:14px; border:1.5px solid var(--border); background:#fff; padding:0 14px; display:flex; align-items:center; font-weight:600; font-size:15px; width:100%; }
.otp-row { display:flex; gap:8px; justify-content:center; margin:20px 0; }
.otp-box { width:48px; height:56px; border-radius:12px; border:1.5px solid var(--border); background:#fff; display:grid; place-items:center; font-size:22px; font-weight:800; }
.grid-2 { display:grid; grid-template-columns:1fr 1fr; gap:10px; }
.grid-3 { display:grid; grid-template-columns:1fr 1fr 1fr; gap:10px; }
.class-tile { height:72px; border-radius:14px; border:1.5px solid var(--border); background:#fff; display:flex; flex-direction:column; align-items:center; justify-content:center; gap:4px; font-size:12px; font-weight:700; color:var(--text-2); }
.class-tile.on { border-color:var(--teal); background:var(--teal-container); color:#0F766E; }
.desk-shell { display:grid; grid-template-columns:220px 1fr; height:100%; }
.desk-nav { background:var(--navy); color:#fff; padding:20px 14px; }
.desk-nav .logo { font-weight:800; font-size:17px; margin-bottom:16px; }
.desk-nav a { display:block; padding:9px 12px; border-radius:10px; color:#94A3B8; font-size:12px; font-weight:600; text-decoration:none; margin-bottom:2px; }
.desk-nav a.on { background:rgba(13,148,136,.22); color:#5EEAD4; }
.desk-main { display:flex; flex-direction:column; min-width:0; background:var(--canvas); }
.desk-top { height:56px; background:#fff; border-bottom:1px solid var(--border); display:flex; align-items:center; justify-content:space-between; padding:0 20px; }
.desk-body { padding:16px 20px; overflow:auto; flex:1; }
.table { width:100%; border-collapse:collapse; font-size:12px; }
.table th { text-align:left; padding:10px 8px; color:var(--text-2); border-bottom:1px solid var(--border); font-weight:600; }
.table td { padding:12px 8px; border-bottom:1px solid var(--border); font-weight:600; }
.progress { height:8px; border-radius:999px; background:var(--border); overflow:hidden; }
.progress > i { display:block; height:100%; background:var(--teal); }
.stepper { display:flex; gap:6px; margin-bottom:16px; }
.stepper span { flex:1; height:4px; border-radius:4px; background:var(--border); }
.stepper span.on { background:var(--teal); }
.ring-big { width:140px; height:140px; border-radius:50%; border:10px solid var(--teal-container); border-top-color:var(--teal); display:grid; place-items:center; margin:12px auto; }
.settings-row { display:flex; align-items:center; gap:12px; padding:14px 0; border-bottom:1px solid var(--border); }
.settings-row .ico-tile { width:40px; height:40px; border-radius:12px; background:var(--muted); display:grid; place-items:center; font-size:16px; flex-shrink:0; }
.settings-row .grow-col { flex:1; min-width:0; }
.settings-row .chev { color:var(--text-2); font-weight:800; }
.toggle { width:48px; height:28px; border-radius:999px; background:var(--border); position:relative; flex-shrink:0; }
.toggle.on { background:var(--teal); }
.toggle::after { content:""; position:absolute; top:3px; left:3px; width:22px; height:22px; border-radius:50%; background:#fff; box-shadow:0 2px 6px rgba(15,23,42,.2); }
.toggle.on::after { left:23px; }
.legal-body { font-size:13px; line-height:1.55; color:var(--text-2); }
.legal-body h4 { color:var(--navy); font-size:14px; font-weight:750; margin:14px 0 6px; }
.check-row { display:flex; gap:12px; align-items:flex-start; padding:12px; border:1.5px solid var(--border); border-radius:14px; background:#fff; margin-bottom:10px; }
.check-row.on { border-color:var(--teal); background:var(--teal-container); }
.check { width:22px; height:22px; border-radius:7px; border:2px solid var(--border); background:#fff; flex-shrink:0; display:grid; place-items:center; font-size:12px; font-weight:800; color:transparent; }
.check-row.on .check { background:var(--teal); border-color:var(--teal); color:#fff; }
.empty-hero { text-align:center; padding:40px 20px; }
.empty-hero .glyph { width:72px; height:72px; border-radius:24px; background:var(--teal-container); color:var(--teal-deep); display:grid; place-items:center; font-size:28px; font-weight:800; margin:0 auto 16px; }
"""

def wrap_page(title, subtitle, body):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1"/>
<title>{title} — ParkSpot Complete Mockups</title>
<link rel="stylesheet" href="styles.css"/>
<style>{SHELL_CSS}</style>
</head>
<body>
<div class="flow-page">
  <div class="label" style="color:#64748B;margin-bottom:8px;">PARKSPOT · COMPLETE UI/UX FLOW · DESIGN.MD V4</div>
  <h1>{title}</h1>
  <p class="sub">{subtitle}</p>
  <p style="margin-bottom:24px;"><a href="index.html" style="color:#5EEAD4;font-weight:600;">← All flows</a></p>
  {body}
</div>
</body>
</html>"""

def phone(sid, title, inner, bg="var(--canvas)"):
    return f"""
<div class="shot">
  <div class="sid">{sid}</div>
  <div class="stitle">{title}</div>
  <div class="phone" style="background:{bg}">
    <div class="phone-inner">{inner}</div>
    <div class="home-indicator"></div>
  </div>
</div>"""

def desk(sid, title, inner):
    return f"""
<div class="shot">
  <div class="sid">{sid}</div>
  <div class="stitle">{title}</div>
  <div class="desktop">{inner}</div>
</div>"""

def status(dark=False):
    c = "#fff" if dark else "var(--navy)"
    return f'<div class="status-bar" style="color:{c};flex-shrink:0;"><span>9:41</span><span>5G ▮▮▮</span></div>'

def tabbar(active="Explore"):
    tabs = ["Explore", "Bookings", "Passes", "Profile"]
    items = "".join(
        f'<div class="tab {"active" if t==active else ""}"><div class="ico">{"◉" if t==active else "○"}</div>{t}</div>'
        for t in tabs
    )
    return f'<nav class="tabbar">{items}</nav>'

def btn(label, kind="primary", extra=""):
    return f'<button class="btn {kind} xl" style="width:100%;{extra}">{label}</button>'

def nav(title, sub=""):
    return f"""<div class="nav-top">
  <div class="back">←</div>
  <div><div class="h3" style="font-size:16px;">{title}</div>
  {f'<div class="meta">{sub}</div>' if sub else ''}</div>
</div>"""

# ─── DRIVER SCREENS ───────────────────────────────────────────

def driver_screens():
    screens = []

    screens.append(phone("AUTH-01", "Splash", f"""
      <div class="hero-media" style="flex:1;">
        <img class="img-cover" src="{ASSETS['facility']}" alt=""/>
        <div style="position:absolute;inset:0;background:linear-gradient(180deg,rgba(11,18,32,.15) 0%,rgba(11,18,32,.55) 45%,rgba(11,18,32,.92) 100%);"></div>
        {status(True)}
        <div style="position:absolute;left:24px;right:24px;top:72px;z-index:2;">
          <div style="display:inline-flex;align-items:center;gap:10px;padding:10px 14px;border-radius:16px;background:rgba(255,255,255,.12);backdrop-filter:blur(12px);border:1px solid rgba(255,255,255,.18);">
            <div style="width:36px;height:36px;border-radius:10px;background:linear-gradient(145deg,#2DD4BF,#0D9488);display:grid;place-items:center;font-weight:900;color:#fff;font-size:18px;">P</div>
            <div style="font-size:22px;font-weight:800;letter-spacing:-.04em;color:#fff;">Park<span style="color:#5EEAD4;">Spot</span></div>
          </div>
        </div>
        <div style="position:absolute;left:24px;right:24px;bottom:28px;color:#fff;z-index:2;">
          <div class="h1" style="color:#fff;font-size:34px;margin-top:10px;">Bay certainty.<br/>Honest price.</div>
          <div class="body" style="color:#CBD5E1;margin-top:10px;max-width:300px;">Know the bay is free. Know the total before you pay. Gate in seconds.</div>
        </div>
      </div>
      <div style="padding:16px 16px 34px;background:#0B1220;display:grid;gap:10px;">
        {btn("Get started")}
        <div style="text-align:center;"><span class="meta" style="color:#64748B;">Already have an account? </span><span style="color:#5EEAD4;font-weight:700;font-size:13px;">Sign in</span></div>
      </div>
    """, bg="var(--navy)"))

    screens.append(phone("AUTH-02", "Phone sign-in", f"""
      {status()}
      {nav("Sign in with mobile")}
      <div class="pad grow">
        <div class="h2" style="margin-bottom:8px;">Your number is your ID</div>
        <div class="body" style="margin-bottom:18px;">OTP via SMS. WhatsApp fallback if SMS is delayed.</div>
        <div class="input" style="font-size:18px;letter-spacing:.02em;"><span style="color:var(--text-2);margin-right:8px;font-size:15px;">+91</span>98765 43210</div>
        <div class="meta" style="margin-top:14px;line-height:1.5;">By continuing you agree to our <span style="color:var(--teal);font-weight:700;">Terms</span>, <span style="color:var(--teal);font-weight:700;">Privacy Policy</span>, and <span style="color:var(--teal);font-weight:700;">DPDP notice</span>.</div>
      </div>
      <div class="sticky-bottom">{btn("Send OTP")}</div>
    """))

    screens.append(phone("AUTH-03", "OTP verify", f"""
      {status()}
      {nav("Enter OTP", "Sent to +91 98765 43210")}
      <div class="pad grow" style="text-align:center;">
        <div class="otp-row">
          <div class="otp-box">4</div><div class="otp-box">8</div><div class="otp-box">2</div>
          <div class="otp-box">1</div><div class="otp-box">9</div><div class="otp-box" style="border-color:var(--teal);">|</div>
        </div>
        <div class="meta">Resend in 0:24 · <span style="color:var(--teal);font-weight:700;">WhatsApp fallback</span></div>
      </div>
      <div class="sticky-bottom">{btn("Verify")}</div>
    """))

    screens.append(phone("AUTH-04", "Profile setup", f"""
      {status()}
      {nav("Your profile")}
      <div class="pad grow">
        <div class="label" style="margin-bottom:6px;">FULL NAME</div>
        <div class="input" style="margin-bottom:14px;">Mahesh Giri</div>
        <div class="label" style="margin-bottom:6px;">EMAIL (OPTIONAL)</div>
        <div class="input" style="margin-bottom:14px;">mahesh@example.com</div>
        <div class="label" style="margin-bottom:6px;">LANGUAGE</div>
        <div class="grid-2">
          <div class="class-tile on">English</div>
          <div class="class-tile">हिन्दी</div>
        </div>
      </div>
      <div class="sticky-bottom">{btn("Save & continue")}</div>
    """))

    screens.append(phone("AUTH-05", "Permissions", f"""
      {status()}
      {nav("App permissions")}
      <div class="pad grow">
        <div class="body" style="margin-bottom:16px;">ParkSpot needs these to find nearby facilities and keep your booking on time. You can change anytime in Settings.</div>
        <div class="card lift" style="padding:16px;margin-bottom:12px;">
          <div class="row-between">
            <div><div class="h3" style="font-size:15px;">Location</div><div class="meta" style="margin-top:4px;">While using · map &amp; ETA</div></div>
            <div class="toggle on"></div>
          </div>
        </div>
        <div class="card lift" style="padding:16px;margin-bottom:12px;">
          <div class="row-between">
            <div><div class="h3" style="font-size:15px;">Notifications</div><div class="meta" style="margin-top:4px;">Pass, T-15, overstay, refunds</div></div>
            <div class="toggle on"></div>
          </div>
        </div>
        <div class="card" style="padding:16px;">
          <div class="row-between">
            <div><div class="h3" style="font-size:15px;">WhatsApp alerts</div><div class="meta" style="margin-top:4px;">Opt-in · DLT templates</div></div>
            <div class="toggle"></div>
          </div>
        </div>
      </div>
      <div class="sticky-bottom" style="display:grid;gap:10px;">
        {btn("Allow & continue")}
        <div style="text-align:center;"><span class="meta" style="color:var(--text-2);">Not now · limited map</span></div>
      </div>
    """))

    screens.append(phone("AUTH-06", "Consent & agreements", f"""
      {status()}
      {nav("Agreements", "Required to create account")}
      <div class="pad grow">
        <div class="check-row on">
          <div class="check">✓</div>
          <div><strong style="font-size:13px;">Terms of Service</strong><div class="meta" style="margin-top:4px;">Booking, refunds, SLA, liability limits</div></div>
        </div>
        <div class="check-row on">
          <div class="check">✓</div>
          <div><strong style="font-size:13px;">Privacy Policy</strong><div class="meta" style="margin-top:4px;">What we collect · retention · processors</div></div>
        </div>
        <div class="check-row on">
          <div class="check">✓</div>
          <div><strong style="font-size:13px;">DPDP notice (v2026.10)</strong><div class="meta" style="margin-top:4px;">Purposes, rights, grievance officer</div></div>
        </div>
        <div class="check-row">
          <div class="check"></div>
          <div><strong style="font-size:13px;">Marketing offers (optional)</strong><div class="meta" style="margin-top:4px;">Promos &amp; city launches · withdraw anytime</div></div>
        </div>
        <div class="meta" style="margin-top:8px;">Consent recorded with timestamp, version, and channel.</div>
      </div>
      <div class="sticky-bottom">{btn("I agree · create account")}</div>
    """))

    screens.append(phone("DRV-18", "Vehicle garage", f"""
      {status()}
      {nav("Your garage", "6 vehicle classes supported")}
      <div class="pad grow">
        <div class="card" style="padding:14px;margin-bottom:12px;border-color:var(--teal);">
          <div class="row-between"><div class="h3" style="font-size:15px;">Hyundai Creta</div><span class="pill teal">Default</span></div>
          <img src="{ASSETS['plate']}" alt="" style="margin:10px 0;width:100%;height:48px;object-fit:cover;border-radius:8px;border:1.5px solid var(--navy);"/>
          <div class="meta">Car · H 1.63m · EV off · FASTag not linked</div>
        </div>
        <div class="card" style="padding:14px;margin-bottom:12px;">
          <div class="h3" style="font-size:15px;">Activa 6G</div>
          <div class="meta" style="margin-top:6px;">KA 01 AB 4455 · Two-wheeler</div>
        </div>
        <div class="label" style="margin:16px 0 8px;">ADD VEHICLE · CLASS</div>
        <div class="grid-3">
          <div class="class-tile">Cycle</div><div class="class-tile">2W</div><div class="class-tile on">Car</div>
          <div class="class-tile">Auto</div><div class="class-tile">SUV</div><div class="class-tile">Truck</div>
        </div>
      </div>
      <div class="sticky-bottom">{btn("Add vehicle")}</div>
    """))

    # Existing explore-like compact version
    screens.append(phone("DRV-01", "Explore map", f"""
      {status()}
      <div class="grow" style="position:relative;min-height:320px;">
        <div class="map-photo" style="background-image:url('{ASSETS['map']}');"></div>
        <div class="pad" style="position:absolute;left:0;right:0;top:8px;z-index:2;">
          <div class="card" style="padding:12px 14px;display:flex;gap:8px;align-items:center;">
            <span style="color:var(--teal);font-weight:800;">◎</span>
            <strong style="font-size:14px;">Indiranagar Metro</strong>
          </div>
          <div style="display:flex;gap:6px;margin-top:8px;overflow:hidden;">
            <span class="pill">Cycle</span><span class="pill">2W</span><span class="pill teal">● Car</span><span class="pill">Auto</span>
          </div>
        </div>
        <div class="pin ok" style="position:absolute;top:140px;left:70px;"><span>12</span></div>
        <div class="pin selected" style="position:absolute;top:180px;left:220px;"><span>✓</span></div>
      </div>
      <div style="background:#fff;border-radius:24px 24px 0 0;padding:12px 16px 90px;box-shadow:0 -4px 16px rgba(15,23,42,.08);">
        <div class="row-between"><div class="h3">Nearby parking</div><span class="pill teal">Filters</span></div>
        <div class="card selected" style="padding:10px;margin-top:10px;display:flex;gap:10px;">
          <img class="thumb" src="{ASSETS['facility']}" alt="" style="width:64px;height:64px;"/>
          <div style="flex:1;">
            <div class="row-between"><strong style="font-size:13px;">Indiranagar Metro MLCP</strong><span class="currency" style="font-weight:800;">₹30</span></div>
            <div class="meta" style="margin:4px 0 6px;">0.4 km · Covered · 2.1m</div>
            <span class="pill ok">● 166 free · Ledger · 2m</span>
          </div>
        </div>
      </div>
      {tabbar("Explore")}
    """))

    screens.append(phone("DRV-12", "Filters", f"""
      {status()}
      {nav("Filters")}
      <div class="pad grow">
        <div class="label">CLEARANCE</div>
        <div class="card" style="padding:14px;margin:8px 0 16px;">Only show &gt; 2.0m for Creta H:1.63m <span class="pill ok" style="float:right;">ON</span></div>
        <div class="label">RADIUS</div>
        <div class="meta" style="margin:8px 0;">0.5 km —————●—— 15 km · <strong>3 km</strong></div>
        <div class="label" style="margin-top:16px;">FRESHNESS</div>
        <div class="grid-2" style="margin-top:8px;">
          <div class="class-tile on">Live only</div><div class="class-tile">All</div>
        </div>
        <div class="label" style="margin-top:16px;">STRUCTURE</div>
        <div class="grid-3" style="margin-top:8px;">
          <div class="class-tile on">Covered</div><div class="class-tile">Surface</div><div class="class-tile">MLCP</div>
        </div>
        <div class="label" style="margin-top:16px;">AMENITIES</div>
        <div style="display:flex;gap:6px;flex-wrap:wrap;margin-top:8px;">
          <span class="pill teal">EV</span><span class="pill">CCTV</span><span class="pill">24×7</span><span class="pill">Washroom</span>
        </div>
      </div>
      <div class="sticky-bottom" style="display:grid;grid-template-columns:1fr 1.4fr;gap:10px;">
        {btn("Reset", "secondary")}<div>{btn("Apply")}</div>
      </div>
    """))

    screens.append(phone("DRV-02", "Facility detail", f"""
      {status()}
      <div class="hero-media" style="height:200px;"><img class="img-cover" src="{ASSETS['facility']}" alt=""/></div>
      <div class="pad grow" style="margin-top:-24px;">
        <div class="card" style="padding:16px;">
          <div class="row-between"><div class="h2" style="font-size:18px;">Indiranagar Metro MLCP</div><span class="pill navy">T1</span></div>
          <div class="meta" style="margin:6px 0;">100 Feet Rd · 24×7 · Verified operator</div>
          <span class="pill ok">● 166 free · Ledger · 2m ago</span>
        </div>
        <div class="card" style="padding:14px;margin-top:12px;">
          <div class="h3" style="font-size:14px;margin-bottom:8px;">Compatibility · Creta</div>
          <div class="meta">Clearance 2.1m ✓ · Car accepted · Covered</div>
        </div>
        <div class="card" style="padding:14px;margin-top:12px;">
          <div class="h3" style="font-size:14px;margin-bottom:8px;">Rate card</div>
          <div class="row-between list-item"><span>First 2 hours</span><strong>₹100</strong></div>
          <div class="row-between list-item"><span>Each extra hour</span><strong>₹40</strong></div>
          <div class="row-between" style="padding-top:10px;"><span class="meta">Grace 10 min · Cancel &gt;60m = 100%</span></div>
        </div>
      </div>
      <div class="sticky-bottom" style="display:grid;grid-template-columns:1fr 1fr;gap:10px;">
        {btn("Navigate", "secondary")}{btn("Continue")}
      </div>
    """))

    screens.append(phone("DRV-02P", "Choose product", f"""
      {status()}
      {nav("How do you want to park?", "Indiranagar Metro · Bay eligible")}
      <div class="pad grow">
        <div class="card selected" style="padding:16px;margin-bottom:12px;">
          <div class="row-between"><div class="h3">Advance reservation</div><span class="pill teal">Certainty</span></div>
          <div class="meta" style="margin-top:8px;">Lock a bay now · pay quote up front · Guaranteed Bay at T1+</div>
          <div class="meta" style="margin-top:6px;">Best when arrival time is known</div>
        </div>
        <div class="card" style="padding:16px;">
          <div class="row-between"><div class="h3">Pay as you use</div><span class="pill info">Floating</span></div>
          <div class="meta" style="margin-top:8px;">Arrival window + OTM pre-auth · billed on actual dwell</div>
          <div class="meta" style="margin-top:6px;">Minimum charge applies · top-up at 80%</div>
        </div>
        <div class="card" style="padding:12px;margin-top:12px;background:var(--muted);border:0;">
          <div class="meta">Cancel policy, grace, and GST apply to both products. Quotes expire in 10 minutes.</div>
        </div>
      </div>
      <div class="sticky-bottom" style="display:grid;grid-template-columns:1fr 1fr;gap:10px;">
        {btn("Floating", "secondary")}{btn("Reserve bay")}
      </div>
    """))

    screens.append(phone("DRV-02A", "Aggregated zone", f"""
      {status()}
      {nav("Choose zone", "Aggregated capacity · guaranteed entry")}
      <div class="pad grow">
        <div class="card" style="padding:14px;margin-bottom:10px;border-color:var(--teal);">
          <div class="row-between"><strong>Surface Lot A</strong><span class="pill ok">42 free</span></div>
          <div class="meta" style="margin-top:6px;">Ledger · 1m · from ₹20/hr</div>
        </div>
        <div class="card" style="padding:14px;margin-bottom:10px;">
          <div class="row-between"><strong>Basement B1</strong><span class="pill warn">8 free</span></div>
          <div class="meta" style="margin-top:6px;">Ledger · 1m · covered</div>
        </div>
        <div class="card" style="padding:14px;">
          <div class="row-between"><strong>Overflow</strong><span class="pill stale">Updated 40m · Operator</span></div>
          <div class="meta" style="margin-top:6px;">Request to book only</div>
        </div>
      </div>
      <div class="sticky-bottom">{btn("Continue to quote")}</div>
    """))

    screens.append(phone("DRV-02B", "Bay deck map", f"""
      {status()}
      {nav("Select bay · B2", "NUMBERED_BAYS")}
      <div style="display:flex;gap:6px;padding:0 16px 10px;overflow:auto;">
        <span class="pill stale">B1 Full</span><span class="pill navy">B2 · 14</span><span class="pill">L1</span><span class="pill">Terrace</span>
      </div>
      <div class="pad grow">
        <div class="card" style="height:340px;position:relative;overflow:hidden;">
          <img src="{ASSETS['garage']}" alt="" style="position:absolute;inset:0;width:100%;height:100%;object-fit:cover;opacity:.28;"/>
          <div style="position:absolute;inset:0;background:linear-gradient(180deg,rgba(255,255,255,.7),rgba(248,250,252,.92));"></div>
          <div style="position:relative;z-index:1;height:100%;">
          <div style="position:absolute;left:12px;top:12px;" class="meta">Lift A</div>
          <div style="position:absolute;left:50%;top:45%;transform:translate(-50%,-50%);font-size:10px;font-weight:800;color:#94A3B8;">ONE WAY →</div>
          <div style="position:absolute;left:70px;top:140px;width:48px;height:30px;border:2px solid var(--teal);background:var(--teal-container);border-radius:6px;display:grid;place-items:center;font-size:10px;font-weight:800;color:#0F766E;">B2-19</div>
          <div style="position:absolute;left:130px;top:140px;width:48px;height:30px;border:1.5px solid #86EFAC;border-radius:6px;display:grid;place-items:center;font-size:9px;">B2-06</div>
          <div style="position:absolute;left:70px;top:200px;width:48px;height:30px;background:var(--muted);border-radius:6px;display:grid;place-items:center;font-size:9px;color:#94A3B8;">occ</div>
        </div></div>
      </div>
      <div class="sticky-bottom">
        <div class="row-between" style="margin-bottom:10px;"><div><div class="h3">Bay B2-19</div><div class="meta">Pillar P-09 · Lift A 30s</div></div><span class="pill ok">Clearance OK</span></div>
        {btn("Hold bay for 10:00 & continue")}
      </div>
    """))

    screens.append(phone("DRV-03", "Quote · reservation", f"""
      {status()}
      {nav("Quote summary", "Expires with 10m hold")}
      <div class="pad grow">
        <div class="card" style="padding:14px;">
          <div class="h3" style="font-size:15px;">Indiranagar Metro MLCP</div>
          <div class="meta">Bay B2-19 · Today 18:00–20:00 · 2h</div>
          <div class="meta" style="margin-top:6px;">KA 01 MJ 8821 · Car</div>
        </div>
        <div class="card" style="padding:14px;margin-top:12px;">
          <div class="label">PRICE BREAKDOWN</div>
          <div class="row-between" style="padding:8px 0;"><span>Parking tariff</span><strong>₹100.00</strong></div>
          <div class="row-between" style="padding:8px 0;"><span>Platform fee</span><strong>₹2.00</strong></div>
          <div class="row-between" style="padding:8px 0;"><span>CGST 9%</span><strong>₹9.18</strong></div>
          <div class="row-between" style="padding:8px 0;"><span>SGST 9%</span><strong>₹9.18</strong></div>
          <div class="row-between" style="padding-top:12px;border-top:1px solid var(--border);">
            <span class="h3">Total payable</span><span class="h2 currency">₹120.36</span>
          </div>
        </div>
        <div class="meta" style="margin-top:10px;">Policy v3 · cancellation disclosed above</div>
      </div>
      <div class="sticky-bottom">{btn("Hold bay & pay")}</div>
    """))

    screens.append(phone("DRV-03F", "Quote · floating", f"""
      {status()}
      {nav("Pay as you use", "Floating session")}
      <div class="pad grow">
        <div class="card" style="padding:14px;">
          <div class="label">ARRIVAL WINDOW</div>
          <div class="h3" style="margin:6px 0;">18:00 – 18:30</div>
          <div class="label" style="margin-top:12px;">EXPECTED STAY</div>
          <div class="row-between" style="margin-top:8px;">
            <span class="pill">−</span><strong>2 hours</strong><span class="pill">+</span>
          </div>
        </div>
        <div class="card" style="padding:14px;margin-top:12px;">
          <div class="row-between"><span>Minimum charge</span><strong>₹50</strong></div>
          <div class="row-between" style="padding:8px 0;"><span>Per 15 min</span><strong>₹12</strong></div>
          <div class="row-between" style="padding:8px 0;"><span>Daily cap</span><strong>₹400</strong></div>
          <div class="row-between" style="padding-top:12px;border-top:1px solid var(--border);">
            <span class="h3">Pre-auth hold</span><span class="h2 currency">₹300</span>
          </div>
          <div class="meta" style="margin-top:6px;">Estimated max + 25% · UPI OTM / card</div>
        </div>
      </div>
      <div class="sticky-bottom">{btn("Authorise hold & continue")}</div>
    """))

    screens.append(phone("DRV-04", "UPI checkout", f"""
      {status()}
      {nav("Secure checkout")}
      <div class="pad grow">
        <div class="card" style="padding:20px;text-align:center;">
          <div class="label">BAY HOLD EXPIRES IN</div>
          <div class="ring-big"><div class="h1 currency" style="font-size:26px;">07:24</div></div>
          <div class="h3">Bay B2-19 locked</div>
        </div>
        <div class="card" style="padding:14px;margin-top:12px;">
          <div class="row-between"><span>Total payable</span><span class="h3 currency">₹120.36</span></div>
        </div>
        <div class="label" style="margin:14px 0 8px;">PAY WITH UPI</div>
        <div class="grid-2">
          <div class="class-tile on">GPay</div><div class="class-tile">PhonePe</div>
          <div class="class-tile">Paytm</div><div class="class-tile">UPI ID</div>
        </div>
      </div>
      <div class="sticky-bottom">{btn("Pay ₹120.36 with GPay")}<div class="meta" style="text-align:center;margin-top:8px;">Don’t close the app</div>
        <div class="meta" style="text-align:center;margin-top:6px;">Also: Cards · Netbanking · Wallet</div></div>
    """))

    screens.append(phone("DRV-04P", "Payment pending", f"""
      {status()}
      {nav("Confirming payment")}
      <div class="pad grow" style="display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;">
        <div class="ring-big"><div class="meta" style="font-weight:800;">Waiting</div></div>
        <div class="h3" style="margin-top:16px;">PENDING_CONFIRMATION</div>
        <div class="body" style="margin-top:8px;max-width:280px;">Bank authorised · waiting for PSP webhook. We poll at 30s, 2m, 10m. Keep this screen open.</div>
        <div class="card" style="padding:14px;margin-top:20px;width:100%;text-align:left;">
          <div class="row-between"><span>Hold</span><strong>07:01 left</strong></div>
          <div class="row-between" style="margin-top:8px;"><span>Amount</span><strong class="currency">₹120.36</strong></div>
          <div class="row-between" style="margin-top:8px;"><span>Bay</span><strong>B2-19</strong></div>
        </div>
      </div>
      <div class="sticky-bottom">{btn("Refresh status", "secondary")}</div>
    """))

    screens.append(phone("DRV-04X", "Payment failed", f"""
      {status()}
      {nav("Payment failed")}
      <div class="pad grow">
        <div class="card" style="padding:16px;background:var(--danger-bg);border-color:#FECACA;">
          <div class="h3" style="color:var(--danger);">UPI declined / timed out</div>
          <div class="meta" style="margin-top:6px;">Booking still HELD · same idempotency key · retry safe</div>
        </div>
        <div class="card" style="padding:14px;margin-top:12px;">
          <div class="row-between"><span>Bay hold</span><span class="pill warn">05:42 left</span></div>
          <div class="row-between" style="margin-top:10px;"><span>Payable</span><strong class="currency">₹120.36</strong></div>
        </div>
        <div class="label" style="margin:16px 0 8px;">TRY ANOTHER RAIL</div>
        <div class="grid-2">
          <div class="class-tile on">UPI</div><div class="class-tile">Cards</div>
          <div class="class-tile">Netbanking</div><div class="class-tile">Wallet</div>
        </div>
      </div>
      <div class="sticky-bottom" style="display:grid;grid-template-columns:1fr 1.2fr;gap:10px;">
        {btn("Cancel hold", "secondary")}{btn("Retry payment")}
      </div>
    """))

    screens.append(phone("DRV-04E", "Lease expired", f"""
      {status()}
      {nav("Hold expired")}
      <div class="pad grow" style="text-align:center;display:flex;flex-direction:column;justify-content:center;">
        <div class="h2">Bay released</div>
        <div class="body" style="margin:12px auto;max-width:280px;">10-minute inventory lease ended before payment confirmed. Slot returned to pool. No charge if payment never captured.</div>
        <div class="card" style="padding:14px;text-align:left;margin-top:8px;">
          <div class="meta">If money left your bank, refund auto-starts (FAILED_REFUNDING path).</div>
        </div>
      </div>
      <div class="sticky-bottom" style="display:grid;grid-template-columns:1fr 1fr;gap:10px;">
        {btn("Back to facility", "secondary")}{btn("Find another bay")}
      </div>
    """))

    screens.append(phone("DRV-04F", "OTM pre-auth", f"""
      {status()}
      {nav("One-time mandate")}
      <div class="pad grow">
        <div class="card" style="padding:16px;">
          <div class="h3">Block ₹300.00</div>
          <div class="meta" style="margin-top:6px;">Valid until expected end + 24h · one capture at exit</div>
        </div>
        <div class="card" style="padding:14px;margin-top:12px;">
          <div class="label">MANDATE DETAILS</div>
          <div class="row-between" style="padding:8px 0;"><span>Max amount</span><strong>₹300</strong></div>
          <div class="row-between" style="padding:8px 0;"><span>Frequency</span><strong>One-time</strong></div>
          <div class="meta" style="margin-top:8px;">Top-up prompted at 80% utilisation</div>
        </div>
      </div>
      <div class="sticky-bottom">{btn("Approve OTM on UPI app")}</div>
    """))

    screens.append(phone("DRV-04T", "Floating top-up", f"""
      {status()}
      {nav("Top-up required", "80% of OTM block used")}
      <div class="pad grow">
        <div class="card" style="padding:16px;background:var(--warn-bg);border-color:#FCD34D;">
          <div class="h3" style="color:var(--warn);">Pre-auth nearly exhausted</div>
          <div class="meta" style="margin-top:6px;">Blocked ₹300 · accrued ₹248 · session continues if you decline, but exit needs gate settlement</div>
        </div>
        <div class="card" style="padding:14px;margin-top:12px;">
          <div class="row-between"><span>Suggested top-up</span><strong class="currency">₹200</strong></div>
          <div class="row-between" style="margin-top:8px;"><span>New mandate</span><strong>OTM #2</strong></div>
          <div class="meta" style="margin-top:8px;">NPCI: one capture per mandate · never partial mid-session</div>
        </div>
      </div>
      <div class="sticky-bottom" style="display:grid;grid-template-columns:1fr 1.2fr;gap:10px;">
        {btn("Decline", "secondary")}{btn("Approve top-up")}
      </div>
    """))

    screens.append(phone("DRV-05", "Digital pass", f"""
      {status(True)}
      <div class="pad" style="color:#fff;"><div class="label" style="color:#94A3B8;">BOOKING CONFIRMED</div><div class="h2" style="color:#fff;">Your digital pass</div></div>
      <div class="pad grow" style="display:flex;align-items:center;">
        <div class="card" style="width:100%;overflow:hidden;">
          <div style="background:var(--navy);color:#fff;padding:16px;">
            <div class="row-between"><div><div class="meta" style="color:#94A3B8;">ParkSpot</div><div class="h3" style="color:#fff;">Indiranagar Metro MLCP</div></div><span class="pill teal">Ed25519</span></div>
            <div style="display:flex;gap:28px;margin-top:14px;"><div><div class="meta" style="color:#94A3B8;">BAY</div><div style="font-size:22px;font-weight:800;">B2-19</div></div><div><div class="meta" style="color:#94A3B8;">WINDOW</div><div style="font-weight:700;">18:00–20:00</div></div></div>
          </div>
          <div style="padding:16px;text-align:center;">
            <img src="{ASSETS['qr']}" width="160" height="160" alt="QR" style="border-radius:12px;border:8px solid #fff;outline:1px solid var(--border);box-shadow:var(--shadow-sm);"/>
            <div style="color:var(--teal);font-family:var(--mono);font-size:12px;font-weight:700;margin-top:10px;">14:48:22 IST · SINGLE USE</div>
            <img src="{ASSETS['plate']}" alt="Plate" style="margin-top:12px;width:200px;height:48px;object-fit:cover;border-radius:8px;border:2px solid var(--navy);"/>
          </div>
        </div>
      </div>
      <div class="pad" style="padding-bottom:28px;display:flex;flex-direction:column;gap:8px;">
        {btn("Boost brightness")}
        {btn("Add to Google Wallet", "secondary")}
        {btn("Navigate to entrance", "navy")}
      </div>
    """, bg="var(--navy)"))

    screens.append(phone("DRV-06", "Active session", f"""
      {status()}
      {nav("Active session", "Checked in 18:04")}
      <div class="pad grow">
        <div class="card" style="padding:20px;text-align:center;">
          <div class="ring-big"><div><div class="h1" style="font-size:24px;">01:14</div><div class="meta">of 02:00</div></div></div>
          <div class="h3">Bay B2-19</div>
          <div class="meta">Pillar P-09 · near Lift A</div>
        </div>
        <div class="card" style="padding:14px;margin-top:12px;">
          <div class="row-between"><span>Dues so far</span><strong class="currency">₹100.00</strong></div>
          <div class="meta" style="margin-top:4px;">Prepaid · grace remaining 10m at end</div>
        </div>
        <div class="label" style="margin:14px 0 8px;">EXTEND</div>
        <div class="grid-3">
          <div class="class-tile">+30m</div><div class="class-tile on">+1h</div><div class="class-tile">+2h</div>
        </div>
      </div>
      <div class="sticky-bottom" style="display:grid;grid-template-columns:1fr 1fr;gap:10px;">
        {btn("SOS", "secondary")}{btn("Find car", "navy")}
      </div>
    """))

    screens.append(phone("DRV-07", "Extend parking", f"""
      {status()}
      {nav("Extend session")}
      <div class="pad grow">
        <div class="card" style="padding:14px;">
          <div class="meta">Current end 20:00 → new end <strong>21:00</strong></div>
          <span class="pill ok" style="margin-top:8px;">Capacity available</span>
        </div>
        <div class="card" style="padding:14px;margin-top:12px;">
          <div class="row-between"><span>+1 hour (evening band)</span><strong>₹36.00</strong></div>
          <div class="row-between" style="padding:8px 0;"><span>GST</span><strong>₹6.48</strong></div>
          <div class="row-between" style="border-top:1px solid var(--border);padding-top:12px;">
            <span class="h3">Pay now</span><span class="h2 currency">₹42.48</span>
          </div>
        </div>
      </div>
      <div class="sticky-bottom">{btn("Pay & extend")}</div>
    """))

    screens.append(phone("DRV-07X", "Extension unavailable", f"""
      {status()}
      {nav("Cannot extend")}
      <div class="pad grow">
        <div class="card" style="padding:16px;background:var(--danger-bg);border-color:#FECACA;">
          <div class="h3" style="color:var(--danger);">EXTENSION_UNAVAILABLE</div>
          <div class="meta" style="margin-top:6px;">Bay B2-19 needed from 20:15 for incoming booking</div>
        </div>
        <div class="card" style="padding:14px;margin-top:12px;">
          <div class="label">LATEST FREE UNTIL</div>
          <div class="h2" style="margin-top:6px;">20:10</div>
          <div class="meta" style="margin-top:8px;">Alternatives: B2-06 free · Terrace aggregated</div>
        </div>
      </div>
      <div class="sticky-bottom" style="display:grid;grid-template-columns:1fr 1fr;gap:10px;">
        {btn("Leave by 20:10", "secondary")}{btn("Move bay")}
      </div>
    """))

    screens.append(phone("DRV-08", "Overstay alert", f"""
      {status()}
      {nav("Overstay")}
      <div class="pad grow">
        <div class="card" style="padding:16px;border-color:#F59E0B;background:var(--warn-bg);">
          <div class="h3" style="color:var(--warn);">Grace expired</div>
          <div class="meta" style="margin-top:6px;">Booked end 20:00 · now 20:18 · surcharge active</div>
        </div>
        <div class="card" style="padding:14px;margin-top:12px;">
          <div class="row-between"><span>Overstay 18 min</span><strong>₹48.00</strong></div>
          <div class="row-between" style="padding:8px 0;"><span>GST</span><strong>₹8.64</strong></div>
          <div class="row-between" style="border-top:1px solid var(--border);padding-top:12px;">
            <span class="h3">Settle before gate</span><span class="h2 currency">₹56.64</span>
          </div>
        </div>
      </div>
      <div class="sticky-bottom">{btn("Pay overstay now")}</div>
    """))

    screens.append(phone("DRV-09", "Tax invoice", f"""
      {status()}
      {nav("Session complete")}
      <div class="pad grow">
        <div class="card" style="padding:16px;text-align:center;">
          <span class="pill ok">COMPLETED</span>
          <div class="h2" style="margin-top:10px;">₹120.36</div>
          <div class="meta">Entry 18:04 · Exit 19:58 · QR both</div>
        </div>
        <div class="card" style="padding:14px;margin-top:12px;">
          <div class="label">INVOICES</div>
          <div class="list-item row-between"><span>Operator parking receipt</span><strong>PDF</strong></div>
          <div class="list-item row-between"><span>Platform fee tax invoice</span><strong>PDF</strong></div>
          <div class="meta">CGST/SGST lines · WhatsApp delivery available</div>
        </div>
      </div>
      <div class="sticky-bottom" style="display:grid;grid-template-columns:1fr 1fr;gap:10px;">
        {btn("WhatsApp", "secondary")}{btn("Rate session")}
      </div>
    """))

    screens.append(phone("DRV-20", "Bookings hub", f"""
      {status()}
      {nav("Bookings")}
      <div class="pad grow">
        <div style="display:flex;gap:8px;margin-bottom:12px;">
          <span class="pill teal">Active</span><span class="pill">Upcoming</span><span class="pill">Past</span>
        </div>
        <div class="card" style="padding:14px;border-color:var(--teal);">
          <div class="row-between"><strong>Indiranagar Metro</strong><span class="pill ok">CHECKED IN</span></div>
          <div class="meta" style="margin:6px 0;">B2-19 · ends 20:00 · 01:14 elapsed</div>
          {btn("Open session", "secondary")}
        </div>
        <div class="card" style="padding:14px;margin-top:10px;">
          <div class="row-between"><strong>Cyber City Hub</strong><span class="pill info">CONFIRMED</span></div>
          <div class="meta" style="margin-top:6px;">Tomorrow 09:00–11:00 · Bay A-12</div>
        </div>
      </div>
      {tabbar("Bookings")}
    """))

    screens.append(phone("DRV-22", "Cancel & refund", f"""
      {status()}
      {nav("Cancel booking")}
      <div class="pad grow">
        <div class="card" style="padding:14px;">
          <div class="h3" style="font-size:15px;">Cyber City Hub · A-12</div>
          <div class="meta">Tomorrow 09:00 · paid ₹120.00</div>
        </div>
        <div class="card" style="padding:14px;margin-top:12px;">
          <div class="label">POLICY (&gt; 60 MIN)</div>
          <div class="row-between" style="padding:6px 0;"><span>Tariff + GST</span><strong>₹118.00</strong></div>
          <div class="row-between" style="padding:6px 0;"><span>Platform fee</span><strong>₹2.00</strong></div>
          <div class="row-between" style="border-top:1px solid var(--border);padding-top:10px;">
            <span class="h3">Refund</span><span class="h2 currency">₹120.00</span>
          </div>
          <div class="meta" style="margin-top:8px;">UPI refund typically same day–5 days · not instant</div>
        </div>
        <div class="label" style="margin-top:14px;">REASON</div>
        <div class="input" style="margin-top:8px;color:var(--text-2);">Plans changed</div>
      </div>
      <div class="sticky-bottom">{btn("Confirm cancellation", "navy")}</div>
    """))

    screens.append(phone("DRV-22T", "Refund tracker", f"""
      {status()}
      {nav("Refund status", "#SP-99102 cancelled")}
      <div class="pad grow">
        <div class="card" style="padding:16px;text-align:center;">
          <div class="h2 currency">₹120.00</div>
          <div class="meta">Credit note CN-2026-4418 issued</div>
        </div>
        <div class="card" style="padding:14px;margin-top:12px;">
          <div class="list-item row-between"><span>1. Requested</span><span class="pill ok">Done</span></div>
          <div class="list-item row-between"><span>2. Inventory released</span><span class="pill ok">Done</span></div>
          <div class="list-item row-between"><span>3. PSP refund API</span><span class="pill info">In progress</span></div>
          <div class="list-item row-between" style="border:0;"><span>4. Completed to UPI</span><span class="pill stale">Pending</span></div>
          <div class="meta" style="margin-top:8px;">Typical UPI: same day to 5 days · never promised instant</div>
        </div>
      </div>
      <div class="sticky-bottom">{btn("Back to bookings", "secondary")}</div>
    """))

    screens.append(phone("DRV-19", "SOS bay occupied", f"""
      {status()}
      {nav("SOS · Bay occupied")}
      <div class="pad grow">
        <div class="card" style="padding:14px;background:var(--danger-bg);border-color:#FECACA;">
          <div class="h3" style="color:var(--danger);">Report squatter</div>
          <div class="meta">Photo required · geofence verified</div>
        </div>
        <div style="height:160px;margin-top:12px;border-radius:16px;background:var(--muted);display:grid;place-items:center;font-weight:700;color:var(--text-2);">Tap to capture plate photo</div>
        <div class="card" style="padding:14px;margin-top:12px;">
          <div class="label">SYSTEM WILL TRY</div>
          <div class="meta" style="margin-top:6px;">1) Same zone · 2) Other zone · 3) Standby bay · 4) SLA credit at T1+</div>
        </div>
      </div>
      <div class="sticky-bottom">{btn("Submit SOS")}</div>
    """))

    screens.append(phone("DRV-19R", "SOS rerouted", f"""
      {status()}
      {nav("Bay reassigned")}
      <div class="pad grow">
        <div class="card" style="padding:16px;background:var(--ok-bg);border-color:#86EFAC;">
          <div class="h3" style="color:var(--ok);">New bay assigned</div>
          <div class="meta" style="margin-top:6px;">B2-19 → <strong>B2-06</strong> · same zone · new Ed25519 pass issued</div>
        </div>
        <div class="card" style="padding:14px;margin-top:12px;">
          <div class="row-between"><span>Walk to</span><strong>Pillar P-08 · Lift A</strong></div>
          <div class="row-between" style="margin-top:8px;"><span>Attendant</span><strong>Notified</strong></div>
          <div class="meta" style="margin-top:8px;">Squatter plate logged as incident</div>
        </div>
      </div>
      <div class="sticky-bottom">{btn("Open new pass")}</div>
    """))

    screens.append(phone("DRV-19S", "SOS SLA breached", f"""
      {status()}
      {nav("No bay available")}
      <div class="pad grow">
        <div class="card" style="padding:16px;background:var(--danger-bg);border-color:#FECACA;">
          <div class="h3" style="color:var(--danger);">SLA_BREACHED</div>
          <div class="meta" style="margin-top:6px;">T1 numbered facility · automatic compensation</div>
        </div>
        <div class="card" style="padding:14px;margin-top:12px;">
          <div class="row-between"><span>Full refund</span><strong class="currency">₹120.36</strong></div>
          <div class="row-between" style="margin-top:8px;"><span>Goodwill credit</span><strong class="currency">₹100.00</strong></div>
          <div class="meta" style="margin-top:10px;">At T0: refund only. Operator debited when squatter was walk-in / unblocked bay.</div>
        </div>
      </div>
      <div class="sticky-bottom">{btn("View wallet credit")}</div>
    """))

    screens.append(phone("DRV-25", "Notifications", f"""
      {status()}
      {nav("Alerts")}
      <div class="pad grow">
        <div class="card" style="padding:14px;margin-bottom:10px;border-color:var(--warn);">
          <div class="label" style="color:var(--warn);">T-15 REMINDER</div>
          <div class="h3" style="font-size:14px;margin-top:4px;">Session ends 20:00</div>
          <div class="meta">Extend now or pre-settle overstay</div>
        </div>
        <div class="card" style="padding:14px;margin-bottom:10px;">
          <div class="label">WHATSAPP · DLT</div>
          <div class="meta" style="margin-top:4px;">Pass ready · show QR at Gate 2</div>
        </div>
        <div class="card" style="padding:14px;">
          <div class="label">OVERSTAY ACCRUAL</div>
          <div class="meta" style="margin-top:4px;">+₹12 since grace ended · pay before exit</div>
        </div>
      </div>
      <div class="sticky-bottom">{btn("Open session")}</div>
    """))

    screens.append(phone("DRV-26", "Network error", f"""
      {status()}
      <div class="pad grow" style="display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;">
        <div class="h2">You're offline</div>
        <div class="body" style="margin:12px 0;max-width:260px;">Search needs network. Confirmed passes still open offline from Bookings.</div>
        <div class="card" style="padding:14px;width:100%;text-align:left;">
          <div class="meta">Zero silent failure: we never show stale capacity as live.</div>
        </div>
      </div>
      <div class="sticky-bottom" style="display:grid;grid-template-columns:1fr 1fr;gap:10px;">
        {btn("Open passes", "secondary")}{btn("Retry")}
      </div>
    """))

    screens.append(phone("DRV-21", "Monthly passes", f"""
      {status()}
      {nav("Passes")}
      <div class="pad grow">
        <div class="card" style="padding:0;overflow:hidden;background:var(--navy);color:#fff;">
          <div style="padding:18px;">
            <div class="meta" style="color:#94A3B8;">ACTIVE</div>
            <div class="h2" style="color:#fff;margin:6px 0;">Cyber City Unlimited</div>
            <div class="meta" style="color:#CBD5E1;">KA 01 MJ 8821 · ends 31 Oct</div>
            <div class="progress" style="margin-top:14px;background:#334155;"><i style="width:62%;"></i></div>
          </div>
        </div>
        <div class="card" style="padding:14px;margin-top:12px;">
          <div class="row-between"><span>AutoPay</span><span class="pill teal">ON · ₹3,499/mo</span></div>
          <div class="meta" style="margin-top:6px;">24h pre-debit notification required</div>
        </div>
        <div class="label" style="margin:16px 0 8px;">CATALOG</div>
        <div class="card" style="padding:14px;margin-bottom:8px;"><strong>Weekday Commuter</strong><div class="meta">08:00–20:00 · ₹2,199</div></div>
        <div class="card" style="padding:14px;"><strong>Two-wheeler Unlimited</strong><div class="meta">₹899/mo</div></div>
      </div>
      {tabbar("Passes")}
    """))

    screens.append(phone("DRV-23", "Support case", f"""
      {status()}
      {nav("Report a problem")}
      <div class="pad grow">
        <div class="card" style="padding:14px;">
          <div class="meta">Linked booking</div>
          <div class="h3" style="font-size:15px;margin-top:4px;">#SP-99214 · Indiranagar · B2-19</div>
        </div>
        <div class="label" style="margin:14px 0 8px;">CATEGORY</div>
        <div class="grid-2">
          <div class="class-tile on">Overcharge</div><div class="class-tile">Access issue</div>
          <div class="class-tile">Damage</div><div class="class-tile">Other</div>
        </div>
        <div class="label" style="margin:14px 0 8px;">DETAILS</div>
        <div style="min-height:100px;border:1.5px solid var(--border);border-radius:14px;padding:12px;background:#fff;color:var(--text-2);">Describe what happened…</div>
        <div class="meta" style="margin-top:10px;">Support SLA: first response in 4 business hours</div>
      </div>
      <div class="sticky-bottom">{btn("Submit case")}</div>
    """))

    screens.append(phone("DRV-24", "Profile & settings", f"""
      {status()}
      <div class="pad" style="padding-top:8px;">
        <div class="h2">Profile</div>
      </div>
      <div class="pad grow" style="padding-top:0;">
        <div class="card lift" style="padding:16px;margin-bottom:14px;display:flex;gap:14px;align-items:center;">
          <div style="width:56px;height:56px;border-radius:18px;background:linear-gradient(145deg,#2DD4BF,#0D9488);color:#fff;display:grid;place-items:center;font-weight:800;font-size:20px;">MG</div>
          <div style="flex:1;">
            <div class="h3">Mahesh Giri</div>
            <div class="meta">+91 98765 43210</div>
            <div class="meta" style="color:var(--teal-deep);font-weight:700;margin-top:2px;">Edit profile</div>
          </div>
        </div>
        <div class="label" style="margin-bottom:4px;">ACCOUNT</div>
        <div class="settings-row"><div class="ico-tile">🚗</div><div class="grow-col"><strong style="font-size:14px;">Vehicle garage</strong><div class="meta">2 vehicles</div></div><div class="chev">→</div></div>
        <div class="settings-row"><div class="ico-tile">₹</div><div class="grow-col"><strong style="font-size:14px;">Payment methods</strong><div class="meta">UPI · cards</div></div><div class="chev">→</div></div>
        <div class="settings-row"><div class="ico-tile">◎</div><div class="grow-col"><strong style="font-size:14px;">Wallet &amp; credits</strong><div class="meta">₹100 goodwill</div></div><div class="chev">→</div></div>
        <div class="label" style="margin:14px 0 4px;">PREFERENCES</div>
        <div class="settings-row"><div class="ico-tile">🔔</div><div class="grow-col"><strong style="font-size:14px;">Notifications</strong><div class="meta">Push · WhatsApp · SMS</div></div><div class="chev">→</div></div>
        <div class="settings-row"><div class="ico-tile">अ</div><div class="grow-col"><strong style="font-size:14px;">Language</strong><div class="meta">English</div></div><div class="chev">→</div></div>
        <div class="label" style="margin:14px 0 4px;">SUPPORT &amp; LEGAL</div>
        <div class="settings-row"><div class="ico-tile">?</div><div class="grow-col"><strong style="font-size:14px;">Help &amp; FAQ</strong></div><div class="chev">→</div></div>
        <div class="settings-row"><div class="ico-tile">🛡</div><div class="grow-col"><strong style="font-size:14px;">Privacy &amp; DPDP rights</strong></div><div class="chev">→</div></div>
        <div class="settings-row"><div class="ico-tile">📄</div><div class="grow-col"><strong style="font-size:14px;">Terms · Privacy · About</strong></div><div class="chev">→</div></div>
        <div class="settings-row" style="border:0;"><div class="ico-tile" style="background:var(--danger-bg);color:var(--danger);">⎋</div><div class="grow-col"><strong style="font-size:14px;color:var(--danger);">Sign out</strong></div></div>
      </div>
      {tabbar("Profile")}
    """))

    screens.append(phone("DRV-28", "Notification prefs", f"""
      {status()}
      {nav("Notifications")}
      <div class="pad grow">
        <div class="card" style="padding:16px;margin-bottom:12px;">
          <div class="row-between" style="margin-bottom:14px;"><div><strong>Push</strong><div class="meta">Device alerts</div></div><div class="toggle on"></div></div>
          <div class="row-between" style="margin-bottom:14px;"><div><strong>WhatsApp</strong><div class="meta">Opt-in · DLT</div></div><div class="toggle on"></div></div>
          <div class="row-between"><div><strong>SMS</strong><div class="meta">Fallback channel</div></div><div class="toggle"></div></div>
        </div>
        <div class="label" style="margin-bottom:8px;">EVENT TYPES</div>
        <div class="card" style="padding:16px;">
          <div class="row-between" style="margin-bottom:12px;"><span>Booking &amp; pass</span><div class="toggle on"></div></div>
          <div class="row-between" style="margin-bottom:12px;"><span>T-15 / expiry</span><div class="toggle on"></div></div>
          <div class="row-between" style="margin-bottom:12px;"><span>Overstay accrual</span><div class="toggle on"></div></div>
          <div class="row-between" style="margin-bottom:12px;"><span>Refund updates</span><div class="toggle on"></div></div>
          <div class="row-between"><span>Offers &amp; promos</span><div class="toggle"></div></div>
        </div>
      </div>
      <div class="sticky-bottom">{btn("Save preferences")}</div>
    """))

    screens.append(phone("DRV-29", "Legal & about", f"""
      {status()}
      {nav("Legal & about")}
      <div class="pad grow">
        <div class="settings-row"><div class="ico-tile">ℹ</div><div class="grow-col"><strong style="font-size:14px;">About ParkSpot</strong><div class="meta">v1.0.0 (build 240)</div></div><div class="chev">→</div></div>
        <div class="settings-row"><div class="ico-tile">📄</div><div class="grow-col"><strong style="font-size:14px;">Terms of Service</strong><div class="meta">Updated 12 Oct 2026</div></div><div class="chev">→</div></div>
        <div class="settings-row"><div class="ico-tile">🔒</div><div class="grow-col"><strong style="font-size:14px;">Privacy Policy</strong><div class="meta">DPDP-aligned</div></div><div class="chev">→</div></div>
        <div class="settings-row"><div class="ico-tile">✉</div><div class="grow-col"><strong style="font-size:14px;">Grievance officer</strong><div class="meta">grievance@parkspot.in</div></div><div class="chev">→</div></div>
        <div class="settings-row"><div class="ico-tile">⚖</div><div class="grow-col"><strong style="font-size:14px;">Open-source licenses</strong></div><div class="chev">→</div></div>
        <div class="settings-row" style="border:0;"><div class="ico-tile">★</div><div class="grow-col"><strong style="font-size:14px;">Rate the app</strong></div><div class="chev">→</div></div>
      </div>
    """))

    screens.append(phone("DRV-29A", "About", f"""
      {status()}
      {nav("About ParkSpot")}
      <div class="pad grow" style="text-align:center;">
        <div style="width:72px;height:72px;border-radius:22px;background:linear-gradient(145deg,#2DD4BF,#0D9488);color:#fff;display:grid;place-items:center;font-weight:900;font-size:32px;margin:12px auto 16px;box-shadow:var(--shadow-md);">P</div>
        <div class="h2">ParkSpot</div>
        <div class="meta" style="margin-top:6px;">Bay certainty · Honest price</div>
        <div class="card" style="padding:16px;margin-top:20px;text-align:left;">
          <div class="legal-body">
            ParkSpot helps drivers find parking with honest availability and clear GST-inclusive quotes. Operators keep the parking supply; we run discovery, booking, credentials, and payouts.
            <h4>Version</h4>
            App 1.0.0 · API 3.0 · Credential Ed25519
            <h4>Made for India</h4>
            UPI · HSRP plates · IST · en / हिन्दी
          </div>
        </div>
      </div>
      <div class="sticky-bottom">{btn("Open Terms", "secondary")}</div>
    """))

    screens.append(phone("DRV-29T", "Terms of Service", f"""
      {status()}
      {nav("Terms of Service", "Effective 12 Oct 2026")}
      <div class="pad grow">
        <div class="legal-body">
          <h4 style="margin-top:0;">1. Service</h4>
          ParkSpot provides marketplace software for parking discovery, reservation, floating sessions, and digital passes. The facility operator is the supplier of parking. ParkSpot supplies the platform fee line where applicable.
          <h4>2. Bookings &amp; leases</h4>
          Quotes create a short lease (typically 10 minutes). Payment confirmation issues an Ed25519-signed pass. No-shows and cancellations follow the published refund policy at checkout.
          <h4>3. SLA &amp; SOS</h4>
          Numbered-bay SLA (where opted in) may include reseat or refund + goodwill credit. Abuse of SOS is monitored.
          <h4>4. Liability</h4>
          ParkSpot is not a bailee of the vehicle. Facility rules and local law apply on premises.
          <h4>5. Contact</h4>
          support@parkspot.in · Grievance: grievance@parkspot.in
        </div>
      </div>
      <div class="sticky-bottom">{btn("Back to legal")}</div>
    """))

    screens.append(phone("DRV-29P", "Privacy Policy", f"""
      {status()}
      {nav("Privacy Policy", "DPDP Act 2023")}
      <div class="pad grow">
        <div class="legal-body">
          <h4 style="margin-top:0;">What we collect</h4>
          Phone, name, vehicles (VRN encrypted + hash), booking history, approximate location for search, device push tokens, payment references (not full card data).
          <h4>Purposes</h4>
          Account, booking, gate credentials, invoices, fraud prevention, support, legal obligations (tax/audit).
          <h4>Retention</h4>
          Account life + 90 days; financial records longer as required; ANPR images short-lived unless disputed.
          <h4>Your rights</h4>
          Access, correction, erasure (with legal holds), consent withdraw for optional purposes. Use in-app DPDP desk or write to dpo@parkspot.in.
          <h4>Processors</h4>
          Payment aggregator, SMS/WhatsApp DLT providers, cloud in India regions.
        </div>
      </div>
      <div class="sticky-bottom">{btn("Manage consents", "secondary")}</div>
    """))

    screens.append(phone("DRV-24D", "DPDP rights", f"""
      {status()}
      {nav("Your data rights")}
      <div class="pad grow">
        <div class="card" style="padding:14px;margin-bottom:10px;">
          <div class="row-between"><strong>Download my data</strong><span class="pill teal">Export</span></div>
          <div class="meta" style="margin-top:6px;">ZIP within 7 days · bookings, invoices, consents</div>
        </div>
        <div class="card" style="padding:14px;margin-bottom:10px;">
          <div class="row-between"><strong>Correct profile</strong><span class="chev">→</span></div>
          <div class="meta" style="margin-top:6px;">Name, email, vehicle plate typos</div>
        </div>
        <div class="card" style="padding:14px;margin-bottom:10px;">
          <div class="row-between"><strong>Manage consents</strong><span class="chev">→</span></div>
          <div class="meta" style="margin-top:6px;">Marketing · WhatsApp · location precision</div>
        </div>
        <div class="card" style="padding:14px;border-color:#FECACA;background:var(--danger-bg);">
          <div class="h3" style="font-size:14px;color:var(--danger);">Delete account</div>
          <div class="meta" style="margin-top:6px;">Erasure request · 90-day SLA · ledger may retain masked IDs</div>
        </div>
      </div>
      <div class="sticky-bottom">{btn("Request data export")}</div>
    """))

    screens.append(phone("DRV-30", "Payment methods", f"""
      {status()}
      {nav("Payment methods")}
      <div class="pad grow">
        <div class="card selected" style="padding:14px;margin-bottom:10px;">
          <div class="row-between"><strong>UPI · @maheshgiri</strong><span class="pill ok">Default</span></div>
          <div class="meta" style="margin-top:6px;">GPay · PhonePe · any UPI app</div>
        </div>
        <div class="card" style="padding:14px;margin-bottom:10px;">
          <div class="row-between"><strong>UPI AutoPay</strong><span class="pill teal">Pass renewals</span></div>
          <div class="meta" style="margin-top:6px;">Mandate active · 24h pre-debit notice</div>
        </div>
        <div class="card" style="padding:14px;margin-bottom:10px;">
          <div class="row-between"><strong>Cards</strong><span class="meta">•••• 4242</span></div>
          <div class="meta" style="margin-top:6px;">Via payment aggregator · PCI handled by PA</div>
        </div>
        <div class="meta">ParkSpot never stores full card PAN. Refunds return to original method.</div>
      </div>
      <div class="sticky-bottom">{btn("Add UPI / card")}</div>
    """))

    screens.append(phone("DRV-31", "Help & FAQ", f"""
      {status()}
      {nav("Help")}
      <div class="pad grow">
        <div class="input" style="margin-bottom:14px;color:var(--text-2);">Search help…</div>
        <div class="card" style="padding:14px;margin-bottom:8px;"><strong style="font-size:14px;">How do I enter the facility?</strong><div class="meta" style="margin-top:6px;">Show the digital pass QR · attendant or gate scanner verifies Ed25519 signature.</div></div>
        <div class="card" style="padding:14px;margin-bottom:8px;"><strong style="font-size:14px;">What if my bay is occupied?</strong><div class="meta" style="margin-top:6px;">Use SOS · we reseat or refund + credit per facility SLA.</div></div>
        <div class="card" style="padding:14px;margin-bottom:8px;"><strong style="font-size:14px;">Cancellation &amp; refunds</strong><div class="meta" style="margin-top:6px;">Policy shown on quote · tracker in Bookings.</div></div>
        <div class="card" style="padding:14px;"><strong style="font-size:14px;">Contact support</strong><div class="meta" style="margin-top:6px;">In-app case · SLA 4 business hours</div></div>
      </div>
      <div class="sticky-bottom">{btn("Start a support case")}</div>
    """))

    screens.append(phone("DRV-20E", "Bookings empty", f"""
      {status()}
      {nav("Bookings")}
      <div class="pad grow">
        <div class="empty-hero">
          <div class="glyph">◎</div>
          <div class="h2">No bookings yet</div>
          <div class="body" style="margin-top:8px;">Find a facility nearby, lock a bay, and your pass will show up here.</div>
        </div>
      </div>
      <div class="sticky-bottom">{btn("Explore parking")}</div>
      {tabbar("Bookings")}
    """))

    screens.append(phone("DRV-32", "Language", f"""
      {status()}
      {nav("Language")}
      <div class="pad grow">
        <div class="class-tile on" style="height:64px;margin-bottom:10px;flex-direction:row;justify-content:space-between;padding:0 16px;"><span>English</span><span style="color:var(--teal);font-weight:800;">✓</span></div>
        <div class="class-tile" style="height:64px;margin-bottom:10px;flex-direction:row;justify-content:space-between;padding:0 16px;"><span>हिन्दी</span><span></span></div>
        <div class="meta">More languages roll out city by city. Notification templates follow your choice.</div>
      </div>
      <div class="sticky-bottom">{btn("Save language")}</div>
    """))

    screens.append(phone("DRV-33", "Wallet & credits", f"""
      {status()}
      {nav("Wallet")}
      <div class="pad grow">
        <div class="card" style="padding:20px;background:linear-gradient(145deg,#0F766E,#0B1220);color:#fff;border:0;">
          <div class="meta" style="color:#99F6E4;">AVAILABLE CREDIT</div>
          <div class="h1 currency" style="color:#fff;margin-top:8px;font-size:36px;">₹100.00</div>
          <div class="meta" style="color:#CBD5E1;margin-top:6px;">Goodwill · SOS SLA · expires 90 days</div>
        </div>
        <div class="label" style="margin:16px 0 8px;">HISTORY</div>
        <div class="list-item row-between"><div><strong>SOS goodwill</strong><div class="meta">#SP-99102</div></div><strong class="currency" style="color:var(--ok);">+₹100</strong></div>
        <div class="list-item row-between" style="border:0;"><div><strong>Promo PARK10</strong><div class="meta">Used on #SP-99001</div></div><strong class="currency">−₹10</strong></div>
        <div class="meta" style="margin-top:8px;">Credits apply at checkout before UPI. Ledger-backed · abuse controls apply.</div>
      </div>
      <div class="sticky-bottom">{btn("Apply to next booking")}</div>
    """))

    screens.append(phone("DRV-34", "Location denied", f"""
      {status()}
      <div class="pad grow" style="display:flex;flex-direction:column;justify-content:center;">
        <div class="empty-hero" style="padding:20px 8px;">
          <div class="glyph">◎</div>
          <div class="h2">Location is off</div>
          <div class="body" style="margin-top:8px;">Enable location for nearby results, or search a landmark / area manually.</div>
        </div>
        <div class="input" style="margin-top:8px;">Search Indiranagar, Koramangala…</div>
      </div>
      <div class="sticky-bottom" style="display:grid;grid-template-columns:1fr 1.2fr;gap:10px;">
        {btn("Open Settings", "secondary")}{btn("Continue")}
      </div>
    """))

    return '<div class="row">' + "".join(screens) + "</div>"


def attendant_screens():
    screens = []
    dock = lambda active: f"""
    <div style="position:absolute;bottom:0;left:0;right:0;height:72px;background:#fff;border-top:1px solid var(--border);display:grid;grid-template-columns:repeat(4,1fr);padding:8px 4px 18px;font-size:11px;font-weight:700;color:#94A3B8;">
      {"".join(f'<div style="text-align:center;color:{"var(--teal)" if t==active else "#94A3B8"};">{t}</div>' for t in ["Scan","Walk-in","Exit","Shift"])}
    </div>"""

    screens.append(phone("ATT-01", "Shift login", f"""
      {status()}
      <div class="pad grow" style="display:flex;flex-direction:column;justify-content:center;">
        <div class="h2">Attendant login</div>
        <div class="meta" style="margin:8px 0 20px;">POS-04 · Indiranagar Gate 2 · Lane 02</div>
        <div class="input" style="margin-bottom:10px;letter-spacing:.3em;justify-content:center;">••••</div>
        <div class="meta" style="text-align:center;">PIN or biometric · device-bound</div>
      </div>
      <div class="sticky-bottom">{btn("Unlock shift")}</div>
    """))

    screens.append(phone("ATT-02", "Open shift / float", f"""
      {status()}
      {nav("Open shift", "Count opening float")}
      <div class="pad grow">
        <div class="grid-2">
          <div class="card" style="padding:12px;text-align:center;"><div class="meta">₹500</div><div class="h3">× 4</div></div>
          <div class="card" style="padding:12px;text-align:center;"><div class="meta">₹200</div><div class="h3">× 5</div></div>
          <div class="card" style="padding:12px;text-align:center;"><div class="meta">₹100</div><div class="h3">× 10</div></div>
          <div class="card" style="padding:12px;text-align:center;"><div class="meta">₹50</div><div class="h3">× 6</div></div>
        </div>
        <div class="card" style="padding:14px;margin-top:12px;">
          <div class="row-between"><span>Opening float</span><strong class="currency">₹4,300</strong></div>
        </div>
        <span class="pill ok" style="margin-top:12px;">Keys valid · Manifest 11h 40m</span>
      </div>
      <div class="sticky-bottom">{btn("Start shift")}</div>
    """))

    screens.append(phone("ATT-10", "QR scanner", f"""
      {status(True)}
      <div style="flex:1;position:relative;overflow:hidden;">
        <img class="img-cover" src="{ASSETS['garage']}" alt="" style="filter:brightness(.5);"/>
        <div style="position:absolute;top:12px;left:12px;right:12px;display:flex;flex-wrap:wrap;gap:6px;">
          <span class="chip" style="background:rgba(15,23,42,.75);color:#E2E8F0;border-radius:8px;padding:6px 8px;font-size:10px;font-weight:700;">POS-04</span>
          <span style="background:rgba(180,83,9,.9);color:#FEF3C7;border-radius:8px;padding:6px 8px;font-size:10px;font-weight:700;">OFFLINE · Ed25519</span>
        </div>
        <div style="position:absolute;left:50%;top:42%;transform:translate(-50%,-50%);width:200px;height:200px;border:2px solid #34D399;border-radius:24px;box-shadow:0 0 0 9999px rgba(15,23,42,.4);"></div>
      </div>
      <div style="background:#fff;border-radius:24px 24px 0 0;padding:16px 16px 80px;">
        <span class="pill ok">PASS VERIFIED · 180ms</span>
        <div class="h3 plate" style="margin-top:10px;">KA 01 MJ 8821</div>
        <div class="meta">Car · B2-19 · 18:00–20:00</div>
        {btn("Confirm & open barrier")}
      </div>
      {dock("Scan")}
    """, bg="var(--navy)"))

    screens.append(phone("ATT-11", "Entry confirm", f"""
      {status()}
      {nav("Confirm entry")}
      <div class="pad grow">
        <div class="card" style="padding:16px;">
          <div class="plate" style="font-size:20px;font-weight:800;">KA 01 MJ 8821</div>
          <div class="meta" style="margin-top:8px;">Car · Booking #SP-99214</div>
          <div class="h3" style="margin-top:12px;">Bay B2-19</div>
          <div class="meta">Window 18:00–20:00 · plate match ✓</div>
        </div>
      </div>
      <div class="sticky-bottom" style="display:grid;grid-template-columns:1.3fr .8fr;gap:10px;">
        {btn("Confirm & open")}{btn("Override…", "secondary")}
      </div>
    """))

    screens.append(phone("ATT-10R", "Pass rejected", f"""
      {status()}
      {nav("Verification failed")}
      <div class="pad grow">
        <div class="card" style="padding:16px;background:var(--danger-bg);border-color:#FECACA;">
          <div class="h3" style="color:var(--danger);">REJECTED</div>
          <div class="meta" style="margin-top:6px;">Do not open barrier</div>
        </div>
        <div class="card" style="padding:14px;margin-top:12px;">
          <div class="label">REASON</div>
          <div class="h3" style="margin-top:6px;">Nonce revoked / already used</div>
          <div class="meta" style="margin-top:8px;">Also common: expired window · plate mismatch · wrong facility · signature invalid</div>
        </div>
        <div class="grid-2" style="margin-top:12px;">
          <div class="class-tile">Plate lookup</div><div class="class-tile">Walk-in</div>
        </div>
      </div>
      <div class="sticky-bottom">{btn("Scan next")}</div>
    """))

    screens.append(phone("ATT-03", "Plate lookup", f"""
      {status()}
      {nav("Find booking", "Today's manifest")}
      <div class="pad grow">
        <div class="input plate" style="letter-spacing:.08em;">KA 01 MJ 8821</div>
        <div class="card" style="padding:14px;margin-top:12px;border-color:var(--teal);">
          <div class="row-between"><strong>#SP-99214</strong><span class="pill ok">CONFIRMED</span></div>
          <div class="meta" style="margin-top:6px;">Bay B2-19 · 18:00–20:00 · Car</div>
          <div class="meta">Photo capture optional for audit</div>
        </div>
        <div class="card" style="padding:14px;margin-top:10px;">
          <div class="row-between"><strong>#SP-99001</strong><span class="pill stale">NO SHOW</span></div>
          <div class="meta" style="margin-top:6px;">Same plate · morning window</div>
        </div>
      </div>
      <div class="sticky-bottom" style="display:grid;grid-template-columns:1fr 1.2fr;gap:10px;">
        {btn("Capture photo", "secondary")}{btn("Confirm entry")}
      </div>
    """))

    screens.append(phone("ATT-08O", "Override + PIN", f"""
      {status()}
      {nav("Manual override", "Reason mandatory")}
      <div class="pad grow">
        <div class="label">REASON CODE</div>
        <div class="grid-2" style="margin-top:8px;">
          <div class="class-tile on">Scanner fault</div><div class="class-tile">VIP admit</div>
          <div class="class-tile">Ambulance</div><div class="class-tile">Other</div>
        </div>
        <div class="label" style="margin-top:14px;">FREE TEXT</div>
        <div class="input" style="margin-top:8px;color:var(--text-2);">Camera fogged · basement</div>
        <div class="card" style="padding:14px;margin-top:12px;background:var(--warn-bg);border-color:#FCD34D;">
          <div class="h3" style="font-size:14px;color:var(--warn);">Supervisor PIN required</div>
          <div class="meta">3rd override this shift</div>
          <div class="input" style="margin-top:10px;letter-spacing:.35em;justify-content:center;">••••</div>
        </div>
      </div>
      <div class="sticky-bottom">{btn("Authorize override", "navy")}</div>
    """))

    screens.append(phone("ATT-16", "Walk-in admit", f"""
      {status()}
      {nav("Walk-in admission")}
      <div class="pad grow">
        <div class="stepper"><span class="on"></span><span class="on"></span><span></span></div>
        <div class="label">CLASS</div>
        <div class="grid-3" style="margin:8px 0 14px;">
          <div class="class-tile">2W</div><div class="class-tile on">Car</div><div class="class-tile">Auto</div>
        </div>
        <div class="label">PLATE</div>
        <div class="input plate" style="margin-top:8px;letter-spacing:.08em;">KA 05 XY 2211</div>
        <div class="card" style="padding:12px;margin-top:12px;">
          <div class="row-between"><span>Float buffer left</span><span class="pill warn">3 car</span></div>
        </div>
      </div>
      <div class="sticky-bottom">{btn("Admit & print slip")}</div>
      {dock("Walk-in")}
    """))

    screens.append(phone("ATT-16F", "Capacity full", f"""
      {status()}
      {nav("Cannot admit")}
      <div class="pad grow">
        <div class="card" style="padding:16px;background:var(--danger-bg);border-color:#FECACA;">
          <div class="h3" style="color:var(--danger);">CAPACITY_FULL</div>
          <div class="meta" style="margin-top:6px;">Float buffer exhausted · no free Car capacity · bay reserved within 60m</div>
        </div>
        <div class="card" style="padding:14px;margin-top:12px;">
          <div class="meta">Attendant MUST NOT admit. Override needs supervisor PIN and is reported to leakage audit.</div>
        </div>
      </div>
      <div class="sticky-bottom" style="display:grid;grid-template-columns:1fr 1fr;gap:10px;">
        {btn("Dismiss", "secondary")}{btn("Override…", "navy")}
      </div>
    """))

    screens.append(phone("ATT-12", "Exit & dues", f"""
      {status()}
      {nav("Exit clearance")}
      <div class="pad grow">
        <div class="card" style="padding:14px;">
          <div class="plate" style="font-weight:800;">KA 05 XY 2211</div>
          <div class="meta">Walk-in · 2h 14m · Surface Lot A</div>
        </div>
        <div class="card" style="padding:14px;margin-top:12px;">
          <div class="row-between"><span>Walk-in tariff</span><strong>₹80.00</strong></div>
          <div class="row-between" style="padding:8px 0;"><span>GST</span><strong>₹14.40</strong></div>
          <div class="row-between" style="border-top:1px solid var(--border);padding-top:12px;">
            <span class="h3">Collect</span><span class="h2 currency">₹94.40</span>
          </div>
        </div>
        <div class="grid-2" style="margin-top:12px;">
          <div class="class-tile on">UPI QR</div><div class="class-tile">Cash</div>
        </div>
      </div>
      <div class="sticky-bottom">{btn("Mark paid & open exit")}</div>
      {dock("Exit")}
    """))

    screens.append(phone("ATT-12Q", "Exit UPI QR", f"""
      {status()}
      {nav("Collect dues", "Amount-locked UPI QR")}
      <div class="pad grow" style="text-align:center;">
        <div class="h2 currency">₹94.40</div>
        <div class="meta">Walk-in · KA 05 XY 2211</div>
        <div style="width:200px;height:200px;margin:20px auto;background:#fff;border:1px solid var(--border);border-radius:16px;display:grid;place-items:center;box-shadow:var(--shadow-md);">
          <img src="{ASSETS['qr']}" width="168" height="168" alt="UPI QR"/>
        </div>
        <div class="meta">Driver scans with any UPI app · webhook confirms before barrier</div>
        <div class="grid-2" style="margin-top:16px;text-align:left;">
          <div class="class-tile">Cash instead</div><div class="class-tile">Mark prepaid</div>
        </div>
      </div>
      <div class="sticky-bottom">{btn("Waiting for payment…", "secondary")}</div>
    """))

    screens.append(phone("ATT-05H", "Shift handover", f"""
      {status()}
      {nav("Handover", "Outgoing CLOSING")}
      <div class="pad grow">
        <div class="card" style="padding:14px;">
          <div class="row-between"><span>Outgoing</span><strong>Ramesh #B409</strong></div>
          <div class="row-between" style="margin-top:8px;"><span>Incoming</span><strong>Sunil Sharma</strong></div>
          <div class="row-between" style="margin-top:8px;"><span>Cash counted</span><strong class="currency">₹3,420</strong></div>
          <div class="row-between" style="margin-top:8px;"><span>Variance</span><span class="pill ok">ZERO</span></div>
        </div>
        <div class="card" style="padding:14px;margin-top:12px;">
          <div class="meta">Manager acknowledge required if SHORT/OVER &gt; ₹200 or &gt;1%</div>
          <div class="input" style="margin-top:10px;letter-spacing:.3em;justify-content:center;">Manager PIN</div>
        </div>
      </div>
      <div class="sticky-bottom">{btn("Print slip & close shift")}</div>
    """))

    screens.append(phone("ATT-13", "Offline mode", f"""
      {status()}
      <div style="background:var(--warn-bg);color:var(--warn);padding:10px 16px;font-size:12px;font-weight:700;flex-shrink:0;">
        OFFLINE · local Ed25519 verify · queue 7 events · manifest age 42m
      </div>
      {nav("Offline operations")}
      <div class="pad grow">
        <div class="card" style="padding:14px;">
          <div class="row-between"><span>Clock skew</span><span class="pill warn">+48s</span></div>
          <div class="row-between" style="margin-top:10px;"><span>Cached keys</span><span class="pill ok">Valid</span></div>
          <div class="row-between" style="margin-top:10px;"><span>Revocation delta</span><strong>12 entries</strong></div>
        </div>
        <div class="meta" style="margin-top:12px;">Cash still recorded locally · sync on reconnect</div>
      </div>
      <div class="sticky-bottom">{btn("Continue scanning")}</div>
    """))

    screens.append(phone("ATT-05", "Shift close", f"""
      {status()}
      {nav("Close shift")}
      <div class="pad grow">
        <div class="card" style="padding:14px;">
          <div class="row-between"><span>Vehicles</span><strong>184</strong></div>
          <div class="row-between" style="padding:6px 0;"><span>Pre-book / walk-in</span><strong>142 / 42</strong></div>
          <div class="row-between"><span>Digital collections</span><strong>₹11,400</strong></div>
          <div class="row-between"><span>Cash expected</span><strong>₹3,420</strong></div>
        </div>
        <div class="card" style="padding:14px;margin-top:12px;">
          <div class="label">COUNTED CASH</div>
          <div class="h2 currency" style="margin:8px 0;">₹3,420</div>
          <span class="pill ok">Δ ₹0.00 · ZERO VARIANCE</span>
        </div>
        <div class="meta" style="margin-top:10px;">T1: loop vs digital Δ = 0 unexplained</div>
      </div>
      <div class="sticky-bottom">{btn("Print handover & close")}</div>
      {dock("Shift")}
    """))

    screens.append(phone("ATT-08", "Incident capture", f"""
      {status()}
      {nav("Capture incident")}
      <div class="pad grow">
        <div class="grid-2">
          <div class="class-tile on">Squatter</div><div class="class-tile">Damage</div>
          <div class="class-tile">Tailgate</div><div class="class-tile">Dispute</div>
        </div>
        <div style="height:140px;margin-top:14px;border-radius:16px;background:var(--muted);display:grid;place-items:center;font-weight:700;color:var(--text-2);">Add photo</div>
        <div class="input" style="margin-top:12px;color:var(--text-2);">Notes…</div>
      </div>
      <div class="sticky-bottom">{btn("Submit incident")}</div>
    """))

    screens.append(phone("ATT-11L", "Lane / barrier T1", f"""
      {status()}
      {nav("Lane control", "Gate 2 · T1 connected")}
      <div class="pad grow">
        <div class="grid-2">
          <div class="card" style="padding:14px;"><div class="label">LOOP A</div><div class="h3" style="color:var(--ok);">Clear</div></div>
          <div class="card" style="padding:14px;"><div class="label">LOOP B</div><div class="h3" style="color:var(--warn);">Occupied</div></div>
          <div class="card" style="padding:14px;"><div class="label">BARRIER</div><div class="h3">Closed</div></div>
          <div class="card" style="padding:14px;"><div class="label">GATEWAY</div><div class="h3" style="color:var(--ok);">Online</div></div>
        </div>
        <div class="meta" style="margin-top:12px;">Safe open requires reason if no valid credential</div>
      </div>
      <div class="sticky-bottom" style="display:grid;grid-template-columns:1fr 1fr;gap:10px;">
        {btn("Safe open", "secondary")}{btn("Close barrier", "navy")}
      </div>
    """))

    return '<div class="row">' + "".join(screens) + "</div>"


def operator_nav(active):
    items = ["Overview","Live board","Zones","Tariffs","Bookings","Staff","Reports","Payouts","Disputes","Settings"]
    return "".join(f'<a class="{"on" if i==active else ""}" href="#">{i}</a>' for i in items)

def desk_frame(sid, title, active_nav, body_html, top_right=""):
    return desk(sid, title, f"""
    <div class="desk-shell">
      <aside class="desk-nav"><div class="logo">Park<span style="color:#5EEAD4;">Spot</span> Ops</div>{operator_nav(active_nav)}</aside>
      <section class="desk-main">
        <header class="desk-top">
          <div><div class="h3" style="font-size:15px;">Indiranagar Metro MLCP</div><div class="meta">Tier 1 · Bengaluru</div></div>
          <div>{top_right}</div>
        </header>
        <div class="desk-body">{body_html}</div>
      </section>
    </div>""")


def operator_screens():
    screens = []

    def kyc_shell(step, title, body):
        dots = "".join(f'<span class="{"on" if i < step else ""}"></span>' for i in range(7))
        return desk(f"OPR-01.{step}", title, f"""
    <div class="desk-shell">
      <aside class="desk-nav"><div class="logo">ParkSpot Ops</div><a class="on">Onboarding</a></aside>
      <section class="desk-main">
        <header class="desk-top"><div class="h3">Operator onboarding</div><span class="pill info">Step {step} / 7</span></header>
        <div class="desk-body">
          <div class="stepper">{dots}</div>
          {body}
        </div>
      </section>
    </div>""")

    screens.append(kyc_shell(1, "KYC · Business", """
          <div class="card" style="padding:20px;max-width:720px;">
            <div class="h3">Business entity</div>
            <div class="grid-2" style="margin-top:14px;">
              <div><div class="label">LEGAL NAME</div><div class="input" style="margin-top:6px;">Nexus Parking Pvt Ltd</div></div>
              <div><div class="label">ENTITY TYPE</div><div class="input" style="margin-top:6px;">Private Limited</div></div>
              <div><div class="label">PAN</div><div class="input" style="margin-top:6px;">AABCN8821F</div></div>
              <div><div class="label">CIN / LLPIN</div><div class="input" style="margin-top:6px;">U63030KA2019PTC…</div></div>
            </div>
            <div style="margin-top:14px;"><button class="btn primary">Continue</button></div>
          </div>"""))

    screens.append(kyc_shell(2, "KYC · GSTIN", """
          <div class="card" style="padding:20px;max-width:720px;">
            <div class="h3">GST registration</div>
            <div class="label" style="margin-top:14px;">GSTIN</div>
            <div class="input" style="margin-top:6px;">29AABCN8821F1Z5</div>
            <div class="meta" style="margin-top:10px;">Auto-fetched: Nexus Parking Pvt Ltd · Karnataka · Active</div>
            <div class="list-item row-between" style="margin-top:12px;"><span>Place of supply default</span><strong>KA</strong></div>
            <div style="margin-top:14px;"><button class="btn primary">Continue</button></div>
          </div>"""))

    screens.append(kyc_shell(3, "KYC · Bank", """
          <div class="card" style="padding:20px;max-width:720px;">
            <div class="h3">Bank account · penny-drop</div>
            <div class="grid-2" style="margin-top:14px;">
              <div><div class="label">ACCOUNT</div><div class="input" style="margin-top:6px;">XXXXXXXX4521</div></div>
              <div><div class="label">IFSC</div><div class="input" style="margin-top:6px;">HDFC0001234</div></div>
            </div>
            <div class="card" style="padding:12px;margin-top:12px;background:var(--ok-bg);border-color:#A7F3D0;">
              <div class="row-between"><span>Name match</span><span class="pill ok">PASS</span></div>
              <div class="meta" style="margin-top:6px;">₹1 credited · UTR HDFC…9912</div>
            </div>
            <div style="margin-top:14px;"><button class="btn primary">Continue</button></div>
          </div>"""))

    screens.append(kyc_shell(4, "KYC · Documents", """
          <div class="card" style="padding:20px;max-width:720px;">
            <div class="h3">Upload documents</div>
            <div class="list-item row-between"><span>PAN card</span><span class="pill ok">Uploaded</span></div>
            <div class="list-item row-between"><span>GST certificate</span><span class="pill ok">Uploaded</span></div>
            <div class="list-item row-between"><span>Cancelled cheque / passbook</span><span class="pill ok">Uploaded</span></div>
            <div class="list-item row-between" style="border:0;"><span>Lease / ownership proof</span><span class="pill warn">Required</span></div>
            <div style="margin-top:14px;display:flex;gap:10px;"><button class="btn secondary">Upload lease</button><button class="btn primary">Continue</button></div>
          </div>"""))

    screens.append(kyc_shell(5, "KYC · Authorized signatory", """
          <div class="card" style="padding:20px;max-width:720px;">
            <div class="h3">Authorized signatory</div>
            <div class="grid-2" style="margin-top:14px;">
              <div><div class="label">NAME</div><div class="input" style="margin-top:6px;">Ananya Rao</div></div>
              <div><div class="label">DESIGNATION</div><div class="input" style="margin-top:6px;">Director</div></div>
              <div><div class="label">AADHAAR (masked)</div><div class="input" style="margin-top:6px;">XXXX-XXXX-4521</div></div>
              <div><div class="label">MOBILE</div><div class="input" style="margin-top:6px;">+91 98xxx x2144</div></div>
            </div>
            <div style="margin-top:14px;"><button class="btn primary">Send eSign link</button></div>
          </div>"""))

    screens.append(kyc_shell(6, "KYC · Facility draft", """
          <div class="card" style="padding:20px;max-width:720px;">
            <div class="h3">Primary facility (draft)</div>
            <div class="meta">You can refine geometry after approval · required for PENDING_REVIEW</div>
            <div class="label" style="margin-top:14px;">FACILITY NAME</div>
            <div class="input" style="margin-top:6px;">Indiranagar Metro MLCP</div>
            <div class="label" style="margin-top:12px;">CITY</div>
            <div class="input" style="margin-top:6px;">Bengaluru</div>
            <div class="grid-2" style="margin-top:12px;">
              <div class="class-tile on">T0 Manual</div><div class="class-tile">T1 Gate</div>
            </div>
            <div style="margin-top:14px;"><button class="btn primary">Continue</button></div>
          </div>"""))

    screens.append(kyc_shell(7, "KYC · Submit", """
          <div class="card" style="padding:20px;max-width:720px;">
            <div class="h3">Submit for review</div>
            <div class="list-item row-between"><span>Business + GSTIN</span><span class="pill ok">Complete</span></div>
            <div class="list-item row-between"><span>Bank penny-drop</span><span class="pill ok">Matched</span></div>
            <div class="list-item row-between"><span>Documents</span><span class="pill ok">4/4</span></div>
            <div class="list-item row-between" style="border:0;"><span>eSign</span><span class="pill ok">Signed</span></div>
            <div class="meta" style="margin-top:12px;">SLA: platform reviews within 2 business days · payouts blocked until APPROVED</div>
            <div style="margin-top:14px;"><button class="btn primary">Submit PENDING_REVIEW</button></div>
          </div>"""))

    screens.append(desk_frame("OPR-02", "Facility editor", "Settings", """
      <div class="grid-2" style="grid-template-columns:1.2fr 1fr;gap:16px;">
        <div class="card" style="height:420px;background:linear-gradient(135deg,#E2E8F0,#F8FAFC);display:grid;place-items:center;color:var(--text-2);font-weight:700;">Geofence polygon · entrance pins</div>
        <div class="card" style="padding:16px;">
          <div class="h3">Facility details</div>
          <div class="label" style="margin-top:12px;">NAME</div><div class="input" style="margin-top:6px;">Indiranagar Metro MLCP</div>
          <div class="label" style="margin-top:12px;">HOURS</div><div class="input" style="margin-top:6px;">24×7</div>
          <div class="label" style="margin-top:12px;">TIER</div><div class="pill navy" style="margin-top:8px;">T1 Connected gate</div>
        </div>
      </div>
    """, '<span class="pill ok">Draft saved</span>'))

    screens.append(desk_frame("OPR-03", "Zones & slots", "Zones", """
      <div class="card" style="padding:16px;">
        <div class="row-between"><div class="h3">Zones</div><span class="pill teal">+ Add zone</span></div>
        <table class="table" style="margin-top:12px;">
          <tr><th>Zone</th><th>Mode</th><th>Capacity</th><th>Classes</th><th></th></tr>
          <tr><td>B1</td><td>NUMBERED</td><td>220 bays</td><td>Car, SUV</td><td>Edit</td></tr>
          <tr><td>B2</td><td>NUMBERED</td><td>240 bays</td><td>Car, EV</td><td>Edit</td></tr>
          <tr><td>Surface</td><td>AGGREGATED</td><td>180</td><td>2W, Auto</td><td>Edit</td></tr>
          <tr><td>Terrace</td><td>AGGREGATED</td><td>210</td><td>Car</td><td>Edit</td></tr>
        </table>
      </div>
    """))

    screens.append(desk_frame("OPR-05", "Rate card editor", "Tariffs", """
      <div class="grid-2" style="gap:16px;">
        <div class="card" style="padding:16px;">
          <div class="h3">Car · weekday</div>
          <div class="row-between list-item"><span>Base block (2h)</span><strong>₹100</strong></div>
          <div class="row-between list-item"><span>Increment / hr</span><strong>₹40</strong></div>
          <div class="row-between list-item"><span>Evening peak 17–21</span><strong>1.2×</strong></div>
          <div class="row-between list-item"><span>Overstay multiplier</span><strong>1.5×</strong></div>
          <div class="row-between" style="padding-top:10px;"><span>Walk-in tariff</span><strong>₹50 first hour</strong></div>
        </div>
        <div class="card" style="padding:16px;">
          <div class="h3">Preview calculator</div>
          <div class="meta" style="margin:8px 0;">Car · 2h · 18:00 start</div>
          <div class="h2 currency">₹120.36</div>
          <div class="meta">Matches driver quote breakdown</div>
        </div>
      </div>
    """))

    screens.append(desk_frame("OPR-06", "Float buffer", "Zones", """
      <div class="card" style="padding:16px;max-width:800px;">
        <div class="h3">Float buffer by time band</div>
        <table class="table" style="margin-top:12px;">
          <tr><th>Band</th><th>Measured walk-in</th><th>Configured</th><th></th></tr>
          <tr><td>09–12</td><td>11%</td><td>15%</td><td><span class="pill teal">Apply suggestion</span></td></tr>
          <tr><td>12–17</td><td>18%</td><td>15%</td><td><span class="pill warn">Below measured</span></td></tr>
          <tr><td>17–21</td><td>22%</td><td>20%</td><td><span class="pill ok">OK · floor 5%</span></td></tr>
        </table>
      </div>
    """))

    # reuse compact live board
    screens.append(desk_frame("OPR-14", "Live board", "Live board", """
      <div class="grid-2" style="grid-template-columns:repeat(4,1fr);gap:12px;margin-bottom:16px;">
        <div class="card" style="padding:14px;"><div class="label">OCCUPANCY</div><div class="h2">84.6%</div></div>
        <div class="card" style="padding:14px;"><div class="label">ARRIVALS 30M</div><div class="h2">38</div></div>
        <div class="card" style="padding:14px;"><div class="label">OVERSTAYS</div><div class="h2" style="color:var(--warn);">7</div></div>
        <div class="card" style="padding:14px;"><div class="label">COLLECTIONS</div><div class="h2 currency">₹78,640</div></div>
      </div>
      <div class="card" style="padding:16px;">
        <div class="h3">Occupancy by zone</div>
        <div class="list-item row-between"><span>B1</span><span class="pill danger">98.7%</span></div>
        <div class="list-item row-between"><span>B2</span><span class="pill ok">74%</span></div>
        <div class="list-item row-between" style="border:0;"><span>Terrace</span><span class="pill warn">92.5%</span></div>
      </div>
    """, '<span class="pill ok">Live · Ledger+Loops</span>'))

    screens.append(desk_frame("OPR-15", "Blocks & capacity", "Zones", """
      <div class="card" style="padding:16px;">
        <div class="row-between"><div class="h3">Active blocks</div><span class="pill teal">+ Block bay</span></div>
        <table class="table" style="margin-top:12px;">
          <tr><th>Target</th><th>Window</th><th>Reason</th><th>Actor</th></tr>
          <tr><td>B1-44</td><td>Today 10–18</td><td>Waterlogging</td><td>Manager</td></tr>
          <tr><td>Terrace · 20 units</td><td>Sat–Sun</td><td>Event hold</td><td>Owner</td></tr>
        </table>
        <div class="meta" style="margin-top:10px;">Reason mandatory · written to audit_log</div>
      </div>
    """))

    screens.append(desk_frame("OPR-09", "Staff & devices", "Staff", """
      <div class="card" style="padding:16px;">
        <table class="table">
          <tr><th>Name</th><th>Role</th><th>Facility</th><th>Shift</th><th>Device</th></tr>
          <tr><td>Ramesh Kumar</td><td>Attendant</td><td>Gate 2</td><td>Open</td><td>POS-04</td></tr>
          <tr><td>Sunil Sharma</td><td>Attendant</td><td>Gate 4</td><td>Scheduled</td><td>POS-07</td></tr>
          <tr><td>Ananya Rao</td><td>Manager</td><td>All</td><td>—</td><td>—</td></tr>
        </table>
      </div>
    """))

    screens.append(desk_frame("OPR-10", "Bookings desk", "Bookings", """
      <div class="card" style="padding:16px;">
        <div class="input" style="margin-bottom:12px;max-width:360px;">Search plate / booking code</div>
        <table class="table">
          <tr><th>Code</th><th>Plate</th><th>Bay</th><th>Status</th><th>Window</th></tr>
          <tr><td>#SP-99214</td><td>KA 01 MJ 8821</td><td>B2-19</td><td><span class="pill ok">CHECKED IN</span></td><td>18–20</td></tr>
          <tr><td>#SP-99255</td><td>KA 03 AB 1199</td><td>A-12</td><td><span class="pill info">CONFIRMED</span></td><td>19–21</td></tr>
          <tr><td>#SP-99102</td><td>DL 01 CA 7788</td><td>—</td><td><span class="pill stale">NO SHOW</span></td><td>12–14</td></tr>
        </table>
      </div>
    """))

    screens.append(desk_frame("OPR-10D", "Booking detail", "Bookings", """
      <div class="grid-2" style="gap:16px;">
        <div class="card" style="padding:16px;">
          <div class="row-between"><div class="h3">#SP-99214</div><span class="pill ok">CHECKED_IN</span></div>
          <div class="meta" style="margin-top:6px;">KA 01 MJ 8821 · Car · Bay B2-19</div>
          <div class="list-item row-between" style="margin-top:12px;"><span>Window</span><strong>18:00–20:00 IST</strong></div>
          <div class="list-item row-between"><span>Product</span><strong>Reservation</strong></div>
          <div class="list-item row-between"><span>Paid</span><strong class="currency">₹141.60</strong></div>
          <div class="list-item row-between" style="border:0;"><span>Credential</span><strong>Ed25519 · nonce used</strong></div>
        </div>
        <div class="card" style="padding:16px;">
          <div class="h3">Timeline</div>
          <div class="list-item"><strong>18:01</strong> · HELD → CONFIRMED</div>
          <div class="list-item"><strong>18:04</strong> · Entry · POS-04</div>
          <div class="list-item" style="border:0;"><strong>—</strong> · Exit pending</div>
          <div style="display:flex;gap:8px;margin-top:14px;flex-wrap:wrap;">
            <span class="pill teal">Force complete</span><span class="pill">Refund</span><span class="pill warn">Open dispute</span>
          </div>
        </div>
      </div>
    """))

    screens.append(desk_frame("OPR-20", "Pass pools", "Tariffs", """
      <div class="card" style="padding:16px;">
        <div class="row-between"><div class="h3">Monthly pass pools</div><span class="pill teal">+ New pool</span></div>
        <table class="table" style="margin-top:12px;">
          <tr><th>Pool</th><th>Facility</th><th>Quota</th><th>Sold</th><th>Price</th><th>Valid</th></tr>
          <tr><td>Metro Commuter</td><td>Indiranagar</td><td>80</td><td>62</td><td>₹4,999</td><td>Nov 2026</td></tr>
          <tr><td>Office Day</td><td>Cyber City</td><td>40</td><td>40</td><td>₹6,500</td><td><span class="pill warn">Sold out</span></td></tr>
          <tr><td>2W Express</td><td>Surface</td><td>120</td><td>88</td><td>₹999</td><td>Nov 2026</td></tr>
        </table>
        <div class="meta" style="margin-top:10px;">Quota reserves capacity · oversell blocked · pass QR uses same Ed25519 path</div>
      </div>
    """))

    screens.append(desk_frame("OPR-17", "Reports", "Reports", """
      <div class="grid-2" style="grid-template-columns:repeat(3,1fr);gap:12px;margin-bottom:16px;">
        <div class="card" style="padding:14px;"><div class="label">GROSS TODAY</div><div class="h2 currency">₹78,640</div></div>
        <div class="card" style="padding:14px;"><div class="label">UPI / CASH</div><div class="h2">82% / 18%</div></div>
        <div class="card" style="padding:14px;"><div class="label">NO-SHOWS</div><div class="h2">6</div></div>
      </div>
      <div class="card" style="padding:16px;">
        <div class="row-between"><div class="h3">Exports</div>
          <div style="display:flex;gap:8px;"><span class="pill teal">CSV</span><span class="pill">GSTR-1 helper</span></div>
        </div>
        <div class="meta" style="margin-top:8px;">Operator is supplier of parking · platform TCS context in footnotes</div>
      </div>
    """))

    screens.append(desk_frame("OPR-18", "Payouts", "Payouts", """
      <div class="card" style="padding:16px;">
        <table class="table">
          <tr><th>Batch</th><th>Gross</th><th>Fees</th><th>TCS</th><th>TDS</th><th>Net</th><th>UTR</th></tr>
          <tr><td>23 Oct</td><td>₹2,40,000</td><td>₹12,000</td><td>₹2,160</td><td>₹216</td><td>₹2,25,624</td><td>HDFC…8891</td></tr>
          <tr><td>22 Oct</td><td>₹1,98,400</td><td>₹9,920</td><td>₹1,786</td><td>₹179</td><td>₹1,86,515</td><td>HDFC…7742</td></tr>
        </table>
      </div>
    """))

    screens.append(desk_frame("OPR-19", "Disputes inbox", "Disputes", """
      <div class="card" style="padding:16px;">
        <div class="list-item row-between"><div><strong>#D-204 · Overcharge</strong><div class="meta">SLA 1d 4h left</div></div><span class="pill warn">Respond</span></div>
        <div class="list-item row-between"><div><strong>#D-198 · SLA breach</strong><div class="meta">Evidence uploaded</div></div><span class="pill info">In review</span></div>
        <div class="list-item row-between" style="border:0;"><div><strong>#D-190 · No-show contested</strong><div class="meta">Closed</div></div><span class="pill ok">Resolved</span></div>
      </div>
    """))

    screens.append(desk_frame("OPR-21", "Tier commissioning", "Settings", """
      <div class="card" style="padding:16px;max-width:720px;">
        <div class="h3">Request Tier 2 · ANPR</div>
        <div class="list-item row-between"><span>Edge gateway paired</span><span class="pill ok">Done</span></div>
        <div class="list-item row-between"><span>Loop A/B calibrated</span><span class="pill ok">Done</span></div>
        <div class="list-item row-between"><span>ANPR cameras · RTSP</span><span class="pill warn">Pending</span></div>
        <div class="list-item row-between" style="border:0;"><span>Test cycle results</span><span class="pill stale">Not run</span></div>
        <div style="margin-top:14px;">{btn("Submit commissioning request")}</div>
      </div>
    """))

    return '<div class="row">' + "".join(screens) + "</div>"


def admin_nav(active):
    items = ["Operations","KYC queue","Facility review","Bookings","Support","Finance","Fraud","Audit","Edge fleet","DPDP"]
    return "".join(f'<a class="{"on" if i==active else ""}" href="#">{i}</a>' for i in items)

def admin_frame(sid, title, active, body, dark=False):
    bg = "#0B1220" if dark else "var(--canvas)"
    nav_bg = "#020617" if dark else "var(--navy)"
    return desk(sid, title, f"""
    <div class="desk-shell" style="background:{bg};">
      <aside class="desk-nav" style="background:{nav_bg};"><div class="logo">Park<span style="color:#5EEAD4;">Spot</span></div>{admin_nav(active)}</aside>
      <section class="desk-main" style="background:{bg};">
        <header class="desk-top" style="background:{"#020617" if dark else "#fff"};border-color:{"#1E293B" if dark else "var(--border)"};">
          <div class="h3" style="color:{"#fff" if dark else "var(--navy)"};">{title}</div>
        </header>
        <div class="desk-body">{body}</div>
      </section>
    </div>""")


def admin_screens():
    screens = []

    screens.append(admin_frame("ADM-01", "Operations command", "Operations", """
      <div class="grid-2" style="grid-template-columns:repeat(4,1fr);gap:12px;margin-bottom:16px;">
        <div class="card" style="padding:14px;background:#0F172A;border-color:#1E293B;"><div class="label" style="color:#64748B;">OCCUPANCY</div><div class="h2" style="color:#fff;">87.4%</div></div>
        <div class="card" style="padding:14px;background:#0F172A;border-color:#1E293B;"><div class="label" style="color:#64748B;">GMV</div><div class="h2 currency" style="color:#fff;">₹14.8L</div></div>
        <div class="card" style="padding:14px;background:#0F172A;border-color:#1E293B;"><div class="label" style="color:#64748B;">ONLINE</div><div class="h2" style="color:#fff;">148/152</div></div>
        <div class="card" style="padding:14px;background:#0F172A;border-color:#1E293B;"><div class="label" style="color:#64748B;">VERIFY P95</div><div class="h2" style="color:#5EEAD4;">186ms</div></div>
      </div>
      <div class="grid-2" style="gap:16px;">
        <div class="card" style="height:360px;background:#07111f;border-color:#1E293B;display:grid;place-items:center;color:#64748B;font-weight:700;">PostGIS density map</div>
        <div class="card" style="padding:14px;background:#0F172A;border-color:#1E293B;">
          <div class="h3" style="color:#fff;">Watchdog</div>
          <div style="margin-top:12px;padding:12px;border:1px solid #1E293B;border-radius:12px;"><span class="pill danger">ANPR mismatch</span><div class="meta" style="margin-top:8px;color:#CBD5E1;">DL 01 AB 1234 dual gate</div></div>
          <div style="margin-top:10px;padding:12px;border:1px solid #1E293B;border-radius:12px;"><span class="pill warn">Override spike</span><div class="meta" style="margin-top:8px;color:#CBD5E1;">Gate 3 · 6 lifts / 15m</div></div>
        </div>
      </div>
    """, dark=True))

    screens.append(admin_frame("ADM-02", "KYC queue", "KYC queue", """
      <div class="card" style="padding:16px;">
        <table class="table">
          <tr><th>Org</th><th>PAN</th><th>Penny-drop</th><th>Docs</th><th>SLA</th><th></th></tr>
          <tr><td>Nexus Parking Pvt</td><td>AABCN…</td><td><span class="pill ok">Match</span></td><td>4/4</td><td>1d left</td><td><span class="pill teal">Review</span></td></tr>
          <tr><td>Urban Lots LLP</td><td>AABCU…</td><td><span class="pill warn">Name mismatch</span></td><td>3/4</td><td>6h</td><td><span class="pill teal">Review</span></td></tr>
        </table>
      </div>
    """))

    screens.append(admin_frame("ADM-03", "Facility review", "Facility review", """
      <div class="grid-2" style="gap:16px;">
        <div class="card" style="height:380px;background:var(--muted);display:grid;place-items:center;font-weight:700;color:var(--text-2);">Geometry audit map</div>
        <div class="card" style="padding:16px;">
          <div class="h3">Listing quality</div>
          <div class="h2" style="margin:8px 0;">82 / 100</div>
          <div class="list-item row-between"><span>Photos</span><span class="pill ok">OK</span></div>
          <div class="list-item row-between"><span>Entrance pins</span><span class="pill ok">OK</span></div>
          <div class="list-item row-between"><span>Rate card</span><span class="pill warn">Missing night band</span></div>
          <div style="display:grid;grid-template-columns:1fr 1fr;gap:10px;margin-top:16px;">
            {btn("Suspend", "secondary")}{btn("Publish")}
          </div>
        </div>
      </div>
    """.replace("{btn(\"Suspend\", \"secondary\")}", '<button class="btn secondary xl">Suspend</button>').replace("{btn(\"Publish\")}", '<button class="btn primary xl">Publish</button>')))

    screens.append(admin_frame("ADM-04", "Booking timeline", "Bookings", """
      <div class="card" style="padding:16px;max-width:800px;">
        <div class="h3">#SP-99214 timeline</div>
        <div class="list-item"><strong>18:01</strong> · Quote accepted · HELD</div>
        <div class="list-item"><strong>18:02</strong> · Payment captured · CONFIRMED · Ed25519 issued</div>
        <div class="list-item"><strong>18:04</strong> · Gate entry · ATT POS-04 · CHECKED_IN</div>
        <div class="list-item"><strong>19:58</strong> · Exit scan · dues ₹0 · COMPLETED</div>
        <div class="list-item" style="border:0;"><strong>19:58</strong> · Invoice + ledger lines queued</div>
      </div>
    """))

    screens.append(admin_frame("ADM-05", "Support / disputes", "Support", """
      <div class="card" style="padding:16px;">
        <div class="list-item row-between"><div><strong>Case #C-881 · Overcharge</strong><div class="meta">Driver · refund limit ₹500</div></div><span class="pill warn">Open</span></div>
        <div class="list-item row-between"><div><strong>Dispute #D-204</strong><div class="meta">Evidence: loop events + gate photo</div></div><span class="pill info">Awaiting ops</span></div>
        <div class="list-item row-between" style="border:0;"><div><strong>Case #C-870</strong><div class="meta">Macro: payment pending webhook</div></div><span class="pill ok">Resolved</span></div>
      </div>
    """))

    screens.append(admin_frame("ADM-05D", "Dispute decision", "Support", """
      <div class="grid-2" style="gap:16px;">
        <div class="card" style="padding:16px;">
          <div class="row-between"><div class="h3">Dispute #D-204</div><span class="pill warn">Overcharge</span></div>
          <div class="meta" style="margin-top:6px;">#SP-99188 · Driver claims peak misapplied</div>
          <div class="list-item row-between" style="margin-top:12px;"><span>Charged</span><strong class="currency">₹188.80</strong></div>
          <div class="list-item row-between"><span>Quoted (driver)</span><strong class="currency">₹141.60</strong></div>
          <div class="list-item row-between" style="border:0;"><span>Delta</span><strong style="color:var(--danger);">₹47.20</strong></div>
          <div class="h3" style="margin-top:16px;font-size:14px;">Evidence</div>
          <div class="meta">Rate card snapshot · entry 17:58 · exit 19:42 · CGST/SGST lines</div>
        </div>
        <div class="card" style="padding:16px;">
          <div class="h3">Decision</div>
          <div class="grid-2" style="margin-top:12px;">
            <div class="class-tile on">Full refund</div><div class="class-tile">Partial ₹47.20</div>
            <div class="class-tile">Reject</div><div class="class-tile">Credit note</div>
          </div>
          <div class="label" style="margin-top:14px;">RATIONALE (audit)</div>
          <div class="input" style="margin-top:6px;min-height:72px;align-items:flex-start;">Peak band not published for that window · operator fault</div>
          <div style="display:grid;grid-template-columns:1fr 1fr;gap:10px;margin-top:16px;">
            <button class="btn secondary xl">Escalate</button><button class="btn primary xl">Apply decision</button>
          </div>
        </div>
      </div>
    """))

    screens.append(admin_frame("ADM-07", "Feature flags", "Operations", """
      <div class="card" style="padding:16px;">
        <div class="row-between"><div class="h3">Platform flags · P07</div><span class="pill info">Scoped by city / tier</span></div>
        <table class="table" style="margin-top:12px;">
          <tr><th>Flag</th><th>Scope</th><th>State</th><th>Rollout</th></tr>
          <tr><td>floating_session</td><td>Bengaluru</td><td><span class="pill ok">ON</span></td><td>100%</td></tr>
          <tr><td>otm_preauth</td><td>All</td><td><span class="pill warn">Canary</span></td><td>15%</td></tr>
          <tr><td>sos_reroute</td><td>Metro cities</td><td><span class="pill ok">ON</span></td><td>100%</td></tr>
          <tr><td>anpr_auto_exit</td><td>T2+</td><td><span class="pill stale">OFF</span></td><td>0%</td></tr>
          <tr><td>corporate_billing</td><td>Pilot orgs</td><td><span class="pill warn">Canary</span></td><td>5%</td></tr>
        </table>
        <div class="meta" style="margin-top:10px;">Changes require dual approval · written to audit_log with request_id</div>
      </div>
    """))

    screens.append(admin_frame("ADM-08", "Finance / tax", "Finance", """
      <div class="grid-2" style="grid-template-columns:repeat(3,1fr);gap:12px;margin-bottom:16px;">
        <div class="card" style="padding:14px;"><div class="label">PAYOUT QUEUE</div><div class="h2">₹18.2L</div></div>
        <div class="card" style="padding:14px;"><div class="label">TCS MTD</div><div class="h2">₹42,180</div></div>
        <div class="card" style="padding:14px;"><div class="label">TDS MTD</div><div class="h2">₹8,436</div></div>
      </div>
      <div class="card" style="padding:16px;">
        <div class="row-between"><div class="h3">Payout batch 24 Oct</div><span class="pill warn">Needs dual approval</span></div>
        <div class="meta" style="margin-top:8px;">Approver A signed · waiting Approver B</div>
        <div style="display:flex;gap:8px;margin-top:12px;"><span class="pill teal">GSTR-8 export</span><span class="pill">Form 26Q</span><span class="pill">16A certificates</span></div>
      </div>
    """))

    screens.append(admin_frame("ADM-10", "Reconciliation", "Finance", """
      <div class="card" style="padding:16px;">
        <div class="h3">PSP settlement vs ledger</div>
        <table class="table" style="margin-top:12px;">
          <tr><th>Date</th><th>PSP</th><th>Ledger</th><th>Δ</th><th>Status</th></tr>
          <tr><td>23 Oct</td><td>₹14,82,450</td><td>₹14,82,450</td><td>₹0</td><td><span class="pill ok">Matched</span></td></tr>
          <tr><td>22 Oct</td><td>₹13,10,200</td><td>₹13,09,880</td><td>₹320</td><td><span class="pill warn">Exception</span></td></tr>
        </table>
      </div>
    """))

    screens.append(admin_frame("ADM-06", "Fraud watchlist", "Fraud", """
      <div class="card" style="padding:16px;">
        <div class="list-item row-between"><div><strong>SOS abuse</strong><div class="meta">3 accounts &gt; 2 SOS / 30d</div></div><span class="pill danger">Review</span></div>
        <div class="list-item row-between"><div><strong>Duplicate plates</strong><div class="meta">KA 01 MJ 8821 dual active</div></div><span class="pill warn">Flagged</span></div>
        <div class="list-item row-between" style="border:0;"><div><strong>Webhook anomalies</strong><div class="meta">Signature fail spike</div></div><span class="pill info">Watching</span></div>
      </div>
    """))

    screens.append(admin_frame("ADM-11", "Audit log", "Audit", """
      <div class="card" style="padding:16px;">
        <table class="table">
          <tr><th>Time</th><th>Actor</th><th>Action</th><th>Resource</th><th>Request ID</th></tr>
          <tr><td>14:48</td><td>admin@ps</td><td>KYC_APPROVE</td><td>org_8821</td><td>req_9f2a</td></tr>
          <tr><td>14:22</td><td>mgr_ananya</td><td>BLOCK_BAY</td><td>B1-44</td><td>req_8c11</td></tr>
          <tr><td>13:01</td><td>att_b409</td><td>OVERRIDE</td><td>gate_3</td><td>req_7710</td></tr>
        </table>
      </div>
    """))

    screens.append(admin_frame("ADM-12", "DPDP rights desk", "DPDP", """
      <div class="card" style="padding:16px;">
        <div class="list-item row-between"><div><strong>Access request</strong><div class="meta">user_441 · due in 62 days</div></div><span class="pill info">In progress</span></div>
        <div class="list-item row-between"><div><strong>Erasure request</strong><div class="meta">user_902 · retention check</div></div><span class="pill warn">Legal hold?</span></div>
        <div class="list-item row-between" style="border:0;"><div><strong>Correction</strong><div class="meta">Plate typo · completed</div></div><span class="pill ok">Done</span></div>
      </div>
    """))

    screens.append(admin_frame("ADM-13", "Edge fleet", "Edge fleet", """
      <div class="card" style="padding:16px;">
        <table class="table">
          <tr><th>Device</th><th>Facility</th><th>Heartbeat</th><th>Firmware</th><th>Status</th></tr>
          <tr><td>gw-ind-01</td><td>Indiranagar</td><td>8s</td><td>1.4.2</td><td><span class="pill ok">Healthy</span></td></tr>
          <tr><td>gw-cbr-03</td><td>Cyber City</td><td>2m</td><td>1.4.1</td><td><span class="pill warn">Degraded</span></td></tr>
          <tr><td>cam-l2-a</td><td>Indiranagar</td><td>12s</td><td>—</td><td><span class="pill ok">RTSP OK</span></td></tr>
        </table>
      </div>
    """))

    return '<div class="row">' + "".join(screens) + "</div>"


def main():
    driver = wrap_page(
        "Driver app · complete flow",
        "Production-ready driver: splash → OTP → consent/permissions → garage → explore → book/pay → pass/session → SOS/refunds → profile settings, legal, notifications, payments, help, wallet.",
        driver_screens(),
    )
    attendant = wrap_page(
        "Attendant POS · complete flow",
        "Full shift: login → float → scan → entry/reject → plate lookup → override → walk-in/capacity → exit/UPI → handover → offline → close → incident → lane.",
        attendant_screens(),
    )
    operator = wrap_page(
        "Operator SaaS · complete flow",
        "Full KYC 7-step + facility, zones, tariffs, float, live board, blocks, staff, bookings/detail, pass pools, reports, payouts, disputes, tier commissioning.",
        operator_screens(),
    )
    admin = wrap_page(
        "Platform admin · complete flow",
        "Command center, KYC, facility review, booking timeline, support, dispute decision, feature flags, finance/tax, reconciliation, fraud, audit, DPDP, edge fleet.",
        admin_screens(),
    )

    from generate_driver_pro import build_driver_page
    build_driver_page()
    (OUT / "flow-attendant.html").write_text(attendant, encoding="utf-8")
    (OUT / "flow-operator.html").write_text(operator, encoding="utf-8")
    (OUT / "flow-admin.html").write_text(admin, encoding="utf-8")

    # Keep handcrafted premium index.html (do not overwrite)
    print("Generated: flow-driver, flow-attendant, flow-operator, flow-admin")


if __name__ == "__main__":
    main()
