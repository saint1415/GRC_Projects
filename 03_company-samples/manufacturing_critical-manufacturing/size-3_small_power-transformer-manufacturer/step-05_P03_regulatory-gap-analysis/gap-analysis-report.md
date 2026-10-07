# Regulatory Gap Analysis: Cris Santos Company | Critical Manufacturing | Small

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (power and distribution transformer manufacturer, Florida) |
| Tier / Vertical | Small / Critical Manufacturing (NAICS 335311) |
| Primary benchmark | NIST Cybersecurity Framework (CSF) 2.0 (NIST CSWP 29, February 26, 2024) with NIST SP 800-82 Rev. 3, *Guide to Operational Technology (OT) Security* (September 2023) as the OT implementation guide. **Voluntary**: no binding sector-wide cyber rule applies |
| Secondary obligations (binding by contract) | FAR 52.204-21 in the company's one federal contract; the Supplier Cyber Security Addenda in 12 utility contracts, which flow down the six topics of NERC CIP-013-2 Requirement R1 Part 1.2 |
| Also checked | FAR 52.204-25 and 52.204-23; the four requirements in the vertical registry (C-CRITICAL-MFG-R01 to R04); NERC CIP-013-2 direct applicability |
| Sources read | eCFR (version 2026-09-23) for FAR 4.1903, 4.2105, 52.204-21, -23, -25, -26 and 15 CFR 762.6; CIRCIA NPRM text (89 FR 23644); CIP-013-2 PDF and the CIP-013-2 and CIP-013-3 pages on nerc.com; the SP 800-82 Rev. 3 PDF and the SP 800-82 Rev. 4 draft page on csrc.nist.gov; Federal Register API (2026-09-26) |
| Assessment dates | 2026-07-13 to 2026-07-24 (plant walkthrough 2026-07-16; covered telecommunications inquiry 2026-07-20) |
| Assessors | IT Manager and Controls Engineer, with the Contracts and Compliance Manager, VP Engineering, and Field Service Manager |

## 1. Applicability
Applicability comes first, because for this company the most useful finding is what does **not** bind it.

### 1.1 No binding sector cyber rule
Critical manufacturing has no sector-wide federal cybersecurity regulation. The vertical registry lists four requirements, and each was checked against the company's facts:

| ID | Requirement | Applies? | Why |
|---|---|---|---|
| C-CRITICAL-MFG-R01 | CIRCIA, proposed 6 CFR Part 226 | **Not yet** | Proposed only. No final rule appears in the Federal Register as of 2026-09-26 (the latest CIRCIA mentions are the 2026-08-14 Unified Agenda notices). **If it is finalized as proposed, the company would be covered despite being SBA-small:** proposed 226.2(b)(3) reaches any entity that "owns or has business operations that engage in" electrical equipment, appliance, and component manufacturing, which is NAICS subsector 335 and includes 335311. The proposal would require reports to CISA within 72 hours of a reasonable belief that a covered cyber incident occurred and within 24 hours of a ransom payment. Row G-089 records readiness only |
| C-CRITICAL-MFG-R02 | ICTS connected vehicles rule, 15 CFR Part 791 Subpart D | No | The company makes no connected vehicles or vehicle systems (G-090) |
| C-CRITICAL-MFG-R03 | EAR, 15 CFR Parts 730-774 | **Yes, narrowly** | The company exports EAR99 transformers to two Caribbean utilities. The cyber-relevant duty is keeping export records for 5 years (15 CFR 762.6(a)); the ERP keeps them for 7 (G-091, Met) |
| C-CRITICAL-MFG-R04 | DFARS 252.204-7012 | No | No DoD contracts or subcontracts. The federal contract is with a civilian agency and contains no DFARS clauses, so SP 800-171 and CMMC are not triggered (G-092) |

### 1.2 NERC CIP-013 binds the utilities, not the company
**CIP-013-2** (Cyber Security, Supply Chain Risk Management) is the version in force on nerc.com, "Mandatory Subject to Enforcement" since 2022-10-01. Its section 4.1 lists the Responsible Entities it applies to: Balancing Authorities, certain Distribution Providers, Generator Operators and Owners, Reliability Coordinators, and Transmission Operators and Owners. The company is none of these and is not NERC-registered (G-088, Not applicable).

The standard still reaches the company through its customers. Requirement R1 Part 1.2 makes each Responsible Entity's procurement process address six topics: (1.2.1) vendor notification of vendor-identified incidents, (1.2.2) coordination of responses, (1.2.3) vendor notification when access should no longer be granted, (1.2.4) vendor disclosure of known vulnerabilities, (1.2.5) verification of software integrity and authenticity, and (1.2.6) coordination of vendor-initiated remote access. The transformer monitoring units (TMUs) the company ships with power transformers can sit inside medium impact BES substations, so 12 utilities have added a Supplier Cyber Security Addendum that turns those six topics into contract duties with deadlines (48-hour incident notice, 1-business-day access notice, 30-day vulnerability disclosure). **Those deadlines come from the contracts, not from NERC.** CIP-013-2 itself notes that contract terms are outside the scope of R2. Rows G-082 to G-087 assess the addendum duties.

**Watch item:** **CIP-013-3** is listed on nerc.com as "Subject to Future Enforcement," with a FERC order date of 2026-03-19 and an effective date of 2028-07-01 (Project 2016-02). The company should expect utilities to revise their addenda before then.

### 1.3 Federal contract clauses
The company won one civilian federal contract in 2025 (14 pad-mounted transformers plus 2 spares, built to agency specifications, so not COTS).
- **FAR 52.204-21 applies.** FAR 4.1903 prescribes the clause "when the contractor or a subcontractor at any tier may have Federal contract information residing in or transiting through its information system." The agency's specifications and drawings, delivery schedules, and test reports are FCI, and they sit in the ERP, PLM, email, and file shares. The clause's 15 basic safeguarding requirements, (b)(1)(i) to (xv), and the flow-down in (c) are rows G-063 to G-079. The clause contains **no incident reporting duty**.
- **FAR 52.204-25 applies.** FAR 4.2105(b) prescribes it "in all solicitations and contracts." Paragraph (b)(2) bars agencies from contracting with an entity that **uses** covered telecommunications or video surveillance equipment, "regardless of whether that use is in performance of work under a Federal contract." Paragraph (d) requires a report within one business day of identification and more information within 10 business days (G-080).
- **FAR 52.204-23 applies** (Kaspersky covered articles; report within 3 business days). No covered articles were found (G-081, Met).

### 1.4 Why CSF 2.0 with SP 800-82 Rev. 3 is the benchmark
With no binding cyber rule, the company needs a yardstick that covers both IT and the plant floor. CSF 2.0 is sector-neutral, is what the P08 runbook follows (SP 800-61 Rev. 3 is a CSF 2.0 Community Profile), and is the language utilities use in supplier questionnaires. SP 800-82 Rev. 3 supplies the OT guidance for each outcome. Two cautions:
- SP 800-82 Rev. 3 Section 6 is organized by **CSF 1.1** categories. This analysis cites SP 800-82 Rev. 3 by **section number only** and uses CSF 2.0 IDs for the outcomes.
- **SP 800-82 Rev. 4 is an initial public draft only** (published 2026-09-21; comments due 2026-11-30). Rev. 3 remains the final guide used here.

The 62 CSF 2.0 subcategories (G-001 to G-062) were selected for a transformer plant with an IT/OT boundary, remote OEM access, and product obligations to utilities. Every CSF 2.0 category is covered by at least one row, but this is not a full 106-subcategory profile.

**Target:** CSF Tier 2 (Risk Informed) by the end of 2027, with the High gaps closed first.

## 2. Method
1. **Requirements.**
   - CSF rows use the subcategory text from `00_universal-framework/frameworks/csf2_core.csv`, plus the SP 800-82 Rev. 3 section that gives OT guidance.
   - FAR rows follow the clause's own paragraph structure and quote the public-domain text briefly.
   - Utility addendum rows follow the addendum sections, each tied to its CIP-013-2 Part.
2. **Crosswalk.**
   - CSF rows use the **official** NIST CSF 2.0 to SP 800-53 Rev. 5.2.0 mapping (`00_universal-framework/crosswalks/csf2_to_sp800-53r5.csv`). Where only part of a long mapping is listed, the `crosswalk_source` column says "subset." Where an OT control from the SP 800-82 Rev. 3 overlay was added (for example MA-4 on PR.AA-03), the column names it as an author addition.
   - FAR, addendum, and applicability rows are **author mappings**, labeled as such. No official NIST mapping exists for them.
3. **Evidence.**
   - Interviews: President, VP Operations, VP Engineering, IT Manager, Controls Engineer, Plant Manager, Production Planning Manager, Quality Manager, Contracts and Compliance Manager, Field Service Manager, and HR Manager.
   - Documents: contracts and addenda, the 2021 IT handbook, the IT call list, and work instructions.
   - Configuration exports: firewall, identity provider, ERP roles, backup jobs, EDR console.
   - The plant walkthrough on 2026-07-16.
4. **Status.** Met, Partially met, Not met, or Not applicable, as of the end of fieldwork. Gaps were rated with the P01 risk scale.

## 3. Results summary
| Section | Met | Partially met | Not met | N/A | Rows |
|---|---|---|---|---|---|
| **A. CSF 2.0 with SP 800-82 Rev. 3 (benchmark)** | | | | | |
| Govern | 1 | 9 | 7 | 0 | 17 |
| Identify | 1 | 5 | 9 | 0 | 15 |
| Protect | 2 | 12 | 2 | 0 | 16 |
| Detect | 0 | 1 | 5 | 0 | 6 |
| Respond | 0 | 1 | 3 | 0 | 4 |
| Recover | 0 | 2 | 2 | 0 | 4 |
| **Subtotal CSF** | **4** | **30** | **28** | **0** | **62** |
| **B. FAR 52.204-21 (applicability, (b)(1)(i)-(xv), (c))** | 8 | 7 | 2 | 0 | 17 |
| **C. FAR 52.204-25 and 52.204-23** | 1 | 1 | 0 | 0 | 2 |
| **D. Utility addenda (CIP-013-2 R1.2 flow-down)** | 0 | 1 | 5 | 0 | 6 |
| **E. Direct applicability (CIP-013-2, R01 to R04)** | 1 | 0 | 0 | 4 | 5 |
| **Total** | **14** | **39** | **35** | **4** | **92** |

Of the 74 unmet or partially met rows, **26 are rated High, 36 Moderate, and 12 Low**:
- CSF: 21 High, 27 Moderate, 10 Low.
- FAR clauses: 1 High, 7 Moderate, 2 Low.
- Utility addenda: 4 High, 2 Moderate.

**Reading the results.**
- **Office IT is in fair shape.** MFA, EDR, and physical security are in place, so 8 of the 15 FAR 52.204-21 safeguards are met.
- **The plant floor is not.** The OT network is flat and IT can reach it freely. OEM remote access is always on with shared passwords. Nobody holds an inventory, backups, or a plan for OT. A ransomware infection in the office would reach the winding machines and ovens.
- **The customer-facing duties are the sharpest exposure.** The company signed 12 addenda that it has no process to honor. Two field technician departures went unreported, and two supplier vulnerability advisories were never passed on to utilities.

## 4. Priority gaps and roadmap
| Gap | Citation (row) | Risk level | Action | Owner | Target |
|---|---|---|---|---|---|
| Covered cameras in use; SAM representation inaccurate | FAR 52.204-25(b)(2), (d) (G-080) | High | Disconnect and replace the 4 cameras; correct the representation with counsel; purchasing check | Contracts and Compliance Manager | 2026-10-31 |
| Addendum duties unassigned; 2 supplier advisories not disclosed; departures not reported | Addendum secs. 1, 3, 4, 5 (G-082, G-084 to G-086); CSF GV.SC-02, GV.OC-03 (G-013, G-002) | High | Obligations register; disclose the 2 open advisories; access-notice step in HR checklist; firmware hashes with each shipment | Contracts and Compliance Manager; VP Engineering; Field Service Manager | 2026-09-30 to 2026-11-30 |
| Flat plant network, any-any rule, dual-homed MES | CSF PR.IR-01, RS.MI-01 (G-046, G-058) | High | OT DMZ, zoning, deny-by-default rules; documented isolation points | Controls Engineer | 2027-03-31 (isolation points 2026-11-30) |
| Always-on OEM remote access without MFA | CSF PR.AA-03, DE.CM-06 (G-034, G-051) | High | Single remote access gateway with MFA, per-session approval, recording | Controls Engineer | 2026-12-31 |
| Backups exposed and untested; OT programs not backed up | CSF PR.DS-11, RC.RP-02 (G-041, G-059) | High | Immutable separate-account backups; scheduled OT program backups; quarterly restore tests; recovery order | IT Manager | 2026-12-31 |
| No IR plan for OT; no retainer; no notice procedure | CSF ID.IM-04, RS.MA-01, RS.CO-02 (G-032, G-055, G-057) | High | POL-03 and the P08 runbook; OT-capable retainer; notification matrix | IT Manager; Controller | 2026-11-30 |
| TMU firmware not verified | CSF ID.RA-09 (G-029); addendum sec. 5 (G-086) | High | Signature or hash check on receipt and at final test | Quality Manager | 2026-11-30 |
| No OT inventory; unsupported HMIs; no OT vulnerability management | CSF ID.AM-01, ID.AM-08, ID.RA-01, PR.PS-02 (G-018, G-023, G-024, G-043) | High | OT inventory; life-cycle plan; advisory subscription; OEM-approved patch reviews | Controls Engineer | 2026-12-31 to 2027-06-30 |
| No monitoring; EDR alerts unwatched | CSF DE.CM-01, DE.CM-09 (G-049, G-052) | High | 24x7 managed detection; passive OT monitoring | IT Manager | 2027-03-31 |
| FCI on open shares; public AI use | FAR 52.204-21(b)(1)(i), (iv) (G-064, G-067) | Moderate | Restrict FCI folders; approved AI tools list | IT Manager; Contracts and Compliance Manager | 2026-10-31 |

The full list, with evidence, is in `gap-analysis.csv`. High and Moderate gaps are carried into the risk register (P01) and the POA&M (P07).

## 5. Pending and proposed changes (none treated as current obligations)
- **CIRCIA final rule** (C-CRITICAL-MFG-R01). The Unified Agenda targeted September 2026, but nothing was published as of 2026-09-26. If the sector criterion survives, the company would have 72-hour and 24-hour reporting duties to CISA. The P08 runbook already includes a voluntary CISA report, and the notification matrix carries CIRCIA as "not yet required."
- **NIST SP 800-82 Rev. 4 initial public draft** (2026-09-21; comments due 2026-11-30). Update the section references in G-001 to G-062 when Rev. 4 is final.
- **CIP-013-3** takes effect 2028-07-01. Watch for addendum revisions from the 12 utilities.
- **FAR overhaul.** The Revolutionary FAR Overhaul proposed rule for parts 1, 2, 4, 33, 39, 40, 52, and 53 (FR Doc. 2026-12559, 91 FR 37550, June 23, 2026; comments closed 2026-07-23) would move information security clauses into FAR part 40. It is proposed only. The company will follow the clauses in its awarded contract and check any modification or new solicitation for the new numbering.
