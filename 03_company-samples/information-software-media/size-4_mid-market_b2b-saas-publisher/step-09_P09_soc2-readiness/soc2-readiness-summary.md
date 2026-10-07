# SOC 2 Readiness Summary: Cris Santos Company | Information | Mid-Market

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (PE-backed B2B SaaS publisher of a multi-tenant customer service platform) |
| Tier / Vertical | Mid-Market / Information |
| Criteria | AICPA 2017 Trust Services Criteria (With Revised Points of Focus, 2022). Criteria are cited by ID with short topic labels in our own words |
| Categories in scope | Security (CC1 to CC9), Availability (A1), and Confidentiality (C1, new for 2027) |
| Target report | SOC 2 **Type 2** for the calendar year 2027 (examination period 2027-01-01 to 2027-12-31), with the healthcare cell and the AI features added to the system description; report expected by 2028-02-29 |
| Current reports | Type 2 (Security, Availability), 2025-04-01 to 2026-03-31, issued 2026-05-29: unmodified opinion with 4 exceptions. Bridging Type 2 on the same scope, 2026-04-01 to 2026-12-31 (report expected by 2027-02-26) |
| Part A | Readiness checklist, criterion by criterion (`soc2-readiness.csv`) |
| Part B | Sub-processor and critical vendor report reviews (`vendor-soc2-review.csv`) |
| Prepared | 2026-09-08 to 2026-09-18 by the GRC Manager with the Director of Security, using P02, P05, P06, and P07 evidence; approved by the CTO 2026-09-29 |

## 1. Why SOC 2 for this organization
The company is a service organization in the SOC 2 sense: 2,400 businesses run their customer support on its platform, and their auditors and security teams need assurance about controls they cannot see. The MSA promises a current SOC 2 Type 2 report under NDA. The company has issued Type 2 reports for 3 years, so this is not a first audit. The readiness question is about **scope growth**:
- **Confidentiality.** Enterprise customers now ask for it, because the platform holds their customers' messages and attachments.
- **The healthcare cell.** Launched in November 2025 and not in the current system description. Healthcare customers want SOC 2 coverage of the cell alongside their BAAs.
- **The AI features.** AI Assist and Answer Bot send customer content to the AI model provider. Customers ask how that flow is controlled.

**Why a new period, not a change mid-period.** Adding categories and components in the middle of a period would leave part of the period untested for them. The service auditor agreed to a bridging report on the current scope through 2026-12-31 and a calendar-year 2027 period on the expanded scope. That makes **2026-12-15** the date by which new and fixed controls must be operating.

**Alternatives considered (vertical assurance alternatives):**
- **ISO/IEC 27001 certification:** a few customers accept it, but most U.S. customers ask for SOC 2, and a certificate does not report test exceptions. Not pursued now.
- **FedRAMP authorization:** only for cloud services sold to federal agencies. The company has no federal customers (N51-R07 does not apply).
- **HITRUST certification for the healthcare cell:** 3 healthcare customers asked about it. The company will offer the SOC 2 report plus a HIPAA mapping (P03) instead, and revisit HITRUST if more than 10% of healthcare revenue depends on it.

**Service auditor independence.** The SOC 2 examination is performed by an independent CPA firm that is **not** the co-sourced internal audit firm, so the internal audit work in P07 does not create an independence question.

**How this file relates to P03.** P03 tests the FTC's Section 5 expectations, the HIPAA Security Rule for the healthcare cell, and the company's own promises, including those in the SOC 2 system description. This file checks each Trust Services criterion and does not repeat that analysis. Where the same weakness appears in both, both point to the same POA&M item in P07.

## 2. System description (2027 scope)
| Element | In scope |
|---|---|
| Services | The Customer Engagement Platform: ticketing and agent workspace, channels, help center, APIs and integrations, AI Assist and Answer Bot, and the healthcare edition |
| Infrastructure | Production (SYS-01), healthcare cell (SYS-02), DR region (SYS-03), and the landing zone (SYS-04) as described in P02 and P04 |
| Software | Platform services, source hosting and CI/CD (SYS-05), identity provider (SYS-06), admin console (SYS-07), monitoring (SYS-08) |
| People | Platform engineering, engineering, security and GRC, customer support (support view operators), and corporate IT |
| Data | Customer content (Restricted under POL-04), including PHI in the healthcare cell; agent accounts; integration credentials |
| Procedures | POL-01 to POL-05, the 10 standards (P06), the P08 runbooks |
| Subservice organizations (carve-out method) | Cloud provider A, the content delivery and WAF provider, the email delivery service, the SMS provider, the AI model provider, the logging SaaS, and the MDR provider. Their controls are covered by their own SOC 2 reports and the complementary subservice organization controls in the description (Part B) |
| Outside the system | The data warehouse on cloud provider B (internal analytics; to hold only counts from 2026-12-31) and corporate SaaS |

**Principal service commitments to describe:** 99.9% and 99.95% monthly availability; 24- and 48-hour incident notice; 10-business-day BAA notice; 30-day sub-processor notice; deletion within 30 days of termination; no training on customer data; U.S. hosting. The **recovery objective** stated in the current description (4 hours) is not yet proven. Management will state the objective it can demonstrate on 2027-01-01 rather than repeat exception 4 (A1.3).

## 3. Readiness results (Part A)
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1 to CC9, 33 criteria) | 12 | 15 | 6 | 0 |
| Availability (A1, 3 criteria) | 1 | 0 | 2 | 0 |
| Confidentiality (C1, 2 criteria) | 0 | 1 | 1 | 0 |
| Processing Integrity (PI1, 5 criteria) | | | | 5 |
| Privacy (P1 to P8, 18 criteria) | | | | 18 |
| **Total (61 criteria)** | **13** | **16** | **9** | **23** |

**Ready (13):**
- governance and risk: CC1.1, CC1.2, CC1.3, CC1.5, CC2.2, CC3.2, CC5.1;
- monitoring of controls: CC4.1, CC4.2;
- boundary and endpoint: CC6.4, CC6.6, CC6.8;
- capacity: A1.1.

**Not ready (9):**
- CC2.3: inaccurate public statements and questionnaire answers; incomplete customer contacts;
- CC6.1: long-lived cloud keys and one-layer tenant isolation;
- CC6.3: standing administrator roles, broad warehouse access, support view without customer approval;
- CC7.1: vulnerability remediation times and the open SSRF finding;
- CC7.2: no data-level monitoring;
- CC9.2: subcontractor BAAs and pending sub-processor reviews;
- A1.2 and A1.3: backups not write-once and recovery not proven;
- C1.2: terminated tenants' data not disposed.

Each maps to a P07 POA&M item. **Processing Integrity and Privacy are out of scope:** the MSA makes no processing integrity commitments, and as a service provider the company leaves notice, choice, and access for end consumers to its customers under the DPA.

### 3.1 Type 2 exceptions (period ending 2026-03-31): status
| Exception | Criteria | Status at readiness | Fix and date |
|---|---|---|---|
| 1. 3 of 40 terminated employees removed late | CC6.2 | Still occurring (2 of 25 in the P07 sample) | Same-day HR entry and reconciliation, 2026-11-30 (POAM-001) |
| 2. 2 of 25 emergency changes without approval | CC8.1 | Still occurring (2 of 25 in P07) | Two-person break-glass deploy, 2026-11-30 (POAM-009) |
| 3. Missed quarterly access review for the data analytics account | CC6.2, CC6.3 | Not repeated since Q3 2025; calendar now tracked in the GRC tool | Review calendar with escalation, done; standing roles removed 2026-12-31 (POAM-007) |
| 4. DR test did not meet the stated 4-hour objective | A1.3 | Not resolved | Restate the objective or prove it, 2027-02-17 (POAM-010) |

Any exception that repeats in the bridging period (through 2026-12-31) will be reported in that report. The goal is that none repeats in the 2027 period.

### 3.2 Readiness gates (must be operating by 2026-12-15)
| Gate | Criteria | Owner | Due |
|---|---|---|---|
| G1. Inaccurate statements corrected; questionnaire library locked | CC2.3 | General Counsel | 2026-10-15 (statements); 2026-11-30 (library) |
| G2. All long-lived cloud keys deleted; federated credentials only | CC6.1 | VP Platform Engineering | 2026-10-31 |
| G3. Healthcare export stopped; healthcare egress limited to BAA subcontractors | CC6.7, CC9.2, C1.1 | Associate General Counsel, Privacy | 2026-10-31 |
| G4. Data-level logging and bulk-read detections live; simulated download detected on retest | CC7.2 | Director of Security | 2026-12-15 |
| G5. Standing roles removed; customer approval for support view on all plans | CC6.3 | VP Platform Engineering; VP Customer Support | 2026-12-15 |
| G6. Deploys blocked for aged critical findings; SSRF fixed | CC7.1 | VP Engineering | 2026-12-15 |
| G7. Write-once backups; DR plan approved with emergency mode procedures | A1.2, CC7.5 | VP Platform Engineering | 2026-12-15 |
| G8. Tenant deletion covers all stores; 61 tenants purged | C1.2, CC6.5 | VP Engineering | 2026-11-30 |
| G9. Updated system description (healthcare cell, AI features, Confidentiality, demonstrable recovery objective) | CC3.1, A1.3 | Chief Technology Officer | 2026-12-15 |

Row-level tenant isolation (due 2027-03-31) and warm standby (due 2027-06-30) will not be complete on 2027-01-01. Management will describe the controls that do operate (application-layer isolation with cross-tenant tests from 2026-12-15; pilot-light DR with the proven recovery time) and update the description when the new controls go live. This is better than describing controls that do not yet exist, which would turn a readiness gap into a deception risk (P03).

## 4. Evidence calendar for the 2027 period
| Frequency | Evidence | Criteria |
|---|---|---|
| Continuous | Deployment records and approvals; just-in-time session logs; data-event logs and alerts; posture findings; vulnerability ageing | CC6.1, CC6.3, CC7.1, CC7.2, CC8.1 |
| Daily | Backup job results; HR-to-identity reconciliation | A1.2, CC6.2 |
| Monthly | Support view session review; deletion evidence report; patch dashboard; AI evaluation results | CC6.3, C1.2, CC7.1, CC3.4 |
| Quarterly | Access reviews for all systems; statement-to-practice review; audit committee report; restore test; break-glass test | CC6.2, CC2.3, CC1.2, A1.3, CC6.1 |
| Twice a year | Regional failover exercise | A1.3, CC7.5 |
| Annually | Risk assessment; policy review; penetration test; incident response tabletop; sub-processor reviews; training | CC3.2, CC5.3, CC7.1, CC7.4, CC9.2, CC1.4 |

**Status reporting.** The GRC Manager reports readiness weekly to the CTO until 2026-12-15, then monthly. The audit committee sees the gate status at its December meeting.

## 5. Sub-processor and critical vendor reviews (Part B)
The company relies on vendor controls for many inherited controls (P02: 9 Common/Inherited and 32 Hybrid). `vendor-soc2-review.csv` covers the 14 DPA sub-processors plus the identity provider and the source hosting and CI service: 16 rows. It is the core of STD-03.

**Tiering approach:**
| Tier | Criteria | Assurance required | Frequency |
|---|---|---|---|
| **Tier 1** | Customer content at scale, healthcare cell data, or production access | SOC 2 Type 2 plus bridge letter; review of opinion, scope, carve-outs, exceptions, complementary user entity controls mapped to company controls; BAA where healthcare data is received | Annually |
| **Tier 2** | Limited or incidental customer data | SOC 2 Type 2 where available, or questionnaire | Annually |
| **Tier 3** | Contact data only, no content | Questionnaire | At contract renewal |

**Results:** 9 Tier 1, 6 Tier 2, 1 Tier 3. 13 reviews complete and 3 open (V-08 error-tracking SaaS, V-11 translation API, V-13 customer data export service), all due by 2026-12-31. Of the 14 sub-processors, 9 were current at P07 fieldwork; V-02 and V-05 were completed during readiness, so 11 are now current.

**Key findings:**
1. **Two subcontractors handle healthcare data without a BAA.** The SMS provider (V-05) and the error-tracking SaaS (V-08). Both flows are switched off for the healthcare cell from 2026-10-31 until BAAs are signed (POAM-006).
2. **The AI model provider's standard endpoint retains prompts for 30 days** (V-06). That conflicts with the trust center statement, so all tenants move to the zero-retention endpoint by 2026-11-30 (POAM-015, POAM-019).
3. **Most complementary user entity controls point back to open company gaps.** The cloud provider's report (V-01) relies on the company to manage keys, logging, and backups, which are exactly the areas in POAM-002, POAM-004, and POAM-011. The vendor's controls protect customers only once the company's side is fixed.
4. **The data platform on cloud provider B has no BAA** (V-02), so PHI must not be loaded there. That is why the healthcare export stops (G3).
