# Regulatory Gap Analysis: Cris Santos Company | Critical Manufacturing | Mid-Market

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (PE-backed power and distribution transformer manufacturer, Florida) |
| Tier / Vertical | Mid-Market / Critical Manufacturing (NAICS 335311) |
| Primary benchmark | NIST Cybersecurity Framework (CSF) 2.0 (NIST CSWP 29, February 26, 2024) with NIST SP 800-82 Rev. 3, *Guide to Operational Technology (OT) Security* (September 2023) as the OT implementation guide. **Voluntary**: no binding sector-wide cyber rule applies. Assessed as a **full profile of all 106 CSF 2.0 subcategories** |
| Secondary obligations (binding by contract) | FAR 52.204-21 in the three federal contracts; FAR 52.204-23, 52.204-25, and 52.204-30; the Supplier Cyber Security Addenda in 31 utility contracts, which flow down the six topics of NERC CIP-013-2 Requirement R1 Part 1.2 |
| Also checked | The four requirements in the vertical registry (C-CRITICAL-MFG-R01 to R04); NERC CIP-013-2 direct applicability; EAR recordkeeping; the FMS subscription agreements (assessed in P09) |
| Sources read | eCFR (version 2026-09-23) for FAR 4.1903, 4.2306, 52.204-21, -23, -25, -30, 13 CFR 121.201, and 15 CFR 762.6; the CIRCIA NPRM text (89 FR 23644); the CIP-013-2 and CIP-013-3 pages on nerc.com (checked 2026-10-05); the SP 800-82 Rev. 3 PDF and the SP 800-82 Rev. 4 draft page on csrc.nist.gov; Federal Register API (2026-10-05) |
| Assessment dates | 2026-07-06 to 2026-07-31 (Plant 1 walkthrough 2026-07-14; Plant 2 walkthrough 2026-07-15 and 2026-07-16; covered equipment inquiry 2026-07-20); evidence refreshed with P07 results through 2026-08-21 |
| Assessors | Security Manager and the GRC analyst with the OT Security Engineer and the vCISO, with the General Counsel and the Contracts and Trade Compliance Manager for contract rows; reviewed by the co-sourced internal audit firm |
| Approved | Chief Operating Officer, 2026-09-15 |

## 1. Applicability
At this size more rules come close to the company, so applicability comes first. The most useful findings are still what does **not** bind it, and which contract terms do.

### 1.1 No binding sector cyber rule
Critical manufacturing has no sector-wide federal cybersecurity regulation. The vertical registry lists four requirements, and each was checked against the company's facts:

| ID | Requirement | Applies? | Why |
|---|---|---|---|
| C-CRITICAL-MFG-R01 | CIRCIA, proposed 6 CFR Part 226 | **Not yet** | Proposed only. No final rule appears in the Federal Register as of 2026-10-05 (the latest CIRCIA items are the 2026-08-14 Unified Agenda notices). **If finalized as proposed, the company would be covered twice over:** under proposed 226.2(a), because it exceeds the SBA size standard for its NAICS code (850 employees against 800 for NAICS 335311 in 13 CFR 121.201), and under proposed 226.2(b)(3)(iii), because it engages in electrical equipment, appliance, and component manufacturing (NAICS subsector 335) regardless of size. The proposal would require reports to CISA within 72 hours of a reasonable belief that a covered cyber incident occurred and within 24 hours of a ransom payment. Row G-134 records readiness only |
| C-CRITICAL-MFG-R02 | ICTS connected vehicles rule, 15 CFR Part 791 Subpart D | No | The company makes no connected vehicles or vehicle systems (G-135) |
| C-CRITICAL-MFG-R03 | EAR, 15 CFR Parts 730-774 | **Yes, narrowly** | The company exports EAR99 transformers to utilities in the Caribbean and Central America. The cyber-relevant duty is keeping export records for 5 years (15 CFR 762.6(a)); the ERP keeps them for 7 (G-136, Met) |
| C-CRITICAL-MFG-R04 | DFARS 252.204-7012 | No | No DoD contracts or subcontracts. The three federal contracts are civilian and contain no DFARS clauses, so SP 800-171 and CMMC are not triggered. A bid review gate stops any bid that would flow the clause down (G-137) |

### 1.2 NERC CIP-013 binds the utilities, not the company
**CIP-013-2** (Cyber Security, Supply Chain Risk Management) is "Mandatory Subject to Enforcement" on nerc.com, effective 2022-10-01. Its section 4.1 lists the Responsible Entities it applies to: Balancing Authorities, certain Distribution Providers, Generator Operators and Owners, Reliability Coordinators, and Transmission Operators and Owners. The company is none of these and is not NERC-registered (G-133, Not applicable).

The standard still reaches the company through its customers. Requirement R1 Part 1.2 makes each Responsible Entity's procurement process address six topics: (1.2.1) vendor notification of vendor-identified incidents, (1.2.2) coordination of responses, (1.2.3) vendor notification when access should no longer be granted, (1.2.4) vendor disclosure of known vulnerabilities, (1.2.5) verification of software integrity and authenticity, and (1.2.6) coordination of vendor-initiated remote access. Thirty-one utilities have turned those topics into contract duties with deadlines: incident notice within 48 hours (22 utilities) or 24 hours (9 utilities), access notice within 1 business day, and vulnerability disclosure within 30 days. **Those deadlines come from the contracts, not from NERC.** Rows G-127 to G-132 assess them. At this size the addenda cover more than the TMUs: they also cover the configuration software the company writes and, for the FMS subscribers that signed them, the FMS.

**Watch item:** **CIP-013-3** is "Subject to Future Enforcement" on nerc.com, with a FERC order dated 2026-03-19 and an effective date of 2028-07-01. CIP-013-2 shows an inactive date of 2028-06-30. Expect utilities to revise their addenda before then.

### 1.3 Federal contract clauses
The company holds three civilian federal contracts, all built to agency specifications (not COTS).
- **FAR 52.204-21 applies.** FAR 4.1903 prescribes the clause "when the contractor or a subcontractor at any tier may have Federal contract information residing in or transiting through its information system." Agency specifications and drawings, delivery schedules, test reports, and correspondence are FCI. They sit in the ERP, email, and labeled project sites, and, as this assessment found, on the Plant 2 file server and in the Plant 2 MES and test PCs (federal power transformers are built and tested at Plant 2). The clause's 15 safeguards, (b)(1)(i) to (xv), and the flow-down in (c) are rows G-107 to G-123. The clause contains **no incident reporting duty**.
- **FAR 52.204-25 applies.** FAR 4.2105 prescribes it in all solicitations and contracts. Paragraph (b)(2) bars agencies from contracting with an entity that **uses** covered telecommunications or video surveillance equipment, "regardless of whether that use is in performance of work under a Federal contract." Paragraph (d) requires a report within 1 business day of identification and more information within 10 business days (G-124, Met after the 2024 Plant 2 camera replacement).
- **FAR 52.204-23 applies** (Kaspersky covered articles; report within 3 business days, then 10 business days) (G-125, Met).
- **FAR 52.204-30 applies** (FASCSA orders). It is in each contract's clause list. Paragraph (c)(1) requires a SAM.gov review "at least once every three months"; reports are due within 3 business days, then 10 business days (G-126, Partially met: one quarterly review was missed).

### 1.4 FMS subscription agreements
The 14 FMS subscription agreements commit to 99.5% monthly availability and confidentiality of utility data, and two require a SOC 2 Type 2 report by 2027-12-31. These are contract commitments, assessed against the Trust Services Criteria in P09 rather than here. The CSF rows that cover the FMS (for example PR.PS-06, DE.CM-09, RC.RP-01) cite them in their evidence.

### 1.5 Why CSF 2.0 with SP 800-82 Rev. 3, as a full profile
With no binding cyber rule, the company needs one yardstick that covers IT, two plants, its products, and a cloud service. CSF 2.0 is sector-neutral, is what both P08 runbooks follow (SP 800-61 Rev. 3 is a CSF 2.0 Community Profile), and is the language utilities use in supplier questionnaires. SP 800-82 Rev. 3 supplies the OT guidance for each outcome. At mid-market size the company assesses **all 106 subcategories** (G-001 to G-106), not a selection, because its scope now includes product development (PR.PS-06), a customer-facing service, and an acquired plant. Two cautions:
- SP 800-82 Rev. 3 Section 6 is organized by **CSF 1.1** categories. This analysis cites SP 800-82 Rev. 3 by **section number only** and uses CSF 2.0 IDs for the outcomes.
- **SP 800-82 Rev. 4 is an initial public draft only** (published 2026-09-21; comments due 2026-11-30). Rev. 3 remains the final guide used here.

**Target:** CSF Tier 3 (Repeatable) for Govern, Identify, and Protect by the end of 2027, and Plant 2 at parity with Plant 1 by 2027-06-30.

## 2. Method
1. **Requirements.**
   - CSF rows use the subcategory text from `00_universal-framework/frameworks/csf2_core.csv`, plus the SP 800-82 Rev. 3 section that gives OT guidance (author references by section number).
   - FAR rows follow each clause's own paragraph structure and quote the public-domain text briefly.
   - Utility addendum rows follow the addendum sections, each tied to its CIP-013-2 Part.
2. **Crosswalk.**
   - CSF rows use the **official** NIST CSF 2.0 to SP 800-53 Rev. 5.2.0 mapping (`00_universal-framework/crosswalks/csf2_to_sp800-53r5.csv`), listing a subset of the controls in `sp800_53_controls`. Three rows add controls that the SP 800-82 Rev. 3 OT guidance points to, and the `crosswalk_source` column labels them as author additions (PR.PS-03, DE.CM-09, RS.AN-07).
   - FAR, addendum, and applicability rows are **author mappings**, labeled as such. No official NIST mapping exists for them.
3. **Evidence.**
   - Interviews: CEO, COO, CFO, General Counsel, vCISO, IT Director, Security Manager, OT Security Engineer, Director of Manufacturing Engineering, both Plant Managers and Controls Leads, VP Engineering, Director of Digital Services, Director of Quality, Director of Supply Chain, Director of Field Service, Contracts and Trade Compliance Manager, HR Director, and the MSSP service lead.
   - Documents: policies, the 2024 IT incident and DR plans, contracts and all 31 addenda, the 3 federal contracts, the obligations register, the Plant 1 OT DMZ design.
   - Configuration exports: firewalls, identity provider, ERP roles, backup jobs, EDR console, SIEM sources, OT sensor inventory, build server.
   - Walkthroughs of both plants.
4. **Evidence sampling.** Where a requirement operates many times, a sample was tested rather than the whole population. Samples were drawn at random from system-generated populations, sized with the co-sourced internal audit firm's attribute sampling table (25 items for a control operating many times a year; 5 to 10 for monthly or weekly controls; the full population when it is small). The same samples were reused in P07 where the controls overlap.

   | Population (12 months to 2026-06-30 unless noted) | Size | Sample | Rows |
   |---|---|---|---|
   | Terminations | 214 | 25 | G-016 |
   | New hires | 236 | 25 | G-016, G-054 |
   | Field technician departures with utility access (2026) | 5 | 5 | G-129 |
   | Vulnerability disclosures to utilities (2026) | 2 | 2 | G-130 |
   | Utility addenda | 31 | 31 | G-003, G-127 to G-132 |
   | Tier 1 suppliers | 22 | 7 | G-028 |
   | Purchase orders (accounts payable) | about 9,000 | 20 | G-026 |
   | Plant 2 MES changes | about 60 | 15 | G-045 |
   | ERP changes | about 140 | 15 | G-045 |
   | Critical vulnerability findings (Q1-Q2 2026) | 50 | 50 | G-039 |
   | Backup job days (July 2026) | 31 | 31 | G-064 |
   | Plant 1 OEM remote sessions | 212 | 20 | G-078 |
   | Plant 2 visitor log entries (July 2026) | 40 | 40 | G-058, G-116 |
   | Incidents | 41 | 10 | G-051, G-086, G-087 |
   | Plant 2 OT devices (walkdown) | 30 | 30 | G-032 |
   | TMU firmware lots received | about 60 | 20 | G-047 |
   | Media disposals | 10 | 10 | G-114 |

   Each `evidence` cell names the sample and its result.
5. **Status.** Each row was rated Met, Partially met, Not met, or Not applicable, as of the end of fieldwork. Gaps were rated with the P01 risk scale.

## 3. Results summary
| Section | Met | Partially met | Not met | N/A | Rows |
|---|---|---|---|---|---|
| **A. CSF 2.0 with SP 800-82 Rev. 3 (benchmark)** | | | | | |
| Govern | 7 | 24 | 0 | 0 | 31 |
| Identify | 7 | 12 | 2 | 0 | 21 |
| Protect | 5 | 16 | 1 | 0 | 22 |
| Detect | 2 | 9 | 0 | 0 | 11 |
| Respond | 1 | 12 | 0 | 0 | 13 |
| Recover | 0 | 5 | 3 | 0 | 8 |
| **Subtotal CSF** | **22** | **78** | **6** | **0** | **106** |
| **B. FAR 52.204-21 (applicability, (b)(1)(i)-(xv), (c))** | 4 | 13 | 0 | 0 | 17 |
| **C. FAR 52.204-25, 52.204-23, 52.204-30** | 2 | 1 | 0 | 0 | 3 |
| **D. Utility addenda (CIP-013-2 R1.2 flow-down)** | 0 | 6 | 0 | 0 | 6 |
| **E. Direct applicability (CIP-013-2, R01 to R04)** | 1 | 0 | 0 | 4 | 5 |
| **Total** | **29** | **98** | **6** | **4** | **137** |

Of the 104 unmet or partially met rows, **32 are rated High, 52 Moderate, and 20 Low**:
- CSF: 28 High, 41 Moderate, 15 Low.
- FAR clauses: 0 High, 10 Moderate, 4 Low.
- Utility addenda: 4 High, 1 Moderate, 1 Low.

**Reading the results.**
- **A defined program with gaps in scale.** Governance, risk management, threat intelligence, encryption, and IT monitoring are Met. Most Partially met rows describe a control that works at HQ, in the cloud, and at Plant 1 but not at Plant 2. That pattern accounts for most of the 98 Partially met rows.
- **The six Not met rows are about recovery and building software:** no OT life-cycle plan (ID.AM-08), no plans that cover the plants and products (ID.IM-04), no secure development practice (PR.PS-06), no recovery priorities (RC.RP-02), no verification of restored plant systems (RC.RP-05), and no public messaging process (RC.CO-04).
- **The customer duties are the sharpest exposure.** All six addendum rows are only Partially met, and three 2026 notices were late. Four of the six are rated High.
- **FAR 52.204-21 is mostly in place for IT.** Every Partially met FAR row traces to Plant 2 systems that hold federal drawings or test data.

## 4. Priority gaps
| Gap | Citation (row) | Risk level | Action | Owner | Target |
|---|---|---|---|---|---|
| Plant 2 has no boundary between office and plant; MES dual-homed | CSF PR.IR-01, RS.MI-01 (G-071, G-097); FAR (b)(1)(x) (G-117) | High | Interim isolation points 2026-11-30; Plant 2 OT DMZ and zones | OT Security Engineer | 2027-06-30 |
| Least privilege at Plant 2: MES service account in corporate Domain Admins (P07); two-way trust | CSF PR.AA-05 (G-057) | High | Rights removed 2026-08-19; one-way trust 2026-10-31; retire the Plant 2 domain | Security Manager | 2027-03-31 |
| Addendum notices unreliable; product vulnerability intake missing | Addendum secs. 1, 3, 4 (G-127, G-129, G-130); CSF GV.OC-03, RS.CO-02, ID.RA-08 (G-003, G-095, G-046) | High | Notice procedures and drills; automated access notices; product vulnerability intake with 30-day tracking | General Counsel; VP Engineering; Director of Field Service | 2026-11-30 to 2026-12-31 |
| Code signing key exposed; no SBOM; no secure development practice | Addendum sec. 5 (G-131); CSF ID.RA-09, PR.PS-06 (G-047, G-070) | High | Hardware-backed signing; SBOM; STD-10 aligned to the NIST SSDF | VP Engineering | 2026-12-15 to 2027-03-31 |
| Plant 2 OEM remote access always on, shared, unlogged | CSF PR.AA-03, DE.CM-06 (G-055, G-078) | High | Routers off between sessions from 2026-10-15; gateway | OT Security Engineer | 2026-12-31 |
| Recovery unproven; plans miss plants and products | CSF ID.IM-04, PR.DS-11, RC.RP-02, RC.RP-03, RC.RP-05 (G-052, G-064, G-100, G-101, G-103) | High | Contingency plan with the BIA order; quarterly restore tests; Plant 2 OT backups; restart verification checklist | IT Director; Director of Manufacturing Engineering | 2026-11-30 to 2027-03-31 |
| Plant-side logs and Plant 2 networks unmonitored | CSF PR.PS-04, DE.CM-01, DE.CM-09 (G-068, G-075, G-079) | High | SIEM onboarding; Plant 2 OT sensor; allowlisting | Security Manager; OT Security Engineer | 2027-01-31 to 2027-03-31 |
| Plant 2 OT inventory and unsupported systems | CSF ID.AM-01, ID.AM-08, ID.RA-01, PR.PS-02 (G-032, G-038, G-039, G-066) | High | Passive inventory and vulnerability matching; OT life-cycle plan | OT Security Engineer; Director of Manufacturing Engineering | 2027-01-31 to 2027-12-31 |
| Suppliers and OEMs not assessed or bound by security terms | CSF GV.SC-05, GV.SC-07, GV.SC-08 (G-026, G-028, G-029) | High | STD-03; OEM security schedule; annual Tier 1 reviews | Director of Supply Chain; Security Manager | 2026-11-30 to 2027-06-30 |
| FCI on Plant 2 systems; FASCSA review lapsed; one subcontract without flow-down | FAR 52.204-21(a)-(b)(1), (b)(1)(i), (c); 52.204-30(c) (G-107, G-108, G-123, G-126) | Moderate | Move drawings; add Plant 2 MES to scope; quarterly SAM.gov task; amend the purchase order | Contracts and Trade Compliance Manager | 2026-10-31 to 2026-12-31 |

High and Moderate gaps are carried into the risk register (P01) and the POA&M (P07). The full list is in `gap-analysis.csv`.

## 5. Program roadmap
| Phase | Window | Outcomes | Rows closed (examples) |
|---|---|---|---|
| **1. Stabilize** | 2026 Q4 | Plant 2 domain trust one-way; routers off between sessions; access points removed; notice procedures, drills, and automated access notices; product vulnerability intake; hardware-backed signing; crisis and OT tabletops; first ERP restore test; FCI moved off the Plant 2 file server; quarterly SAM.gov task; STD-03, STD-07, STD-09 issued | G-003, G-046, G-052, G-057, G-095, G-108, G-123, G-126, G-127, G-129 to G-131 |
| **2. Build** | 2027 Q1 | SIEM onboarding of MES, historians, integration platform, and FMS; Plant 2 OT sensor and inventory; FIDO2 for all privileged accounts; Plant 2 OT backups; first OT restore tests; contingency plan approved; secure development standard and SBOMs; remaining standards issued | G-032, G-039, G-055, G-064, G-068, G-070, G-075, G-100, G-101 |
| **3. Segment and prove** | 2027 Q2 | Plant 2 OT DMZ and zones; Plant 2 OEMs through the gateway; allowlisting at Plant 2; Plant 2 moves to the Plant 1 MES; BIA RTOs demonstrated for High processes; FMS SOC 2 observation period starts 2027-04-01 (P09) | G-071, G-078, G-079, G-097, G-103, G-117, G-120 |
| **4. Sustain** | 2027 Q3-Q4 | Annual risk assessment (July 2027); OT life-cycle replacements; annual Tier 1 supplier reviews; second annual assessment; prepare for CIP-013-3 addendum revisions | G-028, G-038, G-066 |

Progress is reported quarterly to the audit committee as the count of rows moving from Partially met or Not met to Met.

## 6. Pending and proposed changes (none treated as current obligations)
- **CIRCIA final rule** (C-CRITICAL-MFG-R01). The Unified Agenda had targeted September 2026, but nothing was published as of 2026-10-05. If the proposal is finalized as written, the company would be covered under both the size criterion and the manufacturing criterion and would have 72-hour and 24-hour reporting duties to CISA. Both P08 runbooks include a voluntary CISA report, and the notification matrix carries CIRCIA as "not yet required."
- **NIST SP 800-82 Rev. 4 initial public draft** (2026-09-21; comments due 2026-11-30). Update the section references in G-001 to G-106 when Rev. 4 is final.
- **CIP-013-3** takes effect 2028-07-01. Watch for addendum revisions from the 31 utilities.
- **FAR overhaul.** The Revolutionary FAR Overhaul proposed rule for parts 1, 2, 4, 33, 39, 40, and 53 (FR Doc. 2026-12559, published 2026-06-23) would move information security clauses into a new FAR part 40. It is proposed only. The company follows the clauses in its awarded contracts and will check any modification or new solicitation for the new numbering.
