# Regulatory Gap Analysis: Cris Santos Company | Defense Industrial Base | Mid-Market

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (PE-backed aircraft parts manufacturer, DoD subcontractor) |
| Tier / Vertical | Mid-Market / Defense Industrial Base |
| Primary regulation | NIST SP 800-171 Rev. 2 (110 requirements), as required by DFARS 252.204-7012(b)(2) and assessed for CMMC Level 2 (32 CFR 170.14(c)(3)) |
| Other rules for the primary business line | DFARS 252.204-7012 incident, cloud, and flowdown paragraphs; DFARS 252.204-7019, 252.204-7020, 252.204-7021; 32 CFR Part 170 scoping; FAR 52.204-21 and 52.204-25; ITAR and EAR; Fla. Stat. 501.171 (employee data); NISPOM (not applicable) |
| Assessment dates | 2026-07-06 to 2026-07-31 (evidence sampling through the P07 walkthroughs, 2026-08-11 to 2026-08-13) |
| Assessors | Security Manager and GRC analyst, with the Director of Trade Compliance and Contracts and the Manufacturing Systems Manager; reviewed by the vCISO |
| Working file | `gap-analysis.csv` (136 rows: G-001 to G-110 for the 110 requirements, G-111 to G-136 for clause and regulation duties) |
| Approved | Chief Operating Officer, 2026-09-17 |

## 1. Applicability
**DFARS 252.204-7012 applies now.** All current subcontracts with Prime A, Prime B, and Prime C include the clause, and the company receives and creates covered defense information (controlled technical information such as drawings, models, NC programs, build files, and test procedures). The clause has no small-business or size exemption and must be flowed down to any subcontract that involves covered defense information, including for commercial products or services (252.204-7012(m)(1)). It requires SP 800-171 on every covered contractor information system (252.204-7012(b)(2)(i)), which includes both plants' shop-floor systems.

**DFARS 252.204-7019 and 252.204-7020 apply now.** A current SP 800-171 DoD Assessment score (not more than 3 years old) must be in SPRS. The 2025 Basic Assessment of 74 is current by date, but it covered Plant 1 only and is not accurate (section 3).

**CMMC Level 2 (C3PAO) was expected from the next prime solicitations; that requirement is suspended.** Current subcontracts predate 2025-11-10 and do not include DFARS 252.204-7021. All three primes told suppliers that solicitations issued from 2026-11-10 (Phase 2, 32 CFR 170.3(e)(2)) would flow down Level 2 (C3PAO). The DoD (Department of War) CIO memorandum of 2026-07-13 suspends CMMC Phase 2. Until 2028-11-09, DoD includes clause 252.204-7021 only when a program office requires a specific CMMC level, and during the suspension requiring activities may require Level 1 (Self) or Level 2 (Self) (DoD Class Deviation 2026-O0025, Revision 3 (DFARS 240.371-5)). SP 800-171 Rev. 2 under DFARS 252.204-7012 still applies, so the remediation roadmap is unchanged. The company keeps preparing and treats the C3PAO assessment as a voluntary choice, ready in case the primes still ask for it. Where a prime contract does require Level 2 (C3PAO), a subcontractor that processes CUI needs at least that status (32 CFR 170.23(a)(3)). There is no size exemption. Prime A's next production lot (about 28% of revenue) is expected to award in 2027-06, which sets the deadline. The Affirming Official is the Chief Executive Officer (32 CFR 170.22).

**Scope.** The assessment covers the CUI Engineering Enclave defined in the SSP (P02), using the CMMC Level 2 asset categories in 32 CFR 170.19(c). Both plants are in scope because both process CUI. The CNC machines, CMMs, additive printers, test stands, and vision cell are Specialized Assets. The MSSP is an External Service Provider handling Security Protection Data, so its services are in scope as Security Protection Assets (32 CFR 170.19(c)(2)). The corporate network, ERP, and payroll and HR SaaS are Out-of-Scope Assets, except that the Plant 2 corporate segment cannot be treated as out of scope until it is separated from the Plant 2 shop floor.

**Other rules considered:**
- **ITAR and EAR:** decomposed at row level this year (G-131 to G-134) because a mid-market company with visitors, suppliers, and foreign-national employees has more ways to release technical data than the encryption rows alone show.
- **FAR 52.204-21 and 52.204-25:** apply to FCI on corporate systems and ERP, and to covered telecommunications equipment found during performance.
- **Fla. Stat. 501.171:** applies to employee personal information only (G-135).

**Not applicable, with reasons:**
- **3.13.14 (VoIP):** no VoIP components in the assessment scope. Scored as Met (32 CFR 170.24(b)(3)).
- **NISPOM (32 CFR Part 117):** no facility clearance and no classified information (G-136).
- **CIRCIA:** the final rule is not published; nothing is required yet.

**FAR overhaul numbering.** The requirements analyzed here as FAR 52.204-21 appear as FAR 52.240-93 in awards made under an agency's FAR Part 40 class deviation. The 15 requirements are the same, so these results apply to both. New DoD awards under DFARS Part 240 replace DFARS 252.204-7019 and -7020 with 252.240-7997, which covers DoD-led Medium and High assessments; the rows for 7019 and 7020 still describe the contracts awarded before that change. See `00_company-facts.md`.

## 2. Method
1. **Requirements.** The 110 rows follow the official structure of NIST SP 800-171 Rev. 2 (families 3.1 to 3.14), with the CMMC identifier and the point value from the CMMC Scoring Methodology (32 CFR 170.24(c)(2)). Requirement text is quoted from the public-domain NIST publication. The 26 clause and regulation rows cite the paragraph of each clause or section as checked on eCFR (version date 2026-09-23).
2. **Crosswalk.** CSF 2.0 and SP 800-53 Rev. 5 mappings are derived from NIST's official mappings through the SP 800-171 Rev. 3 counterpart of each requirement (the Rev. 2 to Rev. 3 change analysis, the SP 800-171r3 CUI overlay, and the CSF 2.0 to SP 800-171r3 mapping). The route through Rev. 3 is the author's; the `crosswalk_source` column says so for each row. Clause rows use author mappings.
3. **Evidence sampling.** At this size, each requirement was rated on sampled evidence, not on documents alone:
   - account lifecycle: 25 of 96 terminations, 25 of 71 new hires, 25 of 41 transfers;
   - change control: 20 change tickets; vulnerability remediation: 30 findings;
   - configuration: scans of 10 cloud servers and review of all MES and DNC servers;
   - physical: walkthroughs of 8 cells across both plants, the July 2026 visitor logs against gate camera records;
   - suppliers: purchase order terms and SPRS records for all 22 suppliers that receive CUI;
   - AI and data flows: a traffic capture of the predictive maintenance gateway and a review of corporate AI assistant prompt logs.
4. **Status.** Met, Partially met, Not met, or Not applicable. For CMMC scoring, a requirement is NOT MET if any objective is not satisfied (32 CFR 170.24(b)(2)), so every Partially met row counts as NOT MET in the score.
5. **Location.** The `gap_location` column marks each open requirement as "Plant 2 only" or "Enterprise (both plants or cloud)", to support the scoping decision in section 4.

## 3. Results summary

### SP 800-171 Rev. 2 requirements (110)
| Family | Met | Partially met | Not met | N/A | Points lost |
|---|---|---|---|---|---|
| 3.1 Access Control (22) | 16 | 6 | 0 | 0 | 16 |
| 3.2 Awareness and Training (3) | 2 | 0 | 1 | 0 | 1 |
| 3.3 Audit and Accountability (9) | 6 | 3 | 0 | 0 | 13 |
| 3.4 Configuration Management (9) | 3 | 6 | 0 | 0 | 26 |
| 3.5 Identification and Authentication (11) | 7 | 4 | 0 | 0 | 18 |
| 3.6 Incident Response (3) | 1 | 2 | 0 | 0 | 6 |
| 3.7 Maintenance (6) | 4 | 1 | 1 | 0 | 8 |
| 3.8 Media Protection (9) | 3 | 6 | 0 | 0 | 18 |
| 3.9 Personnel Security (2) | 1 | 1 | 0 | 0 | 5 |
| 3.10 Physical Protection (6) | 4 | 2 | 0 | 0 | 2 |
| 3.11 Risk Assessment (3) | 1 | 2 | 0 | 0 | 6 |
| 3.12 Security Assessment (4) | 1 | 3 | 0 | 0 | 8 |
| 3.13 System and Communications Protection (16) | 11 | 4 | 0 | 1 | 14 |
| 3.14 System and Information Integrity (7) | 4 | 3 | 0 | 0 | 13 |
| **Total (110)** | **64** | **43** | **2** | **1** | **154** |

Of the 45 requirements not fully met, 16 are basic and 29 are derived requirements. 24 of the 45 are open only because of Plant 2.

### Clause and regulation duties (26)
| Source | Met | Partially met | Not met | N/A |
|---|---|---|---|---|
| DFARS 252.204-7012 (cloud, special measures, review, reporting, certificate, malware, preservation, forensics, flowdown, incident number) | 5 | 5 | 0 | 0 |
| DFARS 252.204-7019 and 252.204-7020 (SPRS, Government access, subcontractor assessments) | 1 | 2 | 0 | 0 |
| DFARS 252.204-7021 and 32 CFR Part 170 (status and affirmation, CUI on assessed systems, subcontractor flowdown, scope, ESP) | 0 | 3 | 2 | 0 |
| FAR 52.204-21 and 52.204-25 | 1 | 1 | 0 | 0 |
| ITAR and EAR (registration, release, encryption carve-outs, voluntary disclosure) | 2 | 2 | 0 | 0 |
| Fla. Stat. 501.171 (employee data) | 1 | 0 | 0 | 0 |
| NISPOM | 0 | 0 | 0 | 1 |
| **Total (26)** | **10** | **13** | **2** | **1** |

**Gap risk across all 60 open rows:** 1 Very High, 34 High, 22 Moderate, 3 Low.

### Score under 32 CFR 170.24
| Item | Value |
|---|---|
| Maximum score | 110 |
| Points subtracted for the 45 requirements not fully met | 154 (23 at 5 points, 7 at 3 points, 12 at 1 point, 3.5.3 and 3.13.11 at 3 points each as partially effective; 3.12.4 carries no point value) |
| **Recalculated score, full scope (both plants)** | **-44** |
| Score if only the cloud enclave and Plant 1 were in scope | 40 (Plant 2 accounts for 84 points) |
| SPRS score posted 2025-06-12 | 74, Plant 1 scope only (withdrawn; corrected score due 2026-09-30) |
| Minimum for Conditional Level 2 status | 88 (score / 110 of at least 0.8, 32 CFR 170.21(a)(2)(i)) |

**Why 74 became 40 even for Plant 1.** The 2025 self-assessment counted policies as evidence for technical requirements and did not test the shop floor. On sampled evidence, Plant 1 still loses points for shop-floor logging and monitoring (3.3.1, 3.3.5, 3.14.6), OT baselines (3.4.1, 3.4.2), MES scanning and patching (3.11.2, 3.14.1), late account removal (3.1.1, 3.9.2), and reporting that has never been drilled (3.6.2).

Conditional status also allows only 1-point requirements on a POA&M (plus 3.13.11 when encryption is used but not FIPS-validated), and never 3.1.20, 3.1.22, 3.12.4, 3.10.3, 3.10.4, or 3.10.5 (32 CFR 170.21(a)(2)(ii) and (iii)). Four of those six are open: 3.1.20 (AI-003 gateway and AI-001 pilot), 3.10.3 and 3.10.4 (Plant 2 visitors), and 3.12.4 (SSP v4.0 written 2026-09-17, to be verified). **The plan therefore aims for all 110 requirements Met before the C3PAO assessment**, with a POA&M used only as a fallback for 1-point items.

## 4. Scoping decision: Plant 2
Plant 2 accounts for 24 open requirements and 84 points. Three options were analyzed with the COO, the Vice President of Operations, and the vCISO on 2026-07-29:

| Option | What it means | Revenue effect | Decision |
|---|---|---|---|
| A. Integrate Plant 2 into the enclave | Enclave firewall and VLANs, named MES sign-in, replacement servers, logging, scanning, visitor control, printed CUI controls | None | **Chosen.** Funded in the FY2027 plan; target 2027-01-31 |
| B. Make Plant 2 a non-CUI site until integrated | Move all CUI work to Plant 1; Plant 2 builds only commercial parts with no controlled data; prove it cannot process CUI (Out-of-Scope Asset) | Prime A and Prime C assemblies (about $60 million a year) would move to Plant 1, which lacks sheet-metal and assembly capacity | Rejected as the main plan; kept as the **fallback** if Plant 2 is not ready by 2027-01-31 |
| C. Treat Plant 2 OT and MES as Specialized Assets | Document as risk-managed assets | None | Rejected: MES, DNC servers, and terminals are ordinary IT that can be secured, so they are CUI Assets, not Specialized Assets (32 CFR 170.19(c)(1)) |

The fallback decision point is 2027-01-31, after the readiness re-check of Plant 2. Either way, the score posted on 2026-09-30 covers both plants, because Plant 2 handles CUI today.

## 5. Priority gaps and roadmap
| Gap | Citation | Risk level | Action | Owner | Target |
|---|---|---|---|---|---|
| G-124 Not eligible for Level 2 (C3PAO) awards | 252.204-7021(d)(1),(3); 32 CFR 170.17, 170.22 | Very High | Complete this roadmap; C3PAO assessment; affirmation by the CEO | Chief Operating Officer | 2027-03-19 |
| G-121 SPRS score overstates implementation | 252.204-7019(b); 252.204-7020(d) | High | Post -44 for both plants with a date-to-110; update after each milestone | Director of Trade Compliance and Contracts | 2026-09-30 |
| G-020, G-077, G-078, G-087 Cannot be on a POA&M | 3.1.20; 3.10.3; 3.10.4; 3.12.4 | High | Switch off the AI-003 gateway uplink until it moves to an OT DMZ; AI-001 off until boundary confirmation; Plant 2 visitor system; verify SSP v4.0 | Security Manager; Facilities and Security Manager | 2026-10-31 |
| G-088, G-093, G-041 Plant 2 boundary and exposed services | 3.13.1; 3.13.6; 3.4.7 | High | Close remote desktop and legacy file sharing now; Plant 2 enclave firewall and VLANs | IT Director; Manufacturing Systems Manager | 2026-11-30; 2027-01-31 |
| G-044, G-045, G-053, G-039 Plant 2 identity and change rights | 3.5.1; 3.5.2; 3.5.10; 3.4.5 | High | Vault the DNC credential now; replacement MES with named badge plus PIN sign-in and edit rights for programmers only | Manufacturing Systems Manager | 2026-10-31; 2027-01-31 |
| G-026, G-030, G-109 Shop-floor logging and monitoring | 3.3.1; 3.3.5; 3.14.6 | High | Onboard MES, DNC, OT gateways, and Plant 2 firewalls to the SIEM; passive OT monitoring | Security Manager | 2027-01-31 |
| G-082, G-104 Scanning and patching of shop-floor servers | 3.11.2; 3.14.1 | High | Monthly scans including MES; replace Plant 2 servers; Plant 1 MES patch windows | Security Manager; Manufacturing Systems Manager | 2026-12-31; 2027-01-31 |
| G-035, G-036 OT baselines | 3.4.1; 3.4.2 | High | Baselines and hardening for MES and DNC servers at both plants | Manufacturing Systems Manager | 2027-01-31 |
| G-056, G-114, G-117 Reporting and preservation | 3.6.2; 252.204-7012(c)(1)(ii), (e) | High | DIBNet drill in the 2026-11-18 tabletop; OT imaging procedure | Director of Trade Compliance and Contracts; Security Manager | 2026-11-30 |
| G-119, G-123, G-126 Supplier flowdown and verification | 252.204-7012(m)(1); 252.204-7020(g)(2); 252.204-7021(d)(4) | High | Re-paper 9 suppliers; verify all 22; add DFARS 252.204-7021 to templates for primes that flow down a CMMC level | Director of Supply Chain | 2026-10-31 |
| G-066, G-070 Printed CUI and USB loading at Plant 2 | 3.8.3; 3.8.7 | High | Locked shred bins; labeled drive inventory, then the DNC serial gateway | Director of Quality; Manufacturing Systems Manager | 2026-10-31; 2027-01-31 |
| G-098 FIPS mode on the Plant 2 SD-WAN appliance | 3.13.11 | High | Enable FIPS mode or replace the appliance | IT Director | 2026-11-30 |
| G-062 Additive printer vendor remote access | 3.7.5 | High | Move to the company access broker; block the vendor tool | Security Manager | 2026-10-31 |
| G-001, G-074 Account lifecycle | 3.1.1; 3.9.2 | High | Same-day automated disable; quarterly reviews | HR Director; Security Manager | 2027-01-31 |
| G-132 Possible visual release at Plant 2 | 22 CFR 120.56 | High | Escort, log, covered racks | Director of Trade Compliance and Contracts | 2026-10-31 |

**Roadmap by milestone:**
1. **By 2026-09-30:** corrected SPRS score for both plants.
2. **By 2026-10-31:** all items that cannot be on a POA&M; supplier flowdown and DFARS 252.204-7021 in templates; additive vendor access through the broker; Plant 2 shred bins and unowned drives removed; DNC credential vaulted; asset inventory and diagram complete (G-127).
3. **By 2026-11-30:** Plant 2 remote desktop closed; nightly encrypted Plant 2 backups to the cloud vault; FIPS mode at Plant 2; AI-003 gateway moved to an OT DMZ; CUI exfiltration tabletop with DIBNet drill (2026-11-18); OT imaging procedure; MSSP CRM.
4. **By 2026-12-31:** monthly scanning including MES; insider threat training; maintenance media kiosks; full self-assessment against SP 800-171A objectives for both plants; contingency plan.
5. **By 2027-01-31:** Plant 2 enclave firewall and VLANs; replacement Plant 2 MES and DNC with named sign-in; DNC serial gateway; SIEM onboarding and passive OT monitoring; OT baselines; phishing-resistant authenticators. Plant 2 fallback decision (section 4).
6. **2027-02:** readiness re-check by the co-sourced internal audit firm; corrected SPRS score of 110 if all requirements are Met.
7. **2027-03-08 to 2027-03-19:** C3PAO Level 2 certification assessment.

The full list, with evidence, is in `gap-analysis.csv`. High and Very High gaps are carried into the risk register (P01) and the POA&M (P07).

## 6. Pending regulatory changes
- **FAR CUI rule:** proposed (90 FR 4278, 2025-01-15) and not final. Nothing changes until it is final; DFARS 252.204-7012 remains the governing clause (flagged on G-119).
- **Revolutionary FAR Overhaul:** a proposed rule (FR Doc. 2026-12559, 2026-06-23) would reorganize FAR parts, including part 40. FAR 52.204-21 numbering may change (flagged on G-129). Not final.
- **SP 800-171 Rev. 3:** published by NIST, but CMMC Level 2 is fixed to Rev. 2 (32 CFR 170.14(c)(3)). Each row names its Rev. 3 counterpart in `pending_rule_change` for later planning. Rev. 3 is not treated as a current obligation.
- **CMMC Phase 3 (2027-11-10, 32 CFR 170.3(e)(3)):** DoD intends to require Level 2 (C3PAO) for all applicable solicitations and as a condition to exercise option periods on contracts awarded after the effective date. No new requirement for the company beyond holding and maintaining its status, but primes will check status before exercising options. Under DoD Class Deviation 2026-O0025, Revision 3 (DFARS 240.371-5), DoD includes clause 252.204-7021 until 2028-11-09 only when a program office or requiring activity requires a specific CMMC level.
- **CIRCIA:** the final rule is not published. Proposed reporting deadlines are not treated as current obligations.
