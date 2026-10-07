# Security Standards Index

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Owner | Security Manager (alternate CySO) for the index; each standard has its own owner below |
| Approved by | Chief Operating Officer, 2026-09-15 (index and issue schedule) |
| Authority | POL-01 statements 4.1 and 4.6; each standard sits under the parent policy named below |
| Review cycle | Each standard is reviewed at least annually by its owner, and after changes to the Coast Guard rule |

## 1. Why this index exists
The 2024 policies stated intent but had no supporting standards for OT security, vendor remote access, logging or configuration, and no channel for publicly reported vulnerabilities (gap 15 in `../00_company-facts.md`; P03 101.650(b), (c), (e)(3)(ii), (f); P01 R-032, R-040). Subpart F requires each cybersecurity measure to be "in place and documented" in the Cybersecurity Plan, so the measurable rules must exist in writing before the Plan is submitted (target 2027-05-28). Policies say **what** must happen. Standards set the **measurable minimums**: settings, frequencies, thresholds and owners. Procedures and runbooks sit under the standards and are owned by the teams that run them.

## 2. How standards work
- **Hierarchy:** policy (POL) → standard (STD) → procedure or runbook. A standard may not weaken its parent policy.
- **Approval:** the standard's owner drafts it, the Security Manager reviews it for consistency with the SSP (P02) and the Plan outline, and the Chief Operating Officer signs it.
- **Plan mapping:** each standard names the Subpart F paragraphs it documents, so the Cybersecurity Plan sections can cite it directly.
- **Exceptions:** under POL-01 section 4.7, time-limited, recorded in the risk register, with compensating controls documented for the Plan.
- **Testing:** each standard lists what P07 or internal audit checks.
- **Handling:** standards that contain network or OT security details are SSI (STD-10).

## 3. Standards
| ID | Standard | Parent policy | Owner | Status (2026-09-15) | Target issue date | Key minimum requirements | Main SP 800-53 controls | Subpart F paragraphs |
|---|---|---|---|---|---|---|---|---|
| STD-01 | **OT security standard** | POL-02, POL-04 | Director of Maintenance and Engineering with the OT network engineer | Draft in progress (gaps 1, 3, 13) | 2027-03-31 | OT zone at each terminal behind an industrial firewall, deny by default, documented conduits only; security systems in their own zone; named engineering accounts, with documented compensating controls for HMIs that cannot support them; USB and unused ports blocked, with an exception log; company maintenance laptops only; PLC program and HMI changes through change control with offline copies held by the company; passive OT monitoring at both terminals | SC-7, SC-7(5), AC-4, IA-2, MP-7, SI-7, CM-3 | 101.650(a)(6), (h), (i) |
| STD-02 | **Authenticator and privileged access standard** | POL-02 | Director of IT and Cybersecurity (CySO) | Draft in progress (gap 3) | 2027-03-31 | 14-character minimum and banned list; MFA for all identity provider users and remote OT access; FIDO2 keys for administrators; no standing domain, identity provider or TOS administrator rights (just-in-time elevation, maximum 4 hours); vaulted and rotated service account credentials; break-glass accounts tested quarterly; lockout after 10 failures | IA-2, IA-2(1), IA-5, AC-6(2), AC-6(5), AC-7 | 101.650(a)(1)-(7) |
| STD-03 | **Logging and monitoring standard** | POL-03, POL-04 | Security Manager (alternate CySO) | Draft in progress (gap 9) | 2027-01-31 | Required event sources per system class: identity, cloud, firewalls, EDR, portal, gate servers at all three gates, TOS application audit log (including hold overrides), PACS, and OT monitoring at both terminals; 1 year searchable in the SIEM and 2 years in the locked bucket; MSSP high-severity escalation within 30 minutes, including OT alerts; monthly review of vendor remote sessions | AU-2, AU-6, AU-9, AU-11, AU-12, SI-4 | 101.650(c)(1), (f)(3), (h)(2) |
| STD-04 | **Vendor and remote access standard** | POL-01, POL-02 | Procurement Manager with the Director of Maintenance and Engineering | Draft in progress (gaps 2, 8) | 2026-12-31 | Vendor tiers (Tier 1: access to critical IT or OT, or supports a High BIA process; Tier 2: other access or company data; Tier 3: neither); security criteria in every IT, OT and AI purchase; notice of vulnerabilities and reportable cyber incidents without delay (target 24 hours for Tier 1); SSI and personal information terms; all remote access through the privileged remote access service with per-session approval, MFA and recording; annual Tier 1 SOC 2 (or equivalent) review with CUEC mapping (P09) | SA-4, SA-9, SR-6, SR-8, AC-17, MA-4 | 101.650(e)(3)(v), (f)(1)-(3) |
| STD-05 | **Configuration and approved software standard** | POL-04 | Director of IT and Cybersecurity (CySO) | Draft in progress (gap 10) | 2027-03-31 | Approved hardware, firmware and software list for IT, OT and gate systems; benchmark-based baselines for servers, gate servers, kiosks, network devices and cloud services; allowlisting (executables disabled by default) on critical systems; default passwords changed at commissioning; monthly drift report; consolidated network map and OT configuration records updated after every change | CM-2, CM-3, CM-6, CM-7, CM-7(2), CM-8, CM-11, PL-8 | 101.650(a)(2), (b)(1)-(4) |
| STD-06 | **Contingency and recovery standard** | POL-03, POL-04 | Director of IT and Cybersecurity (CySO) | Draft in progress (gap 5) | 2026-12-31 | Recovery objectives from the BIA (P05); TOS hourly isolated snapshots and daily write-once backups; weekly gate server images at all gates; company-held PLC programs and HMI settings for both terminals; quarterly restore tests and an annual failover test to the standby region; manual gate, vessel and dangerous cargo list procedures per terminal; contingency plan coordinated with both FSPs | CP-2, CP-2(1), CP-4, CP-9, CP-10 | 101.650(g)(4) |
| STD-07 | Vulnerability, patch and disclosure standard | POL-01 | Security Manager (alternate CySO) | Existing (2024); update due (gaps 11, 15) | 2026-12-31 | Monthly authenticated scans of IT and T2 gate systems; passive OT vulnerability matching; KEV remediation within 72 hours for internet-facing systems and 7 days otherwise, or documented compensating controls; Critical 14 days and High 30 days for other findings; public vulnerability disclosure address and security.txt with 5-business-day acknowledgment; end-of-support systems replaced or isolated | RA-5, RA-5(11), SI-2, SI-5, SA-22 | 101.625(d)(15); 101.650(e)(3)(i)-(iii), (vi) |
| STD-08 | Encryption and key management standard | POL-04 | Director of IT and Cybersecurity (CySO) | Existing (2024); minor update | 2027-03-31 | TLS 1.2 or higher; AS2 or SFTP for EDI, FTP prohibited from 2026-12-31; encryption at rest for Restricted and SSI data; company-managed keys with separate backup keys; documented feasibility review for OT protocols | SC-8, SC-12, SC-13, SC-28 | 101.650(c)(2) |
| STD-09 | **AI use standard** | POL-01, POL-05 | vCISO with the Director of Planning | Draft in progress (gap 14) | 2026-12-31 | AI inventory; risk tiering per P10; security, data and business review before use; vendor terms with no training on company data; advisory mode for operations with human approval; constraint checks for planning tools; monitoring metrics and decommissioning criteria | PM-9, SA-9, PL-4, RA-3 | 101.650(b)(3), (f)(1) |
| STD-10 | **SSI handling standard** | POL-04 | Director of Port Security (T1 FSO) with the T2 Security Lead | Draft in progress (P03 101.630(b); 1520.9) | 2026-12-31 | Which cyber documents are SSI; marking; SSI-restricted repository and distribution list; vendor SSI terms and need-to-know checks; disposal; reporting of unauthorized disclosure to TSA or the applicable DHS component; annual SSI training for IT and security staff | MP-3, MP-4, MP-6, AC-3, AC-21 | 101.630(b) |

**Summary:** 10 standards. Eight are new and in draft (STD-01 to STD-06, STD-09 and STD-10), as requested in the gap analysis. STD-07 and STD-08 exist from 2024 and need updates.

## 4. Issue schedule
| Quarter | Standards |
|---|---|
| 2026 Q4 | STD-04 Vendor and remote access; STD-06 Contingency and recovery; STD-07 Vulnerability, patch and disclosure; STD-09 AI use; STD-10 SSI handling |
| 2027 Q1 | STD-03 Logging and monitoring (2027-01-31); STD-01 OT security; STD-02 Authenticator and privileged access; STD-05 Configuration and approved software; STD-08 Encryption (2027-03-31) |

All 10 standards will be issued before the Cybersecurity Assessment is completed (2027-03-31), so the Plan draft (2027-04-30) can reference them.

## 5. Related documents
POL-01 to POL-05; `policy-control-map.csv`; P03 roadmap; P07 POA&M; P10 AI governance process
