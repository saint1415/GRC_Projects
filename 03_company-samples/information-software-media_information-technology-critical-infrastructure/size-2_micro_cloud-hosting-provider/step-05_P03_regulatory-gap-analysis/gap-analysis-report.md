# Regulatory Gap Analysis: Cris Santos Company | Information Technology | Micro

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (managed cloud hosting provider) |
| Tier / Vertical | Micro / Information Technology |
| Registry regulation | FedRAMP (44 U.S.C. 3607-3616). **Does not apply** (section 1.1) |
| Regulations analyzed | (A) Bank service provider notification rule: 12 CFR 53.4 (OCC), 12 CFR 304.24 (FDIC), with the parallel 12 CFR 225.303 (FRB). (B) Interagency Guidelines Establishing Information Security Standards, flowed down by both bank contracts: 12 CFR Part 30, App. B and Supplement A (OCC); 12 CFR Part 364, App. B and Supplement A (FDIC). (C) Fla. Stat. 501.171 duties of a third-party agent |
| Assessment dates | Fieldwork 2026-07-20 to 2026-07-31 |
| Assessor | Lead Systems Engineer (Information Security Lead) with the Operations Manager (Compliance Coordinator) |
| Sources checked | eCFR point-in-time 2026-09-23: 12 CFR 53.2, 53.3, 53.4, 225.303, 304.22, 304.24; 12 CFR Part 30, App. B and Supplement A; 12 CFR Part 364, App. B and Supplement A. 12 U.S.C. 1867 (U.S. Code, 2024 edition, govinfo.gov). Fla. Stat. 501.171 (2026, Florida Legislature) |
| Approved | 2026-09-15 by the Owner |

## 1. Applicability
### 1.1 FedRAMP: does not apply
FedRAMP covers cloud services that federal agencies use. It has no size threshold or small-business exemption (C-IT-R01). It applies because of the customer, not the provider's size. **The company has no federal customer.** In April 2026 a regional federal office asked through a reseller whether the company could host a small application. The Owner declined, because the service has no FedRAMP authorization and the cost of getting one is out of reach for a 7-person company. Row G-001 records the finding. If a federal opportunity returns, the Owner will reassess before signing anything that ends with an agency as the user.

### 1.2 What binds the company today: its two bank customers
**Bank A** is a national bank (OCC-supervised). It has 6 hosted VMs holding loan document images and a file server, and the company patches its 8 branch servers through the RMM tool. **Bank B** is a state-chartered nonmember bank (FDIC-supervised). The company patches and checks backups on its 9 servers through the RMM tool. Both vendor contracts treat these services as subject to the Bank Service Company Act. Three sets of rules follow from that.

**A. Bank service provider notification rule (C-IT-R05). Applies by law.**
- A **bank service provider** is a bank service company or other person that performs covered services, meaning services subject to the Bank Service Company Act (12 CFR 53.2(b)(2) and (5); 12 CFR 304.22(b)(2) and (5)).
- It must notify at least one bank-designated point of contact at each affected bank **as soon as possible** after it determines that a computer-security incident has materially disrupted or degraded, or is reasonably likely to, covered services for **four or more hours** (12 CFR 53.4(a); 304.24(a)).
- There is no size exemption.
- The FRB version (12 CFR 225.303) has the same text. It does not bind the company today because neither bank is FRB-supervised.
- The banks then have their own clock: notice to their regulator no later than 36 hours after they determine a notification incident has occurred (for example 12 CFR 53.3). The company's notice feeds that clock.

**B. Interagency Guidelines Establishing Information Security Standards. Apply by contract.**
- The Guidelines bind the banks, not the company. But each bank must "require its service providers by contract to implement appropriate measures designed to meet the objectives of these Guidelines" (App. B, III.D.2). Both contracts do so, in the same words.
- Supplement A adds that a bank's contract with its service provider should require notice to the bank as soon as possible of unauthorized access to the bank's customer information. Both contracts set **24 hours**.
- In addition, services a regularly examined bank has performed for it by contract are subject to examination by the bank's federal regulator as if the bank performed them itself (12 U.S.C. 1867(c)(1)). The OCC or FDIC can look at the company's controls through the banks.
- The company is not itself a bank and has no direct regulatory duty under the Guidelines. The contracts make them its yardstick, so this analysis uses their structure (II and III, with Supplement A) row by row.
- **Adapted rows:** where a paragraph speaks of the board (III.A, III.F), the Owner plays that role. Where it speaks of overseeing service providers (III.D), it is applied to the vendors the company uses to serve the banks (colocation, cloud, RMM, PSA, DNS, MDR). These adaptations are the company's reading of "appropriate measures," not text in the Guidelines.

**C. Florida Information Protection Act (Fla. Stat. 501.171). Applies by law.**
- The company is a **third-party agent**: an entity contracted to maintain, store, or process personal information for a covered entity (501.171(1)(h)). Bank A's loan documents are one example; many hosting customers keep personal information in their VMs.
- As an agent it must take reasonable measures to protect that data (501.171(2)) and dispose of customer records properly (501.171(8)).
- After a breach of a system it maintains, it must notify the customer no later than 10 days after determining the breach, and give the customer all the information the customer needs for its own notices (501.171(6)(a)).
- For its own data (employee records, customer contact and billing data), the company is a covered entity with the duties in 501.171(3) to (5). Those are handled in the P08 notification matrix, not as rows here.

### 1.3 Other vertical requirements
| ID | Requirement | Applies? | Why |
|---|---|---|---|
| C-IT-R01 | FedRAMP | No | Section 1.1 |
| C-IT-R02 | CMMC (32 CFR Part 170) | No | No DoD contracts or subcontracts; the MSA prohibits CUI |
| C-IT-R03 | DFARS 252.204-7012 | No | No covered defense information; no clause flowed down |
| C-IT-R04 | DOJ Data Security Program (28 CFR Part 202) | No | No data brokerage, vendor, employment, or investment agreement gives a country of concern or covered person access to customer data. All staff and the vendor support teams used are U.S.-based. The Operations Manager rechecks at each new vendor contract |
| C-IT-R05 | Bank service provider notification rule | **Yes** | Section 1.2 A |
| C-IT-R06 | CIRCIA | Not in force | No final rule as of 2026-09-25 (section 5) |

## 2. Method
1. **Requirements.** Rows follow each rule's own structure and cite section and paragraph numbers. Summaries paraphrase or briefly quote the public-domain federal and Florida text.
   - G-001: FedRAMP applicability.
   - G-002 to G-006: the bank notification rule (definitions, 53.4(a), (a)(1), (a)(2), (b)).
   - G-007 to G-036: the Interagency Guidelines (I.C definitions, II.A, II.B.1-4, III.A to III.F) and Supplement A (II, II.A.1, II.A.2). III.G (2001 to 2006 implementation dates) is historical and not rated.
   - G-037: Bank Service Company Act examination.
   - G-038 to G-042: Fla. Stat. 501.171 third-party agent duties.
2. **Crosswalk.** Every row is mapped to CSF 2.0 and SP 800-53 Rev. 5. All mappings are **author mappings**; NIST publishes no official mapping for these rules.
3. **Documentary evidence.** Each status rests on a named document or record: the two bank contracts and their security exhibits, the MSA, the bank contact file, the maintenance mailing list, identity provider, RMM, and hypervisor manager user lists, the PSA vault permission report, storage and backup settings, the MDR data source list and July report, the 2025 training report, HR files, warranty return tickets, and the contract folder. Interviews covered all 7 staff.
4. **Status.** Met, Partially met, Not met, or Not applicable, **as of the end of fieldwork (2026-07-31)**. Work completed since then (policies and the P08 runbook approved 2026-09-15, the P07 assessment) is noted in the remediation column but does not change the status.
5. **Gap risk** uses the P01 scale (Very Low to Very High).

The control statements behind these rows are the same as in the SSP (P02), where the regulatory driver column cites the same paragraphs.

## 3. Results summary
| Section | Met | Partially met | Not met | N/A |
|---|---|---|---|---|
| FedRAMP applicability (G-001) | 0 | 0 | 0 | 1 |
| Bank service provider notification rule (G-002 to G-006) | 0 | 3 | 2 | 0 |
| Interagency Guidelines and Supplement A, by contract (G-007 to G-036) | 3 | 16 | 11 | 0 |
| Bank Service Company Act examination (G-037) | 0 | 1 | 0 | 0 |
| Fla. Stat. 501.171 third-party agent duties (G-038 to G-042) | 1 | 2 | 1 | 1 |
| **Total (42)** | **4** | **22** | **14** | **2** |

Of the 36 rows Partially met or Not met, the gap risk is **8 High, 18 Moderate, and 10 Low**.

**What the numbers say.**
- **The risk assessment rows are the only strong area.** The first assessment (P01) was finished at the end of fieldwork, so III.B.1 and III.B.2 are Met.
- **Everything the banks would ask about first is weak.** There is no written program (II.A), no response program (III.C.1.g), no bank notice procedure (53.4(a)), and no valid bank contact (53.4(a)(1)).
- **Access control is the deepest gap (III.C.1.a, Not met).** Shared and standing privileged accounts reach the bank systems, the same concentration problem behind the top risks in P01.
- **The physical, encryption-in-transit, and background-check pieces are mostly in place**, largely because the colocation provider and the SaaS vendors supply them.

## 4. Priority gaps and roadmap
### 4.1 High gaps
| Gap | Rows | Risk | Action | Owner | Target |
|---|---|---|---|---|---|
| No written information security program | G-008 | High | POL-02, POL-03, POL-04 and the SSP approved 2026-09-15, effective 2026-10-01 | Operations Manager | 2026-10-01 (done) |
| Shared and over-privileged accounts reach bank systems; support desk open to social engineering | G-011, G-018 | High | Remove shared RMM accounts (2026-10-15); named, MFA-protected hypervisor and BMC administration; least-privilege portal account; call-back check (R-001, R-003, R-004, R-005) | Lead Systems Engineer | 2026-12-31 |
| No dual control for actions that can harm every customer | G-022 | High | Two-person approval for multi-customer RMM scripts (2026-11-30) and backup deletion (2026-12-31) | Lead Systems Engineer | 2026-12-31 |
| No monitoring of the management plane | G-023 | High | RMM, cloud, hypervisor manager, and DNS logs to the MDR; 12-month retention; weekly review | Lead Systems Engineer | 2027-01-31 |
| No response program | G-024 | High | POL-03 and P08 runbook approved 2026-09-15; first tabletop with a bank scenario | Operations Manager | 2026-10-31 |
| Backups deletable and unproven; no plan for a DC-1 loss | G-025 | High | Separate backup account with object lock; quarterly restore tests; contingency plan; degraded-mode recovery test | Lead Systems Engineer | 2026-12-31 to 2027-05-31 |
| Unpatched management interfaces; no DDoS procedure | G-010 | High | Monthly authenticated scans; host and BMC updates; null-route procedure | Lead Systems Engineer | 2027-01-31 |

### 4.2 Bank notice gaps (apply now, by law and contract)
- **No procedure for the 4-hour determination or the notice** (G-003, Not met). The P08 runbook now puts the determination at the 2-hour mark of any incident touching a bank's VMs or servers. It is untested; the first tabletop uses a bank scenario.
- **No valid designated contact at either bank** (G-004, Not met). The Operations Manager requests contacts in writing from both banks and verifies them quarterly, by 2026-10-31. Until then the CEO and CIO fallback (G-005) applies, so their contacts go into the incident kit.
- **24-hour contract notice of unauthorized access to customer information** (G-034, Not met). Added to the P08 notification matrix. It is shorter than the MSA's 72 hours and usually comes first.
- **Maintenance notices miss Bank B** (G-006). Without prior notice, planned work on Bank B's servers is not covered by the 53.4(b) exception.

### 4.3 Roadmap
| Phase | Due | Actions | Rows closed |
|---|---|---|---|
| 1. Program and notice basics | 2026-10-31 | Independent control assessment (done 2026-08-19, P07); policies effective (done 2026-10-01); bank contacts and register; incident kit; tabletop; monthly report to the Owner; inventory of bank customer information; shared RMM accounts removed (2026-10-15); colocation access list reviewed | G-002 to G-005, G-007, G-008, G-013, G-017, G-014, G-019, G-024, G-034, G-040 |
| 2. Access and change | 2026-12-31 | Named and MFA-protected administration everywhere; least-privilege portal account; dual control; change log and maintenance notices to banks; vault restrictions; disposal and warranty changes; role-based training; vendor reviews and contract terms; separate backup account | G-006, G-009, G-011, G-012, G-018, G-020 to G-022, G-026, G-028 to G-031, G-039, G-042 |
| 3. Detection and testing | 2027-01-31 | Management-plane logs to the MDR with 12-month retention; weekly review; monthly scans; quarterly restore tests; host and BMC updates | G-010, G-023, G-027, G-035 |
| 4. Resilience | 2027-05-31 | Contingency plan (2027-03-31); degraded-mode recovery test before hurricane season | G-025 |
| 5. Annual cycle | 2027-07-31 to 2027-09-30 | Risk assessment update (July); program review and annual report to the Owner (September) | G-015, G-032, G-033 |

**Examiner and due diligence readiness (G-037).** Both banks sent 2026 vendor due diligence questionnaires due 2026-10-30. The answer package is the SSP, the P07 results and POA&M, and the P09 readiness summary. The same package serves if an examiner asks the banks about the company.

**Progress check.** The Lead Systems Engineer reports progress to the Owner at the monthly security meeting, using the P07 POA&M as the tracker. High and Moderate gaps are carried in the risk register (P01). Where the related control was assessed, they also appear in the POA&M.

## 5. Pending regulatory changes
- **CIRCIA** (6 U.S.C. 681b; proposed 6 CFR Part 226, 89 FR 23644): no final rule as of 2026-09-25, so there is no current obligation. The statute sets 72 hours for covered cyber incidents and 24 hours for ransom payments, once a final rule takes effect. Whether a 7-person hosting provider would be a covered entity depends on the final size and sector criteria; the proposed rule tied size to the SBA standards. Flagged in the `pending_rule_change` column of the incident rows.
- **The other rules were checked as currently in force only.** The Operations Manager rechecks 12 CFR 53.4, 304.24, and 225.303, Appendix B to Parts 30 and 364, and Fla. Stat. 501.171 for amendments at each September program review (G-032).
