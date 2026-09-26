# SOC 2 Readiness Summary: Cris Santos Company | Health Care | Small

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (multi-specialty physician practice) |
| Tier / Vertical | Small / Health Care and Social Assistance |
| Criteria | AICPA 2017 Trust Services Criteria (With Revised Points of Focus, 2022) |
| Categories in scope | Security (CC1-CC9), Availability (A1), Confidentiality (C1) |
| Part A | Practice readiness self-assessment (`soc2-readiness.csv`) |
| Part B | EHR vendor SOC 2 Type 2 report review (`vendor-soc2-review.csv`) |
| Prepared | 2026-08-20 by the IT Manager |

## 1. Why SOC 2 for this organization
A physician practice is usually **not** a SOC 2 service organization: it delivers care to patients rather than services to other businesses. SOC 2 appears here for two legitimate reasons:

**A. Customer assurance request.** A regional health system invited the practice into its clinically integrated network. Members exchange PHI through shared systems, and the health system asked each member for evidence of security controls, using the Trust Services Criteria as the yardstick. The practice will answer with this readiness self-assessment and a remediation plan, **not** a CPA-issued SOC 2 report.

Why not a formal SOC 2 audit now:
- A Type 2 audit needs controls that have operated over a period, typically 6 to 12 months.
- The practice's controls were mostly defined in August 2026.
- An audit would cost more than the health system's request requires.

Other options considered:
- A security questionnaire: the health system accepted this TSC-based format instead.
- HITRUST certification: a private certification common in health care. Out of proportion for a 60-person practice today.

**B. Third-party risk management.** The practice relies on its EHR vendor for most inherited controls (P02, P04). The vendor's SOC 2 Type 2 report is the evidence for those controls. The practice reviews it every year (HIPAA 164.308(b), SA-9).

## 2. System description (scope)
- **Services:** clinical care and billing for the practice's patients, and data exchange with the clinically integrated network.
- **Infrastructure and software:** the Clinical and Revenue Cycle Platform (SSP, P02).
- **People:** 60 workforce members and the MSP.
- **Data:** ePHI, claims, and workforce data.
- **Procedures:** POL-01 to POL-05 and the P08 runbook.

## 3. Readiness results (Part A)
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33 criteria) | 5 | 21 | 7 | 0 |
| Availability (A1, 3) | 0 | 1 | 2 | 0 |
| Confidentiality (C1, 2) | 0 | 2 | 0 | 0 |
| Processing Integrity (PI1, 5) | | | | 5 |
| Privacy (P1-P8, 18) | | | | 18 |

**Ready:**
- CC1.3: roles are designated
- CC3.1 and CC3.2: objectives and risk analysis are done
- CC4.2: deficiencies are tracked
- CC6.6: boundary protection is in place

**Not ready:**
- CC3.3: fraud risk not assessed
- CC6.3: late terminations and excess access rights
- CC7.1 and CC7.2: no vulnerability or security monitoring
- CC7.5, A1.2, and A1.3: recovery (the same gap as risk R-005)
- CC8.1: no change management
- CC9.2: vendor management

## 4. Findings from the EHR vendor report (Part B)
- **Opinion:** Type 2, unqualified. One access-removal exception at the vendor, remediated.
- **Availability:** the vendor's stated RTO of 4 hours and RPO of 15 minutes **meet the practice's BIA** (RTO 4 h, RPO 1 h for BP-01 to BP-03).
- **Controls the practice must run.** The report lists controls the customer must operate for the vendor's controls to work (complementary user entity controls): user provisioning and removal, MFA enforcement, role assignment, and **audit report review**. Two of them are open gaps at the practice: removal timing (POAM-001) and audit review (POAM-008). **The vendor's controls only protect the practice once those gaps are closed.**
- **Follow-ups:**
  - Obtain a bridge letter through 2026-06-30.
  - Get assurance information for the carved-out e-prescribing network.
  - Negotiate 24-hour incident notice at BAA renewal.

## 5. Remediation plan and evidence calendar
| Quarter | Criteria addressed | Evidence to start collecting |
|---|---|---|
| 2026 Q4 | CC6.3, CC9.2, CC2.2, CC7.3-7.4 | Termination tickets, signed BAAs, policy acknowledgments, tabletop report |
| 2027 Q1 | CC6.8, CC7.1-7.2, CC7.5, A1.2-A1.3 | EDR alerts and tickets, scan reports, restore test records |
| 2027 Q2 | CC8.1, CC3.3, CC1.2 | Change log, updated risk analysis, owner review minutes |

**Response to the health system:** send this summary, the readiness checklist, and the POA&M (P07). Commit to an updated self-assessment in April 2027.
