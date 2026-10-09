# Security Assessment Plan and Summary: Cris Santos Company | Arts, Entertainment, and Recreation | Micro

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (live event venue operator with ticketing; one music club) |
| System assessed | Ticketing and Venue Operations Platform (TVOP), per the SSP (P02) |
| Tier / Vertical | Micro / Arts, Entertainment, and Recreation |
| Procedures | NIST SP 800-53A Rev. 5, Release 5.2.0 (determination statements from NIST OSCAL content) |
| Assessor and independence | Independent security consultant with payment card experience (not a QSA), under a fixed-fee engagement. Did not take part in the risk assessment (P01) or the gap analysis (P03), operates no control, and will not be the company's ASV. Accompanied by the Venue Manager; MSP account technician on call |
| Assessment window | 2026-08-10 to 2026-08-12 (on site 2026-08-11, a dark night) |
| Also supports | Evidence for the 2026 SAQs (PCI DSS v4.0.1, N71-R04) and FTC reasonable security (N71-R05) |

## 1. Scope and controls selected
Micro tier scope: 10-15 controls. **13 controls, 91 determination statements.** Controls were chosen because they support the four High risks in P01 (website skimming, ticketing account takeover, PCI DSS validation, fee display), cover High gaps in P03, or test what the MSP does on the company's behalf. The fee display risk (R-014) is a pricing practice, not a security control, so it is tracked in P03 and P10 rather than tested here.

| Control | Why selected | Depth | Coverage |
|---|---|---|---|
| AC-2, PS-4 | Shared and stale logins (P03 8.2); R-002, R-006, R-007 | Focused | Comprehensive (all 9 ticketing accounts, website and suite users, API tokens) |
| IA-2(1), IA-5 | No MFA and shared passwords (P03 8.3, 8.4); R-001, R-002 | Focused | Focused (4 sign-in tests; password handling observed) |
| SI-7 | No change detection on the pages that host the checkout widget (P03 6.4.3, 11.6.1); R-001 | Focused | Focused (two page captures compared) |
| CM-8 | No inventory of readers and scripts (P03 9.5, 12.5); R-011 | Focused | Comprehensive (physical count of every device and reader) |
| SC-7 | Flat staff network (P03 1.3); R-003, R-010 | Focused | Focused (traffic tests from both Wi-Fi networks) |
| SI-12 | Card data in email and on paper (P03 3.2, 3.3); R-004, R-013 | Basic | Focused (repeat card-number search) |
| AT-2, IR-6 | No training or reporting (P03 12.6, 12.10); R-008, R-021 | Basic | Focused (5 employees and 2 contractor door leads interviewed) |
| AU-6 | No log review (P03 10.4) | Basic | Basic |
| CP-9 | Backup gaps (P04 finding 4); R-012 | Focused | Basic |
| SA-9 | No service provider oversight (P03 12.8); R-015, R-022 | Focused | Comprehensive (all 9 providers and integrations) |

## 2. Methods and objects
- **Examine:** ticketing user, role, and API token lists; ticketing security settings; website account settings and plugin list; suite user export and MFA report; firewall export; backup report and settings; vendor contracts, the ticketing vendor's AOC and SOC 2 report, and the P2PE listings; the termination record for the former Marketing Coordinator; the P01 risk register.
- **Interview:** Owner, Venue Manager, Box Office and Ticketing Manager, Marketing Coordinator, Bar Manager, Bookkeeper, the web designer, the MSP account technician, and 2 contractor door leads (on training, card handling, and incident reporting).
- **Test:**
  - sign-ins without a second factor to a ticketing administrator test account, the website administrator login, the backup console, and the firewall management page (with the MSP present)
  - reconciliation of the 9 ticketing accounts and all API tokens against the staff and contractor roster
  - traffic tests from a laptop on the staff Wi-Fi and a phone on the guest Wi-Fi
  - a physical count of computers, tablets, scanners, and P2PE readers with serial numbers
  - a second browser capture of an event page, compared with the P03 capture of 2026-07-21
  - a repeat card-number search of the mailboxes and the back-office PC

### What each test could show
The new policies (P06) were drafted from 2026-07-27 to 2026-08-07 and were drafts during fieldwork; they were approved on 2026-08-31, after fieldwork ended. The drafts were therefore reviewed for design only. A control that a draft policy introduces has not operated yet, so it cannot be tested for operation. The `test_type` column in `assessment-results.csv` says which kind of conclusion each determination statement supports:

| Test type | Meaning | Statements |
|---|---|---|
| Operating effectiveness | The control or practice existed before the assessment and was tested on records, samples or live systems | 40 |
| Design | The control exists only in a draft policy (POL-02 B.9 password rules; POL-03 4.2 incident reporting); its design was reviewed. Operation is tested at the 2027-02 follow-up | 3 |
| Not implemented | Nothing existed to test | 48 |

Evidence for every statement is listed in the [evidence register](../step-00_P00_intake/evidence-register.csv) under the `evidence_ref` IDs (EV-AC-2 and so on), with the population each test was drawn from (for example, the ticketing accounts were compared with the 7 employees and the March 2026 departure in EV-001 and the 9 accounts in EV-004, and the computers come from the MSP device list in EV-019).

### MSP evidence requested
The MSP operates most technical controls, so evidence came from it. Requested on 2026-08-03 with a one-week deadline:

| Item | Supports | Received |
|---|---|---|
| Monthly patch report (July 2026) | SI-2 context | Yes, 2026-08-07 |
| Anti-malware console export | SI-3 context | Yes, 2026-08-07 |
| Encryption report for the 5 office computers | SC-28 context | Yes, 2026-08-07 |
| Backup job report (July 2026) and retention settings | CP-9 | Yes, 2026-08-10 |
| Record of any restore test | CP-9 | No record exists (confirmed by the MSP) |
| Firewall rule export | SC-7 | Yes, 2026-08-07 |
| Technician list with access, and MFA on the remote management tool | AC-17, SA-9 | Not received by fieldwork end; follow-up in POAM-012 |

## 3. Rules of engagement
- No testing during a show, an on-sale, or doors. On-site tests ran on a dark night (2026-08-11).
- No real card data was entered, copied, or photographed. The repeat card-number search reported matches by location only.
- No change was made to the website or ticketing settings during testing. Findings were handed to the system owners to fix.
- The assessor would stop and tell the Venue Manager at once about any critical exposure. **One was found:** the forgotten API token (below), reported the same day.

## 4. Results summary
| Result | Determination statements |
|---|---|
| Satisfied | 17 |
| Other than satisfied | 74 |
| **Total** | **91** |

**Fully other than satisfied (no statement satisfied):** IA-2(1), AT-2, AU-6, SI-7, IR-6, SI-12. For these, no process or technology existed.
**Partly satisfied:** SC-7 (3 of 6: the firewall and guest Wi-Fi separation work; inside the staff network nothing is separated), CP-9 (2 of 6), IA-5 (3 of 10), AC-2 (5 of 26: roles are well defined in the platform, but nothing around them is managed).

**New findings from testing:**
1. **A forgotten integration.** A 2024 API token for a former email marketing service, with patron read access, was still sending patron records every night to the company's lapsed account at that service (SA-09a.[02], AC-02h.01). The Marketing Coordinator revoked it on 2026-08-12 and asked the former service in writing to delete the data. Added to the risk register as R-023 and to POAM-012.
2. **Page content changed during the assessment.** A seventh script, a sponsor's tracking tag added by the web designer at the sponsor's request, appeared on the event pages between the captures of 2026-07-21 and 2026-08-11. Nobody at the company knew. This confirms that SI-7 is the control that would catch the P08 scenario, and it does not exist (POAM-008).
3. **The flat network is real.** A laptop on the staff Wi-Fi reached the back-office PC's shared folder and both door tablets (SC-07a.[04]; POAM-009).
4. **MFA test:** the ticketing administrator test account, the website administrator login, the backup console, and the firewall management page all accepted a password alone (IA-02(01); POAM-003).
5. **Excess rights:** the web designer's ticketing account held the marketing role with patron export rights it does not need. Removed on 2026-08-12 (POAM-001).

All 13 controls have at least one weakness and a POA&M item in `poam.csv`. The High items are POAM-001, POAM-003, and POAM-008: logins and the website, the same theme as the High risks in P01.

## 5. Deliverables
`assessment-results.csv` (91 rows), `poam.csv` (13 items), and this plan and summary. The Owner and General Manager accepted the results on 2026-08-31.
