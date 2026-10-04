# Security Assessment Plan and Summary: Cris Santos Company | Retail Trade | Micro

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (neighborhood grocery store with online ordering) |
| System assessed | Store Commerce Platform (SCP), per the SSP (P02) |
| Tier / Vertical | Micro / Retail Trade |
| Procedures | NIST SP 800-53A Rev. 5, Release 5.2.0 (determination statements from NIST OSCAL content) |
| Assessor and independence | Independent security consultant (not a QSA) under a fixed-fee engagement. Did not take part in the risk assessment (P01) or the gap analysis (P03) and operates no control. Accompanied by the Store Manager; MSP technician on call |
| Assessment window | 2026-08-10 to 2026-08-12 (on site 2026-08-11) |
| Also supports | Evidence for the 2026 SAQ P2PE and SAQ A (PCI DSS v4.0.1, N44-45-R01) and the FTC Act Section 5 reasonable-security expectation (N44-45-R02) |

## 1. Scope and controls selected
Micro tier scope: 10-15 controls. **13 controls, 100 determination statements.** Controls were chosen because they support the two High risks in P01 (R-001 skimming, R-002 administrator takeover), cover the High and Moderate PCI DSS gaps in P03 (6.4.3, 11.6.1, 8.2, 8.4, 9.5, 12.8, 12.10), or test what the MSP does for the store.

| Control | Why selected | Depth | Coverage |
|---|---|---|---|
| CM-7, SI-7 | Store-added scripts on the checkout page (P03 G-027, G-055); R-001 | Focused | Comprehensive (every script on the checkout page) |
| CM-8 | No terminal list or inventory (P03 G-042, G-060); R-003, R-004 | Focused | Comprehensive (all 3 card devices, 2 tablets, store phone) |
| AC-2, PS-4 | Shared cashier code; former cashier active (P03 G-033); R-009, R-010 | Focused | Comprehensive (every dashboard user, POS code, online store administrator, and mailbox) |
| IA-2(1) | Administrator logins without MFA (P03 G-035); R-002, R-025 | Focused | Comprehensive (every login above cashier) |
| SC-7 | Flat network and exposed CCTV recorder; R-006, R-008 | Focused | Focused (office PC to other devices; external port check) |
| AT-2, IR-6 | No training and no reporting rule (P03 G-061, G-065); R-012 | Basic | Focused (5 of 7 staff interviewed) |
| SA-9 | Provider, MSP, and freelancer oversight (P03 G-063); R-011, R-022 | Focused | Comprehensive (all 4 outside parties with access) |
| CP-9 | Backup of the office PC; R-021 | Basic | Basic |
| RA-3 | First documented risk assessment (P03 G-058) | Basic | Basic |
| SI-4 | No monitoring of the platform or network; R-025 | Focused | Focused (platform notifications; payout settings) |

## 2. Methods and objects
- **Examine:** dashboard user and POS code lists, online store administrator and app lists, custom code setting, suite user export and MFA settings, payroll roster, the 2025 SAQs, merchant agreement, provider AOC and SOC 2 report, MSP contract, the P01 register, and the MSP evidence listed below.
- **Interview:** Owner, Store Manager, Bookkeeper, both Cashiers, the Order Picker and Delivery Driver, the marketing freelancer, and the MSP technician.
- **Test:**
  - browser capture of the checkout page on 2026-08-11, compared with the capture from 2026-07-28
  - sign-in tests with the Store Manager's dashboard login, the freelancer's online store login (freelancer present), and the firewall login (MSP present)
  - comparison of every account and POS code with the payroll roster
  - a payout settings change attempt with the Store Manager's login, cancelled before saving (Owner present)
  - reachability test from the office PC to the other staff network devices, and an external check of open ports
  - role test of a cashier code on a POS tablet

### MSP evidence requested
The MSP operates the office computers and network, so evidence came from it. Requested on 2026-08-03 with a one-week deadline:

| Item | Supports | Received |
|---|---|---|
| Firewall rule export and port forwarding list | SC-7 | Yes, 2026-08-07 |
| Device list from the remote management tool | CM-8 | Yes, 2026-08-07 |
| Backup job report (July 2026) and retention settings | CP-9 | Yes, 2026-08-07 |
| Record of any restore test | CP-9 | No record exists (confirmed by the MSP) |
| Technician list with access to the store, and MFA on the remote management platform | SA-9 | Not received by fieldwork end; follow-up in POAM-010 |
| MFA status of the firewall and backup console logins | IA-2(1) | Confirmed by test: firewall login has no MFA; backup console not tested |

## 3. Rules of engagement
- No testing with real cards and no changes to the live checkout page. Script review used browser captures only.
- The payout settings test was cancelled before saving, with the Owner watching.
- No customer data left the store. Screenshots were redacted.
- The assessor would stop and tell the Store Manager and Owner at once about any critical exposure. The open port to the CCTV recorder was reported the same day; the MSP closed it on 2026-08-14.

## 4. Results summary
| Result | Determination statements |
|---|---|
| Satisfied | 24 |
| Other than satisfied | 76 |
| **Total** | **100** |

**Fully other than satisfied:** IA-2(1), AT-2, and IR-6. No process or technology met the objective.
**Largely satisfied:** RA-3 (6 of 8 statements; the first risk assessment exists, but no review cycle had been set). CP-9 is half satisfied: backups run, but nobody has ever restored one.
**Mostly inherited where satisfied:** the satisfied statements in SI-7 and CP-9 come from the provider's P2PE solution and platform backups, and in SA-9 from the provider's AOC. The store's own side of those controls is where the gaps are.

**The checkout page result drives the SAQ decision.** CM-7, SI-7, and SI-4 show that nothing controls or watches the scripts around the provider's card fields. The two captures 2 weeks apart showed that the chat widget script had changed version without anyone knowing. Until POAM-001 and POAM-002 close, the store cannot support the SAQ A statement that its site is not susceptible to script attacks (P03 section 1).

**New findings from testing:**
1. The Store Manager's login, which has no MFA, could reach and edit the payout bank account. The only signal is an email to the Owner after a change is saved (SI-04a.02[03], SI-04b.). Added to the risk register as R-025 and to POAM-013.
2. The port forwarded to the CCTV recorder was still open on 2026-08-11 (SC-07a.[02]). Closed by the MSP on 2026-08-14 (R-008 closed).
3. The retired POS tablet in the back office drawer still holds a cached manager login (AC-02f.[05]). Factory reset added to POAM-004.

All 13 controls have at least one weakness and a POA&M item in `poam.csv` (13 items, one per control). The High items are POAM-001, POAM-002, and POAM-005: the checkout page and administrator MFA, the same theme as P01. Eight items are Moderate and two are Low.

## 5. Deliverables
`assessment-results.csv` (100 rows), `poam.csv` (13 items), and this plan and summary. The Owner accepted the results on 2026-08-31.
