# SOC 2 Readiness Summary: Cris Santos Company | Public Administration | Enterprise

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (publicly traded GovTech systems integrator serving state and local agencies) |
| Tier / Vertical | Enterprise / Public Administration |
| Criteria | AICPA 2017 Trust Services Criteria (With Revised Points of Focus, 2022) |
| Service lines | SL-1 Agency Case Management Cloud (ACMC; 132 agency tenants); SL-2 IES operations (integrated eligibility systems, contact centers, and document processing for 4 state human services agencies) |
| Categories in scope | SL-1: Security, Availability, Confidentiality. SL-2: Security, Availability, Confidentiality, and Processing Integrity |
| Target reports | SL-1: Type 2, period 2027-01-01 to 2027-12-31 (fourth annual report). SL-2: first Type 2, period 2027-04-01 to 2027-09-30 |
| Files | `soc2-readiness.csv` (every criterion for each service line: 122 rows); `soc2-evidence-map.csv` (26 evidence items) |
| Prepared | 2026-09-25 by the GRC team with the President, State and Local Platforms and the President, Eligibility and Enrollment Operations; reviewed by the CISO and the Chief Audit Executive |

## 1. Why SOC 2 for this organization
The company is a **service organization** in the plainest sense: agencies hand it their data and their programs' daily operations, and they rely on its controls. Two service lines need a CPA's SOC 2 report.
- **SL-1 ACMC.** The multi-tenant case management service has issued a SOC 2 Type 2 report (Security, Availability, Confidentiality) every year since 2024, covering calendar years. Agency procurements and renewals ask for it, and local governments that cannot run their own supplier assessments rely on it. The 2026 report, due in 2027-02, is expected to carry exceptions for the findings Internal Audit raised in 2026 (P07), such as the FTI ticket exposure and late agency notices. This readiness review is for the **2027 period**.
- **SL-2 IES operations.** The 4 human services agencies rely on the company to run eligibility systems, answer applicants, and process their documents. Their contracts require an independent assurance report for the operation, and the 2027 renewals for the two out-of-state agencies name a SOC 2 Type 2 report with **Processing Integrity**, because accurate and timely eligibility processing is the core promise. There is no SOC 2 report for IES today.

**Why not Privacy.** For both lines, the agencies give privacy notices, collect consent, and answer access and correction requests under their program rules (42 CFR 431.300-431.307; 7 CFR 272.1(c); Florida and other state law). The company processes personal information only on agency instructions. The reason is recorded in each Privacy row of the CSV.

**Assurance alternatives and companions (not replacements):**
| Option | What it is | Role for this company |
|---|---|---|
| GovRAMP (formerly StateRAMP) | Nonprofit membership program, not law. Verification of cloud providers serving state and local governments against SP 800-53, with tiers (Core, Ready, Provisional or Authorized) (N92-R08) | ACMC holds Authorized status since 2025 (P02 section 4.2). Not pursued for IES: each IES environment is single-tenant and operated for one state, and the 4 agencies asked for SOC 2. The SP 800-53 evidence carries over between the two |
| CJIS audits by state CJIS Systems Agencies | Audits of criminal justice agencies and their contractors against CJISSECPOL | Required for ACMC CJI tenants and legacy hosting regardless of SOC 2. Results go to the audited agency, not to other customers |
| IRS safeguard reviews | IRS Office of Safeguards reviews of revenue agencies, which can include contractor facilities (Pub. 1075) | Required for the 6 FTI tenants regardless of SOC 2. Not relevant to IES, which holds no FTI |
| FedRAMP | Federal authorization program | Not pursued: no federal agency uses ACMC or IES. The cloud providers' FedRAMP Moderate authorizations are used as subservice evidence |
| CMMC Level 2 | DoD certification for the CUI enclave (32 CFR Part 170) | Separate track (POAM-023); the enclave is outside both SOC 2 systems |

**Relationship to other assurance.** The enterprise common controls (identity, landing zone, SOC, software delivery, third-party risk; P02 section 10.3 and P04 section 5) support both service lines, so one set of evidence serves both reports, the GovRAMP package, agency audits, and SOX IT general controls. Items marked "Both" in the evidence map are collected once.

## 2. System description (scope)
| Element | SL-1 ACMC | SL-2 IES operations |
|---|---|---|
| Services | Hosting, operation, and support of case management for 132 agency tenants (justice and public safety, revenue, motor vehicle, local government); the integration hub interfaces that feed it | Operation of 4 single-tenant eligibility systems for SNAP, TANF, and Medicaid; contact centers (about 61,000 calls a day); document scanning and indexing (about 120,000 pages a day); eligibility notices; AG-04 Medicaid enrollment and premium processing support |
| Infrastructure | Cloud provider A, two U.S. regions; integration hub cloud services and the DC-1 VPN edge (SYS-01, SYS-02) | Cloud provider B, U.S. regions; document processing centers; telephony (SYS-03, SYS-12) |
| Software | ACMC application; integration hub; identity platform; pipeline (SYS-04, SYS-06) | IES application and rules engine; document management; AI eligibility assistant pilot (AI-001, suggestions off since 2026-09-11) |
| People | ACMC platform operations; SOC; identity, cloud, and network teams; support | Eligibility operations staff (about 1,500); IES engineering; SOC; identity and cloud teams |
| Data | FTI (6 tenants), CJI including CHRI (15 tenants), DPPA motor vehicle records, local government data; about 22 million individuals | Applicant and household data, Social Security numbers, income documents, AG-04 ePHI; about 14 million individuals; **no FTI** |
| Procedures | P06 policy hierarchy; P08 runbook; ACMC operations procedures | P06; P08; state-specific eligibility operations procedures |
| Subservice organizations (carve-out) | Cloud provider A; colocation provider for DC-1; ticketing SaaS; tier-1 help desk subcontractor for municipal customers | Cloud provider B; document imaging and mail vendor; telephony carrier; identity verification service; managed language model service (AI-001) |

**Out of scope for both reports:** legacy managed hosting (SYS-09), AQ-1 (SYS-15), and the CUI enclave (SYS-10). Where those systems touch ACMC (the AQ-1 peering, the DC-1 VPN edge), the connection is in scope.

**Complementary user entity controls** the agencies must run, listed in each report and contract: approve and review their users' access; enforce MFA in their own identity providers where they federate; keep FTI and CJI out of tickets and free-text fields; tell the company promptly of incidents on their side; and, for IES, make every eligibility decision through their own merit staff (7 CFR 272.4(a)(2); 42 CFR 431.10).

## 3. Readiness results
**SL-1 ACMC**
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33) | 20 | 13 | 0 | 0 |
| Availability (A1, 3) | 2 | 1 | 0 | 0 |
| Confidentiality (C1, 2) | 0 | 2 | 0 | 0 |
| Processing Integrity (PI1, 5) | | | | 5 |
| Privacy (P1-P8, 18) | | | | 18 |

**SL-2 IES operations**
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33) | 24 | 7 | 2 | 0 |
| Availability (A1, 3) | 2 | 0 | 1 | 0 |
| Confidentiality (C1, 2) | 1 | 1 | 0 | 0 |
| Processing Integrity (PI1, 5) | 2 | 3 | 0 | 0 |
| Privacy (P1-P8, 18) | | | | 18 |

**SL-1 has no Not ready criteria, but 16 are Partially ready:** CC1.4, CC2.2, CC3.4, CC6.2, CC6.3, CC6.5, CC6.6, CC6.7, CC7.1, CC7.2, CC7.4, CC8.1, CC9.2, A1.2, C1.1, and C1.2. Each matches a 2026 Internal Audit finding or a P03 gap: the AQ-1 peering and directory (POAM-001, POAM-004), CJIS screening (POAM-002), the VPN cryptography and FTI ticket exposure (POAM-006, POAM-009), standing CJI support access (POAM-016), late agency notices (POAM-014), deletion certificates (POAM-020), and supplier reviews (POAM-011). **14 of the 16 are due to close before the period starts on 2027-01-01.** Two close later and will be described in the report if still open:
- CC6.2: AQ-1 federation completes 2027-01-31 (POAM-001). Compensating control: AQ-1 engineers reach ACMC only through the restricted peering and are reviewed monthly.
- A1.2: the second VPN edge in DC-2 is due 2027-06-30 (P01 R-031). Compensating control: cloud-to-cloud interfaces and agency message switch terminals.

Controls fixed late in 2026 will have only a short operating history when the period starts. The service auditor will test them across the full year, so a fix that slips (for example the SOAR timer for CC7.4, due 2026-12-15) becomes a report exception.

**SL-2 is not yet ready for a Type 2 period to start.** Not ready: CC2.3 (no system description or written user entity controls), CC9.2 (the document imaging and mail vendor handles AG-04 ePHI without business associate terms), and A1.3 (AG-04 recovered in 14 hours against an 8-hour RTO). Partially ready: CC3.1, CC3.2, CC4.1, CC6.2, CC7.5, CC8.1, CC9.1, C1.1, PI1.1, PI1.3, and PI1.4. Closing the system description (2027-01-31), the IES DR redesign and retest (POAM-015, 2027-02-28), the subcontractor BAA (2026-11-30), the vendor backlog and the Internal Audit assessment of IES (POAM-011, POAM-012, 2027-03-31), and the AI-001 conditions (POAM-022, 2026-12-31) makes SL-2 ready to start its period on 2027-04-01. **C1.1 closes later** (tokenized Social Security numbers in analytics extracts, 2027-06-30); the compensating control is that extracts are limited to the analytics role with data loss prevention, and it would be described in the report.

**Why Processing Integrity is the hard part for SL-2.** The eligibility rules engine and document quality checks are mature (PI1.2, PI1.5 Ready). The gaps are the AI-001 pilot, where caseworkers accepted most AI suggestions including wrong ones (PI1.3; P10), and notice reconciliation, which runs daily only for AG-03 (PI1.4). A notice that is generated but never mailed can push a household past federal processing deadlines, so the reconciliation is extended to all 4 states before the period starts.

## 4. Remediation plan and evidence calendar
| Quarter | Criteria addressed | Actions | Evidence to start collecting |
|---|---|---|---|
| 2026 Q4 (by 2026-10-31) | SL-1 CC1.4, CC2.2, CC7.2; both CC6.2 (subcontractors) | Screening and certification reconciliation; recertification automation; weekly FTI review workflow; subcontractor termination feed | Certification lists; recertification reports; review records; termination feed reports |
| 2026 Q4 (by 2026-12-31) | SL-1 CC3.4, CC6.3, CC6.5, CC6.6, CC6.7, CC7.1, CC7.4, CC8.1, CC9.2, C1.1, C1.2; SL-2 CC3.2, CC8.1, PI1.3, CC9.2 (BAA) | AQ-1 peering allow-list and interconnection agreement; just-in-time CJI support access; deletion certificates; FTI discovery in tickets; SOAR timer; emergency change gate; ACMC supplier reviews; AI-001 conditions; masking gate; mail vendor BAA | Peering rules; PAM logs; certificates; scan results; timer reports; change records; vendor reviews; AI monitoring reports; signed BAA |
| 2027-01-01 | All SL-1 in-scope criteria | **SL-1 Type 2 period starts** (2027-01-01 to 2027-12-31) | Monthly evidence folders per criterion |
| 2027 Q1 | SL-1 CC6.2 (AQ-1); SL-2 CC2.3, CC3.1, PI1.1 (by 2027-01-31); CC7.5, A1.3 (by 2027-02-28); CC4.1, CC9.1, CC9.2, PI1.4 (by 2027-03-31) | AQ-1 federation; SL-2 system description and user entity controls; IES DR retest; Internal Audit assessment of IES; print and mail fallback test; notice reconciliation for all 4 states | Federation records; system description; DR retest report; audit report; fallback test report; reconciliation reports |
| 2027 Q1 (March) | Readiness check by Internal Audit for SL-2 | Mock walkthrough with the service auditor | Walkthrough results |
| 2027-04-01 | All SL-2 in-scope criteria | **SL-2 Type 2 period starts** (2027-04-01 to 2027-09-30) | Monthly evidence folders per criterion |
| 2027 Q2 | SL-1 A1.2; SL-2 C1.1 (by 2027-06-30) | Second VPN edge in DC-2; tokenized Social Security numbers in analytics extracts | Tunnel test report; extract scans |

**Evidence map.** `soc2-evidence-map.csv` lists each evidence item, its source system, owner, frequency, the Type 2 sample the service auditor is expected to draw, and the deliverable it reuses. Items marked "Both" are enterprise common controls collected once for both reports. Status: 12 collecting, 5 ready, 9 not started (each tied to a POA&M item or a dated action above).

**Owner and follow-up.** The GRC team runs the program; each service line president owns its readiness. Progress is reported monthly to the executive risk committee with the POA&M. **Agency communication:** ACMC customers receive the 2026 report when issued, a bridge letter, and this summary's SL-1 section; the 4 IES agencies receive this summary, the remediation calendar, and the expected first SL-2 report date (2027-11).
