# Regulatory Gap Analysis: Cris Santos Company | Finance and Insurance | Micro

| Field | Value |
|---|---|
| Organization | Cris Santos Community Federal Credit Union (member-owned federal credit union) |
| Tier / Vertical | Micro / Finance and Insurance |
| Regulation analyzed | NCUA security program rule, 12 CFR 748.0 and 748.1, with Appendix A (Guidelines for Safeguarding Member Information) and Appendix B (response programs and member notice). Text read from eCFR, current through 2026-09-23 |
| Requirement IDs | N52-R01 (GLBA section 501(b), which Part 748 Appendix A implements); C-FINANCIAL-R03 (12 CFR 748.1(c)) |
| Assessment dates | 2026-07-13 to 2026-07-24 |
| Assessor | Operations Manager (Information Security Officer) with the MSP lead technician |
| Approved | President and CEO, 2026-08-31 |

## 1. Applicability
**The vertical's default regulation does not apply.** The Finance and Insurance overlay names the Interagency Guidelines Establishing Information Security Standards (12 CFR 30 App. B for the OCC, 208 App. D-2 and 225 App. F for the Federal Reserve, 364 App. B for the FDIC; N52-R02). Those Guidelines cover national banks, federal savings associations, state member and nonmember banks, and bank holding companies. A credit union is none of these. The same is true of the 36-hour Computer-Security Incident Notification Rule (12 CFR Part 53, 225 Subpart N, 304 Subpart C). **The OCC rules used in the Small sample (Cris Santos Bank, N.A.) do not apply to this credit union.**

**The governing regulation is NCUA Part 748, and it applies.** Section 748.0(a) says each federally insured credit union "will develop a written security program," and Appendix A I.A says the Guidelines "apply to member information maintained by or on behalf of federally insured credit unions." The credit union is a federal credit union insured by NCUA. Part 748 has no size exemption. Appendix A II.A asks for a program "appropriate to the size and complexity of the credit union," which lets a 7-person credit union choose simpler ways to meet each standard, not skip one. Appendix A was issued under GLBA sections 501 and 505(b) and is modeled on the same structure as the banks' Guidelines (program, board, risk assessment, controls, service providers, adjustment, board report), so the Small sample's analysis pattern carries over with NCUA citations.

**Charter decision.** The credit union holds a federal charter, so NCUA is its only supervisor. Two consequences: Appendix B II.A.1.b's notice to "its applicable state supervisory authority" (for state-chartered credit unions) does not apply, and the federal-only rules on disposal (748.0(c), 717.83) do.

**How binding each part is.** The requirement type column keeps the regulation's own wording:
- **Rule (will/must):** 748.0 and 748.1 (10 rows analyzed).
- **Guideline (should):** Appendix A II and III, except III.C.1.a to h. Appendix A calls itself "guidance standards," but 748.0 requires the program they describe.
- **Measure to consider (must consider; adopt if appropriate):** Appendix A III.C.1.a to h. The credit union "must consider" each measure and adopt those it concludes are appropriate. For a credit union that sends wires and offers online banking, all eight are appropriate, so each is assessed as if required.
- **Guidance (should):** Appendix B, NCUA's interpretation of the response program 748.0(b)(3) requires.

**Excluded, with reasons:**
- **748.2 (BSA compliance program)** is examined through the BSA independent test, not the information security program. The SAR duty in 748.1(d) is included because the response program relies on it.
- **Appendix A I and Appendix B I** (introductions, definitions, and background) state no requirement.

**Related rules considered but not analyzed row by row:** the Identity Theft Prevention Program for federal credit unions (12 CFR 717.90) drives the member account takeover treatment (P01 R-003); Part 749 (vital records, rewritten effective 2026-07-16) is covered through 748.0(b)(5); Fla. Stat. 501.171 drives the P08 notification matrix. The FTC Safeguards Rule (N52-R03) does not apply: it covers non-federally insured credit unions, and this one is federally insured.

## 2. Method
1. **Requirements.** Each paragraph of 748.0 and 748.1, Appendix A II and III, and Appendix B II and III was made one row. Appendix A III.C.1.a has three parts (workforce access, member authentication, and fraudulent-means controls) and gets three rows; II.B lists four objectives and gets four rows.
2. **Crosswalk.** Each row was mapped to CSF 2.0 subcategories and SP 800-53 Rev. 5 controls. This is an **author mapping**: no official NIST mapping of Part 748 was found.
3. **Documentary evidence.** Each status rests on a named document or record: the 2019 policy manual and incident plan, board minutes from 2019 to 2026, the core, admin console, wire portal, and suite user lists, the vendor contracts and SOC reports, the MSP device list and monthly report, the SAR log (reviewed without copying contents), a sample of 10 June 2026 wire request files, and a walkthrough of the office on 2026-07-15. Interviews covered all 7 employees and the MSP lead technician.
4. **Status.** Each row was rated Met, Partially met, Not met, or Not applicable **as of the end of fieldwork (2026-07-24)**. Actions completed since then (the shared mailbox conversion on 2026-08-12, board approvals on 2026-08-25) are noted in the remediation column but do not change the status.

## 3. Results summary
| Section | Met | Partially met | Not met | N/A |
|---|---|---|---|---|
| 748.0 and 748.1 (program, certification, reports) | 1 | 8 | 2 | 0 |
| App. A II (program and objectives) | 0 | 5 | 0 | 0 |
| App. A III.A Involve the board | 0 | 1 | 1 | 0 |
| App. A III.B Assess risk | 0 | 3 | 0 | 0 |
| App. A III.C Manage and control risk | 1 | 10 | 3 | 0 |
| App. A III.D Oversee service providers | 0 | 2 | 1 | 0 |
| App. A III.E and III.F Adjust and report | 0 | 0 | 2 | 0 |
| App. B (response program and member notice) | 0 | 4 | 6 | 0 |
| **Total (50)** | **2** | **33** | **15** | **0** |

Of the 48 unmet or partially met rows: 10 are **Rule** provisions of 748.0 or 748.1, 19 are Appendix A **Guideline** items, 9 are Appendix A III.C.1 **measures** the credit union must consider and has judged appropriate, and 10 are Appendix B **Guidance** items. By gap risk: 6 High, 28 Moderate, 14 Low.

**What the numbers say.** The two Met rows are physical security (III.C.1.b) and SAR filing (748.1(d)), both long-standing credit union routines. The weakest areas are the ones that changed after 2019: the NCUA 72-hour report (in force since 2023-09-01), member notice, vendor oversight, and the board's view of the program. The credit union has relied on its vendors' controls without reading their SOC reports or setting incident notice terms.

## 4. Priority gaps
| Gap | Citation | Risk | Action | Owner | Target |
|---|---|---|---|---|---|
| No independent check that a member made an emailed wire request | App. A III.C.1.a (fraudulent means), G-025 | High | Written wire security procedure: callback to the number on file for every wire not requested in person; BEC training | Operations Manager | 2026-10-31 |
| No 72-hour NCUA cyber incident report procedure | 748.1(c), G-010 | High | Reportable-incident test, clock, and NCUA contact in POL-03 and P08 | Operations Manager | 2026-10-31 |
| Vendor contracts silent on incident notice | App. B II, G-041 | High | Core side letter; MSP amendment; renewal terms | President and CEO | 2026-10-31 |
| Weak member authentication; 2025 takeover | App. A III.C.1.a (member authentication), G-024 | High | Member MFA and alerts; verified contact changes | Operations Manager | 2026-12-31 |
| Member documents in a password-only shared mailbox | 748.0(b)(2), G-003; App. A II.B, G-015 | High | Delegated mailbox with MFA (done 2026-08-12); document clean-up; secure upload link | Operations Manager | 2026-12-31 |
| No board oversight, ISO designation, or annual report since 2022 | App. A III.A.2, III.F, G-018, G-040 | Moderate | ISO designated and first report delivered 2026-08-25; quarterly status | President and CEO | 2026-09-30 |
| SOC reports never reviewed | App. A III.D.3, G-038 | Moderate | Annual review with CUEC mapping (core done 2026-08-18) | Operations Manager | 2026-11-30 |
| No member notice procedure | App. B II.A.1.e, III, G-046, G-048 | Moderate | Decision record and template in P08 | Operations Manager | 2026-10-31 |
| No monitoring or log review | App. A III.C.1.f, G-030 | Moderate | Monthly review; suite alerts; EDR | Operations Manager | 2026-12-31 |
| Vital records program out of date after the Part 749 rewrite | 748.0(b)(5), G-006 | Moderate | Update the program and log; confirm 749.2(b) language with the core processor | President and CEO | 2026-12-31 |

The full list, with evidence, is in `gap-analysis.csv`. Every High and Moderate gap is carried into the risk register (P01) and, where the control was assessed, the POA&M (P07).

## 5. Remediation plan
The plan fits a 7-person credit union: most actions are one-page procedures, vendor settings, or contract letters, not new systems. The MSP performs the technical work under the ISO's direction. Costs are in the P01 treatment summary.

| Phase | Due | Actions | Gaps closed (citation) |
|---|---|---|---|
| 1. Governance and contracts | 2026-09-30 | Board approval of the program and ISO designation (done 2026-08-25); first annual report (done 2026-08-25); shared mailbox MFA (done 2026-08-12); termination checklist | 748.0(a); App. A II.A, III.A.1, III.A.2, III.F |
| 2. Wires and incidents | 2026-10-31 | Written wire security procedure with callbacks; BEC training; POL-03 and the P08 runbook with the 748.1(c) and Appendix B steps; core side letter on incident notice; access reconciliation and override clean-up; suite log retention; change approval step | 748.1(c); 748.0(b)(3), (b)(4); App. A III.C.1.a, III.C.1.d, III.C.1.e, III.C.1.g, III.C.2; App. B II, II.A.1.a to e, II.A.2, III.A to III.C |
| 3. Vendors and monitoring | 2026-11-30 | SOC reviews with CUEC mapping; vendor due diligence checklist; inventory of member information locations; tabletop exercise | App. A III.B.1, III.B.3, III.D.1, III.D.3 |
| 4. Hardening and resilience | 2026-12-31 | Member MFA and alerts; desktop encryption; secure upload and encrypted email; EDR and alerts; separate imaging backup copy; failover router; continuity plan rewrite with the catastrophic act report and vital records log; disposal certificates | 748.0(b)(2), (b)(5), 748.0(c), 748.1(b); App. A II.B, III.C.1.c, III.C.1.f, III.C.1.h, III.C.4 |
| 5. Annual cycle | 2027-01-31 to 2027-08-31 | Certification based on the updated program (January); risk assessment update (July); independent assessment, program review, and board report (August); MSP and core contract terms at renewal | 748.1(a); App. A III.B.2, III.C.3, III.D.2, III.E |

**Progress check.** The ISO reports progress to the President and CEO each month and to the board each quarter, using the P07 POA&M as the tracker.

## 6. Pending regulatory changes
- **Appendix A and Appendix B may leave the CFR.** On 2025-12-11 NCUA proposed removing Appendix A (90 FR 57399) and Appendix B (90 FR 57397) from the CFR and republishing their content as a Letter to Credit Unions and as guidance. NCUA's stated reason is that the appendices are guidance, not regulation, so placing them in the CFR may be confusing. Comments closed 2026-02-09. As of 2026-09-23 eCFR still shows both appendices, and no final rule was found in the Federal Register. The duties in 748.0 (written program, response to unauthorized access) and 748.1(c) (72-hour report) would not change. The rows that could move are flagged in the `pending_rule_change` column. Note that 748.1(c)(1)(i)(A) defines a member information system by reference to Appendix A I.B.2.e, so a final rule may also amend that cross-reference.
- **Catastrophic act reporting.** On 2025-12-29 NCUA proposed giving credit unions more time to report catastrophic acts and dropping the specific list of items to document (90 FR 60591). Not final; 748.1(b) is analyzed as in force.
- **AML/CFT programs.** On 2026-04-10 the OCC, FDIC, and NCUA proposed AML/CFT program rules (91 FR 18304) that amend Part 748. Not final; not analyzed here.
- **Vital records.** Part 749 was rewritten by a final rule effective 2026-07-16 (91 FR 36073). This analysis uses the new text (G-006).
- **Third-party guidance.** On 2026-09-15 the OCC, Federal Reserve, FDIC, and NCUA published proposed third-party risk management guidance (91 FR 58536; comments due 2026-11-16). It is guidance, still proposed, and its content was not analyzed here. The Appendix A III.D rows rest on the regulation text, which it would not change.
