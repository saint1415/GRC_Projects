# Risk Register Report: Cris Santos Company | Healthcare and Public Health | Small

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (rural critical access hospital, 12 beds, 24-hour ED) |
| Size tier | Small (60 employees) |
| Vertical | Healthcare and Public Health (CISA critical infrastructure sector) |
| Method | NIST SP 800-30 Rev. 1 (Tables G-2 to G-5, H-3, I-2) |
| Also satisfies | HIPAA risk analysis, 45 CFR 164.308(a)(1)(ii)(A); the security risk analysis attested under the Medicare Promoting Interoperability Program (42 CFR 495.24); input to the facility-based all-hazards risk assessment for emergency preparedness (42 CFR 485.625(a)(1)) |
| Prepared | 2026-07-24 by the IT Manager (Security Officer), with the Facilities Manager (Emergency Preparedness Coordinator) and the Director of Nursing |
| Approved | 2026-08-31 by the CEO (Moderate and below) and the governing body (High and Very High) |

## 1. Scope and risk framing
**Scope.** The Hospital Clinical Information System (HCIS) defined in the SSP (P02), the building and clinical OT that shares its network (SYS-08), and every business process in the BIA (P05). That covers every system that creates, receives, maintains, or transmits ePHI, plus the vendors that handle ePHI for the hospital ([asset inventory](../step-00_P00_intake/asset-inventory.csv) and [vendor register](../step-00_P00_intake/vendor-register.csv)).

**Why this register is different from a clinic's.** The hospital runs a 24-hour emergency department and inpatient beds. An IT outage is a patient-safety event, not only a business interruption: it can force ambulance diversion in a county where the next hospital is about 45 miles away. Impact ratings therefore use the BIA safety category (P05 section 3) whenever a risk can stop ED, medication, laboratory, or imaging work.

**Risk tolerance and who can accept risk:**
- Low and Very Low: the IT Manager may accept.
- Moderate: the CEO may accept, with a treatment plan or a documented reason.
- High and Very High: only the governing body may accept, and only temporarily with a dated treatment plan. Patient-safety risks at High or above may not be accepted without a treatment plan.

The last risk analysis was a consultant's report in 2023 (EV-034). It did not cover medical devices, building OT, or the cloud tenant.

## 2. Method
1. **Identify.** Threat sources and events came from SP 800-30 Appendices D and E, the five threats in HHS 405(d) HICP (2023 edition: social engineering, ransomware, loss or theft of equipment or data, insider data loss, and attacks on connected medical devices), the BIA, the intake evidence, and interviews with the Director of Nursing, Laboratory and Imaging Managers, Facilities Manager, and Business Office Manager (EV-060). The gap analysis (P03) ran in the same fieldwork window, as is usual for a HIPAA risk analysis, and the two shared findings.
2. **Rate likelihood.** Likelihood of initiation (adversarial) or occurrence (non-adversarial) was rated, along with the likelihood that the event causes adverse impact. The two were combined with **Table G-5**. Each rating rests on evidence named in the `likelihood_basis` column: the security ticket history (EV-047), configuration exports, the walk-throughs, the emergency program records and interviews. A rating with no evidence behind it would be a guess, so none was made.
3. **Rate impact.** Impact was rated with **Table H-3**, using the BIA impact categories (cost, operations, regulatory, safety, reputation).
4. **Determine risk.** Risk level comes from **Table I-2**. The overall likelihood and risk level columns in `risk-register.csv` were computed from the tables by script, not assigned by hand.

## 3. Results

| Risk level | Count |
|---|---|
| Very High | 1 |
| High | 4 |
| Moderate | 21 |
| Low | 7 |
| **Total** | **33** |

Treatment: 30 risks are being mitigated and 3 are accepted (R-024, R-025, R-031).

### Top risks
| Risk ID | Risk | Level | Treatment | Owner | Due |
|---|---|---|---|---|---|
| R-001 | Ransomware through the teleradiology vendor's shared VPN account forces EHR downtime and ambulance diversion | Very High | Named vendor accounts with MFA; 24x7 managed detection and response; network segmentation; immutable backups | IT Manager | 2026-12-31 |
| R-003 | Backups destroyed along with production | High | Take the backup appliance off the directory; separate immutable backup account in a second region; quarterly restore tests | IT Manager | 2026-11-30 |
| R-007 | Tampered infusion pump drug library harms a patient | High | Patch and isolate the drug-library server; alert on library changes | Facilities Manager | 2026-12-31 |
| R-018 | MSP remote management tool compromise reaches every server and workstation | High | MFA and source restrictions on the MSP tool; named MSP admin accounts; annual MSP review | CFO | 2026-12-31 |
| R-002 | Phishing-delivered ransomware spreads across the flat network | High | Phishing exercises; training for contracted clinicians; 24x7 alert response | IT Manager | 2027-01-31 |
| R-004 | EHR outage with untested downtime procedures leads to medication or result errors | Moderate | New downtime procedures; monthly downtime PC tests; quarterly drills | Director of Nursing | 2026-12-31 |
| R-016 | Emergency preparedness plan omits cyberattack and EHR outage | Moderate | Add to the all-hazards risk assessment; diversion criteria; ransomware tabletop | Facilities Manager | 2026-12-31 |

The five High and Very High risks share one theme: **an attacker who gets in today can reach everything, and the hospital could not recover quickly.** Vendor and MSP access is weakly controlled (R-001, R-018), alerts go unwatched at night (R-002), backups are reachable (R-003), and clinical devices sit on the same network as everything else (R-007). The same fixes also reduce six Moderate risks (R-004 through faster recovery, R-005, R-006, R-022, R-030, and R-033) and one Low risk (R-008).

**Two passes.** Pass 1 was completed on 2026-07-24 from intake and fieldwork evidence. Pass 2 followed the control assessment (P07): R-026 was added on 2026-08-07 after testing found a manufacturer default password on the patient monitor central station (EV-IA-5). The `assessment_pass` column shows which pass produced each risk. R-020 and R-021 come from pass 1 and were re-rated on 2026-08-21 after the sepsis model review (P10).

## 4. Treatment summary
- **Funded (2026 Q4 and 2027 budget, $93,000 approved by the governing body):**
  - 24x7 managed detection and response through the MSP: $38,000 per year
  - Backup redesign (separate immutable account, second region): $9,000 per year
  - Network segmentation for medical devices, building OT, servers, and phones: $24,000 one time
  - Second, diverse internet carrier: $15,000 per year (install by 2027 Q1)
  - Phishing exercise and training platform covering contracted clinicians: $3,000 per year
  - Analog and cellular backup phones for the nursing station, laboratory, and imaging: $4,000 one time
- **Staff-time actions:** named vendor accounts with MFA (R-001), desktop encryption (R-013), agency account expiry (R-009), access report review (R-010), downtime procedures and drills (R-004), emergency plan update (R-016).
- **Accepted:**
  - R-024: Low, hardware security keys already in place
  - R-025: Moderate, covered by 60 days of cash on hand and Medicare periodic interim payments
  - R-031: Low, vendor-managed
- **Contract actions:** BAAs for the cloud fax service and the biomedical service contractor (R-019, R-027), due 2026-10-31; MSP and teleradiology access terms (R-001, R-018).

## 5. Approval
- CEO: approved Moderate and Low treatments and acceptances, 2026-08-31.
- Governing body: approved the High and Very High treatment plans and the $93,000 budget, 2026-08-31. R-001 stays open as a Very High risk until named vendor accounts with MFA and 24x7 monitoring are live; the governing body receives a monthly status report until then.
- Next full review: July 2027, or sooner after a major change or incident. The Facilities Manager carries the cyber-related risks into the 2026-27 emergency preparedness risk assessment (P03, 485.625(a)(1)).
