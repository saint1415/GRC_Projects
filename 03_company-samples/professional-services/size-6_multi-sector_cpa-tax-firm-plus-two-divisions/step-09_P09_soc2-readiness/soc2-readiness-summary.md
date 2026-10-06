# SOC 2 Readiness Summary: Cris Santos Company Holdings | Professional Services | Multi-Sector

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. |
| Tier / Vertical | Multi-Sector / Professional, Scientific, and Technical Services (focus division: CPA and Tax Services) |
| Criteria | AICPA 2017 Trust Services Criteria (With Revised Points of Focus, 2022). Criteria are listed by ID with short topic labels in our own words |
| Scoping | Per division and service line (section 1). Two readiness reports: Practice Cloud (`soc2-readiness.csv`) and Tax and Advisory's client accounting services (`soc2-readiness-client-accounting.csv`). Tax preparation, Wealth, and the CPA Partners attest practice are out of scope |
| Prepared | 2026-09-10 by the Group Chief Risk Officer's assurance team with the Practice Cloud trust and assurance director and the client accounting services director |
| Service auditor | An unaffiliated CPA firm for both reports. CPA Partners sells SOC examinations to outside service organizations, but it does not examine the holding company or any group entity (`../00_company-facts.md` section 1), so it cannot be the service auditor here |

## 1. Scoping decisions per division
A SOC 2 report covers controls at a **service organization** for the **user entities** that rely on its service. For each service line the question is whether other organizations rely on its controls as part of their own.

| Division | Service line | Service organization? | Decision | Categories | Report |
|---|---|---|---|---|---|
| Practice Cloud | Multi-tenant practice management SaaS (SYS-S1) for about 26,000 accounting and tax firms | **Yes, a true service organization.** Customer firms are Safeguards Rule financial institutions that rely on Practice Cloud as their service provider (16 CFR 314.4(f)) | **In scope (full).** Existing annual Type 2 | Security, Availability, Confidentiality | Type 2, 12 months ending September 30 |
| CPA and Tax Services (Tax and Advisory) | Client accounting services: bookkeeping for 34,000 small businesses and payroll for 21,000 of them (SYS-T2) | **Yes, for this service line.** Client businesses rely on it to run payroll and keep their books, and 60 larger clients asked for a SOC 2 report in 2026 | **In scope.** First readiness assessment | Security, Availability, Processing Integrity | Type 1 as of 2027-06-30, then Type 2 for 2027-07-01 to 2027-12-31 |
| CPA and Tax Services (Tax and Advisory) | Individual and business tax preparation (TPCP) | No. Clients receive a return, not an outsourced process they build their own controls on | Out of scope (reasons below) | n/a | n/a |
| CPA and Tax Services (CPA Partners) | Audits, reviews, and SOC examinations | No. Clients rely on its opinions, not on its systems | Out of scope (reasons below) | n/a | n/a |
| Wealth | Investment advice and portfolio management for about 980,000 households | No. Its clients are households, not user entities | Out of scope (reasons below) | n/a | n/a |

**Why tax preparation is out of scope:**
1. **No user entities.** Individual clients buy a completed return. Business clients use the return, not Tax and Advisory's systems, in their own control environment.
2. **Other assurance exists.** The FTC Safeguards Rule program, the Qualified Individual's annual report to the board of managers (314.4(i)), IRS e-file program duties (Pub. 1345), and this sample's P03 and P07 results cover what clients ask about.
3. **Revisit trigger:** if Tax and Advisory begins preparing returns as an outsourced function for other firms, assess a SOC 2 report.

**Why the attest practice is out of scope:** CPA Partners' clients rely on its audit and examination opinions. Its own systems are not part of their control environments. CPA Partners is overseen through professional standards (quality management and peer review under AICPA standards and state board rules). It relies on group services, which are covered by the common control catalog and, once POAM-016 closes, its documented inheritance. **Independence also matters:** CPA Partners must not examine group services or controls that it relies on.

**Why Wealth is out of scope:**
1. **No user entities.** Households and individuals buy advice and portfolio management. They do not build controls on Wealth's systems.
2. **Assurance comes from regulators and custodians.** Wealth is examined by the SEC and is bound by Regulation S-P, Regulation S-ID, and the Advisers Act compliance and books-and-records rules (P03). Client assets are held by three unaffiliated qualified custodians, whose own assurance reports Wealth reviews.
3. **Institutional questionnaires** are answered with the group security program description and the P03 and P07 results.
4. **Revisit trigger:** if Wealth begins offering outsourced investment operations or sub-advisory services to other advisers, assess a SOC 1 or SOC 2 report.

**Other assurance considered.** A SOC 1 report addresses controls relevant to user entities' financial reporting. For client accounting services, payroll could be relevant to clients' financial statements, but the small private businesses it serves rarely have auditors who request SOC 1, and the clients that asked want security assurance. SOC 2 comes first; SOC 1 for payroll will be reconsidered in 2028. The vertical overlay names no other standard assurance mechanism beyond SOC reports and client assurance through engagement letters.

## 2. System descriptions (scope)
### 2.1 Practice Cloud
- **Services:** client portal with secure document exchange and e-signature (including IRS Form 8879), document management, workflow, time and billing, and invoice payment through a payment processor's hosted page; the **AI document intake** feature for 2,300 opt-in customer firms (launched 2026-02-02).
- **Infrastructure and software:** SYS-S1 on cloud provider B (container platform, managed database, primary and warm standby regions); group identity (SYS-G1), SOC (SYS-G2), and the backup vault (SYS-G3) as internal shared services.
- **Subservice organizations (carve-out):** cloud provider B; the payment processor (hosted page); **the third-party model provider for AI document intake** (not yet in the description, scenario gap 5).
- **People:** about 5,500 Practice Cloud employees plus the group SOC and identity teams.
- **Data:** customer firms' client documents and contact data (about 41 million end-client contacts across all tenants).
- **Complementary user entity controls:** customers enforce MFA for their staff (31% do not today, SW-004), provision and remove their users, decide their own IRC 7216 basis for using AI document intake, and review the report.

### 2.2 Client accounting services
- **Services:** bookkeeping, payroll processing, payroll tax deposits and filings, and pay statements for client businesses.
- **Infrastructure and software:** SYS-T2, a bookkeeping ledger SaaS and a payroll SaaS with bank feed connectors; documents exchanged through the Tax and Advisory tenant of Practice Cloud; group common controls carved in.
- **Subservice organizations (carve-out):** the ledger SaaS vendor and the payroll SaaS vendor. Their assurance reports are reviewed every year (CC9.2).
- **People:** client accounting specialists and payroll specialists in Tax and Advisory, plus group services.
- **Data:** client business financial records; payroll data for about 260,000 client employees, including SSNs and bank account numbers.
- **Complementary user entity controls:** clients approve each payroll, report employee changes promptly, review registers, and protect their own portal accounts.

## 3. Readiness results
### 3.1 Practice Cloud (`soc2-readiness.csv`)
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33 criteria) | 27 | 5 | 1 | 0 |
| Availability (A1, 3) | 3 | 0 | 0 | 0 |
| Confidentiality (C1, 2) | 0 | 2 | 0 | 0 |
| Processing Integrity (PI1, 5) | | | | 5 |
| Privacy (P1-P8, 18) | | | | 18 |

**Not ready:** CC2.3. The AI document intake feature and its model provider were not communicated to customers, are not on the sub-processor list, and are not in the system description; the product page made an unsubstantiated accuracy claim.
**Partially ready:** CC3.4 and CC8.1 (the launch skipped the privacy, IRC 7216, and contract review, and no adversarial testing was done), CC9.2 (the model provider was not assessed or monitored), CC7.2 (bulk-download alerts are not in the group SIEM), CC7.4 (24-hour notice customers not flagged), C1.1 (U.S.-only processing is a setting, not a contract term), and C1.2 (manual deletion; 11 of 40 certificates late).

**The immediate issue is the report now being prepared.** The 2026 observation period ended 2026-09-30, and the AI feature operated for about eight of its twelve months. Management must describe the feature, the model provider (as a carved-out subservice organization, with any complementary subservice organization controls), and the change itself. Expect the service auditor to evaluate CC2.3, CC3.4, CC8.1, and CC9.2 for exceptions. The report is due by 2026-12-15. POAM-020 covers the fix; the target is to send customer notices before the report is issued.

**Processing Integrity** is out of scope because Practice Cloud makes no processing integrity commitments. It is under evaluation for 2027, because customers now ask whether AI extraction is complete and accurate (P10). Adding it would require accuracy commitments Practice Cloud can evidence.

### 3.2 Client accounting services (`soc2-readiness-client-accounting.csv`)
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33 criteria) | 26 | 6 | 1 | 0 |
| Availability (A1, 3) | 1 | 1 | 1 | 0 |
| Processing Integrity (PI1, 5) | 4 | 1 | 0 | 0 |
| Confidentiality (C1, 2) | | | | 2 |
| Privacy (P1-P8, 18) | | | | 18 |

**Why so many Ready criteria for a first-time report:** control environment, risk assessment, identity, endpoint, monitoring, and incident criteria are met by group common controls already assessed in P07 and already relied on in the Practice Cloud report.
**Not ready:** CC2.3 (no written service commitments or system description) and A1.3 (no recovery test of payroll processing).
**Partially ready:** CC2.1 (no connector and data flow inventory), CC4.1 (service-specific controls never tested), CC6.1 (manually rotated bank feed credentials), CC7.2 (payroll SaaS logs not in the SIEM), CC7.4 (no client notice procedure), CC9.1 and A1.2 (no payroll continuity procedure, POAM-017), and PI1.2 (3 of 30 direct deposit changes without a recorded call-back).

## 4. Remediation plan and evidence calendar
| Quarter | Service line | Criteria | Evidence to collect |
|---|---|---|---|
| 2026 Q4 | Practice Cloud | CC2.3, CC3.4, CC8.1, CC9.2 | Updated system description for the period ending 2026-09-30; sub-processor notice and customer communications; release gate records; model provider assurance review (POAM-020) |
| 2026 Q4 | Practice Cloud | CC7.2, CC7.4, C1.1 | SIEM ingestion of bulk-download alerts (POAM-004); 24-hour flags in the tooling (POAM-005); model provider contract amendment |
| 2026 Q4 | Client accounting services | CC9.1, A1.2 | Updated contingency plan and manual payroll procedure (POAM-017) |
| 2027 Q1 | Practice Cloud | CC8.1, C1.2 | Red-team results (POAM-021); automated deletion workflow |
| 2027 Q1 | Client accounting services | CC2.1, CC2.3, CC4.1, CC6.1, CC7.2, CC7.4, A1.3, PI1.2 | Connector inventory; service commitments and draft system description; readiness test; connector rotation; payroll SaaS log ingestion; matrix rows for clients; payroll recovery exercise; call-back enforcement |
| 2027 Q2 | Client accounting services | All in-scope criteria | Type 1 as of 2027-06-30 |
| 2026 Q4 to 2027 Q3 | Practice Cloud | All in-scope criteria | Operating evidence for the period 2026-10-01 to 2027-09-30 |
| 2027 Q3 to Q4 | Client accounting services | All in-scope criteria | Operating evidence for the first Type 2 period (2027-07-01 to 2027-12-31) |

**Communication:** the Practice Cloud division president briefs the 140 enterprise customers on the AI feature change and the remediation before the 2026 report is issued. The client accounting services director sends the 60 requesting clients a readiness letter with the 2027 timeline.
