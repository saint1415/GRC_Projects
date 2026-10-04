# Security Assessment Plan and Summary: Cris Santos Company Holdings | Retail Trade | Multi-Sector

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. |
| Scope | Group common controls (SYS-G1 to SYS-G4 and group HR), the E-commerce and Point-of-Sale Platform (EPP, SYS-D1, the P02 SSP system), and samples of Grocery Retail, Grocery Wholesale, and Financial Services controls |
| Tier / Vertical | Multi-Sector / Retail Trade (focus division: Grocery Retail) |
| Procedures | NIST SP 800-53A Rev. 5, Release 5.2.0 (determination statements from `00_universal-framework/frameworks/sp800-53a_objectives.csv`) |
| Assessor and independence | Group internal audit, which reports to the board audit committee and neither designs nor operates the controls. Division security and compliance leads acted as liaisons only |
| Assessment window | 2026-07-01 to 2026-08-31 |
| Also supports | The Financial Services test of key safeguards (16 CFR 314.4(d)(1)); evidence for the 2026 PCI DSS ROC (QSA fieldwork 2026-10-19 to 2026-11-20). It does not replace the QSA's testing |

## 1. Approach: assess common controls once, then sample divisions
All three divisions sign in through the same identity platform, are watched by the same SOC, run in the same cloud landing zones, and publish their websites through the same digital front door. Testing those controls three times would waste effort and produce three slightly different answers. So:
1. **Common controls** marked "assessed once" in the P02 common control catalog (23 controls) were assessed **once** for the whole group, with samples drawn from every division (for example, the joiner-mover-leaver sample took events from stores, distribution centers, cardholder service, and corporate).
2. **The EPP's** system-specific controls were assessed because it is the SSP system, the retail cardholder data environment, and the system behind the top group risk (GR-01).
3. **Division samples** covered controls each division operates itself, chosen from its High risks and its P03 gaps. Division findings are reported to that division, not averaged into the group.

Financial Services and Grocery Wholesale were both sampled on CA-2, because neither has documented which safeguards it inherits from group providers (scenario gap 9). Financial Services was also sampled on PL-1, because its standards drifted from group policy (scenario gap 11).

## 2. Controls selected
**42 control assessments** (34 distinct controls; SC-7 was assessed in three scopes, and AC-17, AU-6, CA-2, CM-8, CP-9, and SA-9 in two), **275 determination statements**.

| Scope | Controls | Statements | Why selected | Depth / coverage |
|---|---|---|---|---|
| Common control (SYS-G1 identity) | AC-2, AC-2(3), AC-6(5), IA-2, IA-2(1), IA-5 | 44 | Every division's access; GR-07; payment switch accounts (RT-011) | Focused / Comprehensive (all divisions sampled) |
| Common control (Group HR with SYS-G1) | PS-4, AT-2 | 15 | Terminations and training for 45,000 users | Focused / Focused |
| Common control (SYS-G2 SOC) | SI-4, IR-3, IR-4, IR-6, IR-8, RA-5 | 54 | GR-03, GR-12; scenario gap 10 | Focused / Comprehensive |
| Common control (SYS-G3 cloud) | CP-9, SC-7, SC-8, SC-12, SC-28, CM-6 | 22 | GR-02, GR-15; immutable backups and guardrails | Focused / Focused |
| Common control (SYS-G4 digital front door) | CM-3, SA-9, SC-18 | 23 | GR-01 (High); scenario gap 1 | Comprehensive / Comprehensive (all four payment pages) |
| EPP (SYS-D1) | SI-7, AC-4, CM-12, SC-7, SI-2, AU-6, AC-17 | 37 | RT-001, RT-002, RT-003 (High); scenario gaps 2, 3, 4 | Comprehensive / Focused (10 stores, 5 of them acquired) |
| Division sample: Grocery Retail | AC-21, PT-2, CM-8 | 10 | RT-016, GR-09; scenario gap 5; PIN pad inventory (PCI DSS 9.5) | Focused / Focused (12 stores for CM-8) |
| Division sample: Grocery Wholesale | AC-17, SC-7, CP-9, CM-8, CA-2 | 33 | WD-001 (High), WD-002, WD-003, WD-011, WD-013; scenario gaps 6, 7, 9 | Focused / Focused (6 distribution centers) |
| Division sample: Financial Services | PL-1, CA-2, SA-9, AU-6 | 37 | FS-003 (High), FS-007, FS-010; scenario gaps 9, 11 | Focused / Focused |
| **Total** | **42** | **275** | | |

Controls that are common but not on this year's list (83 of the 106 in the catalog) are scheduled for the 2027 cycle, as the catalog's `assessed_in_P07` column shows.

## 3. Methods and objects
- **Examine:** identity governance and PAM configuration, the payment switch account register, SIEM data sources and use cases, alert routing, tag management publishing history, script inventories, the TPSP list and responsibility matrix, data flow diagrams, the PCI scope document and data discovery results, store and distribution center network diagrams and firewall rules, backup schedules, the intercompany data agreement and CDP audience rules, the Financial Services standards and Safeguards program, and the card processor's SOC 1 and SOC 2 reports.
- **Interview:** group identity, SOC, cloud platform, and digital directors; the Grocery Retail CISO, chief digital officer, and payments director; the Group General Counsel and Group Chief Privacy Officer; the Grocery Wholesale engineering and IT directors; the Financial Services CISO (Qualified Individual).
- **Test:**
  - a joiner-mover-leaver sample of 60 events across divisions, and 25 terminations;
  - a hardware-key administrator sign-in and federation checks on 40 applications;
  - browser captures of all four payment pages (retail web checkout, app web checkout view, wholesale portal invoice payment, cardholder portal bill payment) on 2026-07-28 and 2026-07-29;
  - a harmless test change to the retail web checkout on 2026-08-05 (approved by the Grocery Retail CISO) to see whether payment page monitoring alerts and who acts on them;
  - segmentation checks at 10 stores (5 acquired) and passive OT network capture at 1 distribution center;
  - restores of 3 datasets from the immutable vault;
  - a TLS scan of 80 endpoints and an external exposure scan of both providers' landing zones;
  - comparison of the Financial Services opt-out file with CDP audiences on 2026-07-20.

## 4. Rules of engagement
- No testing that could interrupt checkout, card authorization, SNAP EBT acceptance, distribution center operations, or cardholder service. Store tests ran outside trading peaks; OT capture was passive only.
- No card numbers, Rewards Card numbers, or cardholder data left group systems. Screenshots were masked to the first six and last four digits or less.
- The payment page test change was harmless and reverted within 1 hour, and the SOC was told in advance.
- The assessor would stop and notify the Group CISO on any critical exposure. The 2026-08-05 test showed alerts were not acted on for 6 days; the Group CISO was told the same day and the finding went straight to POAM-002.

## 5. Results summary
| Scope | Satisfied | Other than satisfied | Total |
|---|---|---|---|
| Common controls | 135 | 23 | 158 |
| EPP (SYS-D1) | 25 | 12 | 37 |
| Division sample: Grocery Retail | 7 | 3 | 10 |
| Division sample: Grocery Wholesale | 23 | 10 | 33 |
| Division sample: Financial Services | 30 | 7 | 37 |
| **Total** | **220** | **55** | **275** |

**Common controls are mostly strong.** 135 of 158 common statements were satisfied. Identity (AC-2(3), AC-6(5), IA-2, IA-2(1)), training (AT-2), terminations (PS-4), and cloud protection (CP-9, SC-7, SC-8, SC-12, SC-28, CM-6) had no findings. The common findings cluster in three places:
- **The digital front door** (CM-3, SC-18, SA-9): 7 of 23 statements failed. Marketing teams in all three divisions can publish scripts to payment pages without review, and the tag and script vendors are outside service provider oversight (scenario gap 1).
- **Incident response across divisions** (IR-3, IR-4, IR-6, IR-8): Financial Services still uses its own severity scale, and the plan and matrix do not cover the Rewards Card, the FTC notice, or wholesale customer notices (scenario gap 10).
- **Monitoring coverage and application accounts** (SI-4, RA-5, AC-2, IA-5): payment page alerts do not reach the SOC, the acquired stores and distribution center OT networks are not monitored or scanned, and payment switch application accounts are managed by hand.

**The EPP is where the card data risk is.** 12 of 37 statements failed. AC-4 failed outright: the Rewards Card number and code travel through a company-hosted field on the checkout page (scenario gap 2). The test change on 2026-08-05 was detected, but the alert sat in a mailbox for 6 days (SI-7). The 46 acquired stores account for 7 of the 12 findings (SC-7, SI-2, AU-6, AC-17; scenario gap 3), and the stray card numbers on the finance share for 2 more (CM-12; scenario gap 4).

**Division samples:**
- *Grocery Retail:* opted-out cardholders are not suppressed from card-derived CDP audiences, and no record shows when the affiliate marketing exception is used (AC-21, PT-2; scenario gap 5). The PIN pad inventory (CM-8) passed in all 12 sampled stores.
- *Grocery Wholesale:* always-on OT vendor access (AC-17), weak WMS-to-OT segmentation (SC-7), weekly instead of nightly WMS server backups (CP-9), missing OT inventories (CM-8; scenario gap 6), and no inheritance documentation for the portal (CA-2; gap 9).
- *Financial Services:* standards that conflict with group policy (PL-1; gap 11), inheritance never documented or tested (CA-2; gap 9), and processor oversight limited to receiving SOC reports (SA-9). Cardholder service activity monitoring (AU-6) passed.

**Controls fully other than satisfied** (every statement failed): IR-3 (common), AC-4 (EPP), and AC-21 (Grocery Retail). IR-3 and AC-4 each have one determination statement; AC-21 has two.

28 of the 42 control assessments had at least one statement other than satisfied. All are in `poam.csv`.

## 6. POA&M
`poam.csv` has **23 items**: 19 from this assessment, 1 from the P05 BIA (POAM-013, the digital front door recovery test), and 3 from the P03 gap analyses (POAM-021 to POAM-023). By risk: **9 High** (POAM-001 tag management, POAM-002 payment page monitoring, POAM-004 Rewards Card field, POAM-006 and POAM-007 acquired stores, POAM-011 cross-division notification, POAM-014 and POAM-015 distribution center OT, POAM-021 adverse action reasons) and **14 Moderate**. Status: 19 In progress, 4 Open. Each item names the related P01 risks and the P03 rows it also closes.

**Before the 2026 ROC fieldwork (2026-10-19 to 2026-11-20):** POAM-001, POAM-002, POAM-005, POAM-006, and POAM-007 are on the critical path. A PCI DSS requirement that is not in place when the QSA tests it is reported as not in place; it cannot be fixed by this POA&M after the fact.

## 7. Deliverables and acceptance
`assessment-results.csv` (275 rows, with an `assessment_scope` column), `poam.csv` (23 items), and this plan and summary. Results were presented to the board risk committee and accepted by the Group CISO and the Group Chief Risk Officer on 2026-09-10. Division presidents accepted their division findings the same week.
