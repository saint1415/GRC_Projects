# Security Assessment Plan and Results Memo: Cris Santos Company | Agriculture | Sole Proprietorship

| Field | Value |
|---|---|
| Organization | Cris Santos Company (precision-agriculture crop farm) |
| System assessed | Farm Management and Irrigation Control Platform (FMICP), per the system profile (P02) |
| Tier / Vertical | Sole Proprietorship / Agriculture, Forestry, Fishing and Hunting |
| Procedures | NIST SP 800-53A Rev. 5, Release 5.2.0 (determination statements from NIST OSCAL content); SP 800-82 Rev. 3 cautions for testing OT |
| Assessor(s) and independence | The owner-operator (self-assessment), assisted by the on-call IT technician. **Independence is limited**: the owner designed, operates, and assessed these controls. The technician ran the network tests and read the settings but also supports the laptop and router |
| Assessment window | 2026-07-13 to 2026-07-17 (tests on 2026-07-16) |
| Criteria | P02 control statements and POL-01 (adopted 2026-08-31; draft rules used as criteria during fieldwork) |

## 1. Scope and controls selected
Sole Proprietorship scope: 6-10 controls. **9 controls, 51 determination statements.** Controls were chosen because they support the High risks in P01 (R-001, R-002, R-005) or a High gap in P03.

| Control | Why selected | Depth / coverage |
|---|---|---|
| IA-2(1) | MFA on the accounts that control irrigation and hold records (R-002; PR.AA-03) | Basic / 5 SaaS accounts |
| IA-5 | Password reuse, browser storage, and default device passwords (R-001, R-005; PR.AA-01) | Focused / all accounts and network and OT devices |
| AC-17 | Dealer and vendor remote control of the pump and pivot (R-004; PR.AA-05) | Basic |
| SC-7 | Flat network shared with customer Wi-Fi (R-005; PR.IR-01) | Focused / Home Farm network |
| CP-9 | Backups and the qualified exemption records (R-007; PR.DS-11; 21 CFR 112.7(b)) | Basic / SaaS and local data |
| SI-3 | Ransomware defense on the laptop, including USB sticks (R-001, R-012) | Focused / laptop |
| SA-9 | Vendors, the dealer, and the AI vendor (R-004, R-011; GV.SC-05) | Basic / 6 providers |
| IR-6 | Incident reporting and Florida notice contacts (R-010; Fla. Stat. 501.171) | Basic |
| RA-3 | Risk assessment (ID.RA) | Basic |

## 2. Methods and objects
- **Examine:** account security pages for SYS-01, booking, email, accounting, and the bank; the SYS-01 user list and support access setting; router settings and connected-device list; the dealer agreement and vendor terms; the FMIS vendor's SOC 2 report; P01 and P05.
- **Test (2026-07-16):** sign-ins from a new browser to each SaaS account; a phone joined to the customer Wi-Fi tried to reach the pump controller's web page; the router and pump controller login pages tried with their published factory passwords (read only: no setting was changed); a standard antivirus test file downloaded and copied from a USB stick; router port check from outside.
- **Interview:** replaced by a written **self-review**, because the only person to interview is the assessor. The owner answered the SP 800-53A interview questions in writing, and the IT technician challenged each answer against what was on screen.

## 3. Rules of engagement (OT safety)
- Following SP 800-82 Rev. 3 cautions on testing live OT, no scanning tool was run against the pump controller or pivot panel. The only OT tests were opening the controller's login page and logging in to read settings, with the pump switched to Off at the panel and outside pivot run times.
- No customer or W-9 data was copied off any system; screenshots were cropped to settings.
- The IT technician worked only in sessions the owner started and watched.

## 4. Results summary
| Result | Determination statements |
|---|---|
| Satisfied | 25 |
| Other than satisfied | 26 |
| **Total** | **51** |

**Fully satisfied:** SI-3 (antivirus caught the test file on download and from the USB stick).
**Fully other than satisfied:** IA-2(1) and IR-6.
**Partly satisfied:** RA-3 (the assessment exists; no review cycle yet), IA-5 (devices protect stored credentials; everything else fails), AC-17 (one remote path, but no rules or authorization for the dealer), SC-7 (inbound blocked, but no internal separation), CP-9 (vendor backups only), SA-9 (only the FMIS vendor is overseen).

**New finding (IA-05e.):** the pump controller's local web page accepted the manufacturer's default password from the laptop, and a phone on the customer Wi-Fi could reach that page (SC-07a.[04], SC-07b.). Anyone given the posted Wi-Fi password could have changed pump, fertigation, or freeze-zone settings. This went back into the risk register as part of R-005 (High) and is tracked in POAM-002 and POAM-004. As an interim step the owner changed the customer Wi-Fi password and took down the posted sign on 2026-07-16; guest isolation follows by 2026-09-15, and the dealer will change the controller password at the September service visit.

The 8 controls with weaknesses each have one POA&M item in `poam.csv` (POAM-001 to POAM-008). The High items are POAM-001 (MFA), POAM-002 (passwords), POAM-004 (network), and POAM-005 (backups).

## 5. Deliverables
`assessment-results.csv` (51 rows), `poam.csv` (8 items), and this memo. Accepted by the owner-operator on 2026-08-31. Because independence is limited, POL-01 4.5 requires an outside reviewer at least every second year.
