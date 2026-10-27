#!/usr/bin/env python3
"""
Adds the 15 uncreated/unseen screens to generate_stitch_suite.py and recompiles stitch-screens/index.html.
Expands the suite from 30 screens to 45 screens across 14 lifecycle stages.
"""

from pathlib import Path
import re

GEN_FILE = Path("/Users/maheshgiri/Documents/Projects/Parking/docs/figma-mockups/stitch-screens/generate_stitch_suite.py")
content = GEN_FILE.read_text(encoding="utf-8")

# 1. Add extra CSS styles for Ticker, Battery, VMS, and Thermal Ticket
extra_css = """
    /* Additional Styles for Unseen Screens */
    .meter-ticker {
      font-family: 'Share Tech Mono', 'JetBrains Mono', monospace;
      font-size: 36px;
      font-weight: 700;
      color: #00685F;
      letter-spacing: 2px;
      text-shadow: 0 0 16px rgba(0,104,95,0.25);
    }
    .battery-circle {
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
    }
    .vms-board {
      background: #050505;
      border: 4px solid #1E293B;
      border-radius: 14px;
      padding: 14px 12px;
      font-family: 'Share Tech Mono', monospace;
      color: #22C55E;
      box-shadow: inset 0 0 20px rgba(0,0,0,0.9), 0 10px 25px rgba(0,0,0,0.7);
      position: relative;
      overflow: hidden;
    }
    .vms-amber { color: #F59E0B; text-shadow: 0 0 8px rgba(245,158,11,0.6); }
    .vms-green { color: #10B981; text-shadow: 0 0 8px rgba(16,185,129,0.6); }
    .vms-cyan  { color: #06B6D4; text-shadow: 0 0 8px rgba(6,182,212,0.6); }
    .vms-red   { color: #EF4444; text-shadow: 0 0 8px rgba(239,68,68,0.6); }

    .thermal-ticket {
      background: #FFFEF9;
      color: #1E293B;
      font-family: 'JetBrains Mono', 'Courier New', monospace;
      border: 1px dashed #CBD5E1;
      border-radius: 6px;
      padding: 18px 14px;
      box-shadow: 0 8px 20px -4px rgba(0,0,0,0.12);
      position: relative;
    }
"""

# Insert extra CSS before `/* Studio Wall Grid & Device Scaling */`
if "/* Additional Styles for Unseen Screens */" not in content:
    content = content.replace("    /* Studio Wall Grid & Device Scaling */", extra_css + "\n    /* Studio Wall Grid & Device Scaling */")

# 2. Add the 15 screens after STITCH-30
new_screens_code = '''
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
'''

# 3. Insert new screens before `# Build Stage Filter Pills`
target_marker = "    # Build Stage Filter Pills"
if 'add_screen("STITCH-31"' not in content:
    content = content.replace(target_marker, new_screens_code + "\n" + target_marker)

# 4. Update stages list to 14 stages
old_stages = '''    stages = [
        ("All", "All Screens (30)"),
        ("1", "1. Launch & Onboard (4)"),
        ("2", "2. Auth Suite (8)"),
        ("3", "3. Flagship 5-Tabs (5)"),
        ("4", "4. Vehicle & Garage (2)"),
        ("5", "5. Map & Search HUD (2)"),
        ("6", "6. Facility & B2 Deck (2)"),
        ("7", "7. Quote ₹76.70 & UPI (2)"),
        ("8", "8. Ingress & Active Dwell (3)"),
        ("9", "9. Tax Invoice & SOS (2)"),
    ]'''

new_stages = '''    stages = [
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
    ]'''

content = content.replace(old_stages, new_stages)

# 5. Update header subtitle badge
content = content.replace("Complete 30-Screen Flow", "Complete 45-Screen Master Flow")
content = content.replace("B2 Bay &amp; Quote ₹76.70</p>", "B2 Bay &amp; Quote ₹76.70 → Floating Meter, EV 60kW, Overstay &amp; Physical VMS</p>")

GEN_FILE.write_text(content, encoding="utf-8")
print("Successfully updated generate_stitch_suite.py with 15 unseen screens!")
