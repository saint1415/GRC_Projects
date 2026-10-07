# Security Assessment Plan and Summary: Cris Santos Company | Construction | Micro

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (commercial and institutional building general contractor) |
| System assessed | Project and Payment System (PPS), per the SSP (P02) |
| Tier / Vertical | Micro / Construction |
| Procedures | NIST SP 800-53A Rev. 5, Release 5.2.0 (determination statements from NIST OSCAL content) |
| Assessor and independence | Independent security consultant under a fixed-fee engagement ($3,500). Did not take part in the risk assessment (P01) or the gap analysis (P03) and operates no control. Accompanied by the Office Manager; MSP lead technician on call and on site for the tests |
| Assessment window | 2026-08-17 to 2026-08-19 (office and 2 jobsites visited 2026-08-18) |
| Relationship to CMMC | A readiness check only. The CMMC Level 1 self-assessment itself must use the NIST SP 800-171A (June 2018) objectives (32 CFR 170.15(c)(1)) and is scheduled for early December 2026. The controls below were chosen so that each of the 15 FAR 52.204-21 requirements is tested through at least one mapped SP 800-53 control |

## 1. Scope and controls selected
Micro tier scope: 10-15 controls. **15 controls, 97 determination statements.** Controls were chosen for one of three reasons:
- they map to a FAR 52.204-21 requirement (P03, through the SP 800-171 Rev. 3 tailoring tables);
- they support the Very High and High risks in P01 (business email compromise, bank-change fraud);
- they test what the MSP does on the company's behalf, or the Section 889 duty.

| Control | Why selected | Depth | Coverage |
|---|---|---|---|
| AC-2, IA-2 | FAR (b)(1)(i), (v); departed Superintendent's accounts; shared mailbox (P01 R-005, R-011) | Focused | Comprehensive (every user in the suite, SYS-01, SYS-02, SYS-03, bank portal) |
| AC-5 | FAR (b)(1)(ii); bank-change fraud (P01 R-002, High) | Focused | Focused (walk-through of one vendor bank change) |
| IA-2(1), IA-2(2) | FAR (b)(1)(vi); mailbox takeover (P01 R-001, Very High); MSP-held administrator logins | Focused | Focused |
| AC-20 | FAR (b)(1)(iii); FCI in personal email and the AI tool | Basic | Focused (all 3 field and project staff interviewed) |
| AU-6 | Detection of mailbox compromise (P01 R-001) | Basic | Comprehensive (rules on all 6 mailboxes) |
| AT-2 | Payment-fraud awareness (P01 R-001, R-002, R-015) | Basic | Comprehensive (all 5 email users) |
| MP-6 | FAR (b)(1)(vii) | Basic | Basic |
| PE-3 | FAR (b)(1)(viii), (ix) | Basic | Focused (office and 2 jobsites) |
| SC-7 | FAR (b)(1)(x), (xi) | Focused | Focused |
| SI-2, SI-3 | FAR (b)(1)(xii)-(xv); MSP-run controls | Focused | Focused (2 laptops and the desktop; alert routing test) |
| CP-9 | Backup of email and files (P01 R-013) | Focused | Focused (single-file restore) |
| SR-5 | Section 889 (FAR 52.204-25(b)(1)); FC-1 recorder (P01 R-008) | Focused | Comprehensive (all 4 federal low-voltage and network submittals on FC-1) |

## 2. Methods and objects
- **Examine:** user exports from the suite, SYS-01, SYS-02, and SYS-03; bank portal roles; SYS-02 vendor-change log; mailbox rules for all 6 mailboxes; the MSP evidence listed below; the FC-1 submittal log and subcontracts; asset and lease records; the SYS-01 vendor's SOC 2 report.
- **Interview:** Owner, Office Manager, Project Manager and Estimator, both Superintendents, one Carpenter (visitors and keys), and the MSP lead technician.
- **Test:**
  - sign-in attempts without a second factor to the bids mailbox, a staff SYS-01 account, the backup console, and the firewall management page (with the MSP present)
  - a walk-through of a vendor bank change in SYS-02 using a test vendor, then deleted
  - a visitor laptop on the office Wi-Fi, to see what it could reach
  - patch status on 2 laptops and the desktop; firewall and printer firmware versions
  - a harmless industry-standard antivirus test file on 1 laptop at 17:45, to check detection and after-hours alert routing
  - a single-file restore from the email and file backup

### MSP evidence requested
The MSP operates most technical controls, so evidence came from it. Requested on 2026-08-10 with a one-week deadline:

| Item | Supports | Received |
|---|---|---|
| Monthly patch report (July 2026) and patch policy | SI-2 | Yes, 2026-08-14 |
| Antivirus console export (all devices) and alert settings | SI-3 | Yes, 2026-08-14 |
| Laptop encryption report | SC-28 (context) | Yes, 2026-08-14 |
| Backup job report (July 2026) and retention settings | CP-9 | Yes, 2026-08-17 |
| Record of any restore test | CP-9 | No record exists (confirmed by the MSP) |
| Firewall rule export, Wi-Fi configuration, and firmware record | SC-7, SI-2 | Yes, 2026-08-14 |
| Technician list with access to the company, and proof of MFA on the remote management platform | AC-17, IA-2(1) | Not received by fieldwork end; follow-up in POAM-004 |

## 3. Rules of engagement
- No testing that could disrupt payroll, a pay app, or a bid. The SYS-02 walk-through used a test vendor that was deleted the same day; no payment was released.
- No FCI or payroll data left the company. Screenshots were redacted before they went into the evidence folder.
- The assessor would stop and tell the Office Manager and Owner at once about any critical exposure. The forwarding rule found under AU-6 was reported and removed on 2026-08-18.

## 4. Results summary
| Result | Determination statements |
|---|---|
| Satisfied | 24 |
| Other than satisfied | 73 |
| **Total** | **97** |

**Fully other than satisfied:** AC-5, AC-20, AT-2, AU-6, IA-2(1), IA-2(2), MP-6, SR-5. No process or technology met the objective.
**Largely satisfied:** SI-3 (detection, updates, scanning, and quarantine work; only after-hours alerting fails), and CP-9 (backups run daily and are encrypted; integrity and restore are unproven).

**New findings from testing:**
1. **Forwarding rule (AU-6, AC-20).** The Project Manager's mailbox had an inbox rule, created in 2025, forwarding all mail from the FC-1 Contracting Officer to a personal address "to read on the phone". It was a convenience, not an attack, but it sent FCI outside the boundary. Removed 2026-08-18. Tracked in POAM-003 and POAM-005.
2. **Password-only sign-ins (IA-2(1), IA-2(2)).** The bids mailbox, a staff SYS-01 account, the backup console, and the firewall management page all accepted a password alone. POAM-004 and POAM-007.
3. **Visitor Wi-Fi reaches company devices (SC-7).** A visitor laptop on the office Wi-Fi opened the printer's web page and saw the desktop's shared scan folder, which held scanned drawings. POAM-011.
4. **Alert routing (SI-3).** The test-file alert at 17:45 was not seen by the MSP until 08:30 the next day. POAM-014.

All 15 controls have at least one weakness and a POA&M item in `poam.csv`. POAM-016 (DMARC, SI-8) comes from P01 and P04 rather than this assessment, making 16 items. The High items are POAM-002 and POAM-007: bank-change approval and phishing-resistant sign-in, the same payment theme as P01. **The POA&M is an internal work plan.** CMMC Level 1 permits no POA&M (32 CFR 170.21(a)(1)), so every item mapped to a FAR requirement must be closed before the Owner affirms.

## 5. Deliverables
`assessment-results.csv` (97 rows), `poam.csv` (16 items), and this plan and summary. The Owner accepted the results on 2026-08-31.
