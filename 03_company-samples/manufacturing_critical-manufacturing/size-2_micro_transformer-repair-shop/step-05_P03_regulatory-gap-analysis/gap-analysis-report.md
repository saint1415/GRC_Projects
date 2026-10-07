# Regulatory Gap Analysis: Cris Santos Company | Critical Manufacturing | Micro

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (transformer repair and remanufacturing shop, Florida) |
| Tier / Vertical | Micro / Critical Manufacturing (NAICS 335311) |
| Primary benchmark | NIST Cybersecurity Framework (CSF) 2.0 (NIST CSWP 29, February 26, 2024) with NIST SP 800-82 Rev. 3, *Guide to Operational Technology (OT) Security* (September 2023), as the OT guide. **Voluntary**: no binding sector-wide cyber rule applies |
| Secondary obligations (binding) | FAR 52.204-21 in the shop's one federal purchase order; the G&T cooperative's Vendor Cyber Security Exhibit, which flows down CIP-013-2 Requirement R1 Parts 1.2.1 to 1.2.3; Fla. Stat. 501.171(2) for employee personal information |
| Also checked | FAR 52.204-25 and 52.204-23; CIP-013-2 direct applicability; the four requirements in the vertical registry (C-CRITICAL-MFG-R01 to R04) |
| Sources read | eCFR (version 2026-09-23) for FAR 4.1903, 4.2004, 4.2105, 52.204-21, -23, -25 and 13 CFR 121.201; CIRCIA NPRM text (89 FR 23644); Federal Register API (2026-10-05); CIP-013-2 and CIP-013-3 pages on nerc.com; the SP 800-82 Rev. 4 draft page on csrc.nist.gov; Fla. Stat. 501.171 (2026) |
| Assessment dates | 2026-07-13 to 2026-07-24 (shop walkthrough and FAR 52.204-25 reasonable inquiry 2026-07-14) |
| Assessors | Office Manager (Security Coordinator) with the MSP lead technician, the Owner, and the Shop Manager |
| Approved | 2026-08-31 by the Owner |

## 1. Applicability
Applicability comes first, because for a 7-person shop the most useful finding is which duties are real and which are not.

### 1.1 No binding sector cyber rule
Critical manufacturing has no sector-wide federal cybersecurity regulation. The vertical registry lists four requirements, and each was checked against the shop's facts:

| ID | Requirement | Applies? | Why |
|---|---|---|---|
| C-CRITICAL-MFG-R01 | CIRCIA, proposed 6 CFR Part 226 | **Not yet** | Proposed only; no final rule in the Federal Register as of 2026-10-05. **Size would not protect the shop if it is finalized as proposed.** Proposed 226.2(a) covers entities above the SBA size standard (the shop is far below 800 employees), but proposed 226.2(b)(3) separately covers any entity that "owns or has business operations that engage in" electrical equipment, appliance, and component manufacturing, regardless of size. The proposal would require reports to CISA within 72 hours of a reasonable belief that a covered cyber incident occurred and within 24 hours of a ransom payment (proposed 226.5). Row G-062 records readiness only |
| C-CRITICAL-MFG-R02 | ICTS connected vehicles rule, 15 CFR Part 791 Subpart D | No | No vehicles or vehicle systems (G-063) |
| C-CRITICAL-MFG-R03 | EAR, 15 CFR Parts 730-774 | No | The shop has never exported (G-064). Recheck before any storm work or sale outside the United States |
| C-CRITICAL-MFG-R04 | DFARS 252.204-7012 | No | No DoD contracts or subcontracts; the federal order is civilian with no DFARS clauses, so SP 800-171 and CMMC are not triggered (G-065) |

### 1.2 NERC CIP-013 binds the cooperative, not the shop
**CIP-013-2** (Cyber Security, Supply Chain Risk Management) is "Mandatory Subject to Enforcement" on nerc.com, effective 2022-10-01. Its section 4.1 lists the Responsible Entities it applies to, such as Transmission Owners and Generator Owners. The shop is not NERC-registered (G-061, Not applicable).

The standard reaches the shop through one customer. CIP-013-2 Requirement R1 Part 1.2 makes each Responsible Entity's procurement process address vendor notification of incidents (1.2.1), coordination of responses (1.2.2), vendor notification when remote or onsite access should no longer be granted (1.2.3), vulnerability disclosure (1.2.4), software integrity (1.2.5), and vendor remote access (1.2.6). The G&T cooperative's exhibit takes the three topics that fit a service vendor with substation badges and turns them into contract terms: **72-hour incident notice, response coordination, and 1-business-day access notice.** Those deadlines come from the contract, not from NERC. The shop supplies no software, firmware, or remote access, so Parts 1.2.4 to 1.2.6 are not in its exhibit. Rows G-057 to G-059 assess the exhibit.

**Watch item:** **CIP-013-3** is "Subject to Future Enforcement" on nerc.com, with a FERC order date of 2026-03-19 and an effective date of 2028-07-01. The cooperative may revise its exhibit before then.

### 1.3 Federal purchase order clauses
The shop won one civilian federal purchase order on 2026-03-10 (rewind two 750 kVA units and supply a spare, to agency specifications, so not COTS).
- **FAR 52.204-21 applies.** FAR 4.1903 prescribes the clause "when the contractor or a subcontractor at any tier may have Federal contract information residing in or transiting through its information system." The agency's site drawings, unit records, delivery schedule, and the shop's test reports for those units are FCI, and they sit in email, the shared drive, the ERP, and the test PC. The 15 basic safeguards, (b)(1)(i) to (xv), and the flow-down in (c) are rows G-038 to G-054. The clause has **no incident reporting duty**.
- **FAR 52.204-25 applies.** FAR 4.2105(b) prescribes it "in all solicitations and contracts." Paragraph (b)(2) bars agencies from contracting with an entity that uses covered telecommunications or video surveillance equipment, "regardless of whether that use is in performance of work under a Federal contract." Paragraph (d) requires a report within one business day of identification and more information within 10 business days (G-055).
- **FAR 52.204-23 applies** (FAR 4.2004: "in all solicitations and contracts"). Report within 3 business days of identifying a Kaspersky covered article. None found (G-056, Met).

### 1.4 Florida
Fla. Stat. 501.171(2) requires every covered entity to "take reasonable measures to protect and secure data in electronic form containing personal information." The shop holds HR and payroll files for 7 current and about 15 former employees (G-060). The breach notice duties in 501.171(3) to (6) drive the P08 notification matrix and are not analyzed row by row.

### 1.5 Why CSF 2.0 with SP 800-82 Rev. 3 is the benchmark
With no binding cyber rule, the shop needs a yardstick that covers both the office and the shop floor (test bay, drying oven, winding machine). CSF 2.0 is sector-neutral, is what the P08 runbook follows (SP 800-61 Rev. 3 is a CSF 2.0 Community Profile), and is the language the cooperative's questionnaire uses. SP 800-82 Rev. 3 supplies OT guidance for each outcome. Two cautions:
- SP 800-82 Rev. 3 Section 6 is organized by **CSF 1.1** categories. This analysis cites SP 800-82 Rev. 3 by **section number only** and uses CSF 2.0 IDs for the outcomes.
- **SP 800-82 Rev. 4 is an initial public draft only** (published 2026-09-21; comments due 2026-11-30). Rev. 3 remains the final guide used here.

**Scope at this size.** The 37 CSF 2.0 subcategories (G-001 to G-037) cover all 22 CSF 2.0 categories and were chosen for a shop with a flat network, OEM remote access, and duties to a utility customer. This is not a full 106-subcategory profile.

**Target:** CSF Tier 2 (Risk Informed) by the end of 2027, with the High gaps closed first.

## 2. Method
1. **Requirements.**
   - CSF rows use the subcategory text from `00_universal-framework/frameworks/csf2_core.csv`, plus the SP 800-82 Rev. 3 section that gives OT guidance.
   - FAR rows follow each clause's own paragraph structure and quote the public-domain text briefly.
   - Exhibit rows follow the exhibit's sections, each tied to its CIP-013-2 Part.
2. **Crosswalk.**
   - CSF rows use the **official** NIST CSF 2.0 to SP 800-53 Rev. 5.2.0 mapping (`00_universal-framework/crosswalks/csf2_to_sp800-53r5.csv`). Where only part of a long mapping is listed, the `crosswalk_source` column says "subset." Where an OT control was added from the SP 800-82 Rev. 3 overlay (for example MA-4 on PR.AA-03), the column names it as an author addition.
   - FAR, exhibit, Florida, and applicability rows are **author mappings**, labeled as such.
3. **Documentary evidence.** Each status rests on a named document or record: the federal purchase order and the cooperative agreement, the ERP user and role lists, the suite user export, sharing report, and permission report, the MSP's device list, patch report, antivirus export, encryption report, and backup job report, the firewall rule export, the Wi-Fi settings, the reasonable inquiry worksheet, and the leaver record for the former Field Service Technician. Interviews covered all 7 employees and the MSP lead technician.
4. **Status.** Met, Partially met, Not met, or Not applicable **as of the end of fieldwork (2026-07-24)**. One exception: G-049 (FAR (b)(1)(xi)) was re-rated on 2026-08-12 after P07 testing found the test PC exposed to the internet. Actions completed since fieldwork are noted in the remediation column but do not change the status. Gaps were rated with the P01 risk scale.

## 3. Results summary
| Section | Met | Partially met | Not met | N/A | Rows |
|---|---|---|---|---|---|
| **A. CSF 2.0 with SP 800-82 Rev. 3 (benchmark)** | | | | | |
| Govern | 0 | 4 | 6 | 0 | 10 |
| Identify | 1 | 0 | 5 | 0 | 6 |
| Protect | 0 | 8 | 2 | 0 | 10 |
| Detect | 0 | 1 | 3 | 0 | 4 |
| Respond | 0 | 0 | 4 | 0 | 4 |
| Recover | 0 | 0 | 3 | 0 | 3 |
| **Subtotal CSF** | **1** | **13** | **23** | **0** | **37** |
| **B. FAR 52.204-21 (applicability, (b)(1)(i)-(xv), (c))** | 1 | 13 | 2 | 1 | 17 |
| **C. FAR 52.204-25 and 52.204-23** | 1 | 1 | 0 | 0 | 2 |
| **D. Cooperative exhibit (CIP-013-2 R1.2.1-1.2.3 flow-down)** | 0 | 0 | 3 | 0 | 3 |
| **E. Fla. Stat. 501.171(2)** | 0 | 1 | 0 | 0 | 1 |
| **F. Direct applicability (CIP-013-2, R01 to R04)** | 0 | 0 | 0 | 5 | 5 |
| **Total** | **3** | **28** | **28** | **6** | **65** |

Of the 56 unmet or partially met rows, **17 are rated High, 30 Moderate, and 9 Low**:
- CSF: 12 High, 18 Moderate, 6 Low.
- FAR clauses: 3 High, 11 Moderate, 2 Low.
- Cooperative exhibit: 2 High, 1 Moderate.
- Florida: 1 Low.

**Reading the results.**
- **The FAR safeguards are mostly partly there.** MFA on email, MSP antivirus and patching, and a locked office mean 1 of the 15 safeguards is met and 12 are partly met. What pulls them down is the same short list: shared logins, the unsupported test PC, open sharing links, and no internal network boundary.
- **The shop floor is joined to everything.** The test PC, the oven HMI, the camera recorder, and visitors share the office network, the test PC was reachable from the internet, and the oven OEM can connect at any time. That is why Protect has no Met rows and Respond and Recover have none at all.
- **The sharpest exposure is the contract nobody read.** The cooperative exhibit has two deadlines (72 hours and 1 business day), and the shop already missed one by more than two months.

## 4. Priority gaps
| Gap | Citation (row) | Risk level | Action | Owner | Target |
|---|---|---|---|---|---|
| Exhibit duties unknown; access notice missed | Exhibit secs. 1, 3 (G-057, G-059); CSF GV.OC-03, RS.CO-02 (G-001, G-033) | High | Obligations list; notice step in the leaver checklist; 72-hour notice template | Office Manager | 2026-09-30 |
| Test PC exposed to the internet; no external scanning | FAR (b)(1)(xi) (G-049); CSF ID.RA-01 (G-014) | High | Rule removed 2026-08-11; approval rule for port forwarding; quarterly external scan | Office Manager | 2026-09-30 |
| One flat network for office, shop equipment, and visitors | CSF PR.IR-01 (G-025); FAR (b)(1)(x) (G-048) | High | Office, shop equipment, and guest networks | Office Manager (MSP performs) | 2026-11-30 |
| Oven OEM modem always on; MSP and OEM activity unseen | CSF PR.AA-03, DE.CM-06 (G-018, G-028) | High | Modem off except approved sessions; MSP session report | Shop Manager; Office Manager | 2026-10-31 |
| ERP without MFA; MSP shared firewall login | CSF PR.AA-03 (G-018) | High | Enforce ERP MFA; named MSP logins with MFA | Office Manager | 2026-09-30 |
| Unsupported test PC with no backup | CSF PR.PS-02, PR.DS-11 (G-024, G-023); FAR (b)(1)(xii) (G-050) | High | Nightly database copy; replacement or supported operating system | Shop Manager | 2026-12-31 |
| No incident plan; no coordination with MSP and insurer | CSF ID.IM-04, RS.MA-01 (G-016, G-031) | High | P08 runbook (approved 2026-08-31); tabletop | Office Manager | 2026-11-30 |
| Backups never tested | CSF RC.RP-03 (G-036) | High | First restore test; quarterly after | Office Manager (MSP performs) | 2026-09-30 |
| Vendors with access have no security terms | CSF GV.SC-05 (G-009) | High | MSP amendment; OEM terms; AI data processing addendum | Owner | 2026-12-31 |
| Camera recorder of unknown origin | FAR 52.204-25(b)(2) (G-055) | Moderate | Documented replacement; purchasing check | Owner | 2026-10-31 |
| Public sharing links to FCI | FAR (b)(1)(iv) (G-042) | Moderate | Remove links; turn off anyone-with-the-link sharing | Office Manager | 2026-09-30 |

The full list, with evidence, is in `gap-analysis.csv`. Every High and Moderate gap is carried into the risk register (P01) and, where the control was assessed, the POA&M (P07).

## 5. Remediation plan
The plan fits a 7-person shop: most actions are one-page procedures, settings in SaaS consoles, or MSP work, not new systems. The MSP performs the technical work under the Office Manager's direction. Costs are in the P01 treatment summary.

| Phase | Due | Actions | Rows closed |
|---|---|---|---|
| 1. Contracts and identity | 2026-09-30 | Obligations list; exhibit notice steps; leaver checklist; ERP MFA and separate admin accounts; named MSP logins with MFA; remove public links; port forwarding approval rule; first restore test; ERP export; AI data processing addendum | G-001, G-003, G-004, G-005, G-033, G-036, G-039, G-041, G-042, G-044, G-049, G-057, G-059 |
| 2. Visibility and hardening | 2026-10-31 | Device, vendor, and data inventory; FCI folder and labels; monthly log review and POA&M meeting; modem and MSP session records; desktop encryption; training and phishing simulations; modem off except approved sessions; visitor sign-in; disposal records; camera replacement | G-007, G-008, G-011, G-013, G-018, G-019, G-020, G-021, G-022, G-028, G-030, G-038, G-040, G-045, G-047, G-053, G-055, G-060 |
| 3. Separation and response | 2026-11-30 | Three networks; network diagram; contingency plan and recovery order; OT program copies; tabletop with the MSP; isolation steps; customer update templates | G-012, G-016, G-023, G-025, G-031, G-034, G-035, G-037, G-048, G-058 |
| 4. Detection and replacement | 2026-12-31 | EDR; log forwarding; quarterly scans; MSP and OEM terms; vendor review; test PC replacement or supported operating system | G-009, G-010, G-014, G-017, G-024, G-027, G-029, G-032, G-043, G-050 to G-052 |
| 5. Annual cycle | 2027-05-31 to 2027-07-31 | BIA and hurricane checklist update (May); generator decision; risk and gap analysis update (July) | G-002, G-026 |

Items already closed by approval on 2026-08-31: adopted policies (G-006) and the P08 runbook (part of G-016). They remain "Not met" in the CSV because the status reflects fieldwork.

**Progress check.** The Office Manager reports progress to the Owner at a monthly 30-minute meeting, using the P07 POA&M as the tracker (G-007).

## 6. Pending and proposed changes (none treated as current obligations)
- **CIRCIA final rule** (C-CRITICAL-MFG-R01). The 2026-08-14 Unified Agenda notices mention CIRCIA, but no final rule was published as of 2026-10-05. If the sector criterion survives, the shop would have 72-hour and 24-hour reporting duties to CISA. The P08 runbook already includes a voluntary CISA report, and the notification matrix carries CIRCIA as "not yet required."
- **NIST SP 800-82 Rev. 4 initial public draft** (2026-09-21; comments due 2026-11-30). Update the section references in G-001 to G-037 when Rev. 4 is final.
- **CIP-013-3** takes effect 2028-07-01. Watch for a revised exhibit from the cooperative.
- **FAR overhaul.** The Revolutionary FAR Overhaul proposed rule (FR Doc. 2026-12559, 91 FR 37550, June 23, 2026; comments closed 2026-07-23) proposes revisions to FAR parts 1, 2, 4, 33, 39, 40, 52, and 53, which include the parts where the clauses above are prescribed (part 4) and printed (part 52). It is proposed only. The shop follows the clauses in its awarded order and will check any modification or new solicitation for changed clause numbers or text.
