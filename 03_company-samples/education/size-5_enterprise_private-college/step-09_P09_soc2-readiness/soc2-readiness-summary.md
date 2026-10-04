# SOC 2 Readiness Summary: Cris Santos Company | Educational Services | Enterprise

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (publicly traded postsecondary education company; operates the College) |
| Tier / Vertical | Enterprise / Educational Services |
| Criteria | AICPA 2017 Trust Services Criteria (With Revised Points of Focus, 2022) |
| Service lines | SL-1 Workforce Education Services (tuition-benefit programs for about 310 employer clients); SL-2 Online Program Services (LMS tenant hosting, instructional design, 24x7 student technical support, and learning analytics for 14 partner institutions, about 41,000 partner students) |
| Categories in scope | SL-1: Security, Availability, Confidentiality, and (new) Privacy. SL-2: Security, Availability, Confidentiality, and Processing Integrity |
| Target reports | SL-1: Type 2, period 2027-01-01 to 2027-12-31 (fourth annual report; Privacy added). SL-2: first Type 2, period 2027-04-01 to 2027-09-30 |
| Files | `soc2-readiness.csv` (every criterion for each service line: 122 rows); `soc2-evidence-map.csv` (25 evidence items) |
| Prepared | 2026-09-18 by the GRC team with the two service line owners; reviewed by the CISO and the Chief Audit Executive |

## 1. Why SOC 2 for this organization
Most of the company's work is teaching its own students, which SOC 2 does not cover. Two service lines are different: the company **provides services to other organizations**, so it is a service organization for them, and those clients ask for a CPA's SOC 2 report as part of their vendor reviews.
- **SL-1 Workforce Education Services.** About 310 employers fund tuition for their employees. Employer administrators use the SL-1 portal to enroll employees, see progress (only for students who have given written FERPA consent, 34 CFR 99.30(a)), and receive invoices. SL-1 has issued a SOC 2 Type 2 report (Security, Availability, Confidentiality) every year since 2024. Large employer clients now ask for **Privacy**, because the portal carries their employees' education records and consent choices.
- **SL-2 Online Program Services.** The company hosts LMS tenants and runs course design, student technical support, and learning analytics for 14 partner institutions. For that work it acts as a school official of each partner under FERPA (34 CFR 99.31(a)(1)(i)(B)), and partners that participate in Title IV must hold it to service provider safeguards by contract (16 CFR 314.4(f)(2)). Partners' vendor programs now require a SOC 2 Type 2 report that includes **Processing Integrity**, because roster sync and grade passback must be complete and accurate.

**Alternatives considered:** the profile for this vertical names no sector-specific assurance alternative. A higher education community vendor assessment questionnaire is accepted by some partners, but it is self-reported and does not replace an independent report. An ISO/IEC 27001 certification was considered and set aside because the clients ask for SOC 2 specifically and one framework per service line is cheaper to run.

**Relationship to other assurance:** the enterprise common controls (P02 section 10.3; P04 section 5) support both service lines, so one set of evidence serves both reports, the Safeguards Rule program (P03), and SOX IT general controls. Internal Audit's assessment (P07) is the main input; its POA&M items are the remediation plan for most gaps below. The cloud providers, the LMS vendor, and the video conferencing service are subservice organizations presented with the carve-out method; their own SOC reports are reviewed under CC9.2. SOC 2 is not a FERPA or Safeguards Rule compliance opinion and is not presented to clients as one.

## 2. System description (scope)
| Element | SL-1 Workforce Education Services | SL-2 Online Program Services |
|---|---|---|
| Services | Employer enrollment, consent-based progress reporting, invoicing for tuition-benefit programs (P05 BP-11, RTO 12 hours) | Partner LMS tenants, course design, 24x7 student technical support, learning analytics (P05 BP-12, RTO 8 hours) |
| Infrastructure | SL-1 portal on Cloud provider A managed containers inside the landing zone (P04) | LMS vendor SaaS (multi-tenant); integration platform on Cloud provider A for partner roster feeds |
| Software | Company-built SL-1 portal; SIS consent and disclosure records (SYS-01) | LMS partner tenants; LTI tools approved per partner; learning analytics dashboards built from LMS activity data |
| People | Workforce Education Services team; registrar's consent desk; SOC; identity and cloud platform teams | Online Program Services team; academic technology; support center; SOC |
| Data | Sponsored students' enrollment, progress (with consent), and invoice data; about 52,000 sponsored students | Partner students' roster, course activity, and grades (about 41,000 students); partner data does not enter the SIS |
| Procedures | P06 policy hierarchy; P08 runbook with client notice terms; SL-1 support procedures | P06; P08; partner onboarding and roster sync procedures |
| Subservice organizations (carved out) | Cloud provider A; email and notification service | LMS vendor; Cloud provider A; video conferencing service |
| User entity controls (complementary) | Employer administrators manage their users and attest quarterly (POL-02 4.8) | Partner administrators register their faculty and students and attest quarterly (POL-02 4.8; not yet operating, POAM-022) |

## 3. Readiness results
**SL-1 Workforce Education Services**
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33) | 33 | 0 | 0 | 0 |
| Availability (A1, 3) | 3 | 0 | 0 | 0 |
| Confidentiality (C1, 2) | 2 | 0 | 0 | 0 |
| Processing Integrity (PI1, 5) | | | | 5 |
| Privacy (P1-P8, 18) | 14 | 4 | 0 | 0 |

**SL-2 Online Program Services**
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33) | 19 | 12 | 2 | 0 |
| Availability (A1, 3) | 2 | 1 | 0 | 0 |
| Confidentiality (C1, 2) | 1 | 1 | 0 | 0 |
| Processing Integrity (PI1, 5) | 3 | 2 | 0 | 0 |
| Privacy (P1-P8, 18) | | | | 18 |

**SL-1** is ready for its next Type 2 on the existing categories. The new Privacy criteria have 4 partially ready items (P2.1, P3.2, P4.2, P6.1). Three come from one cause: 4 of 60 sampled sponsored students had no current FERPA consent and consent does not expire when a student leaves an employer program (POAM-021, due 2026-12-31). The fourth is the missing retention period for SL-1 portal data, which the records schedule approval fixes (POAM-010 milestone, 2026-12-31). All four close before the SL-1 period starts on 2027-01-01.

**SL-2** is not yet ready for a Type 2 period to start. Not ready: CC6.2 (partners register their own faculty with no attestation) and CC7.5 (the LMS vendor contract RTO is 24 hours against the 8-hour partner commitment). Partially ready: CC1.3, CC2.3, CC3.1, CC3.4, CC6.1, CC6.3, CC6.7, CC7.2, CC7.4, CC8.1, CC9.1, CC9.2, A1.3, C1.2, PI1.1, PI1.3. These are the same weaknesses found elsewhere in this folder: partner identity lifecycle (P01 R-022; POAM-022), shared roster transfer credentials (R-038), LMS recovery (R-011; POAM-007), vendor assurance (POAM-005), vendor incident handling (POAM-017), and partner launches without due diligence (R-061). Closing them by 2027-03-31 makes SL-2 ready to start its period on 2027-04-01.

## 4. Remediation plan and evidence calendar
| Quarter | Criteria addressed | Actions | Evidence to start collecting |
|---|---|---|---|
| 2026 Q4 | SL-1 P2.1, P3.2, P4.2, P6.1; SL-2 CC2.3, CC6.1, CC6.7, CC7.4, PI1.1 | Consent cleanup and expiry logic (POAM-021); retention schedule approval (POAM-010); partner notice procedure tested in the 2026-11-12 tabletop; MFA for all partner administrators; individual roster transfer accounts; vendor incident template (POAM-017); sync objectives documented | Consent records; approved schedule; tabletop report; MFA configuration; transfer account inventory |
| 2027 Q1 (January) | SL-2 CC1.3, CC3.1, CC3.4, CC6.2, CC6.3, CC8.1, C1.2, PI1.3 | SL-2 system description and commitments register; security checklist in partner onboarding; partner attestation and inactivity rule in all 14 tenants (POAM-022); LTI review standard (STD-05.4); data return and deletion addenda; daily roster reconciliation | Attestations; tenant inactivity reports; LTI reviews; reconciliation reports |
| 2027 Q1 (March) | SL-2 CC7.2, CC7.5, CC9.1, CC9.2, A1.3 | LMS event review for partner tenants; LMS contract amendment with an 8-hour RTO and observed failover (POAM-007); vendor reviews current (POAM-005) | Monthly review records; amended contract; failover report; vendor reviews |
| 2027 Q1 (late March) | Readiness check by Internal Audit for both lines; SL-2 Type 2 period starts 2027-04-01 | Mock walkthrough with the service auditor | Walkthrough results |

**Evidence map.** `soc2-evidence-map.csv` lists each evidence item, its source system, owner, frequency, and the Type 2 sample the service auditor is expected to draw. Items marked "Both" (13) are enterprise common controls collected once and used for both reports; 6 items are SL-1 only and 6 are SL-2 only. Status: 14 collecting, 4 ready, 7 not started (each tied to a POA&M item or a dated action above).

**Client communication:** SL-1 clients receive the 2025 report, a bridge letter, and a Privacy roadmap letter. SL-2 partners receive this summary, a bridge letter describing the remediation, and the expected SL-2 report date (2027-11).
