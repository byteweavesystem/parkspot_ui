#!/usr/bin/env python3
"""Five Dribbble-Grade Driver Iterations — Award-Winning Mobile UI Mockups.

Inspired by top Dribbble mobility, navigation, and fintech designs.
Strictly conforms to ParkSpot_Master_Specification_v3.0.md and docs/design.md.
"""
from pathlib import Path
import json

OUT = Path(__file__).parent
A = "../assets"

# Inline SVG icons for Dribbble-level fidelity
def ico(name, color="currentColor", size=16):
    icons = {
        "search": f'<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="{color}" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg>',
        "pin": f'<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="{color}" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg>',
        "shield": f'<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="{color}" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><polyline points="9 12 11 14 15 10"/></svg>',
        "bolt": f'<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="{color}" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"/></svg>',
        "car": f'<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="{color}" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="11" width="18" height="8" rx="2"/><path d="M5 11l2-5h10l2 5"/><circle cx="7.5" cy="15.5" r="1.5"/><circle cx="16.5" cy="15.5" r="1.5"/></svg>',
        "check": f'<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="{color}" stroke-width="2.8" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"/></svg>',
        "clock": f'<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="{color}" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>',
        "arrow_right": f'<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="{color}" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/></svg>',
        "chevron_right": f'<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="{color}" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><polyline points="9 18 15 12 9 6"/></svg>',
        "filter": f'<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="{color}" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><polygon points="22 3 2 3 10 12.46 10 19 14 21 14 12.46 22 3"/></svg>',
        "sparkle": f'<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="{color}" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2v4M12 18v4M4.93 4.93l2.83 2.83M16.24 16.24l2.83 2.83M2 12h4M18 12h4M4.93 19.07l2.83-2.83M16.24 7.76l2.83-2.83"/></svg>',
        "star": f'<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="{color}" stroke="{color}" stroke-width="1"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg>',
        "lock": f'<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="{color}" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/></svg>',
        "navigation": f'<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="{color}" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><polygon points="3 11 22 2 13 21 11 13 3 11"/></svg>',
        "qr": f'<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="{color}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="7" height="7"/><rect x="14" y="3" width="7" height="7"/><rect x="14" y="14" width="7" height="7"/><rect x="3" y="14" width="7" height="7"/></svg>',
    }
    return icons.get(name, "")

# Base Dribbble Studio CSS (single braces)
BASE = """
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:var(--fb);background:#070B14;color:var(--text);-webkit-font-smoothing:antialiased}
.page{padding:48px 32px 90px;max-width:1820px;margin:0 auto}
.page-head{margin-bottom:36px;color:#E2E8F0}
.page-head .id{color:#5EEAD4;font-size:12px;font-weight:800;letter-spacing:.16em;text-transform:uppercase}
.page-head h1{font-family:var(--fd);font-size:40px;font-weight:800;letter-spacing:-.03em;margin:8px 0 12px;color:#fff}
.page-head p{color:#94A3B8;max-width:780px;line-height:1.6;font-size:16px}
.page-head .layout-note{margin-top:16px;padding:14px 18px;border-radius:14px;background:#0F172A;border:1px solid #1E293B;color:#CBD5E1;font-size:13.5px;line-height:1.55}
.page-head a{color:#5EEAD4;font-weight:700;text-decoration:none;display:inline-flex;align-items:center;gap:6px;margin-top:16px;font-size:14px}
.page-head a:hover{text-decoration:underline}
.rail{display:flex;gap:40px;overflow-x:auto;padding:12px 10px 52px;align-items:flex-start;scroll-snap-type:x mandatory}
.shot{flex:0 0 auto;width:390px;scroll-snap-align:start}
.shot .label{color:#94A3B8;font-size:11.5px;font-weight:800;letter-spacing:.1em;text-transform:uppercase;margin-bottom:14px;display:flex;align-items:center;gap:8px}
.shot .label span{color:#5EEAD4;font-family:var(--fm);background:rgba(94,234,212,.12);padding:2px 8px;border-radius:6px}

/* iPhone 16 Pro Premium Dribbble Frame */
.phone{width:390px;height:844px;border-radius:52px;overflow:hidden;position:relative;background:var(--canvas);box-shadow:0 0 0 11px #1E2433,0 0 0 13px #2D374D,0 45px 110px rgba(0,0,0,.8);isolation:isolate}
.glass-reflection{position:absolute;top:0;left:0;right:0;height:240px;background:linear-gradient(135deg,rgba(255,255,255,.07) 0%,transparent 65%);pointer-events:none;z-index:70}
.island{position:absolute;top:11px;left:50%;transform:translateX(-50%);height:35px;border-radius:24px;z-index:60;background:#000;display:flex;align-items:center;justify-content:space-between;padding:0 12px;color:#fff;font-size:11px;font-weight:700;box-shadow:inset 0 0 0 1px rgba(255,255,255,.12);pointer-events:none}
.island.compact{width:124px}
.island.live{width:230px;padding:0 14px;background:#070C16;border:1px solid rgba(20,184,166,.4);box-shadow:0 4px 16px rgba(13,148,136,.25)}
.island .dot{width:7px;height:7px;border-radius:50%;background:#14B8A6;box-shadow:0 0 8px #14B8A6;animation:dotPulse 1.8s infinite}
@keyframes dotPulse{0%,100%{opacity:1;transform:scale(1)}50%{opacity:.4;transform:scale(.8)}}
.phone-body{position:absolute;inset:0;display:flex;flex-direction:column;overflow:hidden;z-index:1}
.home-bar{position:absolute;bottom:8px;left:50%;transform:translateX(-50%);width:138px;height:5px;border-radius:99px;background:var(--text);opacity:.25;z-index:50;pointer-events:none}
.status{height:54px;display:flex;align-items:flex-end;justify-content:space-between;padding:0 26px 10px;font-size:13px;font-weight:700;z-index:30;flex-shrink:0}
.status .icons{display:flex;align-items:center;gap:6px}
.screen{flex:1;display:flex;flex-direction:column;position:relative;min-height:0;overflow:hidden}
.tabular{font-variant-numeric:tabular-nums;letter-spacing:-.01em}
"""

def status_bar(color="#fff"):
    return f"""<div class="status" style="color:{color}">
      <span class="tabular">9:41</span>
      <div class="icons">
        <svg width="15" height="11" viewBox="0 0 16 12" fill="currentColor"><rect x="0" y="8" width="2.5" height="4" rx="0.5"/><rect x="4" y="5.5" width="2.5" height="6.5" rx="0.5"/><rect x="8" y="3" width="2.5" height="9" rx="0.5"/><rect x="12" y="0" width="2.5" height="12" rx="0.5"/></svg>
        <svg width="14" height="11" viewBox="0 0 16 12" fill="currentColor"><path d="M8 2.5C10.5 2.5 12.8 3.5 14.5 5.2L15.9 3.8C13.8 1.7 11 0.5 8 0.5C5 0.5 2.2 1.7 0.1 3.8L1.5 5.2C3.2 3.5 5.5 2.5 8 2.5ZM8 6.5C9.7 6.5 11.2 7.2 12.3 8.3L13.7 6.9C12.2 5.4 10.2 4.5 8 4.5C5.8 4.5 3.8 5.4 2.3 6.9L3.7 8.3C4.8 7.2 6.3 6.5 8 6.5ZM8 10.5C8.8 10.5 9.5 11.2 9.5 12H6.5C6.5 11.2 7.2 10.5 8 10.5Z"/></svg>
        <svg width="22" height="11" viewBox="0 0 24 12" fill="none" stroke="currentColor" stroke-width="1.5"><rect x="1" y="1" width="19" height="10" rx="3"/><rect x="2.5" y="2.5" width="13" height="7" rx="1.5" fill="currentColor"/><path d="M21 4.5V7.5" stroke-linecap="round"/></svg>
      </div>
    </div>"""

def phone_frame(inner, island_html='<div class="island compact"><span>9:41</span></div>'):
    return f'<div class="phone"><div class="glass-reflection"></div>{island_html}<div class="phone-body">{inner}</div><div class="home-bar"></div></div>'

def page(meta, css, shots_html):
    return f"""<!DOCTYPE html>
<html lang="en"><head>
<meta charset="UTF-8"/><meta name="viewport" content="width=device-width, initial-scale=1"/>
<title>Iteration {meta['id']} · {meta['name']} — ParkSpot Driver</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?{meta['fonts']}&display=swap" rel="stylesheet"/>
<style>
:root{{{meta['root']}}}
{BASE}
{css}
</style></head><body>
<div class="page">
  <div class="page-head">
    <div class="id">Iteration {meta['id']} · {meta['slug']}</div>
    <h1>{meta['name']}</h1>
    <p><strong style="color:#F8FAFC">{meta['tagline']}</strong><br/>{meta['thesis']}</p>
    <div class="layout-note"><strong style="color:#5EEAD4">Dribbble UX Architecture:</strong> {meta['layout']}</div>
    <a href="index.html">← Compare All 5 Dribbble Iterations</a>
  </div>
  <div class="rail">{shots_html}</div>
</div>
</body></html>"""

# ═════════════════════════════════════════════════════════════════
# ITERATION A — NEO-MOBILITY COCKPIT: Apple Maps / Uber Reserve
# ═════════════════════════════════════════════════════════════════
def build_A():
    meta = {
        "id": "A", "slug": "neo-mobility-cockpit", "name": "Neo-Mobility Cockpit",
        "tagline": "Dribbble Trending #1 · Apple Glassmorphism · Dynamic Island · PassKit Ticket",
        "thesis": "Ultra-polished Apple & Uber Reserve aesthetic: frosted glass pill headers, interactive Dynamic Island live activity, glowing vehicle spotlight, and an authentic perforated boarding pass.",
        "layout": "Dynamic Island live widget · floating frosted search & filter HUD · 3D vehicle stage · multi-snap capacity card · perforated boarding pass with Ed25519 seal",
        "fonts": "family=Plus+Jakarta+Sans:wght@500;600;700;800&family=JetBrains+Mono:wght@600;700",
        "root": "--fd:'Plus Jakarta Sans',sans-serif;--fb:'Plus Jakarta Sans',sans-serif;--fm:'JetBrains Mono',monospace;--canvas:#F8FAFC;--text:#0F172A;--text-sec:#475569;--teal:#0D9488;--teal-bright:#14B8A6;--teal-deep:#0F766E;--teal-glow:rgba(20,184,166,.25);--surface:#FFFFFF;--border:#E2E8F0;--card-shadow:0 12px 32px -4px rgba(15,23,42,.08),0 4px 12px -2px rgba(15,23,42,.04);",
    }
    css = """
.a-bg-dusk{flex:1;background:radial-gradient(circle at 50% 25%, #182848 0%, #080E18 100%);color:#fff;display:flex;flex-direction:column;position:relative;padding:0 24px}
.a-ambient-glow{position:absolute;top:30%;left:50%;transform:translate(-50%,-50%);width:280px;height:280px;background:radial-gradient(circle,rgba(20,184,166,.35) 0%,transparent 70%);border-radius:50%;filter:blur(30px);pointer-events:none}
.a-btn-glow{width:100%;height:54px;border-radius:18px;background:linear-gradient(135deg,#14B8A6,#0D9488);color:#fff;border:0;font-weight:800;font-size:16px;font-family:var(--fb);display:flex;align-items:center;justify-content:center;gap:10px;box-shadow:0 10px 28px rgba(13,148,136,.4);cursor:pointer;transition:transform .2s ease}
.a-btn-glow:active{transform:scale(.98)}
.a-btn-ghost{width:100%;height:50px;border-radius:18px;background:rgba(255,255,255,.07);backdrop-filter:blur(10px);color:#fff;border:1px solid rgba(255,255,255,.14);font-weight:700;font-size:15px;font-family:var(--fb);margin-top:10px}

/* Vehicle Stage */
.a-car-stage{position:relative;height:180px;border-radius:20px;overflow:hidden;margin-bottom:18px;background:radial-gradient(circle at 50% 70%, #1E293B 0%, #0F172A 100%);box-shadow:var(--card-shadow);display:flex;align-items:center;justify-content:center}
.a-car-stage img{width:90%;height:auto;object-fit:contain;filter:drop-shadow(0 14px 20px rgba(0,0,0,.6))}
.a-car-tag{position:absolute;top:12px;left:14px;background:rgba(15,23,42,.8);backdrop-filter:blur(8px);color:#5EEAD4;font-size:11px;font-weight:800;padding:4px 10px;border-radius:8px;border:1px solid rgba(94,234,212,.3)}

/* HSRP Plate */
.a-hsrp-badge{background:linear-gradient(145deg,#FFFFFF,#F1F5F9);border:2.5px solid #0F172A;border-radius:12px;padding:12px 14px;display:flex;align-items:center;gap:12px;box-shadow:0 6px 18px rgba(0,0,0,.08);margin-bottom:16px}
.a-hsrp-ind{background:#0F172A;color:#fff;padding:6px 8px;border-radius:6px;display:flex;flex-direction:column;align-items:center;font-size:9px;font-weight:900}
.a-hsrp-num{font-family:var(--fm);font-size:22px;font-weight:800;letter-spacing:.14em;color:#0F172A;flex:1}

/* Glass Card */
.a-card{background:var(--surface);border:1px solid var(--border);border-radius:20px;padding:16px 18px;margin-bottom:12px;box-shadow:var(--card-shadow)}
.a-tag{display:inline-flex;align-items:center;gap:4px;padding:4px 9px;border-radius:8px;font-size:11px;font-weight:750}
.a-tag-mint{background:#CCFBF1;color:#0F766E}
.a-tag-amber{background:#FEF3C7;color:#92400E}

/* PassKit Ticket */
.a-pass-card{background:#fff;border-radius:26px;overflow:hidden;box-shadow:0 24px 60px rgba(15,23,42,.25);position:relative}
.a-pass-header{background:linear-gradient(135deg,#0F766E,#0D9488,#14B8A6);color:#fff;padding:16px 20px}
.a-pass-cut{height:26px;position:relative;background:#fff;display:flex;align-items:center}
.a-pass-cut::before,.a-pass-cut::after{content:'';position:absolute;width:24px;height:24px;border-radius:50%;background:#F8FAFC;top:1px}
.a-pass-cut::before{left:-12px}
.a-pass-cut::after{right:-12px}
.a-pass-dash{width:100%;height:1px;border-top:2px dashed #CBD5E1}
"""
    shots = []
    # 01 Ambient Splash
    shots.append(("01 · Splash Cockpit", phone_frame(f"""
      <div class="a-bg-dusk">
        {status_bar("#fff")}
        <div class="a-ambient-glow"></div>
        <div style="margin-top:auto;margin-bottom:52px;position:relative;z-index:2">
          <div style="display:inline-flex;align-items:center;gap:6px;padding:6px 14px;border-radius:99px;background:rgba(20,184,166,.18);border:1px solid rgba(20,184,166,.4);color:#5EEAD4;font-size:12px;font-weight:800;letter-spacing:.08em;margin-bottom:16px">
            {ico('sparkle','#5EEAD4',14)} CERTAINTY GUARANTEED
          </div>
          <h1 style="font-size:38px;font-weight:800;letter-spacing:-.03em;line-height:1.1;margin-bottom:12px">ParkSpot<span style="color:#2DD4BF">.</span></h1>
          <p style="color:#94A3B8;font-size:15px;line-height:1.55;margin-bottom:30px">Guaranteed empty bay on arrival. Exact itemized quote before payment. 2-second FastGate clearance.</p>
          <button class="a-btn-glow">Unlock with Face ID {ico('arrow_right','#fff',18)}</button>
          <button class="a-btn-ghost">Sign in with mobile number</button>
        </div>
      </div>
    """, '<div class="island compact"><span>9:41</span></div>')))

    # 02 Vehicle Passport
    shots.append(("02 · Vehicle Passport", phone_frame(f"""
      <div style="flex:1;background:var(--canvas);display:flex;flex-direction:column">
        {status_bar("#0F172A")}
        <div style="padding:12px 20px 8px;display:flex;justify-content:space-between;align-items:center">
          <div>
            <div style="font-size:11px;font-weight:800;color:var(--teal);letter-spacing:.08em;text-transform:uppercase">GARAGE · STEP 1/2</div>
            <h2 style="font-size:22px;font-weight:800">Vehicle Passport</h2>
          </div>
          <span class="a-tag a-tag-mint">{ico('shield','currentColor',12)} VAHAN Verified</span>
        </div>
        <div style="flex:1;padding:8px 20px 24px;overflow-y:auto">
          <div class="a-car-stage">
            <span class="a-car-tag">Electric SUV</span>
            <img src="{A}/car-detail.jpg"/>
          </div>

          <div class="a-hsrp-badge">
            <div class="a-hsrp-ind"><span>IND</span><span style="font-size:6px">KA</span></div>
            <div class="a-hsrp-num">KA 01 MJ 8821</div>
            <span class="a-tag a-tag-mint">{ico('check','currentColor',12)} Active</span>
          </div>

          <div class="a-card">
            <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:8px">
              <span style="font-size:12px;font-weight:800;color:var(--text-sec);text-transform:uppercase">FACILITY CLEARANCE CHECK</span>
              <span style="font-size:12px;font-weight:800;color:var(--teal)">100% Match</span>
            </div>
            <div style="display:flex;gap:16px;font-size:13px">
              <div><span style="color:#64748B;font-size:11px;display:block">VEHICLE HEIGHT</span><b>1.82m</b> (Max 2.1m)</div>
              <div><span style="color:#64748B;font-size:11px;display:block">FASTAG RFID</span><b>ICICI Linked</b></div>
            </div>
          </div>

          <button class="a-btn-glow" style="margin-top:16px">Confirm &amp; Explore Bays {ico('arrow_right','#fff',18)}</button>
        </div>
      </div>
    """, '<div class="island live"><span class="dot"></span><span>KA 01 MJ 8821 · Synced</span></div>')))

    # 03 Explore Map & Floating Bottom Sheet
    shots.append(("03 · Map Explore", phone_frame(f"""
      <div style="flex:1;position:relative;background:#E2E8F0">
        <img src="{A}/parkspot-map-base.jpg" style="position:absolute;inset:0;width:100%;height:100%;object-fit:cover"/>
        <div style="position:absolute;inset:0;background:linear-gradient(180deg,rgba(11,19,43,.4) 0%,transparent 30%)"></div>
        {status_bar("#fff")}

        <!-- Floating Frosted Search HUD -->
        <div style="position:absolute;top:62px;left:16px;right:16px;display:flex;gap:8px;z-index:20">
          <div style="flex:1;height:46px;background:rgba(255,255,255,.9);backdrop-filter:blur(16px);border-radius:14px;padding:0 14px;display:flex;align-items:center;gap:10px;box-shadow:var(--card-shadow);border:1px solid rgba(255,255,255,.6)">
            {ico('search','#0F172A',18)}
            <input readonly value="Indiranagar 100 Feet Rd" style="border:0;background:transparent;font-family:var(--fb);font-weight:700;font-size:14px;color:#0F172A;flex:1"/>
          </div>
          <div style="width:46px;height:46px;background:rgba(15,23,42,.85);backdrop-filter:blur(16px);border-radius:14px;display:grid;place-items:center;color:#5EEAD4;box-shadow:var(--card-shadow)">
            {ico('filter','#5EEAD4',18)}
          </div>
        </div>

        <!-- 3D Map Pin -->
        <div style="position:absolute;top:44%;left:50%;transform:translate(-50%,-100%);z-index:10">
          <div style="background:#0F172A;color:#fff;padding:8px 12px;border-radius:12px;box-shadow:0 12px 28px rgba(0,0,0,.35);border:2px solid #14B8A6;display:flex;align-items:center;gap:8px">
            {ico('bolt','#5EEAD4',16)}
            <div>
              <div style="font-size:13px;font-weight:800" class="tabular">₹30<span style="font-size:10px;font-weight:600;color:#94A3B8">/hr</span></div>
              <div style="font-size:10px;color:#5EEAD4;font-weight:700">12 bays free</div>
            </div>
          </div>
        </div>

        <!-- Docked Multi-Snap Bottom Sheet -->
        <div style="position:absolute;left:0;right:0;bottom:0;background:#fff;border-radius:28px 28px 0 0;padding:14px 20px 28px;box-shadow:0 -10px 40px rgba(15,23,42,.15);z-index:30">
          <div style="width:40px;height:4px;border-radius:99px;background:#CBD5E1;margin:0 auto 14px"></div>
          <div style="display:flex;gap:14px;align-items:center;margin-bottom:12px">
            <img src="{A}/parkspot-facility-hero.jpg" style="width:68px;height:68px;border-radius:14px;object-fit:cover"/>
            <div style="flex:1">
              <div style="display:flex;gap:6px;align-items:center;margin-bottom:2px">
                <span class="a-tag a-tag-mint">{ico('clock','currentColor',11)} Live 2m</span>
                <span style="font-size:11px;font-weight:750;color:#64748B">T1 Boom Barrier</span>
              </div>
              <h3 style="font-size:17px;font-weight:800">Indiranagar Metro MLCP</h3>
              <div style="font-size:12px;color:#64748B;margin-top:2px">0.4 km · 3 min walk · Height 2.1m</div>
            </div>
          </div>
          <div style="display:flex;justify-content:space-between;align-items:center;background:#F8FAFC;border:1px solid #E2E8F0;border-radius:14px;padding:10px 14px;margin-bottom:14px">
            <div>
              <span style="font-size:10px;font-weight:800;color:#64748B;letter-spacing:.05em">LIVE OCCUPANCY</span>
              <div style="font-size:13px;font-weight:800;color:#0F172A">84% Capacity (12 Free)</div>
            </div>
            <b style="font-size:20px;font-weight:800;color:#0F766E" class="tabular">₹30<span style="font-size:12px;color:#64748B">/hr</span></b>
          </div>
          <button class="a-btn-glow">Reserve Bay · View Deck {ico('arrow_right','#fff',18)}</button>
        </div>
      </div>
    """, '<div class="island live"><span class="dot"></span><span>12 Bays Free · 0.4km</span></div>')))

    # 04 Bay Deck Selection
    shots.append(("04 · Bay Deck", phone_frame(f"""
      <div style="flex:1;background:var(--canvas);display:flex;flex-direction:column">
        {status_bar("#0F172A")}
        <div style="padding:10px 20px 8px;display:flex;justify-content:space-between;align-items:center">
          <div>
            <div style="font-size:11px;font-weight:800;color:var(--teal);letter-spacing:.06em">INDIRANAGAR METRO MLCP</div>
            <h2 style="font-size:22px;font-weight:800">Basement Deck B2</h2>
          </div>
          <span class="a-tag a-tag-amber">{ico('clock','currentColor',12)} Hold: 09:52</span>
        </div>
        <div style="flex:1;padding:8px 20px 24px;overflow-y:auto">
          <!-- Level Selector Pills -->
          <div style="display:flex;gap:8px;margin-bottom:14px">
            <div style="flex:1;padding:8px;text-align:center;border-radius:12px;background:#F1F5F9;font-size:12px;font-weight:700;color:#64748B">Level B1 (Full)</div>
            <div style="flex:1;padding:8px;text-align:center;border-radius:12px;background:#0F766E;color:#fff;font-size:12px;font-weight:800;box-shadow:0 4px 12px rgba(15,118,110,.25)">Level B2 (7 Free)</div>
            <div style="flex:1;padding:8px;text-align:center;border-radius:12px;background:#fff;border:1px solid #CBD5E1;font-size:12px;font-weight:700">Level B3 (5 Free)</div>
          </div>

          <!-- Selected Bay Card -->
          <div class="a-card" style="border:2px solid var(--teal);background:linear-gradient(180deg,#F0FDFA,#FFFFFF)">
            <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:8px">
              <span style="font-family:var(--fm);font-size:20px;font-weight:800;color:#0F766E">BAY B2-19</span>
              <span class="a-tag a-tag-mint">{ico('check','currentColor',12)} Reserved For You</span>
            </div>
            <div style="font-size:12.5px;color:#334155;line-height:1.5">Standard Covered Bay · Pillar Protection · 15m to Lift Core 2</div>
          </div>

          <!-- Floor Plan Thumbnail -->
          <div style="border-radius:16px;overflow:hidden;height:120px;position:relative;margin-bottom:14px">
            <img src="{A}/parkspot-garage-b2.jpg" style="width:100%;height:100%;object-fit:cover"/>
            <div style="position:absolute;inset:0;background:linear-gradient(180deg,transparent,rgba(15,23,42,.7))"></div>
            <div style="position:absolute;bottom:10px;left:14px;color:#fff;font-size:12px;font-weight:700">Aisle 2 Entry Ramp Approach</div>
          </div>

          <button class="a-btn-glow">Confirm Slot · Review Quote {ico('arrow_right','#fff',18)}</button>
        </div>
      </div>
    """, '<div class="island live"><span class="dot"></span><span>Bay B2-19 Locked</span></div>')))

    # 05 Transparent Statutory Quote
    shots.append(("05 · Statutory Quote", phone_frame(f"""
      <div style="flex:1;background:var(--canvas);display:flex;flex-direction:column">
        {status_bar("#0F172A")}
        <div style="padding:10px 20px 8px;display:flex;justify-content:space-between;align-items:center">
          <div>
            <div style="font-size:11px;font-weight:800;color:var(--teal);letter-spacing:.06em">INVARIANT TARIFF ENGINE</div>
            <h2 style="font-size:22px;font-weight:800">Payable Quote</h2>
          </div>
          <span style="font-family:var(--fm);font-size:11px;color:#64748B">#INV-9921</span>
        </div>
        <div style="flex:1;padding:8px 20px 24px;overflow-y:auto">
          <div class="a-card">
            <div style="display:flex;justify-content:space-between;padding:8px 0;border-bottom:1px solid #F1F5F9;font-size:13px">
              <span style="color:#64748B">Base Parking (2.0 hrs @ ₹30)</span>
              <b class="tabular">₹60.00</b>
            </div>
            <div style="display:flex;justify-content:space-between;padding:8px 0;border-bottom:1px solid #F1F5F9;font-size:13px">
              <span style="color:#64748B">Platform Convenience Fee</span>
              <b class="tabular">₹5.00</b>
            </div>
            <div style="display:flex;justify-content:space-between;padding:8px 0;border-bottom:1px solid #F1F5F9;font-size:12px;color:#64748B">
              <span>CGST (9.0%)</span>
              <span class="tabular">₹5.85</span>
            </div>
            <div style="display:flex;justify-content:space-between;padding:8px 0;border-bottom:1px solid #F1F5F9;font-size:12px;color:#64748B">
              <span>SGST (9.0%)</span>
              <span class="tabular">₹5.85</span>
            </div>
            <div style="display:flex;justify-content:space-between;padding:14px 0 4px;font-size:16px;font-weight:800;border-top:2px solid #0F172A">
              <span>Total Payable</span>
              <span style="font-size:24px;color:var(--teal-deep)" class="tabular">₹76.70</span>
            </div>
          </div>

          <div style="font-size:12px;font-weight:800;color:#64748B;letter-spacing:.06em;text-transform:uppercase;margin:12px 0 8px">1-Tap Payment</div>
          <div class="a-card" style="display:flex;align-items:center;gap:12px;border-color:var(--teal);background:#F0FDFA;margin-bottom:16px">
            <div style="width:38px;height:38px;border-radius:10px;background:#fff;display:grid;place-items:center;font-weight:800;color:#0F766E">UPI</div>
            <div style="flex:1">
              <div style="font-size:14px;font-weight:750">Google Pay / PhonePe / CRED</div>
              <div style="font-size:11px;color:#64748B">Zero payment failure · Instant barrier sync</div>
            </div>
            <span style="color:var(--teal);font-weight:800">●</span>
          </div>

          <button class="a-btn-glow">Pay ₹76.70 via UPI {ico('arrow_right','#fff',18)}</button>
        </div>
      </div>
    """, '<div class="island live"><span class="dot"></span><span>Total: ₹76.70 · UPI</span></div>')))

    # 06 Perforated PassKit Boarding Pass
    shots.append(("06 · PassKit Ticket", phone_frame(f"""
      <div style="flex:1;background:radial-gradient(circle at 50% 20%, #1E293B 0%, #0F172A 100%);padding:14px 18px 24px;display:flex;flex-direction:column;justify-content:center">
        {status_bar("#fff")}
        <div class="a-pass-card">
          <div class="a-pass-header">
            <div style="display:flex;justify-content:space-between;align-items:center">
              <div>
                <span style="font-size:10px;font-weight:800;letter-spacing:.12em;text-transform:uppercase;opacity:.85">DIGITAL TRANSIT PASS</span>
                <h3 style="font-size:17px;font-weight:800">Indiranagar Metro MLCP</h3>
              </div>
              <span style="font-family:var(--fm);font-size:11px;background:rgba(0,0,0,.25);padding:4px 8px;border-radius:6px">#SP-99214</span>
            </div>
          </div>

          <div style="padding:16px 18px">
            <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:12px">
              <div>
                <span style="font-size:10px;font-weight:800;color:#64748B">ASSIGNED BAY</span>
                <div style="font-size:26px;font-weight:800;color:#0F172A">Bay B2-19</div>
              </div>
              <div style="text-align:right">
                <span style="font-size:10px;font-weight:800;color:#64748B">VEHICLE</span>
                <div style="font-family:var(--fm);font-size:16px;font-weight:800;color:#0F172A">KA 01 MJ 8821</div>
              </div>
            </div>
            <div style="display:flex;justify-content:space-between;background:#F8FAFC;border-radius:10px;padding:8px 12px;font-size:12px">
              <span>Gate 2 Barrier Lane</span>
              <b style="color:#0F766E">18:00 – 20:00 Window</b>
            </div>
          </div>

          <div class="a-pass-cut"><div class="a-pass-dash"></div></div>

          <div style="padding:14px;text-align:center">
            <img src="{A}/qr-pass.png" style="width:144px;height:144px;display:inline-block;border-radius:12px"/>
            <div style="font-family:var(--fm);font-size:10px;color:#64748B;margin-top:6px">ED25519 VERIFIED · SINGLE-USE NONCE</div>
          </div>
        </div>

        <button class="a-btn-glow" style="margin-top:14px;background:#0F172A;border:1px solid rgba(255,255,255,.2)">I'm at Gate 2 Barrier {ico('arrow_right','#fff',18)}</button>
      </div>
    """, '<div class="island live"><span class="dot"></span><span>Gate 2 Ready · B2-19</span></div>')))

    html = "".join(f'<div class="shot"><div class="label"><span>{meta["id"]}</span> {l}</div>{s}</div>' for l, s in shots)
    return meta, page(meta, css, html)

# ═════════════════════════════════════════════════════════════════
# ITERATION B — CYBER-HUD OBSIDIAN: Tesla / Rivian Precision
# ═════════════════════════════════════════════════════════════════
def build_B():
    meta = {
        "id": "B", "slug": "cyber-hud-obsidian", "name": "Cyber-HUD Obsidian",
        "tagline": "Dribbble Dark Mode #1 · Tesla Telemetry · Lower 40% Thumb Zone",
        "thesis": "Ultra-contrast OLED dark mode inspired by Tesla and Rivian. Designed for extreme glare resistance in bright Indian sunlight and rapid 1-thumb operation.",
        "layout": "Lower 40% thumb ergonomics · dark vector radar map · wireframe vehicle telemetry · architectural B2 blueprint grid · high-luminance barrier pass",
        "fonts": "family=Space+Grotesk:wght@500;700;800&family=Share+Tech+Mono",
        "root": "--fd:'Space Grotesk',sans-serif;--fb:'Space Grotesk',sans-serif;--fm:'Share Tech Mono',monospace;--canvas:#05070A;--text:#F0F6FC;--text-sec:#8B949E;--emerald:#10B981;--emerald-glow:rgba(16,185,129,.25);--surface:#0D1117;--border:#1E2633;--cyan:#38BDF8;",
    }
    css = """
.b-wrap{flex:1;background:var(--canvas);color:var(--text);display:flex;flex-direction:column;position:relative}
.b-term-head{padding:12px 20px;border-bottom:1px solid var(--border);display:flex;justify-content:space-between;align-items:center;font-family:var(--fm);font-size:11px;color:var(--emerald)}
.b-body{flex:1;padding:20px;display:flex;flex-direction:column;overflow-y:auto}
.b-card{background:var(--surface);border:1px solid var(--border);border-radius:16px;padding:16px;margin-bottom:14px;box-shadow:0 8px 24px rgba(0,0,0,.6)}
.b-card.active{border-color:var(--emerald);box-shadow:0 0 24px rgba(16,185,129,.2)}
.b-btn{height:54px;border-radius:14px;background:var(--emerald);color:#05070A;border:0;font-weight:800;font-family:var(--fd);font-size:15px;letter-spacing:.04em;display:flex;align-items:center;justify-content:center;gap:10px;text-transform:uppercase;cursor:pointer;box-shadow:0 8px 24px var(--emerald-glow)}
"""
    shots = []
    # 01 Terminal Splash
    shots.append(("01 · Splash HUD", phone_frame(f"""
      <div class="b-wrap">
        {status_bar("#F0F6FC")}
        <div class="b-term-head"><span>SYS // PARKSPOT_V3</span><span>STATUS: OPTIMAL</span></div>
        <div class="b-body" style="justify-content:center">
          <div style="font-family:var(--fm);font-size:11px;letter-spacing:.2em;color:var(--emerald);margin-bottom:8px">HARDWARE CONTROL SYSTEM</div>
          <div style="font-size:42px;font-weight:800;line-height:1.0;margin-bottom:16px">ACCURACY.<br/>CLEARANCE.<br/>ENTRY.</div>
          <div class="b-card active" style="margin:20px 0">
            <div style="font-family:var(--fm);font-size:12px;color:var(--text-sec)">GROUND PROTOCOL VERIFIED</div>
            <div style="font-family:var(--fm);font-size:14px;color:#fff;margin-top:4px">ED25519 · OFFLINE MANIFEST · NO CLOUD WAIT</div>
          </div>
          <button class="b-btn" style="margin-top:auto">INITIALIZE DRIVER CONSOLE >> </button>
        </div>
      </div>
    """)))

    # 02 Vehicle Setup
    shots.append(("02 · Vehicle Spec", phone_frame(f"""
      <div class="b-wrap">
        {status_bar("#F0F6FC")}
        <div class="b-term-head"><span>VEHICLE TELEMETRY</span><span>KA-01-MJ-8821</span></div>
        <div class="b-body">
          <div style="font-size:22px;font-weight:800;margin-bottom:14px">Active Vehicle Unit</div>
          <div class="b-card active">
            <div style="display:flex;justify-content:space-between">
              <span style="font-family:var(--fm);font-size:20px;font-weight:700;color:var(--emerald)">KA 01 MJ 8821</span>
              <span style="font-family:var(--fm);font-size:11px;color:var(--emerald)">[LOCKED]</span>
            </div>
            <div style="display:grid;grid-template-columns:1fr 1fr;gap:10px;margin-top:14px">
              <div style="background:#080B0F;padding:10px;border-radius:10px;border:1px solid #1E2633"><div style="font-size:10px;color:var(--text-sec)">CLASS</div><b style="font-family:var(--fm)">MID SUV</b></div>
              <div style="background:#080B0F;padding:10px;border-radius:10px;border:1px solid #1E2633"><div style="font-size:10px;color:var(--text-sec)">HEIGHT</div><b style="font-family:var(--fm)">1.82M</b></div>
            </div>
          </div>
          <button class="b-btn" style="margin-top:auto">CONFIRM SPEC &amp; RADAR >> </button>
        </div>
      </div>
    """)))

    # 03 Radar Explore
    shots.append(("03 · Radar Explore", phone_frame(f"""
      <div class="b-wrap">
        <div style="flex:1;position:relative">
          <img src="{A}/map-aerial.jpg" style="position:absolute;inset:0;width:100%;height:100%;object-fit:cover;filter:grayscale(1) brightness(.3)"/>
          {status_bar("#fff")}
          <div style="position:absolute;bottom:0;left:0;right:0;padding:16px 20px 32px;background:linear-gradient(180deg,transparent,#05070A 50%)">
            <div class="b-card active" style="margin-bottom:12px">
              <div style="display:flex;justify-content:space-between;align-items:baseline">
                <b style="font-size:17px">Indiranagar Metro MLCP</b>
                <span style="font-family:var(--fm);color:var(--emerald);font-size:14px">₹30/HR</span>
              </div>
              <div style="font-family:var(--fm);font-size:11px;color:var(--text-sec);margin-top:4px">0.4 KM · LIVE LATENCY &lt;12S · T1 BOOM</div>
            </div>
            <button class="b-btn" style="width:100%">ENGAGE TARGET >> </button>
          </div>
        </div>
      </div>
    """)))

    # 04 Bay Blueprint
    shots.append(("04 · Bay Blueprint", phone_frame(f"""
      <div class="b-wrap">
        {status_bar("#F0F6FC")}
        <div class="b-term-head"><span>DECK LEVEL B2</span><span>SLOT ASSIGNMENT</span></div>
        <div class="b-body">
          <div class="b-card active">
            <div style="font-size:11px;font-family:var(--fm);color:var(--emerald)">SLOT RESERVED // HOLD 09:44</div>
            <div style="font-size:28px;font-weight:800;font-family:var(--fm);margin:6px 0">BAY B2-19</div>
            <div style="font-size:12px;color:var(--text-sec)">Direct aisle approach · 2.1m clearance certified</div>
          </div>
          <button class="b-btn" style="margin-top:auto">LOCK BAY &amp; REVIEW QUOTE >> </button>
        </div>
      </div>
    """)))

    # 05 Ledger Quote
    shots.append(("05 · Ledger Quote", phone_frame(f"""
      <div class="b-wrap">
        {status_bar("#F0F6FC")}
        <div class="b-term-head"><span>LEDGER INVOICE</span><span>TAX ACCREDITED</span></div>
        <div class="b-body">
          <div class="b-card">
            <div style="display:flex;justify-content:space-between;font-family:var(--fm);font-size:13px;padding:6px 0"><span>BASE CHARGE (2H)</span><span>₹60.00</span></div>
            <div style="display:flex;justify-content:space-between;font-family:var(--fm);font-size:13px;padding:6px 0"><span>PLATFORM ACCREDITATION</span><span>₹05.00</span></div>
            <div style="display:flex;justify-content:space-between;font-family:var(--fm);font-size:12px;color:var(--text-sec);padding:6px 0"><span>CGST + SGST (18%)</span><span>₹11.70</span></div>
            <div style="display:flex;justify-content:space-between;font-family:var(--fm);font-size:20px;font-weight:800;color:var(--emerald);border-top:1px solid var(--border);padding-top:12px;margin-top:8px">
              <span>NET PAYABLE</span><span>₹76.70</span>
            </div>
          </div>
          <button class="b-btn" style="margin-top:auto">SLIDE TO AUTHORIZE UPI >> </button>
        </div>
      </div>
    """)))

    # 06 Gate HUD
    shots.append(("06 · Gate Scanner", phone_frame(f"""
      <div class="b-wrap" style="background:#000">
        {status_bar("#fff")}
        <div class="b-body" style="align-items:center;justify-content:center;text-align:center">
          <div style="font-family:var(--fm);font-size:12px;color:var(--emerald)">HIGH-LUMINANCE SCANNER MODE</div>
          <div style="font-size:44px;font-weight:800;font-family:var(--fm);color:#fff;margin:8px 0">BAY B2-19</div>
          <div style="background:#fff;border-radius:18px;padding:16px;box-shadow:0 0 50px rgba(255,255,255,.2);margin:16px 0">
            <img src="{A}/qr-pass.png" width="160" height="160"/>
          </div>
          <div style="font-family:var(--fm);font-size:12px;color:#aaa">KA 01 MJ 8821 · ED25519</div>
          <button class="b-btn" style="width:100%;margin-top:24px">MAX LUMINANCE ACTIVE</button>
        </div>
      </div>
    """)))

    html = "".join(f'<div class="shot"><div class="label"><span>{meta["id"]}</span> {l}</div>{s}</div>' for l, s in shots)
    return meta, page(meta, css, html)

# ═════════════════════════════════════════════════════════════════
# ITERATION C — FLUID CORRIDOR STREAM: Linear / Modern Commuter
# ═════════════════════════════════════════════════════════════════
def build_C():
    meta = {
        "id": "C", "slug": "fluid-corridor-stream", "name": "Fluid Corridor Stream",
        "tagline": "Dribbble Trending #2 · Split-Screen Telemetry · Corridor Clusters",
        "thesis": "Modern commuter stream organizing parking by busy urban corridors (100 Feet Rd, Indiranagar Metro) with photo entrance guidance.",
        "layout": "40/60 Split-screen interface · transit corridor groupings · live barrier entry latency · gate approach photo wayfinding pass",
        "fonts": "family=Plus+Jakarta+Sans:wght@500;600;700;800&family=IBM+Plex+Mono:wght@600;700",
        "root": "--fd:'Plus Jakarta Sans',sans-serif;--fb:'Plus Jakarta Sans',sans-serif;--fm:'IBM Plex Mono',monospace;--canvas:#F1F5F9;--text:#0F172A;--text-sec:#64748B;--blue:#2563EB;--surface:#FFFFFF;--border:#E2E8F0;",
    }
    css = """
.c-split{flex:1;display:flex;flex-direction:column;background:var(--canvas)}
.c-btn{height:52px;border-radius:16px;background:var(--blue);color:#fff;border:0;font-weight:750;font-size:15px;font-family:var(--fb);display:flex;align-items:center;justify-content:center;gap:8px;cursor:pointer;box-shadow:0 8px 24px rgba(37,99,235,.25)}
"""
    shots = []
    # 01 Stream Splash
    shots.append(("01 · Stream Splash", phone_frame(f"""
      <div class="c-split">
        <div style="height:320px;position:relative;background:#0F172A">
          <img src="{A}/city-street.jpg" style="position:absolute;inset:0;width:100%;height:100%;object-fit:cover"/>
          <div style="position:absolute;inset:0;background:linear-gradient(180deg,rgba(15,23,42,.6),rgba(15,23,42,.9))"></div>
          {status_bar("#fff")}
          <div style="position:absolute;bottom:24px;left:20px;right:20px;color:#fff">
            <span style="font-size:11px;font-weight:800;color:#93C5FD">URBAN TRANSIT STREAM</span>
            <h1 style="font-size:32px;font-weight:800;line-height:1.15;margin-top:6px">4,820 bays live in Bengaluru.</h1>
          </div>
        </div>
        <div style="flex:1;background:#fff;border-radius:24px 24px 0 0;margin-top:-20px;z-index:10;padding:20px;display:flex;flex-direction:column">
          <p style="color:var(--text-sec);font-size:14px;line-height:1.55;margin-bottom:20px">Zero-wait parking. Real-time sensor accuracy, guaranteed reservations, frictionless gate clearance.</p>
          <button class="c-btn" style="margin-top:auto">Connect Mobile &amp; Vehicle {ico('arrow_right','#fff',16)}</button>
        </div>
      </div>
    """)))

    # 02 Vehicle Locker
    shots.append(("02 · Vehicle Locker", phone_frame(f"""
      <div class="c-split">
        {status_bar("#0F172A")}
        <div style="padding:12px 20px 10px"><h2 style="font-size:22px;font-weight:800">Vehicle Stream Locker</h2></div>
        <div style="flex:1;padding:0 20px 24px;overflow-y:auto">
          <div style="border:1.5px solid var(--blue);border-radius:16px;padding:14px;background:#EFF6FF;display:flex;gap:12px;align-items:center">
            <div style="width:40px;height:40px;border-radius:10px;background:#2563EB;color:#fff;display:grid;place-items:center">{ico('car','#fff',20)}</div>
            <div style="flex:1">
              <div style="font-family:var(--fm);font-size:16px;font-weight:700">KA 01 MJ 8821</div>
              <div style="font-size:12px;color:var(--text-sec)">Mid SUV · ICICI FASTag Linked</div>
            </div>
            <span style="color:var(--blue);font-weight:800">●</span>
          </div>
          <button class="c-btn" style="width:100%;margin-top:auto">Confirm &amp; Find Corridors {ico('arrow_right','#fff',16)}</button>
        </div>
      </div>
    """)))

    # 03 Corridor Explore
    shots.append(("03 · Corridor Explore", phone_frame(f"""
      <div class="c-split">
        <div style="height:240px;position:relative">
          <img src="{A}/parkspot-map-base.jpg" style="position:absolute;inset:0;width:100%;height:100%;object-fit:cover"/>
          <div style="position:absolute;inset:0;background:linear-gradient(180deg,rgba(15,23,42,.6),rgba(15,23,42,.85))"></div>
          {status_bar("#fff")}
          <div style="position:absolute;bottom:14px;left:20px;color:#fff">
            <span style="font-size:11px;font-weight:800;color:#93C5FD">ACTIVE CORRIDOR</span>
            <div style="font-size:18px;font-weight:800">100 Feet Road Metro Link</div>
          </div>
        </div>
        <div style="flex:1;background:#fff;border-radius:24px 24px 0 0;margin-top:-20px;z-index:10;padding:16px 20px 24px;display:flex;flex-direction:column">
          <div style="border:1.5px solid var(--blue);border-radius:14px;padding:12px 14px;background:#EFF6FF;margin-bottom:10px;display:flex;justify-content:space-between;align-items:center">
            <div>
              <div style="font-size:15px;font-weight:750">Indiranagar Metro MLCP</div>
              <div style="font-size:12px;color:var(--text-sec)">0.4 km · 12 free bays · Live 1m</div>
            </div>
            <b style="font-family:var(--fm);color:var(--blue);font-size:16px">₹30/h</b>
          </div>
          <button class="c-btn" style="margin-top:auto">Lock Metro MLCP Bay {ico('arrow_right','#fff',16)}</button>
        </div>
      </div>
    """)))

    # 04 Gate Camera Wayfinding
    shots.append(("04 · Entrance Guidance", phone_frame(f"""
      <div class="c-split">
        <div style="height:220px;position:relative">
          <img src="{A}/parking-sign.jpg" style="position:absolute;inset:0;width:100%;height:100%;object-fit:cover"/>
          <div style="position:absolute;inset:0;background:linear-gradient(180deg,rgba(15,23,42,.5),rgba(15,23,42,.8))"></div>
          {status_bar("#fff")}
          <div style="position:absolute;bottom:12px;left:20px;color:#fff">
            <span style="font-size:10px;font-weight:800;color:#93C5FD">WAYFINDING GUIDE</span>
            <div style="font-size:17px;font-weight:800">Gate 2 Entry Ramp Approach</div>
          </div>
        </div>
        <div style="flex:1;background:#fff;border-radius:24px 24px 0 0;margin-top:-20px;z-index:10;padding:16px 20px 24px;display:flex;flex-direction:column">
          <div style="background:#F8FAFC;border:1px solid var(--border);border-radius:14px;padding:14px;margin-bottom:12px">
            <div style="font-size:11px;font-weight:800;color:var(--blue)">ASSIGNED BAY</div>
            <div style="font-size:24px;font-weight:800;font-family:var(--fm)">Bay B2-19</div>
            <div style="font-size:12px;color:var(--text-sec);margin-top:4px">Gate 2 barrier lane · Take ramp to B2</div>
          </div>
          <button class="c-btn" style="margin-top:auto">View Final Invoice Quote {ico('arrow_right','#fff',16)}</button>
        </div>
      </div>
    """)))

    # 05 Stream Quote
    shots.append(("05 · Stream Quote", phone_frame(f"""
      <div class="c-split">
        {status_bar("#0F172A")}
        <div style="padding:12px 20px 8px"><h2 style="font-size:22px;font-weight:800">Invoice Review</h2></div>
        <div style="flex:1;padding:0 20px 24px;overflow-y:auto">
          <div style="background:#fff;border:1px solid var(--border);border-radius:16px;padding:16px;margin-bottom:16px">
            <div style="display:flex;justify-content:space-between;padding:6px 0;font-size:13px"><span>2-Hour Tariff</span><b>₹60.00</b></div>
            <div style="display:flex;justify-content:space-between;padding:6px 0;font-size:13px"><span>Platform Access</span><b>₹5.00</b></div>
            <div style="display:flex;justify-content:space-between;padding:6px 0;font-size:12px;color:var(--text-sec)"><span>GST (18%)</span><span>₹11.70</span></div>
            <div style="display:flex;justify-content:space-between;padding:12px 0 0;border-top:1.5px solid #0F172A;font-size:18px;font-weight:800"><span>Payable</span><span style="color:var(--blue)">₹76.70</span></div>
          </div>
          <button class="c-btn" style="width:100%;margin-top:auto">Pay &amp; Receive Pass {ico('arrow_right','#fff',16)}</button>
        </div>
      </div>
    """)))

    # 06 Pass
    shots.append(("06 · Wayfinding Pass", phone_frame(f"""
      <div class="c-split">
        {status_bar("#0F172A")}
        <div style="flex:1;padding:20px;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center">
          <span style="font-size:11px;font-weight:800;color:var(--blue)">ACTIVE BARRIER PASS</span>
          <h2 style="font-size:28px;font-weight:800;margin:6px 0">Bay B2-19</h2>
          <div style="margin:16px auto;padding:14px;background:#fff;border:1px solid var(--border);border-radius:20px;box-shadow:0 10px 30px rgba(0,0,0,.08)">
            <img src="{A}/qr-pass.png" width="160" height="160"/>
          </div>
          <div style="font-family:var(--fm);font-size:12px;color:var(--text-sec)">KA 01 MJ 8821 · ED25519</div>
        </div>
      </div>
    """)))

    html = "".join(f'<div class="shot"><div class="label"><span>{meta["id"]}</span> {l}</div>{s}</div>' for l, s in shots)
    return meta, page(meta, css, html)

# ═════════════════════════════════════════════════════════════════
# ITERATION D — EXECUTIVE BESPOKE LUXE: Champagne Gold & Midnight
# ═════════════════════════════════════════════════════════════════
def build_D():
    meta = {
        "id": "D", "slug": "executive-bespoke-luxe", "name": "Executive Bespoke Luxe",
        "tagline": "Dribbble Luxury #1 · Champagne Gold & Obsidian · Curated Dossiers",
        "thesis": "Ultra-luxury mobility concierge (Lexus / Grand Hyatt / Changi Private). Warm champagne gold accents on midnight obsidian with curated dossiers.",
        "layout": "Luxury card spacing · subtle champagne gold borders · curated facility dossiers with high-res photography · gold-embossed digital credential",
        "fonts": "family=Outfit:wght@400;500;600;700;800&family=JetBrains+Mono:wght@600;700",
        "root": "--fd:'Outfit',sans-serif;--fb:'Outfit',sans-serif;--fm:'JetBrains Mono',monospace;--canvas:#080C16;--surface:#0F1626;--text:#F8FAFC;--text-sec:#94A3B8;--gold:#D4AF37;--border:rgba(212,175,55,.25);",
    }
    css = """
.d-wrap{flex:1;background:var(--canvas);color:var(--text);display:flex;flex-direction:column;position:relative}
.d-card{background:var(--surface);border:1px solid var(--border);border-radius:18px;padding:18px;margin-bottom:14px;box-shadow:0 12px 32px rgba(0,0,0,.5)}
.d-btn-gold{height:54px;border-radius:16px;background:linear-gradient(135deg,#D4AF37,#AA820A);color:#080C16;border:0;font-weight:800;font-size:15px;font-family:var(--fb);display:flex;align-items:center;justify-content:center;gap:8px;cursor:pointer;box-shadow:0 8px 24px rgba(212,175,55,.3)}
"""
    shots = []
    # 01 Welcome Dossier
    shots.append(("01 · Welcome Dossier", phone_frame(f"""
      <div class="d-wrap">
        {status_bar("#fff")}
        <div style="flex:1;padding:24px;display:flex;flex-direction:column;justify-content:center">
          <div style="font-size:11px;font-weight:800;color:var(--gold);letter-spacing:.2em;text-transform:uppercase">ParkSpot Private</div>
          <h1 style="font-size:38px;font-weight:800;line-height:1.1;margin:12px 0 16px">Bespoke Urban Arrival.</h1>
          <p style="color:var(--text-sec);font-size:15px;line-height:1.6;margin-bottom:32px">Exclusively guaranteed executive bays, verified clearance, and white-glove security in premier business corridors.</p>
          <button class="d-btn-gold">Experience Concierge Access {ico('arrow_right','#000',16)}</button>
        </div>
      </div>
    """)))

    # 02 Fleet Profile
    shots.append(("02 · Fleet Profile", phone_frame(f"""
      <div class="d-wrap">
        {status_bar("#fff")}
        <div style="padding:14px 20px 8px"><h2 style="font-size:22px;font-weight:800;color:#F3E8CB">Executive Garage</h2></div>
        <div style="flex:1;padding:10px 20px 24px;overflow-y:auto">
          <div class="d-card" style="border-color:rgba(212,175,55,.4)">
            <div style="display:flex;justify-content:space-between;align-items:baseline">
              <span style="font-size:11px;font-weight:700;color:var(--gold)">TIER 1 REGISTERED</span>
              <span style="font-family:var(--fm);font-size:11px;color:var(--text-sec)">#KA01MJ8821</span>
            </div>
            <div style="font-size:20px;font-weight:800;margin:8px 0 4px">Tata Nexon EV Max</div>
            <div style="font-size:12px;color:var(--text-sec)">Extra-wide covered stall preferred · EV Charging capable</div>
          </div>
          <button class="d-btn-gold" style="width:100%;margin-top:auto">View Curated Stalls {ico('arrow_right','#000',16)}</button>
        </div>
      </div>
    """)))

    # 03 Curated Explore
    shots.append(("03 · Curated Explore", phone_frame(f"""
      <div class="d-wrap">
        {status_bar("#fff")}
        <div style="padding:10px 20px"><h2 style="font-size:20px;font-weight:800">Curated Arrival</h2></div>
        <div style="flex:1;padding:0 20px 20px;overflow-y:auto">
          <div class="d-card">
            <div style="height:120px;border-radius:12px;overflow:hidden;margin-bottom:12px">
              <img src="{A}/parkspot-facility-hero.jpg" style="width:100%;height:100%;object-fit:cover"/>
            </div>
            <div style="display:flex;justify-content:space-between;align-items:baseline">
              <b style="font-size:17px">Prestige Metro MLCP</b>
              <span style="font-family:var(--fm);color:var(--gold);font-weight:700">₹40/HR</span>
            </div>
            <div style="font-size:12px;color:var(--text-sec);margin-top:4px">24/7 Security Concierge · 15m to VIP Lobby</div>
          </div>
          <button class="d-btn-gold" style="width:100%;margin-top:auto">Reserve Executive Stall {ico('arrow_right','#000',16)}</button>
        </div>
      </div>
    """)))

    # 04 VIP Stall
    shots.append(("04 · VIP Stall", phone_frame(f"""
      <div class="d-wrap">
        {status_bar("#fff")}
        <div style="padding:14px 20px 8px"><h2 style="font-size:20px;font-weight:800">Executive Stall Locked</h2></div>
        <div style="flex:1;padding:10px 20px 24px;overflow-y:auto">
          <div class="d-card" style="border-color:var(--gold)">
            <span style="font-size:11px;color:var(--gold);font-weight:800">STALL E-08 · LEVEL B1</span>
            <div style="font-size:26px;font-weight:800;margin:6px 0">Wide Bay E-08</div>
            <div style="font-size:12px;color:var(--text-sec);line-height:1.5">2.6m wide stall with protective pillar buffering. Directly adjacent to Concierge Elevator.</div>
          </div>
          <button class="d-btn-gold" style="width:100%;margin-top:auto">Confirm &amp; Pay Statement {ico('arrow_right','#000',16)}</button>
        </div>
      </div>
    """)))

    # 05 Billing Statement
    shots.append(("05 · Billing Statement", phone_frame(f"""
      <div class="d-wrap">
        {status_bar("#fff")}
        <div style="padding:14px 20px 8px"><h2 style="font-size:20px;font-weight:800">Payable Statement</h2></div>
        <div style="flex:1;padding:10px 20px 24px;overflow-y:auto">
          <div class="d-card">
            <div style="display:flex;justify-content:space-between;padding:6px 0;font-size:13px"><span>Executive Bay (2h)</span><b>₹80.00</b></div>
            <div style="display:flex;justify-content:space-between;padding:6px 0;font-size:13px"><span>Concierge Access</span><b>₹10.00</b></div>
            <div style="display:flex;justify-content:space-between;padding:6px 0;font-size:12px;color:var(--text-sec)"><span>GST (18%)</span><span>₹16.20</span></div>
            <div style="display:flex;justify-content:space-between;padding:12px 0 0;border-top:1px solid var(--border);font-size:18px;font-weight:800"><span>Payable</span><span style="color:var(--gold)">₹106.20</span></div>
          </div>
          <button class="d-btn-gold" style="width:100%;margin-top:auto">Authenticate Payment {ico('arrow_right','#000',16)}</button>
        </div>
      </div>
    """)))

    # 06 VIP Pass
    shots.append(("06 · VIP Pass", phone_frame(f"""
      <div class="d-wrap">
        {status_bar("#fff")}
        <div style="flex:1;padding:24px 20px;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center">
          <div class="d-card" style="width:100%;border-color:var(--gold);padding:24px 18px">
            <span style="font-size:11px;font-weight:800;color:var(--gold);letter-spacing:.15em">VIP TRANSIT CREDENTIAL</span>
            <div style="font-size:28px;font-weight:800;margin:6px 0">Stall E-08</div>
            <div style="margin:16px 0"><img src="{A}/qr-pass.png" width="150" height="150" style="background:#fff;padding:8px;border-radius:14px"/></div>
            <div style="font-family:var(--fm);font-size:12px;color:var(--text-sec)">KA 01 MJ 8821 · ED25519</div>
          </div>
          <button class="d-btn-gold" style="width:100%;margin-top:16px">Concierge Intercom</button>
        </div>
      </div>
    """)))

    html = "".join(f'<div class="shot"><div class="label"><span>{meta["id"]}</span> {l}</div>{s}</div>' for l, s in shots)
    return meta, page(meta, css, html)

# ═════════════════════════════════════════════════════════════════
# ITERATION E — HSRP NATIONAL ELITE: Bharat Mobility High-Trust
# ═════════════════════════════════════════════════════════════════
def build_E():
    meta = {
        "id": "E", "slug": "hsrp-national-elite", "name": "HSRP National Elite",
        "tagline": "Dribbble GovTech #1 · Bharat Mobility Standard · VAHAN Verified",
        "thesis": "High-trust institutional design: official VAHAN vehicle registry, regulated municipal parking tariff directory, and high-trust Ed25519 cryptographic tokens with HSRP plate security branding.",
        "layout": "National Mobility top header bar · official registration form layouts · municipal sensor registry · cryptographic permit pass with security hologram branding",
        "fonts": "family=IBM+Plex+Sans:wght@500;600;700;800&family=IBM+Plex+Mono:wght@600;700",
        "root": "--fd:'IBM Plex Sans',sans-serif;--fb:'IBM Plex Sans',sans-serif;--fm:'IBM Plex Mono',monospace;--canvas:#F8FAFC;--navy:#0A192F;--green:#059669;--saffron:#EA580C;--text:#0F172A;--text-sec:#475569;--surface:#FFFFFF;--border:#CBD5E1;",
    }
    css = """
.e-wrap{flex:1;background:var(--canvas);color:var(--text);display:flex;flex-direction:column}
.e-gov-bar{background:var(--navy);color:#fff;padding:8px 20px;font-size:11px;font-weight:700;display:flex;justify-content:space-between;letter-spacing:.05em}
.e-card{background:#fff;border:1px solid var(--border);border-radius:14px;padding:16px;margin-bottom:12px;box-shadow:0 4px 16px rgba(0,0,0,.04)}
.e-btn{height:52px;border-radius:12px;background:var(--navy);color:#fff;border:0;font-weight:750;font-size:15px;font-family:var(--fb);display:flex;align-items:center;justify-content:center;gap:8px;cursor:pointer}
"""
    shots = []
    # 01 National Gateway Splash
    shots.append(("01 · Bharat Gateway", phone_frame(f"""
      <div class="e-wrap">
        <div class="e-gov-bar"><span>BHARAT MOBILITY // REGISTRY</span><span>GOVT ACCREDITED</span></div>
        {status_bar("#0F172A")}
        <div style="flex:1;padding:24px 20px;display:flex;flex-direction:column;justify-content:center">
          <div style="font-size:11px;font-weight:800;color:var(--green);letter-spacing:.08em;text-transform:uppercase">ParkSpot National Network</div>
          <h1 style="font-size:32px;font-weight:800;line-height:1.2;margin:10px 0 14px">Unified Parking Interface</h1>
          <p style="color:var(--text-sec);font-size:14px;line-height:1.55;margin-bottom:28px">Official digital parking marketplace connecting municipal MLCPs and commercial plazas across India.</p>
          <button class="e-btn">Authenticate with Aadhaar / Mobile {ico('arrow_right','#fff',16)}</button>
        </div>
      </div>
    """)))

    # 02 VAHAN Verification
    shots.append(("02 · VAHAN Registry", phone_frame(f"""
      <div class="e-wrap">
        <div class="e-gov-bar"><span>VAHAN 4.0 INTEGRATION</span><span>VERIFIED</span></div>
        {status_bar("#0F172A")}
        <div style="padding:12px 20px 8px"><h2 style="font-size:20px;font-weight:800">Vehicle Verification</h2></div>
        <div style="flex:1;padding:10px 20px 24px;overflow-y:auto">
          <div class="e-card">
            <div style="display:flex;justify-content:space-between;border-bottom:1px solid #E2E8F0;padding-bottom:8px">
              <span style="font-family:var(--fm);font-size:16px;font-weight:700">KA 01 MJ 8821</span>
              <span style="color:var(--green);font-size:11px;font-weight:700">✓ VAHAN VALID</span>
            </div>
            <div style="font-size:12px;color:var(--text-sec);margin-top:8px">Petrol SUV · Fitness Active · FASTag Bank: SBI</div>
          </div>
          <button class="e-btn" style="width:100%;margin-top:auto">Confirm &amp; Proceed {ico('arrow_right','#fff',16)}</button>
        </div>
      </div>
    """)))

    # 03 Municipal Directory
    shots.append(("03 · Municipal Explore", phone_frame(f"""
      <div class="e-wrap">
        <div class="e-gov-bar"><span>MUNICIPAL DIRECTORY</span><span>BLR EAST</span></div>
        {status_bar("#0F172A")}
        <div style="padding:12px 20px 8px"><h2 style="font-size:20px;font-weight:800">Regulated Lots</h2></div>
        <div style="flex:1;padding:10px 20px 24px;overflow-y:auto">
          <div class="e-card">
            <div style="display:flex;justify-content:space-between">
              <b>BBMP Metro MLCP</b>
              <span style="font-family:var(--fm);color:var(--green);font-weight:700">₹30/hr</span>
            </div>
            <div style="font-size:12px;color:var(--text-sec);margin-top:4px">Reg ID: BLR-PKG-082 · 12 live sensors verified</div>
          </div>
          <button class="e-btn" style="width:100%;margin-top:auto">Select Municipal Lot {ico('arrow_right','#fff',16)}</button>
        </div>
      </div>
    """)))

    # 04 Certified Bay
    shots.append(("04 · Certified Bay", phone_frame(f"""
      <div class="e-wrap">
        <div class="e-gov-bar"><span>SLOT ALLOCATION</span><span>HOLD 10M</span></div>
        {status_bar("#0F172A")}
        <div style="padding:12px 20px 8px"><h2 style="font-size:20px;font-weight:800">Certified Bay</h2></div>
        <div style="flex:1;padding:10px 20px 24px;overflow-y:auto">
          <div class="e-card">
            <div style="font-family:var(--fm);font-size:22px;font-weight:700">BAY B2-19</div>
            <div style="font-size:12px;color:var(--text-sec);margin-top:4px">Municipal structural clearance certified · 2.1m height</div>
          </div>
          <button class="e-btn" style="width:100%;margin-top:auto">Proceed to GST Invoice {ico('arrow_right','#fff',16)}</button>
        </div>
      </div>
    """)))

    # 05 Statutory GST Quote
    shots.append(("05 · Statutory Quote", phone_frame(f"""
      <div class="e-wrap">
        <div class="e-gov-bar"><span>TAX COMPLIANCE</span><span>SAC 996729</span></div>
        {status_bar("#0F172A")}
        <div style="padding:12px 20px 8px"><h2 style="font-size:20px;font-weight:800">Statutory Invoice</h2></div>
        <div style="flex:1;padding:10px 20px 24px;overflow-y:auto">
          <div class="e-card">
            <div style="display:flex;justify-content:space-between;padding:4px 0;font-size:13px"><span>Base (2h)</span><b>₹60.00</b></div>
            <div style="display:flex;justify-content:space-between;padding:4px 0;font-size:13px"><span>Service Fee</span><b>₹5.00</b></div>
            <div style="display:flex;justify-content:space-between;padding:4px 0;font-size:12px;color:var(--text-sec)"><span>CGST (9%)</span><span>₹5.85</span></div>
            <div style="display:flex;justify-content:space-between;padding:4px 0;font-size:12px;color:var(--text-sec)"><span>SGST (9%)</span><span>₹5.85</span></div>
            <div style="display:flex;justify-content:space-between;padding:10px 0 0;border-top:1px solid #E2E8F0;font-size:17px;font-weight:800"><span>Total</span><span>₹76.70</span></div>
          </div>
          <button class="e-btn" style="width:100%;margin-top:auto">Pay via NPCI UPI {ico('arrow_right','#fff',16)}</button>
        </div>
      </div>
    """)))

    # 06 Cryptographic Pass
    shots.append(("06 · Cryptographic Pass", phone_frame(f"""
      <div class="e-wrap">
        <div class="e-gov-bar"><span>DIGITAL TRANSIT PERMIT</span><span>OFFLINE ED25519</span></div>
        {status_bar("#0F172A")}
        <div style="flex:1;padding:20px;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center">
          <div class="e-card" style="width:100%">
            <span style="font-size:10px;font-weight:800;color:var(--green);letter-spacing:.1em">BHARAT MOBILITY VERIFIED</span>
            <div style="font-size:24px;font-weight:800;margin:6px 0">Bay B2-19</div>
            <div style="margin:14px 0"><img src="{A}/qr-pass.png" width="150" height="150"/></div>
            <div style="font-family:var(--fm);font-size:11px;color:var(--text-sec)">KA 01 MJ 8821 · NONCE #SP-99214</div>
          </div>
          <button class="e-btn" style="width:100%;margin-top:16px">Present at Barrier Scanner</button>
        </div>
      </div>
    """)))

    html = "".join(f'<div class="shot"><div class="label"><span>{meta["id"]}</span> {l}</div>{s}</div>' for l, s in shots)
    return meta, page(meta, css, html)

# ═════════════════════════════════════════════════════════════════
# Comparison Board Index
# ═════════════════════════════════════════════════════════════════
def build_board(items):
    cards = []
    for meta, _ in items:
        cards.append(f"""
        <a class="card" href="iteration-{meta['slug']}.html">
          <div class="id">ITERATION {meta['id']} · {meta['slug'].upper()}</div>
          <div class="name">{meta['name']}</div>
          <div class="tag">{meta['tagline']}</div>
          <p>{meta['layout']}</p>
          <div class="cta">Explore Full 6-Screen Architecture →</div>
        </a>""")
    return f"""<!DOCTYPE html>
<html lang="en"><head>
<meta charset="UTF-8"/><meta name="viewport" content="width=device-width, initial-scale=1"/>
<title>ParkSpot Driver — 5 Dribbble-Grade UI Mockups</title>
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@600;700;800&display=swap" rel="stylesheet"/>
<style>
*{{box-sizing:border-box;margin:0;padding:0}}
body{{font-family:'Plus Jakarta Sans',system-ui,sans-serif;background:#070B14;color:#E2E8F0}}
.wrap{{max-width:1200px;margin:0 auto;padding:56px 24px 100px}}
.eyebrow{{color:#5EEAD4;font-size:12px;font-weight:800;letter-spacing:.16em}}
h1{{font-size:44px;letter-spacing:-.03em;margin:10px 0 12px;font-weight:800;color:#fff}}
.sub{{color:#94A3B8;max-width:760px;line-height:1.6;font-size:16px;margin-bottom:28px}}
.note{{padding:16px 20px;border:1px solid #1E293B;border-radius:16px;background:#0F172A;color:#94A3B8;font-size:14px;margin-bottom:32px;line-height:1.55}}
.note strong{{color:#5EEAD4}}
.grid{{display:grid;grid-template-columns:1fr;gap:20px}}
a.card{{display:block;padding:24px 28px;border:1px solid #1E293B;border-radius:22px;background:linear-gradient(180deg,#0F172A,#0A101D);text-decoration:none;color:inherit;transition:all .2s ease}}
a.card:hover{{border-color:#5EEAD4;transform:translateY(-2px);box-shadow:0 16px 40px rgba(13,148,136,.18)}}
.id{{color:#5EEAD4;font-size:11px;font-weight:800;letter-spacing:.14em}}
.name{{font-size:28px;font-weight:800;margin:6px 0;color:#fff}}
.tag{{color:#CBD5E1;font-size:14px;font-weight:600;margin-bottom:10px}}
.card p{{color:#94A3B8;font-size:13.5px;line-height:1.5}}
.cta{{margin-top:16px;font-weight:750;font-size:13.5px;color:#5EEAD4;display:flex;align-items:center;gap:6px}}
</style></head><body>
<div class="wrap">
  <div class="eyebrow">DRIBBLE-GRADE MOCKUPS · ROUND 5</div>
  <h1>ParkSpot Driver: High-Fidelity UI Screens</h1>
  <p class="sub">Five distinct, world-class mobile app designs modeled after top-trending Dribbble mobility and smart parking shots. Real 390×844 iPhone 16 Pro viewports across all 6 core stages (Splash → Vehicle Passport → Explore → Bay Deck → Itemized Quote → Gate Pass).</p>
  <div class="note"><strong>Interactive Comparison Gallery:</strong> Click any direction to inspect the full horizontal device rail. Reply with your preferred letter (<strong>A, B, C, D, or E</strong>) to lock the direction for production rollout.</div>
  <div class="grid">{''.join(cards)}</div>
</div>
</body></html>"""

def main():
    builders = [build_A, build_B, build_C, build_D, build_E]
    items = []
    for b in builders:
        meta, html = b()
        path = OUT / f"iteration-{meta['slug']}.html"
        path.write_text(html, encoding="utf-8")
        print("Wrote", path.name, "—", meta["tagline"])
        items.append((meta, html))
    
    # Also write legacy aliases so existing links remain valid
    legacy_map = {
        "iteration-hsrp-official.html": items[0][1],
        "iteration-gate-black.html": items[1][1],
        "iteration-thermal-receipt.html": items[2][1],
        "iteration-sodium-basement.html": items[3][1],
        "iteration-midday-stone.html": items[4][1],
        "iteration-transit-cockpit.html": items[0][1],
        "iteration-minimalist-hud.html": items[1][1],
        "iteration-operational-stream.html": items[2][1],
        "iteration-executive-concierge.html": items[3][1],
    }
    for fname, content in legacy_map.items():
        (OUT / fname).write_text(content, encoding="utf-8")

    (OUT / "index.html").write_text(build_board(items), encoding="utf-8")
    print("Wrote index.html and all aliases successfully.")
    try:
        g = Path.home() / ".gstack/projects/Projects/designs/driver-iterations-20261024"
        g.mkdir(parents=True, exist_ok=True)
        (g / "iterations.json").write_text(json.dumps({
            "round": 5,
            "note": "Dribbble-grade UI Mockups",
            "items": [{"id": m["id"], "slug": m["slug"], "name": m["name"], "layout": m["layout"]} for m, _ in items],
        }, indent=2), encoding="utf-8")
    except OSError as e:
        print("skip gstack mirror:", e)

if __name__ == "__main__":
    main()
