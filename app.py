import streamlit as st

# ==============================================================================
# STREAMLIT PAGE CONFIGURATION & THEME SETUP
# Optimized for Samsung Galaxy S26 Ultra (high-resolution vertical mobile viewports)
# ==============================================================================
st.set_page_config(
    page_title="CNS Psychological Services Clinical Systems Audit Portal",
    page_icon="🧬",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Custom CSS for Scientific-Digital, Holographic & Sci-Fi Matrix aesthetic
# Deep dark purple background, glowing vibrant green accents, clean white cards
st.markdown("""
<style>
    /* Main body background & Holographic matrix overlay */
    .stApp {
        background: radial-gradient(circle at center, #120822 0%, #080311 100%) !important;
        color: #FFFFFF !important;
        font-family: 'Segoe UI', -apple-system, BlinkMacSystemFont, Roboto, sans-serif !important;
        position: relative;
    }
    
    /* Digital Grid Mask */
    .stApp::before {
        content: "";
        position: absolute;
        top: 0; left: 0; width: 100%; height: 100%;
        background-image: 
            linear-gradient(rgba(34, 197, 94, 0.012) 1px, transparent 1px),
            linear-gradient(90deg, rgba(34, 197, 94, 0.012) 1px, transparent 1px);
        background-size: 20px 20px;
        pointer-events: none;
        z-index: 0;
    }

    /* Device frame mockup for Samsung S26 Ultra centered canvas */
    @media (min-width: 450px) {
        .block-container {
            max-width: 440px !important;
            padding: 24px !important;
            background: rgba(18, 8, 34, 0.96) !important;
            border-radius: 40px !important;
            box-shadow: 0 0 45px rgba(34, 197, 94, 0.2) !important;
            margin-top: 15px !important;
            margin-bottom: 25px !important;
            border: 4px solid #3B125C !important; /* Rich deep purple outer frame */
            position: relative;
            z-index: 1;
        }
    }
    
    /* Holographic scientific data cards */
    .scientific-card {
        background: rgba(26, 12, 48, 0.75) !important;
        border: 1px solid rgba(34, 197, 94, 0.25) !important;
        border-radius: 16px !important;
        padding: 16px !important;
        margin-bottom: 16px !important;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.6) !important;
        backdrop-filter: blur(12px) !important;
        transition: all 0.3s ease !important;
    }
    .scientific-card:hover {
        border-color: rgba(34, 197, 94, 0.6) !important;
        box-shadow: 0 0 20px rgba(34, 197, 94, 0.35) !important;
    }
    
    /* Glowing custom typography */
    .glow-title {
        font-size: 22px !important;
        font-weight: 900 !important;
        color: #FFFFFF !important;
        text-shadow: 0 0 15px rgba(34, 197, 94, 0.7) !important;
        text-align: center !important;
        font-family: 'Courier New', Courier, monospace !important;
        letter-spacing: 1px !important;
        margin-bottom: 2px !important;
    }
    
    .glow-subtitle {
        font-size: 11px !important;
        color: #22c55e !important; /* Vibrant Matrix Green */
        text-align: center !important;
        font-family: 'Courier New', Courier, monospace !important;
        letter-spacing: 1.5px !important;
        margin-bottom: 24px !important;
        text-transform: uppercase !important;
        font-weight: bold !important;
    }
    
    /* Policy and Target Digital readouts */
    .badge-policy {
        font-size: 10px;
        font-weight: 700;
        background-color: rgba(75, 16, 96, 0.45); /* Deep purple background */
        color: #E1BEE7; /* Light purple text */
        padding: 4px 8px;
        border-radius: 6px;
        display: inline-block;
        margin-bottom: 6px;
        border: 1px solid rgba(123, 31, 162, 0.5);
        font-family: monospace;
    }
    
    .badge-target {
        font-size: 10px;
        font-weight: 700;
        background-color: rgba(34, 197, 94, 0.08); /* Transparent green tint */
        color: #22c55e; /* Vibrant green text */
        padding: 4px 8px;
        border-radius: 6px;
        display: inline-block;
        margin-bottom: 6px;
        margin-left: 4px;
        border: 1px solid rgba(34, 197, 94, 0.35);
        font-family: monospace;
    }

    /* Interactive Popover Trigger styling override */
    div.stPopover > button {
        background-color: rgba(34, 197, 94, 0.05) !important;
        border: 1px solid rgba(34, 197, 94, 0.3) !important;
        color: #22c55e !important;
        border-radius: 8px !important;
        font-size: 10px !important;
        font-family: 'Courier New', Courier, monospace !important;
        text-transform: uppercase !important;
        letter-spacing: 1px !important;
        padding: 2px 8px !important;
        transition: all 0.2s ease !important;
    }
    div.stPopover > button:hover {
        background-color: rgba(34, 197, 94, 0.15) !important;
        border-color: #22c55e !important;
        box-shadow: 0 0 10px rgba(34, 197, 94, 0.4) !important;
        color: #FFFFFF !important;
    }
    
    /* Popover Content box */
    .popover-header {
        font-size: 13px;
        color: #22c55e;
        font-family: monospace;
        font-weight: bold;
        border-bottom: 1px solid rgba(34, 197, 94, 0.3);
        padding-bottom: 4px;
        margin-bottom: 8px;
    }
    
    .popover-body {
        font-size: 11px;
        color: #E2E8F0;
        line-height: 1.4;
    }

    /* Warning & Remediation styling */
    .remedy-alert-box {
        background-color: rgba(251, 192, 45, 0.08) !important;
        border: 1px solid rgba(251, 192, 45, 0.35) !important;
        border-left: 5px solid #FBC02D !important;
        padding: 12px !important;
        border-radius: 8px !important;
        margin-top: 10px !important;
        font-size: 11.5px !important;
        color: #FFE082 !important;
        line-height: 1.4;
    }
    
    /* Cascading Warning banner */
    .critical-cascade {
        background-color: rgba(239, 68, 68, 0.08) !important;
        border: 1px solid rgba(239, 68, 68, 0.3) !important;
        border-left: 5px solid #EF4444 !important;
        padding: 12px !important;
        border-radius: 12px !important;
        margin-bottom: 16px !important;
        font-size: 11px !important;
        color: #FEE2E2 !important;
        line-height: 1.4;
    }

    /* Scientific terminal lines */
    .neon-divider {
        height: 2px;
        background: linear-gradient(to right, rgba(34, 197, 94, 0.5), rgba(75, 16, 96, 0.8), transparent);
        border: none;
        margin: 15px 0;
    }
    
    /* Text overrides to force white text inside columns */
    .stText, p, span, label {
        color: #FFFFFF !important;
    }
</style>
""", unsafe_allow_html=True)

# Title & Holographic System Header
st.markdown('<div class="glow-title">CNS_CLINICAL_SYS_PORTAL</div>', unsafe_allow_html=True)
st.markdown('<div class="glow-subtitle">90-Day Appraisal Compliance Hub v5.0</div>', unsafe_allow_html=True)

# ==============================================================================
# STRATEGIC CLINICAL DATABASE - SOURCED DIRECTLY FROM SOURCE WORKFLOWS
# ==============================================================================
audit_metadata = {
    "Phase 1": {
        "title": "Phase 1: Discovery (Days 1–30)",
        "objective": "Establish an empirical baseline and discover regulatory vulnerabilities in CNS's psychometric operations.",
        "rationale": "Prior to redesigning administrative templates or billing codes, clinical operations must identify licensing, documentation, and waitlist gaps to guard against external audit failures and protect state-level CCBHC certifications.",
        "strengths_overlay": {
            "title": "🧠 CliftonStrengths Strategy: Learner® & Intellection®",
            "guide": "Apply the Learner drive to meticulously absorb licensing regulations, state technical manuals, and CPT billing codes. Deploy Intellection to deeply examine the root causes of compliance and scheduling bottlenecks, establishing a defensible operational blueprint.",
            "examples": [
                "**Learner in Action (Task 1.1)**: Meticulously audits the Form LARA/BPL Rev. 6/25 supervision logs of Limited License Psychologists (LLPs) across all clinics, turning dry state laws into an engaging study of licensing fidelity.",
                "**Intellection in Action (Task 1.2)**: Analyzes why completed testing charts lack documented interactive feedback under CPT 96130, concluding that systemic EHR routing gaps are responsible rather than simple clinician neglect."
            ]
        },
        "tasks": {
            "p1_t1": {
                "label": "Verify LLP Supervision Logs (LARA Compliance)",
                "policy": "MCL 333.18223 & LARA Rule 338.2569: Limited License Psychologists (LLPs) must receive 4 hours/month face-to-face supervision.",
                "target": "100% compliant logs on Form LARA/BPL Rev. 6/25",
                "desc": "Check and verify official supervisory logs for all active LLPs and Temporary LLPs across Oakland, Wayne, and Macomb clinics.",
                "rationale": "Missing or unsigned LARA evaluation logs invalidate all psychological testing claims rendered by LLPs, exposing the agency to immediate licensing board penalties and retrospective Medicaid clawbacks.",
                "remediation": "Immediately halt billing for any LLP found to have undocumented supervision hours. Transition all logs to a centralized HR digital folder. Implement a strict EHR validation lock that prevents bill release until the supervising Licensed Psychologist (LP) signs the supervisory record."
            },
            "p1_t2": {
                "label": "Audit 30 Completed Testing Charts (Interactive Feedback)",
                "policy": "CPT 96130 Guidelines & Medicare Local Coverage Determinations (LCD): First-hour evaluation requires documented interactive feedback.",
                "target": "100% documented feedback session presence in EHR",
                "desc": "Manually extract and audit 30 completed psychological and neuropsychological evaluations across pediatric, adult, and geriatric caseloads.",
                "rationale": "Billing evaluation code CPT 96130 without documenting the delivery of interactive feedback to the patient or caregiver constitutes billing non-compliance.",
                "remediation": "Disclose any deficient billing claims identified and adjust encounters. Deploy a mandatory NextGen EHR template that prevents note-locking until a timestamped section labeled 'Interactive Feedback and Clinical Decision Making' is completed."
            },
            "p1_t3": {
                "label": "Shadow Triage and Referral Velocity Workflows",
                "policy": "SAMHSA CCBHC Access Criteria (2023): Mandates timely, unimpeded access to care (routine care within 14 days, urgent within 1 day).",
                "target": "Map 100% of pipeline lifecycle from referral to intake",
                "desc": "Trace psychological testing referrals from initial clinician request, through the EHR queue, to scheduling, tracking all Prepaid Inpatient Health Plan (PIHP) portals.",
                "rationale": "Prolonged diagnostic wait times bottleneck patient entry into clinical services, triggering MDHHS Corrective Action Plans (CAPs) and threatening CCBHC PPS funding.",
                "remediation": "Construct process maps of administrative handoffs, identify specific delays within the Prepaid Inpatient Health Plan (PIHP) authorization systems, and schedule open-access triage blocks."
            },
            "p1_t4": {
                "label": "Survey Clinical Stakeholders (Report Utility)",
                "policy": "CARF Accreditation Standards (ASPIRE) & CCBHC Care Coordination: Demands that clinical assessments have recognized utility and guide treatment.",
                "target": ">80% response rate from top 20 referring clinicians",
                "desc": "Deploy digital surveys and interview psychiatrists, therapists, and primary care providers regarding report utility and readability.",
                "rationale": "If diagnostic reports fail to influence the Person-Centered Plan (PCP) or guide treatment, psychological testing acts as an isolated, high-cost administrative task.",
                "remediation": "Assess report clarity and standardize the format. Standardize all report layouts to mandate a summary block containing actionable, interdisciplinary recommendations."
            }
        }
    },
    "Phase 2": {
        "title": "Phase 2: Optimization (Days 31–60)",
        "objective": "Re-engineer electronic workflows and standardise clinician tools to resolve operational bottlenecks.",
        "rationale": "Transition from discovery to active system re-engineering. This phase builds standardized EHR templates and voice dictation software workflows to reduce administrative burden and eliminate same-day billing conflicts.",
        "strengths_overlay": {
            "title": "🧠 CliftonStrengths Strategy: Ideation® & Individualization®",
            "guide": "Apply Ideation to brainstorm and build standardized NextGen templates and Dragon voice dictation macros that automate repetitive documentation. Deploy Individualization to deliver customized training, aligning these new digital workflows with each clinician's unique writing and cognitive style.",
            "examples": [
                "**Ideation in Action (Task 2.1)**: Conceptualizes and configures a dynamic 'Smart-Phrase' directory in Dragon Medical One, standardizing Mental Status Exam (MSE) text blocks to cut typing time by 60%.",
                "**Individualization in Action (Task 2.2)**: Tailors training sessions for the clinical team, recognizing that some psychologists learn best via video walk-throughs while others require hands-on clinical co-auditing."
            ]
        },
        "tasks": {
            "p2_t1": {
                "label": "Standardize NextGen EHR Assessment Templates",
                "policy": "CARF Documentation Standards & CCBHC Demonstration Guidelines: Mandates structured, person-centered notes aligned with SOAP criteria.",
                "target": "100% adoption of updated EHR testing templates",
                "desc": "Build and deploy optimized clinical documentation templates inside NextGen EHR, ensuring direct integration of Measurement-Informed Care metrics.",
                "rationale": "Non-standardized, unstructured clinical narratives cause documentation variance, slow down supervisor sign-off, and increase the risk of external audit failure.",
                "remediation": "Collaborate with EHR developers to push the updated clinical assessment template live. Enforce automated validation checks that prevent saving until required fields (e.g., PHQ-9, GAD-7) are entered."
            },
            "p2_t2": {
                "label": "Configure Dragon Medical One & Voice Dictation Macros",
                "policy": "CCBHC Quality Improvement and Efficiency Mandate: Encourages technological modernization to reduce clinician administrative burden.",
                "target": "70% average reduction in narrative documentation time",
                "desc": "Program specialized voice dictation macros and custom templates in Dragon Medical One to standardize auto-text formatting for report writing.",
                "rationale": "Manual typing of complex psychological reports is a primary driver of clinician burnout and extended turnaround times, directly limiting patient access to care.",
                "remediation": "Create and distribute a 'Dragon Clinical Macro Guide' containing pre-formatted voice command scripts for testing feedback and mental status exams."
            },
            "p2_t3": {
                "label": "Audit Billing Modifiers for Same-Day Services (NCCI Edits)",
                "policy": "CMS National Correct Coding Initiative (NCCI) Edits: Prohibits same-day psychologist (96136) and technician (96138) billing without modifiers.",
                "target": "100% billing modifier accuracy for multi-provider testing",
                "desc": "Review same-day billing entries to verify if Billing Modifier 59 (distinct procedural service) or Modifier XE (separate encounter) are correctly applied.",
                "rationale": "Failing to apply modifiers on same-day dual-provider encounters triggers automated claim rejections, locking up clinical revenue.",
                "remediation": "Establish hardcoded billing validation rules in the EHR that flag same-day testing code combinations and automatically append Modifier XE or 59 prior to claim generation."
            },
            "p2_t4": {
                "label": "Implement Telehealth Modifier Mapping (Virtual Feedback)",
                "policy": "MDHHS Telehealth Billing Guidelines & Commercial Payer Rules: Mandates correct modifiers and Place of Service codes for virtual sessions.",
                "target": "100% compliance with virtual clinical feedback coding",
                "desc": "Review virtual CPT 96130 feedback sessions to ensure modifiers 95/GT and location markers POS 02 (telehealth home) or 10 are aligned.",
                "rationale": "Missing telehealth modifiers or incorrect POS codes cause immediate claim rejections, artificially depressing realization rates.",
                "remediation": "Configure the EHR telehealth video module to auto-generate and attach the correct virtual POS and 95 modifier when clinical feedback is delivered via the clinic's digital interface."
            }
        }
    },
    "Phase 3": {
        "title": "Phase 3: Sustainability (Days 61–90)",
        "objective": "Build long-term quality monitoring systems and establish structured diagnostic triage pathways.",
        "rationale": "Ensure that the changes made during the 90 days are sustainable. This phase implements the Stepped-Care model to manage waitlists and designs a live KPI dashboard to track clinical and financial trends.",
        "strengths_overlay": {
            "title": "🧠 CliftonStrengths Strategy: Strategic®",
            "guide": "Deploy Strategic to synthesize multi-source audit findings, billing denial rates, and clinical turnaround metrics into a unified, forward-looking roadmap. This roadmap guides executive decisions on capital investments and ensures long-term regulatory alignment.",
            "examples": [
                "**Strategic in Action (Task 3.1)**: Translates the financial overhead analysis of diagnostic kits and software into a business-case proposal for the executive board, successfully justifying the capital budget to transition to a fully digital platform.",
                "**Strategic in Action (Task 3.2)**: Anticipates potential future changes in Medicaid policies, structuring the EHR KPI dashboard to capture adaptable, cost-based data essential for future rate-rebasing."
            ]
        },
        "tasks": {
            "p3_t1": {
                "label": "Implement Stepped-Care Assessment Clinical Pathway",
                "policy": "SAMHSA CCBHC Core Service #2: Screening, Assessment, and Diagnosis. Requires the optimized allocation of clinical resources.",
                "target": "100% of testing referrals triaged through the new algorithm",
                "desc": "Deploy a clinical screening algorithm that filters low-acuity cases using brief screenings (CPT 96127) at intake, reserving intensive batteries for complex differential diagnosis.",
                "rationale": "Conducting multi-day diagnostic testing for low-acuity referrals wastes psychologist capacity, driving up waitlists for high-acuity SMI/SED populations.",
                "remediation": "Develop and approve the Stepped-Care Assessment clinical algorithm, establishing a strict diagnostic intake screen to preserve testing resources."
            },
            "p3_t2": {
                "label": "Configure EHR-Integrated Assessment KPI Dashboard",
                "policy": "CCBHC Continuous Quality Improvement (CQI) Plan: Demands high-fidelity, data-driven performance monitoring.",
                "target": "Live dashboard tracking 5 core clinical-financial metrics",
                "desc": "Coordinate with IT to build a Business Intelligence dashboard inside the EHR tracking referral volume, report turnaround time (TAT), denials, waitlists, and cost.",
                "rationale": "A lack of ongoing, visual tracking tools leads to unrecognized bottlenecks and billing errors, resulting in compounding financial and operational regressions.",
                "remediation": "Coordinate with IT to configure a live, EHR-integrated Business Intelligence dashboard that gives management immediate visibility over clinician performance and claims denials."
            },
            "p3_t3": {
                "label": "Package 'State of Psychological Testing' Executive Appraisal",
                "policy": "MDHHS Demonstration Guidelines & SAMHSA Certification Criteria: Requires documented administrative and clinical evaluations.",
                "target": "Formal submission and presentation to the Executive Board",
                "desc": "Assemble all baseline chart audits, modifier denial rates, and kit cost overhead analyses into a formalized Executive Appraisal Report.",
                "rationale": "Omission of documented appraisal findings violates state certification rules and limits the agency's ability to justify cost-based rate rebasing in future demonstration years.",
                "remediation": "Synthesize all Phase I and II findings into the formalized executive report, securing final signatures from clinical and financial leadership."
            },
            "p3_t4": {
                "label": "Secure Approval for 12-Month Strategic Optimization Roadmap",
                "policy": "CCBHC Certification Program Requirement #6: Strategic Planning and Capital Investment.",
                "target": "Executive board consensus and approved budget allocation",
                "desc": "Present the completed 12-month strategic roadmap to the executive board, detailing necessary capital investments (EHR digital scoring integrations).",
                "rationale": "Failure to plan for long-term capital investments results in operational stagnation, persistent clinician burnout, and unresolved financial leakage.",
                "remediation": "Present the 12-month roadmap to the executive board to secure budget allocation and strategic alignment for the top three operational priorities."
            }
        }
    }
}

# ==============================================================================
# STATE MANAGEMENT
# ==============================================================================
if "audit_v5_states" not in st.session_state:
    st.session_state.audit_v5_states = {}
    for phase_key, phase_val in audit_metadata.items():
        for task_key in phase_val["tasks"].keys():
            st.session_state.audit_v5_states[task_key] = "Pending"

# ==============================================================================
# VIEWPORT & NAVIGATION
# Optimized drop-down selector for high-resolution mobile views
# ==============================================================================
active_view = st.selectbox(
    "SELECT VIEWPORT:",
    ["Phase 1: Discovery", "Phase 2: Optimization", "Phase 3: Sustainability", "Progress & Findings Report"],
    index=0
)

# ==============================================================================
# PHASE 1: DISCOVERY VIEW
# ==============================================================================
if active_view == "Phase 1: Discovery":
    st.markdown('<div class="neon-divider"></div>', unsafe_allow_html=True)
    st.markdown(f"### **{audit_metadata['Phase 1']['title']}**")
    
    # Phase popover
    with st.popover("🔬 VIEW SYSTEM DIAGNOSTIC BLUEPRINT"):
        st.markdown('<div class="popover-header">PHASE I STRATEGIC OBJECTIVE</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="popover-body">{audit_metadata["Phase 1"]["objective"]}<br><br><strong>Why This Matters:</strong> {audit_metadata["Phase 1"]["rationale"]}</div>', unsafe_allow_html=True)
        
    st.write("Perform real-time compliance audits. Tap info buttons to view detailed clinical rationales.")

    phase_tasks = audit_metadata["Phase 1"]["tasks"]
    for t_key, t_val in phase_tasks.items():
        st.markdown('<div class="scientific-card">', unsafe_allow_html=True)
        
        # Grid layout for badges & info popover
        col_badge, col_info = st.columns([3, 1])
        with col_badge:
            st.markdown(f'<div class="badge-policy">{t_val["policy"]}</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="badge-target">KPI: {t_val["target"]}</div>', unsafe_allow_html=True)
        with col_info:
            with st.popover("[INFO]"):
                st.markdown('<div class="popover-header">TASK DIAGNOSTICS & RATIONALE</div>', unsafe_allow_html=True)
                st.markdown(f'<div class="popover-body"><strong>Task:</strong> {t_val["desc"]}<br><br><strong>Appraisal Rationale:</strong> {t_val["rationale"]}</div>', unsafe_allow_html=True)
                
        st.markdown(f"**{t_val['label']}**")
        
        # State Selector
        curr_status = st.session_state.audit_v5_states[t_key]
        status_opts = ["Pending", "Compliant", "Outside of Compliance"]
        status_idx = status_opts.index(curr_status)
        
        selected_status = st.radio(
            f"Status for {t_key}",
            status_opts,
            index=status_idx,
            key=f"radio_{t_key}",
            horizontal=True,
            label_visibility="collapsed"
        )
        
        # Save state
        st.session_state.audit_v5_states[t_key] = selected_status
        
        # Render Remediation on Demand
        if selected_status == "Outside of Compliance":
            st.markdown(
                f'<div class="remedy-alert-box">'
                f'⚠️ <strong>REMEDIATION DIRECTIVE:</strong> {t_val["remediation"]}'
                f'</div>',
                unsafe_allow_html=True
            )
            
        st.markdown('</div>', unsafe_allow_html=True)
        
    st.markdown('<div class="neon-divider"></div>', unsafe_allow_html=True)
    
    # CliftonStrengths Overlay
    strengths_info = audit_metadata["Phase 1"]["strengths_overlay"]
    st.markdown(f"#### **{strengths_info['title']}**")
    st.write(strengths_info["guide"])
    for ex in strengths_info["examples"]:
        st.markdown(f"• {ex}")

# ==============================================================================
# PHASE 2: OPTIMIZATION VIEW
# ==============================================================================
elif active_view == "Phase 2: Optimization":
    st.markdown('<div class="neon-divider"></div>', unsafe_allow_html=True)
    st.markdown(f"### **{audit_metadata['Phase 2']['title']}**")
    
    # Phase popover
    with st.popover("🔬 VIEW SYSTEM DIAGNOSTIC BLUEPRINT"):
        st.markdown('<div class="popover-header">PHASE II STRATEGIC OBJECTIVE</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="popover-body">{audit_metadata["Phase 2"]["objective"]}<br><br><strong>Why This Matters:</strong> {audit_metadata["Phase 2"]["rationale"]}</div>', unsafe_allow_html=True)
        
    # CARRYOVER CHECKS
    p1_non_compliant = [tk for tk in audit_metadata["Phase 1"]["tasks"].keys() if st.session_state.audit_v5_states[tk] == "Outside of Compliance"]
    if p1_non_compliant:
        st.markdown('<div class="critical-cascade">', unsafe_allow_html=True)
        st.markdown("🚨 <strong>CRITICAL CARRYOVER ALERT: UNRESOLVED PHASE I RISKS DETECTED!</strong>", unsafe_allow_html=True)
        st.write("The following baseline components remain out of compliance, directly threatening the validity of Phase II operational audits:")
        for tk in p1_non_compliant:
            st.markdown(f"• **{audit_metadata['Phase 1']['tasks'][tk]['label']}**")
        st.markdown("</div>", unsafe_allow_html=True)
    else:
        st.markdown('<div style="background-color: rgba(34, 197, 94, 0.08); padding: 12px; border-radius: 12px; border-left: 5px solid #22c55e; border: 1px solid rgba(34, 197, 94, 0.2); margin-bottom: 16px; font-size: 11.5px; color: #22c55e;">✓ <strong>All Phase I baselines are verified and compliant.</strong> Transitioning cleanly into Phase II operational audits.</div>', unsafe_allow_html=True)

    phase_tasks = audit_metadata["Phase 2"]["tasks"]
    for t_key, t_val in phase_tasks.items():
        st.markdown('<div class="scientific-card">', unsafe_allow_html=True)
        
        col_badge, col_info = st.columns([3, 1])
        with col_badge:
            st.markdown(f'<div class="badge-policy">{t_val["policy"]}</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="badge-target">KPI: {t_val["target"]}</div>', unsafe_allow_html=True)
        with col_info:
            with st.popover("[INFO]"):
                st.markdown('<div class="popover-header">TASK DIAGNOSTICS & RATIONALE</div>', unsafe_allow_html=True)
                st.markdown(f'<div class="popover-body"><strong>Task:</strong> {t_val["desc"]}<br><br><strong>Appraisal Rationale:</strong> {t_val["rationale"]}</div>', unsafe_allow_html=True)
                
        st.markdown(f"**{t_val['label']}**")
        
        curr_status = st.session_state.audit_v5_states[t_key]
        status_opts = ["Pending", "Compliant", "Outside of Compliance"]
        status_idx = status_opts.index(curr_status)
        
        selected_status = st.radio(
            f"Status for {t_key}",
            status_opts,
            index=status_idx,
            key=f"radio_{t_key}",
            horizontal=True,
            label_visibility="collapsed"
        )
        
        st.session_state.audit_v5_states[t_key] = selected_status
        
        if selected_status == "Outside of Compliance":
            st.markdown(
                f'<div class="remedy-alert-box">'
                f'⚠️ <strong>REMEDIATION DIRECTIVE:</strong> {t_val["remediation"]}'
                f'</div>',
                unsafe_allow_html=True
            )
            
        st.markdown('</div>', unsafe_allow_html=True)
        
    st.markdown('<div class="neon-divider"></div>', unsafe_allow_html=True)
    
    # CliftonStrengths Overlay
    strengths_info = audit_metadata["Phase 2"]["strengths_overlay"]
    st.markdown(f"#### **{strengths_info['title']}**")
    st.write(strengths_info["guide"])
    for ex in strengths_info["examples"]:
        st.markdown(f"• {ex}")

# ==============================================================================
# PHASE 3: SUSTAINABILITY VIEW
# ==============================================================================
elif active_view == "Phase 3: Sustainability":
    st.markdown('<div class="neon-divider"></div>', unsafe_allow_html=True)
    st.markdown(f"### **{audit_metadata['Phase 3']['title']}**")
    
    # Phase popover
    with st.popover("🔬 VIEW SYSTEM DIAGNOSTIC BLUEPRINT"):
        st.markdown('<div class="popover-header">PHASE III STRATEGIC OBJECTIVE</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="popover-body">{audit_metadata["Phase 3"]["objective"]}<br><br><strong>Why This Matters:</strong> {audit_metadata["Phase 3"]["rationale"]}</div>', unsafe_allow_html=True)
        
    # CARRYOVER CHECKS
    p2_non_compliant = [tk for tk in audit_metadata["Phase 2"]["tasks"].keys() if st.session_state.audit_v5_states[tk] == "Outside of Compliance"]
    if p2_non_compliant:
        st.markdown('<div class="critical-cascade">', unsafe_allow_html=True)
        st.markdown("🚨 <strong>CRITICAL CARRYOVER ALERT: UNRESOLVED PHASE II GAPS DETECTED!</strong>", unsafe_allow_html=True)
        st.write("The following operational gaps remain unresolved, directly impacting the deployment of long-term sustainable recommendations:")
        for tk in p2_non_compliant:
            st.markdown(f"• **{audit_metadata['Phase 2']['tasks'][tk]['label']}**")
        st.markdown("</div>", unsafe_allow_html=True)
    else:
        st.markdown('<div style="background-color: rgba(34, 197, 94, 0.08); padding: 12px; border-radius: 12px; border-left: 5px solid #22c55e; border: 1px solid rgba(34, 197, 94, 0.2); margin-bottom: 16px; font-size: 11.5px; color: #22c55e;">✓ <strong>All Phase II analytical objectives are compliant.</strong> Synthesizing final strategic roadmaps.</div>', unsafe_allow_html=True)

    phase_tasks = audit_metadata["Phase 3"]["tasks"]
    for t_key, t_val in phase_tasks.items():
        st.markdown('<div class="scientific-card">', unsafe_allow_html=True)
        
        col_badge, col_info = st.columns([3, 1])
        with col_badge:
            st.markdown(f'<div class="badge-policy">{t_val["policy"]}</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="badge-target">KPI: {t_val["target"]}</div>', unsafe_allow_html=True)
        with col_info:
            with st.popover("[INFO]"):
                st.markdown('<div class="popover-header">TASK DIAGNOSTICS & RATIONALE</div>', unsafe_allow_html=True)
                st.markdown(f'<div class="popover-body"><strong>Task:</strong> {t_val["desc"]}<br><br><strong>Appraisal Rationale:</strong> {t_val["rationale"]}</div>', unsafe_allow_html=True)
                
        st.markdown(f"**{t_val['label']}**")
        
        curr_status = st.session_state.audit_v5_states[t_key]
        status_opts = ["Pending", "Compliant", "Outside of Compliance"]
        status_idx = status_opts.index(curr_status)
        
        selected_status = st.radio(
            f"Status for {t_key}",
            status_opts,
            index=status_idx,
            key=f"radio_{t_key}",
            horizontal=True,
            label_visibility="collapsed"
        )
        
        st.session_state.audit_v5_states[t_key] = selected_status
        
        if selected_status == "Outside of Compliance":
            st.markdown(
                f'<div class="remedy-alert-box">'
                f'⚠️ <strong>REMEDIATION DIRECTIVE:</strong> {t_val["remediation"]}'
                f'</div>',
                unsafe_allow_html=True
            )
            
        st.markdown('</div>', unsafe_allow_html=True)
        
    st.markdown('<div class="neon-divider"></div>', unsafe_allow_html=True)
    
    # CliftonStrengths Overlay
    strengths_info = audit_metadata["Phase 3"]["strengths_overlay"]
    st.markdown(f"#### **{strengths_info['title']}**")
    st.write(strengths_info["guide"])
    for ex in strengths_info["examples"]:
        st.markdown(f"• {ex}")

# ==============================================================================
# PROGRESS & FINDINGS REPORT (EXECUTIVE DASHBOARD)
# ==============================================================================
elif active_view == "Progress & Findings Report":
    st.markdown('<div class="neon-divider"></div>', unsafe_allow_html=True)
    
    # Executive Header
    st.markdown("""
    <div style="text-align: center; border: 2px solid rgba(34, 197, 94, 0.4); padding: 16px; border-radius: 16px; background-color: rgba(26, 12, 48, 0.95); margin-bottom: 20px; box-shadow: 0 0 20px rgba(34, 197, 94, 0.15);">
        <h3 style="color: #FFFFFF; margin: 0; font-weight: 900; font-family: monospace; font-size:15px; letter-spacing: 1.5px; text-shadow: 0 0 10px rgba(34, 197, 94, 0.5);">CNS HEALTHCARE PSYCHOLOGICAL SERVICES</h3>
        <h4 style="color: #22c55e; margin: 4px 0 0 0; font-weight: 700; font-family: monospace; font-size:11px; letter-spacing: 1px;">EXECUTIVE PROGRESS & FINDINGS REPORT</h4>
        <p style="color: #E1BEE7; font-size: 9.5px; margin: 6px 0 0 0; font-family: monospace; line-height: 1.3;">Prepared for: Provider Supervisors & Executive Board<br>Auditor: Dr. Scott Niewinski, Psy.D., Manager of Psychological Services</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Calculate counts
    total_tasks = 0
    compliant_list = []
    non_compliant_list = []
    pending_list = []
    
    for p_key, p_val in audit_metadata.items():
        for t_key, t_val in p_val["tasks"].items():
            total_tasks += 1
            status = st.session_state.audit_v5_states[t_key]
            task_entry = {"info": t_val, "phase": p_val["title"]}
            if status == "Compliant":
                compliant_list.append(task_entry)
            elif status == "Outside of Compliance":
                non_compliant_list.append(task_entry)
            else:
                pending_list.append(task_entry)
                
    comp_rate = (len(compliant_list) / total_tasks) * 100 if total_tasks > 0 else 0
    
    # Key Metrics Display
    col_pct, col_non = st.columns(2)
    with col_pct:
        st.metric("COMPLIANCE RATE", f"{comp_rate:.1f}%", f"{len(compliant_list)}/{total_tasks} Verified")
    with col_non:
        st.metric("ACTIVE OUTSTANDING GAPS", f"{len(non_compliant_list)}", delta="- Action Remediation Required", delta_color="inverse")
        
    st.progress(len(compliant_list) / total_tasks if total_tasks > 0 else 0)
    st.markdown('<div class="neon-divider"></div>', unsafe_allow_html=True)
    
    st.markdown("### **📋 APPRAISAL STATUS BREAKDOWN**")
    
    # 1. COMPLIANT ITEMS
    if compliant_list:
        with st.expander("🟢 VERIFIED STRENGTHS & COMPLIANT AREAS", expanded=True):
            for item in compliant_list:
                st.markdown(f"**✓ {item['info']['label']}**")
                st.markdown(f"<span style='font-size:10px; color:#22c55e; font-family: monospace;'>Phase: {item['phase']} | Policy: {item['info']['policy']}</span>", unsafe_allow_html=True)
                st.markdown("<hr style='margin: 8px 0; border: none; border-bottom: 1px solid rgba(255,255,255,0.08);'>", unsafe_allow_html=True)
                
    # 2. PENDING ITEMS
    if pending_list:
        with st.expander("🟡 PENDING AUDIT ITEMS"):
            for item in pending_list:
                st.markdown(f"**• {item['info']['label']}**")
                st.markdown(f"<span style='font-size:10px; color:#FFE082; font-family: monospace;'>Phase: {item['phase']} | Policy: {item['info']['policy']}</span>", unsafe_allow_html=True)
                st.markdown("<hr style='margin: 8px 0; border: none; border-bottom: 1px solid rgba(255,255,255,0.08);'>", unsafe_allow_html=True)

    # 3. NON-COMPLIANT GAPS & MATRIX
    if non_compliant_list:
        st.markdown("### **🔴 ACTIVE RISK & REMEDIATION MATRIX**")
        st.write("The following items are out of compliance and represent active regulatory, financial, or licensing risks:")
        
        for item in non_compliant_list:
            st.markdown(f"<div style='border: 1px solid rgba(239, 68, 68, 0.4); border-radius: 12px; padding: 14px; margin-bottom: 12px; background-color: rgba(239, 68, 68, 0.08);'>", unsafe_allow_html=True)
            st.markdown(f"<strong style='color:#FCA5A5; font-family: monospace;'>[GAP] {item['info']['label']}</strong><br><span style='font-size:10px; color:#E1BEE7;'>Phase: {item['phase']}</span>", unsafe_allow_html=True)
            st.markdown(f"<p style='margin: 8px 0 4px 0; font-size:12px; color: #F3F4F6;'><strong>Governing Directive:</strong> {item['info']['policy']}</p>", unsafe_allow_html=True)
            st.markdown(f"<p style='margin: 4px 0 4px 0; font-size:12px; color: #22c55e; font-family: monospace;'><strong>Target Metric:</strong> {item['info']['target']}</p>", unsafe_allow_html=True)
            st.markdown(f"<p style='margin: 4px 0 4px 0; font-size:12px; color: #FFCDD2;'><strong>Systemic Rationale:</strong> {item['info']['rationale']}</p>", unsafe_allow_html=True)
            
            st.markdown(
                f'<div class="remedy-alert-box">'
                f'🛠️ <strong>REMEDIATION DIRECTIVE:</strong> {item["info"]["remediation"]}'
                f'</div>',
                unsafe_allow_html=True
            )
            st.markdown("</div>", unsafe_allow_html=True)
    else:
        if len(compliant_list) == total_tasks:
            st.success("🎉 Spectacular! All 90-Day appraisal deliverables are verified as 100% compliant with LARA, MDHHS, and CARF guidelines. No active risks detected.")

# Sticky Scientific Footer
st.markdown("<hr style='margin-top: 30px; border-color: rgba(34, 197, 94, 0.25);'>", unsafe_allow_html=True)
st.markdown(
    '<div style="font-size:9px; color:#808080; text-align:center; padding-bottom:15px; font-family: monospace;">'
    'CNS Healthcare Appraisal Systems • Grounded strictly in "90-Day Psychological Services Appraisal Plan.docx"</div>',
    unsafe_allow_html=True
)
