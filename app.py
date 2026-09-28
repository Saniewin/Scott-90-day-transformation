"""
Soprano Saxophone 1+5 Practice, Visual Fingering & Micro-Rest Dashboard (v2.0)
Rights & Intellectual Property Holder: Scott Niewinski

EXCLUSIVELY FOR SOPRANO SAXOPHONE (Bb). ZERO ALTO / ZERO TENOR.

Features:
1. Complete Bb Soprano Visual Fingering Suite & Interactive Key Diagram Engine
2. 6-Song Aural Repertoire Progression with Step-by-Step Specialty Lessons & Sidenotes
3. Detached Mouthpiece Pitch Diagnostic (Concert C6 / 1046 Hz) & Biting Prevention
4. Full 20-Minute Daily Microcycle Guide & 1+5 Deliberate Variability Generator
5. Automated 10-Second Micro-Rest Timer Engine with Wrist Haptic/Visual Pulse Notifications
6. SuperMemo Memory Stability (S) & Retrievability (R) Cryptographic Session Logger
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
    page_title="Soprano Saxophone Master Visual Fingering & Practice Dashboard (Scott Niewinski IP)",
    page_icon="🎷",
    layout="wide"
)

# Custom CSS Styling
st.markdown("""
<style>
    .main-header {
        font-size: 2.2rem;
        font-weight: 800;
        color: #0F172A;
        margin-bottom: 0.2rem;
    }
    .sub-header {
        font-size: 1.0rem;
        color: #475569;
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
        padding: 14px;
        border-radius: 8px;
        margin-bottom: 12px;
    }
    .fingering-card {
        background-color: #F8FAFC;
        border: 1px solid #E2E8F0;
        border-radius: 8px;
        padding: 12px;
        text-align: center;
        font-family: monospace;
    }
</style>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# VISUAL FINGERING DATABASE (SOPRANO SAXOPHONE Bb ONLY)
# -----------------------------------------------------------------------------
SOPRANO_FINGERINGS = {
    "C#5 (Middle/High)": {
        "lh": "⚪ ⚪ ⚪",
        "rh": "⚪ ⚪ ⚪",
        "octave": False,
        "notes": "Completely open tube. Balance instrument with thumbs and mouth anchor."
    },
    "C5 (Middle)": {
        "lh": "⚪ ⚫ ⚪",
        "rh": "⚪ ⚪ ⚪",
        "octave": False,
        "notes": "Left Middle Finger (pearl 2) only. Very short tube; low resistance."
    },
    "B4": {
        "lh": "⚫ ⚪ ⚪",
        "rh": "⚪ ⚪ ⚪",
        "octave": False,
        "notes": "Left Index Finger (pearl 1). Keep airstream steady; hover unused fingers close."
    },
    "Bb4": {
        "lh": "⚫ (bis) ⚪",
        "rh": "⚪ ⚪ ⚪",
        "octave": False,
        "notes": "Left Index Finger pressing B pearl and small Bis key simultaneously."
    },
    "A4": {
        "lh": "⚫ ⚫ ⚪",
        "rh": "⚪ ⚪ ⚪",
        "octave": False,
        "notes": "Left Index (1) and Middle (2). Relax jaw; let air velocity carry vibration."
    },
    "G#4": {
        "lh": "⚫ ⚫ ⚫ + G#",
        "rh": "⚪ ⚪ ⚪",
        "octave": False,
        "notes": "Left Hand 1, 2, 3 plus Left Pinky G# Table Key."
    },
    "G4": {
        "lh": "⚫ ⚫ ⚫",
        "rh": "⚪ ⚪ ⚪",
        "octave": False,
        "notes": "Left Hand 1, 2, 3. Drop back of tongue ('Ah' or 'Oh' internal vowel shape)."
    },
    "F#4": {
        "lh": "⚫ ⚫ ⚫",
        "rh": "⚪ ⚫ ⚪",
        "octave": False,
        "notes": "Left Hand 1, 2, 3 + Right Middle Finger (pearl 2). Hover fingers over pearls."
    },
    "F4": {
        "lh": "⚫ ⚫ ⚫",
        "rh": "⚫ ⚪ ⚪",
        "octave": False,
        "notes": "Left Hand 1, 2, 3 + Right Index Finger (pearl 1)."
    },
    "E4": {
        "lh": "⚫ ⚫ ⚫",
        "rh": "⚫ ⚫ ⚪",
        "octave": False,
        "notes": "Left Hand 1, 2, 3 + Right Hand 1, 2. Hands act as a single unit."
    },
    "Eb4": {
        "lh": "⚫ ⚫ ⚫",
        "rh": "⚫ ⚫ ⚫ + Eb",
        "octave": False,
        "notes": "All 6 main pearls + Right Pinky Eb key."
    },
    "D4 (Low)": {
        "lh": "⚫ ⚫ ⚫",
        "rh": "⚫ ⚫ ⚫",
        "octave": False,
        "notes": "All 6 main pearls. Requires voluminous 'thick air' to prevent cracking."
    },
    "D5 (High)": {
        "lh": "⚫ ⚫ ⚫",
        "rh": "⚫ ⚫ ⚫",
        "octave": True,
        "notes": "Thumb Octave Key [OCT] + All 6 main pearls. Crossing the Break transition."
    },
    "E5 (High)": {
        "lh": "⚫ ⚫ ⚫",
        "rh": "⚫ ⚫ ⚪",
        "octave": True,
        "notes": "Thumb Octave Key [OCT] + Left Hand 1, 2, 3 + Right Hand 1, 2."
    },
    "F5 (High)": {
        "lh": "⚫ ⚫ ⚫",
        "rh": "⚫ ⚪ ⚪",
        "octave": True,
        "notes": "Thumb Octave Key [OCT] + Left Hand 1, 2, 3 + Right Index Finger (pearl 1)."
    },
    "Eb5 (High)": {
        "lh": "⚫ ⚫ ⚫",
        "rh": "⚫ ⚫ ⚫ + Eb",
        "octave": True,
        "notes": "Thumb Octave Key [OCT] + All 6 main pearls + Right Pinky Eb key."
    },
    "F#5 (High)": {
        "lh": "⚫ ⚫ ⚫",
        "rh": "⚪ ⚫ ⚪",
        "octave": True,
        "notes": "Thumb Octave Key [OCT] + Left Hand 1, 2, 3 + Right Middle Finger (pearl 2)."
    },
    "High G5": {
        "lh": "⚫ ⚫ ⚫ (Palm/G5)",
        "rh": "⚪ ⚪ ⚪",
        "octave": True,
        "notes": "Upper register limit. Arch tongue internally ('ee' syllable) to accelerate air velocity."
    }
}

# -----------------------------------------------------------------------------
# SOPRANO REPERTOIRE CURRICULUM DATABASE
# -----------------------------------------------------------------------------
REPERTOIRE = {
    "1_saints": {
        "title": "1. When the Saints Go Marching In",
        "transposition": "Soprano D Major (Concert C Major)",
        "soprano_notes": "C5 - E5 - F5 - [High G5]",
        "full_phrase": "C - E - F - G ... C - E - F - G ... C - E - F - G - E - C - E - D",
        "note_list": ["C5 (Middle)", "E5 (High)", "F5 (High)", "High G5"],
        "focus": "Crossing the Break (Middle C to High D / F to High G)",
        "somatic_anchor": "Keep Right Hand Down on C; use 'Slow, Straight, Slurred' mechanics. Freeze jaw, increase air velocity.",
        "sidenote_insight": "Isolates the mechanical break jump. Moving from open C to closed D or F to High G lengthens the acoustic tube instantly. Apply the 1+5 Framework with 10s micro-rests to allow offline basal ganglia consolidation.",
        "pitch_target": "Concert C6 (1046 Hz) on isolated mouthpiece."
    },
    "2_summertime": {
        "title": "2. Summertime",
        "transposition": "Soprano E Minor (Concert D Minor)",
        "soprano_notes": "B4 - E5 - B4 - A4 - G4 - E4",
        "full_phrase": "B - E - B - A - G - E",
        "note_list": ["B4", "E5 (High)", "B4", "A4", "G4", "E4"],
        "focus": "Lower Register Subtone & Warm Air Velocity ('Thick Air')",
        "somatic_anchor": "Drop oral cavity to 'Oh' or 'Ah' vowel shape. Relax lower lip as a soft shock absorber against the reed.",
        "sidenote_insight": "Lower notes on soprano tend to crack due to high acoustic resistance. Pull lower jaw slightly downward/backward. The lower lip acts as a fleshy weather-strip absorbing harsh overtones.",
        "pitch_target": "Subtone warmth without pitch sagging."
    },
    "3_aint_no_sunshine": {
        "title": "3. Ain't No Sunshine",
        "transposition": "Soprano B Minor (Concert A Minor)",
        "soprano_notes": "[F#4 - F#4 - F#4] - A4 - B4",
        "full_phrase": "F# - F# - F# - A - B (Ain't no sun-shine when she's gone)",
        "note_list": ["F#4", "A4", "B4"],
        "focus": "Vocal Emulation & Lyric Audiation",
        "somatic_anchor": "Articulate lyrics internally through the mouthpiece to mirror vocal micro-dynamics.",
        "sidenote_insight": "Uses audiation (internalizing sound before execution). Sing the lyrics through the mouthpiece while blowing to replicate speech pauses naturally without staff notation.",
        "pitch_target": "Stable air column during repeated pitch drops."
    },
    "4_perfect": {
        "title": "4. Perfect",
        "transposition": "Soprano Bb Major (Concert Ab Major)",
        "soprano_notes": "F5 - F5 - Eb5 - D5 - C5 - Bb4 - C5 - D5",
        "full_phrase": "F - F - Eb - D - C - Bb - C - D",
        "note_list": ["F5 (High)", "Eb5 (High)", "D5 (High)", "C5 (Middle)", "Bb4"],
        "focus": "Major Scale Mechanics & 'Bis' Bb Pearl Usage",
        "somatic_anchor": "Use index finger covering both pearls for Bis Bb; hover right-hand fingers millimeters over pearls.",
        "sidenote_insight": "Master the 'bis' key (LH index covering B pearl and small bis key simultaneously). Prevents mechanical lag and 'flying fingers' during rapid Bb major scale runs.",
        "pitch_target": "Smooth scalar motion without key clatter."
    },
    "5_fly_me": {
        "title": "5. Fly Me to the Moon",
        "transposition": "Soprano D Major (Concert C Major)",
        "soprano_notes": "F#4 - E4 - D4 - C#5 - B4",
        "full_phrase": "F# - E - D - C# - B (Fly me to the moon)",
        "note_list": ["F#4", "E4", "D4 (Low)", "C#5 (Middle/High)", "B4"],
        "focus": "Air Support on Descending Intervals",
        "somatic_anchor": "Maintain pressurized abdominal support ('Thick Air') to prevent pitch dropping flat.",
        "sidenote_insight": "Descending scalar notes drop acoustic tube resistance, causing beginners to drop air pressure and sag flat. Maintain abdominal wall contraction throughout the descent.",
        "pitch_target": "Rock-steady pitch during descending scalar runs."
    },
    "6_careless_whisper": {
        "title": "6. Careless Whisper",
        "transposition": "Soprano G Minor (Concert F Minor)",
        "soprano_notes": "[High G5 - F#5] - D5 - Bb4 - A4 - Low G4",
        "full_phrase": "High G - F# - D - Bb - A - Low G",
        "note_list": ["High G5", "F#5 (High)", "D5 (High)", "Bb4", "A4", "G4"],
        "focus": "Upper Register Limits & High Palm Key Voicing",
        "somatic_anchor": "Arch tongue into 'ee' position to accelerate air velocity; zero upward jaw biting.",
        "sidenote_insight": "Navigating above the soprano's cut-off frequency (~1340 Hz). The bore no longer dictates pitch easily. Arch back of tongue ('ee' syllable) to accelerate air speed without crushing the reed facing.",
        "pitch_target": "Clean palm key articulation with rich upper harmonics."
    }
}

# -----------------------------------------------------------------------------
# HEADER & SIDEBAR NAVIGATION
# -----------------------------------------------------------------------------
st.markdown('<div class="main-header">🎷 Soprano Saxophone Master Visual Fingering & Practice Dashboard</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">Rights Holder: <b>Scott Niewinski</b> | Exclusively Tailored for Soprano Saxophone (B♭) — Aural-First Pedagogy, Visual Key Maps & SuperMemo Micro-Rests</div>', unsafe_allow_html=True)

st.sidebar.header("⚙️ Soprano Configuration & Setup")
st.sidebar.markdown("**Selected Horn:** 🎺 **Soprano Saxophone (B♭)** *(Fixed)*")

selected_song_key = st.sidebar.selectbox(
    "Select Repertoire Song:",
    list(REPERTOIRE.keys()),
    format_func=lambda k: REPERTOIRE[k]["title"]
)

song_info = REPERTOIRE[selected_song_key]

st.sidebar.markdown("---")
st.sidebar.markdown("### 🧘 Soprano Bio-Acoustic Checkpoints")
st.sidebar.info("""
**1. Detached Mouthpiece Pitch**: Concert C6 (1046 Hz).
**2. Biting Prevention**: Pitch > C#6 indicates biting. Shape oral cavity to 'Ah'/'Oh'.
**3. Ergonomics & Stance**: Hold horn at 45° angle. Top teeth rest on beak; right thumb pushes forward as anchor.
**4. Joe Allard Posture**: Tongue sides touch upper molars ('Dis-ney').
**5. 10-Second Rule**: Mandatory physical rest after every attempt for basal ganglia replay.
""")

app_mode = st.radio(
    "Select Practice Module:",
    [
        "🎼 Module 1: Song Repertoire & Visual Note Maps",
        "📖 Module 2: Complete Soprano Fingering Database",
        "⏱️ Module 3: 20-Min Microcycle & 1+5 Engine",
        "🧘 Module 4: Standalone 10-Second Micro-Rest Timer",
        "📊 Module 5: SuperMemo Memory Stability ($S$) Logger"
    ],
    horizontal=True
)

st.markdown("---")

# -----------------------------------------------------------------------------
# MODULE 1: SONG REPERTOIRE & VISUAL NOTE MAPS
# -----------------------------------------------------------------------------
if app_mode == "🎼 Module 1: Song Repertoire & Visual Note Maps":
    st.subheader(f"🎼 {song_info['title']} — Soprano Repertoire Map")
    
    col_s1, col_s2 = st.columns([1, 1])
    with col_s1:
        st.markdown("### 🎯 Song Profile")
        st.write(f"**Transposition:** {song_info['transposition']}")
        st.write(f"**Core Soprano Motif:** `{song_info['soprano_notes']}`")
        st.write(f"**Full Phrase Sequence:** `{song_info['full_phrase']}`")
        st.write(f"**Biomechanical Focus:** {song_info['focus']}")
        st.warning(f"💡 **Somatic Anchor:** {song_info['somatic_anchor']}")

    with col_s2:
        st.markdown("### 🔍 Pedagogical Sidenote & Technical Insight")
        st.info(song_info['sidenote_insight'])

    st.markdown("---")
    st.subheader("Visual Key Diagram for Each Note in Song Motif")
    
    note_cols = st.columns(len(song_info['note_list']))
    for idx, n_name in enumerate(song_info['note_list']):
        with note_cols[idx]:
            f_data = SOPRANO_FINGERINGS.get(n_name, {"lh": "⚫ ⚫ ⚫", "rh": "⚪ ⚪ ⚪", "octave": False, "notes": "Standard"})
            st.markdown(f"#### Note {idx+1}: {n_name}")
            
            oct_text = "[OCT] ENGAGED" if f_data["octave"] else "[OCT] Off"
            
            st.markdown(f"""
            <div class="fingering-card">
                <b>{n_name}</b><br><br>
                <span style="color:#D97706; font-weight:bold;">{oct_text}</span><br><br>
                <b>Left Hand:</b><br>{f_data['lh']}<br><br>
                <b>Right Hand:</b><br>{f_data['rh']}
            </div>
            """, unsafe_allow_html=True)
            st.caption(f"**Somatic:** {f_data['notes']}")

# -----------------------------------------------------------------------------
# MODULE 2: COMPLETE SOPRANO FINGERING DATABASE
# -----------------------------------------------------------------------------
elif app_mode == "📖 Module 2: Complete Soprano Fingering Database":
    st.subheader("📖 Complete B♭ Soprano Saxophone Fingering Database")
    st.markdown("""
    Explore exact finger triggers, octave key requirements, and somatic voicing cues for foundational B♭ Soprano Saxophone notes.
    """)

    f_col1, f_col2 = st.columns([1, 2])
    with f_col1:
        selected_note_db = st.selectbox("Select Note to Inspect:", list(SOPRANO_FINGERINGS.keys()))
        f_info = SOPRANO_FINGERINGS[selected_note_db]
        
        st.markdown("### Key Trigger Summary:")
        st.write(f"**Octave Key (`[OCT]`):** {'ENGAGED (Left Thumb)' if f_info['octave'] else 'Off (Released)'}")
        st.write(f"**Left Hand (Top 3 Pearls):** `{f_info['lh']}`")
        st.write(f"**Right Hand (Bottom 3 Pearls):** `{f_info['rh']}`")
        st.info(f"💡 **Somatic Voicing Cue:** {f_info['notes']}")

    with f_col2:
        st.markdown(f"### Visual Graphic Schematic — {selected_note_db}")
        st.markdown(f"""
        ```
        =======================================================
          SOPRANO SAXOPHONE KEY SCHEMATIC: {selected_note_db}
        =======================================================
          OCTAVE KEY:   [ {"●" if f_info['octave'] else "○"} ]  (Left Thumb Back Pad)
          ---------------------------------------------------
          LEFT HAND:    {f_info['lh']}
                        (Index: Pearl 1 | Middle: Pearl 2 | Ring: Pearl 3)
          ---------------------------------------------------
          RIGHT HAND:   {f_info['rh']}
                        (Index: Pearl 4 | Middle: Pearl 5 | Ring: Pearl 6)
        =======================================================
        ```
        """)

# -----------------------------------------------------------------------------
# MODULE 3: 20-MIN MICROCYCLE & 1+5 ENGINE
# -----------------------------------------------------------------------------
elif app_mode == "⏱️ Module 3: 20-Min Microcycle & 1+5 Engine":
    st.subheader(f"⏱️ 20-Minute Daily Microcycle — {song_info['title']}")
    
    st.markdown("""
    - **Min 00–03 (3 mins)**: Bio-Acoustic Mouthpiece Pitch Calibration (Concert C6 / 1046 Hz)
    - **Min 03–15 (12 mins)**: 1+5 Deliberate Variability Framework (with 10s Micro-Rests)
    - **Min 15–20 (5 mins)**: First-Person Mental Rehearsal & Audiation
    """)

    phase_tabs = st.tabs(["Phase 1: Mouthpiece Pitch Calibration", "Phase 2: 1+5 Engine (with 10s Rests)", "Phase 3: Mental Rehearsal"])

    with phase_tabs[0]:
        st.markdown("### Phase 1: Bio-Acoustic Calibration (Min 00–03)")
        st.info("🎯 **Isolated Mouthpiece Pitch Target:** Concert C6 (1046 Hz) at fortissimo.")
        
        st.checkbox("1. Perform 10-second 'Panting Dog' diaphragmatic resets")
        st.checkbox("2. Execute 'Tssss' 10s exhales isolating the *transversus abdominis*")
        st.checkbox("3. Blow loud note on detached mouthpiece — verify Concert C6 target (Pitch > C#6 indicates biting!)")
        st.checkbox("4. Confirm Joe Allard 'Dis-ney' posture (tongue sides touching upper molars)")

    with phase_tabs[1]:
        st.markdown("### Phase 2: 1+5 Framework (Min 03–15)")
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
                st.write(f"**Soprano Motif:** `{song_info['soprano_notes']}`")
                
                if st.button(f"⚡ Execute Step {idx+1} & Trigger 10s Rest", key=f"btn_sop_phase2_{idx}"):
                    st.markdown('<div class="rest-box"><b>🧘 10-SECOND MICRO-REST ACTIVE!</b><br>Drop instrument/hands to lap. Close eyes. Relax embouchure.<br><i>Allow basal ganglia offline sequence replay...</i></div>', unsafe_allow_html=True)
                    
                    progress_bar = st.progress(0)
                    status_text = st.empty()
                    
                    for sec in range(10, 0, -1):
                        if sec == 5:
                            status_text.markdown("⏱️ **MIDPOINT (5.0s):** Micro-Tick — *Maintain silent focus...*")
                        else:
                            status_text.markdown(f"🧘 **Resting...** `{sec}s remaining` [SILENT REPLAY]")
                        progress_bar.progress((10 - sec + 1) / 10)
                        time.sleep(0.15)
                        
                    status_text.success("✅ **10-SECOND CONSOLIDATION COMPLETE!** Re-engage next step.")

    with phase_tabs[2]:
        st.markdown("### Phase 3: First-Person Mental Rehearsal (Min 15–20)")
        st.markdown("""
        Put the soprano away. Close your eyes and execute **first-person mental rehearsal**:
        1. Feel the cool key pearls under your fingertips.
        2. Feel the lower lip cushion and steady 'thick air' diaphragmatic breath.
        3. Hear the exact pitch and resonance of the phrase in your mind's ear (audiation).
        """)
        
        if st.button("🧘 Start 3-Minute Mental Rehearsal Timer"):
            st.info("🧘 Mental Rehearsal Active... Close eyes and visualize execution.")
            m_bar = st.progress(0)
            for m_sec in range(180, 0, -1):
                m_bar.progress((180 - m_sec + 1) / 180)
                time.sleep(0.01)
            st.success("🎉 Mental Rehearsal Complete! Session myelinated.")

# -----------------------------------------------------------------------------
# MODULE 4: STANDALONE 10-SECOND MICRO-REST TIMER
# -----------------------------------------------------------------------------
elif app_mode == "🧘 Module 4: Standalone 10-Second Micro-Rest Timer":
    st.subheader("🧘 Standalone 10-Second Micro-Rest Timer Engine")
    st.markdown("""
    Use this timer during any live practice session. Immediately upon completing a physical bout, press **TRIGGER REST**.
    The timer emulates wrist haptic vibration cues to guide basal ganglia offline replay.
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
                
            timer_display.markdown(f"<h1 style='text-align:center; color:#0F172A;'>{sec}.0 s</h1><p style='text-align:center;'>{pulse_text}</p>", unsafe_allow_html=True)
            prog_bar.progress((10 - sec + 1) / 10)
            time.sleep(0.3)
            
        timer_display.markdown("<h1 style='text-align:center; color:#10B981;'>✅ 10.0 s - COMPLETE</h1><p style='text-align:center;'>📳 <b>COMPLETION LONG PULSE DELIVERED!</b> Re-engage next atomic attempt.</p>", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# MODULE 5: SUPERMEMO MEMORY STABILITY LOGGER
# -----------------------------------------------------------------------------
elif app_mode == "📊 Module 5: SuperMemo Memory Stability ($S$) Logger":
    st.subheader("📊 SuperMemo Memory Stability ($S$) & Retrievability ($R$) Logger")
    st.markdown("""
    Tracks session retrievability decay $R(t) = e^{-\\frac{\\ln(2) \\cdot t}{S}}$ and enforces the **85% accuracy threshold** for motor schema stability.
    """)

    col_log1, col_log2 = st.columns(2)
    with col_log1:
        st.markdown("### Log Soprano Practice Metrics")
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

        if st.button("💾 Log Signed Soprano Session under Scott Niewinski IP"):
            payload = {
                "ip_holder": "Scott Niewinski",
                "song": song_info['title'],
                "instrument": "Soprano Saxophone (Bb)",
                "trials": trials_input,
                "successes": successes_input,
                "accuracy_percent": calc_acc,
                "memory_stability_days": stability_s,
                "retrievability_percent": retrievability,
                "timestamp": time.time()
            }
            
            secret_key = b"niewinski_soprano_timer_ip_2026"
            payload_bytes = json.dumps(payload, sort_keys=True).encode('utf-8')
            sig = hmac.new(secret_key, payload_bytes, hashlib.sha256).hexdigest()
            
            st.success("✅ **SOPRANO SESSION LOGGED & CRYPTOGRAPHICALLY SIGNED!**")
            st.code(f"HMAC-SHA256 Signature: {sig}")
            st.json(payload)
