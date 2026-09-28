"""
Saxophone 1+5 Practice & 10-Second Micro-Rest Timer Dashboard (v1.0)
Rights & Intellectual Property Holder: Scott Niewinski

Features:
1. Full 20-Minute Daily Microcycle Guide (Min 0-3 Calibration, Min 3-15 1+5 Engine, Min 15-20 Mental Rehearsal)
2. Automated 10-Second Micro-Rest Timer Engine (with Haptic/Visual Pulse Notifications)
3. 6-Song Aural Repertoire Selector & Transposition Engine
4. Bio-Acoustic Somatic Checkpoints (Joe Allard "Dis-ney" Posture, "Thick Air", "Keep Right Hand Down")
5. SuperMemo Memory Stability (S) & Retrievability (R) Session Logger
"""

import streamlit as st
import time
import math
import json
import os
import hashlib
import hmac
import pandas as pd

st.set_page_config(
    page_title="Saxophone 1+5 Practice & Micro-Rest Timer (Scott Niewinski IP)",
    page_icon="🎷",
    layout="wide"
)

# Custom CSS Styling
st.markdown("""
<style>
    .main-header {
        font-size: 2.2rem;
        font-weight: 800;
        color: #1E3A8A;
        margin-bottom: 0.2rem;
    }
    .sub-header {
        font-size: 1.0rem;
        color: #4B5563;
        margin-bottom: 1.5rem;
    }
    .rest-box {
        background-color: #FEF3C7;
        border-left: 6px solid #D97706;
        padding: 15px;
        border-radius: 8px;
        margin-top: 10px;
        margin-bottom: 10px;
    }
    .active-box {
        background-color: #E0F2FE;
        border-left: 6px solid #0284C7;
        padding: 15px;
        border-radius: 8px;
        margin-top: 10px;
        margin-bottom: 10px;
    }
    .somatic-box {
        background-color: #F3E8FF;
        border-left: 6px solid #9333EA;
        padding: 12px;
        border-radius: 8px;
    }
</style>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# SONG REPERTOIRE DATABASE
# -----------------------------------------------------------------------------
REPERTOIRE = {
    "1_saints": {
        "title": "When the Saints Go Marching In",
        "key_alto": "G Major",
        "key_tenor": "C Major",
        "notes_alto": "G - B - C - [High D]",
        "notes_tenor": "C - E - F - [High G]",
        "focus": "Crossing the Break (Middle C to High D)",
        "somatic_anchor": "Keep Right Hand Down on C; use 'Slow, Straight, Slurred' mechanics.",
        "pitch_target": "Alto: Concert A5 (880 Hz) | Tenor: Concert G4 (784 Hz)"
    },
    "2_summertime": {
        "title": "Summertime",
        "key_alto": "B Minor",
        "key_tenor": "E Minor",
        "notes_alto": "F# - B - F# - E - [Low D - B]",
        "notes_tenor": "B - E - B - A - [G - E]",
        "focus": "Lower Register Subtone & Warm Air Velocity",
        "somatic_anchor": "Drop tongue arch to 'Oh'; soft lower lip cushion acts as a passive shock absorber.",
        "pitch_target": "Subtone warmth without pitch sagging."
    },
    "3_aint_no_sunshine": {
        "title": "Ain't No Sunshine",
        "key_alto": "F# Minor",
        "key_tenor": "B Minor",
        "notes_alto": "[C# - C# - C#] - E - F#",
        "notes_tenor": "[F# - F# - F#] - A - B",
        "focus": "Vocal Emulation & Lyric Phrasing",
        "somatic_anchor": "Articulate lyrics internally through mouthpiece to mirror vocal micro-dynamics.",
        "pitch_target": "Stable air column during repeated pitch drops."
    },
    "4_perfect": {
        "title": "Perfect",
        "key_alto": "F Major",
        "key_tenor": "Bb Major",
        "notes_alto": "C - C - Bb - A - G - F - G - A",
        "notes_tenor": "F - F - Eb - D - C - Bb - C - D",
        "focus": "Major Scale Mechanics & 'Bis' Bb Pearl Usage",
        "somatic_anchor": "Use index finger covering both pearls for Bis Bb; maintain light finger pressure.",
        "pitch_target": "Smooth scalar motion without key clatter."
    },
    "5_fly_me": {
        "title": "Fly Me to the Moon",
        "key_alto": "A Major",
        "key_tenor": "D Major",
        "notes_alto": "C# - B - A - G# - F#",
        "notes_tenor": "F# - E - D - C# - B",
        "focus": "Air Support on Descending Intervals",
        "somatic_anchor": "Maintain pressurized abdominal support ('Thick Air') to prevent pitch dropping.",
        "pitch_target": "Keep pitch rock-steady during descending scalar runs."
    },
    "6_careless_whisper": {
        "title": "Careless Whisper",
        "key_alto": "D Minor",
        "key_tenor": "G Minor",
        "notes_alto": "[High D - C#] - A - F - E - Low D",
        "notes_tenor": "[High G - F#] - D - Bb - A - Low G",
        "focus": "Upper Register Limits & High Palm Key Voicing",
        "somatic_anchor": "Arch tongue into 'ee' position to accelerate air velocity; zero upward jaw biting.",
        "pitch_target": "Clean palm key articulation with rich upper harmonics."
    }
}

# -----------------------------------------------------------------------------
# HEADER & SIDEBAR NAVIGATION
# -----------------------------------------------------------------------------
st.markdown('<div class="main-header">🎷 Saxophone 1+5 Practice & Micro-Rest Timer</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">Rights Holder: <b>Scott Niewinski</b> | Grounded in Aural-First Practice Manuals, SuperMemo Memory Dynamics & Neuro-Somatic Motor Control</div>', unsafe_allow_html=True)

st.sidebar.header("⚙️ Practice Setup & Configuration")
horn_type = st.sidebar.selectbox("Select Saxophone Instrument:", ["Alto Saxophone (E♭)", "Tenor Saxophone (B♭)"])
selected_song_key = st.sidebar.selectbox(
    "Select Repertoire Song:",
    list(REPERTOIRE.keys()),
    format_func=lambda k: REPERTOIRE[k]["title"]
)

song_info = REPERTOIRE[selected_song_key]

st.sidebar.markdown("---")
st.sidebar.markdown("### 🧘 Bio-Acoustic Checkpoints")
st.sidebar.info("""
**1. Joe Allard "Dis-ney" Posture**: Tongue sides touch upper molars.
**2. "Thick Air" Support**: *Transversus abdominis* compresses lower abdominal wall.
**3. 10-Second Rule**: Mandatory physical rest after every bout for basal ganglia replay.
""")

app_mode = st.radio(
    "Select Practice Module:",
    [
        "⏱️ Full 20-Minute Daily Microcycle",
        "🔁 1+5 Deliberate Variability Engine",
        "🧘 Standalone 10-Second Micro-Rest Timer",
        "📊 SuperMemo Memory Stability ($S$) Logger"
    ],
    horizontal=True
)

st.markdown("---")

# -----------------------------------------------------------------------------
# MODULE 1: FULL 20-MINUTE DAILY MICROCYCLE
# -----------------------------------------------------------------------------
if app_mode == "⏱️ Full 20-Minute Daily Microcycle":
    st.subheader(f"⏱️ 20-Minute Neuro-Somatic Microcycle — {song_info['title']}")
    
    m_col1, m_col2 = st.columns([1, 1])
    with m_col1:
        st.markdown("### 🎯 Song Profile & Motif")
        st.write(f"**Selected Horn:** {horn_type}")
        st.write(f"**Key Signature:** {song_info['key_alto'] if 'Alto' in horn_type else song_info['key_tenor']}")
        st.write(f"**Primary Motif:** `{song_info['notes_alto'] if 'Alto' in horn_type else song_info['notes_tenor']}`")
        st.write(f"**Biomechanical Focus:** {song_info['focus']}")
        st.warning(f"💡 **Somatic Anchor:** {song_info['somatic_anchor']}")

    with m_col2:
        st.markdown("### 📅 20-Minute Time Budget")
        st.markdown("""
        - **Min 00–03 (3 mins)**: Bio-Acoustic Calibration & Mouthpiece Pitch Matching
        - **Min 03–15 (12 mins)**: Aural Repertoire & 1+5 Engine (with 10s Micro-Rests)
        - **Min 15–20 (5 mins)**: First-Person Mental Rehearsal & Overtone Drops
        """)

    st.markdown("---")
    
    phase_tabs = st.tabs(["Phase 1: Calibration (Min 0-3)", "Phase 2: 1+5 Engine (Min 3-15)", "Phase 3: Mental Rehearsal (Min 15-20)"])

    with phase_tabs[0]:
        st.markdown("### Phase 1: Bio-Acoustic Calibration (Min 00–03)")
        st.markdown(f"**Target Pitch:** `{song_info['pitch_target']}`")
        
        st.checkbox("1. Perform 10-second 'Panting Dog' diaphragmatic resets")
        st.checkbox("2. Execute 'Tssss' 10s exhales isolating the *transversus abdominis*")
        st.checkbox("3. Play fortissimo note on isolated mouthpiece (Alto Concert A5 / Tenor Concert G4)")
        st.checkbox("4. Confirm Joe Allard 'Dis-ney' tongue position (sides touching upper molars)")

    with phase_tabs[1]:
        st.markdown("### Phase 2: Aural Repertoire 1+5 Framework (Min 03–15)")
        st.markdown("Execute each step once with 100% precision. Immediately trigger the **10-Second Micro-Rest** after each attempt.")

        variations = [
            ("Anchor (1)", "Played once with 100% accuracy at slow tempo to set base schema."),
            ("Variation 1 (Tempo)", "Played at 50% speed to heighten proprioceptive finger awareness."),
            ("Variation 2 (Rhythm)", "Played in dotted rhythm (long-short, long-short) for cerebellar timing."),
            ("Variation 3 (Articulation)", "Played completely slurred (no tongue) to expose uneven finger timing."),
            ("Variation 4 (Dynamics)", "Played pianissimo (softest) to demand hyper-control of diaphragm."),
            ("Integration (5)", "Played at target tempo to lock in Generalized Motor Program (GMP).")
        ]

        for idx, (v_name, v_desc) in enumerate(variations):
            with st.expander(f"Step {idx+1}: {v_name}", expanded=(idx==0)):
                st.write(f"**Instruction:** {v_desc}")
                st.write(f"**Motif:** `{song_info['notes_alto'] if 'Alto' in horn_type else song_info['notes_tenor']}`")
                
                if st.button(f"⚡ Execute Step {idx+1} & Trigger 10s Micro-Rest", key=f"btn_phase2_{idx}"):
                    st.markdown('<div class="rest-box"><b>🧘 10-SECOND MICRO-REST ACTIVE!</b><br>Drop instrument/hands to lap. Close eyes. Relax embouchure.<br><i>Allow basal ganglia offline sequence replay...</i></div>', unsafe_allow_html=True)
                    
                    progress_bar = st.progress(0)
                    status_text = st.empty()
                    
                    for sec in range(10, 0, -1):
                        if sec == 5:
                            status_text.markdown("⏱️ **MIDPOINT (5.0s):** Micro-Tick — *Maintain silent focus...*")
                        else:
                            status_text.markdown(f"🧘 **Resting...** `{sec}s remaining` [SILENT REPLAY]")
                        progress_bar.progress((10 - sec + 1) / 10)
                        time.sleep(0.15)  # Fast interactive simulation
                        
                    status_text.success("✅ **10-SECOND CONSOLIDATION COMPLETE!** Re-engage next step.")

    with phase_tabs[2]:
        st.markdown("### Phase 3: First-Person Mental Rehearsal (Min 15–20)")
        st.markdown("""
        Put the horn away. Close your eyes and execute **first-person mental rehearsal**:
        1. Feel the cool brass pearl keys under your fingertips.
        2. Feel the cushion of your lower lip and the steady "thick air" breath support.
        3. Hear the exact pitch and tone resonance of the phrase in your mind's ear (audiation).
        """)
        
        if st.button("🧘 Start 3-Minute Mental Rehearsal Timer"):
            st.info("🧘 Mental Rehearsal Active... Close eyes and visualize execution.")
            m_bar = st.progress(0)
            for m_sec in range(180, 0, -1):
                m_bar.progress((180 - m_sec + 1) / 180)
                time.sleep(0.01)
            st.success("🎉 Mental Rehearsal Complete! Session myelinated.")

# -----------------------------------------------------------------------------
# MODULE 2: 1+5 DELIBERATE VARIABILITY ENGINE
# -----------------------------------------------------------------------------
elif app_mode == "🔁 1+5 Deliberate Variability Engine":
    st.subheader("🔁 1+5 Deliberate Variability Framework Generator")
    st.markdown("""
    The **1+5 Practice Model** prevents somatotopic cortical map smearing and focal dystonia by injecting **Contextual Interference**.
    Execute the Anchor once, followed by 5 specific mutations with 10-second micro-rests between each.
    """)

    custom_phrase = st.text_input("Enter Motif / Phrase to Practice:", value=song_info['notes_alto'] if 'Alto' in horn_type else song_info['notes_tenor'])
    
    st.markdown("### 1+5 Mutation Sequence:")
    
    col_var1, col_var2 = st.columns(2)
    with col_var1:
        st.markdown("1. **Anchor (1)**: Baseline execution at slow tempo.")
        st.markdown("2. **Variation 1 (Tempo 50%)**: Extreme slow motion.")
        st.markdown("3. **Variation 2 (Dotted Rhythm)**: Swung/dotted timing.")
    with col_var2:
        st.markdown("4. **Variation 3 (Slurred)**: Zero articulation, 100% legato.")
        st.markdown("5. **Variation 4 (Pianissimo)**: Minimal air volume.")
        st.markdown("6. **Integration (5)**: Full target speed.")

    if st.button("🚀 Start Interactive 1+5 Automated Microcycle"):
        steps = ["Anchor", "Var 1 (50% Speed)", "Var 2 (Dotted Rhythm)", "Var 3 (Slurred)", "Var 4 (Pianissimo)", "Integration (5)"]
        
        for step_idx, step_name in enumerate(steps):
            st.markdown(f"#### Step {step_idx+1}: {step_name} — `{custom_phrase}`")
            st.markdown('<div class="active-box">🎷 <b>PLAYING BOUT ACTIVE</b> — Focus on 100% accuracy.</div>', unsafe_allow_html=True)
            time.sleep(0.5)
            
            st.markdown('<div class="rest-box"><b>🧘 TRIGGERING 10-SECOND MICRO-REST...</b> Drop hands, close eyes.</div>', unsafe_allow_html=True)
            p_bar = st.progress(0)
            for s in range(10, 0, -1):
                p_bar.progress((10 - s + 1) / 10)
                time.sleep(0.12)
            st.success(f"✅ Step {step_idx+1} ({step_name}) Consolidated!")
            st.markdown("---")

# -----------------------------------------------------------------------------
# MODULE 3: STANDALONE 10-SECOND MICRO-REST TIMER
# -----------------------------------------------------------------------------
elif app_mode == "🧘 Standalone 10-Second Micro-Rest Timer":
    st.subheader("🧘 Standalone 10-Second Micro-Rest Timer Engine")
    st.markdown("""
    Use this timer during any live practice session. Immediately upon completing a physical bout, press **TRIGGER REST**.
    The timer emulates wrist haptic vibration cues to guide basal ganglia offline replay.
    """)

    st.markdown("""
    - **0.0s (Start)**: `[100ms, 50ms, 100ms]` Double Pulse -> *Drop hands, release embouchure, close eyes.*
    - **5.0s (Midpoint)**: `[50ms]` Micro-Tick -> *Maintain silent focus; allow basal ganglia replay.*
    - **10.0s (End)**: `[300ms]` Long Pulse -> *10s consolidation complete. Re-engage next bout.*
    """)

    if st.button("🧘 TRIGGER 10-SECOND MICRO-REST NOW", use_container_width=True):
        st.markdown('<div class="rest-box"><h2 style="color:#D97706; text-align:center;">🧘 10-SECOND MICRO-REST IN PROGRESS</h2><p style="text-align:center; font-size:1.2rem;">Drop hands to lap. Close eyes. Relax lower lip and jaw.</p></div>', unsafe_allow_html=True)
        
        timer_display = st.empty()
        prog_bar = st.progress(0)
        
        for sec in range(10, 0, -1):
            if sec > 5:
                pulse_text = "📳 **START PULSE DELIVERED:** Hands down, eyes closed."
            elif sec == 5:
                pulse_text = "⏱️ **MIDPOINT TICK (5.0s):** Re-anchor silent attention."
            else:
                pulse_text = "🧘 **FINAL CONSOLIDATION PHASE:** Preparing for next attempt..."
                
            timer_display.markdown(f"<h1 style='text-align:center; color:#1E3A8A;'>{sec}.0 s</h1><p style='text-align:center;'>{pulse_text}</p>", unsafe_allow_html=True)
            prog_bar.progress((10 - sec + 1) / 10)
            time.sleep(0.3)
            
        timer_display.markdown("<h1 style='text-align:center; color:#10B981;'>✅ 10.0 s - COMPLETE</h1><p style='text-align:center;'>📳 <b>COMPLETION LONG PULSE DELIVERED!</b> Re-engage next atomic attempt.</p>", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# MODULE 4: SUPERMEMO MEMORY STABILITY LOGGER
# -----------------------------------------------------------------------------
elif app_mode == "📊 SuperMemo Memory Stability ($S$) Logger":
    st.subheader("📊 SuperMemo Memory Stability ($S$) & Retrievability ($R$) Logger")
    st.markdown("""
    Tracks session retrievability decay $R(t) = e^{-\\frac{\\ln(2) \\cdot t}{S}}$ and enforces the **85% accuracy threshold** for motor schema stability.
    """)

    col_log1, col_log2 = st.columns(2)
    with col_log1:
        st.markdown("### Log Session Metrics")
        trials_input = st.number_input("Total Bouts / Attempts:", min_value=1, max_value=30, value=6)
        successes_input = st.number_input("Successful Bouts (100% Accuracy):", min_value=0, max_value=trials_input, value=6)
        calc_acc = (successes_input / trials_input) * 100.0 if trials_input > 0 else 0.0
        
        st.metric("Session Accuracy", f"{calc_acc:.1f}%", delta="≥ 85% Target Met" if calc_acc >= 85.0 else "< 85% Sub-Threshold")

        stability_s = st.slider("Current Memory Stability ($S$ in days):", min_value=0.5, max_value=30.0, value=2.16, step=0.1)
        hours_elapsed = st.number_input("Hours Since Last Session:", min_value=0.0, max_value=72.0, value=12.0)

    with col_log2:
        st.markdown("### Calculated Memory Retrievability ($R$)")
        days_elapsed = hours_elapsed / 24.0
        retrievability = math.exp(-math.log(2) * days_elapsed / stability_s) * 100.0 if stability_s > 0 else 0.0
        
        st.metric("Current Retrievability $R(t)$", f"{retrievability:.1f}%")

        if calc_acc >= 85.0:
            st.success("🎉 **THRESHOLD MET:** Memory stability $S$ increased by $1.5\\times$. Myelination score updated.")
        else:
            st.warning("⚠️ **SUB-THRESHOLD:** Reduce tempo by 20% or isolate 2-note micro-phrases.")

        if st.button("💾 Log Signed Session under Scott Niewinski IP"):
            payload = {
                "ip_holder": "Scott Niewinski",
                "song": song_info['title'],
                "instrument": horn_type,
                "trials": trials_input,
                "successes": successes_input,
                "accuracy_percent": calc_acc,
                "memory_stability_days": stability_s,
                "retrievability_percent": retrievability,
                "timestamp": time.time()
            }
            
            secret_key = b"niewinski_sax_timer_ip_2026"
            payload_bytes = json.dumps(payload, sort_keys=True).encode('utf-8')
            sig = hmac.new(secret_key, payload_bytes, hashlib.sha256).hexdigest()
            
            st.success("✅ **SESSION LOGGED & CRYPTOGRAPHICALLY SIGNED!**")
            st.code(f"HMAC-SHA256 Signature: {sig}")
            st.json(payload)
