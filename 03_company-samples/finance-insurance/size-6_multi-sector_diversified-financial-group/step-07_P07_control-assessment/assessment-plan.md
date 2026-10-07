# Security Assessment Plan and Summary: Cris Santos Company Holdings | Finance and Insurance | Multi-Sector

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. |
| Scope | Group common controls (SYS-G1, SYS-G2, SYS-G3, group HR), the Core and Digital Banking Platform (P02 SSP), and samples of Banking, Financial Software, and Commercial Real Estate controls |
| Tier / Vertical | Multi-Sector / Finance and Insurance (focus division: Banking) |
| Procedures | NIST SP 800-53A Rev. 5, Release 5.2.0 (determination statements from `00_universal-framework/frameworks/sp800-53a_objectives.csv`) |
| Assessor and independence | Group internal audit (third line). The Chief Audit Executive reports to the holding company and bank audit committees and no front line executive oversees internal audit (12 CFR 30 App. D I.E.8). Internal audit neither designs nor operates the controls it tested. Division security and compliance leads acted as liaisons only |
| Assessment window | 2026-07-01 to 2026-08-31 |
| Also satisfies | Regular testing of key controls by independent staff under 12 CFR 30 App. B III.C.3 (bank) and 12 CFR 225 App. F III.C.3 (holding company and nonbank subsidiaries) |

## 1. Approach: assess common controls once, then sample divisions
Most safeguards in all three divisions come from the same corporate providers. Testing them three times would waste effort and produce three slightly different answers. So:
1. **Common controls** in the P02 common control catalog were assessed **once**, across all divisions, with samples drawn from every division (for example, the joiner-mover-leaver sample took events from all three).
2. **The CDBP's** system-specific controls were assessed because it is the SSP system and carries top group risks (GR-02, GR-04).
3. **Division samples** covered controls each division operates itself, chosen from its High risks and its P03 gaps. Division findings are reported to that division, not averaged into the group.

Commercial Real Estate was sampled for the first time. Its inheritance is undocumented and its policies have drifted (scenario gap 2), so internal audit chose governance and funding controls (PL-1, CA-2, AT-3, AU-6).

## 2. Controls selected
**40 control assessments** (36 distinct controls: SA-9 was assessed in three scopes, and AT-3 and AU-6 in two), **269 determination statements**.

| Scope | Controls | Statements | Why selected | Depth / coverage |
|---|---|---|---|---|
| Common control (SYS-G1 identity) | AC-2, AC-2(3), AC-6(5), IA-2, IA-2(1), IA-5, AC-12 | 45 | Every division's access; GR-02 | Focused / Comprehensive (all divisions sampled) |
| Common control (Group HR) | PS-4, AT-2 | 15 | Terminations and training for 45,000 users | Focused / Focused |
| Common control (SYS-G2 SOC) | SI-4, IR-4, IR-6, IR-8, IR-3, RA-5 | 54 | GR-02, GR-03; scenario gap 5 | Focused / Comprehensive |
| Common control (SYS-G3 infrastructure) | CP-9, SC-7, SC-8, SC-12, SC-28, CM-6 | 22 | GR-06; immutable backups and guardrails | Focused / Focused |
| CDBP (SSP system) | AC-3, AC-5, AC-6, IA-8, AU-6, CP-4, SA-9 | 19 | GR-04, FS-001 (High); scenario gaps 3 and 6 | Comprehensive / Comprehensive |
| Division sample: Banking | RA-3, CP-2, AT-3, SA-9 | 47 | BR-003, BR-013; risk appetite link (App. D II.E) | Focused / Focused (2 operations centers, 3 contact centers) |
| Division sample: Financial Software | CM-3, CM-4, SA-11, SA-9 | 27 | FS-008 (High); scenario gap 4 | Focused / Focused |
| Division sample: Commercial Real Estate | PL-1, CA-2, AT-3, AU-6 | 40 | RR-001 (High); scenario gaps 1 and 2 | Focused / Focused (2 closing offices, 30 funding files) |
| **Total** | **40** | **269** | | |

## 3. Methods and objects
- **Examine:** identity governance and PAM configuration, session policies, SIEM data sources and use cases, landing-zone and data center firewall policies, backup and immutability settings, key inventories, support console roles, contingency plans and test reports, the intercompany services agreement, vendor and SOC review files, change records, division policy sets, training records, and loan system audit exports.
- **Interview:** the group identity, SOC, and cloud platform directors; the CDBP system owner; the Head of Commercial Payments Operations; the Head of Technology and Cyber Risk; the client risk and assurance director; the Financial Software data services lead; the director of loan closing and funding; closers at 2 offices.
- **Test:**
  - a joiner-mover-leaver sample of 60 events across divisions, and 25 terminations;
  - a hardware-key administrator sign-in and federation checks on 52 applications;
  - a **session replay test**: a copied workforce session token was used from an unmanaged device (with SOC approval) to check device binding;
  - simulated token replay and inbox-rule creation to test detection;
  - a test sign-in with a support console role to see which tenants it could read;
  - cross-tenant access attempts in platform test tenants;
  - restores of 3 CDBP databases from the provider B vault;
  - a TLS scan of 80 endpoints including the payment path, and an external exposure scan;
  - a sample of 60 bank wires (callbacks and dual control) and 30 CRE fundings (instruction source and callback number).

## 4. Rules of engagement
- No testing that could affect payments, customers, or client institutions. Platform tests ran in test tenants; the session replay and detection tests used test accounts and were time-boxed with the SOC.
- No customer information left group systems. Screenshots were redacted.
- The assessor would stop and notify the Group CISO on any critical exposure. The session replay result was reported to the Group CISO the same day (2026-07-22) and treated as a priority finding; no other critical exposure was found.

## 5. Results summary
| Scope | Satisfied | Other than satisfied | Total |
|---|---|---|---|
| Common controls (SYS-G1, Group HR, SYS-G2, SYS-G3) | 119 | 17 | 136 |
| CDBP (SSP system) | 14 | 5 | 19 |
| Division sample: Banking | 45 | 2 | 47 |
| Division sample: Financial Software | 22 | 5 | 27 |
| Division sample: Commercial Real Estate | 30 | 10 | 40 |
| **Total** | **230** | **39** | **269** |

**Common controls are strong.** 119 of 136 common statements were satisfied. MFA and federation (IA-2, IA-2(1)), privileged access (AC-6(5)), account disabling (AC-2(3)), terminations (PS-4), training (AT-2), vulnerability management (RA-5), backups (CP-9), boundaries and encryption (SC-7, SC-8, SC-12, SC-28) had no findings. The common findings are about **sessions and service accounts** (AC-12, AC-2, IA-5), **detection across identity, email, and consoles** (SI-4), and **cross-division incident handling and notices** (IR-3, IR-4, IR-6, IR-8), which is scenario gap 5.

**The CDBP is sound at its core and weak at its edges.** Separation of duties (AC-5) held in all 60 sampled wires; tenant isolation (AC-3) held in every cross-tenant attempt. The failures are the support console's reach (AC-6), no review of support activity (AU-6), untested gateway and region failover (CP-4), and the bank's missing oversight of the affiliate that runs the platform (SA-9). IA-8 was satisfied as written (every end user is uniquely identified and authenticated); the 41 client tenants without business payment MFA are tracked from P03 as POAM-009.

**Division samples:**
- *Banking:* the risk assessment (RA-3), role-based training (AT-3), and oversight of outside vendors (SA-9) met every statement. The only finding is a contingency plan that does not cover a deliberate suspension of digital payment initiation (CP-2).
- *Financial Software:* the cash-flow data service changes outside configuration control (CM-3, CM-4) and without fairness testing or client-ready documentation (SA-11), which is scenario gap 4. Its oversight of its own providers (SA-9) met every statement.
- *Commercial Real Estate:* policies not disseminated or updated since the acquisition (PL-1), no prior assessment (CA-2), no payment-fraud role training for closers (AT-3), and no review of funding-instruction changes (AU-6). In the 30 funding files, 9 callbacks went to numbers taken from the closing package.

**Controls fully other than satisfied** (every statement failed): AC-12 (common), IR-3 (common), and AC-6 (CDBP). Each has only one determination statement.

21 of the 40 control assessments had at least one statement other than satisfied. All are in `poam.csv`.

## 6. POA&M
`poam.csv` has **24 items**: 8 from this assessment alone, 10 from this assessment and the P03 gap analyses together, 5 from the P03 gap analyses alone (POAM-009, POAM-016, and POAM-022 to POAM-024), and 1 from the P10 AI assessment (POAM-021). By risk: 5 High (POAM-003 sessions, POAM-008 support console, POAM-015 data service testing, POAM-019 CRE funding and training, POAM-021 credit model reasons), 15 Moderate, and 4 Low. Status: 18 In progress, 6 Open. Each item names the related P01 risks.

## 7. Deliverables and acceptance
`assessment-results.csv` (269 rows, with an `assessment_scope` column), `poam.csv` (24 items), and this plan and summary. Results were presented to the holding company and bank board risk committees on 2026-09-10 and accepted by the Group CISO and the Group Chief Risk Officer, with second-line concurrence from the Head of Technology and Cyber Risk. Division presidents accepted their division findings the same week.
