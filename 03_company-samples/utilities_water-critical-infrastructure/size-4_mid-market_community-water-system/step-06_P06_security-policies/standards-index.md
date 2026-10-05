# Security Standards Index

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Owner | Security Manager (index); each standard has its own owner below |
| Approved by | Chief Operating Officer, 2026-09-15 (index and issue schedule) |
| Authority | POL-01 statements 4.1 and 4.6; each standard sits under the parent policy named below |
| Review cycle | Each standard is reviewed at least annually by its owner |

## 1. Why this index exists
The 2024 policies stated intent but had thin supporting standards. There was no OT security standard and no rule for bringing an acquired water system into the program (gap 14 in `../00_company-facts.md`; P03 G-022; P01 R-050). Policies say **what** must happen. Standards set the **measurable minimums**: settings, frequencies, and thresholds. Procedures and runbooks sit under the standards and are owned by the teams that run them.

## 2. How standards work
- **Hierarchy:** policy (POL) to standard (STD) to procedure or runbook. A standard may not weaken its parent policy.
- **Approval:** the owner drafts it, the Security Manager reviews it for consistency, and the parent policy's approver signs it. OT standards also need the Director of Water Operations' sign-off, so that no requirement conflicts with safe operation.
- **Exceptions:** under POL-01 statement 4.7, time-limited and recorded in the risk register.
- **Testing:** each standard lists what P07 or internal audit checks.

## 3. Standards
| ID | Standard | Parent policy | Owner | Status (2026-09-15) | Target issue date | Key minimum requirements | Main SP 800-53 controls |
|---|---|---|---|---|---|---|---|
| STD-01 | **OT security standard** | POL-01, POL-02 | SCADA and Controls Engineering Manager with the OT security analyst | Draft in progress (gaps 1, 4, 7, 14) | 2027-03-31 | Zones and conduits per SP 800-82 Rev. 3 section 5 at every plant; OT DMZ for any IT or cloud flow; baselines for SCADA servers, HMIs, PLCs, and modems; PLC key switches in RUN except during approved changes; named HMI accounts; vaulted device credentials; offline backups of logic and projects; integrity comparison quarterly and after changes; OT inventory reconciled quarterly | AC-4, CM-2, CM-5, CM-6, CM-8, SC-7, SI-7 |
| STD-02 | **Logging and monitoring standard** | POL-03 | Security Manager | Draft in progress (gap 5) | 2027-01-31 | Required event types per system class (HMI security events, logic downloads, remote sessions, firewall and tunnel traffic, identity events); all covered systems' SCADA and VPNs send logs to the SIEM; passive OT sensors at every staffed plant; MSSP OT playbooks; high-severity OT alerts to the ROC within 15 minutes; 1 year searchable, 3 years archived | AU-2, AU-6, AU-11, AU-12, SI-4 |
| STD-03 | Configuration and encryption standard | POL-01, POL-04 | IT Director | Existing (2024); update due | 2027-03-31 | Benchmark-based baselines for workstations, servers, cloud images, and network devices; monthly drift report; TLS 1.2 or higher and approved algorithms; company-managed keys for cloud workloads; separate backup keys | CM-2, CM-6, SC-8, SC-12, SC-28 |
| STD-04 | Authenticator and privileged access standard | POL-02 | IT Director | Existing (2024); update due for OT devices and phishing-resistant MFA | 2026-12-31 | 14-character minimum and banned list; MFA for all users; phishing-resistant MFA for administrators and integrators; device credentials vaulted and rotated yearly and on staff change; service accounts vaulted and rotated; break-glass accounts tested quarterly | IA-2, IA-5, AC-6(2), AC-6(5) |
| STD-05 | Media sanitization and disposal standard | POL-04 | IT Director | Existing (2024) | In force | Methods by media type per NIST SP 800-88 Rev. 2; certificates for each batch; OT drives wiped or destroyed before leaving a plant; paper customer records shredded | MP-6, MP-4 |
| STD-06 | **Contingency and recovery standard** | POL-03 | SCADA and Controls Engineering Manager with the Emergency Management and Resilience Manager | Draft in progress (gaps 6, 10) | 2026-12-31 | Recovery objectives from the BIA (P05); written manual-mode procedure for each chemical feed at every plant; manual-mode drills twice a year at covered plants; annual SCADA rebuild test per covered system; offline backups for every OT site; alternate ROC position; link to each ERP | CP-2, CP-3, CP-4, CP-7, CP-9, CP-10 |
| STD-07 | **Acquisition integration standard** | POL-01 | Chief Operating Officer (owner) with the IT Director | Draft in progress (gap 14) | 2026-12-31 | OT security assessment during due diligence; risk register entry before close; isolation until baseline controls are met (gateway-only remote access, named accounts, offline backups, monitoring, inventory); interconnection agreement for any link to the ROC; RRA update trigger for covered systems; integrator contracts re-papered within 90 days | CA-3, RA-3, SA-4, PL-8 |
| STD-08 | **Vendor and OT remote access standard** | POL-01, POL-02 | Security Manager with the Purchasing Manager | Draft in progress (gap 9) | 2026-12-31 | Vendor tiers (Tier 1: OT remote access, customer or client data at scale, or support for a High BIA process); required contract terms (MFA, gateway-only access, background checks, 24-hour incident notice, return of project files, 72-hour breach notice for data vendors); annual SOC 2 or equivalent review for Tier 1; signed access agreement before any session; monthly session review | SA-9, SR-6, AC-17, MA-4, PS-7 |
| STD-09 | Vulnerability and patch management standard | POL-01 | Security Manager | Existing (2024, IT only); OT update due | 2026-12-31 | Monthly authenticated scans in IT; passive vulnerability identification in OT; quarterly external exposure scans of all public addresses and modems; weekly advisory review; IT remediation targets (Critical 14 days if internet-facing, 30 days otherwise); OT patches quarterly after vendor qualification, with compensating controls when patching must wait | RA-5, SI-2, SI-5 |
| STD-10 | **AI use standard** | POL-01, POL-05 | Water Quality and Compliance Manager with the vCISO | Draft in progress (gap 13) | 2026-12-31 | AI inventory; risk tiering per P10; review before use; no-training contract terms; pinned model versions with change notice; human review of outputs; no write path to SCADA; monitoring and decommissioning criteria | PM-9, SA-9, PL-4, RA-3 |

**Summary:** 10 standards. Six are new and in draft (STD-01, STD-02, STD-06, STD-07, STD-08, STD-10). Four exist from 2024: STD-05 is current, and STD-03, STD-04, and STD-09 need updates, mainly to add OT.

## 4. Issue schedule
| Quarter | Standards |
|---|---|
| 2026 Q4 | STD-04 update; STD-06 Contingency and recovery (needed for the Ridge ERP); STD-07 Acquisition integration; STD-08 Vendor and OT remote access; STD-09 OT update; STD-10 AI use |
| 2027 Q1 | STD-01 OT security; STD-02 Logging and monitoring; STD-03 update |

## 5. Related documents
POL-01 to POL-05; `policy-control-map.csv`; P03 roadmap; P07 POA&M; P10 AI governance process
