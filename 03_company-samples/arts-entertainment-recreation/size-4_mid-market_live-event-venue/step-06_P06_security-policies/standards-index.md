# Security Standards Index

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Owner | Security Manager (index); each standard has its own owner below |
| Approved by | Chief Operating Officer, 2026-09-15 (index and issue schedule) |
| Authority | POL-01 statements 4.1 and 4.6; each standard sits under the parent policy named below |
| Review cycle | Each standard is reviewed at least annually by its owner |

## 1. Why this index exists
The 2024 policies stated intent but had no supporting standards for configuration, logging, scripts on payment pages, card handling, or service providers (intake policy library and document request, EV-029 and EV-030; P03 rows G-006, G-022, G-045, G-061; P01 R-001, R-005, R-037). A ROC tests measurable rules, not intent. Policies say **what** must happen. Standards set the **measurable minimums**: settings, frequencies, and thresholds. Procedures and runbooks sit under the standards and are owned by the teams that run them.

## 2. How standards work
- **Hierarchy:** policy (POL) to standard (STD) to procedure or runbook. A standard may not weaken its parent policy.
- **Approval:** the standard's owner drafts it, the Security Manager reviews it for consistency, and the parent policy's approver signs it.
- **Exceptions:** under POL-01 section 4.7, time-limited and recorded in the risk register.
- **Targeted risk analyses:** where PCI DSS lets the company choose a frequency, the standard states the frequency and points to the targeted risk analysis that supports it (POL-01 4.3).
- **Testing:** each standard lists what P07, internal audit, or the QSA checks.

## 3. Standards
| ID | Standard | Parent policy | Owner | Status (2026-09-15) | Target issue date | Key minimum requirements | Main SP 800-53 controls |
|---|---|---|---|---|---|---|---|
| STD-01 | **Configuration standard** | POL-01 | IT Director | Draft (EV-029, EV-024) | 2026-12-31 | Benchmark-based baselines for laptops, cloud servers, CMS servers, SD-WAN edges, and VMS servers; vendor defaults changed before connection; one primary function per server; documented deviations; monthly drift report; firewall rule review every 6 months | CM-2, CM-6, CM-7, SC-7 |
| STD-02 | **Logging and monitoring standard** | POL-03 | Security Manager | Draft (EV-027) | 2026-10-30 | Required sources: identity provider, cloud, firewalls, EDR, web edge, ticketing audit log, tag manager publish history, CMS, payment partner portal; 12 months retention with 3 months searchable; use cases for new administrators, bulk exports, script changes, and unusual virtual terminal volume; daily automated review; MSSP escalation within 30 minutes | AU-2, AU-6, AU-11, AU-12, SI-4 |
| STD-03 | **Service provider and vendor risk standard** | POL-01 | Security Manager with the General Counsel | Draft (EV-030, EV-043) | 2026-10-15 | Provider list with PCI DSS responsibility matrix; tiers (Tier 1: card data, payment pages, or more than 10,000 patron records, or a High-criticality BIA process); Tier 1 annual review of the AOC or SOC 2 Type 2 report with bridge letter; breach notice within 72 hours for Tier 1; security terms for agencies; exit and data return terms | SA-9, SR-2, SR-6, RA-3(1) |
| STD-04 | **Payment page and website standard** | POL-01 | Vice President of Marketing and Digital | Draft (EV-068, EV-011) | 2026-10-30 | Script inventory with owner, data collected, justification, and authorization; integrity checks for every script on pages that embed the payment form; two-person tag manager publishing on SSO with MFA; change and tamper detection at least weekly per targeted risk analysis with alerts to the MSSP; secure release review for CMS templates and plug-ins; role-based training for publishers | CM-3, CM-7, CM-8, SI-7, SA-11 |
| STD-05 | **AI use standard** | POL-01, POL-05 | vCISO with the General Counsel | Draft (EV-058) | 2026-12-31 | AI inventory; risk tiering per P10; security, privacy, legal, and accessibility review before use; human review of patron-facing outputs; bias and performance monitoring plan per use case; total-price and accessible seating parity checks for pricing tools; decommissioning criteria | PM-9, SA-4, SA-9, RA-3 |
| STD-06 | Authenticator and privileged access standard | POL-02 | IT Director | Existing (2024); update due | 2026-10-31 | SSO and MFA for all accounts; app-based MFA for approved local accounts; 14-character minimum (12 on local accounts); scoped, vaulted API keys rotated yearly; no more than 6 ticketing administrators; security keys for administrators by 2027-03-31; break-glass accounts sealed and tested quarterly | IA-2, IA-5, AC-6(2), AC-6(5) |
| STD-07 | Contingency and event-day continuity standard | POL-03 | IT Director with the Vice President of Venue Operations | Draft (EV-026, EV-035) | 2026-11-30 | Recovery objectives from the BIA (P05); manual entry procedure at every venue with offline manifest download on each door checklist; drills each season; quarterly restore tests of company workloads; second connection for every venue | CP-2, CP-3, CP-4, CP-9, CP-10 |
| STD-08 | **Card data handling standard** | POL-04, POL-05 | Chief Financial Officer | Draft (EV-069) | 2026-10-30 | Card entry only on validated P2PE devices or provider forms; no card data in CRM, email, chat, files, or paper; quarterly discovery scans; POI device inventory reconciled quarterly and inspected before each event (frequency per targeted risk analysis); card handling training for payment staff | SI-12, MP-6, CM-8, PE-3, AT-3 |
| STD-09 | Vulnerability, patch, and testing standard | POL-01 | Security Manager | Existing (2024); update due | 2026-10-30 | Quarterly authenticated internal scans of all in-scope components; quarterly ASV scans of all public addresses; critical patches within one month (14 days for internet-facing); annual internal, external, and segmentation penetration tests; quarterly wireless checks at venues | RA-5, SI-2, CA-8, SI-5 |

**Summary:** 9 standards. Seven are new and in draft (STD-01, STD-02, STD-03, STD-04, STD-05, STD-07, STD-08). STD-06 and STD-09 exist from 2024 and need updates. Six standards (STD-02, STD-03, STD-04, STD-06, STD-08, STD-09) must be issued before QSA fieldwork starts on 2026-11-02, because the ROC tests them.

## 4. Issue schedule
| Quarter | Standards |
|---|---|
| 2026 Q4, before 2026-11-02 | STD-02 Logging and monitoring; STD-03 Service provider; STD-04 Payment page and website; STD-06 Authenticator; STD-08 Card data handling; STD-09 Vulnerability, patch, and testing |
| 2026 Q4, after QSA fieldwork | STD-01 Configuration; STD-05 AI use; STD-07 Contingency and event-day continuity |

## 5. Related documents
POL-01 to POL-05; `policy-control-map.csv`; P03 roadmap; P07 POA&M; P10 AI governance process
