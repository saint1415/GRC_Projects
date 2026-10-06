# Security Assessment Plan and Summary: Cris Santos Company Holdings | Professional Services | Multi-Sector

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. (corporate shared services, CPA and Tax Services including CPA Partners, Wealth, and Practice Cloud) |
| Scope | Group common controls (SYS-G1 to SYS-G4 and group HR), the Tax Preparation and Client Portal Platform (TPCP, the P02 SSP system), and samples of Tax and Advisory, CPA Partners, Wealth, and Practice Cloud controls |
| Tier / Vertical | Multi-Sector / Professional, Scientific, and Technical Services (focus division: CPA and Tax Services) |
| Procedures | NIST SP 800-53A Rev. 5, Release 5.2.0 (determination statements from `00_universal-framework/frameworks/sp800-53a_objectives.csv`) |
| Assessor and independence | Group internal audit, led by the Chief Audit Executive, who reports to the board audit committee. Internal audit neither designs nor operates the controls it assessed. Division security and compliance leads acted as liaisons only. Practice Cloud's SOC 2 report is issued by an unaffiliated CPA firm; CPA Partners did not take part, because an attest firm examining controls it relies on would not be independent |
| Assessment window | 2026-07-06 to 2026-08-28 |
| Also satisfies | The regular testing of safeguards in 16 CFR 314.4(d)(1) for Tax and Advisory; the annual review of Wealth's compliance policies and procedures (17 CFR 275.206(4)-7(b)) for the controls sampled; the HIPAA evaluation (45 CFR 164.308(a)(8)) for CPA Partners' inherited controls, once POAM-016 documents them |

## 1. Approach: assess common controls once, then sample divisions
All three divisions and CPA Partners rely on the same corporate identity, SOC, cloud, and email services. Testing those controls in each division would repeat the same work and could produce four slightly different answers. So:
1. **Common controls** in the P02 common control catalog were assessed **once**, with samples drawn from every division. For example, the joiner-mover-leaver sample took 60 events across all divisions, and the seasonal sample covered tax offices in 9 states.
2. **The TPCP's** system-specific controls were assessed because it is the SSP system and carries two of the group's High risks (GR-01 tax-to-wealth sharing and GR-02 business email compromise).
3. **Division samples** covered controls each division or CPA Partners operates itself, chosen from its High risks and its P03 gaps. Division findings are reported to that division and are not averaged into the group result.

CPA Partners was sampled on governance controls (PL-1, CA-2) because its inheritance of group controls is undocumented and its supplement has drifted (scenario gap 7).

## 2. Controls selected
**45 control assessments** (37 distinct controls), **270 determination statements**. Seven controls were assessed in more than one scope because each division operates its own version: SA-9 (three scopes), and AC-3, AC-4, CM-4, IA-8, IR-8, and SA-11 (two scopes each).

| Scope | Controls | Statements | Why selected | Depth / coverage |
|---|---|---|---|---|
| Common control (SYS-G1 identity) | AC-2, AC-2(3), AC-6(5), IA-2, IA-2(1) | 34 | GR-05, GR-18; scenario gap 2 (seasonal identity) | Focused / Comprehensive (all divisions sampled) |
| Common control (Group HR) | PS-3, PS-4, AT-2 | 18 | GR-05; 45,000 permanent and about 11,000 seasonal users | Focused / Focused |
| Common control (SYS-G2 SOC) | SI-4, IR-3, IR-4, IR-6, IR-8, RA-5 | 54 | GR-02, GR-03, GR-11; scenario gaps 3 and 6 | Focused / Comprehensive |
| Common control (SYS-G3 cloud and network) | CP-9, SC-7, SC-8, SC-12, SC-28, CM-6 | 22 | GR-06, GR-15; immutable backups and guardrails | Focused / Focused |
| Common control (SYS-G4 email) | AC-4 | 1 | GR-02; the forwarding exception list (scenario gap 3) | Focused / Comprehensive (all 212 exceptions) |
| TPCP (SSP system) | AC-3, AC-6, AC-4, AC-21, PT-4, AU-6, CM-4, SA-11, CP-4, IA-8 | 26 | GR-01 and GR-02 (High); TX-002, TX-003, TX-004, TX-008, TX-009, TX-014; scenario gaps 1 and 4 | Comprehensive / Comprehensive |
| Division sample: Tax and Advisory | SA-9, MP-6, CP-2 | 34 | TX-010, TX-015, TX-021; P03 G-032 | Focused / Focused (4 tier 1 vendors; 40 lease returns) |
| Division sample: CPA Partners | PL-1, CA-2 | 28 | GR-09, TX-024, TX-025; scenario gap 7 | Focused / Focused |
| Division sample: Wealth | SA-9, IR-8, AU-11, IA-8 | 25 | WM-001, WM-003, WM-006, WM-017; P03 WM-G06, WM-G10, WM-G16 | Focused / Focused |
| Division sample: Practice Cloud | SA-9, CM-3, CM-4, SA-11, AC-3 | 28 | SW-001, SW-002, SW-003 (High and Moderate); scenario gap 5 | Focused / Focused |
| **Total** | **45** | **270** | | |

## 3. Methods and objects
- **Examine:** identity governance and PAM configuration; HR and background check records; SIEM data sources and use cases; landing-zone guardrails; backup and immutability settings; mail flow rules and the forwarding exception list; the SYS-T1 role matrix and the referral interface specification and code; IRC 7216 consent templates; change and release records for AI-002 and the Practice Cloud AI document intake feature; vendor files and intercompany agreements; the CPA Partners supplement; Wealth's Regulation S-P response program.
- **Interview:** group identity, SOC, cloud platform, and collaboration services directors; the Tax division technology director and security and compliance lead; 6 integrated planning coordinators; the client accounting services director; the CPA Partners risk and quality partner; the Wealth Chief Compliance Officer; the Practice Cloud CISO and chief technology officer.
- **Test:**
  - a joiner-mover-leaver sample of 60 events across divisions, 25 permanent terminations, and 60 seasonal season-end events;
  - background check and training dates matched to activation dates for 120 seasonal staff;
  - a hardware-key administrator sign-in and federation checks on 48 applications;
  - a simulated inbox rule and external forwarding on a test tax office mailbox (with SOC approval) to test detection;
  - 80 referral records traced from SYS-T1 to the Wealth CRM and compared with signed consent dates and template content;
  - sign-ins under 5 TPCP roles and a client portal sign-in without MFA (blocked);
  - restores of 3 SYS-T1 databases from the provider B vault;
  - a TLS scan of 70 endpoints and an external exposure scan of both landing zones;
  - a step-up authentication test for a Wealth portal transfer request;
  - cross-tenant access attempts in 4 Practice Cloud test tenants.

## 4. Rules of engagement
- No testing during market hours on Wealth trading systems, and no testing that could delay a client return, payroll, or transfer. Tests ran in non-production tenants where possible. The mailbox detection test used a dedicated test mailbox.
- No tax return information, customer information, or PHI left group systems. Screenshots were redacted. Referral records were reviewed in place by an auditor who had completed IRC 7216 training.
- The assessor would stop and notify the Group CISO on any critical exposure. None was found. The referral interface finding (AC-4) was reported to the Group CISO and the Chief Tax Officer on 2026-08-14, the day it was confirmed, and transfers without a recorded consent were suspended from 2026-10-15 (POAM-009).

## 5. Results summary
| Scope | Satisfied | Other than satisfied | Total |
|---|---|---|---|
| Common controls | 110 | 19 | 129 |
| TPCP (SSP system) | 15 | 11 | 26 |
| Division sample: Tax and Advisory | 30 | 4 | 34 |
| Division sample: CPA Partners | 24 | 4 | 28 |
| Division sample: Wealth | 20 | 5 | 25 |
| Division sample: Practice Cloud | 23 | 5 | 28 |
| **Total** | **222** | **48** | **270** |

**Common controls are sound where they were built once for everyone.** 110 of 129 common statements were satisfied. Privileged access (AC-6(5)), administrator MFA (IA-2(1)), inactive accounts (AC-2(3)), cloud protection (CP-9, SC-7, SC-8, SC-12, SC-28), and vulnerability management (RA-5) had no findings. The common findings are about **seasonal staff** (AC-2, PS-3, PS-4, AT-2; scenario gap 2), **tax office email** (IA-2, SI-4, and the SYS-G4 forwarding exceptions under AC-4; gap 3), and **cross-division incident handling and notification** (IR-3, IR-4, IR-6, IR-8; gap 6).

**The TPCP is where the risk is.** 11 of its 26 statements were other than satisfied. The referral interface sends tax return information to Wealth without checking a recorded consent (AC-4, AC-21, PT-4: 9 of 80 transfers preceded the consent), office managers and coordinators see more than they need (AC-6), portal bulk downloads and refund bank-field changes are not reviewed (AU-6), and the AI tools were changed and tested without the reviews the Group AI Standard requires (CM-4, SA-11). Role-based access (AC-3) and client portal MFA (IA-8) were satisfied.

**Division samples:**
- *Tax and Advisory:* tier 1 vendors, including the AI-001 model provider, are reviewed only at onboarding (SA-9); 6 of 40 leased printer-scanners went back without an overwrite certificate (MP-6); and the client accounting services plan does not cover running payroll through a payroll SaaS outage (CP-2).
- *CPA Partners:* its 2023 supplement is not aligned to the 2026 group policies or to HIPAA subcontractor needs (PL-1), and the group controls it inherits have never been identified or confirmed (CA-2).
- *Wealth:* affiliates are outside its service provider oversight, and the integrated planning agreement has no 72-hour notice term (SA-9, IR-8); AI meeting summaries are not in the archive (AU-11). Client portal step-up authentication (IA-8) passed.
- *Practice Cloud:* the AI document intake feature added a model provider without the sub-processor notice, privacy analysis, or monitoring its commitments require (SA-9, CM-3, CM-4), and has had no prompt-injection testing (SA-11). Tenant isolation tests (AC-3) passed.

**Controls fully other than satisfied** (every statement failed): IR-3 (common), AC-4 (SYS-G4), AC-6, AC-4, AC-21, PT-4, and CM-4 (TPCP), and AU-11 (Wealth). All have one or two determination statements.

32 of the 45 control assessments had at least one statement other than satisfied. All are in `poam.csv`.

## 6. POA&M
`poam.csv` has **24 items**: 21 from this assessment (POAM-001 to POAM-021) and 3 that trace directly to the P03 gap analyses (POAM-022 to POAM-024). By risk: 5 High (POAM-002 legacy authentication on office intake mailboxes, POAM-004 tax office email monitoring, POAM-009 referral interface consent check, POAM-020 Practice Cloud AI feature commitments, POAM-022 IRC 7216 consent redesign), 17 Moderate, and 2 Low. Status: 17 In progress, 7 Open. Each item names its scope and the related P01 risks.

**Before the 2027 filing season.** POAM-001, POAM-002, POAM-003, POAM-010, POAM-011, and POAM-012 are due by 2027-01-04 or earlier, because the season starts in mid-January.

## 7. Deliverables and acceptance
`assessment-results.csv` (270 rows, with an `assessment_scope` column), `poam.csv` (24 items), and this plan and summary. Results were presented to the board risk committee and accepted by the Group CISO and the Group Chief Risk Officer on 2026-09-10. Division presidents and the CPA Partners managing partner accepted their findings the same week. The Qualified Individual's annual report to the Tax and Advisory board of managers (due 2026-10-15) summarizes the Tax and Advisory and common control results (16 CFR 314.4(i)).
