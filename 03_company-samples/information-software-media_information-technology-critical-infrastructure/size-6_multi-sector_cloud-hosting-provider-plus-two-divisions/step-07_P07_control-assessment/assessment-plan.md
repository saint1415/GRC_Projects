# Security Assessment Plan and Summary: Cris Santos Company Holdings | Information Technology | Multi-Sector

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. |
| Scope | Group common controls (SYS-G1, SYS-G2, SYS-G3, group HR), the HCP (P02 SSP), and samples of Managed IT and Payment Processing controls |
| Tier / Vertical | Multi-Sector / Information Technology (focus division: Cloud Hosting) |
| Procedures | NIST SP 800-53A Rev. 5, Release 5.2.0 (determination statements from `00_universal-framework/frameworks/sp800-53a_objectives.csv`) |
| Assessor and independence | Group internal audit, which reports to the board audit committee and neither designs nor operates the controls. Division security leads acted as liaisons only |
| Assessment window | 2026-07-06 to 2026-08-28 |
| Also supports | The HIPAA evaluation (45 CFR 164.308(a)(8)) for both business associate divisions; testing of key controls under 16 CFR 314.4(d)(1) for Payment Processing; evidence for the G1 FedRAMP assessment starting 2027-02-08 and for the Managed IT CMMC readiness work. It is **not** a FedRAMP independent assessment, a PCI DSS assessment, or a CMMC assessment, each of which needs its own recognized assessor |

## 1. Approach: assess common controls once, then sample divisions
Most safeguards in all three divisions come from the same corporate providers. Testing them three times would waste effort and produce three slightly different answers. So:
1. **Common controls** in the P02 common control catalog were assessed **once**, across all divisions, with samples drawn from every division (for example, the joiner-mover-leaver sample took events from all three, and the seeded alert test planted alerts in HCP, CDE, and Managed IT log sources).
2. **The HCP's** system-specific controls were assessed because it is the SSP system and carries the top group risk (GR-01). The sample was weighted toward the partner-operator path and the FedRAMP 2026 transition.
3. **Division samples** covered controls each division operates itself, chosen from its High risks and its P03 gaps. Division findings are reported to that division, not averaged into the group.

Managed IT was sampled more heavily on governance (PL-1, CA-2) because its inheritance is undocumented (scenario gap 9) and its standards have drifted (gap 8). Payment Processing was sampled on the affiliate paths into its scope (gap 6), not on its own CDE controls, which its QSA tested in April 2026.

## 2. Controls selected
**40 control assessments** (33 distinct controls; AC-2, AC-6, AU-6, AU-11, CM-8, IR-6, and SA-9 were assessed in two scopes), **257 determination statements**.

| Scope | Controls | Statements | Why selected | Depth / coverage |
|---|---|---|---|---|
| Common control (SYS-G1 identity) | AC-2, AC-6(5), IA-2(1) | 28 | Every division's access; GR-01 | Focused / Comprehensive (all divisions sampled) |
| Common control (Group HR with SYS-G1; Group HR) | PS-4, AT-2 | 15 | Terminations and training for 45,000 users | Focused / Focused |
| Common control (SYS-G2 SOC) | SI-4, IR-4, IR-6, IR-3, IR-8, AU-6 | 48 | GR-03, GR-04; scenario gaps 4 and 7 | Focused / Comprehensive |
| Common control (SYS-G3) | CP-9, AU-9, AU-11, SC-12 | 11 | GR-07; immutable backups and log protection | Focused / Focused |
| HCP (SSP system) | AC-3, AC-6, AC-12, AU-2, CM-3, CM-8, CA-5, CA-7, RA-5, SC-13, SA-9, SI-7, CP-4 | 66 | GR-01, GR-05 (High); gaps 1 and 3 | Comprehensive / Comprehensive |
| Division sample: Managed IT | AC-2, AC-17, CM-5, AU-11, PL-1, CA-2, IR-6 | 67 | GR-02, GR-06; MS-001, MS-002 (High); gaps 2, 5, 8, 9 | Focused / Focused |
| Division sample: Payment Processing | SA-9, CM-8, SC-7, AU-6, AC-6 | 22 | PY-001 (High); GR-08; gap 6 | Focused / Focused (10 of 140 connected-to servers) |
| **Total** | **40** | **257** | | |

## 3. Methods and objects
- **Examine:** identity governance, PAM, and partner-operator federation configuration; SIEM sources, detection catalog, SOAR actions, and AI triage statistics; vault and log archive settings; the HCP change system, inventory, and G1 FedRAMP boundary list; cryptographic module inventory; RMM settings and agent inventory; supplements and policies; contract registers and the PCI DSS scope description.
- **Interview:** the Group identity, SOC, and cloud platform directors; the control plane engineering director; the Government Cloud compliance director; division security leads; the Managed IT federal contracts compliance officer; the Payment Processing Qualified Individual and chief compliance officer.
- **Test:**
  - a joiner-mover-leaver sample of 75 events across divisions, and 25 terminations;
  - hardware-key sign-in tests for three administrator roles;
  - 120 cross-tenant access attempts in commercial and G1 test tenants;
  - a partner-operator run-command against an unassigned test tenant, and replay of a copied partner-operator token from an unmanaged device;
  - a burst of 200 run-command executions across 40 test tenants, to test detection;
  - a seeded alert test: 40 true-positive alerts planted in HCP, CDE, and Managed IT sources, to measure AI triage auto-close;
  - deployment of a deliberately altered test artifact through the signing pipeline;
  - restores from the vault at external provider X;
  - an RMM test job across 12 sandbox clients, to test the approval rule;
  - an outbound connection test and local administrator review on 10 Payment Processing connected-to servers.

## 4. Rules of engagement
- No testing that could affect customers, agencies, clients, or card transactions. HCP tests ran in test tenants; RMM tests ran in a sandbox; the connected-to server review was read-only.
- No customer data, federal customer data, CUI, or account data left its environment. Screenshots were redacted.
- G1 tests were run by U.S.-person auditors and coordinated with the Government Cloud compliance director, so that no test would become a FedRAMP Reportable Incident.
- The assessor would stop and notify the Group CISO on any critical exposure. The partner-operator token replay (AC-12) was reported the same day; the 1-hour session limit was the interim response.

## 5. Results summary
| Scope | Satisfied | Other than satisfied | Total |
|---|---|---|---|
| Common controls | 88 | 14 | 102 |
| HCP (SSP system) | 56 | 10 | 66 |
| Division sample: Managed IT | 54 | 13 | 67 |
| Division sample: Payment Processing | 14 | 8 | 22 |
| **Total** | **212** | **45** | **257** |

**Common controls are strong where they are fully in group hands.** 88 of 102 common statements were satisfied. PAM (AC-6(5)), administrator MFA (IA-2(1)), training (AT-2), backups (CP-9), log protection and retention (AU-9, AU-11), and key management (SC-12) had no findings. The common findings are about **the Managed IT legacy tenant** (AC-2, PS-4), **the AI triage service** (SI-4, IR-4, AU-6, IR-8), and **cross-division incident consistency and notification** (IR-3, IR-6, IR-8), which is scenario gap 7.

**The HCP is sound except for one path and one transition.** Tenant isolation (AC-3: 120 of 120 cross-tenant attempts denied), signing (SI-7), logging (AU-2), and the POA&M process (CA-5) were satisfied. AC-6 and AC-12 failed because of the partner-operator path: a partner-operator account ran a command in a tenant outside its client team, and a copied token worked from an unmanaged device (scenario gap 1). Five findings are about the FedRAMP 2026 transition: change types (CM-3), offering inventory (CM-8), reporting (CA-7), remediation by PAIN rating (RA-5), and module documentation (SC-13). Two are about the third-party model service (SA-9), and one about contingency testing (CP-4).

**Division samples:**
- *Managed IT:* RMM accounts and approvals (AC-2, CM-5), RMM reach into other divisions (AC-17), log retention (AU-11), supplement drift (PL-1, gap 8), undocumented inheritance and a CUI enclave not assessed since 2024 (CA-2, gaps 5 and 9), and DIBNet reporting resilience (IR-6).
- *Payment Processing:* all five controls had findings, and all trace to the affiliates: no intercompany oversight (SA-9, four statements), the RMM path missing from scope (CM-8), an unlisted outbound connection (SC-7), RMM actions outside log review (AU-6), and RMM administrator rights (AC-6).

**Controls fully other than satisfied** (every statement failed): IR-3 (common), AC-6 and AC-12 (HCP), AU-11 (Managed IT), and AC-6 (Payment Processing). Each has only one determination statement.

29 of the 40 control assessments had at least one statement other than satisfied. All are in `poam.csv`.

## 6. POA&M
`poam.csv` has **23 items**: 19 from this assessment and 4 from the P03 gap analyses (POAM-005, POAM-011, POAM-020, POAM-022). By risk: 8 High (POAM-001 partner-operator path, POAM-003 AI triage, POAM-006 FedRAMP VDR and VER, POAM-008 G1 offering scope, POAM-013 RMM approvals, POAM-014 RMM reach into other divisions, POAM-018 Payment Processing affiliate oversight, POAM-021 CMMC Level 2) and 15 Moderate. Status: 21 In progress, 2 Open. Each item names the related P01 risks.

## 7. Deliverables and acceptance
`assessment-results.csv` (257 rows, with an `assessment_scope` column), `poam.csv` (23 items), and this plan and summary. Results were presented to the board risk committee and accepted by the Group CISO and the Group Chief Risk Officer on 2026-09-17. Division presidents accepted their division findings the same week.
