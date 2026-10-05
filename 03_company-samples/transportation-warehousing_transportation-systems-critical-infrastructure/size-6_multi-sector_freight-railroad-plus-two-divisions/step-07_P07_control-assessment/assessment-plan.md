# Security Assessment Plan and Summary: Cris Santos Company Holdings | Transportation Systems | Multi-Sector

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. |
| Scope | Group common controls (SYS-G1, SYS-G2, SYS-G3, group HR, group governance and third-party risk), the Train Dispatching and PTC Back Office Platform (TDPB, the P02 SSP system), and samples of Freight Railroad, Transload and Wholesale, and Real Estate controls |
| Tier / Vertical | Multi-Sector / Transportation Systems (focus division: Freight Railroad) |
| Procedures | NIST SP 800-53A Rev. 5, Release 5.2.0 (determination statements from `00_universal-framework/frameworks/sp800-53a_objectives.csv`) |
| Assessor and independence | Group internal audit, with co-sourced OT specialists, reporting functionally to the board audit committee. It neither designs nor operates the controls. Division security and compliance leads acted as liaisons only |
| Assessment window | 2026-07-06 to 2026-08-28 (NOC walkthrough 2026-07-15; DC-2 and backup NOC 2026-07-22; CR-13 PTC wayside visit 2026-07-29; terminals 2026-08-05 and 2026-08-06; buildings 2026-08-12) |
| Also satisfies | The 2026 assessments under the Covered Railroads' TSA Cybersecurity Assessment Plan (SD 1580/82-2022-01E III.F.2.a and III.F.2.d); results feed the annual CAP report due 2026-11-14 |

## 1. Approach: assess common controls once, then sample divisions
Most safeguards in all three divisions come from the same corporate providers. Testing them three times would waste effort and give three slightly different answers. So:
1. **Common controls** in the P02 common control catalog were assessed **once**, across all divisions, with samples drawn from every division (for example, the joiner-mover-leaver sample took events from all three, and the termination sample included acquired terminals).
2. **TDPB's** system-specific controls were assessed because it is the SSP system, holds the Covered Railroads' Critical Cyber Systems, and carries High risks (RR-002, RR-004). The selection also covers CIP measures in the one-third due for assessment in 2026.
3. **Division samples** covered controls each division operates itself, chosen from its High risks and its P03 gaps. Division findings are reported to that division, not averaged into the group.

Governance controls (PL-1, CA-2) were sampled on Transload and Wholesale and Real Estate because those divisions have no supplements (scenario gap 9) and undocumented inheritance (gap 10).

## 2. Controls selected
**35 control assessments** (29 distinct controls; AC-17, AC-2, CM-8, SA-9, SC-7 were assessed in two scopes), **276 determination statements**.

| Scope | Controls | Statements | Why selected | Depth / coverage |
|---|---|---|---|---|
| Common control (SYS-G1 identity) | AC-2, AC-2(3), AC-6(5), IA-2(1), IA-5 | 42 | Every division signs in through SYS-G1; GR-11; scenario gap 4 | Focused / Comprehensive (all divisions sampled) |
| Common control (Group HR) | PS-4, AT-2 | 15 | Terminations and training for 45,000 users; TSA training records | Focused / Focused |
| Common control (SYS-G2 SOC) | SI-4, AU-6, IR-3, IR-6, IR-8, RA-5 | 44 | GR-02, GR-03, GR-14; CIP monitoring measures; scenario gap 8 | Focused / Comprehensive |
| Common control (SYS-G3 network, data centers, and cloud) | CP-9, SC-7, CM-6 | 18 | GR-02; immutable backups and segmentation the CIP relies on | Focused / Focused |
| Common control (group governance and third parties) | PL-1, CA-2, SA-9 | 34 | Scenario gaps 9 and 10; GR-06 to GR-08; sampled on Transload and Wholesale and Real Estate | Focused / Focused |
| SSP system (TDPB) | AC-4, CA-3, CM-8, SI-2, CP-4, AU-11, AC-21 | 33 | GR-01, RR-002, RR-004 (High); scenario gaps 1, 2, and 12; CIP measures due for the 2026 one-third | Comprehensive / Comprehensive |
| Division sample: Freight Railroad (field and NOC) | AC-17, CP-2 | 28 | RR-008, RR-010, RR-015; field vendor access and manual operations | Focused / Focused (4 railroads, 12 crossing sites) |
| Division sample: Transload and Wholesale | SC-7, SI-3, AC-17, CM-8 | 24 | TW-001, TW-002 (High); scenario gap 5 | Focused / Focused (2 terminals) |
| Division sample: Real Estate | SC-7, AC-2, SA-9 | 38 | RE-001, RE-002; scenario gap 7 | Focused / Focused (2 buildings; all 5 vendors) |
| **Total** | **35** | **276** | | |

## 3. Methods and objects
- **Examine:** identity governance and PAM configuration, the CTC shared account register, SIEM sources and use cases, DMZ and hub firewall rules, the OT asset inventory, patch status and KEV tracking, DR test reports, the CIRP and CIP (SSI, reviewed in the restricted room), file share permissions, division supplements and inheritance records, vendor contracts and assurance reports.
- **Interview:** Group CISO; Director, Rail OT Security; Director, NOC; PTC Program Director; Group SOC Director; NOC managers at 4 railroads; terminal managers at 2 terminals; Director, Facilities Technology; Federal contracts compliance manager; Group General Counsel.
- **Test:**
  - a joiner-mover-leaver sample of 60 events across divisions, and 25 terminations;
  - a hardware-key administrator sign-in and 20 recorded PAM sessions;
  - a segmentation test from the corporate network toward the NOC operations zone (blocked) and a capture at the TMS interface server (found the SYS-G5 flow);
  - authenticated scans of CAD and PTC servers;
  - restores of the CAD and TOS databases into the clean-room recovery account;
  - segmentation tests at 2 terminals (a laptop on the office network of the acquired terminal reached rack controllers);
  - an external exposure scan of building address space (found 9 BAS controllers);
  - an access test to the corporate share from a Real Estate user account (SSI readable).

## 4. Rules of engagement
- No testing that could affect train movement, PTC, signals, hazmat loading, or building life safety. OT tests were passive or run in maintenance windows with the NOC and terminal managers present.
- The CIP, CIRP, and CAP were reviewed as SSI: in a restricted room, by assessors who are covered persons with a need to know.
- The assessor would stop and notify the Group CISO on any critical exposure. Two were escalated the same day they were found: the CTC shared passwords known to former administrators (2026-07-15), whose rotation needs CTC vendor support because the accounts are embedded in code unit configurations (POAM-002, 2026-10-15), and the internet-exposed BAS controllers (2026-08-12), 7 of which were taken off the internet by 2026-08-20 (POAM-012).

## 5. Results summary
| Scope | Satisfied | Other than satisfied | Total |
|---|---|---|---|
| Common controls (5 providers) | 134 | 19 | 153 |
| SSP system (TDPB) | 20 | 13 | 33 |
| Division sample: Freight Railroad (field and NOC) | 25 | 3 | 28 |
| Division sample: Transload and Wholesale | 13 | 11 | 24 |
| Division sample: Real Estate | 27 | 11 | 38 |
| **Total** | **219** | **57** | **276** |

**Common controls are strong.** 134 of 153 common statements were satisfied. MFA and PAM (IA-2(1), AC-6(5)), inactive account handling (AC-2(3)), training (AT-2), backups (CP-9), segmentation of the corporate network from the NOC operations zone (SC-7), and cloud guardrails (CM-6) had no findings. The common findings are about **shared OT accounts** (AC-2, IA-5), **OT monitoring coverage** (SI-4, AU-6), **cross-division notification** (IR-3, IR-6, IR-8, scenario gap 8), and the two divisions that sit **outside the platform** (PS-4, RA-5, PL-1, CA-2).

**TDPB is where the directive gaps are.** 13 of 33 statements were other than satisfied: the SYS-G5 flow was never approved (AC-4, CA-3; scenario gap 1), PTC servers are unpatched without mitigations (SI-2; gap 2), CTC and PTC logs are kept 30 days (AU-11), and SSI is readable across divisions (AC-21; gap 12).

**Division samples:**
- *Freight Railroad:* crossing monitor vendor modems are an unauthorized remote access path (AC-17), and manual CTC dispatch is unproven at 5 railroads (CP-2). The RSSM 30-minute fallback was tested and passed.
- *Transload and Wholesale:* acquired terminals are flat, unmonitored, and without EDR (SC-7, SI-3), the rack vendor has always-on access (AC-17), and there is no terminal OT inventory (CM-8).
- *Real Estate:* internet-exposed BAS controllers (SC-7), shared vendor logins (AC-2), and vendors not bound or monitored (SA-9).

**Controls fully other than satisfied** (every statement failed): IR-3 (SOC), AC-4 (TDPB), AU-11 (TDPB), AC-21 (TDPB). Each has only one or two determination statements.

28 of the 35 control assessments had at least one statement other than satisfied. All are in `poam.csv`.

## 6. POA&M
`poam.csv` has **25 items**: 19 from this assessment, 5 from the P03 gap analyses (POAM-018 to POAM-022), and 1 from the P10 AI assessment (POAM-023). By risk: 8 High (POAM-001, POAM-002, POAM-003, POAM-004, POAM-009, POAM-011, POAM-012, POAM-018), 17 Moderate, and 0 Low. Status: 18 In progress, 7 Open. Each item names the related P01 risks.

## 7. Deliverables and acceptance
`assessment-results.csv` (276 rows, with an `assessment_scope` column), `poam.csv` (25 items), and this plan and summary. The report was issued on 2026-09-04. Results were presented to the board safety, security, and risk committee and the audit committee on 2026-09-10 and accepted by the Group CISO and the Group Chief Risk Officer. Division presidents accepted their division findings the same week. The Vice President, Rail Cybersecurity uses the TDPB and common control results in the 2026 CAP annual report to TSA (SSI).
