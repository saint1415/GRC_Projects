# Scenario facts: Cris Santos Company | Health Care | Multi-Sector

All 10 deliverables in this folder use the facts below. The company is fictitious. This scenario is independent of the other sizes.

## 1. The organization
| Item | Fact |
|---|---|
| Legal name | Cris Santos Company Holdings, Inc. (publicly traded SEC registrant) |
| Structure | A holding company with three divisions and corporate shared services |
| Division 1: Care Delivery (NAICS 621111), **focus of this scenario** | Multi-specialty medical group, ASCs, imaging, and lab. About 20,000 employees. A HIPAA covered entity |
| Division 2: Health Plan (NAICS 524114, sector 52 Finance and Insurance) | Medicare Advantage and commercial health plans; about 900,000 members. About 14,000 employees. A HIPAA covered entity (health plan). State insurance regulation applies in each state of operation (handled generically) |
| Division 3: Health-Tech SaaS (NAICS 513210, sector 51 Information) | Care-coordination SaaS sold to external hospitals and practices nationwide. About 6,000 employees. A **business associate** of its customers; issues SOC 2 Type 2 reports |
| Corporate shared services | Identity, network, security operations, data platform, HR, finance, legal. About 5,000 employees |
| Location | Headquartered in Florida. Care Delivery and the Health Plan in 6 southeastern states; the SaaS serves customers nationwide. **State law handled generically**, with Florida as the worked example |
| Workforce / revenue | 45,000 employees; about $18 billion revenue (fictional) |
| Affiliation | The Care Delivery division and the Health Plan share some PHI for treatment, payment, and health care operations. Minimum necessary rules apply; confirm the affiliated covered entity designation in P03 |

## 2. People (role titles only)
| Role | Duties |
|---|---|
| Board risk committee | Group cyber oversight |
| Group CISO; Group Chief Risk Officer; Group Chief Privacy Officer | Group standards and group risk register |
| Division security and compliance leads (3) | Division registers, division-specific regulators |
| Division HIPAA Security and Privacy Officers | Each covered entity (Care Delivery, Health Plan) designates its own |
| Group internal audit | Assesses common controls once; samples division controls |
| Disclosure committee | SEC materiality |

## 3. Systems
| ID | System | Owner |
|---|---|---|
| SYS-G1 | Group identity platform (SSO, MFA, PAM, identity governance) | Corporate |
| SYS-G2 | Group SOC, SIEM, and EDR | Corporate |
| SYS-G3 | Group cloud platform (two providers, vendor-agnostic) and data platform | Corporate |
| SYS-D1 | Care Delivery EHR/PM, LIS, PACS | Care Delivery |
| SYS-D2 | Claims, enrollment, and utilization management platforms (including an AI utilization-management model) | Health Plan |
| SYS-D3 | Care-coordination SaaS (multi-tenant) | Health-Tech SaaS |

**SSP system (P02):** the *Group Data Platform* (shared corporate system). It holds PHI from both covered-entity divisions and de-identified data for SaaS analytics, and inherits common controls from SYS-G1 to SYS-G3.

## 4. Current security posture: mostly compliant, with group-level gaps
**In place today:**
- Group policies aligned to CSF 2.0
- A common control catalog
- 24x7 group SOC
- PAM
- Quarterly access certification
- Immutable backups
- SaaS SOC 2 Type 2 reports issued annually
- SEC Item 106 disclosure

**Gaps:**
1. **Data segregation.** The Group Data Platform mixes Health Plan and Care Delivery PHI with inconsistent purpose-based access. Minimum-necessary enforcement between divisions is not verified.
2. **Division supplements.** Division policy supplements have drifted from group policy. The Health Plan's standards were last aligned in 2024.
3. **Utilization-management AI.** The Health Plan's AI utilization-management model must support, not replace, individualized medical necessity determinations (42 CFR 422.101(c)(1)(i)). Documentation of clinician review is incomplete.
4. **SaaS product AI.** The SaaS division launched a generative AI summarization feature for customers without updating its SOC 2 system description or customer BAAs.
5. **Shared incident notification.** A shared-service incident may trigger notices from two covered entities, SaaS customer notices under BAAs, SEC disclosure, and state insurance regulators. The single notification matrix is not yet exercised.
6. **Common control inheritance.** It is documented for Care Delivery but not for the Health Plan.

## 5. Scenario choices
| Deliverable | Choice |
|---|---|
| P08 | An incident in the Group Data Platform affecting all three divisions: a multi-regulator notification matrix and SEC materiality |
| P09 | SOC 2 Type 2 readiness scoped per division: the SaaS is in scope as a true service organization; Care Delivery's patient-app platform is in scope; the Health Plan is out of scope, with reasons |
| P10 | Group AI governance program: group standards, division use cases, and the regulator-specific rules (MA utilization management, Section 1557, SaaS customer commitments) |
| Cloud | Shared corporate platform plus division workloads, vendor-agnostic |

## 6. Assessment calendar (fictional)
| Date | Event |
|---|---|
| 2026-05-01 to 2026-07-31 | Group and division risk analyses |
| 2026-07-01 to 2026-08-31 | Common control assessment (group internal audit) plus division samples |
| 2026-09-10 | Results to the board risk committee |

## 7. Facts added while building the deliverables (Phase 2)
These facts were added so the deliverables could be completed. They do not change sections 1 to 6.

| Topic | Added fact |
|---|---|
| Legal entities | Care Delivery and the Health Plan are legally separate subsidiaries under common ownership. They have **not** designated themselves an affiliated covered entity (45 CFR 164.105(b)); each is a separate covered entity. Corporate shared services sits in the parent holding company and acts as a business associate of both covered entities under intercompany BAAs (Care Delivery BAA signed 2024; Health Plan BAA signed 2019, before the Group Data Platform existed) |
| Care Delivery scale | About 2.1 million active patients; 160 clinic sites, 14 ambulatory surgery centers (ASCs), 22 imaging centers, and 2 regional laboratories in 6 southeastern states. Accepts Medicare and Medicaid (Section 1557 applies). 14 practices acquired in 2025 still run a legacy EHR, due to migrate to SYS-D1 by 2027-06-30 |
| SYS-D4 | Care Delivery **patient-app platform**: patient mobile app and web portal back end (scheduling, messaging, results, bill pay), hosted on SYS-G3. Also offered as a white-label service to 38 independent practices in the group's clinically integrated network; for them Care Delivery is a business associate, and they have asked for a SOC 2 Type 2 report by the end of 2027 |
| Care Delivery AI | AI scribe (ambient documentation) used by about 400 providers since 2025; EHR-embedded predictive decision support (sepsis and readmission risk scores) |
| Health Plan scale | About 540,000 Medicare Advantage members and 360,000 commercial members. Licensed as an HMO and insurer in the same 6 states; **not licensed in New York**. About 210,000 people are both Care Delivery patients and Health Plan members |
| Health Plan UM model | The in-house AI utilization-management model (on SYS-D2, trained on the Group Data Platform) scores prior authorization requests. It auto-approves requests that meet coverage criteria (about 38% of volume) and routes all others to nurse reviewers with a recommendation. It never issues denials; potential adverse medical necessity decisions go to a physician reviewer. The model has not been presented to the Utilization Management committee |
| Health-Tech SaaS scale | About 420 customer organizations (hospitals, health systems, and physician practices) nationwide; about 12 million patients' records in the multi-tenant service. SOC 2 Type 2 report (Security, Availability, Confidentiality) issued annually for the 12 months ending September 30. No federal agency customers (FedRAMP not applicable); no child-directed services |
| SaaS AI feature | Generative "care summary assist" launched 2026-04-15 for opt-in customers (61 customers as of 2026-08-31). It sends patient documents to a hosted large language model service from a third-party model provider under a subcontractor BAA (signed 2026-03) with zero-data-retention terms |
| SaaS BAA terms | The standard SaaS BAA (2024 version) requires notice to the customer of a breach of unsecured PHI within 10 calendar days of discovery and of other security incidents within 5 business days. 42 customers negotiated 72-hour breach notice. 97 customer BAAs signed before 2022 do not expressly permit de-identification for product analytics |
| Group Data Platform content | Care Delivery PHI (clinical and billing data for about 2.1 million patients), Health Plan PHI (claims, enrollment, and UM data for about 900,000 members), and de-identified SaaS analytics data sets (expert determination method, 45 CFR 164.514(b)(1)) |
| Cloud | Provider A (primary) hosts the corporate landing zone, the Group Data Platform, and Care Delivery and Health Plan cloud workloads. Provider B hosts SaaS production and the Group Data Platform disaster recovery replica and backup vault. SYS-D1 EHR is hosted by the EHR vendor. The Health Plan claims core (SYS-D2) runs in a group colocation data center |
| Out of scope by fact | No division operates a federally assisted substance use disorder program (42 CFR Part 2 program). No division holds a bank charter or a New York insurance license |
| Risk acceptance | Low: division security and compliance lead. Moderate: division president. High: Group Chief Risk Officer with the Group CISO, reported to the board risk committee. Very High: board risk committee only |
