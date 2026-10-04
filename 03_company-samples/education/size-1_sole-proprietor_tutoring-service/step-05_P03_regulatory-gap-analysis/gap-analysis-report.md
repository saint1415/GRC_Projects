# Regulatory Gap Analysis: Cris Santos Company | Educational Services | Sole Proprietorship

| Field | Value |
|---|---|
| Organization | Cris Santos Company (tutoring and educational support service) |
| Tier / Vertical | Sole Proprietorship / Educational Services |
| Regulation analyzed | FTC Children's Online Privacy Protection Rule (COPPA Rule), 16 CFR Part 312, as amended by 90 FR 16918 (Apr. 22, 2025). Text checked on eCFR (current version); effective 2025-06-23, compliance date 2026-04-22 (N61-R03) |
| Secondary (limited) | Three Florida duties that reach the records COPPA does not: Fla. Stat. 501.171(2) and (8), and 934.03(2)(d) |
| Why not the vertical's default | The Educational Services profile names the GLBA Safeguards Rule as enforced by Federal Student Aid for Title IV institutions. A tutoring business takes no Title IV funds, so that rule does not reach it (section 1). COPPA is the federal rule that does |
| Assessment dates | 2026-07-13 to 2026-07-17 (self-assessment; tests on 2026-07-16) |
| Assessor | Owner-tutor, with the on-call IT technician (confidentiality and data-handling agreement signed 2026-07-08). Evidence is self-attested, checked on screen where possible |
| Adopted | 2026-07-31 |

## 1. Applicability
**The COPPA Rule applies.** The rule covers an "operator" of "a website or online service directed to children" (16 CFR 312.2 and 312.3). The business is an operator: it runs a commercial website, and through the website builder (its service provider) it collects and maintains personal information from the users of the members-only student portal (312.2, "operator", which counts information collected by an agent or service provider). The portal is a portion of the site built for students in grades 2 to 7, which the rule calls a website or online service directed to children ("or portion thereof"). What it collects is personal information under 312.2: first and last name, a user name, photographs of work that can show a child's image, audio files that contain a child's voice, and messages combined with those identifiers. Online sessions add video and audio recordings of children (cloud recordings on the video platform), which are also personal information.

**The test is online collection from children under 13, not size.** COPPA has no small-business exemption. The only size language is in 312.8(b): the written security program must be appropriate to "the operator's size, complexity, and nature and scope of activities." If the owner taught only in person and collected nothing online from children, COPPA would not apply. Information that parents give the owner (intake forms, report cards, IEP and 504 plans, evaluations) is not collected from a child, so COPPA does not reach it. Florida law and the FTC Act still do.

**The 2025 amendments apply in full.** They took effect on 2025-06-23 and operators had until 2026-04-22 to comply, except three safe harbor reporting provisions (312.11(d)(1), (d)(4), and (g)) that do not concern operators. Fieldwork in July 2026 is after that date. The amendments that matter most here are the written information security program (312.8(b)), the written data retention policy published in the online notice (312.10), and separate consent for disclosure to third parties (312.5(a)(2)). The Federal Register API showed no document affecting 16 CFR Part 312 published since the 2025 amendments (checked 2026-10-04).

**Other education rules checked (no gap rows):**
| Requirement | Result | Reason |
|---|---|---|
| FERPA (N61-R01) | Does not apply | FERPA applies to an educational agency or institution "to which funds have been made available under any program administered by the Secretary" (34 CFR 99.1(a)). The business receives no such funds and has no contract with a school or district. Recheck if it ever tutors under a school or district contract |
| GLBA Safeguards Rule for Title IV institutions (N61-R02) | Does not apply | Not a Title IV participant and not a financial institution: it extends no credit and offers no financing (author's analysis) |
| CIPA (N61-R04) | Does not apply | Not an E-Rate recipient |
| HIPAA Security Rule (N61-R05) | Does not apply | Not a health care provider or covered entity. Evaluations shared by parents are protected under Florida law instead (G-037) |
| CIRCIA (N61-R06) | Not in effect | Proposed only (89 FR 23644); no final rule as of 2026-09-25. The proposed education criteria (school districts with 1,000 or more students, Title IV institutions) would not reach a tutor in any case |

**Excluded COPPA rows, with reasons (5):** G-003 and G-009 (no contact information is collected from the child to seek consent), G-010 (the voluntary, multiple-contact, and safety notices go with consent exceptions the business does not use), G-015 (reading audio is kept under parental consent, not the one-time audio exception), and G-036 (safe harbor membership is voluntary).

## 2. Method
1. **Requirements.** Each row is a paragraph of 16 CFR 312.4 to 312.11 at the level the rule uses (for example 312.4(c)(1)(i) to (vii) and 312.8(b)(1) to (5)). 312.10 has four separate duties, so it has four rows. Summaries paraphrase public-domain regulatory text. The three Florida rows are limited to duties that fill COPPA's gaps for records parents provide.
2. **Requirement type.** COPPA has no required/addressable split. Its duties are mandatory; "Conditional" marks duties that apply only when a practice is used.
3. **Crosswalk.** Each row maps to CSF 2.0 and SP 800-53 Rev. 5. These are **author mappings**; no official NIST mapping exists for 16 CFR Part 312.
4. **Evidence.** Self-attested by the owner and checked on screen with the IT technician: the enrollment agreement, the website and portal pages (2026-07-15), the builder's member, collaborator, and analytics settings, the video recording list, vendor terms, and the P07 tests on 2026-07-16.
5. **Status.** Met, Partially met, Not met, or Not applicable as of the end of fieldwork (2026-07-17). Items fixed since (POL-01 adopted 2026-07-31) appear in the remediation columns, not as a changed status.

## 3. Results summary
| Section | Met | Partially met | Not met | N/A |
|---|---|---|---|---|
| 312.4 Notice | 0 | 3 | 9 | 4 |
| 312.5 Parental consent | 0 | 2 | 1 | 0 |
| 312.6 Parent review and deletion | 0 | 3 | 0 | 0 |
| 312.7 No conditioning on extra data | 0 | 1 | 0 | 0 |
| 312.8 Security program | 1 | 4 | 3 | 0 |
| 312.10 Retention and deletion | 0 | 1 | 3 | 0 |
| 312.11 Safe harbor | 0 | 0 | 0 | 1 |
| **COPPA subtotal (36)** | **1** | **14** | **16** | **5** |
| Florida (3) | 0 | 3 | 0 | 0 |
| **Total (39)** | **1** | **17** | **16** | **5** |

Of the 33 rows that are not met or partially met, 8 are rated **High**, 15 **Moderate**, and 10 **Low**.

**The main finding.** The portal was built and launched in January 2025 as a teaching tool, and nobody treated it as a children's online service. Parents do sign and pay before a child gets an account, which is a sound consent method (G-019), but they sign something that does not tell them what the portal collects or who sees it. Two duties that the 2025 amendments added are entirely missing: the written security program (312.8(b)) and the published retention policy (312.10). The one Met row is the risk assessment (G-027), completed during this self-assessment.

## 4. Action list (half page)
In order. The first six cost nothing and must be done before the fall term starts on 2026-08-17.

| # | Action | Rows | Gap risk | Target |
|---|---|---|---|---|
| 1 | Stop entering student information in the consumer AI assistant; delete history; request deletion (P10) | G-006, G-018 | High | 2026-08-14 |
| 2 | Turn on MFA (email suite, website builder, video platform); laptop encryption; separate family account | G-024, G-028, G-037 | High | 2026-08-14 |
| 3 | Post the online children's privacy notice with links on the home page, sign-in page, and each upload form | G-011 to G-014, G-016, G-035 | High | 2026-08-14 |
| 4 | Send the new direct notice and collect fresh consent from every portal family | G-001, G-002, G-004 to G-008, G-017 | High | 2026-08-14 |
| 5 | Turn off portal analytics; remove the birth date and school name fields | G-014, G-023 | Moderate | 2026-08-14 |
| 6 | Parents set portal passwords; delete the password spreadsheet | G-022, G-037 | High | 2026-08-14 |
| 7 | Adopt POL-01 as the written program, with the coordinator designation and retention schedule | G-025, G-026, G-034 | Moderate | 2026-07-31 (done) |
| 8 | Record only with consent on file; 30-day automatic deletion of recordings | G-039, G-032 | Moderate | 2026-08-31 |
| 9 | Written security assurances from the website builder and video platform | G-031 | High | 2026-09-30 |
| 10 | First retention purge; wipe the old laptop; deletion checklist; monthly sign-in review | G-032, G-033, G-038, G-021, G-029 | Moderate | 2026-09-30 |

High and Moderate gaps are in the risk register (P01, mainly R-005, R-006, and R-007) and the POA&M (P07).

## 5. Pending regulatory changes
- **COPPA Rule:** no proposed or final amendment to 16 CFR Part 312 has been published since the 2025 amendments (Federal Register API, checked 2026-10-04). The `pending_rule_change` column is "None" for every row.
- **CIRCIA (N61-R06)** remains proposed and would not cover this business as proposed.
- **No breach notice duty in COPPA.** 16 CFR Part 312 contains no breach notification requirement. Breach notice duties come from Florida law (P08).
