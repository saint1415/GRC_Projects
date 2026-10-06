# Regulatory Gap Analysis: Cris Santos Company | Commercial Facilities | Sole Proprietorship

| Field | Value |
|---|---|
| Organization | Cris Santos Company (owner-operator of one mixed-use commercial building) |
| Tier / Vertical | Sole Proprietorship / Commercial Facilities (NAICS 531120) |
| Primary benchmark | CISA Cross-Sector Cybersecurity Performance Goals, Version 2.0 (CPG 2.0), December 2025 (C-COMMERCIAL-FACILITIES-R05). **Voluntary** |
| OT tailoring | NIST SP 800-82 Rev. 3, *Guide to Operational Technology (OT) Security* (final), for the door controllers, cameras, and thermostats |
| Legal baseline (binding) | FTC Act Section 5, 15 U.S.C. 45(a) (C-COMMERCIAL-FACILITIES-R02); Fla. Stat. 501.171(2) and (8); FTC Disposal Rule, 16 CFR 682.3(a) |
| Assessment dates | 2026-07-20 to 2026-07-24 (self-assessment; building walkthrough 2026-07-21; tests 2026-07-23) |
| Assessor | Owner, with the on-call IT consultant. Evidence is self-attested, checked on screen where possible |
| Adopted | 2026-08-31 |

## 1. Applicability
**No mandatory cybersecurity regulation exists for commercial facilities**, so the vertical overlay names the CISA CPGs, with PCI DSS for payment environments. Each candidate was checked for a one-building sole proprietor:

| Candidate | Applies? | Reason |
|---|---|---|
| CISA CPG 2.0 (R05) | **Voluntary** | CPG 2.0 states that the goals are not "Mandated by CISA" and that CISA intends organizations "to voluntarily adopt" them. There are no size tiers. The owner adopted CPG 2.0 as the benchmark on 2026-07-17 |
| FTC Act Section 5 (R02) | **Yes** | No size threshold. Reaches unreasonable data security and misleading statements about data practices, including undisclosed biometric collection |
| Fla. Stat. 501.171 | **Yes** | The "covered entity" definition names a sole proprietorship that "acquires, maintains, stores, or uses personal information" (501.171(1)(b)). The owner holds about 15 guarantors' Social Security numbers and driver license copies. Subsection (2) requires "reasonable measures"; subsection (8) requires disposal of customer records; notice duties are in P08 |
| FTC Disposal Rule, 16 CFR 682.3(a) | **Yes** | Applies to "any person" who maintains consumer information for a business purpose (682.2(b)). The owner pulls consumer credit reports on individual guarantors |
| PCI DSS v4.0.1 (R01) | **No** | The owner is not a merchant. Rent is paid by ACH through the property management vendor's payment partner, or by check. Reassess before card payments are turned on |
| CCPA/CPRA (R03) | No | No California business; revenue (about $180,000) is far below the $26,625,000 threshold |
| SEC cybersecurity disclosure (R04) | No | Not a public company |
| CIRCIA (R06) | No (proposed rule only) | No final rule as of 2026-09-25. The NPRM (89 FR 23644, 2024-04-04) proposes no sector-based criterion for the Commercial Facilities Sector and relies on the size-based criterion (exceeding the SBA size standard). The business is far under its $34.0 million SBA standard |

**Decision.** The binding rules (Florida's "reasonable measures", FTC Section 5) do not say what reasonable security is. The owner uses CPG 2.0, the Sector Risk Management Agency's own baseline, to define it. The CPG rows are rated like requirements so the action list can show gaps, but **a CPG gap is not a violation.** The legal rows are.

**CPG 2.0 structure (verified in the Small sample on cisa.gov):** 34 goals in six functions: Govern 1.A to 1.E, Identify 2.A to 2.E, Protect 3.A to 3.S, Detect 4.A and 4.B, Respond 5.A and 5.B, Recover 6.A. CPG 2.0 folded the OT goals into universal goals with "OT:" guidance lines, which were applied here to the cloud-managed building devices.

**Tailoring for one person.** All 34 goals were rated. One is Not applicable: 2.D (public vulnerability disclosure), because the business publishes no software or service. Goals that assume staff (1.A responsibilities, 3.G separate accounts, 3.J training) were applied to the owner and the contractors.

## 2. Method
1. **Requirements.** CPG rows are the 34 goals at goal level; summaries paraphrase the goal and its OT line. Legal rows cite the statute or rule. PCI DSS is one row, recorded as not applicable.
2. **Crosswalk.** CPG rows use the CSF 2.0 references published in CPG 2.0, with an SP 800-53 subset chosen by the author from the CPG's own references (goal 3.O uses an author mapping, labeled). Legal rows are author mappings.
3. **Evidence.** Self-attested, checked on screen with the IT consultant: portal user lists and security settings, router settings, the laptop's browser password report, file sharing settings, DNS records, and the building walkthrough on 2026-07-21. Tenants were asked to confirm their credential lists on 2026-07-22.
4. **Status.** Met, Partially met, Not met, or Not applicable. Gap risk uses the P01 scale.

## 3. Results summary
| Source | Rows | Met | Partially met | Not met | N/A |
|---|---|---|---|---|---|
| CPG 2.0 Govern (1.A-1.E) | 5 | 0 | 2 | 3 | 0 |
| CPG 2.0 Identify (2.A-2.E) | 5 | 0 | 2 | 2 | 1 |
| CPG 2.0 Protect (3.A-3.S) | 19 | 2 | 7 | 10 | 0 |
| CPG 2.0 Detect (4.A-4.B) | 2 | 1 | 1 | 0 | 0 |
| CPG 2.0 Respond (5.A-5.B) | 2 | 0 | 0 | 2 | 0 |
| CPG 2.0 Recover (6.A) | 1 | 0 | 1 | 0 | 0 |
| **CPG 2.0 subtotal** | **34** | **3** | **13** | **17** | **1** |
| Legal baseline (15 U.S.C. 45(a); Fla. Stat. 501.171(2), (8); 16 CFR 682.3(a)) | 4 | 0 | 2 | 2 | 0 |
| PCI DSS v4.0.1 | 1 | 0 | 0 | 0 | 1 |
| **Total** | **39** | **3** | **15** | **19** | **2** |

The 34 unmet or partially met rows break down by gap risk as 4 High, 16 Moderate, and 14 Low. The High gaps are CPG 3.C (unique credentials), 3.F (MFA), 3.H (least privilege), and Fla. Stat. 501.171(2) (reasonable measures for guarantor data).

**The pattern.** What the vendors run is in reasonable shape: encrypted SaaS, vendor-pushed firmware, door controllers that work offline, no open ports. **What the owner runs was never set up:** sign-ins (no MFA on the building portals, shared and reused passwords, a default router password), who has access (installer administrator accounts, departed credential holders, a public folder link), and a plan for a bad day.

## 4. Action list (half page)
In order. The first six cost nothing and take under a day together.

| # | Action | Citation | Gap risk | Target |
|---|---|---|---|---|
| 1 | MFA by app on the access control, video, and thermostat portals (owner and installer accounts); email from text codes to an app | CPG 3.F | High | 2026-09-15 |
| 2 | Password manager; unique 16+ character passphrases; separate HVAC contractor login; change the router's default password | CPG 3.A, 3.B, 3.C | High | 2026-09-15 |
| 3 | Remove the public link to the lease application folder (done 2026-08-05); move guarantor files into one restricted folder | CPG 3.H; Fla. Stat. 501.171(2) | High | 2026-09-15 |
| 4 | Adopt POL-01 (roles, approval rule for new devices and AI features, retention) | CPG 1.A, 1.B, 3.P | Moderate | 2026-08-31 (done) |
| 5 | Adopt and print the P08 runbook and contact list; walk through it | CPG 1.C, 5.A, 5.B | Moderate | 2026-09-30 |
| 6 | Retire face recognition; keep audio off; update signs | 15 U.S.C. 45(a) | Moderate | 2026-09-30 |
| 7 | Remove installer standing accounts; security terms with 72-hour incident notice for all contractors | CPG 1.D, 1.E | Moderate | 2026-10-31 |
| 8 | Departure reporting rule for tenants and contractors; monthly credential review | CPG 3.D | Moderate | 2026-10-31 |
| 9 | Backups: SaaS backup of mail and files, monthly access control export, laptop backup | CPG 3.O | Moderate | 2026-10-31 |
| 10 | Retention and disposal rule; shred and purge guarantor and credit report files | Fla. Stat. 501.171(8); 16 CFR 682.3(a) | Low | 2026-10-31 |
| 11 | Business router: separate building-device and guest networks | CPG 3.I | Moderate | 2026-12-31 |
| 12 | Manual procedures for doors and thermostats; sealed envelope | CPG 6.A | Moderate | 2026-12-31 |

High and Moderate gaps are in the risk register (P01) and the POA&M (P07). The full list, with evidence, is in `gap-analysis.csv`.

## 5. Pending regulatory changes
- **CIRCIA:** final rule not published as of 2026-09-25. If the final rule keeps the NPRM's approach, this business stays out of scope. If it adds a Commercial Facilities criterion, recheck P08.
- **PCI DSS:** PCI SSC ran a request for comments on v4.0.1 in June and July 2026 toward a next version. No effect unless the owner starts taking cards.
- **NIST SP 800-82 Rev. 4** is an initial public draft (2026-09-21); Rev. 3 remains the final guide.
- **CPG 2.0** states a targeted revision cycle of 24 to 36 months.

None of these is treated as a current obligation.
