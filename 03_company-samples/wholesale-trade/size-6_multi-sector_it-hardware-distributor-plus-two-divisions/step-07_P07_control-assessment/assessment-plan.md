# Security Assessment Plan and Summary: Cris Santos Company Holdings | Wholesale Trade | Multi-Sector

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. |
| Scope | Group common controls (SYS-G1, SYS-G2, SYS-G3, Group HR, the group supply chain risk office), the Order-to-Fulfillment Platform (P02 SSP, including the Federal Fulfillment Enclave), and samples of IT Distribution, Logistics, and Online Retail controls |
| Tier / Vertical | Multi-Sector / Wholesale Trade (focus division: IT Distribution) |
| Procedures | NIST SP 800-53A Rev. 5, Release 5.2.0 (determination statements from `00_universal-framework/frameworks/sp800-53a_objectives.csv`) |
| Assessor and independence | Group internal audit, which reports to the board audit and risk committee and neither designs nor operates the controls. Division security and compliance leads acted as liaisons only |
| Assessment window | 2026-07-06 to 2026-08-28 (DC walkthroughs at DC-1, DC-3, DC-6, DC-8; night walkthrough at DC-6 on 2026-08-12) |
| Also supports | SP 800-171 Rev. 2 requirement 3.12.1 (periodic assessment) for the CUI environment; readiness for the C3PAO assessment in 2027-01; evidence for the 2026 PCI DSS ROC and the P09 SOC 2 readiness work |

## 1. Approach: assess common controls once, then sample divisions
Most safeguards in all three divisions come from the same corporate providers. Testing them three times would waste effort and give three slightly different answers. So:
1. **Common controls** in the P02 common control catalog were assessed **once**, across all divisions, with samples drawn from every division (for example, the joiner-mover-leaver sample took events from all three, and handheld sign-in tests covered DCs that serve every division).
2. **The OFP's** system-specific and hybrid controls were assessed because it is the SSP system, holds the CUI environment, and carries the top group risk for CUI (GR-03).
3. **Division samples** covered controls each division operates itself, chosen from its High risks and its P03 gaps. Division findings are reported to that division, not averaged into the group.

Logistics was sampled on maintenance, remote access, physical protection, and contingency testing because its inheritance is undocumented (scenario gap 8) and its supplement has drifted (gap 9).

**This is not a CMMC assessment.** It is an SP 800-53A assessment of the SP 800-53 controls in the SSP. A C3PAO will assess the 110 SP 800-171 requirements against SP 800-171A objectives in 2027-01.

## 2. Controls selected
**42 control assessments** (40 distinct controls; AC-3 and SA-9 were assessed in two scopes), **247 determination statements**.

| Scope | Controls | Statements | Why selected | Depth / coverage |
|---|---|---|---|---|
| Common control (SYS-G1 identity) | AC-2, AC-2(3), AC-6(5), IA-2, IA-2(1), IA-5 | 44 | Every division's access control; shared handhelds (GR-16) | Focused / Comprehensive (all divisions sampled) |
| Common control (Group HR) | PS-4, AT-2 | 15 | Terminations and training for 45,000 users | Focused / Focused |
| Common control (SYS-G2 SOC) | SI-4, IR-3, IR-4, IR-6, IR-8, RA-5 | 54 | GR-05; DIBNet reporting; scenario gap 10 | Focused / Comprehensive |
| Common control (SYS-G3 cloud) | CP-9, SC-7, SC-8, SC-13, SC-28, CM-6 | 22 | GR-02, GR-03; FIPS cryptography for CUI | Focused / Focused |
| Common control (group supply chain risk office) | SR-2, SR-5, SR-6 | 16 | GR-01, GR-20; scenario gap 2 | Focused / Focused |
| Order-to-Fulfillment Platform | AC-3, AC-4, AC-20, CM-8, SA-9, CA-2 | 28 | GR-03, GR-04, GR-13; scenario gap 1 | Comprehensive / Comprehensive |
| Division sample: IT Distribution | SR-10, SR-11, SR-4, MP-6, AT-3 | 22 | ID-003, ID-011, ID-019; P08 scenario | Focused / Focused (10 integration jobs; 5 ITAD lines) |
| Division sample: Logistics | MA-4, AC-17, PE-3, CP-4 | 29 | LW-001, LW-004, ID-018; gaps 6 and 9 | Focused / Focused (4 DCs) |
| Division sample: Online Retail | SI-12, SA-9, SI-7, AC-3 | 17 | OR-001, OR-002, OR-005; PCI DSS gaps | Focused / Focused (3 brands; 300 recordings) |
| **Total** | **42** | **247** | | |

## 3. Methods and objects
- **Examine:** identity governance and PAM configuration, WMS user lists, SIEM data sources and rules, landing-zone and lab firewall rules, backup and vault settings, the C-SCRM plan and supplier register, the ERP item master, the CUI discovery scan, vendor contracts and attestations, contingency test records, call recording settings, payment page script inventories, marketplace roles.
- **Interview:** group identity, SOC, and cloud platform directors; the Group CMMC program director; the Group supply chain risk director; integration center managers; DC general managers at 4 DCs; the Logistics OT engineering manager; the Online Retail PCI compliance manager and marketplace director; 12 receiving staff and 6 buyers.
- **Test:**
  - a joiner-mover-leaver sample of 60 events across divisions, 25 terminations, and 15 agency leavers;
  - handheld sign-in on 6 devices at DC-2, DC-8, and DC-9;
  - a hardware-key administrator sign-in and 25 PAM sessions;
  - a simulated beacon from an IC-2 lab test device and traceroutes from the IC-2 lab;
  - a sales-role attempt to open DoD order attachments in the ERP;
  - a CUI-marked test file shared from the commercial collaboration tenant;
  - restores of WMS and portal datasets from the immutable vault;
  - re-testing of 20 sanitized drives from Lifecycle Services lines;
  - a test script injected into staging copies of each storefront brand's payment page;
  - a review of 300 contact center recordings of phone orders;
  - a TLS scan of 80 endpoints.

## 4. Rules of engagement
- No testing that could disrupt shipping, DC automation, or the storefront. Network tests at DCs ran after carrier cut-off with the DC general manager present; nothing was sent to PLCs.
- CUI was viewed only inside the FFE by assessors who are U.S. persons on the CUI roster for the engagement. No CUI, FCI, or cardholder data left group systems; screenshots were redacted.
- Recordings containing card data were reviewed inside the contact center platform only, and each one found was referred to the PCI compliance manager the same day.
- The assessor stopped and notified the Group CISO on any critical exposure. Two were reported the same day: the IC-2 route (SC-7) and card data in recordings (SI-12).

## 5. Results summary
| Scope | Satisfied | Other than satisfied | Total |
|---|---|---|---|
| Common controls | 131 | 20 | 151 |
| Order-to-Fulfillment Platform | 20 | 8 | 28 |
| Division sample: IT Distribution | 17 | 5 | 22 |
| Division sample: Logistics | 22 | 7 | 29 |
| Division sample: Online Retail | 11 | 6 | 17 |
| **Total** | **201** | **46** | **247** |

**Common controls are strong.** 131 of 151 common statements were satisfied. Privileged access (AC-6(5)), MFA (IA-2(1)), terminations (PS-4), awareness training (AT-2), encryption (SC-8, SC-13, SC-28), and configuration guardrails (CM-6) had no findings. The common findings are about **shared handheld logins and agency accounts** at DCs (AC-2, AC-2(3), IA-2, IA-5), **cross-division incident consistency and DIBNet capacity** (IR-3, IR-4, IR-6, IR-8; scenario gap 10), **OT monitoring and backups** (SI-4, CP-9), the **IC-2 lab route** (SC-7), lab scan coverage (RA-5), and **broker oversight** (SR-2, SR-5, SR-6).

**The OFP is where the CUI risk is.** AC-3 and AC-4 failed outright: a sales role opened CUI in the commercial ERP, and a CUI-marked file left the commercial tenant without a block. AC-20, CM-8, SA-9, and CA-2 each had findings tied to CUI outside the enclave and the 2025 assessment scope (scenario gap 1).

**Division samples:**
- *IT Distribution:* firmware hashes taken from a supplier portal on 2 of 10 jobs (SR-10), counterfeit detection dependent on incomplete receiving checks (SR-11, SR-4), undocumented sanitization verification with one readable drive (MP-6), and missing anti-counterfeit training at 5 DCs (AT-3).
- *Logistics:* persistent, unmonitored vendor tunnels into DC automation (MA-4, AC-17), missing night escort records at IC-2 (PE-3), and contingency tests that skip ransomware on the WMS replica and PLC restores (CP-4).
- *Online Retail:* card data in call recordings (SI-12), undetected script changes on 2 of 3 payment pages (SI-7), unassigned vendor responsibilities (SA-9), and broad access to seller financial data (AC-3).

**Controls fully other than satisfied** (every statement failed): IR-3 (common), SR-6 (common), AC-3 and AC-4 (OFP), SR-10 (IT Distribution), and AC-3 (Online Retail). Each has only one determination statement.

34 of the 42 control assessments had at least one statement other than satisfied. All are in `poam.csv`.

## 6. POA&M
`poam.csv` has **27 items**: 21 from this assessment, 5 from the P03 gap analyses (POAM-022 to POAM-024, POAM-026, POAM-027), and 1 from the P10 AI assessment (POAM-025). By risk: 10 High (POAM-002, POAM-006, POAM-007, POAM-009, POAM-010, POAM-012, POAM-014, POAM-017, POAM-018, POAM-026) and 17 Moderate. Status: 21 In progress, 6 Open. Each item names the related P01 risks, and items affecting SP 800-171 requirements note whether the requirement could sit on a CMMC POA&M (P03 `poam_allowed_cmmc`).

## 7. Deliverables and acceptance
`assessment-results.csv` (247 rows, with an `assessment_scope` column), `poam.csv` (27 items), and this plan and summary. Results were presented to the board audit and risk committee and accepted by the Group CISO and the Group Chief Risk Officer on 2026-09-15. Division presidents accepted their division findings the same week.
