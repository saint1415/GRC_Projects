# SOC 2 Readiness Summary: Cris Santos Company | Transportation and Warehousing | Small

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (marine cargo terminal operator, NAICS 488320) |
| Tier / Vertical | Small / Transportation and Warehousing |
| Criteria | AICPA 2017 Trust Services Criteria (With Revised Points of Focus, 2022) |
| Categories in scope | Security (CC1-CC9) and Availability (A1) |
| Target report | None in 2026 or 2027. This is a readiness self-assessment used to answer ocean carrier security questionnaires. A SOC 2 Type 1 would be considered only if a carrier makes it a contract condition |
| Part A | Company readiness self-assessment (`soc2-readiness.csv`) |
| Part B | Review of the TOS vendor's SOC 2 Type 2 report for its hosted portal and remote support (`vendor-soc2-review.csv`) |
| Prepared | 2026-08-28 by the IT Manager (proposed CySO); updated for the approved policies and runbook and approved by the General Manager, 2026-09-04 |

## 1. Why SOC 2 for this organization
A marine terminal operator is **not** a typical SOC 2 subject. It does serve other businesses (ocean carriers), but carriers rarely ask a terminal for a CPA-issued SOC 2 report. The terminal's security is regulated through the Coast Guard: the Facility Security Plan and, from 2027, the Cybersecurity Plan (33 CFR 101.630). SOC 2 appears here for two practical reasons.

**A. Carrier security questionnaires.** Two of the six carrier services sent security questionnaires in 2026, and a third asked about security at contract renewal. They ask how the terminal protects their bay plans, container status and EDI links, and how quickly the gate and vessel operations recover after an outage. The questionnaires follow the Security and Availability themes of the Trust Services Criteria. The company answers with this self-assessment and its remediation dates.

**Why not share the Coast Guard documents instead?** The Cybersecurity Plan is sensitive security information (SSI) under 49 CFR part 1520 (101.630(b)). It cannot be handed to carriers that are not covered persons with a need to know. The TSC format lets the company describe its controls without releasing SSI.

**Why not a formal SOC 2 audit now:**
- A Type 2 audit needs controls that have operated over a period, typically 6 to 12 months. Most of the company's controls were defined in 2026-09, and the Subpart F measures are due 2027-07-16.
- No carrier has made a SOC 2 report a contract condition.
- The audit fee would compete with the $145,000 remediation budget (P01).

**Other options considered:**
- **Questionnaire only:** the carriers accept a TSC-based self-assessment in place of their own forms.
- **CTPAT:** voluntary. Its minimum security criteria include cybersecurity. Being considered for 2027 (N48-49-R05).
- **ISO/IEC 27001 certification:** out of proportion for a 60-person terminal today.

**B. Third-party risk management.** The TOS vendor hosts the truck appointment and customer portal and has remote support access to the TOS. Its SOC 2 Type 2 report is the evidence for the controls marked Provider or Shared in P04. The company reviews it every year (SA-9; 33 CFR 101.650(f)).

## 2. System description (scope)
- **Services:** vessel loading and discharge, yard storage, the truck gate, and EDI with carriers, trucking companies, the port community system and the customs data exchange.
- **Infrastructure and software:** the Terminal Operations and Gate Platform (SSP, P02): the TOS in a vendor-agnostic cloud tenant, gate automation, the identity provider, and the terminal network. The crane and yard equipment controllers (OT) are an interconnected system. Carriers rely on OT for availability, so it is included where it affects availability.
- **People:** 60 employees, longshore labor who use VMTs and equipment, the MSP, and the TOS vendor.
- **Data:** bay plans, load and discharge lists, container status, customs release and hold status, and truck driver details.
- **Procedures:** POL-01 to POL-05, the P08 ransomware runbook, and the FSP procedures (SSI, not shared).

## 3. Readiness results (Part A)
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33 criteria) | 4 | 21 | 8 | 0 |
| Availability (A1, 3) | 0 | 1 | 2 | 0 |
| Confidentiality (C1, 2) | | | | 2 |
| Processing Integrity (PI1, 5) | | | | 5 |
| Privacy (P1-P8, 18) | | | | 18 |

In scope: 36 criteria (4 Ready, 22 Partially ready, 10 Not ready). Out of scope: 25 criteria.

**Ready:**
- CC3.1 and CC3.2: objectives, risk tolerance and the 2026 risk assessment
- CC3.3: fraud risk (container release manipulation and payment redirection are in the register)
- CC4.2: deficiencies tracked in the POA&M with owners and dates

**Not ready:**
- CC1.4: training (the Subpart F deadline was missed)
- CC2.3: no security contact or customer incident notice procedure
- CC6.1 and CC6.3: password-only VPN, flat network, shared gate logins, late account removal
- CC7.1 and CC7.2: no vulnerability scanning or security monitoring
- CC7.5, A1.2 and A1.3: backups exposed and recovery never tested (the same gap as P01 R-004)
- CC9.2: vendor security terms

**How to answer carriers today.** Answer truthfully that the terminal is partially ready. Give the dated milestones below. Point out that the controls carriers care most about (MFA, isolated backups, monitoring) close between 2026-11-30 and 2027-03-31.

## 4. Findings from the TOS vendor report (Part B)
- **Opinion:** Type 2, unqualified, for the 12 months ending 2026-03-31. One exception: 3 of 25 sampled remote support sessions had no customer ticket reference. The vendor remediated it in 2026-02.
- **Scope limit.** The report covers the vendor's hosted portal and remote support operations only. **It does not cover the TOS software the company runs in its own cloud tenant.** Those controls stay in the company's SSP.
- **Availability:** the portal commitments (99.5% monthly uptime, RTO 8 hours, RPO 1 hour) meet the BIA for BP-08 (RTO 8 h, RPO 24 h).
- **Controls the company must run.** The report lists complementary user entity controls: approve and review vendor support sessions; manage portal administrators; enforce MFA for them; tell the vendor about terminated users. Two are open gaps at the company:
  - the standing vendor support account (POAM-013)
  - no review of vendor sessions (POAM-024)

  **The vendor's controls only protect the company once those gaps are closed.** The session exception above shows why.
- **Follow-ups:**
  - Obtain a bridge letter to 2026-09-30.
  - Negotiate incident and vulnerability notice "without delay" at renewal, to meet 33 CFR 101.650(f)(2).
  - Confirm that the vendor reviews its hosting provider's SOC 2 report.

## 5. Remediation plan and evidence calendar
| Quarter | Criteria addressed | Evidence to start collecting |
|---|---|---|
| 2026 Q4 | CC1.3, CC1.4, CC2.2, CC6.2, CC6.3, CC6.6, CC7.3, CC7.4 | CySO designation letter, training records, policy acknowledgments, MFA settings, termination tickets, access reviews, vendor session approvals, tabletop report |
| 2027 Q1 | CC6.1, CC6.8, CC7.1, CC7.2, CC7.5, CC9.2, A1.2, A1.3 | Firewall and OT zone rules, EDR alerts and tickets, scan reports, KEV log, restore test records, amended vendor contracts |
| 2027 Q2 | CC1.2, CC3.4, CC4.1, CC5.3, CC8.1, A1.1 | Quarterly owner reports, change log, monthly POA&M reviews, procedures, capacity alerts. The Cybersecurity Plan is submitted to the Coast Guard by 2027-05-31 (deadline 2027-07-16) |

**Response to carriers:** send this summary, the readiness checklist and the list of POA&M milestones (P07). Do not send SSI: no network map, FSP content or vulnerability details. The company commits to an updated self-assessment in 2027-04, after the Cybersecurity Assessment.
