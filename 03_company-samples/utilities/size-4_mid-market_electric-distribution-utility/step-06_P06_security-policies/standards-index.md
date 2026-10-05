# Security Standards Index

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Owner | Information Security Manager (index); each standard has its own owner below |
| Approved by | Chief Operating Officer, 2026-09-17 (index and issue schedule) |
| Authority | POL-01 statements 4.1 and 4.8; each standard sits under the parent policy named below |
| Review cycle | Each standard is reviewed at least annually by its owner |

## 1. Why this index exists
The 2022 and 2025 policies stated intent, but OT, vendor, and customer data rules were not measurable. The 2026 assessments found the results: legacy IT/OT rules (gap 4), shared OT administrator accounts (gap 5), a contractor modem at a BES substation (gap 2), default passwords on field routers (P07), no OT supply chain review (gap 9), and identity data kept without limit (gap 12). Policies say **what** must happen. Standards set the **measurable minimums**: settings, frequencies, and thresholds. Procedures and runbooks sit under the standards and are owned by the teams that run them.

## 2. How standards work
- **Hierarchy:** policy (POL) to standard (STD) to procedure or runbook. A standard may not weaken its parent policy or a NERC requirement.
- **Approval:** the standard's owner drafts it, the Information Security Manager reviews it for consistency, the NERC Compliance Manager reviews any CIP content, and the parent policy's approver signs it.
- **Exceptions:** under POL-01 4.9, time-limited and recorded in the risk register. Requirements that carry a NERC obligation cannot be excepted.
- **Testing:** each standard lists what P07 or internal audit checks.

## 3. Standards
| ID | Standard | Parent policy | Owner | Status (2026-09-17) | Target issue date | Key minimum requirements | Main SP 800-53 controls |
|---|---|---|---|---|---|---|---|
| STD-01 | **Configuration and change management standard (IT and OT)** | POL-01, POL-02 | OT Engineering Manager (OT); Director of Information Technology (IT) | Draft in progress | 2027-01-31 | Baselines for SCADA servers, HMIs, jump hosts, gateways, RTUs, routers, and cloud images; vendor defaults changed before commissioning; weekly change board for SCADA, OMS, ADMS, and relay settings with DCC sign-off; security impact review for every OT change; commissioning checklist that verifies access lists and remote paths | CM-2, CM-3, CM-4, CM-6, CM-7 |
| STD-02 | **Vulnerability and patch management standard (IT and OT)** | POL-01 | Information Security Manager | Existing (2025); OT section new | 2026-12-31 | IT: monthly authenticated scans, known-exploited vulnerabilities on edge devices within 48 hours, Critical 15 days, High 30 days. OT: passive vulnerability matching from sensors, quarterly vendor advisory review, patches tested on the standby before the primary, compensating controls recorded when a patch cannot be applied | RA-5, SI-2, SI-5, SA-22 |
| STD-03 | **Vendor and OT supply chain risk standard** | POL-01 | Procurement Manager with the Information Security Manager | Draft in progress (gap 9) | 2026-12-31 | Vendor tiers (Tier 1: OT remote access, customer or client data, or supports a High-criticality process); security terms for every Tier 1 and Tier 2 contract; yearly SOC 2 Type 2 (or equivalent) review for Tier 1 with CUEC mapping; incident notice to the company within 24 hours; no vendor remote equipment at substations; Red Flags duties for service providers on covered accounts; OT purchases from approved suppliers with firmware integrity checks | SA-4, SA-9, SR-2, SR-3, SR-5, SR-6, SR-11 |
| STD-04 | **OT asset inventory and substation onboarding standard** | POL-01, POL-02 | Director of Engineering and Protection with the OT Engineering Manager | Draft in progress (gaps 3, 8) | 2026-12-31 | Inventory of every OT asset with firmware version, owner, and support status; checklist for any substation or protection system the company takes over (rekeying, access lists, contractor laptop review, remote path survey, CIP-002 update) completed before the transfer date | CM-8, RA-2, PE-2 |
| STD-05 | **AI use standard** | POL-01, POL-05 | Director of Power Supply and Rates (AI review group chair) with the vCISO | Draft in progress (gap 13) | 2026-12-31 | AI inventory; risk tiering per P10; security and privacy review before use; vendor terms prohibiting training on company data; human review of outputs; model validation, drift monitoring, and change control for in-house models; fairness testing for models that affect customers | PM-9, SA-9, PL-4, RA-3, CM-3 |
| STD-06 | **Authenticator and privileged access standard** | POL-02 | Director of Information Technology with the OT Engineering Manager | Existing (2025); OT update due | 2026-12-31 | 14-character minimum and banned list; MFA for all remote and SaaS access; FIDO2 for administrators and vendor jump host users; PAM check-out for IT, cloud, SaaS, and OT administrator accounts; device passwords unique per site and vaulted; break-glass accounts tested quarterly | IA-2, IA-5, AC-6(2), AC-6(5) |
| STD-07 | **OT network and remote access standard** | POL-02 | OT Engineering Manager | Draft in progress (gaps 2, 4) | 2026-11-30 | Zones and conduits model (corporate, OT DMZ, DCC control zone, substation zones); no direct IT-to-OT rules; quarterly IT/OT rule review with OT sign-off; vendor access only through the jump hosts with DCC enablement; no modems or cellular routers at substations without approval; yearly survey of substations for unmanaged paths | SC-7, AC-4, AC-17, MA-4 |
| STD-08 | **Logging and monitoring standard** | POL-03 | Information Security Manager | Existing (2025); OT update due (gap 6) | 2027-03-31 | Required event types per system class; jump host, gateway, and router logs to the SIEM; OT sensors at the DCC, backup DCC, OT DMZ, and the 20 largest substations; MSSP high-severity escalation within 30 minutes; 1 year searchable, 3 years archived | AU-2, AU-6, AU-11, AU-12, SI-4 |
| STD-09 | **Contingency and recovery standard** | POL-03, POL-04 | OT Engineering Manager (OT); Director of Information Technology (IT) | Draft in progress (gap 7) | 2026-12-31 | Recovery objectives from the BIA (P05); quarterly SCADA restore drill; yearly backup DCC failover before hurricane season; quarterly OMS restore test; offline, hash-verified copies of relay settings; manual operations state defined | CP-2, CP-4, CP-7, CP-9, CP-10, CP-12 |
| STD-10 | **Encryption and key management standard** | POL-04 | Director of Information Technology | Existing (2025); minor update | 2027-03-31 | TLS 1.2 or higher; encryption at rest for all Restricted data in IT, cloud, and SaaS; customer-managed keys for cloud workloads; separate backup keys; tokenization of bank account numbers outside the CIS | SC-8, SC-12, SC-13, SC-28 |
| STD-11 | **Data retention and disposal standard** | POL-04 | Vice President of Customer Operations with the records manager | Draft in progress (gap 12) | 2026-12-31 | Retention periods for customer, credit, client, and operational records; SSN and driver license purge 2 years after final bill and debt resolution; CIS extracts kept no more than 35 days; locked shred bins at all 5 sites; erasure of relays and gateways leaving service | SI-12, MP-6 |

**Summary:** 11 standards. 7 are new drafts (STD-01, STD-03, STD-04, STD-05, STD-07, STD-09, STD-11), and 4 exist from 2025 and need updates (STD-02, STD-06, STD-08, STD-10).

## 4. Issue schedule
| Quarter | Standards |
|---|---|
| 2026 Q4 | STD-02 Vulnerability and patch (OT section); STD-03 Vendor and OT supply chain; STD-04 OT asset inventory and substation onboarding; STD-05 AI use; STD-06 Authenticator and privileged access; STD-07 OT network and remote access; STD-09 Contingency and recovery; STD-11 Data retention and disposal |
| 2027 Q1 | STD-01 Configuration and change management; STD-08 Logging and monitoring; STD-10 Encryption and key management |

## 5. Related documents
POL-01 to POL-05; `policy-control-map.csv`; CIP low impact cyber security plan; Identity Theft Prevention Program; P03 roadmap; P07 POA&M; P10 AI governance process
