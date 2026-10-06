# Security Assessment Plan and Summary: Cris Santos Company | Real Estate | Micro

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (residential real estate brokerage with property management) |
| System assessed | Transaction Management and Closing Communications System (TMCC), per the SSP (P02), with its interface to online banking |
| Tier / Vertical | Micro / Real Estate and Rental and Leasing |
| Procedures | NIST SP 800-53A Rev. 5, Release 5.2.0 (determination statements from NIST OSCAL content) |
| Assessor and independence | Independent security consultant on a fixed fee. Did not take part in the risk assessment (P01) or the gap analysis (P03) and operates no control. Accompanied by the Office Manager; MSP lead technician present for tests |
| Assessment window | 2026-08-17 to 2026-08-19 (on site 2026-08-18) |
| Also serves as | The benchmark Safeguards Rule element for testing key controls (16 CFR 314.4(d)(1)) |

## 1. Scope and controls selected
Micro tier scope: 10-15 controls. **13 controls, 80 determination statements.** Controls were chosen because they support the three High risks in P01 (agent mailbox takeover, spoofed title company instructions, the shared administrator), cover High or Moderate gaps in P03, or test what the MSP and the bank do on the brokerage's behalf.

| Control | Why selected | Depth | Coverage |
|---|---|---|---|
| AC-2 | Departed agent active for 13 days (P01 R-009; P03 G-007, G-008) | Focused | Comprehensive (all 29 users in SYS-01, SYS-02, SYS-03; 4 recent agent departures) |
| AC-5 | Dual control is the main money control (R-002, R-023) | Basic | Comprehensive (all online banking users) |
| IA-2(1) | Shared global administrator without MFA (R-006; G-014) | Focused | Comprehensive (all administrator logins) |
| IA-2(2) | Agents without MFA (R-001, R-005; G-014) | Focused | Comprehensive (all mailboxes) |
| AT-2, IR-6 | No training or reporting rule; agents are the main target (R-001, R-015; G-021) | Basic | Focused (5 employees and 3 agents interviewed) |
| AU-6, SI-4 | No monitoring of mailboxes (R-001, R-025; G-018) | Focused | Comprehensive (forwarding rules in all 29 mailboxes) |
| CP-9, CP-4 | Backup scope and restore never tested (R-008) | Focused | Focused |
| SA-9 | No vendor oversight; MSP reach (R-013, R-014; G-023 to G-025) | Focused | Comprehensive (MSP and 5 SaaS vendors) |
| SC-28 | Unencrypted desktops (R-011; G-011) | Basic | Focused (2 desktops, 1 laptop) |
| SI-8 | Spoofing and look-alike domains (R-004) | Focused | Focused |

## 2. Methods and objects
- **Examine:** user and MFA reports from SYS-01, SYS-02, and SYS-03; administrator role report; online banking entitlement report; agent roster and the last 4 agent departures; draft POL-02 and POL-03; MSP contract; SaaS terms; the transaction platform vendor's SOC 2 report; DNS records; the MSP evidence listed below.
- **Interview:** Broker-owner, Office Manager, Bookkeeper, both Transaction Coordinators, the Property Manager, 3 contractor agents, and the MSP lead technician.
- **Test** (with the Office Manager's written approval and the MSP present):
  - user lists compared against the roster in SYS-01, SYS-02, and SYS-03
  - sign-in to the shared global administrator and the backup console from a new browser, to see whether a second factor is requested
  - a legacy-protocol sign-in to a test mailbox
  - forwarding rule report for all 29 mailboxes
  - a test message from a look-alike domain registered by the assessor, sent to the Office Manager
  - encryption status on 2 desktops and 1 laptop

### MSP evidence requested
The MSP operates the device, network, and backup controls, so evidence came from it. Requested on 2026-08-10 with a one-week deadline:

| Item | Supports | Received |
|---|---|---|
| Monthly patch report (July 2026) | SI-2 (context) | Yes, 2026-08-14 |
| Antivirus console export | SI-3 (context) | Yes, 2026-08-14 |
| Device encryption report | SC-28 | Yes, 2026-08-14 |
| Backup job report (July 2026), scope, and retention settings | CP-9 | Yes, 2026-08-17 |
| Record of any restore test | CP-4 | No record exists (confirmed by the MSP) |
| Firewall alert settings | SI-4 | Yes, 2026-08-14 |
| Technician list and MFA on the remote management platform | AC-17, SA-9 | Not received by fieldwork end; follow-up in POAM-009 |
| MSP security practices questionnaire | SA-9 | Not received by fieldwork end; follow-up in POAM-009 |

## 3. Rules of engagement
- No test could move money or change a payment setting. Online banking was examined from the entitlement report only.
- No client information left the office. Screenshots were redacted before they went into the evidence folder.
- Agents' mailboxes were examined only for forwarding rules and sign-in settings, not message content.
- The assessor would stop and tell the Office Manager at once about any critical exposure. The forwarding rules were reported on 2026-08-18 and removed on 2026-08-19.

## 4. Results summary
| Result | Determination statements |
|---|---|
| Satisfied | 17 |
| Other than satisfied | 63 |
| **Total** | **80** |

**Fully other than satisfied:** IA-2(1), IA-2(2), AT-2, AU-6, CP-4, IR-6, SC-28. No process or technology met the objective.
**Largely satisfied:** SI-8 (the vendor's filtering works; the brokerage's own domain policy does not act on spoofing).
**Strengths:** account roles in the SaaS platforms (AC-02c. to AC-02d.03[01]) and the bank's separation of initiator and approver (AC-05b.).

**New findings from testing:**
1. Three contractor agent mailboxes had rules forwarding all mail to personal webmail accounts (SI-04b.). Added to the risk register as R-025 and to POAM-004.
2. A legacy-protocol sign-in to a test mailbox succeeded with a password alone, so MFA would not stop an attacker using that route even for employees (IA-02(02)). POAM-003.
3. The scanning workstation held 340 scanned IDs and bank statements in a local folder on an unencrypted disk (SC-28). POAM-010.

All 13 controls have at least one weakness and a POA&M item in `poam.csv`. The High items are POAM-002, POAM-003, and POAM-004: administrator MFA, agent MFA, and mailbox monitoring, the same email channel theme as P01.

## 5. Deliverables
`assessment-results.csv` (80 rows), `poam.csv` (13 items), and this plan and summary. The Broker-owner accepted the results on 2026-09-14.
