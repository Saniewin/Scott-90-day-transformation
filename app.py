import streamlit as st

# Set Streamlit Page Configuration - optimized for Samsung Galaxy S26 Ultra (high-res vertical viewport)
st.set_page_config(
    page_title="90-Day Psychological Services Appraisal App",
    page_icon="💜",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Premium Purple, Green, and White CSS styling (Samsung OneUI aesthetic)
st.markdown("""
<style>
    /* Main body styling */
    .stApp {
        background-color: #F9F8FC;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
    }
    
    /* Device frame mockup for Samsung S26 Ultra */
    @media (min-width: 450px) {
        .block-container {
            max-width: 440px !important;
            padding: 24px !important;
            background: #FFFFFF;
            border-radius: 36px;
            box-shadow: 0 24px 80px rgba(74, 21, 75, 0.08);
            margin-top: 15px;
            margin-bottom: 25px;
            border: 8px solid #3A103B; /* Premium Dark Purple Frame */
        }
    }
    
    /* Sleek card styling */
    .app-card {
        background: #FFFFFF;
        border-radius: 18px;
        padding: 16px;
        margin-bottom: 16px;
        box-shadow: 0 4px 20px rgba(74, 21, 75, 0.02);
        border: 1px solid #ECE6F0; /* Purple-tinted border */
    }
    
    /* Premium Header elements */
    .app-title {
        font-size: 26px !important;
        font-weight: 800 !important;
        color: #4A154B; /* Deep Purple */
        text-align: center;
        margin-bottom: 2px;
        letter-spacing: -0.6px;
    }
    
    .app-subtitle {
        font-size: 13px;
        color: #7A8B7B; /* Muted Green-Gray */
        text-align: center;
        margin-bottom: 24px;
        font-weight: 500;
    }
    
    /* Headers inside the cards */
    .section-header {
        font-size: 16px;
        font-weight: 700;
        color: #4A154B;
        border-bottom: 2px solid #E8F5E9; /* Green Accent border */
        padding-bottom: 6px;
        margin-bottom: 12px;
    }
    
    /* Color-coded tags */
    .policy-badge {
        font-size: 11px;
        font-weight: 700;
        background-color: #F3E5F5; /* Light Purple */
        color: #4A154B; /* Deep Purple */
        padding: 4px 10px;
        border-radius: 12px;
        display: inline-block;
        margin-bottom: 10px;
    }
    
    .target-badge {
        font-size: 11px;
        font-weight: 700;
        background-color: #E8F5E9; /* Light Green */
        color: #2E7D32; /* Rich Green */
        padding: 4px 10px;
        border-radius: 12px;
        display: inline-block;
        margin-bottom: 10px;
        margin-left: 5px;
    }

    /* Remediation protocols card */
    .remediation-box {
        background-color: #FFF9C4; /* Warm yellow/amber highlight */
        padding: 12px;
        border-radius: 12px;
        border-left: 5px solid #FBC02D;
        margin-top: 10px;
        font-size: 12px;
        color: #5D4037;
    }
    
    /* Carryover Alert styling */
    .carryover-alert-box {
        background-color: #FFEBEE;
        padding: 12px;
        border-radius: 12px;
        border-left: 5px solid #D32F2F;
        margin-bottom: 16px;
        font-size: 12px;
        color: #C62828;
    }
    
    /* HR style dividers */
    .purple-divider {
        height: 2px;
        background: linear-gradient(to right, #4A154B, #2E7D32, #FFFFFF);
        border: none;
        margin: 15px 0;
    }
</style>
""", unsafe_allow_html=True)

# Title & Metadata mockups
st.markdown('<div class="app-title">CNS HEALTHCARE</div>', unsafe_allow_html=True)
st.markdown('<div class="app-subtitle">90-Day Psychological Services Appraisal Portal</div>', unsafe_allow_html=True)

# Define our structured objectives, tasks, targets, and policies strictly from the Word document
audit_definitions = {
    "Phase I: Assessment & Baseline (Days 1–30)": {
        "tasks": {
            "p1_t1": {
                "label": "Verify Limited License Psychologist (LLP) Supervision Logs.",
                "policy": "Michigan Public Health Code MCL 333.18223 & LARA Rule 338.2569: Requires LLPs to document at least 4 hours/month of individual, face-to-face supervision on Form LARA/BPL Rev. 6/25.",
                "target": "100% compliance with LARA MCL 333.18223 (4 hrs/mo individual)",
                "remediation": "Immediately halt unsupervised LLP billing to avoid recoupment. Establish automated HR tracking for Psychology Supervision Evaluation forms (Rev. 6/25) and mandate co-signatures in the EHR before claim release.",
                "risk_category": "Licensure & LARA Compliance",
                "risk_vulnerability": "Failure of an LP to provide or document mandated LLP supervision hours.",
                "risk_impact": "Disciplinary action against LP/LLP licenses; catastrophic retroactive Medicaid clawback audits for years of billed PPS encounters."
            },
            "p1_t2": {
                "label": "Audit 30 completed psychological/neuropsychological testing charts.",
                "policy": "CPT Manual Definitions & Medicare LCD guidelines: Under CPT 96130, first-hour evaluation requires documented clinical decision-making and face-to-face interactive feedback.",
                "target": "100% presence of interactive feedback documentation for CPT 96130",
                "remediation": "Perform self-disclosure and adjust billing for un-documented feedback. Mandate structured EHR templates for 96130 that explicitly require a timestamped section titled 'Interactive Feedback and Clinical Decision Making' before note locking.",
                "risk_category": "Coding Specificity",
                "risk_vulnerability": "Improper use of 96130 or failing to document the 'interactive feedback' component.",
                "risk_impact": "Fraud, Waste, and Abuse (FWA) compliance risks; severe clawbacks from Medicaid/Commercial payers during routine audits."
            },
            "p1_t3": {
                "label": "Shadow intake and referral triage workflows.",
                "policy": "SAMHSA CCBHC Access Criteria (2023) & MDHHS CCBHC Handbook: Mandates timely, unimpeded access to care and clear referral velocity tracking.",
                "target": "Map 100% of the lifecycle from referral to scheduling",
                "remediation": "Map administrative handoffs and interaction with Prepaid Inpatient Health Plan (PIHP) portals (MHWIN/CHAMPS) to isolate bottleneck points causing scheduling delays.",
                "risk_category": "CCBHC Compliance",
                "risk_vulnerability": "Waitlist duration for testing exceeds the SAMHSA/MDHHS mandated timelines for routine or urgent access.",
                "risk_impact": "Corrective Action Plan (CAP) from the state; potential threat to CCBHC demonstration status and vital PPS funding."
            },
            "p1_t4": {
                "label": "Survey internal prescribers, outpatient therapists, and external stakeholders.",
                "policy": "CARF Accreditation Standards & CCBHC care coordination: Assesses clinical utility, readability, and diagnostic clarity of psychological reports.",
                "target": ">80% response rate from top 20 referring clinicians",
                "remediation": "Review the survey results on report readability; standardize report structures to contain standard, actionable interdisciplinary recommendations.",
                "risk_category": "Clinical Quality",
                "risk_vulnerability": "Completed reports do not effectively penetrate the Person-Centered Plan (PCP) or guide treatment.",
                "risk_impact": "Failure of the CCBHC integrated care model; clinical reports act as isolated, low-impact administrative exercises."
            }
        }
    },
    "Phase II: Operational Analysis & Gap Assessment (Days 31–60)": {
        "tasks": {
            "p2_t1": {
                "label": "Conduct CPT 96130-96139 billing denial audit.",
                "policy": "RCM Clearinghouse 835 Remittance Guidelines: Standardizes claims evaluation based on coding accuracy, bundling, and medical necessity.",
                "target": "Identify top 3 denial reason codes for psychological testing",
                "remediation": "Collaborate with RCM/billing teams to extract a 12-month claims dataset. Segment and analyze denial codes like CO-97 (bundled services) and CO-50 (medical necessity) to target corrective training.",
                "risk_category": "Revenue Cycle Integrity",
                "risk_vulnerability": "Unresolved automated clearinghouse denials due to structural billing mismatch.",
                "risk_impact": "Massive compounding revenue leakage and administrative burden for retroactive, uncompensated billing appeals."
            },
            "p2_t2": {
                "label": "Execute CPT Modifier 59 / XE compliance audit.",
                "policy": "CMS National Correct Coding Initiative (NCCI) Edits & MDHHS Billing Manual: Prohibits same-day psychologist test administration (96136) and tech administration (96138) without distinguishing modifiers.",
                "target": "100% accuracy on same-day provider (96136) and tech (96138) billing",
                "remediation": "Hardcode EHR billing validation rules to automatically flag same-day administration codes. Train billing staff on correctly applying Modifier XE or Modifier 59 to release blocked claims.",
                "risk_category": "Revenue Cycle (NCCI)",
                "risk_vulnerability": "Billing provider (96136) and technician (96138) administration on same date without Modifier 59 or XE.",
                "risk_impact": "Immediate, automated claims denial; post-payment Fraud, Waste, and Abuse (FWA) compliance audit scrutiny."
            },
            "p2_t3": {
                "label": "Audit remote CPT 96130 feedback session telehealth modifiers.",
                "policy": "MDHHS Telehealth Policy & Commercial Payer Guidelines: Requires specific telehealth Modifiers (95/GT) and Place of Service (POS 02/10) to secure virtual feedback reimbursement.",
                "target": "100% compliance with remote feedback session coding",
                "remediation": "Configure the EHR telehealth module to automatically append Modifier 95/GT and POS 02/10 whenever a virtual link is generated for a psychological testing encounter.",
                "risk_category": "Telehealth Regulations",
                "risk_vulnerability": "Providing remote feedback sessions without appropriate POS and Modifiers.",
                "risk_impact": "Claim denial or underpayment due to improper site-of-service identification, artificially suppressing realization rates."
            },
            "p2_t4": {
                "label": "Assess workflow navigation of differing PIHP/MCO Prior Authorization (PA) rules.",
                "policy": "Michigan Medicaid Provider Manual: Governs prior authorization limits and tracking.",
                "target": "Establish centralized workflow for tracking PIHP/MCO PA thresholds",
                "remediation": "Embed an EHR scheduling hard stop that blocks testing appointments exceeding 8 hours annually (Meridian limit) without an active, attached PA number.",
                "risk_category": "Utilization Management",
                "risk_vulnerability": "Exceeding annual testing limits or failing to secure initial PA from regional PIHPs.",
                "risk_impact": "Complete forfeiture of payment for the entire testing battery; uncompensated clinical labor by testing psychologists."
            },
            "p2_t5": {
                "label": "Measure mean and median Turnaround Time (TAT) across clinicians.",
                "policy": "CARF Accreditation Standards & SAMHSA Access Metrics: Benchmarks timelines for clinical evaluation and rapid treatment initiation.",
                "target": "Calculate median days from final test administration to signed report in EHR",
                "remediation": "Segment EHR timestamp data into three intervals: referral-to-authorization, authorization-to-testing, and testing-to-signed-report. Isolate and counsel outlying clinicians.",
                "risk_category": "CCBHC & CARF Access Timeline",
                "risk_vulnerability": "Prolonged report turnaround times delaying treatment initiation.",
                "risk_impact": "Violates the CCBHC care coordination mandate, delaying psychiatric and therapeutic interventions; triggers State CAPs."
            },
            "p2_t6": {
                "label": "Conduct financial overhead analysis of clinical testing batteries.",
                "policy": "CCBHC PPS Cost Allocation Guidelines: Requires tracking expenditures against the daily encounter prospective payment rate.",
                "target": "Establish cost-per-assessment ratio ( Pearson, PAR, WPS vendor invoices vs. claim volume)",
                "remediation": "Cross-reference vendor invoices for digital scoring licenses (Q-interactive, PARiConnect) and consumable kits against Medicaid fee-for-service / PPS revenues to identify high-cost, low-yield instruments.",
                "risk_category": "Financial Sustainability",
                "risk_vulnerability": "High operational overhead of diagnostic kits not offset by encounter billing.",
                "risk_impact": "Unrecognized department deficits and budget imbalances under the value-based CCBHC prospective payment system."
            }
        }
    },
    "Phase III: Synthesis & Strategic Recommendations (Days 61–90)": {
        "tasks": {
            "p3_t1": {
                "label": "Develop Stepped-Care Assessment clinical protocol.",
                "policy": "SAMHSA CCBHC Core Service #2: Screening, Assessment, and Diagnosis. Mandates optimizing resource allocation and clinical triage workflows.",
                "target": "Draft clinical pathway utilizing brief 96127 screenings prior to full testing",
                "remediation": "Establish a rigid triage algorithm. Shift low-acuity diagnostic questions to brief screenings (96127 / 90791) at intake, reserving multi-hour, intensive batteries for complex differential diagnosis.",
                "risk_category": "Utilization Efficiency",
                "risk_vulnerability": "Highly trained psychologists conducting routine diagnostic work for low-acuity referrals.",
                "risk_impact": "Artificially inflated waitlists for SMI/SED populations, causing critical bottleneck failures and CCBHC non-compliance."
            },
            "p3_t2": {
                "label": "Establish ongoing Assessment KPI Dashboard.",
                "policy": "CCBHC Continuous Quality Improvement (CQI) Plan: Demands data-driven performance monitoring for clinical management.",
                "target": "Track 5 core metrics on a live EHR/BI dashboard (Volume, TAT, Denials, Waitlist, Cost)",
                "remediation": "Coordinate with IT to configure a Business Intelligence dashboard inside the EHR, giving leadership real-time visibility over weekly referral volumes and clinician performance.",
                "risk_category": "Oversight and Accountability",
                "risk_vulnerability": "Lack of high-fidelity, real-time tracking leading to administrative and clinical regressions.",
                "risk_impact": "Unrecognized operational bottlenecks and unresolved billing errors leading to compounding revenue loss over time."
            },
            "p3_t3": {
                "label": "Deliver formal 'State of Psychological Testing' Executive Appraisal Report.",
                "policy": "MDHHS & SAMHSA CCBHC Demonstration Guidelines: Mandates rigorous administrative and clinical oversight of certified services.",
                "target": "Submit comprehensive operational and financial analysis document to executive board",
                "remediation": "Assemble all manual chart audit findings, billing denial patterns, and overhead metrics into a formalized, high-impact document to secure leadership approval.",
                "risk_category": "Regulatory Fidelity",
                "risk_vulnerability": "Omission of documented appraisal findings regarding psychological testing service lines.",
                "risk_impact": "Non-compliance with State certification requirements; inability to justify cost-based rate rebasing in future demonstration years."
            },
            "p3_t4": {
                "label": "Present 12-month strategic roadmap.",
                "policy": "CCBHC Certification Program requirement #6: Strategic Planning & Capital Investment.",
                "target": "Secure executive consensus and approval of top 3 optimization priorities",
                "remediation": "Formally present the roadmap outlining capital investments (such as digital scoring platform interoperability), centralized LARA tracking, and coding modifier compliance training.",
                "risk_category": "Long-Term Sustainability",
                "risk_vulnerability": "Failure to plan for systemic, long-term capital investments in psychological service lines.",
                "risk_impact": "Operational stagnation, persistent staff burnout due to EHR administrative burdens, and ongoing financial leaks."
            }
        }
    }
}

# Initialize Session State for audit data
if 'appraisal_audit' not in st.session_state:
    st.session_state.appraisal_audit = {}
    for phase_name, phase_info in audit_definitions.items():
        for task_id, task_info in phase_info["tasks"].items():
            st.session_state.appraisal_audit[task_id] = {
                "compliant": True,
                "notes": ""
            }

# Selection of the active Phase / View
phase_selector = st.selectbox(
    "Select Appraisal Phase to View/Edit:",
    ["Phase I: Assessment & Baseline (Days 1–30)", 
     "Phase II: Operational Analysis & Gap Assessment (Days 31–60)", 
     "Phase III: Synthesis & Strategic Recommendations (Days 61–90)",
     "Progress & Findings Report (Executive Tab)"]
)

# ----------------- PHASE I VIEW -----------------
if phase_selector == "Phase I: Assessment & Baseline (Days 1–30)":
    st.markdown('<div class="purple-divider"></div>', unsafe_allow_html=True)
    st.markdown("### **Phase I: Assessment & Baseline (Days 1–30)**")
    st.write("Perform real-time compliance audits. Mark tasks as 'Compliant' or 'Non-Compliant' per the 90-Day Appraisal Plan to view remediation protocols.")

    phase_tasks = audit_definitions["Phase I: Assessment & Baseline (Days 1–30)"]["tasks"]
    
    for task_id, task_info in phase_tasks.items():
        st.markdown(f'<div class="app-card">', unsafe_allow_html=True)
        st.markdown(f'<div class="policy-badge">{task_info["policy"]}</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="target-badge">Target: {task_info["target"]}</div>', unsafe_allow_html=True)
        st.markdown(f"**{task_info['label']}**")
        
        # Pull current state
        curr_state = st.session_state.appraisal_audit[task_id]["compliant"]
        
        col_lbl, col_sel = st.columns([2, 2])
        with col_lbl:
            st.write("Current Status:")
        with col_sel:
            status_val = st.radio(
                "Status selector",
                ["Compliant", "Non-Compliant"],
                index=0 if curr_state else 1,
                key=f"status_{task_id}",
                horizontal=True,
                label_visibility="collapsed"
            )
        
        # Save to session state
        st.session_state.appraisal_audit[task_id]["compliant"] = (status_val == "Compliant")
        
        # Render remediation instructions if marked Non-Compliant
        if status_val == "Non-Compliant":
            st.markdown(
                f'<div class="remediation-box">'
                f'🚨 <strong>Remediation Directive:</strong> {task_info["remediation"]}<br><br>'
                f'⚠️ <strong>Systemic Vulnerability:</strong> {task_info["risk_vulnerability"]}<br>'
                f'💥 <strong>Operational Impact:</strong> {task_info["risk_impact"]}'
                f'</div>',
                unsafe_allow_html=True
            )
            
        st.markdown('</div>', unsafe_allow_html=True)
        
    st.markdown('<div class="purple-divider"></div>', unsafe_allow_html=True)
    st.markdown("#### **🧠 CliftonStrengths Integration: Phase I Leadership**")
    st.write("Dr. Scott Niewinski should leverage his dominant talents to drive Phase I baseline auditing:")
    
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
elif phase_selector == "Phase II: Operational Analysis & Gap Assessment (Days 31–60)":
    st.markdown('<div class="purple-divider"></div>', unsafe_allow_html=True)
    st.markdown("### **Phase II: Operational Analysis & Gap Assessment (Days 31–60)**")
    
    # CARRYOVER LOGIC: Phase I to Phase II
    # Check if there are any non-compliant items in Phase I
    phase1_tasks = audit_definitions["Phase I: Assessment & Baseline (Days 1–30)"]["tasks"]
    p1_non_compliant_keys = [tid for tid in phase1_tasks.keys() if not st.session_state.appraisal_audit[tid]["compliant"]]
    
    if p1_non_compliant_keys:
        st.markdown('<div class="carryover-alert-box">', unsafe_allow_html=True)
        st.markdown("🚨 **Critical Carryover Alert: Unresolved Phase I Vulnerabilities Detected!**")
        st.write("The following baseline components remain out of compliance, directly threatening the validity of Phase II operational and financial analyses:")
        for tid in p1_non_compliant_keys:
            st.markdown(f"• **{phase1_tasks[tid]['label']}** — *Unresolved risk of licensure disciplinary action or Medicaid recoupment.*")
        st.markdown("</div>", unsafe_allow_html=True)
    else:
        st.markdown('<div style="background-color: #E8F5E9; padding: 12px; border-radius: 12px; border-left: 5px solid #2E7D32; margin-bottom: 16px; font-size: 12px; color: #2E7D32;">✓ <strong>All Phase I baselines are verified and compliant.</strong> Transitioning cleanly into Phase II operational audits.</div>', unsafe_allow_html=True)

    phase_tasks = audit_definitions["Phase II: Operational Analysis & Gap Assessment (Days 31–60)"]["tasks"]
    
    for task_id, task_info in phase_tasks.items():
        st.markdown(f'<div class="app-card">', unsafe_allow_html=True)
        st.markdown(f'<div class="policy-badge">{task_info["policy"]}</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="target-badge">Target: {task_info["target"]}</div>', unsafe_allow_html=True)
        st.markdown(f"**{task_info['label']}**")
        
        # Pull current state
        curr_state = st.session_state.appraisal_audit[task_id]["compliant"]
        
        col_lbl, col_sel = st.columns([2, 2])
        with col_lbl:
            st.write("Current Status:")
        with col_sel:
            status_val = st.radio(
                "Status selector",
                ["Compliant", "Non-Compliant"],
                index=0 if curr_state else 1,
                key=f"status_{task_id}",
                horizontal=True,
                label_visibility="collapsed"
            )
        
        # Save to session state
        st.session_state.appraisal_audit[task_id]["compliant"] = (status_val == "Compliant")
        
        # Render remediation instructions if marked Non-Compliant
        if status_val == "Non-Compliant":
            st.markdown(
                f'<div class="remediation-box">'
                f'🚨 <strong>Remediation Directive:</strong> {task_info["remediation"]}<br><br>'
                f'⚠️ <strong>Systemic Vulnerability:</strong> {task_info["risk_vulnerability"]}<br>'
                f'💥 <strong>Operational Impact:</strong> {task_info["risk_impact"]}'
                f'</div>',
                unsafe_allow_html=True
            )
            
        st.markdown('</div>', unsafe_allow_html=True)

# ----------------- PHASE III VIEW -----------------
elif phase_selector == "Phase III: Synthesis & Strategic Recommendations (Days 61–90)":
    st.markdown('<div class="purple-divider"></div>', unsafe_allow_html=True)
    st.markdown("### **Phase III: Synthesis & Strategic Recommendations (Days 61–90)**")
    
    # CARRYOVER LOGIC: Phase II to Phase III
    phase2_tasks = audit_definitions["Phase II: Operational Analysis & Gap Assessment (Days 31–60)"]["tasks"]
    p2_non_compliant_keys = [tid for tid in phase2_tasks.keys() if not st.session_state.appraisal_audit[tid]["compliant"]]
    
    if p2_non_compliant_keys:
        st.markdown('<div class="carryover-alert-box">', unsafe_allow_html=True)
        st.markdown("🚨 **Critical Carryover Alert: Unresolved Phase II Gaps Detected!**")
        st.write("The following operational and financial gaps remain unresolved. Proposing Phase III strategic recommendations is compromised due to un-quantified or unaligned baselines:")
        for tid in p2_non_compliant_keys:
            st.markdown(f"• **{phase2_tasks[tid]['label']}** — *Unresolved risk of billing denials or uncompensated clinical work.*")
        st.markdown("</div>", unsafe_allow_html=True)
    else:
        st.markdown('<div style="background-color: #E8F5E9; padding: 12px; border-radius: 12px; border-left: 5px solid #2E7D32; margin-bottom: 16px; font-size: 12px; color: #2E7D32;">✓ <strong>All Phase II analytical audits are verified and compliant.</strong> Ready to synthesize strategic recommendations.</div>', unsafe_allow_html=True)

    phase_tasks = audit_definitions["Phase III: Synthesis & Strategic Recommendations (Days 61–90)"]["tasks"]
    
    for task_id, task_info in phase_tasks.items():
        st.markdown(f'<div class="app-card">', unsafe_allow_html=True)
        st.markdown(f'<div class="policy-badge">{task_info["policy"]}</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="target-badge">Target: {task_info["target"]}</div>', unsafe_allow_html=True)
        st.markdown(f"**{task_info['label']}**")
        
        # Pull current state
        curr_state = st.session_state.appraisal_audit[task_id]["compliant"]
        
        col_lbl, col_sel = st.columns([2, 2])
        with col_lbl:
            st.write("Current Status:")
        with col_sel:
            status_val = st.radio(
                "Status selector",
                ["Compliant", "Non-Compliant"],
                index=0 if curr_state else 1,
                key=f"status_{task_id}",
                horizontal=True,
                label_visibility="collapsed"
            )
        
        # Save to session state
        st.session_state.appraisal_audit[task_id]["compliant"] = (status_val == "Compliant")
        
        # Render remediation instructions if marked Non-Compliant
        if status_val == "Non-Compliant":
            st.markdown(
                f'<div class="remediation-box">'
                f'🚨 <strong>Remediation Directive:</strong> {task_info["remediation"]}<br><br>'
                f'⚠️ <strong>Systemic Vulnerability:</strong> {task_info["risk_vulnerability"]}<br>'
                f'💥 <strong>Operational Impact:</strong> {task_info["risk_impact"]}'
                f'</div>',
                unsafe_allow_html=True
            )
            
        st.markdown('</div>', unsafe_allow_html=True)

# ----------------- EXECUTIVE REPORT VIEW -----------------
elif phase_selector == "Progress & Findings Report (Executive Tab)":
    st.markdown('<div class="purple-divider"></div>', unsafe_allow_html=True)
    st.markdown("<div style='text-align: center; border: 2px solid #4A154B; padding: 15px; border-radius: 12px; background-color: #F3E5F5; margin-bottom: 20px;'>", unsafe_allow_html=True)
    st.markdown("<h3 style='color: #4A154B; margin: 0; font-weight: 800; font-size:18px;'>90-DAY PSYCHOLOGICAL SERVICES APPRAISAL</h3>", unsafe_allow_html=True)
    st.markdown("<h4 style='color: #2E7D32; margin: 5px 0 0 0; font-weight: 700; font-size:14px;'>EXECUTIVE PROGRESS & FINDINGS REPORT</h4>", unsafe_allow_html=True)
    st.markdown(f"<p style='color: #7A8B7B; font-size: 11px; margin: 5px 0 0 0;'>Prepared for: CNS Healthcare Clinical & Executive Leadership<br>Auditor: Dr. Scott Niewinski, Psy.D., Manager of Psychological Services</p>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)
    
    # Calculate global metrics
    all_tasks = []
    compliant_count = 0
    non_compliant_list = []
    compliant_list = []
    
    for phase_name, phase_info in audit_definitions.items():
        for task_id, task_info in phase_info["tasks"].items():
            is_comp = st.session_state.appraisal_audit[task_id]["compliant"]
            all_tasks.append((task_id, task_info, phase_name, is_comp))
            if is_comp:
                compliant_count += 1
                compliant_list.append((task_info, phase_name))
            else:
                non_compliant_list.append((task_info, phase_name))
                
    total_count = len(all_tasks)
    comp_pct = (compliant_count / total_count) * 100
    
    # Executive Scorecards
    col_pct, col_non = st.columns(2)
    with col_pct:
        st.metric("Total Compliance Score", f"{comp_pct:.1f}%", f"{compliant_count}/{total_count} Verified")
    with col_non:
        st.metric("Identified Compliance Gaps", f"{len(non_compliant_list)}", delta="- Active Gaps", delta_color="inverse")
        
    st.progress(compliant_count / total_count)
    st.markdown('<div class="purple-divider"></div>', unsafe_allow_html=True)
    
    # Detailed section breakups
    st.markdown("### **🔍 Detailed Appraisal Findings**")
    
    # Compliant Items Summary
    if compliant_list:
        with st.expander("🟢 Verified Strengths & Compliant Areas", expanded=True):
            for t_info, p_name in compliant_list:
                st.markdown(f"✓ **{t_info['label']}** ({p_name})")
                st.markdown(f"<span style='font-size:11px; color:#2E7D32;'>Policy: {t_info['policy']}</span>", unsafe_allow_html=True)
                st.markdown("<hr style='margin: 6px 0;'>", unsafe_allow_html=True)
    
    # Non-Compliant Gaps Summary with dynamic Remediation Directives
    if non_compliant_list:
        st.markdown("### **🔴 Critical Vulnerabilities & Active Risk Matrix**")
        st.write("The following items are out of compliance and present active regulatory, financial, or operational liabilities:")
        
        for t_info, p_name in non_compliant_list:
            st.markdown(f"<div style='border: 1.5px solid #FFCDD2; border-radius: 12px; padding: 14px; margin-bottom: 12px; background-color: #FFF5F5;'>", unsafe_allow_html=True)
            st.markdown(f"<strong style='color:#C62828;'>[GAP] {t_info['label']}</strong><br><span style='font-size:11px; color:#78909C;'>Phase: {p_name}</span>", unsafe_allow_html=True)
            st.markdown(f"<p style='margin: 8px 0 4px 0; font-size:12px;'><strong>Regulatory Policy:</strong> {t_info['policy']}</p>", unsafe_allow_html=True)
            st.markdown(f"<p style='margin: 4px 0 4px 0; font-size:12px;'><strong>Target Metric:</strong> {t_info['target']}</p>", unsafe_allow_html=True)
            st.markdown(f"<p style='margin: 4px 0 4px 0; font-size:12px; color: #D32F2F;'><strong>Active Risk Category:</strong> {t_info['risk_category']}</p>", unsafe_allow_html=True)
            st.markdown(f"<p style='margin: 4px 0 4px 0; font-size:12px; color: #5D4037;'><strong>Vulnerability:</strong> {t_info['risk_vulnerability']}</p>", unsafe_allow_html=True)
            st.markdown(f"<p style='margin: 4px 0 4px 0; font-size:12px; color: #C62828;'><strong>Operational Impact:</strong> {t_info['risk_impact']}</p>", unsafe_allow_html=True)
            
            st.markdown(
                f'<div style="background-color: #FFF9C4; padding: 10px; border-radius: 8px; border-left: 4px solid #FBC02D; margin-top: 8px; font-size: 12px; color: #5D4037;">'
                f'🛠️ <strong>REMEDIATION DIRECTIVE:</strong> {t_info["remediation"]}'
                f'</div>',
                unsafe_allow_html=True
            )
            st.markdown("</div>", unsafe_allow_html=True)
    else:
        st.success("🎉 Spectacular! All 90-Day appraisal deliverables are verified as 100% compliant with LARA, MDHHS, and CARF guidelines. No active risks detected.")

# Sticky Footer
st.markdown("<hr style='margin-top: 30px;'>", unsafe_allow_html=True)
st.markdown(
    '<div style="font-size:10px; color:#90A4AE; text-align:center; padding-bottom:15px;">'
    'CNS Healthcare Appraisal Dashboard • Strictly Grounded in "90-Day Psychological Services Appraisal Plan.docx"'
    '</div>',
    unsafe_allow_html=True
)
