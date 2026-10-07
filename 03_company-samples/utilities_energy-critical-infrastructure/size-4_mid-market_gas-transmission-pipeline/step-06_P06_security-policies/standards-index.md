# Security Standards Index

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Owner | GRC lead (index); each standard has its own owner below |
| Approved by | Chief Operating Officer, 2026-09-17 (index and issue schedule) |
| Authority | POL-01 statements 4.1 and 4.6; each standard sits under the parent policy named below |
| Review cycle | Each standard is reviewed at least annually by its owner, and when a TSA directive is renewed with changes |

## 1. Why this index exists
The 2024 policies state intent, and the TSA plans state the measures TSA inspects against, but staff and suppliers need measurable rules between the two: which settings, how often, and by when. The gap analysis (P03) found the measures drift where no standard holds them (for example the password reset mitigations, OT log retention, and supplier paths into OT). Policies say **what** must happen. Standards set the **measurable minimums**. Procedures (how-to steps) sit under the standards and are owned by the teams that run them. Where a standard implements a measure in the TSA-approved Cybersecurity Implementation Plan, the plan cites the standard, and a change to that part of the standard goes through the amendment check in POL-01 4.9.

## 2. How standards work
- **Hierarchy:** policy (POL) to standard (STD) to procedure or runbook. A standard may not weaken its parent policy or a TSA plan measure.
- **Approval:** the owner drafts it, the GRC lead checks consistency with the TSA plans, the Director of Gas Control reviews any OT impact, and the parent policy's approver signs it.
- **Exceptions:** under POL-01 section 4.7, time-limited and recorded in the risk register.
- **Testing:** each standard lists what P07 or the TSA assessment schedule checks.

## 3. Standards
| ID | Standard | Parent policy | Owner | Status (2026-09-17) | Target issue date | Key minimum requirements | Main SP 800-53 controls |
|---|---|---|---|---|---|---|---|
| STD-01 | **Configuration standard (IT and OT)** | POL-01, POL-04 | SCADA and OT Engineering Manager with the IT Director | Existing for control centers (2024); station and PLC baselines missing | 2027-03-31 | Vendor-guide hardening for SCADA servers and HMIs; benchmark baselines for business IT and cloud; PLC logic baselines with hashes for every station; temporary firewall rules expire within 30 days; changes through MOC with point-to-point verification for SCADA; two-person approval | CM-2, CM-3, CM-6, CM-7 |
| STD-02 | **Logging and monitoring standard** | POL-03 | Security Manager | Draft in progress (gap 10) | 2026-12-31 | Required event types per system class; all Critical Cyber Systems send logs to the SIEM; 12 months retention for OT and IT security logs in the write-once archive; OT sensors at all control centers and compressor stations; documented baseline of OT external communications; MSSP escalation within 15 minutes for OT alerts; 24-hour packet capture capability where TSA may request it | AU-2, AU-6, AU-11, AU-12, SI-4 |
| STD-03 | **Supplier risk management standard** | POL-01 | Security Manager with the Supply Chain Manager | Draft in progress (gap 9) | 2026-12-31 | Supplier tiers (Tier 1: OT access, SSI or Restricted data, or a High-criticality BIA process); security addendum before access; annual SOC 2 Type 2 or equivalent review for Tier 1 with CUEC mapping; incident notice within 24 hours; named technicians; data return at exit; TSA measures the supplier performs listed in the contract | SA-4, SA-9, SR-6, SR-8 |
| STD-04 | **OT remote access and field device standard** | POL-02 | OT Security Engineer | Draft in progress (gaps 1, 3, 4) | 2026-12-31 | Remote access only through the gateways with MFA, per-session approval, and recording; no modems or cellular devices in OT except company telemetry gateways in the inventory; defaults changed before connection; field device inventory with firmware; quarterly review of every external connection against the TSA plan list | AC-17, MA-4, CM-8, SC-7(3), IA-5 |
| STD-05 | **AI use standard** | POL-01, POL-05 | Director of Gas Control with the vCISO | Draft in progress (gap 14) | 2026-12-31 | AI inventory; risk tiering per P10; security, safety, and operations review before use; vendor model changes through MOC with revalidation; no AI write-back to OT without a new assessment; approved generative AI tool with no training on company data | PM-9, SA-9, CM-3, RA-3 |
| STD-06 | Authenticator and privileged access standard | POL-02 | OT Security Engineer | Existing (2024); update due | 2026-12-31 | 14-character minimum where supported; OT accounts reset every 12 months, field devices every 24 months, with documented mitigations and timeframes; no more than 4 OT domain administrators; security keys for all gateway users; shared accounts only as POL-02 4.2 allows | IA-2, IA-5, AC-2, AC-6(5) |
| STD-07 | Contingency and recovery standard | POL-03, POL-04 | SCADA and OT Engineering Manager | Draft in progress (gap 8) | 2026-12-31 | Recovery objectives from the BIA (P05); weekly SCADA backups and offline monthly copies at the BCC; PLC logic backups at every station; annual bare-metal rebuild test; annual BCC failover; annual live IT/OT isolation drill | CP-2, CP-4, CP-9, CP-10 |
| STD-08 | Encryption standard | POL-04 | IT Director | Existing (2024); minor update | 2027-03-31 | TLS 1.2 or higher; IPsec for DMZ-to-cloud and MPLS links; encryption at rest for SSI and Restricted data; customer-managed cloud keys; microwave link encryption at the 2027 refresh | SC-8, SC-12, SC-13, SC-28 |
| STD-09 | Vulnerability and patch management standard | POL-01 | SCADA and OT Engineering Manager with the Security Manager | Existing (2024; the TSA patch strategy); update due | 2026-12-31 | CISA KEV entries reviewed weekly; IT Critical within 30 days; OT quarterly windows plus out-of-cycle windows for KEV items; written mitigations and timelines for any OT component that cannot be patched; no active scanning in OT | RA-5, SI-2, SI-5, SA-22 |
| STD-10 | SSI and CEII handling standard | POL-04 | Security Manager with the General Counsel | Existing (2023); update due | 2026-11-30 | Part 1520 marking (including on exports); SSI repository with named access reviewed annually; quarterly file share scan; same-day internal report of any SSI exposure; CEII filing steps under 18 CFR 388.113(d) | MP-2, MP-3, MP-4, MP-6 |

**Summary:** 10 standards. STD-02, STD-03, STD-04, STD-05, and STD-07 are new drafts requested by the gap analysis. STD-01, STD-06, STD-08, STD-09, and STD-10 exist and need updates.

## 4. Issue schedule
| Quarter | Standards |
|---|---|
| 2026 Q4 | STD-02 Logging and monitoring; STD-03 Supplier risk; STD-04 OT remote access and field devices; STD-05 AI use; STD-06; STD-07 Contingency and recovery; STD-09; STD-10 |
| 2027 Q1 | STD-01 Configuration (station and PLC baselines); STD-08 Encryption |

## 5. Related documents
POL-01 to POL-05; `policy-control-map.csv`; P03 roadmap; P07 POA&M; P10 AI governance process; TSA Cybersecurity Implementation Plan (SSI)
