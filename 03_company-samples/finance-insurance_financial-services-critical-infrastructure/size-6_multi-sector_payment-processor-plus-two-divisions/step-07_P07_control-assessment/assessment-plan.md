# Security Assessment Plan and Summary: Cris Santos Company Holdings | Financial Services | Multi-Sector

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. |
| Scope | Group common controls (SYS-G1, SYS-G2, SYS-G3, group HR), the Payment Processing Platform (P02 SSP), and samples of Payments Software Platform and Merchant Consulting controls |
| Tier / Vertical | Multi-Sector / Financial Services (focus division: Payment Processing) |
| Procedures | NIST SP 800-53A Rev. 5, Release 5.2.0 (determination statements from `00_universal-framework/frameworks/sp800-53a_objectives.csv`) |
| Assessor and independence | Group internal audit, which reports to the board audit committee and neither designs nor operates the controls. Division security and compliance leads acted as liaisons only. The QSA's ROC (2026-11-02 to 2026-12-11) is a separate, external assessment |
| Assessment window | 2026-07-01 to 2026-08-31 |
| Also satisfies | Testing and monitoring of safeguards under 16 CFR 314.4(d)(1); evidence for the quarterly PCI DSS reviews (12.4.2) and for the 2026 ROC |

## 1. Approach: assess common controls once, then sample divisions
Most safeguards in all three divisions come from the same corporate providers. Testing them three times would waste effort and produce three slightly different answers. So:
1. **Common controls** in the P02 common control catalog were assessed **once**, across all divisions, with samples drawn from every division (for example, the termination sample took events from corporate, the Payment Processing and Software divisions, and Merchant Consulting).
2. **The Payment Processing Platform's** system-specific controls were assessed because it is the SSP system and carries the top group risks (GR-01, GR-02).
3. **Division samples** covered controls each division operates itself, chosen from its High risks and its P03 gaps. Division findings are reported to that division, not averaged into the group.

Merchant Consulting was sampled most heavily, on identity and governance controls (IA-2(2), AC-2, PL-1, CA-2, AT-3), because its inheritance is undocumented (scenario gap 2), its supplement has drifted, and its users work inside the processor's CDE (gap 1). The Software division was sampled on storefront integrity, its AI feature, and gateway recovery (gaps 3, 6, and 8).

## 2. Controls selected
**39 control assessments** (36 distinct controls; AC-2, CM-8, and CP-4 were assessed in two scopes), **260 determination statements**.

| Scope | Controls | Statements | Why selected | Depth / coverage |
|---|---|---|---|---|
| Common control (SYS-G1 identity) | AC-2, AC-2(3), AC-6(5), IA-2(1), IA-5, AC-17 | 46 | Every division's access to every CDE; GR-02, GR-07 | Focused / Comprehensive (all divisions sampled) |
| Common control (Group HR with SYS-G1) | PS-4, AT-2 | 15 | Terminations and training for 45,000 users | Focused / Focused |
| Common control (SYS-G2 SOC) | SI-4, AU-6, IR-3, IR-4, IR-6, IR-8, RA-5 | 57 | GR-03; scenario gaps 4 and 7 | Focused / Comprehensive |
| Common control (SYS-G3) | CP-9, SC-7, SC-8, CM-6, CP-7 | 23 | GR-06; segmentation, backups, data center failover | Focused / Focused |
| Payment Processing Platform | AC-3, AC-4, AC-6, SC-12, SC-28, CA-8, CP-4, SI-12, CM-8 | 22 | GR-02, GR-09; PP-001, PP-010 (High); PCI DSS core | Comprehensive / Comprehensive |
| Division sample: Payments Software Platform | SI-7, CM-8, SA-9, CP-4, CM-3 | 33 | SW-001, SW-002, SW-004 (High); gaps 3, 6, 8 | Focused / Focused (30 storefronts sampled) |
| Division sample: Merchant Consulting | IA-2(2), AC-2, PL-1, CA-2, AT-3 | 64 | MC-001 (High); gaps 1 and 2 | Focused / Comprehensive (all SYS-M1 users reconciled) |
| **Total** | **39** | **260** | | |

## 3. Methods and objects
- **Examine:** identity governance, PAM, and SYS-M1 conditional access configuration; SIEM data sources and rules; landing-zone policies; backup and immutability settings; vault, HSM, and key procedures; the SYS-P6 role catalog; retention settings; storefront tamper-detection coverage; release records; group and consulting policies; the incident response plan and notification matrix.
- **Interview:** the group identity, SOC, and cloud platform directors; the Payment Processing division CISO, chief technology officer, and head of settlement operations; key custodians; the head of bank and network relationships; the Software division CISO, product lead, and marketplace director; the Merchant Consulting security and compliance lead and dispute services director.
- **Test:**
  - a joiner-mover-leaver sample of 60 events and a termination sample of 40 (15 from Merchant Consulting);
  - a full reconciliation of SYS-M1 users against HR (2026-07-14);
  - a hardware-key administrator sign-in to CDE PAM in both data centers;
  - an SMS code relay through a test page against a test SYS-M1 account (with Group CISO approval);
  - a simulated bulk export of 5,000 synthetic case files from a SYS-P6 test tenant, to test detection;
  - denied-path tests between division accounts and CDE segments; a TLS scan of 75 endpoints;
  - restores of a settlement database copy and a dispute platform backup from the immutable vault;
  - browser captures of 30 sampled storefronts to compare loaded scripts with the inventory.

## 4. Rules of engagement
- No testing that could affect authorization, settlement, funding, or the gateway. Tests ran in non-production tenants where possible; the SYS-P6 export test used synthetic case files.
- No real PAN left group systems. Screenshots were redacted.
- The assessor would stop and notify the Group CISO on any critical exposure. One was reported to the Group CISO the same day it was found: the SYS-M1 trusted-location MFA exemption, which was removed on 2026-09-20 (POAM-002).

## 5. Results summary
| Scope | Satisfied | Other than satisfied | Total |
|---|---|---|---|
| Common controls | 128 | 13 | 141 |
| Payment Processing Platform | 17 | 5 | 22 |
| Division sample: Payments Software Platform | 24 | 9 | 33 |
| Division sample: Merchant Consulting | 52 | 12 | 64 |
| **Total** | **221** | **39** | **260** |

**Common controls are strong.** 128 of 141 common statements were satisfied. Privileged access (AC-6(5)), administrator MFA (IA-2(1)), remote access (AC-17), training (AT-2), vulnerability management (RA-5), and every SYS-G3 control (CP-9, SC-7, SC-8, CM-6, CP-7) had no findings. The common findings are about **people from other divisions** (AC-2 certification of cross-division console users, PS-4 consulting terminations), **monitoring coverage of SYS-P6** (SI-4, AU-6), **cross-division incident response and notification** (IR-3, IR-4, IR-6, IR-8; scenario gaps 4 and 7), and service identity secret rotation (IA-5).

**The Payment Processing Platform's core passed.** Key management (SC-12), encryption at rest (SC-28), access enforcement in the vault (AC-3), penetration and segmentation testing (CA-8), and failover testing (CP-4) were fully satisfied. The five findings are all at the dispute edge: the flow of evidence through consulting mailboxes (AC-4), the bulk export permission (AC-6), retention of case files (SI-12), and the data inventory (CM-8).

**Division samples:**
- *Payments Software Platform:* tamper-detection and script inventory cover only the standard checkout template (SI-7, CM-8; 19 of 30 sampled storefronts used custom themes); no ongoing monitoring of marketplace apps or the model provider (SA-9); the gateway failover is untested since 2025-04 (CP-4); the merchant insights assistant skipped change control (CM-3).
- *Merchant Consulting:* SMS codes can be relayed and 14 users were exempt from MFA (IA-2(2)); 37 departed consultants were still active (AC-2); group policies were never distributed (PL-1); inheritance was never defined or assessed (CA-2); dispute analysts lack PCI DSS role training (AT-3).

**Controls fully other than satisfied** (every statement failed): IR-3 (common), AC-4 and AC-6 (Payment Processing Platform), and IA-2(2) (Merchant Consulting). Each has only one determination statement.

23 of the 39 control assessments had at least one statement other than satisfied. All are in `poam.csv`.

## 6. POA&M
`poam.csv` has **25 items**: 17 from this assessment, 5 from the P03 gap analyses (POAM-009, POAM-021 to POAM-023, POAM-025), and 3 from other sources (POAM-013 and POAM-014 from SSP partial controls, POAM-024 from the 2026-06 PAN discovery finding). By risk: 6 High (POAM-001 consulting account life cycle, POAM-002 consulting MFA, POAM-003 case export, POAM-007 PAN in consulting mailboxes and case files, POAM-015 storefront scripts, POAM-017 AI assistant change control), 14 Moderate, and 5 Low. Status: 15 In progress, 9 Open, and 1 Closed (POAM-024). Each item names the related P01 risks.

**Before the ROC.** POAM-003, POAM-005, and POAM-008 close by 2026-10-31, and the interim steps of POAM-001, POAM-002, and POAM-007 (weekly reconciliation, trusted-location removal, SYS-M1 in scope with PAN blocking) are in place before QSA fieldwork starts on 2026-11-02.

## 7. Deliverables and acceptance
`assessment-results.csv` (260 rows, with an `assessment_scope` column), `poam.csv` (25 items), and this plan and summary. Results were presented to the board risk committee and accepted by the Group CISO and the Group Chief Risk Officer on 2026-09-10. Division presidents accepted their division findings the same week.
