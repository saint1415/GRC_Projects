# Security Standards Index

| Field | Value |
|---|---|
| Organization | Cris Santos Bank, N.A. |
| Owner | IT Risk and Compliance Manager (index); each standard has its own owner below |
| Approved by | Board Risk Committee, 2026-09-15 (index and issue schedule) |
| Authority | POL-01 statements 4.1 and 4.6; each standard sits under the parent policy named below |
| Review cycle | Each standard is reviewed at least annually by its owner |

## 1. Why this index exists
The 2024 policies stated intent, but staff, IT, and vendors had few measurable rules for configuration, logging, cryptography, vendor tiering, payments configuration, or AI (gap 11 in `../00_company-facts.md`; P03 II.A; P01 R-038). Policies say **what** must happen. Standards set the **measurable minimums**: settings, frequencies, and thresholds. Procedures (how-to steps) sit under the standards and are owned by the teams that run them.

## 2. How standards work
- **Hierarchy:** policy (POL) → standard (STD) → procedure or runbook. A standard may not weaken its parent policy.
- **Approval:** the owner drafts the standard, the IT Risk and Compliance Manager checks it for consistency, the ISO reviews it, and the parent policy's owner signs it. Standards that change customer-facing controls (STD-04) are also approved by the COO.
- **Exceptions:** under POL-01 section 4.7, time-limited and recorded in the risk register.
- **Testing:** each standard lists what P07 or internal audit checks.

## 3. Standards
| ID | Standard | Parent policy | Owner | Status (2026-09-15) | Target issue date | Key minimum requirements | Main SP 800-53 controls |
|---|---|---|---|---|---|---|---|
| STD-01 | **Configuration standard** | POL-01, POL-04 | Chief Information Officer | Draft in progress (gap 11) | 2027-03-31 | Benchmark-based baselines for workstations, servers, cloud images, network devices, and SaaS tenants; deviations approved and recorded; monthly drift report; cloud guardrail set reviewed quarterly | CM-2, CM-6, CM-7 |
| STD-02 | **Logging and monitoring standard** | POL-03 | Information Security Officer | Draft in progress (gap 7) | 2027-01-31 | Required event types per system class, including beneficiary, template, limit, and contact-information changes; all COBP components send logs to the SIEM (payments hub, correspondent portal, core security reports); 1 year searchable and 3 years archived; MSSP high-severity call within 30 minutes; monthly core security report review | AU-2, AU-6, AU-11, AU-12, SI-4 |
| STD-03 | **Third-party risk management standard** | POL-01 | Third-Party Risk Manager | Draft in progress (gap 5) | 2026-12-31 | Tiers (Tier 1: customer information at scale, a critical service, or a bank service provider; Tier 2: limited data; Tier 3: no data or access); Tier 1 annual SOC review with CUEC mapping, exception follow-up, and bridge letter; incident notice within a stated time frame (target 24 hours for Tier 1); 53.4 contact for every bank service provider; exit and data return terms | SA-4, SA-9, SR-6, RA-3(1) |
| STD-04 | **Payments and account maintenance security standard** | POL-02, POL-05 | Director of Payments Operations with the Retail Banking Director and Treasury Management Director | Draft in progress (gaps 2 and 3) | 2026-12-31 | Callback to the number on file for every non-face-to-face wire request; out-of-band verification of every contact-information change with alerts to old and new contacts; 10-day second verification after a change; out-of-band confirmation of new online banking beneficiaries; payments hub configuration baseline (limits, approval rules, callback fields) with dual approval for changes; monthly sampling of callbacks and contact changes | AC-5, CM-3, IA-8, IA-12, SI-10 |
| STD-05 | **AI and model use standard** | POL-01, POL-05 | Model Risk Manager with the ISO and the Chief Compliance Officer | Draft in progress (gap 9) | 2026-12-31 | AI inventory; risk tiering per P10; validation on bank data before production for High tier; fair lending testing for any credit use; adverse action reason review; approved-tools list; contract terms (no secondary use of bank data, notice of model changes); monitoring and decommissioning criteria | PM-9, SA-9, RA-3, PL-4 |
| STD-06 | Cryptography and key management standard | POL-04 | Chief Information Officer | Draft in progress (gap 11) | 2027-03-31 | Approved algorithms and protocols (TLS 1.2 or higher); encryption at rest for all Restricted data; customer-managed keys in cloud accounts; separate backup keys; annual key rotation | SC-8, SC-12, SC-13, SC-28 |
| STD-07 | Authenticator and privileged access standard | POL-02 | Chief Information Officer | Existing (2024); update due | 2027-03-31 | 14-character minimum and banned list; MFA for all; hardware keys for administrators; PAM for all privileged accounts including the core security module and payments hub; break-glass accounts tested quarterly; vendor access through PAM with recording; customer authenticator options (app push, passkeys) | IA-2, IA-5, IA-8, AC-6(5), MA-4 |
| STD-08 | Contingency and recovery standard | POL-03, POL-04 | Chief Operating Officer with the CIO | Draft in progress (gap 6) | 2026-12-31 | Recovery objectives from the BIA (P05); semiannual failover test of the payments hub; annual full relocation exercise to the Georgia site including correspondent processing; full restore of each critical workload twice a year; reconciliation runbook for in-flight wires | CP-2, CP-4, CP-7, CP-9, CP-10 |
| STD-09 | Vulnerability and patch management standard | POL-01 | Infrastructure Manager | Existing (2024); update due | 2026-12-31 | Monthly authenticated scans; weekly review of known-exploited vulnerabilities; critical patches within 14 days for internet-facing systems and 30 days otherwise; unsupported systems isolated and on a replacement plan | RA-5, SI-2, SA-22 |
| STD-10 | Physical security standard | POL-01 | Chief Operating Officer | Existing (2024) | 2027-06-30 | Badge access and cameras for wire rooms, operations center, and server room; quarterly badge review; visitor logs; ATM tamper alerts for off-site machines | PE-2, PE-3 |

**Summary:** 10 standards. The 5 new standards requested in the gap analysis (STD-01 to STD-05) and STD-06 and STD-08 are in draft. STD-07, STD-09, and STD-10 exist from 2024; STD-07 and STD-09 need updates.

## 4. Issue schedule
| Quarter | Standards |
|---|---|
| 2026 Q4 | STD-03 Third-party risk; STD-04 Payments and account maintenance; STD-05 AI and model use; STD-08 Contingency and recovery; STD-09 Vulnerability and patch (update) |
| 2027 Q1 | STD-01 Configuration; STD-02 Logging and monitoring; STD-06 Cryptography; STD-07 Authenticator and privileged access (update) |
| 2027 Q2 | STD-10 Physical security (review) |

## 5. Related documents
POL-01 to POL-05; `policy-control-map.csv`; P03 roadmap; P07 POA&M; P10 AI governance process
