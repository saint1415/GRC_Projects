# Security Assessment Plan and Summary: Cris Santos Company Holdings | Public Administration | Multi-Sector

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. (GovTech Integration, IT Consulting, Government Software Products, and corporate shared services) |
| Scope | Group common controls (SYS-G1 identity, group personnel security and HR, SYS-G2 SOC, SYS-G3 cloud), the Agency Case Management Platform (ACMP, the P02 SSP system), and samples of controls each division operates itself |
| Tier / Vertical | Multi-Sector / Public Administration (focus division: GovTech Integration) |
| Procedures | NIST SP 800-53A Rev. 5, Release 5.2.0 (determination statements from `00_universal-framework/frameworks/sp800-53a_objectives.csv`) |
| Assessor and independence | Group internal audit, which reports to the board audit committee and neither designs nor operates the controls it assessed. Division security and compliance leads acted as liaisons only. The group public sector compliance director supplied contracts and agency correspondence but did not rate findings |
| Assessment window | 2026-07-06 to 2026-08-28 |
| Also supports | The annual assessment that agency contracts require under the SP 800-53 Moderate baseline (CA-2); evidence for state CSA CJIS audits and IRS Office of Safeguards reviews of the agencies (N92-R02, N92-R01); the HIPAA evaluation for the IEP business associate work (45 CFR 164.308(a)(8)); input to the IT Consulting CMMC readiness work (N54-R05) |

## 1. Approach: assess common controls once, then sample divisions
All three divisions run on the same corporate identity platform, SOC, cloud landing zones, and personnel processes. Testing those three times would cost three times as much and give three slightly different answers. So:
1. **Common controls** marked "Yes (common control, assessed once)" in the P02 `common-control-catalog.csv` (20 base controls) were assessed **once**, with samples drawn from every division. For example, the joiner-mover-leaver sample took 60 events from all three divisions and corporate, and the screening sample took 120 corporate shared-service staff with access to CJI or FTI environments.
2. **The ACMP's** system-specific and hybrid controls were assessed because it is the SSP system, it holds FTI for 7 revenue agencies and CJI for 212 criminal justice agencies, and it carries the top group risks (P01 GR-01, GR-02, GR-07).
3. **Division samples** covered controls each division operates itself, chosen from its High risks (P01) and its gap analysis rows (P03). Division findings are reported to that division, not averaged into the group result.

This follows POL-01 4.10 (annual assessment of common controls and division samples). Common controls not assessed this year are scheduled for the 2027 cycle in the catalog.

## 2. Controls selected
**45 control assessments** (42 distinct controls; SC-13, CM-3, and SA-9 were assessed in two scopes), **257 determination statements**.

| Scope | Controls | Statements | Why selected | Depth / coverage |
|---|---|---|---|---|
| Common control (SYS-G1 identity) | AC-2, AC-6(5), IA-2, IA-2(1), IA-5 | 40 | Every division's access control; GT-002 (service accounts), GT-016 (interface credentials) | Focused / Comprehensive (all divisions sampled) |
| Common control (group personnel security and HR) | PS-3, PS-4, PS-6, AT-2 | 22 | GR-02 (High); scenario gap 1; P03 CJ-01, CJ-03, PB-01 to PB-03 | Comprehensive / Focused (120 corporate staff, 60 GovTech staff, 25 terminations) |
| Common control (SYS-G2 SOC) | SI-4, AU-6, IR-4, IR-6, IR-8, IR-3 | 48 | GR-01, GR-03 (High); scenario gap 5; P03 CJ-09, PB-11 | Focused / Comprehensive |
| Common control (SYS-G3 cloud) | CP-9, SC-7, SC-12, SC-28, CM-6, AU-11 | 22 | GR-01, GR-09; immutable backups; FTI log retention (scenario gap 2) | Focused / Focused |
| ACMP (SSP system) | AC-3, AC-4, SC-8, SC-13, CP-4, CP-10, CM-3, RA-5, SA-9, PS-7 | 42 | GR-07 (High); GT-001, GT-003, GT-005, GT-014; scenario gaps 8 and 10 | Comprehensive / Comprehensive |
| Division sample: GovTech (IEP and MVSP) | RA-3, CM-4, SA-11, AC-21, PL-4 | 26 | GT-008 (High), GT-009, GT-020; P03 AI-01, AI-02, DP-02 | Focused / Focused (IEP AI launch records in 2 states; MVSP in 3 states) |
| Division sample: IT Consulting | AC-17, SI-3, CA-2, AC-20, MP-7 | 28 | IC-001 (Very High), IC-002, IC-004 (High); scenario gaps 3, 4, and 7 | Focused / Focused (acquired estate and the CUI enclave) |
| Division sample: Government Software Products | SC-13, CM-3, SA-9, CA-7 | 29 | SW-001, SW-003 (High), SW-010, SW-013; scenario gaps 6 and 9 | Focused / Focused (RMS connectors, RMS AI assist beta, Civic Suite, Grants Management) |
| **Total** | **45** | **257** | | |

Depth and coverage use the SP 800-53A attribute values (Basic, Focused, Comprehensive). Comprehensive depth was used where a failure would breach a CJIS Security Addendum or Pub. 1075 Exhibit 7 term, because those findings cannot be risk-accepted (POL-01 4.4).

## 3. Methods and objects
- **Examine:** identity governance and PAM configuration; the group screening registers and the GovTech and Software division registers; signed Security Addendum certification pages and FTI penalty notices; SIEM data sources and detection rules; the group incident response plan, division annexes, and the draft group notification matrix; landing-zone guardrails and the exception register; backup vault and key policies; log archive retention settings; the ACMP role matrix, egress allow-list, module certificate inventory, and restore reports; change records; scan reports; the vendor and subcontract registers; IEP AI launch records; the enclave SSP and SPRS record; RMS beta release records and model service terms; FedRAMP and GovRAMP submissions.
- **Interview:** group identity, SOC, and cloud platform directors; the Group HR director and the GovTech personnel security manager; the Group General Counsel and the group public sector compliance director; the ACMP platform director and GovTech chief technology officer; the GovTech Data and AI director; the IT Consulting security and compliance lead and federal contracts compliance officer; the Software division RMS and Civic Suite general managers.
- **Test:**
  - a joiner-mover-leaver sample of 60 events across divisions, and 25 terminations against SYS-G1 disable times;
  - a hardware-key administrator sign-in, an attempted standing-admin assignment, and federation checks on 40 applications;
  - a simulated bulk read from a test tenant in the ACMP CJI cluster by a service account (with SOC approval) to test detection;
  - cross-tenant access attempts in ACMP test tenants, a blocked outbound connection test, and a TLS scan of 60 endpoints;
  - a deletion-lock test on the backup vault and restores of 3 tenants from it;
  - an external exposure scan of both landing zones and encryption settings on a sample of 40 data stores;
  - on the acquired consulting firm's estate: VPN authentication settings, device control, antivirus currency, and a scan of file shares for CUI markings (2026-08).

## 4. Rules of engagement
- No testing that could affect agency operations. Tests ran in non-production or dedicated test tenants; the bulk-read test used synthetic records in a test tenant inside the CJI cluster.
- No CJI, FTI, CUI, PHI, or motor vehicle records left group systems. Evidence was referenced by record counts and identifiers; screenshots were redacted.
- Test accounts used for the CJI cluster were held by internal audit staff who already had fingerprint-based checks and Security Addendum certifications for the states involved.
- The assessor would stop and notify the Group CISO on any critical exposure. One stop was called: CUI found on acquired file shares and in personal cloud storage (AC-20b.) was reported to the Group CISO and the IT Consulting federal contracts compliance officer on the day it was found, so counsel could decide whether it is a reportable cyber incident under DFARS 252.204-7012 (POAM-020).

## 5. Results summary
| Scope | Satisfied | Other than satisfied | Total |
|---|---|---|---|
| Common control (SYS-G1 identity) | 37 | 3 | 40 |
| Common control (group personnel security and HR) | 19 | 3 | 22 |
| Common control (SYS-G2 SOC) | 37 | 11 | 48 |
| Common control (SYS-G3 cloud) | 20 | 2 | 22 |
| **Common controls subtotal** | **113** | **19** | **132** |
| ACMP (SSP system) | 31 | 11 | 42 |
| Division sample: GovTech (IEP and MVSP) | 20 | 6 | 26 |
| Division sample: IT Consulting | 19 | 9 | 28 |
| Division sample: Government Software Products | 22 | 7 | 29 |
| **Total** | **205** | **52** | **257** |

**Common controls are strong in design and weak in reach.** 113 of 132 common statements were satisfied. MFA and privileged access (IA-2, IA-2(1), AC-6(5)), terminations (PS-4), activity review (AU-6), backups (CP-9), boundary protection (SC-7), keys (SC-12), and encryption at rest (SC-28) had no findings. The findings are about who and what the common controls do not yet cover:
- **Corporate staff outside the screening process** (PS-3, PS-6, AT-2): 31 of the 120 sampled corporate staff with CJI or FTI environment access were unscreened for at least one state or program (scenario gap 1).
- **Service accounts and interface credentials** (AC-2, IA-5): 41 ACMP service accounts are managed by script outside identity governance, and 18 agency interface credentials are past the 1-year rotation standard.
- **Monitoring gaps** (SI-4): the acquired firm's VPN and the directory trust are invisible to the SIEM, and the simulated bulk read from the CJI cluster raised no alert.
- **Cross-division incident handling and notification** (IR-3, IR-4, IR-6, IR-8): no common escalation and closure rules, an incomplete notification matrix, and no exercise (scenario gap 5).
- **Retention** (AU-11): common control logs are kept 2 years where Pub. 1075 requires 7 for FTI systems (scenario gap 2).

**ACMP.** Tenant isolation (AC-3), egress control (AC-4), TLS (SC-8), and FIPS 140-3 modules on CJI paths (SC-13) were all satisfied. The findings are recovery at scale (CP-4, CP-10: about 430 tenants, more than 30 hours estimated against an 8-hour RTO; scenario gap 8), subcontractor screening and terms (PS-7; scenario gap 10), emergency changes (CM-3), container image remediation (RA-5), and FTI and CJI in support tickets (SA-9).

**Division samples:**
- *GovTech (IEP and MVSP):* the AI eligibility assistant went live without an assessment of effects on applicants, a privacy impact analysis, or accuracy and bias testing (RA-3, CM-4, SA-11; scenario gap 6). MVSP bulk requesters are not re-verified in 2 of 3 states (AC-21). Rules of behavior (PL-4) were satisfied.
- *IT Consulting:* the acquired firm's VPN accepts SMS codes and the directory trust was never authorized (AC-17), acquired endpoints run legacy antivirus with alerts outside the SOC (SI-3), DoD CUI sits on acquired file shares and personal cloud storage with USB storage unrestricted (AC-20, MP-7), and the enclave assessment ignores inherited controls and predates the acquisition (CA-2; scenario gaps 3, 4, and 7).
- *Government Software Products:* 41 RMS connectors still use FIPS 140-2 certified modules (SC-13; scenario gap 9); the RMS AI assist beta was released by feature flag without change control, impact analysis, or a CJIS review of the model service (CM-3, SA-9); and a Civic Suite logging change was not reported to GovRAMP (CA-7). Grants Management's FedRAMP continuous monitoring statements were all satisfied.

**Controls fully other than satisfied** (every statement failed): IR-3 (common, 1 statement), AU-11 (common, 1 statement), and CP-10 (ACMP, 2 statements).

31 of the 45 control assessments had at least one statement other than satisfied. Every finding links to a POA&M item.

## 6. POA&M
`poam.csv` has **27 items**: 23 from this assessment (POAM-001 to POAM-023) and 4 from the P03 gap analyses (POAM-024 to POAM-027).

| Risk level | Items |
|---|---|
| High | 10 (POAM-001, POAM-003, POAM-011, POAM-012, POAM-016, POAM-018, POAM-020, POAM-021, POAM-022, POAM-024) |
| Moderate | 16 |
| Low | 1 (POAM-010) |

Status: 20 In progress, 7 Open. Each item names its owner, milestones, and the related P01 risks. The `scope` column shows whether the fix belongs to corporate (common), the ACMP, or a division, so each division sees its own list. High items that touch a CJIS Security Addendum or Pub. 1075 Exhibit 7 term (POAM-001, POAM-012) start with suspending access, because those risks may not be accepted (POL-01 4.4).

## 7. Deliverables and acceptance
`assessment-results.csv` (257 rows, with an `assessment_scope` column), `poam.csv` (27 items), and this plan and summary. Results were presented to the board risk committee on 2026-09-15 and accepted by the Group CISO and the Group Chief Risk Officer the same day. Division presidents accepted their division findings the same week. Each agency receives the common control and ACMP results and the POA&M on request and with each CSA audit or IRS review (P02 SSP section 4.2). Next assessment: 2027 cycle, July to August 2027, including the common controls marked "No (2027 cycle)" in the catalog.
