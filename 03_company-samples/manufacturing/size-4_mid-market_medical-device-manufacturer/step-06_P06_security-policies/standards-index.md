# Security Standards Index

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Owner | Security Manager (index); each standard has its own owner below |
| Approved by | Chief Operating Officer, 2026-09-17 (index and issue schedule) |
| Authority | POL-01 statements 4.1 and 4.9; each standard sits under the parent policy named below |
| Review cycle | Each standard is reviewed at least annually by its owner |

## 1. Why this index exists
The 2024 policies stated intent, but staff, controls engineers, and suppliers had no measurable rules for OT security, secure configuration, or supplier security (gap 14 in `../00_company-facts.md`; P03 G-115; P01 R-040). Product security rules lived in a separate 2025 PSIRT procedure and the SPDF. Policies say **what** must happen. Standards set the **measurable minimums**: settings, frequencies, service levels, and thresholds. Procedures and runbooks sit under the standards; QMS procedures (design control, complaint handling, MDR, corrections and removals) stay in the eQMS and reference these standards.

## 2. How standards work
- **Hierarchy:** policy (POL) → standard (STD) → procedure, work instruction, or runbook. A standard may not weaken its parent policy.
- **Approval:** the standard's owner drafts it, the Security Manager reviews it for consistency, and the parent policy's approver signs it. Standards that change QMS procedures also go through QMS document control (VP QA/RA).
- **Exceptions:** under POL-01 section 4.10, time-limited and recorded in the risk register.
- **Testing:** each standard lists what P07 or internal audit checks.

## 3. Standards
| ID | Standard | Parent policy | Owner | Status (2026-09-17) | Target issue date | Key minimum requirements | Main SP 800-53 controls |
|---|---|---|---|---|---|---|---|
| STD-01 | **Secure configuration standard** | POL-01, POL-04 | Security Manager | Draft in progress (gap 14) | 2027-03-31 | Benchmark-based baselines for cloud accounts, container images, servers, and endpoints; documented deviations; monthly drift report; infrastructure changes only through the pipeline | CM-2, CM-6, CM-7 |
| STD-02 | **Logging and monitoring standard** | POL-03 | Security Manager | Draft in progress (gap 8) | 2027-01-31 | Required event types per system class, including CCC privileged actions and PHI exports, signing service events, MES and provisioning server events; all DLP components send logs to the SIEM; 1 year searchable and 6 years archived for security logs; weekly privileged activity review; MSSP high-severity escalation within 30 minutes | AU-2, AU-6, AU-11, AU-12, SI-4 |
| STD-03 | **Supplier and vendor security standard** | POL-01 | Compliance and Privacy Officer with the Director of Supply Chain | Draft in progress (gap 10) | 2026-12-31 | Tiers (Tier 1: PHI at scale, privileged access, or supports a High BIA process; Tier 2: limited PHI or system access; Tier 3: neither); subcontractor BAA before any PHI; Tier 1 annual SOC 2 Type 2 review with complementary user entity control mapping; critical software component suppliers commit to vulnerability notice within 30 days, support dates, and SBOM delivery; line equipment vendors use brokered remote access only | SA-9, SR-5, SR-6, RA-3(1) |
| STD-04 | **OT security standard** | POL-02, POL-05 | OT Engineering Manager | Draft in progress (gap 4) | 2027-03-31 | Written against NIST SP 800-82 Rev. 3: complete OT asset inventory with firmware versions; zones per line with deny-by-default conduits; no persistent vendor VPNs; application allowlisting on every station; compensating controls for unsupported stations until replaced; passive OT monitoring; offline and cloud copies of MES data with quarterly restore tests; station software changes under design change control | CM-8, SC-7, AC-17, MA-4, SI-3, SA-22, CP-9 |
| STD-05 | **AI use standard** | POL-01, POL-05 | Chief Medical Officer with the vCISO and VP QA/RA | Draft in progress (gap 13) | 2026-12-31 | AI inventory; risk tiering per P10; review before use; AI in devices governed by design controls and the predetermined change control plan where authorized; AI in quality processes validated as QMS software; enterprise tools only under no-training terms; public AI tools blocked on company devices | PM-9, SA-9, PL-4, RA-3 |
| STD-06 | Authenticator and privileged access standard | POL-02 | IT Director | Existing (2024); update due | 2026-12-31 | 14-character minimum and banned list; MFA for all; phishing-resistant MFA for administrators; just-in-time elevation for production and signing; quarterly break-glass tests; badge-based individual login on plant stations | IA-2, IA-5, AC-6(5) |
| STD-07 | Contingency and recovery standard | POL-03 | IT Director with the Director of Cloud Operations | Draft in progress (gap 11) | 2026-12-31 | Recovery objectives from the BIA (P05); quarterly CCC failover tests; yearly HSM key recovery exercise; MES restore tests; golden images for every station type | CP-2, CP-4, CP-9, CP-10 |
| STD-08 | Cryptography and key management standard | POL-04 | Product Security Manager | Existing (2025); update due | 2026-12-31 | Approved algorithms and protocols (TLS 1.2 or higher); signing and certificate authority keys only in the HSM with dual control; no software-held issuing keys; key inventory; rotation and revocation procedures | SC-12, SC-13, SC-17, SC-28 |
| STD-09 | Vulnerability and patch management standard | POL-01, POL-03 | Product Security Manager (products) and Security Manager (IT and OT) | Existing (2025); update due | 2026-12-31 | Products: daily SBOM matching including the KEV catalog; triage within 7 days for KEV items and 30 days for critical items; justified regular release cycle per product; out-of-cycle path with 30-day customer communication and 60-day fix for uncontrolled risk; field adoption reported to hospitals. IT and cloud: monthly authenticated scans; critical fixes within 14 days internet-facing, 30 days otherwise | RA-5, SI-2, SI-5 |
| STD-10 | Secure product development and release standard | POL-01 | VP Engineering with the VP QA/RA | Existing (2025 SPDF); update due | 2026-12-31 | Threat models and cybersecurity risk assessments per release; architecture views including the provisioning path; SBOM per build; static, composition, and fuzz testing; independent penetration tests yearly on production units; two-person signing; release manifests verified by stations; cybersecurity impact question mandatory in change control, including station software | SA-3, SA-8, SA-11, SA-15, CM-3, CM-4, CM-14 |

**Summary:** 10 standards. The 5 new standards requested in the gap analysis (STD-01 to STD-05) are in draft. STD-06, STD-08, STD-09, and STD-10 exist and need updates. STD-07 is new and is needed for the CCC failover and key recovery work.

## 4. Issue schedule
| Quarter | Standards |
|---|---|
| 2026 Q4 | STD-03 Supplier and vendor security; STD-05 AI use; STD-06; STD-07 Contingency and recovery; STD-08; STD-09; STD-10 |
| 2027 Q1 | STD-01 Secure configuration; STD-02 Logging and monitoring; STD-04 OT security |

## 5. Related documents
POL-01 to POL-05; `policy-control-map.csv`; P03 roadmap; P07 POA&M; P10 AI governance process; QMS procedures in the eQMS
