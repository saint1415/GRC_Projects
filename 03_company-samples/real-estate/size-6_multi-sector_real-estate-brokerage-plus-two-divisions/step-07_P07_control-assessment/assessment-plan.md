# Security Assessment Plan and Summary: Cris Santos Company Holdings | Real Estate | Multi-Sector

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. |
| Scope | Group common controls (SYS-G1 to SYS-G5 and group HR), the TMCC (P02 SSP), and samples of Residential Brokerage, Mortgage and Title, and Homebuilding controls |
| Tier / Vertical | Multi-Sector / Real Estate and Rental and Leasing (focus division: Residential Brokerage) |
| Procedures | NIST SP 800-53A Rev. 5, Release 5.2.0 (determination statements from `00_universal-framework/frameworks/sp800-53a_objectives.csv`) |
| Assessor and independence | Group internal audit, which reports to the board audit committee and neither designs nor operates the controls. Division security and compliance leads acted as liaisons only |
| Assessment window | 2026-07-06 to 2026-08-28 |
| Also satisfies | The regular testing of key controls that Home Loans and Title must perform under 16 CFR 314.4(d)(1), and evidence for the Qualified Individual's annual reports (314.4(i)) |

## 1. Approach: assess common controls once, then sample divisions
Most safeguards in all three divisions come from the same corporate providers. Testing them three times would waste effort and give three slightly different answers. So:
1. **Common controls** in the P02 common control catalog were assessed **once**, across all divisions, with samples drawn from every division and from the contractor agent tier (for example, the joiner-mover-leaver sample took events from all three divisions and 40 agent departures).
2. **The TMCC's** system-specific controls were assessed because it is the SSP system and carries the top group risk (GR-01).
3. **Division samples** covered controls each division operates itself, chosen from its High risks and its P03 gaps. Division findings are reported to that division, not averaged into the group.

**SC-37 (out-of-band payee verification) was assessed in four scopes:** the SYS-G5 common control and the actual practice in each division. The same control can be configured centrally and still be bypassed by a division, and that is exactly what the fraud history suggests. Homebuilding was also sampled on governance controls (CA-2, PL-1) because its inheritance is undocumented and it has no supplement (scenario gap 5).

## 2. Controls selected
**42 control assessments** (37 distinct controls; SC-37 was assessed in four scopes, and AC-2 and IA-5 in two), **279 determination statements**.

| Scope | Controls | Statements | Why selected | Depth / coverage |
|---|---|---|---|---|
| Common control (SYS-G1 identity) | AC-2, AC-2(3), AC-2(12), IA-2(1), IA-2(2) | 34 | GR-02; scenario gap 1 | Focused / Comprehensive (all divisions and the contractor tier sampled) |
| Common control (Group HR) | PS-4, AT-2 | 15 | Terminations and training for 45,000 employees and 52,000 agents | Focused / Focused |
| Common control (SYS-G2 SOC) | SI-4, AU-6, IR-3, IR-4, IR-6, IR-8, RA-5 | 57 | GR-04, GR-09; scenario gaps 3 and 7 | Focused / Comprehensive |
| Common control (SYS-G3 cloud) | CP-9, SC-7, SC-8, SC-28 | 14 | GR-03; backups and network protection | Focused / Focused |
| Common control (SYS-G4 email) | SI-8 | 5 | GR-01; the business email compromise channel | Focused / Focused |
| Common control (SYS-G5 payments hub) | SC-37, AC-3(2) | 2 | GR-01 (High); scenario gap 2 | Comprehensive / Comprehensive |
| TMCC (SSP system) | AC-3, AC-4, AC-21, IA-5, IA-12, SI-7, SA-11 | 34 | GR-01, GR-05; scenario gap 4 | Comprehensive / Comprehensive |
| Division sample: Residential Brokerage | AC-6, PS-7, AC-20, SI-12, SC-37 | 14 | BR-001 to BR-010, BR-018; P03 gaps G-009 to G-018 | Focused / Focused (6 states, 40 agents, 45 payment changes) |
| Division sample: Mortgage and Title | SC-37, CP-2, MA-4, SA-9 | 39 | MT-001, MT-008, MT-013, MT-015 | Focused / Focused (60 Title wires, 4 vendors) |
| Division sample: Homebuilding | CA-2, PL-1, IA-5, AC-2, SC-37 | 65 | HB-001, HB-003, HB-004, HB-012; scenario gaps 5 and 8 | Focused / Focused (30 homes, 25 bank changes) |
| **Total** | **42** | **279** | | |

## 3. Methods and objects
- **Examine:** identity governance and PAM configuration, the contractor tier and its exception register, SIEM data sources and rules, SYS-G5 payee verification and approval settings, landing-zone policies, backup and immutability settings, the TMCC integration flow register, contingency plans, vendor contracts and the intercompany services agreement, smart-home role reports, and the policy register.
- **Interview:** group identity, SOC, cloud, and collaboration directors; the Group Treasurer; the TMCC system owner and the President, Title; the Brokers of Record for 6 states; the Homebuilding chief financial and operating officers; the Group General Counsel and the Group Chief Privacy Officer.
- **Test:**
  - a joiner-mover-leaver sample of 60 events across divisions, 25 employee terminations, and 40 agent departures;
  - a sign-in from an anonymizing network with a test agent account, and a password-only sign-in with an agent account still under the expired exception;
  - a simulated payee change in the SYS-B1 test tenant to see whether the SOC is alerted;
  - samples of 120 escrow and trust wires (dual approval), 60 Title disbursement wires, 20 brokerage refunds, 15 owner payout changes, 10 commission changes, and 25 trade partner bank changes (payee verification);
  - a consumer cross-transaction access attempt and an instruction change in the SYS-B2 test environment;
  - restores of the SYS-B2 database and a SYS-H1 dataset from the immutable vault;
  - a TLS scan of 70 endpoints, an external exposure scan, and a lookalike-domain test message;
  - smart-home device checks on 30 sampled homes, with the homeowners' permission.

## 4. Rules of engagement
- No testing that could move money or delay a closing. Payment tests used records and test environments; no live wire was altered.
- No customer information left group systems. Screenshots were redacted.
- Smart-home checks were read-only and done with homeowner consent.
- The assessor would stop and notify the Group CISO on any critical exposure. Two findings were escalated during fieldwork (the shared installer passcode and the payoff without portal verification); both are now in remediation.

## 5. Results summary
| Scope | Satisfied | Other than satisfied | Total |
|---|---|---|---|
| Common controls | 108 | 19 | 127 |
| TMCC (SSP system) | 30 | 4 | 34 |
| Division sample: Residential Brokerage | 8 | 6 | 14 |
| Division sample: Mortgage and Title | 32 | 7 | 39 |
| Division sample: Homebuilding | 55 | 10 | 65 |
| **Total** | **233** | **46** | **279** |

**Common controls are mostly strong.** 108 of 127 common statements were satisfied. Administrator MFA (IA-2(1)), terminations (PS-4), vulnerability management (RA-5), backups and network protection (CP-9, SC-7, SC-8, SC-28), email protection (SI-8), and dual authorization for every escrow and trust wire (AC-3(2)) had no findings. The common findings sit in three places:
- **the contractor agent tier** (AC-2, AC-2(3), AC-2(12), IA-2(2), AT-2): no MFA for about 9,900 agents, late removal, and no sign-in analytics;
- **detection in division applications** (SI-4, AU-6): a simulated payee change in SYS-B1 raised no alert;
- **cross-division incident handling and notice** (IR-3, IR-4, IR-6, IR-8): the matrix has never been exercised and Homebuilding's fraud losses never reached the SOC (scenario gap 7).

**SC-37 tells the main story.** The payee verification capability exists in SYS-G5, but in practice:
- *Mortgage and Title:* 59 of 60 Title wires had a callback record; one payoff was paid on an emailed letter.
- *Residential Brokerage:* none of 45 sampled refunds, owner payout changes, or commission changes were verified out of band.
- *Homebuilding:* all 25 trade partner bank changes were accepted from email with one approver.

**The TMCC itself is well built.** Identity proofing before instructions (IA-12), instruction integrity checks (SI-7), access enforcement (AC-3), and secure development (SA-11) were all satisfied. Its findings are about data leaving it sideways (AC-4, AC-21, scenario gap 4) and two old integration keys (IA-5).

**Division samples:**
- *Residential Brokerage:* office-wide visibility (AC-6), late departure reporting by managing brokers (PS-7), unprotected personal devices (AC-20), and indefinite retention (SI-12).
- *Mortgage and Title:* the title production vendor's RTO (CP-2), vendor support outside PAM (MA-4), and the intercompany agreement (SA-9).
- *Homebuilding:* no inheritance or supplement (CA-2, PL-1), smart-home shared passcodes and retained builder roles (IA-5, AC-2, scenario gap 8).

**Controls fully other than satisfied** (every statement failed): AC-2(12) and IA-2(2) (common, SYS-G1); IR-3 (common, SYS-G2); SC-37 in all four scopes; and AC-4 and AC-21 (TMCC); AC-6 (Brokerage). All but AC-2(12) and AC-21 have only one determination statement.

29 of the 42 control assessments had at least one statement other than satisfied. All are in `poam.csv`.

## 6. POA&M
`poam.csv` has **22 items**: 17 from this assessment (POAM-001 to POAM-014 and POAM-016 to POAM-018; several also close P03 gaps) and 5 from the P03 gap analysis alone (POAM-015 and POAM-019 to POAM-022). By risk: 6 High (POAM-001 agent MFA, POAM-003 payee verification, POAM-004 application log monitoring, POAM-016 smart-home access, POAM-019 AVM quality control, POAM-020 tenant screening) and 16 Moderate. Status: 14 In progress, 8 Open. Each item names the related P01 risks.

## 7. Deliverables and acceptance
`assessment-results.csv` (279 rows, with an `assessment_scope` column), `poam.csv` (22 items), and this plan and summary. Results were presented to the board risk committee and accepted by the Group CISO and the Group Chief Risk Officer on 2026-09-17, and summarized in the Qualified Individual's annual reports to the boards of Home Loans and Title the same day. Division presidents accepted their division findings the same week.
