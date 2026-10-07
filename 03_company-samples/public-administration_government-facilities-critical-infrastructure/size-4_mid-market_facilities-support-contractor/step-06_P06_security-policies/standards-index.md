# Security Standards Index

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Owner | GRC analyst (index); each standard has its own owner below |
| Approved by | Chief Operating Officer, 2026-09-15 (index and issue schedule) |
| Authority | POL-01 statements 4.1 and 4.6; each standard sits under the parent policy named below |
| Review cycle | Each standard is reviewed at least annually by its owner |

## 1. Why this index exists
The 2024 policies stated intent, and IT had working standards, but OT had none. Staff and subcontractors had no measurable rules for OT hardening, logging, remote access, or BAS change control (gap 12 in `../00_company-facts.md`; P03 CM-6, AU-2, SA-9, CM-3; P01 R-001, R-003, R-009, R-017). Policies say **what** must happen. Standards set the **measurable minimums**: settings, frequencies, and thresholds. Procedures (how-to steps) sit under the standards and are owned by the teams that run them.

## 2. How standards work
- **Hierarchy:** policy (POL) → standard (STD) → procedure or runbook. A standard may not weaken its parent policy.
- **Approval:** the standard's owner drafts it, the GRC analyst checks it for consistency, the vCISO reviews it, and the parent policy's approver signs it.
- **Exceptions:** under POL-01 section 4.7, time-limited and recorded in the risk register.
- **Testing:** each standard lists what P07 or internal audit checks.

## 3. Standards
| ID | Standard | Parent policy | Owner | Status (2026-09-15) | Target issue date | Key minimum requirements | Main SP 800-53 controls |
|---|---|---|---|---|---|---|---|
| STD-01 | **OT hardening and configuration standard** | POL-01, POL-02 | OT Security Engineer | Draft in progress (gap 12) | 2027-03-31 | Secure settings for edge firewalls, engineering workstations, BAS clusters, and field controllers; default credentials removed at commissioning; unused services disabled; OT reference architecture (zones, conduits, broker-only management); quarterly drift and default-credential checks | CM-2, CM-6, CM-7, PL-8, SC-7 |
| STD-02 | **Logging and monitoring standard** | POL-02, POL-03 | Security Manager with the OT Security Engineer | Draft in progress (gap 5) | 2027-01-31 | Required event types per system class, including BAS program downloads, tenant administrator actions, door commands at sensitive doors, and OT sensor alerts; all sources to the SIEM; 1 year searchable and 3 years in the write-once bucket; weekly OT review until OT use cases are live; ROC escalation path for OT alerts | AU-2, AU-6, AU-11, AU-12, SI-4 |
| STD-03 | **Third-party, subcontractor, and remote access standard** | POL-01, POL-02 | Contracts Director with the OT Security Engineer | Draft in progress (gaps 1 and 7) | 2026-12-31 | Security addendum terms (MFA, broker-only access, 24-hour incident notice, background checks, FAR flow-downs, CUI terms); vendor and subcontractor tiers; annual review of OT subcontractors and Tier 1 vendors with SOC 2 review where available; per-session approval rules; prohibited tools (always-on remote support, vendor relays, modems) | SA-9, SR-6, PS-7, AC-17, MA-4 |
| STD-04 | **BAS and access control change management standard** | POL-01 | Director of Building Technology | Draft in progress (gap 10) | 2026-12-31 | CMMS change ticket with second-person approval for programs and door schedules; emergency change rules; weekly change report; hash of the approved program stored in the repository and checked before download | CM-3, CM-5, SI-7 |
| STD-05 | **AI use standard** | POL-01, POL-05 | vCISO with the Security Manager | Draft in progress (gap 11) | 2026-12-31 | AI inventory; risk tiering per P10; security, privacy, legal, and fairness review before use; no-training and deletion terms with vendors; human review of outputs; biometric consent, notice, and retention rules; monitoring and decommissioning criteria | PL-4, SA-9, RA-3, SI-12 |
| STD-06 | Authenticator and device credential standard | POL-02 | IT Director (ISO) | Existing (2024, IT only); OT section due | 2027-03-31 | 14-character minimum and banned list; phishing-resistant MFA for administrators; device credentials only in the vault, unique per site, rotated on staff exit; break-glass accounts tested quarterly | IA-2, IA-5, AC-6 |
| STD-07 | Contingency and manual-mode operations standard | POL-01, POL-04 | IT Director (ISO) with the VP Operations | Draft in progress (gap 6) | 2026-12-31 | Recovery objectives from the BIA (P05); manual-mode procedure per customer site with the EOC and data center building first; quarterly cluster restore tests; semiannual backup ROC failover drill; annual customer exercise | CP-2, CP-4, CP-9, CP-10 |
| STD-08 | Encryption and key management standard | POL-04 | IT Director (ISO) | Existing (2024) | Minor update 2027-03-31 | Approved algorithms and protocols (TLS 1.2 or higher); encryption at rest for all Restricted data; company-managed keys for the CUI library and backups; separate backup keys | SC-8, SC-12, SC-13, SC-28 |
| STD-09 | Vulnerability, patch, and firmware management standard | POL-01 | Security Manager with the OT Security Engineer | Existing (2024, IT only); OT section due | 2027-03-31 | Monthly authenticated scans for IT; passive OT vulnerability identification; weekly review of known exploited vulnerabilities and ICS advisories; targets: critical internet-facing 14 days, others 30 days; edge firmware reviewed monthly; OT firmware in customer windows | RA-5, SI-2, SI-5 |
| STD-10 | CUI handling standard | POL-04 | Contracts Director | Existing (2024); update due | 2026-12-31 | CUI library only; marking of derivatives; secure links; data loss rule on CUI markings; locked cabinets at federal buildings; subcontractor CUI terms; CUI training | MP-2, MP-3, MP-4, AC-21 |

**Summary:** 10 standards. 6 are new and in draft (STD-01 to STD-05 and STD-07). STD-06, STD-09, and STD-10 exist from 2024 and need OT or other updates. STD-08 exists and needs a minor update.

## 4. Issue schedule
| Quarter | Standards |
|---|---|
| 2026 Q4 | STD-03 Third-party, subcontractor, and remote access; STD-04 Change management; STD-05 AI use; STD-07 Contingency and manual-mode operations; STD-10 CUI handling |
| 2027 Q1 | STD-01 OT hardening; STD-02 Logging and monitoring; STD-06; STD-08; STD-09 |

## 5. Related documents
POL-01 to POL-05; `policy-control-map.csv`; P03 roadmap; P07 POA&M; P10 AI governance process
