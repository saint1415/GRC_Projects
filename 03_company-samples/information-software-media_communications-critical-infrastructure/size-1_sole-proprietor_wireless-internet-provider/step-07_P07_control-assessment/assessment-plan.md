# Security Assessment Plan and Results Memo: Cris Santos Company | Communications | Sole Proprietorship

| Field | Value |
|---|---|
| Organization | Cris Santos Company (owner-operated wireless internet service provider) |
| System assessed | ISP Operations Systems Profile (IOSP), per the system profile (P02) |
| Tier / Vertical | Sole Proprietorship / Communications |
| Procedures | NIST SP 800-53A Rev. 5, Release 5.2.0 (determination statements from NIST OSCAL content) |
| Assessor(s) and independence | The owner-operator (self-assessment), assisted by the on-call network consultant after the consultant signed confidentiality and security terms on 2026-07-17. **Independence is limited**: the owner designed, operates, and assessed these controls. The consultant ran the port checks and device credential tests but also helps run the router |
| Assessment window | 2026-07-20 to 2026-07-24 (AI assistant test 2026-07-22; other tests 2026-07-23) |
| Also supports | The CPNI "reasonable measures" duty (47 CFR 64.2010(a)) and the evidence behind the annual CPNI certification statement (64.2009(e)) |

## 1. Scope and controls selected
Sole Proprietorship scope: 6-10 controls. **9 controls, 45 determination statements.** Controls were chosen because they guard the two High security risks in P01 (R-001 router takeover, R-002 VoIP portal takeover), the CPNI authentication rules with a High gap in P03 (64.2010(c)), or the CPNI breach notice duty.

| Control | Why selected | Depth / coverage |
|---|---|---|
| SC-7 | Router management exposure (R-001; P03 G-050) | Focused / edge router and management VLAN |
| SI-2 | Router firmware behind a critical advisory (R-001; G-049) | Focused / router, switch, radios, laptop |
| IA-2(1) | MFA on admin accounts, including the VoIP portal (R-002; G-021) | Basic / all 6 SaaS admin accounts and the router |
| IA-5 | Shared and default credentials (R-004) | Focused / laptop password store, 8 access points, 10 customer radios |
| IA-8 | Customer authentication before CPNI (R-003; 64.2010(b), (c), (e), (f)) | Focused / portal, text line, chat |
| CP-9 | Configuration backups (R-011) | Basic / vendor backups and router copies |
| AU-6 | Activity review (64.2010(a) "discover" attempts) | Basic |
| IR-6 | Incident reporting (R-006; 64.2011) | Basic |
| SA-9 | Vendors with CPNI access (R-013; 64.2009(c)) | Basic / 5 vendors and 2 contractors |

## 2. Methods and objects
- **Examine:** SaaS admin and security settings, router filter rules and logging settings, firmware versions and vendor advisories, the laptop password store, the vendor folder, the billing vendor's SOC 2 report, the incident log, P01 and P05.
- **Test (2026-07-22 and 2026-07-23):** a text to the support line from a phone that was not the number of record, using a test account's number and ZIP code; sign-ins to each SaaS admin account from a new browser; port checks from the internet and from a test subscriber connection; credential checks on 8 of 32 access points and 10 of about 310 customer radios; loading the last router configuration onto the spare router.
- **Interview:** replaced by a written **self-review**, because the only person to interview is the assessor. The owner answered the SP 800-53A interview questions in writing, and the network consultant challenged each answer against what was on screen.

## 3. Rules of engagement
- Tests ran after 10:00 p.m. or on a Sunday morning to avoid customer impact. No customer traffic was captured and no customer data was copied; screenshots show settings only.
- The consultant worked only under the terms signed 2026-07-17, through the VPN, in sessions the owner started and watched.

## 4. Results summary
| Result | Determination statements |
|---|---|
| Satisfied | 13 |
| Other than satisfied | 32 |
| **Total** | **45** |

**Fully other than satisfied:** IA-2(1) (the VoIP reseller portal accepted a password alone), IA-8 (the assistant still identifies text users by account number and ZIP code), AU-6, and IR-6.
**Partly satisfied:** CP-9 (4 of 6: vendor backups and document storage work; router copies old and the first restore failed), SC-7 (2 of 6), SI-2 (3 of 10: laptop and SaaS updates work; network firmware does not), IA-5 (3 of 10), SA-9 (1 of 6).
**Fully satisfied:** none.

**New finding:** the access point installed at SITE-3 in 2026-06 still had the vendor-default local password and SNMP community string (IA-05e.). The owner changed both during the session on 2026-07-23. It is now P01 R-015, POL-01 7.3, and part of POAM-005.

**Confirmed fixes:** the 2026-07-22 change to the AI assistant held on retest (no call history on the text line), and the router's web and SSH management no longer answered from the internet after the owner blocked them during the test. Both remain open in the POA&M because the underlying weaknesses are not fully closed.

The 9 controls with weaknesses each have one POA&M item in `poam.csv` (POAM-001 to POAM-009): 3 High, 5 Moderate, 1 Low. The High items are POAM-001 (management filtering), POAM-002 (firmware), and POAM-003 (MFA).

## 5. Deliverables
`assessment-results.csv` (45 rows), `poam.csv` (9 items), and this memo. Accepted by the owner-operator on 2026-08-31. Because independence is limited, POL-01 4.5 requires an outside reviewer at least every second year; the first is planned for July 2027.
