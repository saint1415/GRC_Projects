# SOC 2 Readiness Summary: Cris Santos Company | Construction | Enterprise

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (publicly traded commercial and institutional building general contractor) |
| Tier / Vertical | Enterprise / Construction |
| Criteria | AICPA 2017 Trust Services Criteria (With Revised Points of Focus, 2022) |
| Service lines | SL-1 BTS managed building technology services (remote monitoring and administration of access control, video surveillance, and building automation for about 420 client buildings); SL-2 Capital Program Portal (owner-facing program controls for about 35 institutional owners) |
| Categories in scope | SL-1: Security, Availability, and (new) Confidentiality. SL-2: Security, Availability, Confidentiality, and Processing Integrity. All five categories were evaluated for both lines; Privacy is out of scope for both, and Processing Integrity for SL-1 (section 2) |
| Target reports | SL-1: Type 2, period 2027-01-01 to 2027-12-31 (third annual report; Confidentiality added). SL-2: first Type 2, period 2027-04-01 to 2027-09-30 |
| Files | `soc2-readiness.csv` (every criterion for each service line: 122 rows); `soc2-evidence-map.csv` (25 evidence items) |
| Prepared | 2026-08-21 by the GRC team with the service line owners; reviewed by the CISO and the Chief Audit Executive |

## 1. Why SOC 2 for this organization
Most of the company's work is construction, which SOC 2 does not cover, and the construction vertical names no sector-specific assurance alternative. Two service lines are different: the company **provides ongoing technology services to other businesses**, so it is a service organization for them, and their clients ask for a CPA's SOC 2 report.
- **SL-1 BTS managed services.** BTS holds administrator credentials and layouts for about 420 client buildings, including 9 federal buildings, and monitors their access control, cameras, and building automation 24x7. Clients' security and risk teams require a SOC 2 Type 2 report. SL-1 has issued one (Security and Availability) since 2025; clients now ask for **Confidentiality** because their facility security details are the most sensitive data BTS holds (P01 R-030).
- **SL-2 Capital Program Portal.** Universities, health systems, and public owners use the portal to manage budgets, review pay apps, track change orders, and keep program documents. Their procurement and audit offices now require a SOC 2 Type 2 report, including **Processing Integrity**, because owners approve payments based on portal figures.

**Alternatives considered:** ISO/IEC 27001 certification (some owners accept it, but most institutional procurement offices named SOC 2); CMMC (covers FCI and CUI for DoD, not commercial services; SL-1's 9 federal buildings are already in the enterprise FCI scope); bridge letters and questionnaires only (no longer accepted by the larger clients). SOC 2 is the one report both client groups accept.

**Relationship to other assurance:** the enterprise common controls (P02 section 10.3; P04) support both service lines, so one set of evidence serves both reports, the CMMC Level 1 self-assessment, and the SOX program. Cloud providers A and B and the remote access gateway service are subservice organizations presented with the carve-out method; their SOC 2 reports are reviewed under CC9.2.

## 2. System description (scope)
| Element | SL-1 BTS managed services | SL-2 Capital Program Portal |
|---|---|---|
| Services | 24x7 monitoring, alarm handling, remote administration, and credential management for client access control, video surveillance, and building automation | Budgets, pay app review and approval, change order logs, schedules, and document control for owner capital programs |
| Infrastructure | Monitoring platform on Cloud provider B with an active-passive second region (P04); remote access gateway; client credential vault | Company-built application on Cloud provider A managed containers with a second-region standby (P04) |
| Software | Monitoring platform; vendor management consoles for client systems; vault | Portal application and APIs; integration with the company ERP for pay app data |
| People | About 600 BTS technicians and engineers, the BTS operations center, the SOC, and identity and cloud teams | Program Management Services staff, the portal development team, the SOC, and identity and cloud teams |
| Data | Client building layouts, camera locations, device credentials, alarm and access event data | Owner budgets, contracts, pay app figures, change orders, and program documents |
| Procedures | P06 policy hierarchy; P08 runbooks; BTS service procedures | P06; P08; portal release and support procedures |
| Subservice organizations (carved out) | Cloud provider B; remote access gateway service; colocation provider (COLO-2) | Cloud provider A; e-signature service; email delivery service |
| Not in scope | Installation projects (construction work); client-owned equipment | The company's own construction projects in SYS-01 |

**Why Privacy and SL-1 Processing Integrity are out of scope.** Neither service line collects personal information from data subjects as part of the service; personal data is limited to client staff contact details and access event records that clients control. SL-1 administers client systems but does not process client transactions, so Processing Integrity does not fit its commitments. Both decisions are reviewed annually with the service line owners.

## 3. Readiness results
**SL-1 BTS managed building technology services**
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33) | 30 | 3 | 0 | 0 |
| Availability (A1, 3) | 3 | 0 | 0 | 0 |
| Confidentiality (C1, 2) | 0 | 2 | 0 | 0 |
| Processing Integrity (PI1, 5) | | | | 5 |
| Privacy (P1-P8, 18) | | | | 18 |

**SL-2 Capital Program Portal**
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33) | 26 | 6 | 1 | 0 |
| Availability (A1, 3) | 3 | 0 | 0 | 0 |
| Confidentiality (C1, 2) | 1 | 1 | 0 | 0 |
| Processing Integrity (PI1, 5) | 3 | 1 | 1 | 0 |
| Privacy (P1-P8, 18) | | | | 18 |

**SL-1** is ready to continue its Type 2 on Security and Availability, with 3 partially ready Security items: CC6.1 (client credential rotation), CC6.6 (37 buildings on owner-mandated remote tools, EXC-2026-030), and CC9.2 (Section 889 screening of private-label products, POAM-022). The new Confidentiality criteria (C1.1, C1.2) are partially ready: client layouts and credentials were found outside the vault, and there is no contract-exit deletion procedure. These must close by 2027-02-28 to give the auditor most of the 2027 period; anything still open would be described in the report as an exception.

**SL-2** is not yet ready for a Type 2 period to start. Not ready: CC2.3 (no system description or client security commitments) and PI1.3 (no reconciliation of portal pay app totals to owner approvals and the ERP). Partially ready: CC1.3, CC3.3, CC6.2, CC6.3, CC7.2, CC8.1, C1.2, and PI1.1. The pattern matches the P07 findings for the PDPP: account lifecycle for external users, change approval for hotfixes, and attributable records for payment-related approvals. Closing all SL-2 items by 2027-03-31 lets the period start on 2027-04-01.

**Link to payment fraud (P08).** SL-2 shows pay app figures and remittance-related documents to owners. CC3.3 is partially ready because the fraud risk assessment does not yet treat the portal as a channel for false remittance instructions; P08 variant A applies if it is used that way.

## 4. Remediation plan and evidence calendar
| Quarter | Criteria addressed | Actions | Evidence to start collecting |
|---|---|---|---|
| 2026 Q4 | SL-1 C1.2, CC9.2; SL-2 CC1.3, CC3.3, CC8.1 | Contract exit procedure; Section 889 distributor attestations (POAM-022); portal security lead named; portal added to payment fraud scenarios; pipeline block on unapproved hotfixes | Exit certificates; screening log; pipeline approvals |
| 2027 Q1 (January and February) | SL-1 CC6.1, C1.1; SL-2 CC2.3, CC6.2, CC6.3, CC7.2, PI1.1, PI1.3 | Automated vault rotation; DLP for client credentials; SL-2 system description and client addendum; owner attestations and inactivity disable; application audit events to the SIEM; processing specifications; daily reconciliation | Rotation reports; DLP reports; attestations; reconciliation reports |
| 2027 Q1 (March) | SL-2 C1.2; SL-1 CC6.6; readiness check by Internal Audit (both lines) | Automated tenant deletion; gateway coverage for the remaining client buildings; mock walkthrough with the service auditor | Walkthrough results |
| 2027 Q2 | SL-2 Type 2 period starts 2027-04-01 | Monthly evidence collection for both lines | Evidence map items |

**Evidence map.** `soc2-evidence-map.csv` lists each evidence item, its source system, owner, frequency, and the Type 2 sample the service auditor is expected to draw. Items marked "Both" are enterprise common controls collected once and used for both reports. Status: 11 collecting, 5 ready, 9 not started (each tied to a remediation action above or to the 2026-11-19 tabletop).

**Client communication:** SL-1 clients receive the 2025 report, a bridge letter (the 2026 report is due in 2027 Q1), and a Confidentiality roadmap letter; SL-2 owners receive this summary, a bridge letter describing the remediation, and the expected SL-2 report date (2027-11).
