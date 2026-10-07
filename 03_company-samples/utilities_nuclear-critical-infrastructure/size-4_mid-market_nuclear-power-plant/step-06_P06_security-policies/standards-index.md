# Security Standards Index

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Owner | IT Security Manager (index); each standard has its own owner below |
| Approved by | Site Vice President, 2026-09-17 (index and issue schedule) |
| Authority | POL-01 statements 4.1 and 4.8; each standard sits under the parent policy named below |
| Review cycle | Each standard is reviewed at least annually by its owner |

## 1. Why this index exists
The 2022 policies stated intent but had few measurable rules for configuration, logging, vendors, or the hand-off between IT and the CST. The gap analysis (P03) traced most findings to that seam, and the risk register (P01) to standing privileged access, missing logs, and untested recovery. Policies say **what** must happen. Standards set the **measurable minimums**: settings, frequencies, and thresholds. Procedures sit under the standards and are owned by the teams that run them.

**How standards relate to the CSP.** The CSP and its implementing procedures govern CDAs. These standards govern the business network and the cloud. Where a standard touches the CSP boundary (STD-04, STD-09, STD-10), the Cyber Security Program Manager co-signs it, and the CSP wins any conflict.

## 2. How standards work
- **Hierarchy:** policy (POL) to standard (STD) to procedure or runbook. A standard may not weaken its parent policy.
- **Approval:** the owner drafts it, the IT Security Manager reviews it for consistency, the Cyber Security Program Manager co-signs anything that touches the CSP boundary, and the parent policy's approver signs it.
- **Exceptions:** under POL-01 4.8, time-limited and recorded in the risk register; never for a known regulatory noncompliance.
- **Testing:** each standard lists what P07 or internal audit checks.

## 3. Standards
| ID | Standard | Parent policy | Owner | Status (2026-09-17) | Target issue date | Key minimum requirements | Main SP 800-53 controls |
|---|---|---|---|---|---|---|---|
| STD-01 | **Configuration standard** | POL-01 | IT Security Manager | Draft in progress | 2027-03-31 | Benchmark-based baselines for workstations, servers, cloud virtual machines, network devices, server management interfaces, and SaaS tenants; no default passwords on any device; monthly benchmark scans with a 90% target; change advisory board for infrastructure, WMS, and GDSR changes with a second reviewer | CM-2, CM-3, CM-6, CM-7 |
| STD-02 | **Logging and monitoring standard** | POL-03 | IT Security Manager | Draft in progress (gap 6) | 2026-12-31 | Required log sources include WMS, EDMS, CAP, the receive server, GDSR, and database audit logs; SIEM use cases for attempts to reach boundary addresses, vendor sessions, and egress volume; MSSP high-severity escalation within 30 minutes with the CST on the call list for boundary events; 1 year searchable; CSP-supporting evidence exported for license-life retention | AU-2, AU-6, AU-11, AU-12, SI-4 |
| STD-03 | **Vendor risk management standard** | POL-01 | Compliance and GRC Lead | Draft in progress (gap 8) | 2026-12-31 | Vendor tiers (Tier 1: network access, Restricted data, or support for a High BIA process; Tier 2: Confidential data, no network access; Tier 3: neither); Tier 1 annual SOC 2 Type 2 or equivalent review with CUEC mapping; security addendum (named accounts, MFA, 72-hour incident notice, 10-day personal information breach notice); CDA suppliers stay under the CSP supply chain procedure | SA-9, SR-6, RA-3(1), SA-4 |
| STD-04 | **CSP interface and change screening standard** | POL-01 | Cyber Security Program Manager with the IT Director | Draft in progress (gap 3) | 2026-11-30 | Every IT change ticket and IT purchase answers: does it receive Level 3 data, support an EP function, connect to plant equipment, or add a vendor path near CDAs? Any yes routes to the CST for a 73.54(b)(1) and (d)(3) evaluation and to the 73.58 screening before approval; quarterly CST review of all IT changes; CAP entry for any change found unevaluated | CM-3, CM-4, SA-9, CA-3 |
| STD-05 | **AI use standard** | POL-01, POL-05 | vCISO with the Maintenance Manager and the HR Director | Draft in progress (gap 11) | 2026-12-31 | AI inventory and approved-tools list; risk tiering per P10; security, CSP (STD-04), and data review before use; no AI connection to CDAs and no automatic actions on plant equipment; no SGI or Restricted data in AI tools; human decision for every maintenance and employment action; bias testing for employment uses; monitoring and decommissioning criteria | PM-9, SA-9, PL-4, RA-3 |
| STD-06 | Authenticator and privileged access standard | POL-02 | IT Security Manager | Existing (2022); update due | 2027-01-31 | 14-character minimum and banned list; MFA for all including site console logons; FIDO2 for administrators; no standing domain administrators; just-in-time elevation; vaulted service account passwords rotated annually; break-glass accounts tested quarterly | IA-2, IA-5, AC-6(2), AC-6(5) |
| STD-07 | Contingency and recovery standard | POL-03, POL-04 | IT Director | Draft in progress (gap 5) | 2026-12-31 | Recovery objectives from the BIA (P05); WMS and CAP/EDMS failover tested at least annually and before each refueling outage; 15-minute log shipping for the clearance database; paper CAP intake procedure for 73.77(b); quarterly restore tests per application | CP-2, CP-4, CP-9, CP-10 |
| STD-08 | Encryption and key management standard | POL-04 | IT Director | Existing (2022); minor update | 2027-03-31 | TLS 1.2 or higher; FIPS-validated modules where available; encryption at rest for Restricted and Confidential data; company-managed cloud keys; separate recovery account keys | SC-8, SC-12, SC-13, SC-28 |
| STD-09 | Portable media and transient devices standard | POL-04, POL-05 | Cyber Security Program Manager with the IT Security Manager | Existing (2023); update for business devices | 2027-02-15 | Every portable device is assigned to one security level and labeled; Level 2 devices never used at Level 3 or 4; PMMD kiosk scan before any CDA use; CIP-003-9 Section 5 evidence (kiosk log) for every transient cyber asset connected to the dispatch network; outage contractor briefing | MP-7, AC-19, SI-3 |
| STD-10 | Security-Related Information handling standard | POL-04 | Director of Security | Draft in progress (gap 9) | 2027-01-31 | What counts as SRI; marking; EDMS restricted folders only; sensitivity labels with DLP blocking external sharing; quarterly search of general shares; quarterly restricted-folder review; never in the cloud workloads account or AI tools; SGI stays under the SGI program procedures | AC-3, MP-2, SI-4 |

**Summary:** 10 standards. Seven are new and in draft (STD-01, STD-02, STD-03, STD-04, STD-05, STD-07, STD-10). STD-06, STD-08, and STD-09 exist and need updates. STD-04 is the most important new standard: it closes the IT-to-CSP change seam behind 3 of the 9 High gaps in P03 (G-005, G-008, G-017) and the Moderate gaps G-006, G-042, and G-067.

## 4. Issue schedule
| Quarter | Standards |
|---|---|
| 2026 Q4 | STD-04 CSP interface and change screening (2026-11-30); STD-02 Logging and monitoring; STD-03 Vendor risk; STD-05 AI use; STD-07 Contingency and recovery |
| 2027 Q1 | STD-06 Authenticator and privileged access; STD-10 SRI handling; STD-09 Portable media (before the 2027-03-08 outage); STD-01 Configuration; STD-08 Encryption |

## 5. Related documents
POL-01 to POL-05; `policy-control-map.csv`; P03 roadmap; P07 POA&M; P10 AI governance process; the CSP and its implementing procedures (SRI)
