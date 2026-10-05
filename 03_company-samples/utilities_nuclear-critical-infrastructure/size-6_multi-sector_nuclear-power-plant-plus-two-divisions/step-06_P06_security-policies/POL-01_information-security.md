# Information Security Policy (Group)

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. and all divisions (Nuclear Generation, Engineering and Radiation Services, Radioactive Waste Management) and corporate shared services |
| Policy ID | POL-01 |
| Owner | Group CISO |
| Approved by | Board risk committee |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review 2027-09-30), and after major changes, acquisitions, incidents, or a change in NRC, NERC, or Agreement State requirements |
| Implements (SP 800-53 Rev. 5) | PM-1, PM-2, PM-9, PM-10, PL-1, PL-2, PS-8, RA-3, SA-4, SA-9, CA-2, CA-7, SI-12 |
| CSF 2.0 | GV.OC-03, GV.PO-01, GV.PO-02, GV.RR-02, GV.RR-04, GV.RM-01, GV.OV-01, GV.SC-05, ID.RA-01, ID.IM-01 |
| Regulatory drivers | C-NUCLEAR-R01 (73.54(d)(2)); C-NUCLEAR-S03 (73.58); C-NUCLEAR-S06 (37.43); C-NUCLEAR-S10 (Reg S-K Item 106) |
| Division supplements | Nuclear Generation supplement (v2026); Engineering and Radiation Services supplement (v2026); Radioactive Waste Management supplement (v2024, re-issue due 2026-11-30). See `division-supplements.md` |

## 1. Purpose
Set up one information security program for the whole group, assign who is accountable at group and division level, and give every other group policy and every division supplement its authority. The program protects the group's business systems and information, and it keeps those systems from becoming a path to the systems that NRC, NERC, and Agreement State rules protect.

## 2. Scope
All workforce members of Cris Santos Company Holdings, Inc. and its divisions (employees, contractors, and outage workers), all business systems and data the group owns or operates, and systems operated for the group by service providers.

**Programs this policy does not replace.** Each station's NRC-approved cyber security plan (CSP) under 10 CFR 73.54, the fleet SGI program, the NERC CIP program for the fleet operations center, and the Part 37 security program at the Florida waste facility are separate, regulator-approved programs. Where they set a stricter rule, they govern. Group policy applies to everything outside them and to the interfaces with them.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Board risk committee | Oversees cyber risk; approves this policy; accepts Very High risks |
| Group CISO | Owns the program and group policies; operates common controls through SYS-G1 to SYS-G3; co-accepts High risks |
| Group Chief Risk Officer | Owns the group risk register and ERM roll-up (NIST IR 8286 Rev. 1); co-accepts High risks; chairs the group AI council |
| Group General Counsel | Owns intercompany agreements, client and customer contract terms, and the notification matrix |
| Disclosure committee | Decides SEC materiality of cybersecurity incidents |
| Chief Nuclear Officer | Executive owner of the three CSPs; accepts Moderate risks for Nuclear Generation |
| Division presidents | Accept Moderate risks for their divisions |
| Division security and compliance leads | Maintain division supplements and registers; accept Low risks |
| Fleet cyber security program manager | Owns the CSPs and the cyber security teams (CSTs); decides what business-side changes need CST review |
| Fleet security director; SGI program manager | Own the SGI programs in Nuclear Generation and in Engineering and Radiation Services |
| Group internal audit | Independently assesses common controls once and samples division controls |
| Nuclear Oversight | Independent 24-month security program reviews that include the CSPs (10 CFR 73.55(m)) |
| All workforce | Follow group policy, their division supplement, and the site rules where they work; report suspected incidents immediately |

## 4. Policy statements
4.1 The group must maintain one information security program aligned to NIST CSF 2.0 for all business systems, consistent with the regulator-approved programs named in section 2. (PM-1; GV.PO-01)

4.2 The Group CISO is accountable for the program. Each division must name a security and compliance lead in writing. (PM-2; GV.RR-02)

4.3 Each division and corporate must complete a risk analysis at least annually and after major changes, using NIST SP 800-30 Rev. 1. Division risks that cross divisions, sit in shared services, or need a group decision must roll up to the group register. Nuclear Generation must give the fleet cyber security program manager every business-side risk that could reach a CDA, so the CSP risk process can consider it. (RA-3; PM-9; ID.RA-01; 73.54(d)(2))

4.4 **Risk acceptance authority:** Low, the division security and compliance lead; Moderate, the division president (the Chief Nuclear Officer for Nuclear Generation); High, the Group Chief Risk Officer with the Group CISO, reported to the board risk committee; Very High, the board risk committee only. **A deficiency in a station CSP, the SGI program, or the Part 37 program, or any risk that could affect nuclear or worker safety, cannot be accepted.** It must be entered in the station CAP (or the facility corrective action log) and corrected. (PM-9; GV.RM-01; 73.77(b)(1))

4.5 **Division supplements.** A division may add stricter requirements in a written supplement. A supplement must not weaken group policy. Each supplement must be re-aligned within 90 days after a group policy changes, and each division security and compliance lead must attest alignment every year. (PL-1; GV.PO-02)

4.6 **Common controls.** Corporate control providers must maintain the common control catalog. Each division must document, for each of its systems, which controls it inherits and which responsibilities remain with the division, and must confirm that documentation every year. (PL-2; PM-10; CA-2; GV.RR-02)

4.7 **No shared-service path to protected systems.** No group shared service (SYS-G1 identity, SYS-G2 SOC tools, SYS-G3 cloud and network) may connect to, authenticate users to, or hold data from a CDA, an SGI stand-alone system, the NERC CIP Electronic Security Perimeter, or the Part 37 vault security systems, unless the owning program approves it in writing. (SC-7; AC-4; GV.PO-01; 73.54(c)(2))

4.8 **Changes that touch protected programs.** A business-side change that could affect a CSP control (for example the kiosk update server, the plant data replicas, or the receive side of a one-way device), plant maintenance decisions, or site security must be screened by the fleet cyber security program manager and, for Nuclear Generation, under the 10 CFR 73.58 safety/security interface process before it is made. (CM-4; RA-3; ID.RA-07; 73.58(b)-(c))

4.9 **Sanctions.** Workforce members who violate security policies must be sanctioned in proportion to intent and harm. HR must document every sanction. Violations involving SGI, access authorization information, or Part 37 information are also reported to the owning program. (PS-8; GV.RR-04)

4.10 **Third parties.** No vendor or intercompany service provider may hold group or customer data, or have access to group systems, without a contract with security terms and a security review. Contracts with access authorization service vendors must reserve the audit rights required by 10 CFR 73.56(n)(3)-(4). (SA-9; SA-4; GV.SC-05)

4.11 **Evaluation.** Group internal audit must assess common controls at least annually and sample each division's controls. Results feed the POA&M and the risk registers. Nuclear Oversight's 73.55(m) reviews remain the independent review of the CSPs. (CA-2; CA-7; ID.IM-01)

4.12 **Exceptions** to any group policy or supplement must be requested in writing, risk-rated, approved under 4.4, recorded in the division register, and limited to 12 months or less. Exceptions are not available for the items in the last sentence of 4.4. (PL-1)

4.13 Security policies, procedures, risk analyses, assessments, and required actions must be retained for at least 6 years, or longer where a regulation requires (for example, 73.54(h) records until license termination). (SI-12)

4.14 **AI systems.** No AI system that supports maintenance, engineering, safety, security, or decisions about people may be deployed or materially changed without registration in the group AI inventory and approval under the Group AI Standard (P10). (RA-3; PL-2; GV.RM-01)

## 5. Compliance and enforcement
Violations are handled under 4.9. Compliance is checked through the annual common control assessment and division samples (P07), the annual supplement attestations, quarterly access certifications, and the regulator-approved program reviews.

## 6. Exceptions
Exceptions follow section 4.12.

## 7. Related documents
POL-02 to POL-05; `division-supplements.md`; common control catalog (P02); group and division risk registers (P01); regulation-by-division matrix (P03); Group AI Standard (P10); station CSPs and implementing procedures (held by the CSTs); 10 CFR 73.54, 73.58, 73.21-73.22, 73.56; 10 CFR Part 37.
