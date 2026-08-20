import streamlit as st
import time

# ==============================================================================
# STREAMLIT PAGE CONFIGURATION & DESKTOP WIDE-LAYOUT
# Optimized for standard PC and desktop displays with dynamic viewport adjustment
# ==============================================================================
st.set_page_config(
    page_title="CNS Psychological Services Clinical Systems Audit & Appraisal Portal",
    page_icon="🧬",
    layout="wide",  # Changed to wide layout for standard PC displays
    initial_sidebar_state="expanded"
)

# ==============================================================================
# PERFORMANCE CACHING & HEAVY DATA LOADING PROCESSES
# Using @st.cache_data to model real-world database queries, EHR connections,
# and claims remittance history analysis without overhead or memory leaks.
# ==============================================================================
@st.cache_data(show_spinner="Analyzing 12-month historical clinical claims and EHR logs...")
def load_historical_remittance_data():
    """
    Simulates a heavy RCM (Revenue Cycle Management) database query, extracting 
    12 months of historical claims history for billing codes CPT 96130-96139.
    Provides cached structural baseline parameters for the 90-day appraisal.
    """
    # Simulate a realistic data extraction delay
    time.sleep(1.2) 
    
    simulated_records = {
        "total_claims_analyzed": 1420,
        "clearinghouse_denials_found": 182,
        "ncci_edits_failures": 64,      # Same-day 96136/96138 without Modifier 59/XE
        "telehealth_billing_errors": 42, # Missing 95/GT modifier or POS 02/10 mismatch
        "average_report_tat_days": 24.5, # Median turnaround time from testing to sign-off
        "uncompensated_provider_hours": 128.0 # Hours lost to missing prior authorizations
    }
    return simulated_records

@st.cache_resource
def load_system_compliance_standards():
    """
    Caches core static policy maps and regulatory standards (LARA, MDHHS, SAMHSA)
    to prevent redundant initialization and optimize browser memory overhead.
    """
    return {
        "LARA_Licensure": {
            "statute": "Michigan Public Health Code MCL 333.18223",
            "rule": "LARA Rule 338.2569",
            "mandate": "Requires LLPs/TLLPs to secure 4 hours/month of face-to-face LP supervision on Form LARA/BPL Rev 6/25."
        },
        "CPT_Billing": {
            "source": "AMA CPT 2026 Codebook",
            "rule": "CPT 96130 / 96136 / 96138 Segregation Guidelines",
            "mandate": "CPT 96130 requires interactive face-to-face feedback; 96136 (provider) and 96138 (tech) are same-day mutually exclusive without modifier 59/XE."
        },
        "CCBHC_Access": {
            "source": "SAMHSA 2023 CCBHC Criteria & MDHHS CCBHC Demonstration Handbook v3.1",
            "rule": "Core Service #2 Access Velocity",
            "mandate": "Urgent cases initiated within 1 business day; routine diagnostic referrals initiated within 14 calendar days."
        }
    }

# Load the cached metadata resources
claims_metrics = load_historical_remittance_data()
policy_frameworks = load_system_compliance_standards()

# ==============================================================================
# PREMIUM DESKTOP CSS STYLING
# Clean, scientific-digital themed dashboard optimized for PC widescreen layout
# ==============================================================================
st.markdown("""
<style>
    /* Desktop overall color scheme background */
    .stApp {
        background: radial-gradient(circle at 50% 30%, #120822 0%, #06020E 100%) !important;
        color: #FFFFFF !important;
        font-family: 'Segoe UI', -apple-system, BlinkMacSystemFont, Roboto, sans-serif !important;
    }
    
    /* Subtle digital grid aesthetic overlay for PC */
    .stApp::before {
        content: "";
        position: absolute;
        top: 0; left: 0; width: 100%; height: 100%;
        background-image: 
            linear-gradient(rgba(34, 197, 94, 0.008) 1px, transparent 1px),
            linear-gradient(90deg, rgba(34, 197, 94, 0.008) 1px, transparent 1px);
        background-size: 30px 30px;
        pointer-events: none;
        z-index: 0;
    }
    
    /* Header layout styling */
    .desktop-header {
        background: rgba(26, 12, 48, 0.9);
        border: 1px solid rgba(34, 197, 94, 0.3);
        border-radius: 16px;
        padding: 24px;
        margin-bottom: 24px;
        box-shadow: 0 8px 32px rgba(34, 197, 94, 0.08);
    }
    
    .desktop-title {
        font-size: 28px !important;
        font-weight: 900 !important;
        color: #FFFFFF !important;
        text-shadow: 0 0 15px rgba(34, 197, 94, 0.6) !important;
        font-family: 'Courier New', Courier, monospace !important;
        letter-spacing: 1px !important;
        margin-bottom: 4px !important;
    }
    
    .desktop-subtitle {
        font-size: 12px !important;
        color: #22c55e !important;
        font-family: 'Courier New', Courier, monospace !important;
        letter-spacing: 2px !important;
        text-transform: uppercase !important;
        font-weight: bold !important;
    }
    
    /* Scientific Data Card Styling optimized for Desktop Rows */
    .desktop-card {
        background: rgba(26, 12, 48, 0.8) !important;
        border: 1px solid rgba(34, 197, 94, 0.2) !important;
        border-radius: 16px !important;
        padding: 20px !important;
        margin-bottom: 20px !important;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.5) !important;
        backdrop-filter: blur(12px) !important;
        transition: all 0.3s ease !important;
    }
    .desktop-card:hover {
        border-color: rgba(34, 197, 94, 0.5) !important;
        box-shadow: 0 0 20px rgba(34, 197, 94, 0.25) !important;
    }
    
    /* Metadata tags */
    .pc-badge-policy {
        font-size: 11px;
        font-weight: 700;
        background-color: rgba(75, 16, 96, 0.5);
        color: #E1BEE7;
        padding: 4px 10px;
        border-radius: 6px;
        display: inline-block;
        margin-bottom: 8px;
        border: 1px solid rgba(123, 31, 162, 0.6);
        font-family: monospace;
    }
    
    .pc-badge-target {
        font-size: 11px;
        font-weight: 700;
        background-color: rgba(34, 197, 94, 0.08);
        color: #22c55e;
        padding: 4px 10px;
        border-radius: 6px;
        display: inline-block;
        margin-bottom: 8px;
        margin-left: 4px;
        border: 1px solid rgba(34, 197, 94, 0.35);
        font-family: monospace;
    }

    /* Customized PC Popover buttons */
    div.stPopover > button {
        background-color: rgba(34, 197, 94, 0.05) !important;
        border: 1px solid rgba(34, 197, 94, 0.3) !important;
        color: #22c55e !important;
        border-radius: 8px !important;
        font-size: 11px !important;
        font-family: 'Courier New', Courier, monospace !important;
        text-transform: uppercase !important;
        letter-spacing: 1px !important;
        padding: 4px 12px !important;
        transition: all 0.2s ease !important;
    }
    div.stPopover > button:hover {
        background-color: rgba(34, 197, 94, 0.15) !important;
        border-color: #22c55e !important;
        box-shadow: 0 0 12px rgba(34, 197, 94, 0.4) !important;
        color: #FFFFFF !important;
    }
    
    /* Popover body layouts */
    .pc-popover-header {
        font-size: 14px;
        color: #22c55e;
        font-family: monospace;
        font-weight: bold;
        border-bottom: 1px solid rgba(34, 197, 94, 0.3);
        padding-bottom: 6px;
        margin-bottom: 8px;
    }
    
    /* Warning and remediation block on PC */
    .pc-remediation-banner {
        background-color: rgba(251, 192, 45, 0.08) !important;
        border: 1px solid rgba(251, 192, 45, 0.35) !important;
        border-left: 5px solid #FBC02D !important;
        padding: 14px !important;
        border-radius: 8px !important;
        margin-top: 12px !important;
        font-size: 12px !important;
        color: #FFE082 !important;
        line-height: 1.5;
    }
    
    .pc-cascade-alert {
        background-color: rgba(239, 68, 68, 0.08) !important;
        border: 1px solid rgba(239, 68, 68, 0.3) !important;
        border-left: 5px solid #EF4444 !important;
        padding: 16px !important;
        border-radius: 12px !important;
        margin-bottom: 20px !important;
        font-size: 12px !important;
        color: #FEE2E2 !important;
        line-height: 1.5;
    }

    .pc-divider {
        height: 2px;
        background: linear-gradient(to right, rgba(34, 197, 94, 0.6), rgba(75, 16, 96, 0.8), transparent);
        border: none;
        margin: 24px 0;
    }
    
    /* Clean custom styles for sidebar stats */
    .sidebar-stat-label {
        font-size: 11px;
        color: #A0AEC0;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    
    .sidebar-stat-val {
        font-size: 20px;
        color: #22c55e;
        font-weight: bold;
        font-family: monospace;
    }
</style>
""", unsafe_allow_html=True)

# ==============================================================================
# STRATEGIC CLINICAL DATABASE
# Sourced directly from 90-Day Psychological Services Appraisal Plan.docx
# ==============================================================================
audit_db = {
    "Phase 1": {
        "title": "Phase 1: Discovery (Days 1–30)",
        "objective": "Establish an empirical baseline and identify regulatory vulnerabilities in CNS's psychological testing operations.",
        "rationale": "Prior to redesigning administrative templates or billing rules, clinical operations must map and analyze current licensing, documentation, and waitlist gaps to safeguard against external audit failures and protect state-level CCBHC certification.",
        "strengths": {
            "header": "🧠 CLIFTONSTRENGTHS LEADER STRATEGY: LEARNER® & INTELLECTION®",
            "desc": "Apply your Learner drive to thoroughly study state licensing regulations, CPT billing definitions, and CARF guidelines. Use Intellection to perform a deep, root-cause analysis of documentation and scheduling bottlenecks.",
            "examples": [
                "**Learner (Task 1.1)**: Meticulously examines LARA Public Health Code MCL 333.18223 structures, turning dry legal compliance into an active intellectual journey toward total department compliance.",
                "**Intellection (Task 1.2)**: Introspectively reflects on why completed charts are missing interactive feedback, identifying EHR system gaps rather than simple provider neglect as the root cause."
            ]
        },
        "tasks": {
            "p1_t1": {
                "label": "Verify LLP Supervision Logs (LARA Compliance)",
                "policy": "MCL 333.18223 & LARA Rule 338.2569: Limited License Psychologists (LLPs) must receive 4 hours/month face-to-face LP supervision.",
                "target": "100% compliant logs on Form LARA/BPL Rev. 6/25",
                "desc": "Review all supervisory folders and confirm evaluations are active, signed, and logged for all LLPs and Temporary LLPs in the CMHSP network.",
                "rationale": "Unsigned or missing supervisory logs are a serious compliance risk, exposing the agency to state-level licensing penalties and retroactively invalidating billed Medicaid/PPS services.",
                "remediation": "Immediately halt billing for any LLP found to have undocumented supervision hours. Centralize log management in a secure HR folder and implement an EHR rule that blocks clinical note saving until co-signatures are verified."
            },
            "p1_t2": {
                "label": "Audit 30 Completed Testing Charts (Interactive Feedback)",
                "policy": "CPT 96130 Guidelines & Medicare Local Coverage Determinations (LCD): First-hour evaluation requires documented interactive feedback.",
                "target": "100% documented feedback session presence in EHR",
                "desc": "Conduct a manual, randomized chart audit of 30 completed psychological and neuropsychological evaluations across child, adult, and geriatric caseloads.",
                "rationale": "Billing evaluation code CPT 96130 without documenting interactive face-to-face feedback with the client or caregiver constitutes billing non-compliance.",
                "remediation": "Perform self-disclosure on un-documented feedback claims. Mandate a standardized NextGen template that prevents notes from being locked until a timestamped section labeled 'Interactive Feedback and Clinical Decision Making' is filled."
            },
            "p1_t3": {
                "label": "Shadow Triage and Referral Velocity Workflows",
                "policy": "SAMHSA CCBHC Access Criteria (2023): Requires timely, unimpeded access to care (routine care within 14 days, urgent within 1 day).",
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
        "objective": "Re-engineer electronic workflows and standardize clinician tools to resolve operational bottlenecks.",
        "rationale": "Transition from discovery to active system re-engineering. This phase builds standardized EHR templates and voice dictation software workflows to reduce administrative burden and eliminate same-day billing conflicts.",
        "strengths": {
            "header": "🧠 CLIFTONSTRENGTHS LEADER STRATEGY: IDEATION® & INDIVIDUALIZATION®",
            "desc": "Utilize Ideation to design structured, dynamic NextGen EHR templates and voice dictation command macros. Deploy Individualization to customize implementation training to fit each clinician's unique cognitive and typing styles.",
            "examples": [
                "**Ideation (Task 2.1)**: Designs and configures custom 'Smart-Phrase' voice dictation templates in Dragon Medical One, eliminating 60% of manual typing loops.",
                "**Individualization (Task 2.2)**: Delivers tailored training sessions, recognizing that some psychologists learn best via rapid video walkthroughs while others require hands-on co-auditing."
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
        "strengths": {
            "header": "🧠 CLIFTONSTRENGTHS LEADER STRATEGY: STRATEGIC®",
            "desc": "Deploy your Strategic theme to synthesize data from all manual audits, billing denials, and overhead costs into a cohesive 12-month optimization roadmap.",
            "examples": [
                "**Strategic (Task 3.1)**: Translates the financial overhead analysis of testing materials into a solid business-case proposal for fully digital platform licensing, proving long-term ROI under flat Daily PPS encounter rates.",
                "**Strategic (Task 3.2)**: Anticipates regional prior authorization rule changes, designing flexible tracking modules within the EHR KPI dashboard to capture cost-based rate-rebasing metrics."
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
                "desc": "Assemble all baseline chart audits, modifier denial rates, and kit cost overhead analyses into a formalized 'State of Psychological Testing' Executive Appraisal Report.",
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
# Persistent st.session_state configuration to track compliance statuses
# ==============================================================================
if "desktop_audit_states" not in st.session_state:
    st.session_state.desktop_audit_states = {}
    for phase_key, phase_val in audit_db.items():
        for task_key in phase_val["tasks"].keys():
            st.session_state.desktop_audit_states[task_key] = "Pending"

# ==============================================================================
# SIDEBAR DESKTOP METRIC TELEMETRY
# Displays cached historical claims and live audit metrics on the left panel
# ==============================================================================
with st.sidebar:
    st.markdown("<h3 style='color:#22c55e; font-family:monospace; font-size:16px;'>📊 CACHED TELEMETRY</h3>", unsafe_allow_html=True)
    st.write("Retrieved from 12-month claims database run:")
    
    st.markdown(f"""
    <div style='background-color:rgba(26, 12, 48, 0.9); padding:12px; border-radius:10px; border:1px solid rgba(34,197,94,0.3); margin-bottom:12px;'>
        <div class='sidebar-stat-label'>Claims Analyzed</div>
        <div class='sidebar-stat-val'>{claims_metrics['total_claims_analyzed']}</div>
    </div>
    <div style='background-color:rgba(26, 12, 48, 0.9); padding:12px; border-radius:10px; border:1px solid rgba(34,197,94,0.3); margin-bottom:12px;'>
        <div class='sidebar-stat-label'>NCCI Failures</div>
        <div class='sidebar-stat-val'>{claims_metrics['ncci_edits_failures']}</div>
    </div>
    <div style='background-color:rgba(26, 12, 48, 0.9); padding:12px; border-radius:10px; border:1px solid rgba(34,197,94,0.3); margin-bottom:12px;'>
        <div class='sidebar-stat-label'>Telehealth Mismatch</div>
        <div class='sidebar-stat-val'>{claims_metrics['telehealth_billing_errors']}</div>
    </div>
    <div style='background-color:rgba(26, 12, 48, 0.9); padding:12px; border-radius:10px; border:1px solid rgba(34,197,94,0.3); margin-bottom:12px;'>
        <div class='sidebar-stat-label'>Baseline Median TAT</div>
        <div class='sidebar-stat-val'>{claims_metrics['average_report_tat_days']} days</div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<hr style='border-color:rgba(34,197,94,0.2);'>", unsafe_allow_html=True)
    st.markdown("<span style='font-size:10px; color:#A0AEC0;'>PC Digital Scribing Systems v5.0 Connected</span>", unsafe_allow_html=True)

# ==============================================================================
# MAIN DESKTOP HEADER DISPLAY
# ==============================================================================
st.markdown("""
<div class="desktop-header">
    <div class="desktop-title">CNS_CLINICAL_SYSTEMS_AUDIT</div>
    <div class="desktop-subtitle">Desktop Appraisal Terminal & Executive Reporting Interface</div>
</div>
""", unsafe_allow_html=True)

# ==============================================================================
# DESKTOP STANDARD HORIZONTAL NAVIGATION (4 TABS)
# Prevents any vertical compression or screen restriction
# ==============================================================================
tab_p1, tab_p2, tab_p3, tab_report = st.tabs([
    "Phase 1: Discovery (Days 1–30)",
    "Phase 2: Optimization (Days 31–60)",
    "Phase 3: Sustainability (Days 61–90)",
    "Progress & Findings Report"
])

# ==============================================================================
# TAB 1: PHASE 1 DISCOVERY
# ==============================================================================
with tab_p1:
    st.markdown(f"### **{audit_db['Phase 1']['title']}**")
    
    # Overview popover
    with st.popover("🔬 CLICK FOR PHASE I DIAGNOSTIC BLUEPRINT"):
        st.markdown('<div class="pc-popover-header">PHASE I DIRECTIVE & PURPOSE</div>', unsafe_allow_html=True)
        st.markdown(f"""
        <div class="popover-body">
            <strong>Strategic Focus:</strong> {audit_db["Phase 1"]["objective"]}<br><br>
            <strong>Operational Rationale:</strong> {audit_db["Phase 1"]["rationale"]}
        </div>
        """, unsafe_allow_html=True)
        
    st.write("Audit and track baseline findings. Use popover info boxes to view compliance rationales.")
    st.markdown('<div class="pc-divider"></div>', unsafe_allow_html=True)

    phase_tasks = audit_db["Phase 1"]["tasks"]
    for t_key, t_val in phase_tasks.items():
        st.markdown('<div class="desktop-card">', unsafe_allow_html=True)
        
        # Grid Layout for Wide PC screens
        col_meta, col_interactive = st.columns([2, 3])
        
        with col_meta:
            st.markdown(f'<div class="pc-badge-policy">{t_val["policy"]}</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="pc-badge-target">KPI Target: {t_val["target"]}</div>', unsafe_allow_html=True)
            st.markdown(f"##### **{t_val['label']}**")
            st.write(f"*{t_val['desc']}*")
            
        with col_interactive:
            # Inline popover bubble window inside the task card
            col_pop, col_sel = st.columns([1, 2])
            with col_pop:
                with st.popover("[INFO]"):
                    st.markdown('<div class="pc-popover-header">SYSTEMIC REASONING</div>', unsafe_allow_html=True)
                    st.markdown(f'<div class="popover-body"><strong>Task:</strong> {t_val["desc"]}<br><br><strong>Why This Matters:</strong> {t_val["rationale"]}</div>', unsafe_allow_html=True)
            with col_sel:
                curr_status = st.session_state.desktop_audit_states[t_key]
                selected_status = st.selectbox(
                    "Compliance Status",
                    ["Pending", "Compliant", "Outside of Compliance"],
                    index=["Pending", "Compliant", "Outside of Compliance"].index(curr_status),
                    key=f"pc_sel_{t_key}",
                    label_visibility="collapsed"
                )
                st.session_state.desktop_audit_states[t_key] = selected_status

            # Dynamic Remediation alert below the selectors if Non-Compliant
            if selected_status == "Outside of Compliance":
                st.markdown(
                    f'<div class="pc-remediation-banner">'
                    f'🚨 <strong>CORRECTIVE MITIGATION DIRECTIVE:</strong> {t_val["remediation"]}'
                    f'</div>',
                    unsafe_allow_html=True
                )
                
        st.markdown('</div>', unsafe_allow_html=True)
        
    st.markdown('<div class="pc-divider"></div>', unsafe_allow_html=True)
    
    # CliftonStrengths Block for Phase 1
    st.markdown(f"#### **{audit_db['Phase 1']['strengths']['header']}**")
    st.write(audit_db["Phase 1"]["strengths"]["desc"])
    col_str1, col_str2 = st.columns(2)
    with col_str1:
        st.markdown(f"<div style='background-color:rgba(78,20,111,0.2); padding:16px; border-radius:12px; border-left:4px solid #9C27B0;'>{audit_db['Phase 1']['strengths']['examples'][0]}</div>", unsafe_allow_html=True)
    with col_str2:
        st.markdown(f"<div style='background-color:rgba(34,197,94,0.05); padding:16px; border-radius:12px; border-left:4px solid #22c55e;'>{audit_db['Phase 1']['strengths']['examples'][1]}</div>", unsafe_allow_html=True)

# ==============================================================================
# TAB 2: PHASE 2 OPTIMIZATION
# ==============================================================================
with tab_p2:
    st.markdown(f"### **{audit_db['Phase 2']['title']}**")
    
    with st.popover("🔬 CLICK FOR PHASE II DIAGNOSTIC BLUEPRINT"):
        st.markdown('<div class="pc-popover-header">PHASE II DIRECTIVE & PURPOSE</div>', unsafe_allow_html=True)
        st.markdown(f"""
        <div class="popover-body">
            <strong>Strategic Focus:</strong> {audit_db["Phase 2"]["objective"]}<br><br>
            <strong>Operational Rationale:</strong> {audit_db["Phase 2"]["rationale"]}
        </div>
        """, unsafe_allow_html=True)

    # CARRYOVER CHECK FROM PHASE 1 TO PHASE 2
    p1_non_compliant_keys = [tk for tk in audit_db["Phase 1"]["tasks"].keys() if st.session_state.desktop_audit_states[tk] == "Outside of Compliance"]
    if p1_non_compliant_keys:
        st.markdown('<div class="pc-cascade-alert">', unsafe_allow_html=True)
        st.markdown("⚠️ <strong>CRITICAL DATA CARRYOVER ALERT: UNRESOLVED BASELINE LIABILITIES FOUND</strong>", unsafe_allow_html=True)
        st.write("The following baseline audit criteria are currently Outside of Compliance, directly compromising your optimization phase:")
        for tk in p1_non_compliant_keys:
            st.markdown(f"• **{audit_db['Phase 1']['tasks'][tk]['label']}** — *Unresolved regulatory risk threatens implementation validity.*")
        st.markdown("</div>", unsafe_allow_html=True)
    else:
        st.markdown('<div style="background-color: rgba(34, 197, 94, 0.08); padding: 12px; border-radius: 12px; border-left: 5px solid #22c55e; border: 1px solid rgba(34, 197, 94, 0.2); margin-bottom: 20px; font-size: 12px; color: #22c55e;">✓ <strong>All Phase I Baselines are Verified & Compliant.</strong> Clinical Optimization templates ready for deployment.</div>', unsafe_allow_html=True)

    st.markdown('<div class="pc-divider"></div>', unsafe_allow_html=True)

    phase_tasks = audit_db["Phase 2"]["tasks"]
    for t_key, t_val in phase_tasks.items():
        st.markdown('<div class="desktop-card">', unsafe_allow_html=True)
        
        col_meta, col_interactive = st.columns([2, 3])
        
        with col_meta:
            st.markdown(f'<div class="pc-badge-policy">{t_val["policy"]}</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="pc-badge-target">KPI Target: {t_val["target"]}</div>', unsafe_allow_html=True)
            st.markdown(f"##### **{t_val['label']}**")
            st.write(f"*{t_val['desc']}*")
            
        with col_interactive:
            col_pop, col_sel = st.columns([1, 2])
            with col_pop:
                with st.popover("[INFO]"):
                    st.markdown('<div class="pc-popover-header">SYSTEMIC REASONING</div>', unsafe_allow_html=True)
                    st.markdown(f'<div class="popover-body"><strong>Task:</strong> {t_val["desc"]}<br><br><strong>Why This Matters:</strong> {t_val["rationale"]}</div>', unsafe_allow_html=True)
            with col_sel:
                curr_status = st.session_state.desktop_audit_states[t_key]
                selected_status = st.selectbox(
                    "Compliance Status",
                    ["Pending", "Compliant", "Outside of Compliance"],
                    index=["Pending", "Compliant", "Outside of Compliance"].index(curr_status),
                    key=f"pc_sel_{t_key}",
                    label_visibility="collapsed"
                )
                st.session_state.desktop_audit_states[t_key] = selected_status

            if selected_status == "Outside of Compliance":
                st.markdown(
                    f'<div class="pc-remediation-banner">'
                    f'🚨 <strong>CORRECTIVE MITIGATION DIRECTIVE:</strong> {t_val["remediation"]}'
                    f'</div>',
                    unsafe_allow_html=True
                )
                
        st.markdown('</div>', unsafe_allow_html=True)
        
    st.markdown('<div class="pc-divider"></div>', unsafe_allow_html=True)
    
    # CliftonStrengths Block for Phase 2
    st.markdown(f"#### **{audit_db['Phase 2']['strengths']['header']}**")
    st.write(audit_db["Phase 2"]["strengths"]["desc"])
    col_str1, col_str2 = st.columns(2)
    with col_str1:
        st.markdown(f"<div style='background-color:rgba(78,20,111,0.2); padding:16px; border-radius:12px; border-left:4px solid #9C27B0;'>{audit_db['Phase 2']['strengths']['examples'][0]}</div>", unsafe_allow_html=True)
    with col_str2:
        st.markdown(f"<div style='background-color:rgba(34,197,94,0.05); padding:16px; border-radius:12px; border-left:4px solid #22c55e;'>{audit_db['Phase 2']['strengths']['examples'][1]}</div>", unsafe_allow_html=True)

# ==============================================================================
# TAB 3: PHASE 3 SUSTAINABILITY
# ==============================================================================
with tab_p3:
    st.markdown(f"### **{audit_db['Phase 3']['title']}**")
    
    with st.popover("🔬 CLICK FOR PHASE III DIAGNOSTIC BLUEPRINT"):
        st.markdown('<div class="pc-popover-header">PHASE III DIRECTIVE & PURPOSE</div>', unsafe_allow_html=True)
        st.markdown(f"""
        <div class="popover-body">
            <strong>Strategic Focus:</strong> {audit_db["Phase 3"]["objective"]}<br><br>
            <strong>Operational Rationale:</strong> {audit_db["Phase 3"]["rationale"]}
        </div>
        """, unsafe_allow_html=True)

    # CARRYOVER CHECK FROM PHASE 2 TO PHASE 3
    p2_non_compliant_keys = [tk for tk in audit_db["Phase 2"]["tasks"].keys() if st.session_state.desktop_audit_states[tk] == "Outside of Compliance"]
    if p2_non_compliant_keys:
        st.markdown('<div class="pc-cascade-alert">', unsafe_allow_html=True)
        st.markdown("⚠️ <strong>CRITICAL DATA CARRYOVER ALERT: UNRESOLVED PROCESS GAPS FOUND</strong>", unsafe_allow_html=True)
        st.write("The following clinical-RCM optimization steps are Outside of Compliance, threatening long-term sustainability:")
        for tk in p2_non_compliant_keys:
            st.markdown(f"• **{audit_db['Phase 2']['tasks'][tk]['label']}** — *Unresolved risk of billing denials or clinic revenue leakage.*")
        st.markdown("</div>", unsafe_allow_html=True)
    else:
        st.markdown('<div style="background-color: rgba(34, 197, 94, 0.08); padding: 12px; border-radius: 12px; border-left: 5px solid #22c55e; border: 1px solid rgba(34, 197, 94, 0.2); margin-bottom: 20px; font-size: 12px; color: #22c55e;">✓ <strong>All Phase II systems are verified and compliant.</strong> Transitioning cleanly into Phase III long-term roadmap synthesis.</div>', unsafe_allow_html=True)

    st.markdown('<div class="pc-divider"></div>', unsafe_allow_html=True)

    phase_tasks = audit_db["Phase 3"]["tasks"]
    for t_key, t_val in phase_tasks.items():
        st.markdown('<div class="desktop-card">', unsafe_allow_html=True)
        
        col_meta, col_interactive = st.columns([2, 3])
        
        with col_meta:
            st.markdown(f'<div class="pc-badge-policy">{t_val["policy"]}</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="pc-badge-target">KPI Target: {t_val["target"]}</div>', unsafe_allow_html=True)
            st.markdown(f"##### **{t_val['label']}**")
            st.write(f"*{t_val['desc']}*")
            
        with col_interactive:
            col_pop, col_sel = st.columns([1, 2])
            with col_pop:
                with st.popover("[INFO]"):
                    st.markdown('<div class="pc-popover-header">SYSTEMIC REASONING</div>', unsafe_allow_html=True)
                    st.markdown(f'<div class="popover-body"><strong>Task:</strong> {t_val["desc"]}<br><br><strong>Why This Matters:</strong> {t_val["rationale"]}</div>', unsafe_allow_html=True)
            with col_sel:
                curr_status = st.session_state.desktop_audit_states[t_key]
                selected_status = st.selectbox(
                    "Compliance Status",
                    ["Pending", "Compliant", "Outside of Compliance"],
                    index=["Pending", "Compliant", "Outside of Compliance"].index(curr_status),
                    key=f"pc_sel_{t_key}",
                    label_visibility="collapsed"
                )
                st.session_state.desktop_audit_states[t_key] = selected_status

            if selected_status == "Outside of Compliance":
                st.markdown(
                    f'<div class="pc-remediation-banner">'
                    f'🚨 <strong>CORRECTIVE MITIGATION DIRECTIVE:</strong> {t_val["remediation"]}'
                    f'</div>',
                    unsafe_allow_html=True
                )
                
        st.markdown('</div>', unsafe_allow_html=True)
        
    st.markdown('<div class="pc-divider"></div>', unsafe_allow_html=True)
    
    # CliftonStrengths Block for Phase 3
    st.markdown(f"#### **{audit_db['Phase 3']['strengths']['header']}**")
    st.write(audit_db["Phase 3"]["strengths"]["desc"])
    col_str1, col_str2 = st.columns(2)
    with col_str1:
        st.markdown(f"<div style='background-color:rgba(78,20,111,0.2); padding:16px; border-radius:12px; border-left:4px solid #9C27B0;'>{audit_db['Phase 3']['strengths']['examples'][0]}</div>", unsafe_allow_html=True)
    with col_str2:
        st.markdown(f"<div style='background-color:rgba(34,197,94,0.05); padding:16px; border-radius:12px; border-left:4px solid #22c55e;'>{audit_db['Phase 3']['strengths']['examples'][1]}</div>", unsafe_allow_html=True)

# ==============================================================================
# TAB 4: PROGRESS & FINDINGS REPORT (EXECUTIVE DASHBOARD)
# ==============================================================================
with tab_report:
    st.markdown('<div class="pc-divider"></div>', unsafe_allow_html=True)
    
    # Stylized Executive Header
    st.markdown("""
    <div style="text-align: center; border: 2px solid rgba(34, 197, 94, 0.4); padding: 18px; border-radius: 16px; background-color: rgba(26, 12, 48, 0.95); margin-bottom: 24px; box-shadow: 0 0 25px rgba(34, 197, 94, 0.15);">
        <h3 style="color: #FFFFFF; margin: 0; font-weight: 900; font-family: monospace; font-size:18px; letter-spacing: 2px; text-shadow: 0 0 10px rgba(34, 197, 94, 0.6);">CNS HEALTHCARE PSYCHOLOGICAL SERVICES</h3>
        <h4 style="color: #22c55e; margin: 4px 0 0 0; font-weight: 700; font-family: monospace; font-size:13px; letter-spacing: 1.5px;">EXECUTIVE COMPLIANCE APPRAISAL STATUS REPORT</h4>
        <p style="color: #E1BEE7; font-size: 11px; margin: 8px 0 0 0; font-family: monospace; line-height: 1.4;">Prepared for: Provider Clinical Supervisors, Directors, and Executive Board Members<br>Auditor: Dr. Scott Niewinski, Psy.D., Manager of Psychological Services</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Calculate Live Stats
    all_appraisal_tasks = []
    compliant_list = []
    non_compliant_list = []
    pending_list = []
    
    for phase_key, phase_val in audit_db.items():
        for task_key, task_val in phase_val["tasks"].items():
            status = st.session_state.desktop_audit_states[task_key]
            task_entry = {"info": task_val, "phase": phase_val["title"]}
            all_appraisal_tasks.append(task_entry)
            if status == "Compliant":
                compliant_list.append(task_entry)
            elif status == "Outside of Compliance":
                non_compliant_list.append(task_entry)
            else:
                pending_list.append(task_entry)
                
    total_count = len(all_appraisal_tasks)
    rate_compliance = (len(compliant_list) / total_count) * 100 if total_count > 0 else 0
    
    # Desktop Row metrics display
    col_metric1, col_metric2, col_metric3 = st.columns(3)
    with col_metric1:
        st.metric("VERIFIED COMPLIANCE RATE", f"{rate_compliance:.1f}%", f"{len(compliant_list)}/{total_count} Objectives Passed")
    with col_metric2:
        st.metric("CRITICAL GAPS IDENTIFIED", f"{len(non_compliant_list)} Active Gaps", delta="- Risk Action Required", delta_color="inverse")
    with col_metric3:
        st.metric("PENDING BASELINE EVALUATIONS", f"{len(pending_list)} Tasks Remaining")
        
    st.progress(len(compliant_list) / total_count if total_count > 0 else 0)
    st.markdown('<div class="pc-divider"></div>', unsafe_allow_html=True)
    
    # Splitting findings layout into double column on PC screens
    col_report_left, col_report_right = st.columns(2)
    
    with col_report_left:
        st.markdown("### **🟢 VERIFIED COMPLIANT SYSTEMS**")
        if compliant_list:
            for item in compliant_list:
                st.markdown(f"""
                <div style='background-color: rgba(34, 197, 94, 0.05); border: 1px solid rgba(34, 197, 94, 0.3); border-radius: 12px; padding: 14px; margin-bottom: 12px;'>
                    <strong style='color:#22c55e;'>✓ {item['info']['label']}</strong><br>
                    <span style='font-size:10px; color:#A0AEC0; font-family: monospace;'>Phase: {item['phase']}</span><br>
                    <span style='font-size:11px; color:#FFFFFF;'>Policy Alignment: {item['info']['policy']}</span>
                </div>
                """, unsafe_allow_html=True)
        else:
            st.write("No clinical systems have been validated as compliant yet. Audit selections required.")

    with col_report_right:
        st.markdown("### **🔴 CRITICAL VULNERABILITIES & REMEDIATION PLAN**")
        if non_compliant_list:
            for item in non_compliant_list:
                st.markdown(f"""
                <div style='background-color: rgba(239, 68, 68, 0.05); border: 1px solid rgba(239, 68, 68, 0.3); border-radius: 12px; padding: 14px; margin-bottom: 12px;'>
                    <strong style='color:#EF4444;'>🚨 [GAP DETECTED] {item['info']['label']}</strong><br>
                    <span style='font-size:10px; color:#E1BEE7; font-family: monospace;'>Phase Location: {item['phase']}</span><br>
                    <p style='margin: 8px 0 4px 0; font-size:12px; color: #E2E8F0;'><strong>Regulatory Standard:</strong> {item['info']['policy']}</p>
                    <p style='margin: 4px 0 4px 0; font-size:12px; color: #22c55e; font-family: monospace;'><strong>Target Metric:</strong> {item['info']['target']}</p>
                    <p style='margin: 4px 0 8px 0; font-size:12px; color: #FEE2E2;'><strong>Vulnerability:</strong> {item['info']['rationale']}</p>
                    <div class="pc-remediation-banner" style='margin-top:4px;'>
                        <strong>🛠️ MANDATORY ACTION:</strong> {item['info']['remediation']}
                    </div>
                </div>
                """, unsafe_allow_html=True)
        else:
            if len(compliant_list) == total_count:
                st.success("🎉 Outstanding Quality Control! All clinical, financial, and licensing pipelines are verified as 100% compliant with state and federal regulations.")
            else:
                st.info("Pending task reviews. Resolve outstanding baselines and evaluations to finalize the remediation plan.")

# Sticky Scientific PC Footer
st.markdown("<hr style='margin-top: 40px; border-color: rgba(34, 197, 94, 0.25);'>", unsafe_allow_html=True)
st.markdown(
    '<div style="font-size:11px; color:#A0AEC0; text-align:center; padding-bottom:20px; font-family: monospace;">'
    'CNS Healthcare Appraisal Systems • Strictly Grounded in "90-Day Psychological Services Appraisal Plan.docx"</div>',
    unsafe_allow_html=True
)
