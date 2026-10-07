# Division Supplements to Group Security Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. |
| Authority | POL-01 section 4.5: a supplement may add stricter or division-specific requirements, never weaker ones; it must be re-aligned within 90 days after a group policy changes and attested every year |
| Owner | Each division security lead; alignment reviewed by the Group CISO |
| Status date | 2026-09-17 (group policies v2026 approved; effective 2026-10-01) |

## 1. How group policy and supplements fit together
| Layer | Examples | Who approves |
|---|---|---|
| Group policy (POL-01 to POL-05) | MFA for all workforce, one severity scale, intercompany service rules, regulated environment boundaries | Board risk committee or Group CISO |
| Group standards | Logging standard, landing-zone guardrails, vulnerability standard, Group AI Standard (P10) | Group CISO |
| **Division supplement** | Regulator-specific and system-specific standards (FedRAMP for G1, DFARS and CMMC for the CUI enclave, PCI DSS and 16 CFR Part 314 for the CDE) | Division president, after Group CISO alignment review |
| Division procedures | Runbooks and work instructions | Division security lead |

## 2. Supplement status
| Division | Supplement version | Last aligned to group policy | Status | Action |
|---|---|---|---|---|
| Cloud Hosting | v2026 | 2026-06-30 (to the 2026 draft group policies) | Aligned; minor update for the final 2026 policies due by 2026-12-30 | Confirm alignment; add the FedRAMP 2026 rules as each ruleset is adopted |
| Managed IT | v2024 | 2024-05 | **Drifted** (scenario gap 8); conflicts in section 4 | Re-issue by 2026-11-30 (POAM-016) |
| Payment Processing | v2026 | 2026-04 (after the PCI DSS assessment) | Aligned, but missing the intercompany service rules in POL-01 4.8 | Add affiliate oversight by 2026-12-31 (POAM-018) |

## 3. What each supplement adds
### 3.1 Cloud Hosting supplement (cloud provider; FedRAMP certified G1; bank service provider; HIPAA business associate)
| Topic | Division requirement | Group policy it builds on | Driver |
|---|---|---|---|
| FedRAMP 2026 rules | Each Rev5 ruleset adopted by its maintain date; the Government Cloud compliance director reports status monthly to the division president | POL-01 4.10 | C-IT-R01 (Consolidated Rules for 2026) |
| PAIN rating and IEC reports | Every SOC case touching G1 records a FedRAMP reportability evaluation; a federal incident response coordinator is on call 24x7 with a second person overnight; Initial Incident Reports within 1 hour for PAIN-3 to PAIN-5 | POL-03 4.3, 4.4 | IEC-CSO-EFR; IEC-CSO-IIR |
| Partner-operator access | Granted per managed-hosting tenant with the tenant's consent; through SYS-G1 PAM; 1-hour device-bound sessions; run-command volume alert | POL-02 4.2, 4.4, 4.5 | Customer agreements; 45 CFR 164.312(d) for BAA customers |
| Customer data access by support | Only through case-linked, customer-approved support tooling | POL-05 4.1 | Customer agreements; SOC 2 commitments |
| G1 boundary | No commercial identities, tooling, or data flows into G1 except the documented security log path; shared group services documented in the FedRAMP scope | POL-01 4.14; POL-04 4.3 | MAS-CSO-IIR; MAS-CSO-TPR |
| Significant changes | Every change record has a FedRAMP significant change field; transformative changes notified 30 business days ahead | POL-01 4.10 | SCN-CSO-EVA; SCN-TRF-NIP |
| DIB customers in G1 | DFARS incident steps (DIBNet report, 90-day image preservation, malware submission) in the G1 runbook | POL-03 4.9 | 48 CFR 252.204-7012(b)(2)(ii)(D), (c) to (g) |
| Bank customers | Designated contact register for every bank customer, verified quarterly | POL-03 4.4 | 12 CFR 53.4 |

### 3.2 Managed IT supplement (DoD subcontractor; ESP to DIB clients; HIPAA business associate; bank service provider)
| Topic | Division requirement | Group policy it builds on | Driver |
|---|---|---|---|
| RMM technician accounts | Named accounts in SYS-G1 with hardware keys; console access only from approved locations; two-person approval for multi-client or regulated-environment jobs | POL-02 4.3, 4.9 | NIST SP 800-171 Rev. 2, 3.1.15 and 3.4.5 |
| RMM reach | No RMM agents on systems in G1, the CDE, the CDE connected-to segment, or the CUI enclave unless the environment owner approves and the agent is in the documented scope | POL-01 4.14 | PCI DSS 12.5.2.1; 32 CFR 170.19(c) |
| RMM logs | Forwarded to the SIEM; 1 year searchable | Logging standard | NIST SP 800-171 Rev. 2, 3.3.1; 45 CFR 164.312(b) |
| CUI enclave | Enclave SSP kept current (3.12.4); monthly scans; CUI training for administrators; DIBNet reporting with two certificate holders | POL-03 4.4, 4.9 | 48 CFR 252.204-7012; 32 CFR 170.21 |
| ESP duties to DIB clients | Responsibility matrix and evidence package for each DIB client; notice to clients within 24 hours of discovery affecting their systems | POL-01 4.8 | 32 CFR 170.19(c)(2) |
| Client credentials | Only in the client privileged access broker; secret scanning of tickets and notes | POL-02 4.11 | 45 CFR 164.312(a); 16 CFR 314.4(c)(1) for financial clients |
| AI runbook automation | Executions need technician approval until the agent passes evaluation (P10) | POL-01 4.13 | Client agreements |

### 3.3 Payment Processing supplement (financial institution under 16 CFR Part 314; PCI DSS service provider)
| Topic | Division requirement | Group policy it builds on | Driver |
|---|---|---|---|
| Qualified Individual | Division CISO designated; annual written report to the board | POL-01 4.2 | 16 CFR 314.4(a), (i) |
| Affiliate oversight | Cloud Hosting and Managed IT managed as service providers: intercompany agreements, responsibility matrix, annual assessment | POL-01 4.8 | 16 CFR 314.4(f); PCI DSS 12.8 |
| Scope confirmation | PCI DSS scope confirmed every six months and after changes, including tooling that manages connected-to systems | POL-01 4.14 | PCI DSS 12.5.2.1 |
| Notices | Sponsor banks within 24 hours of a determination; card network reporting through the sponsor bank; FTC within 30 days for 500 or more consumers; state licensing notices | POL-03 4.4 | Sponsor bank agreements; 16 CFR 314.4(j) |
| Automated containment | No AI triage containment in the CDE without analyst approval | POL-03 4.11 | PCI DSS 10 and 12.10 |
| Merchant identities | MFA for merchant users by 2027-01-31; deposit account changes held 3 days with out-of-band confirmation | POL-02 4.10 | 16 CFR 314.4(c)(5) |

## 4. Managed IT drift: conflicts with 2026 group policy
The 2024 Managed IT standards were written before the 2026 group policies and before the division's partner-operator role grew to about 1,900 engineers. Where they conflict, **group policy governs now** (POL-01 4.5), but technicians follow the document they know, so the conflicts are real risks (P01 MS-011; P07 PL-01a.01(b)).

| Topic | Managed IT standard (2024) | Group policy (2026) | Effect |
|---|---|---|---|
| Technician MFA | Push MFA from the legacy identity tenant | Phishing-resistant for all privileged access by 2026-12-31 (POL-02 4.3) | Phishing path into the RMM and the HCP (P01 GR-01, MS-002) |
| Session length | 12 hours | 1 hour for privileged and partner-operator sessions (POL-02 4.5) | Stolen tokens stay useful all day |
| Script approval | One approver for any script | Two-person approval for multi-client or regulated-environment jobs (POL-02 4.9) | One phished or careless technician can reach many clients (GR-02) |
| RMM log retention | Vendor default (90 days) | Logging standard: 1 year searchable (POL-03 4.9 for incidents) | Investigations limited to 90 days (POAM-015) |
| Termination | Next business day in the legacy tenant | Within 4 hours (POL-02 4.6) | Longer exposure window |
| Agents on other divisions' systems | Not addressed | Prohibited in regulated environments without owner approval (POL-01 4.14) | Agents on CDE connected-to and enclave servers (gap 2) |
| AI use | Not addressed | Registration and approval (POL-01 4.13) | AI runbook automation went live without review (P10 AI-005) |
| Common control inheritance | Not addressed | Division must document inheritance (POL-01 4.6) | Gap 9 (POAM-017) |

**Why the drift happened.** Managed IT kept its own identity tenant and standards after the 2022 group consolidation, and the supplement had no owner after a 2025 reorganization. **Fix:** the Managed IT division security and compliance lead owns the supplement, the Group CISO's policy office tracks versions in the policy register, and POL-01 4.5 requires re-alignment within 90 days of any group change and an annual attestation.

## 5. Attestation
Each division security lead signs an annual statement: "The division supplement does not weaken any group policy and reflects all group policy changes made in the last 12 months." The first attestations are due 2026-12-31 (Cloud Hosting, Payment Processing) and on re-issue (Managed IT).
