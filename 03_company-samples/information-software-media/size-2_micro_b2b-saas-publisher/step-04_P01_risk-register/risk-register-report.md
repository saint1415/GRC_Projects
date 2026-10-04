# Risk Register Report: Cris Santos Company | Information | Micro

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (B2B SaaS software publisher, Vendor Compliance Platform) |
| Size tier | Micro (7 employees, about $1.1 million receipts) |
| Vertical | Information |
| Method | NIST SP 800-30 Rev. 1 (Tables G-2 to G-5, H-3, I-2) |
| Also supports | SOC 2 risk assessment criteria (CC3.1 to CC3.4); the "reasonable security" expectation the FTC enforces under Section 5 (15 U.S.C. 45(a)); the "reasonable measures" duty of a third-party agent under Fla. Stat. 501.171(2) |
| Prepared | 2026-08-07 by the CTO (security and compliance lead) with the Operations and Finance Manager and the MSP lead technician |
| Updated | 2026-08-26 (R-025 added from P07 testing); 2026-09-04 (R-015, R-020, R-023 added from the AI and SOC 2 readiness work) |
| Approved | 2026-09-15 by the Chief Executive Officer |

## 1. Scope and risk framing
**Scope.** The whole company and its key vendors: the Vendor Compliance Platform (VCP) defined in the SSP (P02), the laptops that administer it, the contract developer's personal laptop, the sub-processors that receive customer data, the MSP, and the business processes in the BIA (P05). See `../00_company-facts.md` sections 3 and 4.

**What the company protects.** About 41,000 vendor records and 165,000 documents that belong to 45 customers, including about 9,800 W-9s that show an individual's Social Security number. A breach of those documents would trigger the DPA's 72-hour customer notice, Florida's third-party-agent notice, and customers' own notices to individuals in about 21 states. For a company with about $1.1 million in revenue and two anchor customers, losing customer trust is an existential impact, so it is rated Very High.

**Risk tolerance and who can accept risk:**
- Low and Very Low: the CTO may accept.
- Moderate: only the Chief Executive Officer may accept, with a treatment plan or a written reason.
- High and Very High: not accepted. The Chief Executive Officer approves a dated treatment plan instead.

This is the company's first documented risk assessment.

## 2. Method
1. **Identify.** Threat sources and events came from SP 800-30 Appendices D and E, the vertical's critical systems (multi-tenant platforms, identity, CI/CD pipelines), the BIA, the gap analysis (P03), and interviews with the CTO, both engineers, the contract developer, the Customer Success Manager, the Account Executive, the Operations and Finance Manager, and the MSP lead technician (2026-07-27 to 2026-08-07).
2. **Rate likelihood.** The likelihood of initiation (adversarial) or occurrence (non-adversarial) was rated, along with the likelihood that the event causes adverse impact. The two were combined with **Table G-5**.
3. **Rate impact.** Impact was rated with **Table H-3** using the BIA impact categories. Very High is reserved for events that could expose most customers' vendor data or let an attacker take full control of the production account.
4. **Determine risk.** Risk level comes from **Table I-2**. The overall likelihood and risk level columns in `risk-register.csv` were computed from the two tables by script, not assigned by hand.

## 3. Results

| Risk level | Count |
|---|---|
| Very High | 1 |
| High | 2 |
| Moderate | 17 |
| Low | 5 |
| **Total** | **25** |

Status: 11 In progress, 12 Open, 2 Closed (R-021 and R-022, both Low, accepted).

### Top risks
| Risk ID | Risk | Level | Treatment | Owner | Due |
|---|---|---|---|---|---|
| R-001 | Leaked long-lived CI/CD cloud key used to download the document bucket and copy a database snapshot | Very High | Short-lived federated CI credentials; delete the key; data-level logging and alerts | CTO | 2026-10-15 |
| R-002 | Cloud administrator account misused or taken over to read or delete all data and backups | High | Separate roles; remove standing administrator rights; backups in a separate account | CTO | 2026-11-30 |
| R-006 | Public statements, the security exhibit, or questionnaire answers shown to be false | High | Correct the claims; send corrected answers to prospects; CTO approval of every answer | Chief Executive Officer | 2026-10-15 |
| R-003 | Production database extracts on laptops exposed | Moderate | Stop extracts; synthetic test data; company laptop for the contractor | CTO | 2026-10-31 |
| R-005 | Tax IDs exposed at the AI model provider or the error tracking service | Moderate | Mask Social Security numbers before sending; redact error payloads | Senior Software Engineer | 2026-10-31 |
| R-009 | Customer notice misses the 72-hour DPA or Florida 10-day clock | Moderate | Adopt the P08 runbook; contact list; tabletop | CTO | 2026-11-12 |

**The common theme is one key and one person.** A single static administrator key (R-001), five full administrators (R-002), and one CTO who knows how everything fits together (R-019) mean that one mistake or one stolen credential reaches every customer's data and its backups. The treatments for R-001 and R-002 also reduce R-007, R-008, R-012, and R-024.

**The second theme is saying more than is true.** R-006 is High because the company has told customers and prospects things that are not so: that tax IDs never leave the platform, that penetration tests happen every year, that backups are kept 30 days, and that the company is "SOC 2 compliant." Under FTC Act Section 5 a false security claim is a deception risk on its own, whether or not a breach happens (P03 G-032 to G-040).

**Risks found or changed during the work:**
- R-025: added on 2026-08-26 after P07 testing found the root account password in a vault entry shared with all engineers and the contractor.
- R-010: the former Customer Success Manager's support desk and admin console accounts, found active during P07, were disabled on 2026-08-26. Their sign-in history showed no use after the departure date. The process gap remains open.
- R-015, R-020, and R-023: added on 2026-09-04 from the AI risk assessment (P10) and the SOC 2 readiness self-assessment (P09).

## 4. Treatment summary
- **Funded (2026 Q4 to 2027 Q1, approved by the Chief Executive Officer; about $33,000 one-time and $11,700 a year):**
  - SOC 2 Type 1 audit by a CPA firm: about $18,000 one-time
  - External penetration test, including tenant isolation and the AI feature: about $9,000 one-time
  - Compliance automation tool for policies, evidence, and access reviews: about $6,000 a year
  - Provider threat detection, data-level logging, and a 1-year log archive: about $1,800 a year
  - Separate backup account storage with write-once retention: about $900 a year
  - Awareness training with phishing simulations for 8 people (through the MSP) and secure coding training for 4 developers: about $1,600 a year
  - Hardware security keys for 4 people and the root account, and a company laptop for the contract developer: about $1,900 one-time
  - Independent assessment and policy work in 2026 (P07, P06): about $4,100 one-time
  - Annual MSP security review and contract update: about $1,400 a year in MSP time
- **Engineering time (no new spend):** federated CI credentials, cloud roles, versioning, masking of Social Security numbers, log redaction, cross-tenant tests, image scanning, and the deletion of former customers' data. The CTO estimates about 6 engineer-weeks in 2026 Q4.
- **Accepted:** R-021 (Low; laptops encrypted), R-022 (Low; single region, revisit at the SOC 2 Type 2).
- **Contract actions:** model provider DPA and the 30-day customer notice (R-016) by 2026-10-31; contractor security terms (R-003) by 2026-10-31; MSP incident notice and administrator terms (R-012) by 2026-12-31.

## 5. Approval
- Chief Executive Officer: approved all treatment plans, the two acceptances, and the budget on 2026-09-15.
- Progress: the CTO reports to the Chief Executive Officer in a 30-minute monthly review, using the P07 POA&M as the tracker.
- Next full review: July 2027, or sooner after a major change (for example, a new sub-processor, a new AI feature, or general availability of a second product) or an incident.
