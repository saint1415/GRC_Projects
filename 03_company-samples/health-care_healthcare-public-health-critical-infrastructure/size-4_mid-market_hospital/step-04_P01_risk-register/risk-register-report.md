# Risk Register Report: Cris Santos Company | Healthcare and Public Health | Mid-Market

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (PE-backed 112-bed community acute-care hospital with an off-campus outpatient center) |
| Size tier | Mid-Market (600 employees) |
| Vertical | Healthcare and Public Health |
| Method | NIST SP 800-30 Rev. 1 (Tables G-2 to G-5, H-3, I-2, I-3 values); enterprise roll-up per NIST IR 8286 Rev. 1 |
| Also satisfies | HIPAA risk analysis and risk management, 45 CFR 164.308(a)(1)(ii)(A)-(B); the Promoting Interoperability security risk analysis measure (42 CFR 495.24); input to the all-hazards risk assessment of the emergency plan, 42 CFR 482.15(a)(1) |
| Prepared | 2026-07-17 by the Information Security Manager and the vCISO; R-054 added 2026-08-07 from P07 testing; AI risks (R-024 to R-030) re-rated 2026-08-28 after the P10 review |
| Approved | 2026-09-17: Chief Operating Officer (Moderate and below), Chief Executive Officer (High and the temporary exception for R-001); presented to the board audit committee the same day |

## 1. Scope and risk framing
**Scope.** All business units (ED, inpatient and critical care, women's services, surgery, pharmacy, laboratory, imaging and cardiology, patient access, revenue cycle, HIM, facilities, the outpatient center, the affiliated practice program, and enterprise functions); the Hospital EHR and Clinical Systems (HECS: SYS-01 to SYS-08 and SYS-10); building OT (SYS-09); clinical communications (SYS-11); about 210 vendors with PHI access (SYS-12); and the AI tools (SYS-13). Processes and impact values come from the BIA (P05); vulnerabilities come from the gap analysis (P03), the control assessment (P07), and the AI review (P10).

**Who can accept risk (tolerance).**
| Risk level | Who may accept | Conditions |
|---|---|---|
| Very Low and Low | The risk owner (director level or above) | Recorded in the register; reviewed annually |
| Moderate | Chief Operating Officer | Treatment plan or documented reason; reviewed every 6 months |
| High | Chief Executive Officer | Temporary only (up to 12 months) with a dated treatment plan; reported to the audit committee each quarter |
| Very High | Not acceptable | The CEO may approve a temporary exception of up to 90 days only after notifying the audit committee chair, while treatment is under way. Used once: R-001, 2026-09-17, renewable once on evidence of progress |

### Risk appetite statements
Approved by the Chief Executive Officer and noted by the audit committee on 2026-09-17.

| Area | Appetite | Statement and measure |
|---|---|---|
| Patient safety | **Very low** | No cyber or technology risk that could plausibly cause patient harm is accepted above Low. Any such risk rated Moderate or higher must have a funded treatment plan within 90 days. Measure: number of safety-linked risks above Low (14 today: R-001, R-003, R-005, R-006, R-007, R-008, R-015, R-016, R-017, R-024, R-026, R-044, R-047, R-054; target 0 by 2027-12-31) |
| Continuity of emergency care | **Very low** | The ED must not go on diversion because of an IT event that a tested procedure could have carried. Measure: every High-criticality process in the BIA has a passed recovery or downtime test in the last 12 months |
| Confidentiality of PHI | **Low** | The hospital will not accept a risk of a breach affecting 500 or more patients above Moderate. Measure: R-002 and R-014 at Moderate or lower by 2027-06-30 |
| Regulatory compliance | **Low** | No HIPAA Security Rule Required implementation specification may stay Partially met or Not met beyond 2027-06-30. The emergency plan must address cyber hazards before the next survey cycle |
| Third parties | **Moderate**, with conditions | Vendors are used widely, but no vendor receives PHI without a BAA, no vendor reaches the network without MFA, and every Tier 1 vendor is reassessed each year (P09) |
| Innovation and AI | **Moderate** | The hospital wants the benefits of AI in sepsis detection, imaging triage, documentation, and coding, but only through the AI governance process in P10. No AI tool touches PHI without review and a BAA |
| Financial loss from cyber events | **Moderate** | Single-event losses up to the $500,000 insurance retention are tolerable. Scenarios above $2 million need a treatment that reduces likelihood, not only insurance |

## 2. Method
1. **Identify.** Threat sources and events came from SP 800-30 Appendices D and E; the five threats in HHS 405(d) HICP (2023 edition): social engineering, ransomware attacks, loss or theft of equipment or data, insider accidental or malicious data loss, and attacks against network connected medical devices that may affect patient safety. HICP treats a hospital of 51-299 beds as a medium-sized organization, so the medium-sized sub-practices in Technical Volume 2 were used as a reference; the BIA; interviews with every process owner; the gap analysis (P03); the control assessment (P07); and the AI review (P10).
2. **Rate likelihood.** The likelihood of initiation (adversarial) or occurrence (non-adversarial) and the likelihood of adverse impact were each rated, then combined with **Table G-5**.
3. **Rate impact.** Impact used **Table H-3**, anchored to the BIA impact categories (cost, operations, regulatory, patient safety, reputation).
4. **Determine risk.** Risk level came from **Table I-2**. The `overall_likelihood` and `risk_level` columns were computed by script from the two tables, not assigned by hand.
5. **Semi-quantitative view.** `semi_quant_score` gives each risk level its SP 800-30 Appendix I semi-quantitative value (Very High 10, High 8, Moderate 5, Low 2, Very Low 0). `exposure_estimate_usd` gives an order-of-magnitude single-event loss range from the BIA values, used for the enterprise roll-up (NIST IR 8286 Rev. 1). The ranges are estimates for prioritizing, not actuarial figures.

## 3. Results
| Risk level | Count |
|---|---|
| Very High | 1 |
| High | 13 |
| Moderate | 27 |
| Low | 14 |
| Very Low | 0 |
| **Total** | **55** |

Treatments: 50 Mitigate, 5 Accept (R-032, R-045, R-046, R-053, R-055, all Low). Status: 32 Open, 18 In progress, 5 Accepted.

Cyber insurance ($15 million limit, $500,000 retention) transfers part of the financial exposure for R-001, R-002, and R-014. It is not recorded as the treatment for any risk, because it does not lower the likelihood of harm to patients or operations.

### Top risks (Very High and High)
| Risk ID | Risk | Level | Treatment | Owner | Due |
|---|---|---|---|---|---|
| R-001 | Ransomware forces EHR downtime, loss of clinical servers, and diversion | Very High | Vendor access platform; privileged access management; backup appliance off the domain; IT DR plan and restore tests; segmentation; 72-hour tabletop | IT Director (Security Officer) | 2027-06-30 |
| R-002 | PHI exfiltration for extortion | High | Egress alerting; warehouse and file logs to the SIEM; extract approval | Information Security Manager | 2027-01-31 |
| R-003 | On-premises clinical servers cannot be restored within RTO | High | IT DR plan; vendor backups into the appliance; quarterly restore tests | IT Director (Security Officer) | 2027-03-31 |
| R-005 | EHR vendor outage beyond the clinical MTD | High | Recovery terms at renewal; 72-hour downtime procedures; drills | IT Director (Security Officer) | 2027-06-30 |
| R-006 | Paper downtime procedures fail beyond 4 hours | High | Rewrite for 72 hours; quarterly unit drills; downtime kits | Director of Emergency Management | 2027-03-31 |
| R-007 | Attack spreads to devices on the shared clinical VLAN | High | Passive discovery; device VLANs with deny-by-default rules | Director of Biomedical Engineering | 2027-06-30 |
| R-009 | Domain administrator or vendor service account takeover | High | Privileged access management; phishing-resistant admin MFA; vaulted service accounts | Information Security Manager | 2027-03-31 |
| R-010 | Vendor VPN accounts without MFA used as an entry point | High | All vendors on the access platform with MFA | Information Security Manager | 2026-12-31 |
| R-014 | Insider snooping on a high-profile patient goes undetected | High | EHR access analytics; automatic VIP flag; insider-access runbook (P08) | Compliance and Privacy Officer | 2027-03-31 |
| R-016 | Building OT compromise disrupts HVAC, isolation rooms, or blood storage | High | OT segment; named vendor portal accounts with MFA; configuration exports | Information Security Manager | 2027-06-30 |
| R-017 | Network outage takes down phones, smartphones, and alarms | High | Analog or cellular lines on every unit; radios for codes; drills | Director of Emergency Management | 2027-03-31 |
| R-024 | Sepsis model misses patients or causes alert fatigue | High | Local validation; universal screening; threshold decision (P10) | Chief Medical Officer | 2026-12-31 |
| R-029 | PHI pasted into public generative AI | High | Block public tools; enterprise assistant with a BAA; training | Information Security Manager | 2026-12-31 |
| R-054 | Default or shared vendor credentials on clinical servers and devices (found in P07) | High | Change and vault all vendor passwords; onboarding check | Director of Biomedical Engineering | 2026-10-31 |

**Themes.**
- **Recovery, not detection, is the weak point (R-001, R-003, R-004, R-005, R-006).** The hospital can detect attacks (EDR, MSSP, SIEM), and its cloud backups are isolated, but it has never restored a clinical server and has never run downtime past 4 hours. For a hospital, that gap ends in diversion.
- **The campus network is too flat (R-007, R-008, R-016, R-017, R-037, R-054).** Devices, OT, phones, and workstations share segments, and the systems that matter most for patient safety send no logs.
- **Privileged and vendor access (R-009, R-010, R-023, R-050).** 31 standing domain administrators and 14 vendor VPN accounts without MFA are the most likely ways in.
- **Insiders and non-employees (R-013, R-014, R-036, R-038).** A hospital's most common privacy breach is a workforce member looking at a record without a reason; monitoring today would catch only VIP cases.
- **AI adopted without governance (R-024 to R-030).** The sepsis model went live in an EHR upgrade. P10 addresses the portfolio.
- **Emergency preparedness (R-018, R-019).** A CMS condition of participation is at stake, not only IT risk.

## 4. Treatment summary
**Funded in the FY2027 security plan (approved by the CEO 2026-09-17, $1.45 million one-time and $620,000 a year):**
- Vendor access platform for all 46 vendors, privileged access management for every admin plane, and phishing-resistant MFA for administrators ($240,000 one-time, $110,000 a year)
- Passive medical device discovery and monitoring, and device VLANs for monitors, analyzers, cabinets, fetal monitoring, and the cath lab ($420,000 one-time, $90,000 a year)
- SIEM onboarding of the on-premises clinical servers, the interface engine, and device and OT monitoring feeds ($130,000 a year through the MSSP)
- EHR inappropriate-access analytics ($80,000 a year)
- IT disaster recovery plan, restore testing program, and backup appliance redesign ($160,000 one-time)
- 72-hour downtime program: procedures, kits, analog or cellular lines on every unit, and radios ($150,000 one-time)
- OT network segment and named vendor portal accounts ($180,000 one-time)
- One GRC analyst position and vendor risk tooling ($150,000 a year)
- Secondary clearinghouse connection ($40,000 one-time)
- SOC 2 readiness and Type 2 examination for the affiliated practice program ($260,000 across 2027)
- Enterprise generative AI assistant with a BAA ($60,000 a year)

Replacement of unsupported medical devices (R-008) is in the 2027-2029 capital plan. Smaller items (network closet badge readers, DMARC enforcement, exercise facilitation) are funded from the operating budget. Each funded item maps to a P07 POA&M entry.

**Accepted (5, all Low):** R-032 (encrypted laptops), R-045 (redundant cooling), R-046 (two carriers at the outpatient center), R-053 (NPRM tracked; roadmap aligned), R-055 (encrypted, remotely wiped smartphones).

**Contract actions:** BAAs for 42 vendors and an amended AI scribe BAA (R-021, R-028), due 2026-12-31. EHR vendor recovery terms (R-005) and a PACS vendor SOC 2 requirement (R-050) at renewal.

## 5. Enterprise and system-level registers
This file is the **enterprise register**. Following NIST IR 8286 Rev. 1, it rolls up to the hospital's enterprise risk register as one line, "Cybersecurity and technology resilience", owned by the COO and reported to the audit committee each quarter with the counts above and the top risks.

System-level registers are filtered views of this file, kept by each system owner, rather than separate spreadsheets. That keeps one set of ratings. The `register_views` column says which views each risk belongs to.

| System-level register | Owner | Risks in scope |
|---|---|---|
| HECS (SSP in P02) | IT Director (Security Officer) | 46 risks tagged "HECS" (1 Very High, 11 High, 22 Moderate, 12 Low) |
| Emergency preparedness (feeds the 42 CFR 482.15(a)(1) all-hazards risk assessment) | Director of Emergency Management | 9 risks: R-001, R-003, R-005, R-006, R-016, R-017, R-018, R-019, R-044 |
| AI portfolio (P10) | Chief Medical Officer | 7 risks: R-024 to R-030 |
| Affiliated practice service (P09 SOC 2 scope) | Director of Physician Services | 2 service-specific risks: R-038, R-039 (plus the HECS risks that the service inherits) |

When a system-level review changes a rating, the owner updates this file, and the change flows to the enterprise roll-up.

## 6. Approval
- Chief Operating Officer: approved Moderate and Low treatments and the acceptance of the 5 Low risks, 2026-09-17.
- Chief Executive Officer: approved the High treatment plans, the 90-day exception for R-001, the risk appetite statements, and the FY2027 security budget, 2026-09-17.
- Board audit committee: received the results on 2026-09-17. Next report: 2026-12 quarterly meeting, including R-001 progress for the exception review.
- Next full risk analysis: June 2027, or sooner after a major change (for example a new EHR, an acquisition, or a new care site) or a significant incident.
