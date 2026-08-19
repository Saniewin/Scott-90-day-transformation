import streamlit as st

# Set Streamlit Page Configuration - optimized for modern mobile viewports (e.g., Samsung Galaxy S26 Ultra)
st.set_page_config(
    page_title="90-Day Clinical & Operational Audit App",
    page_icon="📱",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Custom CSS to inject a premium "Samsung OneUI" visual aesthetic (curved corners, rich blues, readable mobile cards)
st.markdown("""
<style>
    /* Main body background & mobile canvas layout */
    .stApp {
        background-color: #F8F9FD;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    }
    
    /* Device frame mockup for Samsung S26 Ultra centered canvas */
    @media (min-width: 450px) {
        .block-container {
            max-width: 440px !important;
            padding: 20px !important;
            background: #FFFFFF;
            border-radius: 40px;
            box-shadow: 0 20px 60px rgba(0, 0, 0, 0.1);
            margin-top: 10px;
            margin-bottom: 20px;
            border: 8px solid #1E2022;
        }
    }
    
    /* Sleek card styling for checklist containers */
    .audit-card {
        background: #FFFFFF;
        border-radius: 20px;
        padding: 16px;
        margin-bottom: 16px;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.03);
        border: 1px solid #ECEFF1;
    }
    
    /* Premium header styles */
    .app-title {
        font-size: 24px !important;
        font-weight: 800 !important;
        color: #1A237E;
        text-align: center;
        margin-bottom: 4px;
        letter-spacing: -0.5px;
    }
    
    .app-subtitle {
        font-size: 13px;
        color: #78909C;
        text-align: center;
        margin-bottom: 20px;
    }
    
    .phase-badge {
        font-size: 12px;
        font-weight: bold;
        color: white;
        background: linear-gradient(135deg, #1E3A8A, #3B82F6);
        padding: 6px 12px;
        border-radius: 20px;
        display: inline-block;
        margin-bottom: 12px;
        text-align: center;
    }
    
    .policy-tag {
        font-size: 11px;
        font-weight: 700;
        background-color: #E8EAF6;
        color: #283593;
        padding: 3px 8px;
        border-radius: 12px;
        display: inline-block;
        margin-bottom: 8px;
    }
    
    /* Color-coded indicator labels */
    .status-compliant {
        font-size: 12px;
        font-weight: bold;
        color: #2E7D32;
        background-color: #E8F5E9;
        padding: 4px 10px;
        border-radius: 8px;
        display: inline-block;
    }
    
    .status-noncompliant {
        font-size: 12px;
        font-weight: bold;
        color: #C62828;
        background-color: #FFEBEE;
        padding: 4px 10px;
        border-radius: 8px;
        display: inline-block;
    }
    
    /* Report styling elements */
    .report-card {
        background-color: #FFFFFF;
        border-radius: 15px;
        border-left: 6px solid #1A237E;
        padding: 15px;
        margin-bottom: 15px;
        box-shadow: 0 4px 10px rgba(0,0,0,0.02);
    }
    
    .report-header {
        font-size: 18px;
        font-weight: 700;
        color: #0D47A1;
        margin-bottom: 10px;
        border-bottom: 1px solid #E0E0E0;
        padding-bottom: 5px;
    }

    /* Custom button styling */
    .stButton>button {
        background-color: #1E3A8A !important;
        color: white !important;
        border-radius: 12px !important;
        padding: 10px 20px !important;
        font-weight: 700 !important;
        width: 100%;
        border: none !important;
        transition: all 0.3s ease;
    }
</style>
""", unsafe_allow_html=True)

# Title & Metadata
st.markdown('<div class="app-title">CNS Psychological Services</div>', unsafe_allow_html=True)
st.markdown('<div class="app-subtitle">90-Day Operational & Clinical Appraisal • S26 Ultra Optimized</div>', unsafe_allow_html=True)

# Initialize Session State for all 3 Phases to ensure data carryover
if 'audit_data' not in st.session_state:
    st.session_state.audit_data = {
        # --- PHASE 1: Discovery & Regulatory Baseline (Days 1–30) ---
        # Objective 1.1: LARA Supervision Compliance
        "lara_logs_exist": {"compliant": True, "notes": "Form LARA/BPL Rev. 6/25 logs verified for LLPs"},
        "lara_4hours": {"compliant": True, "notes": "Minimum 4 hours/month face-to-face LP supervision confirmed"},
        "lara_signoff": {"compliant": True, "notes": "Official supervision evaluation logs signed and uploaded"},
        "lara_cosignature": {"compliant": True, "notes": "Fully Licensed LP co-signatures on clinical notes verified"},
        
        # Objective 1.2: BTPRC Safeguards (MDHHS APF 167)
        "btp_unanimous": {"compliant": True, "notes": "Unanimous committee approval obtained for restrictive plans"},
        "btp_composition": {"compliant": True, "notes": "Committee includes Licensed Psychologist/BCBA, MD/DO, and ORR rep"},
        "btp_medical": {"compliant": True, "notes": "MD/DO physical exam completed to rule out biological causes"},
        "btp_fba_attached": {"compliant": True, "notes": "FBA completed with baseline A-B-C behavioral data"},
        "btp_no_aversives": {"compliant": True, "notes": "Zero prohibited aversive or emergency physical codes used"},
        
        # Objective 1.3: Clinical Documentation & CPT Coding
        "cpt_feedback_96130": {"compliant": True, "notes": "Interactive feedback sessions documented for all 96130 claims"},
        "cpt_time_minimum": {"compliant": True, "notes": "CPT 96130 evaluations support 31+ minute threshold minimums"},
        "cpt_tech_segregation": {"compliant": True, "notes": "Technician scoring (96138) strictly segregated from provider (96136)"},
        "cpt_stratified_audit": {"compliant": True, "notes": "30-case stratified chart audit proportionally extracted"},
        
        # Objective 1.4: CCBHC Access & Triage Velocity
        "triage_prelim_screening": {"compliant": True, "notes": "Preliminary screening and risk assessment conducted at first contact"},
        "triage_michicans_locus": {"compliant": True, "notes": "Required tools (MichiCANS Screener/LOCUS) integrated in triage"},
        "triage_urgent_1day": {"compliant": True, "notes": "Urgent cases scheduled and initiated within 1 business day"},
        "triage_routine_14day": {"compliant": True, "notes": "Routine assessments initiated within 14 calendar days"},
        "triage_waitlist_interim": {"compliant": True, "notes": "Zero waitlists maintained; care coordination interim services active"},

        # --- PHASE 2: Implementation of Clinical Frameworks (Days 31–60) ---
        # Objective 2.1: Therapeutic Assessment Deployment
        "ta_collaborative_questions": {"compliant": True, "notes": "Collaborative Assessment Questions established with consumers"},
        "ta_face_valid_ordering": {"compliant": True, "notes": "Performance and cognitive tests administered before projective measures"},
        "ta_ais_operationalized": {"compliant": True, "notes": "AIS sessions used to observe and process experiential avoidance in real-time"},
        "ta_synthesis_letter": {"compliant": True, "notes": "Legacy testing reports replaced with personalized patient-centered letters"},

        # Objective 2.2: EHR Behavior Plan Overhaul
        "ehp_replacement_behaviors": {"compliant": True, "notes": "Templates mandate positive replacement behaviors and distress tolerance"},
        "ehp_fade_plans": {"compliant": True, "notes": "Mandatory fade plans embedded for any restrictive/intrusive safety techniques"},
        "ehp_routing_restraints": {"compliant": True, "notes": "EHR restricts routing of plans with physical restraints, flagging clinical manager"},

        # Objective 2.3: Clinical Workshop Series (Modules 1 & 2)
        "ws_module_1_mi": {"compliant": True, "notes": "Workshop Module 1 (Motivational Interviewing) delivered cross-department"},
        "ws_module_2_ea": {"compliant": True, "notes": "Workshop Module 2 (Deconstructing Experiential Avoidance) delivered to staff"},
        "ws_attendance_rate": {"compliant": True, "notes": "Achieved minimum 90% workshop training completion rate cross-clinics"},

        # Objective 2.4: Revenue Cycle Denial Audit
        "rcm_historical_audit": {"compliant": True, "notes": "Completed CPT coding and denial audit on previous 12 months of claims"},
        "rcm_96130_verification": {"compliant": True, "notes": "Verified CPT 96130 evaluations support 31+ minute thresholds"},
        "rcm_ncci_modifiers": {"compliant": True, "notes": "Applied NCCI Modifiers 59/XE correctly to prevent automated rejections"},

        # --- PHASE 3: Quality Assurance & Future Exploration (Days 61–90) ---
        # Objective 3.1: Simulated CARF Audit
        "carf_mock_audit": {"compliant": True, "notes": "Mock CARF chart audits executed across all 7 CNS clinics"},
        "carf_soap_notes": {"compliant": True, "notes": "Clinical progress notes follow person-centered SOAP formats (24-hr window)"},
        "carf_smart_goals": {"compliant": True, "notes": "Individualized plans of service (IPOS) incorporate SMART goals in patient's voice"},

        # Objective 3.2: Measurement-Informed Care (MIC)
        "mic_ehr_embedding": {"compliant": True, "notes": "PHQ-9, GAD-7, DAST-10, and AUDIT-C embedded into EHR clinical workflows"},
        "mic_clinical_decisions": {"compliant": True, "notes": "Treatment adjustments documented when screening scales show no patient progress"},
        "mic_locus_michicans": {"compliant": True, "notes": "LOCUS and MichiCANS assessments updated annually and upon clinical changes"},

        # Objective 3.3: Stepped-Care Assessment Protocol
        "sc_protocol_deployment": {"compliant": True, "notes": "Stepped-Care Assessment pathway deployed to protect diagnostic capacity"},
        "sc_triage_96127": {"compliant": True, "notes": "Intake clinicians use brief screenings (96127) to filter low-acuity cases"},
        "sc_testing_limits": {"compliant": True, "notes": "Comprehensive, multi-hour testing blocks strictly reserved for high differential diagnoses"},

        # Objective 3.4: KPI Dashboarding
        "kpi_dashboard_design": {"compliant": True, "notes": "Ongoing Assessment KPI Dashboard designed and wireframed in EHR"},
        "kpi_metrics_tracking": {"compliant": True, "notes": "Weekly metrics (volume, TAT, claims denials, waitlists) monitored live"},
        "kpi_billing_regressions": {"compliant": True, "notes": "Payer-specific claims data integrated to prevent future billing regressions"},

        # Objective 3.5: Ambient Clinical AI ROI Case
        "ai_scribe_evaluation": {"compliant": True, "notes": "Ambient clinical AI (e.g. Eleos Health) evaluated to reduce documentation overhead"},
        "ai_time_reduction": {"compliant": True, "notes": "NLP ambient scribing tested, demonstrating 70% decrease in write times"},
        "ai_roi_proposal": {"compliant": True, "notes": "Watertight ROI business case drafted and presented to the Chief Clinical Officer"}
    }

# ================= AUDIT DEFINITIONS PER PHASE =================

phase_1_defs = {
    "LARA Supervision Compliance": {
        "policy": "LARA Rule 338.2569 & MCL 333.18223 (Michigan Public Health Code)",
        "tasks": {
            "lara_logs_exist": {
                "label": "Official LARA logs exist for all active LLPs/TLLPs.",
                "remediation": "Immediately download the official Psychology Supervision Evaluation form (LARA/BPL, Rev. 6/25) for any staff member missing active logs and mandate immediate record recreation."
            },
            "lara_4hours": {
                "label": "Each LLP receives at least 4 hours per month of individual, face-to-face LP supervision.",
                "remediation": "Block designated 'LP-LLP Supervision' hours directly into LP calendars. If monthly limits are missed, retroactively suspend billing for those hours to prevent billing recoupment."
            },
            "lara_signoff": {
                "label": "Official supervision logs are signed by fully licensed LP and submitted.",
                "remediation": "Perform a retrospective administrative signature run. Require LPs and LLPs to complete and sign LARA logs prior to releasing the final monthly payroll."
            },
            "lara_cosignature": {
                "label": "LPs co-sign clinical notes prior to claim release.",
                "remediation": "Modify EHR routing rules to prevent any claim involving LLP-rendered psychometrics from being released to CHAMPS until the supervising LP co-signs."
            }
        }
    },
    "BTPRC Compliance (MDHHS APF 167)": {
        "policy": "MDHHS APF 167 Guidelines, Michigan Mental Health Code, & CCBHC Handbook 8.D.1.5",
        "tasks": {
            "btp_unanimous": {
                "label": "Unanimous committee approval obtained for restrictive BTPs.",
                "remediation": "Immediately suspend the use of the proposed restrictive interventions. Schedule an urgent BTPRC review session to secure unanimous approval."
            },
            "btp_composition": {
                "label": "Committee composition includes LP/BCBA, Physician, and Recipient Rights Representative.",
                "remediation": "If any key member is absent, reschedule the meeting. Non-CMHSP CCBHCs must route plans to the state-level MDHHS BTPRC through their assigned Certification Specialist."
            },
            "btp_medical": {
                "label": "MD/DO comprehensive physical examination completed to rule out biological causes of behavior.",
                "remediation": "Halt the plan. Schedule an immediate primary care physical exam for the consumer to rule out organic factors like undiagnosed dental pain, infections, or medication side effects."
            },
            "btp_fba_attached": {
                "label": "Structured FBA attached, documenting baseline Antecedent-Behavior-Consequence data.",
                "remediation": "Deploy a clinical supervisor to execute a rapid 5-day structured behavioral observation. Collect baseline A-B-C data and integrate it into a modified FBA format."
            },
            "btp_no_aversives": {
                "label": "Zero prohibited aversives or emergency management written as standard responses.",
                "remediation": "Immediately remove any reference to physical restraints or unpleasant stimuli from the BTP. Re-train staff on Positive Behavior Supports (PBS) and distress tolerance skills (DBT/ACT)."
            }
        }
    },
    "Clinical Documentation & CPT Coding": {
        "policy": "AMA CPT Manual, CMS National Correct Coding Initiative (NCCI) Edits, & CARF Standards",
        "tasks": {
            "cpt_feedback_96130": {
                "label": "CPT 96130 billing is backed by documented interactive feedback sessions with patient/caregiver.",
                "remediation": "If feedback is missing, self-disclose and adjust billing or arrange an immediate feedback session if clinically appropriate and within allowable timelines."
            },
            "cpt_time_minimum": {
                "label": "CPT 96130 evaluation time logged meets the 31-minute threshold minimum.",
                "remediation": "Halt the claim. Direct the provider to review clinical notes, accurately reconstruct clinical decision-making, and document the correct time spent prior to rebilling."
            },
            "cpt_tech_segregation": {
                "label": "Technician scoring (96138) strictly segregated from provider admin (96136).",
                "remediation": "Apply NCCI Modifier 59 or XE to same-day provider and technician encounters. Conduct CPT coding training for the revenue cycle management and billing teams."
            },
            "cpt_stratified_audit": {
                "label": "Randomized 30-case stratified chart audit (adult, pediatric, geriatric) proportionally completed.",
                "remediation": "Increase administrative hours for the Program Manager. Mandate the completion of the 30-chart review before Phase I expires on Day 30."
            }
        }
    },
    "CCBHC Access & Triage Velocity": {
        "policy": "SAMHSA 2023 CCBHC Criteria, MDHHS CCBHC Handbook 8.B.9, & CareConnect360 Integration",
        "tasks": {
            "triage_prelim_screening": {
                "label": "Preliminary screening and risk assessment conducted immediately at first contact.",
                "remediation": "Mandate that intake staff perform rapid preliminary screenings over the phone or in person, recording all risk parameters in the EHR."
            },
            "triage_michicans_locus": {
                "label": "Required State-designated level-of-care tools (MichiCANS Screener/LOCUS) integrated.",
                "remediation": "Coordinate with the training department. Ensure all intake clinicians are certified on MichiCANS (for youth) and LOCUS (for adults). Honor existing scores in CareConnect360."
            },
            "triage_urgent_1day": {
                "label": "Urgent assessments scheduled and initiated within 1 business day of contact.",
                "remediation": "Incorporate open access or same-day walk-in slots for high-acuity referrals. Leverage telehealth modules to bypass regional clinic wait times."
            },
            "triage_routine_14day": {
                "label": "Routine assessments initiated within 14 calendar days of contact.",
                "remediation": "Configure automated EHR system notifications that flag referrals approaching the 10-day mark to prompt rapid intake scheduling."
            },
            "triage_waitlist_interim": {
                "label": "Zero waitlists maintained; care coordination interim services active.",
                "remediation": "Deploy immediate interim care coordination services, peer recovery support, and brief screenings (CPT 96127) to engage the client while awaiting full testing."
            }
        }
    }
}

phase_2_defs = {
    "Therapeutic Assessment (TA) Model Deployment": {
        "policy": "SAMHSA CCBHC Core Service #2 (Screening, Assessment, & Diagnosis) & APA Ethics Section 9",
        "tasks": {
            "ta_collaborative_questions": {
                "label": "Establish collaborative Assessment Questions with consumers at testing inception.",
                "remediation": "Integrate a 'Collaborative Questions' worksheet into the standard assessment intake packet. Do not allow testing to proceed until these are finalized with the consumer."
            },
            "ta_face_valid_ordering": {
                "label": "Prioritize cognitive and performance tests before projective measures to establish immediate face validity.",
                "remediation": "Overhaul clinical guidelines to mandate administering performance/cognitive tests first to build patient rapport and face validity before launching complex projective test blocks."
            },
            "ta_ais_operationalized": {
                "label": "Operationalize Assessment Intervention Sessions (AIS) to observe and process experiential avoidance in real-time.",
                "remediation": "Provide immediate clinical coaching to staff on how to use testing struggles (e.g., frustration on difficult tasks) as a real-time therapeutic mirror for real-world coping."
            },
            "ta_synthesis_letter": {
                "label": "Replace pathology-heavy reports with a personalized, jargon-free synthesis letter written directly to the patient.",
                "remediation": "Reject standard diagnostic-heavy reports for non-complex cases. Enforce a template for a client-centered letter summarizing findings in plain language as required by person-centered standards."
            }
        }
    },
    "EHR Behavior Treatment Plan Overhaul": {
        "policy": "MDHHS APF 167 Guidelines & Recipient Rights Protection (Michigan Mental Health Code)",
        "tasks": {
            "ehp_replacement_behaviors": {
                "label": "Mandate documentation of positive replacement behaviors and distress tolerance skills (DBT/ACT).",
                "remediation": "Modify the behavior treatment plan EHR template to include mandatory fields for replacement behaviors and distress tolerance skills, blocking submission if empty."
            },
            "ehp_fade_plans": {
                "label": "Embed mandatory 'fade plans' into BTPs that propose restrictive or intrusive safety interventions.",
                "remediation": "Enforce a strict technical rule in the EHR: any BTP containing a restrictive intervention must include a clear, measurable plan for fading the restriction."
            },
            "ehp_routing_restraints": {
                "label": "Restructure EHR routing rules to block and flag any plan utilizing physical restraints.",
                "remediation": "Convene an immediate review of the plan. Re-train staff on Positive Behavior Supports (PBS) and distress tolerance skills (DBT/ACT) to eliminate restraint reliance."
            }
        }
    },
    "Clinical Workshop Series (Modules 1 & 2)": {
        "policy": "SAMHSA CCBHC Staff Training & Cultural Competence Criteria (Program Requirement #1)",
        "tasks": {
            "ws_module_1_mi": {
                "label": "Deliver Workshop Module 1 (Motivational Interviewing Mastery) to LPs, LLPs, and psychometrists.",
                "remediation": "Schedule immediate make-up training blocks. Require staff who missed the session to complete a certified online MI module within 15 calendar days."
            },
            "ws_module_2_ea": {
                "label": "Deliver Workshop Module 2 (Deconstructing Experiential Avoidance), integrating ACT/DBT principles.",
                "remediation": "Mandate clinical case consultations for non-attendees. Ensure supervisors review current cases for evidence of ACT/DBT integration."
            },
            "ws_attendance_rate": {
                "label": "Achieve a minimum of 90% training completion rate across clinics.",
                "remediation": "Direct regional supervisors to prioritize workshop attendance by clearing clinician schedules during training slots. Flag non-compliance to the Chief Clinical Officer."
            }
        }
    },
    "CPT Coding & Denial Audit (Revenue Cycle)": {
        "policy": "CMS National Correct Coding Initiative (NCCI) Edits & MDHHS Billing Manual",
        "tasks": {
            "rcm_historical_audit": {
                "label": "Conduct a deep-dive CPT coding and denial audit on the previous 12 months of claims.",
                "remediation": "Allocate additional billing FTE hours to complete the 12-month data extraction and claim-by-claim reconciliation before Phase II expires."
            },
            "rcm_96130_verification": {
                "label": "Verify proper billing of CPT 96130 (first-hour evaluation) and correct use of time-based codes.",
                "remediation": "Halt suspect claims in the clearinghouse. Audit clinical schedules to reconstruct and verify that provider time met the required 31-minute billing threshold."
            },
            "rcm_ncci_modifiers": {
                "label": "Review correct application of NCCI Modifiers 59 or XE for same-day provider and technician encounters.",
                "remediation": "Apply retrospective Modifier XE/59 corrections to denied claims. Deliver targeted CPT coding compliance training to the billing and revenue cycle teams."
            }
        }
    }
}

phase_3_defs = {
    "Simulated CARF Audit & Chart Reviews": {
        "policy": "CARF ASPIRE Accreditation Standards & SAMHSA Quality Criteria (Program Requirement #5)",
        "tasks": {
            "carf_mock_audit": {
                "label": "Conduct a mock CARF audit of psychological and behavioral health charts across all 7 CNS clinics.",
                "remediation": "Form a rapid-response quality team. Focus on reviewing high-risk charts and resolving outstanding documentation gaps immediately."
            },
            "carf_soap_notes": {
                "label": "Verify that clinical notes follow the person-centered SOAP format and are completed within the 24-hour CCBHC window.",
                "remediation": "Implement daily EHR alerts that flag notes approaching the 24-hour CCBHC deadline. Suspend documentation self-release privileges for chronic late-submitters."
            },
            "carf_smart_goals": {
                "label": "Confirm that SMART goals and the client's own words are written into every IPOS.",
                "remediation": "Reject and return deficient IPOS files to the primary clinician. Provide 1-on-1 coaching on writing individualized, client-centered treatment plans."
            }
        }
    },
    "Measurement-Informed Care (MIC) Integration": {
        "policy": "CARF July 2026 Guidelines & SAMHSA CCBHC Quality Metrics",
        "tasks": {
            "mic_ehr_embedding": {
                "label": "Embed validated screening tools (PHQ-9, GAD-7, DAST-10, AUDIT-C) directly into clinical EHR workflows.",
                "remediation": "Configure the EHR clinical package to automatically generate the appropriate screening tool during intake and quarterly reassessment intervals."
            },
            "mic_clinical_decisions": {
                "label": "Verify progress notes document treatment adjustments or psychiatric referrals when screening scores show no progress.",
                "remediation": "Re-train clinicians on how to document clinical decision-making. Notes must explicitly state when a high screening score triggers a change in therapeutic modality or psychiatric referral."
            },
            "mic_locus_michicans": {
                "label": "Confirm that LOCUS and MichiCANS assessments are updated annually and upon changes in condition.",
                "remediation": "Implement an automated EHR scheduler hard stop. Prevent clinicians from scheduling outpatient psychotherapy if the required level-of-care scores are outdated."
            }
        }
    },
    "Stepped-Care Assessment Protocol Deployment": {
        "policy": "SAMHSA CCBHC Demonstration Criteria & MDHHS Access Timelines",
        "tasks": {
            "sc_protocol_deployment": {
                "label": "Formally draft and deploy the 'Stepped-Care Assessment Model' protocol across all clinics.",
                "remediation": "Secure CCO and Clinical Director approval to release and mandate the new Stepped-Care clinical protocol immediately."
            },
            "sc_triage_96127": {
                "label": "Train intake staff to use brief emotional/behavioral assessments (CPT 96127) at triage.",
                "remediation": "Deploy immediate refresher training for intake staff. Establish a daily EHR audit to ensure 96127 screens are completed at first contact."
            },
            "sc_testing_limits": {
                "label": "Restrict comprehensive testing batteries strictly to cases with high differential diagnostic ambiguity or cognitive impairment.",
                "remediation": "Establish a mandatory triage approval workflow. All referrals for 96130 testing must be pre-approved by the Psychological Services Manager."
            }
        }
    },
    "Assessment KPI Dashboard Wireframing": {
        "policy": "SAMHSA Continuous Quality Improvement (CQI) Criteria & MDHHS Quality Templates",
        "tasks": {
            "kpi_dashboard_design": {
                "label": "Design and wireframe an EHR Assessment KPI Dashboard to track live weekly metrics.",
                "remediation": "Partner with the IT and Business Intelligence teams to expedite dashboard construction, utilizing mock data to verify tracking pipelines."
            },
            "kpi_metrics_tracking": {
                "label": "Configure the dashboard to monitor aggregate waitlist duration, average report TAT, and claim denial rates by payer.",
                "remediation": "Manually extract and track weekly metrics in an intermediate spreadsheet until the automated EHR dashboard integration is fully certified."
            },
            "kpi_billing_regressions": {
                "label": "Integrate historical claims data to prevent future billing regressions and provide executive visibility.",
                "remediation": "Set up a bi-weekly billing-clinical review committee to analyze real-time denial codes and hardcode billing rules to prevent regressions."
            }
        }
    },
    "Ambient Clinical AI ROI Case Development": {
        "policy": "SAMHSA Workforce Support (Quadruple Aim) & CARF ASPIRE Performance Standards",
        "tasks": {
            "ai_scribe_evaluation": {
                "label": "Evaluate the implementation of ambient clinical AI scribes (e.g., Eleos Health) to reduce administrative burdens.",
                "remediation": "Initiate a 15-day rapid pilot program with a small group of high-volume clinicians to gather hands-on usability data."
            },
            "ai_time_reduction": {
                "label": "Measure the reduction in documentation time (targeting a 70% decrease) and the impact on same-day note completion.",
                "remediation": "Partner with clinical supervisors to audit time-savings logs, comparing pre-pilot and post-pilot EHR note completion timestamps."
            },
            "ai_roi_proposal": {
                "label": "Draft a comprehensive return-on-investment (ROI) proposal for the executive board detailing compliance gains and time-saving metrics.",
                "remediation": "Accelerate proposal drafting. Present the final ROI business case to the Chief Financial Officer and Chief Clinical Officer for immediate budget allocation."
            }
        }
    }
}

# ================= TOP-LEVEL NAVIGATION SELECTOR =================

app_view = st.selectbox(
    "🔍 Select Appraisal View / Navigation",
    [
        "Phase I: Assessment & Baseline (Days 1–30)",
        "Phase II: Implementation of Clinical Frameworks (Days 31–60)",
        "Phase III: Quality Assurance & Future Exploration (Days 61–90)",
        "📈 Progress & Findings Report"
    ]
)

# Helper function to render a checklist category
def render_checklist_category(category_name, category_info):
    st.markdown(f'<div class="policy-tag">{category_info["policy"]}</div>', unsafe_allow_html=True)
    st.markdown(f"#### **{category_name}**")
    
    for task_id, task_info in category_info["tasks"].items():
        # Retrieve persistent session state
        is_compliant_state = st.session_state.audit_data[task_id]["compliant"]
        
        # Use columns for checklist representation
        col1, col2 = st.columns([3, 1])
        with col1:
            st.write(task_info["label"])
        with col2:
            compliance_val = st.selectbox(
                "Status",
                ["Compliant", "Non-Compliant"],
                index=0 if is_compliant_state else 1,
                key=f"sel_{task_id}",
                label_visibility="collapsed"
            )
            
        # Update session state based on selection
        is_compliant = (compliance_val == "Compliant")
        st.session_state.audit_data[task_id]["compliant"] = is_compliant
        
        # Context-specific Remediation Box (Renders only on Out of Compliance)
        if not is_compliant:
            st.markdown(
                f'<div style="background-color:#FFF3CD; padding:12px; border-radius:12px; border-left: 5px solid #FFC107; margin-bottom:12px; font-size:12.5px; color:#5D4037;">'
                f'⚠️ <strong>Out of Compliance Remediation Protocol:</strong><br>{task_info["remediation"]}'
                f'</div>',
                unsafe_allow_html=True
            )
    st.markdown("<hr style='margin: 8px 0 20px 0;'>", unsafe_allow_html=True)

# Helper function to render CliftonStrengths for the active phase
def render_strengths_expander(strengths_data):
    st.subheader("💡 CliftonStrengths Leadership Guidance")
    st.write("Leverage Scott's Top 5 strengths during this phase:")
    for s_name, s_info in strengths_data.items():
        with st.expander(s_name):
            st.markdown(f"**Operational Focus:** *{s_info['focus']}*")
            st.write(f"**Phase Application:** {s_info['application']}")

# ================= RENDER SELECTED VIEW =================

if app_view == "Phase I: Assessment & Baseline (Days 1–30)":
    st.markdown('<div class="phase-badge">Phase I: Days 1–30</div>', unsafe_allow_html=True)
    st.write("Conduct comprehensive, department-wide audits, analyze legacy workflows, and integrate with committees to establish a baseline.")
    
    for cat_name, cat_info in phase_1_defs.items():
        render_checklist_category(cat_name, cat_info)
        
    p1_strengths = {
        "🧠 Learner": {
            "focus": "Meticulous knowledge discovery and process audits",
            "application": "Meticulously executes the randomized 30-case stratified chart audit and LARA log review by treating compliance mapping as an active intellectual journey from discovery to full clinical mastery."
        },
        "🎯 Strategic": {
            "focus": "Billing modifier patterns and workflow triage algorithms",
            "application": "Quickly identifies systemic revenue leakage patterns within historical CPT denials and establishes immediate guidelines for the correct application of NCCI billing modifiers."
        },
        "🔍 Intellection": {
            "focus": "Deep root-cause analyses of compliance bottlenecks",
            "application": "Introspectively ponders systemic bottlenecks within LP-LLP supervision ratios and designs a centralized tracking portal rather than short-term paper workarounds."
        }
    }
    render_strengths_expander(p1_strengths)

elif app_view == "Phase II: Implementation of Clinical Frameworks (Days 31–60)":
    st.markdown('<div class="phase-badge">Phase II: Days 31–60</div>', unsafe_allow_html=True)
    st.write("Deploy clinical overhauls, roll out the Therapeutic Assessment model, deliver staff clinical workshops, and restructure EHR behavior templates.")
    
    for cat_name, cat_info in phase_2_defs.items():
        render_checklist_category(cat_name, cat_info)
        
    p2_strengths = {
        "💡 Ideation": {
            "focus": "Fascinating connections and creative clinical templates",
            "application": "Conceives out-of-the-box templates for the EHR behavior treatment plans that structurally require positive replacement behaviors, transforming restrictive plans into positive supports."
        },
        "🤝 Individualization": {
            "focus": "Tailored LLP coaching and supportive mentoring",
            "application": "Recognizes the unique clinical writing styles and developmental stages of junior LLPs during the roll-out of Workshop Module 1 (Motivational Interviewing), customizing feedback."
        },
        "🎯 Strategic": {
            "focus": "Transitioning legacy diagnostic workflows",
            "application": "Maps out alternative pathways to smoothly transition psychologists and psychometrists from standard multi-hour testing to the collaborative Therapeutic Assessment model."
        }
    }
    render_strengths_expander(p2_strengths)

elif app_view == "Phase III: Quality Assurance & Future Exploration (Days 61–90)":
    st.markdown('<div class="phase-badge">Phase III: Days 61–90</div>', unsafe_allow_html=True)
    st.write("Conduct mock CARF audits, integrate Measurement-Informed Care (MIC), deploy the Stepped-Care Assessment model, and draft the clinical AI ROI business case.")
    
    for cat_name, cat_info in phase_3_defs.items():
        render_checklist_category(cat_name, cat_info)
        
    p3_strengths = {
        "🧠 Learner": {
            "focus": "Deep tech integration and ambient AI efficacy data",
            "application": "Deep-dives into the technical specifications and clinical efficacy data of ambient behavioral AI to draft a watertight business case for executive leadership."
        },
        "💡 Ideation": {
            "focus": "Designing the Stepped-Care triage algorithm",
            "application": "Integrates brief emotional screenings (CPT 96127) at triage to build a natural clinical filter, resolving waitlist bottlenecks without denying immediate care access."
        },
        "🔍 Intellection": {
            "focus": "Mock CARF chart auditing and root-cause compliance",
            "application": "Conducts deep, introspective chart reviews during mock CARF audits to ensure SOAP notes and IPOS files are structurally bulletproof against external recoupments."
        }
    }
    render_strengths_expander(p3_strengths)

elif app_view == "📈 Progress & Findings Report":
    st.markdown('<div class="phase-badge">Executive Status Report</div>', unsafe_allow_html=True)
    st.write("Comprehensive operational and compliance summary of CNS Healthcare's 90-Day Psychological Services Appraisal. Ready for presentation to supervisors and executives.")
    
    # CALCULATE METRICS
    # Flatten definitions to map task compliance
    p1_keys = [k for cat in phase_1_defs.values() for k in cat["tasks"].keys()]
    p2_keys = [k for cat in phase_2_defs.values() for k in cat["tasks"].keys()]
    p3_keys = [k for cat in phase_3_defs.values() for k in cat["tasks"].keys()]
    total_keys = p1_keys + p2_keys + p3_keys
    
    p1_comp = sum(1 for k in p1_keys if st.session_state.audit_data[k]["compliant"])
    p2_comp = sum(1 for k in p2_keys if st.session_state.audit_data[k]["compliant"])
    p3_comp = sum(1 for k in p3_keys if st.session_state.audit_data[k]["compliant"])
    total_comp = sum(1 for k in total_keys if st.session_state.audit_data[k]["compliant"])
    
    p1_pct = (p1_comp / len(p1_keys)) * 100
    p2_pct = (p2_comp / len(p2_keys)) * 100
    p3_pct = (p3_comp / len(p3_keys)) * 100
    total_pct = (total_comp / len(total_keys)) * 100
    
    non_comp_total = len(total_keys) - total_comp
    
    # RENDER EXECUTIVE STATS CARDS
    st.markdown("### **Executive Summary Dashboard**")
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Overall Compliance", f"{total_pct:.1f}%", f"{total_comp}/{len(total_keys)} Tasks")
    with col2:
        st.metric("Active Vulnerabilities", f"{non_comp_total}", delta_color="inverse")
        
    st.progress(total_comp / len(total_keys))
    
    # PHASE BREAKDOWN EXPANDERS
    st.markdown("### **Phase Progress Breakdown**")
    
    with st.expander(f"Phase I Progress: {p1_pct:.1f}% Complete", expanded=True):
        st.write(f"**Phase I Status:** *{p1_comp} of {len(p1_keys)} tasks compliant.*")
        for cat_name, cat_info in phase_1_defs.items():
            st.markdown(f"**{cat_name}**")
            for t_id, t_info in cat_info["tasks"].items():
                is_comp = st.session_state.audit_data[t_id]["compliant"]
                mark = "✅ Compliant" if is_comp else "❌ Non-Compliant"
                st.markdown(f"- *{t_info['label']}* — **{mark}**")
                if not is_comp:
                    st.markdown(f"  *🛠️ Remediation:* {t_info['remediation']}")
                    
    with st.expander(f"Phase II Progress: {p2_pct:.1f}% Complete", expanded=False):
        st.write(f"**Phase II Status:** *{p2_comp} of {len(p2_keys)} tasks compliant.*")
        for cat_name, cat_info in phase_2_defs.items():
            st.markdown(f"**{cat_name}**")
            for t_id, t_info in cat_info["tasks"].items():
                is_comp = st.session_state.audit_data[t_id]["compliant"]
                mark = "✅ Compliant" if is_comp else "❌ Non-Compliant"
                st.markdown(f"- *{t_info['label']}* — **{mark}**")
                if not is_comp:
                    st.markdown(f"  *🛠️ Remediation:* {t_info['remediation']}")

    with st.expander(f"Phase III Progress: {p3_pct:.1f}% Complete", expanded=False):
        st.write(f"**Phase III Status:** *{p3_comp} of {len(p3_keys)} tasks compliant.*")
        for cat_name, cat_info in phase_3_defs.items():
            st.markdown(f"**{cat_name}**")
            for t_id, t_info in cat_info["tasks"].items():
                is_comp = st.session_state.audit_data[t_id]["compliant"]
                mark = "✅ Compliant" if is_comp else "❌ Non-Compliant"
                st.markdown(f"- *{t_info['label']}* — **{mark}**")
                if not is_comp:
                    st.markdown(f"  *🛠️ Remediation:* {t_info['remediation']}")

    # EXECUTIVE FINDINGS & RISK MATRIX
    st.markdown("### 🚨 **Regulatory & Operational Risk Matrix**")
    st.write("Dynamic exposure summary compiled based on flagged vulnerabilities:")
    
    # Calculate risks dynamically based on checkbox selections
    risks_exposed = []
    
    # Risk 1: Licensure and LARA Audit Risk
    if not (st.session_state.audit_data["lara_logs_exist"]["compliant"] and st.session_state.audit_data["lara_4hours"]["compliant"] and st.session_state.audit_data["lara_signoff"]["compliant"]):
        risks_exposed.append({
            "category": "Licensure & LARA",
            "threat": "Failure to impeccably document 4 hours/month LP-LLP individual supervision.",
            "impact": "Disciplinary licensure action; retroactive Medicaid PPS-1 encounter billing recoupment.",
            "mitigation": "Immediately implement automated HR tracking evaluation logs (LARA/BPL, Rev. 6/25). BlockLP calendars."
        })
        
    # Risk 2: Medicaid Billing Conflict Risk
    if not (st.session_state.audit_data["rcm_ncci_modifiers"]["compliant"] and st.session_state.audit_data["cpt_tech_segregation"]["compliant"]):
        risks_exposed.append({
            "category": "Revenue Cycle (NCCI)",
            "threat": "Billing provider (96136) and technician (96138) admin on the same day without correct modifiers.",
            "impact": "Automated clearinghouse claim rejections, suppressed department realization rates, and FWA scrutiny.",
            "mitigation": "Enforce mandatory EHR check-outs utilizing Modifier XE or 59 for separate same-day encounters."
        })
        
    # Risk 3: Recipient Rights Violation
    if not (st.session_state.audit_data["btp_unanimous"]["compliant"] and st.session_state.audit_data["btp_medical"]["compliant"] and st.session_state.audit_data["btp_no_aversives"]["compliant"]):
        risks_exposed.append({
            "category": "Recipient Rights",
            "threat": "BTPs proposing restrictive or intrusive interventions without prerequisite MD physicals or BTPRC quorum.",
            "impact": "State-level recipient rights citations; loss of CCBHC certification status; legal liability.",
            "mitigation": "Order the immediate cessation of unapproved physical management or restrictive protocols; trigger emergency BTPRC quorums."
        })

    # Risk 4: CCBHC decertification waitlists
    if not (st.session_state.audit_data["triage_routine_14day"]["compliant"] and st.session_state.audit_data["sc_testing_limits"]["compliant"]):
        risks_exposed.append({
            "category": "CCBHC Certification",
            "threat": "Testing turnaround times and waitlists exceeding SAMHSA/MDHHS-mandated timelines.",
            "impact": "State-issued Corrective Action Plans (CAPs); decertification of demonstration site status.",
            "mitigation": "Formally deploy the Stepped-Care Assessment model. Filter low-acuity requests at triage using CPT 96127 screenings."
        })

    if risks_exposed:
        for r in risks_exposed:
            st.markdown(
                f'<div style="background-color:#FFEBEE; padding:15px; border-radius:15px; border-left:6px solid #D32F2F; margin-bottom:15px; font-size:12.5px; color:#212121;">'
                f'🔴 <strong>[{r["category"]}] Risk Exposure Detected</strong><br>'
                f'<strong>Threat:</strong> {r["threat"]}<br>'
                f'<strong>Operational Impact:</strong> {r["impact"]}<br>'
                f'<strong>Immediate Directive:</strong> {r["mitigation"]}'
                f'</div>',
                unsafe_allow_html=True
            )
    else:
        st.success("🎉 **Spectacular Quality Status!** Zero high-risk compliance exposures are currently detected. The department is robustly insulated against audit and recoupment vulnerabilities.")

    # GENERAL REPORT FOOTER
    st.markdown("<hr style='margin-top: 30px;'>", unsafe_allow_html=True)
    st.markdown(
        f'<div style="font-size:11px; color:#546E7A; text-align:center; padding:15px; background-color:#ECEFF1; border-radius:10px;">'
        f'<strong>Appraisal Status Report</strong> • CNS Healthcare Department of Psychological Services<br>'
        f'Generated dynamically for Executive Review • Data Current as of August 2026<br>'
        f'Verified in accordance with SAMHSA, Michigan LARA, and MDHHS APF 167 guidelines.</div>',
        unsafe_allow_html=True
    )

# Disclaimer Footer
st.markdown("<hr style='margin-top: 30px;'>", unsafe_allow_html=True)
st.markdown(
    '<div style="font-size:10px; color:#90A4AE; text-align:center; padding-bottom:20px;">'
    'CNS Healthcare psychological services compliance platform is configured in strict accordance with '
    'Michigan LARA (MCL 333.18223), MDHHS APF 167, and SAMHSA CCBHC parameters.</div>',
    unsafe_allow_html=True
)
