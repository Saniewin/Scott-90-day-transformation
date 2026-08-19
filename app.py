import streamlit as st

# Set Streamlit Page Configuration - optimized for Samsung Galaxy S26 Ultra (high-res vertical viewport)
st.set_page_config(
    page_title="90-Day Psychological Services Appraisal Portal",
    page_icon="🧬",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Custom CSS for Dark Purple, Digital Scientific & Matrix-inspired theme (Purple, Green, and White color scheme)
st.markdown("""
<style>
    /* Main body background & Scientific-Digital canvas layout */
    .stApp {
        background: radial-gradient(circle at center, #1E052D 0%, #0C0117 100%) !important;
        color: #FFFFFF !important;
        font-family: 'Segoe UI', -apple-system, BlinkMacSystemFont, Roboto, sans-serif !important;
        position: relative;
    }
    
    /* Glowing digital grid overlay */
    .stApp::before {
        content: "";
        position: absolute;
        top: 0; left: 0; width: 100%; height: 100%;
        background-image: 
            linear-gradient(rgba(0, 255, 102, 0.015) 1px, transparent 1px),
            linear-gradient(90deg, rgba(0, 255, 102, 0.015) 1px, transparent 1px);
        background-size: 25px 20px;
        pointer-events: none;
        z-index: 0;
    }

    /* Device frame mockup for Samsung S26 Ultra centered canvas */
    @media (min-width: 450px) {
        .block-container {
            max-width: 440px !important;
            padding: 24px !important;
            background: rgba(18, 4, 30, 0.95) !important;
            border-radius: 40px !important;
            box-shadow: 0 0 40px rgba(0, 255, 102, 0.15) !important;
            margin-top: 15px !important;
            margin-bottom: 25px !important;
            border: 4px solid #4E146F !important; /* Deep Purple Frame */
            position: relative;
            z-index: 1;
        }
    }
    
    /* Scientific holographic card styling */
    .app-card {
        background: rgba(30, 8, 48, 0.75) !important;
        border: 1px solid rgba(0, 255, 102, 0.2) !important;
        border-radius: 16px !important;
        padding: 16px !important;
        margin-bottom: 16px !important;
        box-shadow: 0 4px 30px rgba(0, 0, 0, 0.5) !important;
        backdrop-filter: blur(10px) !important;
        transition: all 0.3s ease !important;
    }
    .app-card:hover {
        border-color: rgba(0, 255, 102, 0.6) !important;
        box-shadow: 0 0 15px rgba(0, 255, 102, 0.25) !important;
    }
    
    /* Glowing typography headers */
    .app-title {
        font-size: 24px !important;
        font-weight: 900 !important;
        color: #FFFFFF !important;
        text-shadow: 0 0 15px rgba(0, 255, 102, 0.6) !important;
        text-align: center !important;
        font-family: 'Courier New', Courier, monospace !important;
        letter-spacing: 1px !important;
        margin-bottom: 2px !important;
    }
    
    .app-subtitle {
        font-size: 11px !important;
        color: #00FF66 !important; /* Matrix/Vibrant Green */
        text-align: center !important;
        font-family: 'Courier New', Courier, monospace !important;
        letter-spacing: 2px !important;
        margin-bottom: 24px !important;
        text-transform: uppercase !important;
        font-weight: bold !important;
    }
    
    /* Policy and Target digital readouts */
    .policy-label {
        font-size: 11px;
        font-weight: 700;
        background-color: rgba(78, 20, 111, 0.4); /* Purple tint */
        color: #E1BEE7; /* Light Purple text */
        padding: 4px 10px;
        border-radius: 8px;
        display: inline-block;
        margin-bottom: 8px;
        border: 1px solid rgba(78, 20, 111, 0.6);
        font-family: monospace;
    }
    
    .target-label {
        font-size: 11px;
        font-weight: 700;
        background-color: rgba(0, 255, 102, 0.08); /* Green tint */
        color: #00FF66; /* Vibrant Green text */
        padding: 4px 10px;
        border-radius: 8px;
        display: inline-block;
        margin-bottom: 8px;
        margin-left: 4px;
        border: 1px solid rgba(0, 255, 102, 0.3);
        font-family: monospace;
    }

    /* Customized Popover Button (Scientific Bubble Node) */
    div.stPopover > button {
        background-color: rgba(0, 255, 102, 0.05) !important;
        border: 1px solid rgba(0, 255, 102, 0.3) !important;
        color: #00FF66 !important;
        border-radius: 8px !important;
        font-size: 10px !important;
        font-family: 'Courier New', Courier, monospace !important;
        text-transform: uppercase !important;
        letter-spacing: 1px !important;
        padding: 2px 8px !important;
        transition: all 0.2s ease !important;
        box-shadow: 0 0 5px rgba(0, 255, 102, 0.1) !important;
    }
    div.stPopover > button:hover {
        background-color: rgba(0, 255, 102, 0.15) !important;
        border-color: #00FF66 !important;
        box-shadow: 0 0 10px rgba(0, 255, 102, 0.4) !important;
        color: #FFFFFF !important;
    }
    
    /* Dialog/Popover Inner styling */
    .bubble-header {
        font-size: 14px;
        color: #00FF66;
        font-family: monospace;
        font-weight: bold;
        border-bottom: 1px solid rgba(0, 255, 102, 0.3);
        padding-bottom: 4px;
        margin-bottom: 8px;
    }
    
    .bubble-policy {
        font-size: 11px;
        color: #E1BEE7;
        background: rgba(78, 20, 111, 0.3);
        padding: 6px;
        border-radius: 6px;
        border-left: 3px solid #9C27B0;
        margin-bottom: 8px;
    }

    /* Standardized remedial and alert styles */
    .remedy-banner {
        background-color: rgba(251, 192, 45, 0.1) !important;
        border-left: 4px solid #FBC02D !important;
        border: 1px solid rgba(251, 192, 45, 0.25) !important;
        padding: 12px !important;
        border-radius: 8px !important;
        margin-top: 10px !important;
        font-size: 12px !important;
        color: #FFE082 !important;
    }
    
    .cascade-alert {
        background-color: rgba(211, 47, 47, 0.12) !important;
        border: 1px solid rgba(211, 47, 47, 0.3) !important;
        border-left: 5px solid #D32F2F !important;
        padding: 12px !important;
        border-radius: 12px !important;
        margin-bottom: 16px !important;
        font-size: 12px !important;
        color: #FFCDD2 !important;
    }

    /* Scientific matrix-like dividers */
    .digital-divider {
        height: 2px;
        background: linear-gradient(to right, rgba(0, 255, 102, 0.5), rgba(78, 20, 111, 0.8), transparent);
        border: none;
        margin: 15px 0;
    }
</style>
""", unsafe_allow_html=True)

# Title & Digital Metadata Header
st.markdown('<div class="app-title">SYS_DIAGNOSTIC_PORTAL</div>', unsafe_allow_html=True)
st.markdown('<div class="app-subtitle">CNS PSYCH_SERVICES 90-DAY APPRAISAL v4.0</div>', unsafe_allow_html=True)

# Structured objectives, tasks, targets, and policies strictly from the 90-Day Psychological Services Appraisal Plan.docx
audit_db = {
    "Phase I": {
        "title": "Phase I: Baseline Discovery (Days 1–30)",
        "diagnostic_rationale": "Focuses on regulatory discovery and clinical baseline mapping across Wayne, Oakland, and Macomb clinics. Under the CCBHC model, establishing an empirical clinical baseline is critical prior to system re-engineering.",
        "tasks": {
            "p1_t1": {
                "label": "Verify LLP Supervision Logs",
                "policy_short": "MCL 333.18223 & LARA Rule 338.2569",
                "policy_long": "Michigan Public Health Code MCL 333.18223 & LARA Rule 338.2569: Dictates that Limited License Psychologists (LLPs) receive at least 4 hours/month face-to-face supervision on Form LARA/BPL Rev 6/25.",
                "target": "100% compliant LARA logs",
                "desc_long": "Examine supervisory files for all LLPs and Temporary LLPs. Verify that psychology logs are signed by fully Licensed Psychologists (LPs) and that LPs co-sign LLP-written notes in the EHR before billing release.",
                "rationale": "Unsupervised LLP clinical activity is a direct violation of licensure law, exposing CNS Healthcare to severe state disciplinary actions and catastrophic retroactive Medicaid recoupments for billed encounters.",
                "remediation": "Immediately suspend unsupervised LLP billing. Relocate LLP logs to a centralized, automated HR portal. Hardcode EHR co-signature routing blocks to prevent claim release until LP sign-off is completed."
            },
            "p1_t2": {
                "label": "Audit 30 Completed Charts",
                "policy_short": "CPT 96130 Interactive Feedback",
                "policy_long": "CPT Manual Definitions & Medicare LCD guidelines: Under CPT 96130, first-hour evaluation requires documented clinical decision-making and face-to-face interactive feedback with the client or caregiver.",
                "target": "100% documented feedback in EHR",
                "desc_long": "Conduct a manual, randomized chart extraction of 30 recently completed evaluations. Scrutinize time logs to ensure CPT 96130 contains at least 31 minutes of provider time and that technician-administered codes (96138) are correctly segregated.",
                "rationale": "Billing CPT 96130 without documenting interactive feedback is a billing infraction. Failing this audit indicates high exposure to Medicaid/Commercial payer recoupments and Fraud, Waste, and Abuse (FWA) scrutiny.",
                "remediation": "Perform billing self-disclosures on missing logs. Deploy mandatory EHR evaluation templates that physically prevent note-locking until a timestamped 'Interactive Feedback and Clinical Decision Making' section is filled."
            },
            "p1_t3": {
                "label": "Shadow Triage Workflows",
                "policy_short": "SAMHSA CCBHC Access velocity",
                "policy_long": "SAMHSA 2023 CCBHC Certification Criteria: Requires timely, unimpeded access to care (such as routine evaluation initiation within 10-14 days and urgent care within 1 business day).",
                "target": "Map 100% of pipeline lifecycle",
                "desc_long": "Observe intake and triage personnel. Track a psychological testing referral from initial request through the EHR queue and map staff interactions with PIHP prior authorization portals (like MHWIN for DWIHN and CHAMPS).",
                "rationale": "Extended waiting periods for diagnostic testing delay treatment entry. This can trigger MDHHS Corrective Action Plans (CAPs) and jeopardize CCBHC certification.",
                "remediation": "Construct process maps of administrative handoffs, identify delays within PIHP portals, and establish streamlined scheduling protocols to meet access benchmarks."
            },
            "p1_t4": {
                "label": "Survey Clinical Stakeholders",
                "policy_short": "CARF Report Utility Standards",
                "policy_long": "CARF Accreditation Standards & CCBHC care coordination: Demands that clinical assessments have recognized utility and directly integrate into the Person-Centered Plan (PCP).",
                "target": ">80% clinician response rate",
                "desc_long": "Send digital surveys and conduct interviews with internal psychiatric prescribers, outpatient therapists, and external regional stakeholders to grade the readability, diagnostic clarity, and utility of clinical reports.",
                "rationale": "If diagnostic reports fail to influence the PCP, the testing operates as an isolated, high-cost administrative exercise rather than a therapeutic driver.",
                "remediation": "Analyze qualitative gaps in report readability. Standardize report structures to mandate a summary block containing actionable, interdisciplinary recommendations."
            }
        }
    },
    "Phase II": {
        "title": "Phase II: Operational Analysis (Days 31–60)",
        "diagnostic_rationale": "Transition from discovery to data-driven operational analysis. This phase mathematically quantifies workflow bottlenecks, coding leaks, and utilization management gaps across the 12-month historical claims.",
        "tasks": {
            "p2_t1": {
                "label": "RCM Claims Denial Audit",
                "policy_short": "RCM 835 Remittance Guidelines",
                "policy_long": "Revenue Cycle Management Standard Billing: standardizes claims processing based on coding accuracy, bundling guidelines, and medical necessity.",
                "target": "Identify top 3 testing denial codes",
                "desc_long": "Collaborate with the CNS billing department to extract a 12-month historical database of claims involving CPT codes 96130–96139. Segment and audit denial codes like CO-97 (bundled services) and CO-50 (medical necessity).",
                "rationale": "Unresolved clearinghouse denials represent a major source of revenue leakage and impose an excessive administrative burden on staff doing manual retroactive billing appeals.",
                "remediation": "Extract the 12-month 835 remittance data, isolate clearinghouse edit rules causing rejections, and correct structural coding errors at the point of scheduling."
            },
            "p2_t2": {
                "label": "Modifier 59 / XE Audit",
                "policy_short": "CMS NCCI Modifier Edits",
                "policy_long": "CMS National Correct Coding Initiative (NCCI) Edits: Prohibits billing provider-administered testing (96136) and technician-administered testing (96138) on the same date for the same consumer without distinct modifiers.",
                "target": "100% same-day billing accuracy",
                "desc_long": "Review same-day clinical testing entries to verify if Billing Modifier 59 (distinct procedural service) or Modifier XE (separate encounter) are correctly applied to prevent automated rejections.",
                "rationale": "Same-day testing administration by a psychologist and a technician automatically triggers a CMS NCCI denial, locking up revenue and leading to billing backlog.",
                "remediation": "Hardcode NCCI validation rules within the EHR's billing module to automatically append Modifier XE/59 when same-day dual-provider testing encounters are logged."
            },
            "p2_t3": {
                "label": "Telehealth Modifier Audit",
                "policy_short": "MDHHS Telehealth Billing Rules",
                "policy_long": "MDHHS Telehealth Policy: Requires virtual psychological services to append specific Modifiers (95 or GT) and Place of Service codes (POS 02 or 10) to secure valid reimbursement.",
                "target": "100% compliant virtual feedback coding",
                "desc_long": "Audit virtual CPT 96130 feedback sessions to ensure modifiers 95/GT and location markers POS 02 (telehealth home) or 10 are aligned with patient location.",
                "rationale": "Missing telehealth modifiers or incorrect POS codes cause immediate claim rejections, artificially depressing realization rates.",
                "remediation": "Configure the EHR telehealth video module to auto-generate and attach the correct virtual POS and 95 modifier when clinical feedback is delivered via the clinic's digital interface."
            },
            "p2_t4": {
                "label": "PA Limit Tracking",
                "policy_short": "Medicaid Prior Authorization Rules",
                "policy_long": "Michigan Medicaid Provider Manual: Governs prior authorization limits, thresholds, and tracking policies across regional Prepaid Inpatient Health Plans.",
                "target": "Centralize PA threshold mapping",
                "desc_long": "Evaluate how the department tracks Meridian's 8-hour annual calendar limit before a PA is required, versus DWIHN's requirement for immediate bundled authorization using specialty codes.",
                "rationale": "Failing to track annual testing thresholds or executing testing without securing prior authorization results in complete forfeiture of payment, resulting in uncompensated clinical work.",
                "remediation": "Implement a hard stop in the EHR scheduling system that blocks psychological testing bookings exceeding 8 hours annually unless an active PA number is attached."
            },
            "p2_t5": {
                "label": "Turnaround Time (TAT) Metrics",
                "policy_short": "CARF Access & Timeliness Guidelines",
                "policy_long": "CARF Quality Timelines: Benchmarks clinical report turnaround times to prevent delays in treatment initiation.",
                "target": "Calculate median days from test to signed report",
                "desc_long": "Extract EHR timestamps to measure mean and median Turnaround Times (TAT) from final testing date to final report signature, segmenting the clinician pool to isolate bottlenecks.",
                "rationale": "Extended report TATs delay psychiatric prescriptions and therapeutic interventions, violating CCBHC care coordination standards.",
                "remediation": "Segment EHR timestamp data into three distinct intervals (referral-to-auth, auth-to-testing, testing-to-signed) and counsel outlying clinicians with extended write times."
            },
            "p2_t6": {
                "label": "Financial Overhead Audit",
                "policy_short": "CCBHC PPS Cost Allocation",
                "policy_long": "CCBHC PPS Cost Reporting Guidelines: Mandates tracking material and software expenditures to offset operational costs against flat Prospective Payment System encounter rates.",
                "target": "Establish cost-per-assessment ratio",
                "desc_long": "Review vendor invoices for consumable paper forms and digital scoring platform licenses (Pearson Q-interactive, PARiConnect, WPS) and cross-reference against actual claim volumes.",
                "rationale": "Unmonitored diagnostic kit and licensing expenses create unrecognized department deficits under the flat CCBHC daily payment model.",
                "remediation": "Cross-reference all vendor invoices against Medicaid and PPS revenues to identify high-cost, low-yield testing kits, transitioning entirely to digital scoring to lower overhead."
            }
        }
    },
    "Phase III": {
        "title": "Phase III: Synthesis & Recommendations (Days 61–90)",
        "diagnostic_rationale": "The final phase synthesizes clinical, financial, and regulatory data into an actionable strategic roadmap, establishing permanent quality improvement infrastructure and clinical pathways.",
        "tasks": {
            "p3_t1": {
                "label": "Stepped-Care Protocol Design",
                "policy_short": "SAMHSA CCBHC Core Service #2",
                "policy_long": "SAMHSA CCBHC Core Service #2: Screening, Assessment, and Diagnosis. Requires the optimized allocation of highly trained psychological resources.",
                "target": "Completed clinical triage algorithm",
                "desc_long": "Design a clinical pathway that filters low-acuity cases using brief emotional screenings (CPT 96127) at intake, reserving intensive, multi-hour testing batteries (96130/96136/96138) for complex differential diagnosis.",
                "rationale": "Conducting multi-day diagnostic testing for low-acuity referrals wastes psychologist FTE capacity, driving up waitlists for high-acuity SMI/SED populations.",
                "remediation": "Develop and approve the Stepped-Care Assessment clinical algorithm, establishing a strict diagnostic intake screen to preserve testing resources."
            },
            "p3_t2": {
                "label": "EHR KPI Dashboard",
                "policy_short": "CCBHC CQI Performance Monitoring",
                "policy_long": "CCBHC Continuous Quality Improvement Plan: Demands high-fidelity, data-driven performance monitoring for clinical and financial management.",
                "target": "Track 5 core metrics on a live EHR/BI dashboard",
                "desc_long": "Configure and wireframe a real-time Assessment KPI Dashboard inside the EHR or connected BI platform, tracking weekly referral volume, TAT, denials, waitlist size, and cost.",
                "rationale": "A lack of ongoing, visual tracking tools leads to unrecognized bottlenecks and billing errors, resulting in compounding financial and operational regressions.",
                "remediation": "Coordinate with IT to configure a live, EHR-integrated Business Intelligence dashboard that gives management immediate visibility over clinician performance and claims denials."
            },
            "p3_t3": {
                "label": "Executive Appraisal Report",
                "policy_short": "MDHHS Demonstration Oversight",
                "policy_long": "MDHHS & SAMHSA CCBHC Demonstration Guidelines: Mandates regular, documented clinical and administrative evaluations of certified service lines.",
                "target": "Submit comprehensive report to executive board",
                "desc_long": "Assemble all baseline chart audits, modifier denial rates, and kit cost overhead analyses into a formalized 'State of Psychological Testing' Executive Appraisal Report.",
                "rationale": "Omission of documented appraisal findings violates state certification rules and limits the agency's ability to justify cost-based rate rebasing in future demonstration years.",
                "remediation": "Synthesize all Phase I and II findings into the formalized executive report, securing final signatures from clinical and financial leadership."
            },
            "p3_t4": {
                "label": "12-Month Strategic Roadmap",
                "policy_short": "CCBHC Program Requirement #6",
                "policy_long": "CCBHC Certification Program Requirement #6: Strategic Planning and Capital Investment. Mandates strategic, long-term planning for certified service lines.",
                "target": "Secure leadership approval on top 3 priorities",
                "desc_long": "Present the completed 12-month strategic roadmap to the executive board, detailing necessary capital investments (EHR digital scoring integrations), centralized LARA logs, and CPT modifier training.",
                "rationale": "Failure to plan for long-term capital investments results in operational stagnation, persistent clinician burnout, and unresolved financial leakage.",
                "remediation": "Present the 12-month roadmap to the executive board to secure budget allocation and strategic alignment for the top three operational priorities."
            }
        }
    }
}

# Initialize Session State for audit data
if 'appraisal_audit_v4' not in st.session_state:
    st.session_state.appraisal_audit_v4 = {}
    for phase_id, phase_info in audit_db.items():
        for task_id, task_info in phase_info["tasks"].items():
            st.session_state.appraisal_audit_v4[task_id] = {
                "compliant": True,
                "notes": ""
            }

# Dropdown selector for the S26 Ultra Touch UI
phase_selector = st.selectbox(
    "SELECT VIEWPORT MODE:",
    ["Phase I: Baseline Discovery (Days 1–30)", 
     "Phase II: Operational Analysis (Days 31–60)", 
     "Phase III: Synthesis & Recommendations (Days 61–90)",
     "Progress & Findings Report (Executive Tab)"],
    index=0
)

# ----------------- PHASE I VIEW -----------------
if phase_selector == "Phase I: Baseline Discovery (Days 1–30)":
    st.markdown('<div class="digital-divider"></div>', unsafe_allow_html=True)
    st.markdown(f"### **{audit_db['Phase I']['title']}**")
    
    # Phase overarching info popover (Bubble window)
    with st.popover("🔬 CLICK FOR PHASE I DIAGNOSTIC BLUEPRINT"):
        st.markdown(f'<div class="bubble-header">PHASE I OVERVIEW & OBJECTIVE</div>', unsafe_allow_html=True)
        st.write(audit_db["Phase I"]["diagnostic_rationale"])
    
    st.write("Perform real-time compliance audits. Tap policy badges or [INFO] buttons to reveal detailed scientific rationales.")

    phase_tasks = audit_db["Phase I"]["tasks"]
    for task_id, task_info in phase_tasks.items():
        st.markdown(f'<div class="app-card">', unsafe_allow_html=True)
        
        # Policy badge as a trigger for a popover (Bubble window for policy)
        col_badge, col_pop_task = st.columns([3, 1])
        with col_badge:
            st.markdown(f'<div class="policy-label">{task_info["policy_short"]}</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="target-label">Target: {task_info["target"]}</div>', unsafe_allow_html=True)
        with col_pop_task:
            with st.popover("[INFO]"):
                st.markdown(f'<div class="bubble-header">SYSTEMIC ANALYSIS DETAILS</div>', unsafe_allow_html=True)
                st.markdown(f'<div class="bubble-policy"><strong>Policy Source:</strong> {task_info["policy_long"]}</div>', unsafe_allow_html=True)
                st.write(f"**Operational Task:** {task_info['desc_long']}")
                st.markdown(f'<div style="color:#00FF66; margin-top:8px;"><strong>Appraisal Rationale:</strong> {task_info["rationale"]}</div>', unsafe_allow_html=True)

        st.markdown(f"**{task_info['label']}**")
        
        # Pull current state
        curr_state = st.session_state.appraisal_audit_v4[task_id]["compliant"]
        
        col_lbl, col_sel = st.columns([1, 1])
        with col_lbl:
            st.write("Diagnostic Status:")
        with col_sel:
            status_val = st.radio(
                "Select status",
                ["Compliant", "Non-Compliant"],
                index=0 if curr_state else 1,
                key=f"status_{task_id}",
                horizontal=True,
                label_visibility="collapsed"
            )
        
        # Save to session state
        st.session_state.appraisal_audit_v4[task_id]["compliant"] = (status_val == "Compliant")
        
        # Render remediation instructions if marked Non-Compliant
        if status_val == "Non-Compliant":
            st.markdown(
                f'<div class="remedy-banner">'\
                f'⚠️ <strong>REMEDIATION DIRECTIVE:</strong> {task_info["remediation"]}'\
                f'</div>',\
                unsafe_allow_html=True
            )
            
        st.markdown('</div>', unsafe_allow_html=True)
        
    st.markdown('<div class="digital-divider"></div>', unsafe_allow_html=True)
    st.markdown("#### **🧠 CLIFTONSTRENGTHS: PHASE I LEADERSHIP**")
    st.write("Dr. Scott Niewinski can strategically deploy his dominant talents to drive Phase I implementation:")
    
    with st.expander("🎓 Learner® — Meticulous Chart & LARA Auditing"):
        st.write("Apply the Learner drive to meticulously study licensing regulations and CPT guidelines. Treat the **30-case stratified chart audit** and LARA log review as active, intellectually engaging learning journeys from baseline discovery to full clinical mastery.")
    with st.expander("🎯 Strategic® — Workflow Bottleneck Mapping"):
        st.write("Use the Strategic talent to automatically sort through the clutter of referral workflows. Spot underlying patterns of delay as testing requests move through EHR authorization queues toward PIHP portals.")
    with st.expander("🤝 Individualization® — Tailored LLP Mentoring"):
        st.write("Acknowledge the unique clinical and writing styles of Limited License Psychologists (LLPs). Turn chart audit deficiencies into positive, customized growth plans during supervision sessions rather than issuing standardized reprimands.")
    with st.expander("💡 Ideation® — Designing Triage shadow frameworks"):
        st.write("Brainstorm out-of-the-box, highly engaging shadowing techniques and intake filters that capture baseline qualitative experiences without disrupting ongoing client care.")
    with st.expander("🔍 Intellection® — Deep Root-Cause Compliance Analysis"):
        st.write("Engage in focused, introspective analysis of why supervision logs or documentation loops failed in the past, aiming for sustainable, systemic solutions.")

# ----------------- PHASE II VIEW -----------------
elif phase_selector == "Phase II: Operational Analysis (Days 31–60)":
    st.markdown('<div class="digital-divider"></div>', unsafe_allow_html=True)
    st.markdown(f"### **{audit_db['Phase II']['title']}**")
    
    with st.popover("🔬 CLICK FOR PHASE II DIAGNOSTIC BLUEPRINT"):
        st.markdown(f'<div class="bubble-header">PHASE II OVERVIEW & OBJECTIVE</div>', unsafe_allow_html=True)
        st.write(audit_db["Phase II"]["diagnostic_rationale"])
        
    # CARRYOVER LOGIC: Phase I to Phase II
    phase1_tasks = audit_db["Phase I"]["tasks"]
    p1_non_compliant_keys = [tid for tid in phase1_tasks.keys() if not st.session_state.appraisal_audit_v4[tid]["compliant"]]
    
    if p1_non_compliant_keys:
        st.markdown('<div class="cascade-alert">', unsafe_allow_html=True)
        st.markdown("🚨 <strong>CRITICAL CARRYOVER ALERT: UNRESOLVED PHASE I RISKS DETECTED!</strong>", unsafe_allow_html=True)
        st.write("The following baseline components remain out of compliance, directly threatening the validity of Phase II operational and financial analyses:")
        for tid in p1_non_compliant_keys:
            st.markdown(f"• **{phase1_tasks[tid]['label']}** — *Unresolved risk of licensure disciplinary action or Medicaid recoupment.*")
        st.markdown("</div>", unsafe_allow_html=True)
    else:
        st.markdown('<div style="background-color: rgba(0, 255, 102, 0.08); padding: 12px; border-radius: 12px; border-left: 5px solid #00FF66; border: 1px solid rgba(0, 255, 102, 0.2); margin-bottom: 16px; font-size: 12px; color: #00FF66;">✓ <strong>All Phase I baselines are verified and compliant.</strong> Transitioning cleanly into Phase II operational audits.</div>', unsafe_allow_html=True)

    phase_tasks = audit_db["Phase II"]["tasks"]
    for task_id, task_info in phase_tasks.items():
        st.markdown(f'<div class="app-card">', unsafe_allow_html=True)
        
        # Policy badge and popover
        col_badge, col_pop_task = st.columns([3, 1])
        with col_badge:
            st.markdown(f'<div class="policy-label">{task_info["policy_short"]}</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="target-label">Target: {task_info["target"]}</div>', unsafe_allow_html=True)
        with col_pop_task:
            with st.popover("[INFO]"):
                st.markdown(f'<div class="bubble-header">SYSTEMIC ANALYSIS DETAILS</div>', unsafe_allow_html=True)
                st.markdown(f'<div class="bubble-policy"><strong>Policy Source:</strong> {task_info["policy_long"]}</div>', unsafe_allow_html=True)
                st.write(f"**Operational Task:** {task_info['desc_long']}")
                st.markdown(f'<div style="color:#00FF66; margin-top:8px;"><strong>Appraisal Rationale:</strong> {task_info["rationale"]}</div>', unsafe_allow_html=True)

        st.markdown(f"**{task_info['label']}**")
        
        # Pull current state
        curr_state = st.session_state.appraisal_audit_v4[task_id]["compliant"]
        
        col_lbl, col_sel = st.columns([1, 1])
        with col_lbl:
            st.write("Diagnostic Status:")
        with col_sel:
            status_val = st.radio(
                "Select status",
                ["Compliant", "Non-Compliant"],
                index=0 if curr_state else 1,
                key=f"status_{task_id}",
                horizontal=True,
                label_visibility="collapsed"
            )
        
        # Save to session state
        st.session_state.appraisal_audit_v4[task_id]["compliant"] = (status_val == "Compliant")
        
        # Render remediation instructions if marked Non-Compliant
        if status_val == "Non-Compliant":
            st.markdown(
                f'<div class="remedy-banner">'\
                f'⚠️ <strong>REMEDIATION DIRECTIVE:</strong> {task_info["remediation"]}'\
                f'</div>',\
                unsafe_allow_html=True
            )
            
        st.markdown('</div>', unsafe_allow_html=True)

# ----------------- PHASE III VIEW -----------------
elif phase_selector == "Phase III: Synthesis & Recommendations (Days 61–90)":
    st.markdown('<div class="digital-divider"></div>', unsafe_allow_html=True)
    st.markdown(f"### **{audit_db['Phase III']['title']}**")
    
    with st.popover("🔬 CLICK FOR PHASE III DIAGNOSTIC BLUEPRINT"):
        st.markdown(f'<div class="bubble-header">PHASE III OVERVIEW & OBJECTIVE</div>', unsafe_allow_html=True)
        st.write(audit_db["Phase III"]["diagnostic_rationale"])
        
    # CARRYOVER LOGIC: Phase II to Phase III
    phase2_tasks = audit_db["Phase II"]["tasks"]
    p2_non_compliant_keys = [tid for tid in phase2_tasks.keys() if not st.session_state.appraisal_audit_v4[tid]["compliant"]]
    
    if p2_non_compliant_keys:
        st.markdown('<div class="cascade-alert">', unsafe_allow_html=True)
        st.markdown("🚨 <strong>CRITICAL CARRYOVER ALERT: UNRESOLVED PHASE II GAPS DETECTED!</strong>", unsafe_allow_html=True)
        st.write("The following operational and financial gaps remain unresolved. Proposing Phase III strategic recommendations is compromised due to unaligned baselines:")
        for tid in p2_non_compliant_keys:
            st.markdown(f"• **{phase2_tasks[tid]['label']}** — *Unresolved risk of billing denials or uncompensated clinical work.*")
        st.markdown("</div>", unsafe_allow_html=True)
    else:
        st.markdown('<div style="background-color: rgba(0, 255, 102, 0.08); padding: 12px; border-radius: 12px; border-left: 5px solid #00FF66; border: 1px solid rgba(0, 255, 102, 0.2); margin-bottom: 16px; font-size: 12px; color: #00FF66;">✓ <strong>All Phase II analytical audits are verified and compliant.</strong> Ready to synthesize strategic recommendations.</div>', unsafe_allow_html=True)

    phase_tasks = audit_db["Phase III"]["tasks"]
    for task_id, task_info in phase_tasks.items():
        st.markdown(f'<div class="app-card">', unsafe_allow_html=True)
        
        # Policy badge and popover
        col_badge, col_pop_task = st.columns([3, 1])
        with col_badge:
            st.markdown(f'<div class="policy-label">{task_info["policy_short"]}</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="target-label">Target: {task_info["target"]}</div>', unsafe_allow_html=True)
        with col_pop_task:
            with st.popover("[INFO]"):
                st.markdown(f'<div class="bubble-header">SYSTEMIC ANALYSIS DETAILS</div>', unsafe_allow_html=True)
                st.markdown(f'<div class="bubble-policy"><strong>Policy Source:</strong> {task_info["policy_long"]}</div>', unsafe_allow_html=True)
                st.write(f"**Operational Task:** {task_info['desc_long']}")
                st.markdown(f'<div style="color:#00FF66; margin-top:8px;"><strong>Appraisal Rationale:</strong> {task_info["rationale"]}</div>', unsafe_allow_html=True)

        st.markdown(f"**{task_info['label']}**")
        
        # Pull current state
        curr_state = st.session_state.appraisal_audit_v4[task_id]["compliant"]
        
        col_lbl, col_sel = st.columns([1, 1])
        with col_lbl:
            st.write("Diagnostic Status:")
        with col_sel:
            status_val = st.radio(
                "Select status",
                ["Compliant", "Non-Compliant"],
                index=0 if curr_state else 1,
                key=f"status_{task_id}",
                horizontal=True,
                label_visibility="collapsed"
            )
        
        # Save to session state
        st.session_state.appraisal_audit_v4[task_id]["compliant"] = (status_val == "Compliant")
        
        # Render remediation instructions if marked Non-Compliant
        if status_val == "Non-Compliant":
            st.markdown(
                f'<div class="remedy-banner">'\
                f'⚠️ <strong>REMEDIATION DIRECTIVE:</strong> {task_info["remediation"]}'\
                f'</div>',\
                unsafe_allow_html=True
            )
            
        st.markdown('</div>', unsafe_allow_html=True)

# ----------------- PROGRESS & FINDINGS REPORT VIEW -----------------
elif phase_selector == "Progress & Findings Report (Executive Tab)":
    st.markdown('<div class="digital-divider"></div>', unsafe_allow_html=True)
    
    # Styled Executive Header Block (Purple & Green design)
    st.markdown("<div style='text-align: center; border: 2px solid rgba(0, 255, 102, 0.4); padding: 16px; border-radius: 16px; background-color: rgba(30, 8, 48, 0.95); margin-bottom: 20px; box-shadow: 0 0 20px rgba(0, 255, 102, 0.15);'>", unsafe_allow_html=True)
    st.markdown("<h3 style='color: #FFFFFF; margin: 0; font-weight: 900; font-size:16px; font-family: monospace; letter-spacing: 1.5px; text-shadow: 0 0 8px rgba(0, 255, 102, 0.5);'>CNS HEALTHCARE PSYCHOLOGICAL SERVICES</h3>", unsafe_allow_html=True)
    st.markdown("<h4 style='color: #00FF66; margin: 4px 0 0 0; font-weight: 700; font-size:12px; font-family: monospace; letter-spacing: 1px;'>EXECUTIVE PROGRESS & FINDINGS REPORT</h4>", unsafe_allow_html=True)
    st.markdown(f"<p style='color: #E1BEE7; font-size: 10px; margin: 6px 0 0 0; font-family: monospace; line-height: 1.3;'>Prepared for: Provider Supervisors & Executive Leadership<br>Auditor: Dr. Scott Niewinski, Psy.D., Manager of Psychological Services</p>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)
    
    # Calculate live global metrics across all phases
    all_tasks = []
    compliant_count = 0
    non_compliant_list = []
    compliant_list = []
    
    for phase_name, phase_info in audit_db.items():
        for task_id, task_info in phase_info["tasks"].items():
            is_comp = st.session_state.appraisal_audit_v4[task_id]["compliant"]
            all_tasks.append((task_id, task_info, phase_info["title"], is_comp))
            if is_comp:
                compliant_count += 1
                compliant_list.append((task_info, phase_info["title"]))
            else:
                non_compliant_list.append((task_info, phase_info["title"]))
                
    total_count = len(all_tasks)
    comp_pct = (compliant_count / total_count) * 100
    
    # Executive Digital Scorecards
    col_pct, col_non = st.columns(2)
    with col_pct:
        st.metric("COMPLIANCE RATE", f"{comp_pct:.1f}%", f"{compliant_count}/{total_count} Passed")
    with col_non:
        st.metric("ACTIVE GAPS", f"{len(non_compliant_list)}", delta="- Risk Mitigations Needed", delta_color="inverse")
        
    st.progress(compliant_count / total_count)
    st.markdown('<div class="digital-divider"></div>', unsafe_allow_html=True)
    
    st.markdown("### **📋 APPRAISAL STATUS SUMMARY**")
    
    # Compliant Items Summary
    if compliant_list:
        with st.expander("🟢 VERIFIED STRENGTHS & COMPLIANT AREAS", expanded=True):
            for t_info, p_name in compliant_list:
                st.markdown(f"**✓ {t_info['label']}**")
                st.markdown(f"<span style='font-size:10px; color:#00FF66; font-family: monospace;'>Phase: {p_name} | Policy: {t_info['policy_short']}</span>", unsafe_allow_html=True)
                st.markdown("<hr style='margin: 8px 0; border: none; border-bottom: 1px solid rgba(255,255,255,0.1);'>", unsafe_allow_html=True)
    
    # Non-Compliant Gaps Summary with dynamic Remediation Directives
    if non_compliant_list:
        st.markdown("### **🔴 CRITICAL VULNERABILITIES & MITIGATION MATRIX**")
        st.write("These items represent active regulatory, licensing, or billing liabilities demanding immediate executive correction:")
        
        for t_info, p_name in non_compliant_list:
            st.markdown(f"<div style='border: 1px solid rgba(211, 47, 47, 0.4); border-radius: 12px; padding: 14px; margin-bottom: 12px; background-color: rgba(211, 47, 47, 0.08);'>", unsafe_allow_html=True)
            st.markdown(f"<strong style='color:#FF8A80; font-family: monospace;'>[GAP] {t_info['label']}</strong><br><span style='font-size:10px; color:#E1BEE7;'>Phase: {p_name}</span>", unsafe_allow_html=True)
            st.markdown(f"<p style='margin: 8px 0 4px 0; font-size:12px; color: #ECEFF1;'><strong>Regulatory Policy:</strong> {t_info['policy_long']}</p>", unsafe_allow_html=True)
            st.markdown(f"<p style='margin: 4px 0 4px 0; font-size:12px; color: #00FF66; font-family: monospace;'><strong>Target KPI Metric:</strong> {t_info['target']}</p>", unsafe_allow_html=True)
            st.markdown(f"<p style='margin: 4px 0 4px 0; font-size:12px; color: #FFCDD2;'><strong>Active Vulnerability:</strong> {t_info['rationale']}</p>", unsafe_allow_html=True)
            
            st.markdown(
                f'<div class="remedy-banner">'\
                f'🛠️ <strong>REMEDIATION DIRECTIVE:</strong> {t_info["remediation"]}'\
                f'</div>',\
                unsafe_allow_html=True
            )
            st.markdown("</div>", unsafe_allow_html=True)
    else:
        st.success("🎉 Spectacular! All 90-Day appraisal deliverables are verified as 100% compliant with LARA, MDHHS, and CARF guidelines. No active risks detected.")

# Sticky Scientific Footer
st.markdown("<hr style='margin-top: 30px; border-color: rgba(0, 255, 102, 0.2);'>", unsafe_allow_html=True)
st.markdown(
    '<div style="font-size:9px; color:#808080; text-align:center; padding-bottom:15px; font-family: monospace;">'
    'CNS Healthcare Appraisal Systems • Grounded strictly in "90-Day Psychological Services Appraisal Plan.docx"'
    '</div>',
    unsafe_allow_html=True
)
