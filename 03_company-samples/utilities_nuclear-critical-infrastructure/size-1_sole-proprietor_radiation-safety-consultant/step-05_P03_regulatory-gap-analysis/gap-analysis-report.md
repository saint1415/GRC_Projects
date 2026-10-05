# Regulatory Gap Analysis: Cris Santos Company | Nuclear Reactors, Materials, and Waste | Sole Proprietorship

| Field | Value |
|---|---|
| Organization | Cris Santos Company (independent radiation safety consultant, NAICS 541690) |
| Tier / Vertical | Sole Proprietorship / Nuclear Reactors, Materials, and Waste |
| Vertical's primary regulation | 10 CFR 73.54 (with RG 5.71 Rev. 1 controls): **not a direct duty**; it reaches the owner only through Client A's contract (section 1) |
| Requirements analyzed | Client A Contractor Security Requirements (CSR-A), written from Client A's 73.54 program; 10 CFR 73.56 duties of an individual with unescorted access; 10 CFR 73.21-73.22 (conditional); 10 CFR Part 37 information protection as Client B's license condition and agreement (CSIA-B) pass it down; Fla. Stat. 501.171. Text checked on eCFR (version date 2026-09-23) |
| Assessment dates | 2026-07-20 to 2026-07-24 (self-assessment) |
| Assessor | Owner-consultant, with the on-call IT technician (under NDA since 2026-07-14). Evidence is self-attested, checked on screen where possible |
| Workbook | `gap-analysis.csv` (32 rows, G-001 to G-032) |
| Adopted | 2026-08-31 |

## 1. Applicability

### 1.1 The vertical's primary regulation binds Client A, not the owner
**10 CFR 73.54 does not apply directly.** It applies to "each licensee currently licensed to operate a nuclear power plant under part 50" and to Part 52 holders. The business holds no license of any kind and possesses no radioactive material. For the same reason:
- **10 CFR 73.77** (cyber security event notifications) covers "each licensee subject to the provisions of § 73.54 or § 73.110." Client A decides and reports; the owner's part is to tell Client A fast enough for it to meet its 1, 4, and 8-hour clocks (CSR-A (5)).
- **10 CFR 73.110** (Part 53 plants) and **NERC CIP** (registered entities) do not apply.
- **CIRCIA** is not in effect (no final rule as of 2026-09-25). As proposed, the business is below the SBA size standard ($19.0 million for NAICS 541690) and does not own or operate a commercial nuclear power reactor or fuel cycle facility.

**One paragraph of 73.54 names contractors.** 73.54(d)(1) requires the licensee to "ensure that appropriate facility personnel, including contractors, are aware of cyber security requirements and receive the training necessary." Client A meets that duty partly through the owner, so it is a row (G-002) and it is Met.

**The rest arrives by contract.** Client A wrote its Contractor Security Requirements (CSR-A, signed 2026-02-16) from its cyber security plan and access authorization program. Its ten terms are the practical form of 73.54 for a contractor: no connections to plant systems, kiosk-scanned media, MFA and clean devices for the portal, an 8-hour report clock, protection and return of Client A information, photo permits, and approved subcontractors. Rows G-007 to G-015 assess them; CSR-A (3) is G-002 and CSR-A (9) is the 73.56 rows. Client A's cyber security plan itself is not shared with contractors, so the CSF 2.0 and SP 800-53 mappings are the author's, and RG 5.71 control numbers are not cited.

### 1.2 Rules that bind the owner directly
- **10 CFR 73.56** binds the owner as an individual. 73.56(b)(1)(i) puts "any individual to whom a licensee intends to grant unescorted access" in the licensee's program. The owner's own duties are behavioral observation refresher training (73.56(f)(2)(iv)), reporting behavioral concerns (73.56(f)(3)), and promptly self-reporting legal actions (73.56(g)(1)). All are Met. 73.56(m) (protection of personal information in access authorization files) does not apply, because the business runs no access authorization program.
- **Safeguards Information (73.21-73.22)** is conditional. 73.21(a)(1) covers any "other person who produces, receives, or acquires" SGI, so the duty would attach the moment SGI reached the owner. The owner has none (search 2026-07-21) and has no locked security storage container or qualifying computer that 73.22(c) and (g) require. The only safe course is to refuse it: CSR-A (6) and POL-01 8.4.
- **Fla. Stat. 501.171** applies narrowly: the business is a sole proprietorship that keeps one Social Security number (the per-diem technician's W-9).

### 1.3 Part 37 reaches the owner through Client B
Client B's cesium-137 irradiator (about 1,200 Ci) is a category 2 quantity (Part 37 Appendix A: 27.0 Ci). Florida, an NRC Agreement State, applies Part 37 through a standard license condition. 37.43(d) makes **Client B** limit access to its security plan, implementing procedures, and approved-individuals list, decide need to know, run a trustworthiness and reliability determination for anyone without unescorted access (37.43(d)(3)(ii)), keep an access list, and remove people within 7 working days (37.43(d)(6)). Client B did its part for the owner on 2025-05-14 (G-023). The owner's duties come from **CSIA-B**, which turns 37.43(d) into six contract terms (G-024 to G-029).

### 1.4 Not in scope
10 CFR Part 810 and Part 110 (no export or import), DOT hazmat (ships no radioactive material), HIPAA (Client B's contract excludes patient records), FAR clauses (no federal contracts), and 10 CFR Part 26 fitness for duty (Client A runs it; not an information security duty).

## 2. Method
1. **Requirements.** CFR rows follow the regulation's own structure at the most specific paragraph that binds or reaches the owner; brief quotes come from the public-domain eCFR text. Contract rows follow the contract's own numbering. Reactor and grid rules that do not apply are kept as Not applicable rows so the reasoning is visible.
2. **Crosswalk.** No official NIST mapping exists for these requirements, so all CSF 2.0 and SP 800-53 columns are an **author mapping**.
3. **Evidence.** Self-attested by the owner and checked on screen with the IT technician: suite sharing report, email and laptop search, browser password store, USB drive contents, Client A kiosk slips and training records, Client B's 2025-05-14 letter, the paper cabinet.
4. **Status.** Met, Partially met, Not met, or Not applicable.

## 3. Results summary
| Requirement set | Met | Partially met | Not met | N/A | Total |
|---|---|---|---|---|---|
| Reactor and grid rules (C-NUCLEAR-R01 to R05) | 1 | 0 | 0 | 5 | 6 |
| CSR-A, Client A contract (C-NUCLEAR-S01) | 1 | 6 | 2 | 0 | 9 |
| 10 CFR 73.56 individual duties (C-NUCLEAR-S02) | 4 | 0 | 0 | 1 | 5 |
| Safeguards Information (C-NUCLEAR-S03) | 0 | 0 | 0 | 2 | 2 |
| Part 37 through CSIA-B (C-NUCLEAR-S04) | 1 | 1 | 5 | 0 | 7 |
| Fla. Stat. 501.171 (C-NUCLEAR-S05) | 0 | 2 | 1 | 0 | 3 |
| **Total** | **7** | **9** | **8** | **8** | **32** |

Of the 17 rows that are Not met or Partially met, 3 are rated High, 8 Moderate, and 6 Low.

**Pattern.** The duties the owner carries as a person (training, self-reporting, behavior reporting) are all Met; Client A's training and badge process enforce them. The gaps are in **handling client information on the owner's own systems**, where no client checks: Client B's security information in the suite and in an AI chat (5 of the 8 Not met rows), Client A's media and retained documents, and no way to meet the 8-hour and 24-hour notice clocks.

## 4. Action list (half page)
In order. The first five cost nothing and take under a day.

| # | Action | Citation | Gap risk | Target |
|---|---|---|---|---|
| 1 | Keep Client B security information only in Client B's share; named-person sharing; no client text in AI tools (done in part 2026-07-21) | 37.43(d)(1)-(2), (7); CSIA-B (1)-(3) | High | 2026-09-30 |
| 2 | Password manager, clear browser-saved passwords, standard daily account | CSR-A (4) | High | 2026-09-15 |
| 3 | Turn on MFA for accounting; keep the W-9 in one place | 501.171(2) | Low | 2026-09-15 |
| 4 | Return or destroy Client A's 2025 packages and certify; turn off photo sync | CSR-A (7)-(8) | Moderate | 2026-09-30 |
| 5 | Adopt POL-01 (SGI rule 8.4; disposal 8.8; end-of-engagement 6.6) | CSR-A (6); 501.171(8); CSIA-B (6) | Low | 2026-08-31 (done) |
| 6 | Encrypted Client A-only USB drive; field laptop offline | CSR-A (2), (6) | Moderate | 2026-10-09 |
| 7 | P08 runbook, notification matrix, printed contacts; walkthrough before the fall outage | CSR-A (5); CSIA-B (4); 501.171(4) | Moderate | 2026-10-09 |
| 8 | Subcontract with confidentiality terms for the per-diem technician | CSR-A (10) | Low | 2026-10-09 |
| 9 | Encrypted, unsynced notes container for Client B work; destroy and certify after acceptance | 37.43(d)(7)-(8); CSIA-B (2), (5) | Moderate | 2026-12-31 |

High and Moderate gaps are in the risk register (P01) and the POA&M (P07).

## 5. Pending regulatory changes
Checked in the Federal Register on 2026-10-05. None of these is a current obligation.
- **"Modernizing Security Requirements"** (proposed rule, 91 FR 38928, 2026-06-26; comments closed 2026-07-27). As proposed, it would update RG 5.71 (cutting about 19 percent of controls), remove the specific cyber event notifications in 73.77 and send licensees to 50.72, 50.73, and 73.1200 instead, revise 73.54 (introductory paragraph and the program review in 73.54(g)), change several 73.56 elements (credit re-evaluation, supervisory review, audit intervals, record retention), and for SGI allow commercially available FIPS 140 encryption and networked viewing with SP 800-171 controls. **Effect here:** Client A may later change CSR-A. The owner's own 73.56 duties in rows G-017 to G-019 were not among the proposed changes identified. Not final.
- **"Modernizing Requirements Relating to Physical Protection of Category 1 and Category 2 Quantities of Radioactive Material"** (proposed rule, 91 FR 17893, 2026-04-09). In 37.43 it amends only the refresher training paragraph (37.43(c)(3)); **37.43(d) is unchanged**, so the Client B rows stay. A final rule would reach Client B only when Florida updates its license condition.
- **CIRCIA** (proposed 6 CFR Part 226): final rule pending; recheck scope when published.

The `pending_rule_change` column flags each affected row.
