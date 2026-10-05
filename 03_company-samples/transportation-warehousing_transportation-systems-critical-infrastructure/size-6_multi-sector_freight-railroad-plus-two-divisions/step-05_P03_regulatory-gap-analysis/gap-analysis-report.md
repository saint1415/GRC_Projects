# Regulatory Gap Analysis: Cris Santos Company Holdings | Transportation Systems | Multi-Sector

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. (three divisions plus corporate shared services) |
| Tier / Vertical | Multi-Sector / Transportation Systems (focus division: Freight Railroad) |
| Primary regulation | TSA Security Directive 1580/82-2022-01E, Rail Cybersecurity Mitigation Actions and Testing (effective 2026-05-03 to 2027-05-02), with SD 1580-21-01E, Enhancing Rail Cybersecurity (effective 2026-01-16 to 2027-01-15). Both read from the TSA-published texts, which TSA states are not SSI |
| Division regulations | Transload and Wholesale: FAR 52.204-21, 52.204-23, and 52.204-25 in 7 federal contracts; hazmat security plan (49 CFR 172.800); FTC Act Section 5. Real Estate: FTC Act Section 5; the FTC Safeguards Rule does not apply and is used as a reference |
| Group obligations | SEC Reg S-K Item 106 and Form 8-K Item 1.05; state breach notification laws (Florida worked example); OFAC; intercompany and customer contracts |
| Gap tables | `gap-analysis.csv` (Freight Railroad, 85 rows); `gap-analysis-transload-wholesale.csv` (36 rows); `gap-analysis-real-estate.csv` (21 rows); `gap-analysis-group.csv` (11 rows) |
| Assessment dates | 2026-05-04 to 2026-07-31 (applicability confirmed 2026-05-08), with evidence updated from the P07 assessment (to 2026-08-28) |
| Assessors | Division security and compliance leads, the Vice President, Rail Security, and the federal contracts compliance manager, coordinated by the Group Chief Risk Officer's GRC team; legal conclusions by the Group General Counsel; reviewed by group internal audit |

## 1. Applicability
### 1.1 Freight Railroad: which railroads the directives reach
Both directives apply to "each freight railroad carrier identified in 49 CFR 1580.101" and to other railroads TSA designates and notifies. 49 CFR 1580.101 lists three kinds of freight railroad: (a) a Class I railroad; (b) one that "transports one or more of the categories and quantities of RSSM in an HTUA"; and (c) one that "serves as a host railroad" to a railroad in (a) or (b) or to a passenger operation described in 1582.101.

| Railroads | Count | 1580.101 basis | Directives | Other TSA duties |
|---|---|---|---|---|
| CR-01 to CR-10 | 10 | (b): PIH and other RSSM moved inside an HTUA (Florida example: CR-01 in the Jacksonville HTUA, CR-02 in the Tampa HTUA, Appendix A to part 1580) | **Apply** | Security training program (1580.113, 1580.115); RSSM location and chain of custody (part 1580 subpart C) |
| CR-11, CR-12 | 2 | (c): host Amtrak (1582.101(a)) | **Apply** | Security training program; PTC host duties (FRA) |
| CR-13, CR-14 | 2 | (c): host a commuter railroad identified in Appendix A to part 1582 (1582.101(b)) | **Apply** | Security training program; PTC host duties (FRA) |
| Other railroads carrying RSSM outside any HTUA | 17 | None | Do not apply (no TSA designation notice received; confirmed 2026-05-08) | Part 1580 subpart C; 1570.201; 1570.203 |
| Other railroads | 41 | None | Do not apply | 1570.201; 1570.203 |

No group railroad is Class I. Each is classified on its own revenue because the railroads are not operated as a single, integrated rail system (49 CFR part 1201, General Instructions 1-1(b)(1)). **One CIP covers all 14 Covered Railroads**, because they share the NOC, the dispatch and PTC platform, and the corporate network; TSA approved it on 2023-07-26. Group policy applies the same controls to every railroad on the shared platform, so the other 58 railroads benefit from them without being covered.

**PTC systems are Critical Cyber Systems** for CR-11 to CR-14, which must operate PTC under 49 CFR part 236 subpart I (SD 1580/82-2022-01E III.A.2.a). For the locomotives' onboard PTC components, the CIP relies on the physical measures the directive allows in III.C.6 (locked, sealed housings).

**Reporting.** SD 1580-21-01E requires reports to CISA "as soon as practicable, but no later than 72 hours" after identifying a cybersecurity incident (II.C.2). The vertical registry lists 24 hours for this duty; the current E version says 72 hours, and this analysis uses the directive text. A CISA report that states it is made under the directive also satisfies 49 CFR 1570.203 for the same incident (II.C.5). Because 1570.203 itself requires a report within 24 hours, the group files the CISA report within 24 hours by default.

### 1.2 TSA rules that reach all 72 railroads
49 CFR 1580.1(a)(1) covers "each freight railroad carrier that operates rolling equipment on track that is part of the general railroad system of transportation," with no size test. Through it:
- **49 CFR 1570.201**: primary and alternate Security Coordinators at the corporate level, reachable 24/7, reported to TSA within 37 calendar days of any change.
- **49 CFR 1570.203**: report potential threats and significant security concerns within 24 hours of initial discovery. Appendix A to part 1570 lists "Cyber Attack." For the 58 railroads not covered by the directives, this is the only binding cyber reporting duty, and the group's written procedure did not cover them (G-066). TSA's IC Surface-2025-01 recommends, without requiring, a telephone call to the TSA Transportation Security Operations Center (TSOC, 1-866-655-7023) no more than 12 hours after discovery of a significant cybersecurity incident (TSA information collection notice, FR Doc. 2026-17894, 2026-09-01).
- **49 CFR 1570.105(b)**: an owner/operator that starts new or modified operations must decide whether subpart B applies and notify TSA no later than 90 calendar days before starting. This matters for a group that buys railroads (G-068).
- **49 CFR part 1520**: each railroad is a covered person for SSI (1520.7(n)), and so is every group employee or contractor acting for it, including staff in corporate and the Real Estate division (1520.7(k)).

### 1.3 FRA positive train control
- **Host duty (CR-11 to CR-14):** 49 CFR 236.1005(b)(1) requires "each railroad providing or hosting intercity or commuter passenger service" to equip main lines used for regularly provided passenger service with a certified PTC system operated by the host. These 4 railroads run one on 238 route miles.
- **Tenant duty (24 railroads):** where a tenant movement on a Class I PTC line exceeds 20 miles, unequipped Class II and III trains were permitted only through 2023-12-31 (236.1006(b)(4)(iii)(B)), so each controlling locomotive must carry an operative onboard apparatus (236.1006(a)).
- **Security and recovery:** cryptographic message integrity and authentication, key protection, and a prioritized service restoration and mitigation plan (236.1033(a) to (f)).

### 1.4 Transload and Wholesale
| Requirement | Applies? | Basis |
|---|---|---|
| FAR 52.204-21 (N42-R04) | **Yes** | The clause is in 7 federal civilian supply contracts, and the division's ERP records, contracts workspace, and email process Federal Contract Information. The 15 basic safeguarding requirements in (b)(1) and the flow-down in (c) are decomposed in the division table |
| FAR 52.204-25 and 52.204-23 (N42-R05) | **Yes** | Same contracts. Reports of covered telecommunications are due within 1 business day (52.204-25(d)(2)(i)); reports of Kaspersky covered articles within 3 business days (52.204-23(c)(2)(i)); both with follow-up details within 10 business days |
| DFARS 252.204-7012 and CMMC (N42-R02, N42-R03) | No | No Department of Defense contracts and no CUI. Recheck before any DoD bid |
| Hazmat security plan, 49 CFR 172.800 and 172.802 | **Yes** | The division offers and transports large bulk quantities (over 3,000 liters in one packaging) of Class 3 Packing Group II materials by cargo tank (172.800(b)(6)) |
| FTC Act Section 5 (N42-R01) | **Yes** | The division is not a common carrier subject to subtitle IV of title 49, so the 15 U.S.C. 45(a)(2) exemption does not reach it |
| CTPAT (N42-R06) | Voluntary; not joined | Little direct importing |
| CCPA (N42-R08) | No | No operations or sales in California |
| Part 1580 | No | Terminals handle no RSSM, so the division is not a rail hazardous materials shipper or receiver under 1580.1(a)(2)-(3) |
| Voluntary benchmark | NIST CSF 2.0 with SP 800-82 Rev. 3 for terminal OT | No binding rule sets controls for loading racks, scales, or tank controls |

### 1.5 Railside Industrial Real Estate
The vertical registry names the **FTC Safeguards Rule** as the real estate primary regulation. It **does not apply** to this division, for two independent reasons, both checked against the regulation text:
1. The Rule protects "customer information" of "consumers," defined as individuals who obtain a financial product or service "to be used primarily for personal, family, or household purposes" (16 CFR 314.2). The division's tenants and licensees are businesses.
2. Its activity is not financial in nature. 16 CFR 314.2 ties "financial institution" to activities in section 4(k) of the Bank Holding Company Act. The leasing activity listed there (12 CFR 225.28(b)(3)) requires a lease "on a nonoperating basis" and, for real property, a return that compensates the lessor for its full investment plus financing cost. The division operates and maintains its buildings under ordinary operating leases.

The division still uses the Rule's elements as a **voluntary reference** because they are a concrete checklist of reasonable security that the FTC also applies under Section 5, which does apply. Other rules: state breach law for about 210 individual guarantors and for employees; SSI rules for right-of-way staff who handle railroad drawings; no PCI DSS (no card acceptance); no CCPA (no California properties).

### 1.6 Group-wide obligations
SEC Reg S-K Item 106 and Form 8-K Item 1.05 (the group is an SEC registrant); state breach notification laws in each state where affected individuals reside, with Florida as the worked example (Fla. Stat. 501.171); OFAC sanctions screening before any ransom payment; intercompany services agreements; CDS service agreements (P09); and leases.

**Not applicable, with reasons:** pipeline, aviation, and maritime rules (C-TRANSPORTATION-R02 to R05: no pipeline, airport, or MTSA-regulated vessel or facility); HIPAA (the employee health plan is a separate covered entity). CIRCIA (R07) and the TSA surface cyber NPRM (R06) are proposed only (section 6).

## 2. Regulation-by-division matrix
| Requirement | Freight Railroad | Transload and Wholesale | Real Estate | Group (corporate) |
|---|---|---|---|---|
| C-TRANSPORTATION-R01 SD 1580/82-2022-01E and SD 1580-21-01E | **Primary.** CR-01 to CR-14 | Not applicable; its terminal data flows into a Critical Cyber System through SYS-G5 (gap 1) | Not applicable | Common controls named in the CIP; Group CISO is primary Cybersecurity Coordinator |
| S01 49 CFR 1570.105, 1570.201, 1570.203 | All 72 railroads | Not applicable | Not applicable | SOC supports 24-hour reports |
| S02 Part 1580 subpart C (RSSM) | 27 railroads | Not applicable (no RSSM) | Not applicable | Not applicable |
| S03 SSI, 49 CFR part 1520 | Applies | Staff who see railroad SSI | Right-of-way staff (1520.7(k)) | Corporate file share and staff (1520.7(k)) |
| S09 Security training program (1580.113) | CR-01 to CR-14 | Not applicable | Not applicable | Learning system |
| S04 FRA PTC (part 236 subpart I) | Host CR-11 to CR-14; tenant 24 railroads | Not applicable | Not applicable | DC-1 and DC-2 host the back office |
| S05 FRA accident reporting (part 225) | All 72 railroads | Not applicable | Not applicable | Not applicable |
| S06 Hazmat security plan (172.800) | PIH (172.800(b)(5)) | Large bulk Class 3 PG II (172.800(b)(6)) | Not applicable | Not applicable |
| N42-R04, N42-R05 FAR 52.204-21, -23, -25 | Not applicable (no federal contracts) | **Applies** (7 contracts) | Not applicable | Common controls support it |
| N42-R02, N42-R03 DFARS and CMMC | Not applicable | Not applicable (no DoD, no CUI) | Not applicable | Not applicable |
| N42-R01, N53-R02 FTC Act Section 5 | Common carrier activity exempt (15 U.S.C. 45(a)(2), 44); group applies the same program | **Applies** | **Applies** | **Applies** |
| N53-R01 FTC Safeguards Rule | Not applicable | Not applicable | Not applicable (reference only) | Not applicable |
| S07 State breach notification (Florida worked example) | Employees | Employees and drivers | Employees and guarantors | Coordinates notices |
| S10 SEC Item 106 and Form 8-K Item 1.05 | Via group | Via group | Via group | **Applies** |
| R06 TSA NPRM; R07 CIRCIA | Tracked (would apply to all 72 railroads as proposed) | Tracked | Tracked | Tracked |
| SOC 2 (contractual) | CDS service line in scope (P09) | Routed to SOC 1 (P09) | Not in scope (P09) | Group services carved in |

## 3. Method
1. **Requirements.** Directive rows follow the directives' own section numbers at the most granular paragraph that imposes a separate duty. Regulation rows (49 CFR parts 172, 174, 236, 1520, 1570, 1580; FAR clauses; 16 CFR part 314) were read from eCFR (point in time 2026-09-23) and follow their paragraph structure; brief quotes are used because this is public-domain federal text. Florida rows were read from the Florida Senate's published statute text.
2. **Crosswalk.** Directive, regulation, and FAR rows carry an **author mapping** to CSF 2.0 and SP 800-53 Rev. 5, labeled in `crosswalk_source`, because no official NIST mapping exists for them. Benchmark rows use the official NIST CSF 2.0 to SP 800-53 Rev. 5.2.0 mapping in `00_universal-framework/crosswalks/`. SP 800-82 Rev. 3 is cited by section number only.
3. **Evidence.** Interviews (Group CISO, Vice President, Rail Security, Director, Rail OT Security, PTC Program Director, Director, NOC, terminal and property leaders, the federal contracts compliance manager, Group General Counsel), document review (CIP and CAP, TSA correspondence, PTCSP sections, hazmat security plans, contracts, leases), configuration exports, and P07 test results.
4. **Status.** Met, Partially met, Not met, or Not applicable, as of the end of fieldwork. Gaps were rated with the P01 risk scale.

## 4. Results
### 4.1 Freight Railroad (`gap-analysis.csv`)
| Section | Met | Partially met | Not met | N/A |
|---|---|---|---|---|
| SD 1580/82-2022-01E II (CIP, scope, service providers), 4 rows | 2 | 2 | 0 | 0 |
| SD 1580/82-2022-01E III.A (Critical Cyber Systems, PTC), 2 rows | 1 | 1 | 0 | 0 |
| SD 1580/82-2022-01E III.B (segmentation), 6 rows | 4 | 2 | 0 | 0 |
| SD 1580/82-2022-01E III.C (access control), 8 rows | 3 | 3 | 2 | 0 |
| SD 1580/82-2022-01E III.D (monitoring and detection), 12 rows | 9 | 3 | 0 | 0 |
| SD 1580/82-2022-01E III.E (patching), 4 rows | 2 | 1 | 1 | 0 |
| SD 1580/82-2022-01E III.F (assessment plan), 7 rows | 7 | 0 | 0 | 0 |
| SD 1580/82-2022-01E IV to VI (records, procedures, amendments), 7 rows | 4 | 1 | 2 | 0 |
| SD 1580-21-01E (coordinator, reporting, response plan, assessment), 13 rows | 11 | 2 | 0 | 0 |
| 49 CFR parts 1570 and 1580, 9 rows | 7 | 2 | 0 | 0 |
| 49 CFR part 1520 (SSI), 2 rows | 0 | 1 | 1 | 0 |
| 49 CFR part 236 subpart I (PTC), 8 rows | 7 | 1 | 0 | 0 |
| 49 CFR parts 172 and 174 (hazmat security), 3 rows | 2 | 1 | 0 | 0 |
| **Total Freight Railroad, 85 rows** | **59** | **20** | **6** | **0** |

**Not met:** G-018 (III.C.4.b), G-019 (III.C.5), G-036 (III.E.3), G-045 (IV.B), G-050 (VI.B.2; VI.C; VI.D), G-073 (49 CFR 1520.9(a)(1)-(2)).

The railroads meet most of the directive. Segmentation (III.B.1.c to III.B.2), malicious traffic and code controls (III.D.1), the assessment plan (III.F), PTC security (236.1033(a) to (d)), and the RSSM duties are all in place. The gaps sit where the platform met the rest of the group: an integration route added in 2025 without a CIP amendment (G-001, G-007, G-050), shared OT accounts and an unreviewed directory trust (G-018, G-019), OT logs that never reach the SIEM (G-030), unpatched PTC servers without the mitigations III.E.3 requires (G-033, G-036), and SSI stored where every division can read it (G-045, G-073, G-074).

### 4.2 Transload and Wholesale (`gap-analysis-transload-wholesale.csv`)
| Regulation | Met | Partially met | Not met | N/A |
|---|---|---|---|---|
| FAR 52.204-21, 16 rows | 13 | 3 | 0 | 0 |
| FAR 52.204-25 and 52.204-23, 4 rows | 1 | 3 | 0 | 0 |
| 49 CFR part 172 (hazmat security plan), 5 rows | 3 | 2 | 0 | 0 |
| FTC Act Section 5 and state breach law, 3 rows | 1 | 2 | 0 | 0 |
| CTPAT, DFARS, and CMMC, 2 rows | 0 | 0 | 0 | 2 |
| NIST CSF 2.0 with SP 800-82 Rev. 3 (benchmark), 6 rows | 0 | 3 | 3 | 0 |
| **Total Transload and Wholesale, 36 rows** | **18** | **13** | **3** | **2** |

The FAR safeguards are largely met because FCI was kept in a small enclave on group systems (P04). The division's real exposure is outside the FAR scope: 21 acquired terminals on flat networks without EDR, and always-on vendor access to loading rack controllers at hazmat terminals, which the hazmat security plan never assessed (TW-G24, TW-G33, TW-G34).

### 4.3 Real Estate (`gap-analysis-real-estate.csv`)
| Regulation | Met | Partially met | Not met | N/A |
|---|---|---|---|---|
| FTC Safeguards Rule (applicability), 1 rows | 0 | 0 | 0 | 1 |
| FTC Safeguards Rule elements (voluntary reference), 10 rows | 5 | 3 | 2 | 0 |
| FTC Act Section 5, state breach law, SSI, 3 rows | 0 | 3 | 0 | 0 |
| NIST CSF 2.0 with SP 800-82 Rev. 3 (benchmark), 5 rows | 0 | 1 | 4 | 0 |
| PCI DSS and CCPA, 2 rows | 0 | 0 | 0 | 2 |
| **Total Real Estate, 21 rows** | **5** | **7** | **6** | **3** |

The division's systems that matter most are run by vendors: building automation and access control. 9 controllers were reachable from the internet (RE-G08, RE-G16), consoles use shared vendor logins (RE-G17), and the vendor contracts carry no security terms (RE-G09, RE-G18).

### 4.4 Group (`gap-analysis-group.csv`)
| Obligation | Met | Partially met | Not met | N/A |
|---|---|---|---|---|
| SEC Item 106 and Form 8-K Item 1.05, 4 rows | 2 | 2 | 0 | 0 |
| State breach notification (generic; Florida worked example), 4 rows | 1 | 3 | 0 | 0 |
| OFAC, 1 rows | 1 | 0 | 0 | 0 |
| Proposed rules (tracked only), 2 rows | 0 | 0 | 0 | 2 |
| **Total group, 11 rows** | **4** | **5** | **0** | **2** |

Of the 60 unmet or partially met rows across all four tables, 15 are rated High, 37 Moderate, and 8 Low.

## 5. Group roadmap
| # | Gap (scenario gap) | Divisions | Citation | Risk | Action | Owner | Target |
|---|---|---|---|---|---|---|---|
| 1 | Integration platform not in the CIP; no amendment request (1) | Rail, Wholesale, corporate | SD 1580/82-2022-01E III.A, III.B.1.a-b, VI.B.2, VI.D | High | File the CIP amendment request; dedicated DMZ rule; interconnection record | Vice President, Rail Cybersecurity | 2026-11-30 |
| 2 | PTC back office unpatched without III.E.3 mitigations (2) | Rail | SD III.E.1, III.E.3; 49 CFR 236.1033(f) | High | Document mitigations and timeline; vendor certification terms; standby rebuild | PTC Program Director | 2026-10-31 (mitigations); 2027-03-31 (rebuild) |
| 3 | Shared CTC accounts and unreviewed directory trust (4) | Rail | SD III.C.4.b, III.C.5 | High | Rotate and retire shared accounts; review and remove the trust | Director, Rail OT Security | 2026-12-31 |
| 4 | OT logging coverage and retention (3) | Rail | SD III.D.3.a-b | High | Forward CTC and PTC logs | Group SOC Director | 2026-12-31 |
| 5 | Acquired terminals and rack vendor access (5) | Wholesale | 49 CFR 172.802(a)(2); FTC Act Section 5; CSF PR.IR-01 | High | Segment, EDR, PAM for vendors | Director, Security and Compliance (Transload and Wholesale) | 2027-03-31 |
| 6 | Internet-exposed building OT and shared vendor logins (7) | Real Estate | FTC Act Section 5; CSF PR.IR-01, PR.AA-05 | High | Remove exposure; named accounts; contract terms | Director, Facilities Technology | 2026-11-30 |
| 7 | SSI readable across divisions (12) | All | 49 CFR 1520.9(a), (c); SD IV.B | Moderate | Restricted SSI library; access log review; TSA notice if release confirmed | Vice President, Rail Security | 2026-10-31 |
| 8 | Multi-regulator notification not exercised; TSOC procedure for 58 railroads (8) | All | 49 CFR 1570.203; SD 1580-21-01E II.C; Form 8-K Item 1.05; state laws | Moderate | Group matrix and tabletop (P08) | Group General Counsel | 2026-12-15 |
| 9 | FAR reporting procedure and covered telecom inventory | Wholesale | 52.204-25(b)(2), (d); 52.204-23(c) | Moderate | Inventory terminal CCTV and network gear; written procedure | Federal contracts compliance manager | 2026-11-30 |
| 10 | No TSA step in the acquisition checklist | Rail, corporate | 49 CFR 1570.105(b); SD VI.A | Moderate | Add TSA applicability and CIP steps | Vice President, Rail Security | 2026-12-31 |

High and Moderate gaps are carried into the registers (P01) and the POA&M (P07; POAM-001, POAM-004, POAM-007, POAM-008, and POAM-018 to POAM-022 trace directly to this analysis).

## 6. Pending regulatory changes
- **TSA Enhancing Surface Cyber Risk Management NPRM** (89 FR 88488, 2024-11-07; C-TRANSPORTATION-R06). **Still proposed**: no final rule was found in the Federal Register as of 2026-09-26. As proposed, every railroad in 1580.1(a)(1) would need a Cybersecurity Coordinator (proposed 1580.311) and would report reportable cybersecurity incidents to CISA within 24 hours (proposed 1580.325). The full cyber risk management program (proposed 1580.301(b)) would reach Class II and III railroads only if they meet listed criteria, such as carrying RSSM in an HTUA, hosting a covered railroad, serving two or more Class I railroads, averaging at least 400,000 train miles a year, or being a Defense Connector Railroad. CR-01 to CR-14 would be in; the GRC team will test the other 58 against the final criteria.
- **CIRCIA** (6 U.S.C. 681b; proposed 6 CFR part 226, 89 FR 23644; C-TRANSPORTATION-R07). Not in effect: no final rule as of 2026-09-25. Proposed sector criterion 226.2(b)(14)(i) would cover "a freight railroad carrier identified in 49 CFR 1580.1(a)(1), (4), or (5)", so all 72 railroads would likely be covered (72-hour incident reports and 24-hour ransom payment reports).
- **Directive renewals.** SD 1580-21-01E expires 2027-01-15 and SD 1580/82-2022-01E on 2027-05-02. Recheck the text at each renewal.

The `pending_rule_change` column flags affected rows. None of these proposals is treated as a current obligation.
