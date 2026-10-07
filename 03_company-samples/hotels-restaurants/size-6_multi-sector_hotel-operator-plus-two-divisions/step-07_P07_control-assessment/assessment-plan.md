# Security Assessment Plan and Summary: Cris Santos Company Holdings | Accommodation and Food Services | Multi-Sector

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. |
| Scope | Group common controls (SYS-G1 identity, Group HR, SYS-G2 SOC, SYS-G3 cloud and network, SYS-G4 payment services), the Hotel Property Management and Point-of-Sale Platform (PMPS, the P02 SSP system), and samples of Hotels, Attractions, and Vacation Ownership controls |
| Tier / Vertical | Multi-Sector / Accommodation and Food Services (focus division: Hotels) |
| Procedures | NIST SP 800-53A Rev. 5, Release 5.2.0 (determination statements from `00_universal-framework/frameworks/sp800-53a_objectives.csv`) |
| Assessor and independence | Group internal audit with its co-source firm. Internal audit reports to the board audit committee and neither designs nor operates the controls. Division security and compliance leads, the Group Director of Payments and PCI Compliance, and the Qualified Individual acted as liaisons only |
| Assessment window | 2026-07-06 to 2026-08-28 |
| Also supports | PCI DSS v4.0.1 Requirement 12.4.2 quarterly reviews for the Hotels service provider program; the Safeguards Rule testing and monitoring duty (16 CFR 314.4(d)(1)) for the finance subsidiary; QSA fieldwork for the 2026 Hotels ROC (from 2026-10-19), which will rely on this work only as background, not as a substitute |

## 1. Approach: assess common controls once, then sample divisions
All three divisions use the same identity platform, SOC, cloud and network platform, and payment tokenization service. Testing them three times would waste effort and give three slightly different answers. So:
1. **Common controls** in the P02 common control catalog were assessed **once**, with samples drawn from every division (for example, the joiner-mover-leaver sample took events from all three divisions, and the termination sample took seasonal park staff and hotel staff).
2. **The PMPS's** system-specific controls were assessed because it is the SSP system and carries the top Hotels risks (HTL-01, HTL-03) and the top group risk (GR-01).
3. **Division samples** covered controls each division operates itself, chosen from its High risks and its P03 gaps. Division findings are reported to that division, not averaged into the group.

Vacation Ownership was sampled most heavily (47 statements) because it is not yet on SYS-G1, its inheritance of common controls is undocumented (scenario gap 7), its standards have drifted (gap 7), and it has Safeguards Rule gaps (gap 3). Attractions was sampled on ride control (gap 9), the kids' club and biometric data (gaps 4 and 5), and payment pages.

## 2. Controls selected
**41 control assessments** (35 distinct controls; CM-6, SC-7, SC-28, and IR-8 were each assessed in two scopes and SA-9 in three), **270 determination statements**.

| Scope | Controls | Statements | Why selected | Depth / coverage |
|---|---|---|---|---|
| Common control (SYS-G1 identity) | AC-2, AC-2(3), AC-6(5), IA-2, IA-2(1), IA-5, AC-17 | 48 | Every division's access and remote access; GR-01, GR-10 | Focused / Comprehensive (all divisions sampled) |
| Common control (Group HR with SYS-G1; Group HR) | PS-4, AT-2 | 15 | Terminations for 45,000 staff, including seasonal park staff; training in all divisions | Focused / Focused |
| Common control (SYS-G2 SOC) | SI-4, AU-6, IR-3, IR-4, IR-6, IR-8, RA-5 | 57 | GR-03, GR-05, GR-12; scenario gap 8 | Focused / Comprehensive |
| Common control (SYS-G3, SYS-G4) | CP-9, SC-7, SC-8, SC-12, SC-28, CM-6 | 22 | GR-05, GR-17; immutable backups, guardrails, card vault | Focused / Focused |
| PMPS (SSP system) | AC-6, CM-8, SI-3, MA-4, SI-2, CA-3 | 41 | GR-01, GR-02, HTL-01, HTL-03, HTL-12; gaps 1, 2, and 6 | Comprehensive / Comprehensive (12 hotel walkthroughs, discovery at 17 managed hotels) |
| Division sample: Hotels | CM-6, SA-9 | 12 | HTL-04 (penetration test finding); legacy POS vendor | Focused / Focused |
| Division sample: Attractions | SC-7, SI-12, SA-9, CM-7, SI-7 | 28 | GR-09, ATT-02, ATT-03, ATT-04, ATT-05, ATT-06; gaps 4, 5, and 9 | Focused / Focused (7 parks; 3 microsites) |
| Division sample: Vacation Ownership | CP-4, IA-2(2), SC-28, SA-9, IR-8, PL-1 | 47 | GR-06, VO-01, VO-02, VO-05, VO-10, VO-16; gaps 3 and 7 | Focused / Focused |
| **Total** | **41** | **270** | | |

## 3. Methods and objects
- **Examine:** identity governance and PAM configuration, the vendor remote tool configuration, SIEM data sources and rules, landing-zone and guardrail policies, backup and immutability settings, guest profile hub database grants, POI and device inventories, interface specifications, lock server settings, ride control network designs, vendor files and contracts, the division standards and incident plans, and the training platform.
- **Interview:** group identity, SOC, cloud platform, and network directors; the Group Director of Payments and PCI Compliance; the Hotels division payments and systems director; division security and compliance leads (including the Qualified Individual); the Attractions vice president of ride engineering and digital products director; the Group General Counsel.
- **Test:**
  - a joiner-mover-leaver sample of 60 events across divisions, 60 seasonal park leavers, and 25 hotel terminations;
  - administrator sign-in with a hardware key and federation checks on 52 applications;
  - test queries with the CRS integration credential against the guest profile hub (with SOC approval; read-only; no data exported);
  - a simulated vendor remote session into a legacy POS server in a test outlet to check SOC detection;
  - network discovery on payment segments at 17 managed hotels and walkthroughs at 12 hotels;
  - restores of 3 datasets from the immutable vault;
  - a TLS scan of 80 endpoints and an external exposure scan;
  - a sign-in to loan origination from a sales gallery account to confirm the MFA gap.

## 4. Rules of engagement
- No testing that could affect ride and show control, door locks, or card authorizations. Ride control was assessed by document review and the 2026-05 penetration test results only.
- No card data, children's data, or customer information left group systems. Screenshots were redacted.
- The assessor would stop and notify the Group CISO on any critical exposure. The guest profile hub query result (the CRS integration credential can read owners' bank data) was reported to the Group CISO and the Group Chief Privacy Officer on the day it was found, 2026-07-22.

## 5. Results summary
| Scope | Satisfied | Other than satisfied | Total |
|---|---|---|---|
| Common controls | 120 | 22 | 142 |
| PMPS (SSP system) | 28 | 13 | 41 |
| Division sample: Hotels | 8 | 4 | 12 |
| Division sample: Attractions | 19 | 9 | 28 |
| Division sample: Vacation Ownership | 33 | 14 | 47 |
| **Total** | **208** | **62** | **270** |

**Common controls are strong where they are used.** 120 of 142 common statements were satisfied. Identity (AC-2(3), AC-6(5), IA-2, IA-2(1)), cloud and payment platform protection (CP-9, SC-7, SC-8, SC-12, SC-28, CM-6), and most SOC detection had no findings. The common findings sit at the **edges of the common services**: things that are not connected to them (legacy POS servers and the Vacation Ownership legacy data center, SI-4, AU-6, RA-5), the shared vendor's remote tool (AC-17), local and service accounts (AC-2, IA-5), seasonal staff terminations (PS-4), and cross-division incident handling and notification (IR-3, IR-4, IR-6, IR-8), which is scenario gap 8.

**The PMPS findings match the top group risks.** The CRS integration credential reads every guest profile hub table (AC-6, gap 2). The legacy POS vendor's always-on tool fails 4 of 8 maintenance statements (MA-4, gap 1). Legacy POS servers lack group anti-malware alerting and missed a patch window (SI-3, SI-2). Device inventories at 17 managed hotels are kept by hand (CM-8), and owner network connections lack terms (CA-3, gap 6).

**Division samples:**
- *Hotels:* default administrator passwords on door lock servers at 14 hotels (CM-6) and the legacy POS vendor's support service (SA-9).
- *Attractions:* the ride control bridge at 2 parks (SC-7, gap 9); biometric templates and child profiles with no deletion (SI-12, gaps 4 and 5); no written assurances from the kids' club analytics vendor (SA-9); unmanaged scripts on 3 ticket microsites (CM-7, SI-7).
- *Vacation Ownership:* no MFA (IA-2(2)) and no encryption at rest for the loan archive (SC-28), both fully other than satisfied; lapsed service provider oversight (SA-9); no FTC notification step (IR-8); 2023 standards (PL-1); no 2026 restore test (CP-4).

**Controls fully other than satisfied** (every statement failed): IR-3 (common), AC-6 (PMPS), and IA-2(2) and SC-28 (Vacation Ownership). Each has only one determination statement.

31 of the 41 control assessments had at least one statement other than satisfied. All are in `poam.csv`.

**Relation to PCI DSS validations.** The AC-2, AC-17, MA-4, IA-5, SI-3, and AU-6 findings correspond to the four compensating controls in the 2025 Hotels ROC (Requirements 5.2, 8.2, 8.3, and 10.4.1.1; P03). They do not mean the ROC was wrong: the compensating controls still operate. They mean the conditions that made compensating controls necessary have not been removed, and the controls must be revalidated before the 2026 QSA fieldwork.

## 6. POA&M
`poam.csv` has **32 items**: 24 from this assessment (POAM-001 to POAM-024), 1 combining this assessment with P03 gaps (POAM-026, the CA-3 findings with the management agreement gaps), and 7 from the P03 gap analyses (POAM-025 and POAM-027 to POAM-032). By risk: 8 High (POAM-001, POAM-011, POAM-013, POAM-015, POAM-016, POAM-020, POAM-021, POAM-025), 23 Moderate, and 1 Low (POAM-004). Status: 26 In progress, 6 Open. Each item names its scope and the related P01 risks.

## 7. Deliverables and acceptance
`assessment-results.csv` (270 rows, with an `assessment_scope` column), `poam.csv` (32 items), and this plan and summary. Results were presented to the board audit committee and the board risk committee and accepted by the Group CISO and the Group Chief Risk Officer on 2026-09-10. Division presidents accepted their division findings the same week, and the Qualified Individual included the Vacation Ownership findings in the annual report to the finance subsidiary board (16 CFR 314.4(i)).
