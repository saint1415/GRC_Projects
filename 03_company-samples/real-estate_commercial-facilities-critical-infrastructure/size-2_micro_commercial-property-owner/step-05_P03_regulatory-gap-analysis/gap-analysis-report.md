# Regulatory Gap Analysis: Cris Santos Company | Commercial Facilities | Micro

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (commercial office and retail property owner-operator) |
| Tier / Vertical | Micro / Commercial Facilities (NAICS 531120) |
| Primary benchmark | CISA Cross-Sector Cybersecurity Performance Goals, Version 2.0 (CPG 2.0), December 2025 (C-COMMERCIAL-FACILITIES-R05). **Voluntary** |
| OT tailoring | NIST SP 800-82 Rev. 3, *Guide to Operational Technology (OT) Security* (final) |
| Binding by contract | PCI DSS v4.0.1, requirements in the v4.0.1 SAQ P2PE (C-COMMERCIAL-FACILITIES-R01) |
| Legal baseline | FTC Act Section 5, 15 U.S.C. 45(a) (C-COMMERCIAL-FACILITIES-R02); Fla. Stat. 501.171(2) and (8); FTC Disposal Rule, 16 CFR 682.3(a) |
| Assessment dates | 2026-07-20 to 2026-07-31 (walkthroughs of both properties 2026-07-22) |
| Assessors | Property Manager (security and privacy lead) with the MSP lead technician, the Building Engineer, and the Bookkeeper |
| Approved | 2026-08-31 by the Managing Member |

## 1. Applicability
**No mandatory cybersecurity regulation exists for commercial facilities**, so the vertical overlay names the CISA CPGs, with PCI DSS for payment environments. Each candidate was checked for a 7-person, two-property company:

| Candidate | Applies? | Reason |
|---|---|---|
| CISA CPG 2.0 (R05) | **Voluntary** | CPG 2.0 states that the goals are not "Mandated by CISA" and that CISA intends organizations "to voluntarily adopt" them. There are no size tiers. The Managing Member adopted CPG 2.0 as the company's benchmark on 2026-07-15 |
| PCI DSS v4.0.1 (R01) | **Yes, by contract** | The company is a merchant (about 600 card transactions a year on one P2PE terminal) and its merchant agreement requires PCI DSS compliance. PCI DSS is an industry standard, not law; the validation type (SAQ P2PE) is set by the acquirer |
| FTC Act Section 5 (R02) | **Yes** | No size threshold. Reaches unreasonable data security and misleading statements or omissions about data practices, including undisclosed biometric or video analytics |
| Fla. Stat. 501.171 | **Yes** | The company is a "covered entity" (a commercial entity that "acquires, maintains, stores, or uses personal information", 501.171(1)(b)). It holds about 60 guarantors' and applicants' Social Security numbers and driver license copies. Subsection (2) requires "reasonable measures"; subsection (8) requires disposal of customer records; notice duties are in P08 |
| FTC Disposal Rule, 16 CFR 682.3(a) | **Yes** | Applies to any person who maintains consumer information for a business purpose. The company pulls consumer credit reports on individual guarantors and applicants |
| CCPA/CPRA (R03) | No | No California business; revenue (about $1.1 million) is far below the $26,625,000 threshold |
| SEC cybersecurity disclosure (R04) | No | Privately held |
| CIRCIA (R06) | No (proposed rule only) | No final rule as of 2026-09-25. The NPRM (89 FR 23644, 2024-04-04) proposes no sector-based criterion for the Commercial Facilities Sector and relies on the size-based criterion (exceeding the SBA size standard). The company is far under its $34.0 million SBA standard |

**Decision.** The binding rules (Florida's "reasonable measures", FTC Section 5) do not say what reasonable security is. The company uses CPG 2.0, the Sector Risk Management Agency's own baseline, to define it, tailored for OT with SP 800-82 Rev. 3. PCI DSS is analyzed at requirement level because the merchant agreement binds the company to it. The CPG rows are rated like requirements so the roadmap can show gaps, but **a CPG gap is not a violation.** The PCI and legal rows are obligations.

**CPG 2.0 structure (verified in the Small sample on cisa.gov, report dated December 2025):** 34 goals in six functions: Govern 1.A to 1.E, Identify 2.A to 2.E, Protect 3.A to 3.S, Detect 4.A and 4.B, Respond 5.A and 5.B, Recover 6.A. CPG 2.0 folded the OT goals of version 1.0.1 into universal goals with "OT:" guidance lines; those lines were applied here to the BAS, door controllers, and cameras.

**Tailoring for a micro company.** All 34 goals were rated. One is Not applicable: 2.D (public vulnerability disclosure), because the company publishes no software or online service. Goals written for security teams (1.A responsibilities, 3.G separate administrator accounts, 3.Q central logging) were applied at the scale of one security lead plus the MSP.

**PCI DSS scope.** One P2PE terminal, stand-alone on cellular, for fob fees, after-hours HVAC charges, conference room bookings, and Property B kiosk fees. Rent is ACH only. The acquirer requires an annual SAQ P2PE. The PCI rows are the eligibility statement plus the 21 requirements listed in the v4.0.1 SAQ P2PE (October 2024), as recorded in the Small sample's review of that SAQ; the Bookkeeper rechecks the list against the SAQ itself before signing. PCI DSS is copyrighted, so the rows give requirement numbers with short topic labels written for this analysis.

## 2. Method
1. **Requirements.** CPG rows are the 34 goals at goal level, citing the goal ID; summaries paraphrase the goal and its OT line. PCI rows are listed above. Legal rows cite the statute or rule.
2. **Crosswalk.** CPG rows use the CSF 2.0 references published in CPG 2.0, with an SP 800-53 subset chosen by the author from the CPG's own references. For goal 3.O, CPG 2.0 lists PR.IR-01 and DE.CM-01, which repeat goal 3.I; an author mapping (PR.DS-11; CP-9, CP-4, CP-10) is used instead and labeled. PCI and legal rows are author mappings (no official NIST mapping of PCI DSS v4.0.1 was used).
3. **Documentary evidence.** Each status rests on a named document or record: the platform administrator and credential reports, the suite security settings and MFA report, the MSP device list, patch report, antivirus export, backup job report, and external scan, the firewall rule export, the BAS workstation account list and remote-desktop tool settings, the 2025 SAQ P2PE, the processor agreement and P2PE Instruction Manual (PIM), the vendor contracts, DNS records, and the shared drive permissions. Interviews covered all 7 employees, the MSP lead technician, and the controls contractor's technician.
4. **Status.** Met, Partially met, Not met, or Not applicable **as of the end of fieldwork (2026-07-31)**. Actions completed since then (for example, POL-02 approved 2026-08-31) are noted in the remediation column but do not change the status. Gap risk uses the P01 scale.

## 3. Results summary
| Source | Rows | Met | Partially met | Not met | N/A |
|---|---|---|---|---|---|
| CPG 2.0 Govern (1.A-1.E) | 5 | 0 | 1 | 4 | 0 |
| CPG 2.0 Identify (2.A-2.E) | 5 | 0 | 2 | 2 | 1 |
| CPG 2.0 Protect (3.A-3.S) | 19 | 0 | 12 | 7 | 0 |
| CPG 2.0 Detect (4.A-4.B) | 2 | 0 | 1 | 1 | 0 |
| CPG 2.0 Respond (5.A-5.B) | 2 | 0 | 0 | 2 | 0 |
| CPG 2.0 Recover (6.A) | 1 | 0 | 0 | 1 | 0 |
| **CPG 2.0 subtotal** | **34** | **0** | **16** | **17** | **1** |
| PCI DSS v4.0.1 SAQ P2PE (eligibility plus 21 requirements) | 22 | 1 | 8 | 12 | 1 |
| Legal baseline (15 U.S.C. 45(a); Fla. Stat. 501.171(2), (8); 16 CFR 682.3(a)) | 4 | 0 | 2 | 2 | 0 |
| **Total** | **60** | **1** | **26** | **31** | **2** |

The 57 unmet or partially met rows break down by gap risk as 4 High, 26 Moderate, and 27 Low. All four High gaps are CPG goals: 1.E (provider remote access), 3.F (MFA), 3.I (segmentation), and 3.O (backups).

**The pattern.** What the vendors run is in reasonable shape: the cloud access control platform has a SOC 2 report, the terminal keeps card data out of company systems, and the MSP patches the office computers. **What the company runs was never treated as IT:** a BAS workstation with a shared login, no patches, and an always-on contractor tool; building devices on the office network; single-factor administrator accounts; and no plan for a bad day. The PCI gaps come from one habit, writing card numbers from phone orders on a notepad, plus the PIM terminal controls nobody knew about.

## 4. Priority gaps
| Gap | Citation | Risk | Action | Owner | Target |
|---|---|---|---|---|---|
| Contractor and MSP remote access without MFA, approval, or review | CPG 1.E | High | Approved remote access service with named accounts, MFA, per-session approval, recording; yearly MSP review | Building Engineer | 2026-10-31 |
| No MFA on platform administrators, the contractor account, or the backup console | CPG 3.F | High | MFA on all three | Property Manager | 2026-09-30 |
| No segmentation between office IT and building devices | CPG 3.I | High | Building-device segment at each property, deny by default | Property Manager | 2026-12-31 |
| BAS backups untested, not immutable, missing controller programs | CPG 3.O | High | Immutable 90-day backup; program copies; restore test, then quarterly | Building Engineer | 2026-12-31 |
| Card numbers and security codes written on paper | PCI DSS 3.2.1, 3.3.1.2, 9.4.1, 9.4.6 | Moderate | Key phone orders directly; shred existing notes | Bookkeeper | 2026-09-15 |
| SAQ P2PE eligibility (PIM controls missing) | SAQ P2PE eligibility | Moderate | PIM inspections and training; acquirer confirmation before signing | Bookkeeper | 2026-10-31 |
| Shared accounts on the BAS, contractor tool, and integrator access | CPG 3.C | Moderate | Named accounts | Building Engineer | 2026-12-31 |
| Default passwords never checked | CPG 3.A | Moderate | Change defaults; commissioning checklist | Building Engineer | 2026-09-30 |
| No vendor incident notice terms | CPG 1.D | Moderate | Security addendum with 24-hour notice | Managing Member | 2026-12-31 |
| Guarantor files open to all staff and synced to desktops | Fla. Stat. 501.171(2) | Moderate | Restricted folder outside sync | Tenant Services and Leasing Coordinator | 2026-10-31 |
| Face match trial with no notice | 15 U.S.C. 45(a) | Moderate | P10 decision; notice and signs before any analytics use | Property Manager | 2026-09-30 |
| No recovery plan or manual procedures | CPG 6.A | Moderate | Contingency plan; train a second person | Building Engineer | 2026-12-31 |

The full list, with evidence, is in `gap-analysis.csv`. Every High and Moderate gap is carried into the risk register (P01) and, where the control was assessed, the POA&M (P07).

## 5. Remediation plan
The plan fits a 7-person company: most actions are settings, one-page procedures, or contract terms. The MSP and the controls contractor do the technical work under the Property Manager's and Building Engineer's direction. Costs are in the P01 treatment summary.

| Phase | Due | Actions | Gaps closed (citation) |
|---|---|---|---|
| 1. Sign-ins and paper | 2026-09-30 | MFA on platform administrators, contractor account, backup console; change defaults; stop writing card data and shred notes; policies approved and acknowledged; tenant communication and reporting procedures; approval rule for new devices and features; remove email from the BAS workstation | CPG 1.A, 1.B, 3.A, 3.F, 3.M, 3.P, 5.A, 5.B; PCI 3.1.1, 3.2.1, 3.3.1.2, 9.1.1, 9.4.1, 9.4.6, 12.1.1, 12.1.3, 12.8.1, 12.10.1; 15 U.S.C. 45(a) |
| 2. Access and records | 2026-10-31 | Approved remote access service; credential review and inactivity rule; restricted guarantor folder; retention and shredding; desktop encryption; device inventory; contractor change approval; PIM inspections and training; processor monitoring; password manager; sign-in alerts | CPG 1.E, 2.A, 3.B, 3.D, 3.E, 3.H, 3.K, 3.N; PCI eligibility, 9.5.1, 9.5.1.1, 9.5.1.2, 9.5.1.3, 12.8.3, 12.8.4, 12.8.5; Fla. Stat. 501.171(2), (8); 16 CFR 682.3(a) |
| 3. Network and plan | 2026-11-30 | Network diagrams; Property B business router; DMARC enforcement; incident tabletop | CPG 1.C, 2.E, 3.L, 3.S |
| 4. Resilience and detection | 2026-12-31 | Segmentation; immutable backups and restore tests; EDR with after-hours alerting; log service; USB control; named BAS and contractor accounts; separate administrator accounts; training and phishing simulations; contingency plan; vendor security addendum; BAS patching process | CPG 1.D, 2.B, 3.C, 3.G, 3.I, 3.J, 3.O, 3.Q, 3.R, 4.A, 4.B, 6.A; PCI 12.6.1 |
| 5. Annual cycle | 2027-07-31 to 2027-08-31 | Risk assessment update (July); independent assessment and policy review (August) | CPG 2.C; PCI 12.1.2 |

**Before signing the 2026 SAQ P2PE:** close G-035 to G-040, G-042, and G-045 to G-046, and record the acquirer's confirmation of the SAQ path. If card data is ever received by email or typed into a company computer, the company is no longer eligible for SAQ P2PE for that channel and must ask the acquirer how to validate.

**Progress check.** The Property Manager reports progress to the Managing Member at a monthly 30-minute security meeting, using the P07 POA&M as the tracker.

## 6. Pending regulatory changes
- **CIRCIA:** the final rule was not published as of 2026-09-25. If the final rule keeps the NPRM's approach, the company stays out of scope. If it adds a Commercial Facilities sector criterion, the P08 matrix must add the statute's 72-hour incident and 24-hour ransom payment reports to CISA.
- **PCI DSS:** PCI SSC ran a request for comments on v4.0.1 in June and July 2026 toward a next version. No publication date was found. v4.0.1 remains in force.
- **NIST SP 800-82 Rev. 4** is an initial public draft (2026-09-21). It is not used; Rev. 3 remains the final guide.
- **CPG 2.0** states a targeted revision cycle of 24 to 36 months.

None of these is treated as a current obligation.
