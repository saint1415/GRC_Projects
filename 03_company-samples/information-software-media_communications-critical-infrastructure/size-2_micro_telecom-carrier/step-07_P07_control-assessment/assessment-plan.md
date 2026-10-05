# Security Assessment Plan and Summary: Cris Santos Company | Communications | Micro

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (rural fiber broadband and voice carrier) |
| System assessed | Network Operations and Customer Billing Platform (OSS/BSS), per the SSP (P02) |
| Tier / Vertical | Micro / Communications |
| Procedures | NIST SP 800-53A Rev. 5, Release 5.2.0 (determination statements from NIST OSCAL content) |
| Assessor and independence | Independent security consultant with telecom experience, under a fixed-fee engagement. Did not take part in the risk assessment (P01) or the gap analysis (P03) and operates no control. Accompanied by the Office Manager; the Network Operations Lead and the MSP lead technician joined the tests of their systems |
| Assessment window | 2026-08-10 to 2026-08-12 (on site at the office and the hut 2026-08-11) |
| Also supports | Evidence for the annual CPNI certification statement (47 CFR 64.2009(e)) and the "reasonable measures" duty (64.2010(a)) |

## 1. Scope and controls selected
Micro tier scope: 10-15 controls. **13 controls, 93 determination statements.** Controls were chosen because they support the four High risks in P01 (router and VPN foothold, CDR theft from the voice platform, customer records through the API key, middle-mile loss), cover CPNI rules with High gaps in P03, or test what the MSP and the consultant do for the company.

| Control | Why selected | Depth | Coverage |
|---|---|---|---|
| AC-2 | Shared logins; a departed technician still knew the network password (P01 R-005; P03 G-047) | Focused | Comprehensive (all BSS, voice platform, suite, VPN, and network accounts) |
| AC-17, SC-7 | Remote access and the hut network are the intrusion path in P08 (R-001, R-020) | Focused | Focused |
| IA-2(1), IA-5 | No MFA on the voice platform and VPN; secrets in plain text (R-002, R-006) | Focused | Focused (4 sign-in tests; SNMP test on 3 devices) |
| IA-8 | Customer authentication under 64.2010 (P03 G-021 to G-026; R-003, R-004) | Focused | Focused (portal, assistant, 10 phone requests) |
| AT-3, IR-6 | No CPNI training; no reporting rule (64.2009(b); 64.2011) | Basic | Focused (5 of 7 staff interviewed) |
| AU-6 | No log review (R-010) | Basic | Basic |
| CP-9 | Configuration backups in one place, never restored (R-007) | Focused | Focused (one restore test) |
| RA-5, SI-2 | Out-of-date router and OLT firmware (R-001) | Focused | Comprehensive for network devices; MSP report for office IT |
| SA-9 | Vendors that hold CPNI or run part of the network (R-017, R-020, R-023) | Focused | Comprehensive (all 7 vendors) |

## 2. Methods and objects
- **Examine:** user and role lists for the BSS, voice platform, suite, VPN, and network devices; router and OLT configurations and version records; EMS backup list; contract folder; BSS vendor SOC 2 report; POL-02, POL-03, POL-04; P01 risk register; the MSP evidence listed below.
- **Interview:** Owner and General Manager, Office Manager, Network Operations Lead, both Customer Service Representatives, one Field Technician, the network engineering consultant (by phone), and the MSP lead technician.
- **Test:**
  - user lists compared against the staff list in every system
  - sign-in attempts without a second factor to the voice platform portal, the router VPN, the EMS, and the cloud backup console
  - SNMP queries with vendor default community strings against the 2 OLTs and the aggregation switch (read-only queries)
  - an external port check of the hut address range
  - a portal password reset and an AI assistant session on a test account
  - a review of 10 BSS tickets where a customer asked for call detail
  - a restore of one OLT configuration to the spare chassis in the warehouse

### MSP and consultant evidence requested
The MSP runs office IT and the consultant configures the network, so evidence came from them. Requested on 2026-08-03 with a one-week deadline:

| Item | Supports | Received |
|---|---|---|
| Monthly patch report (July 2026) and patch policy | SI-2 | Yes, 2026-08-06 (MSP) |
| Antivirus console export and device encryption report | Context for SI-3, SC-28 | Yes, 2026-08-06 (MSP) |
| Suite backup job report and retention settings | CP-9 | Yes, 2026-08-07 (MSP) |
| Office firewall rule export | SC-7 | Yes, 2026-08-06 (MSP) |
| Router and OLT configuration documentation and change history | SC-7, SI-2, AC-17 | Configuration documented; no change history kept (consultant) |
| Confirmation of how the consultant protects its own computers and the VPN credential | AC-17, SA-9 | Not received by fieldwork end; follow-up in POAM-002 and POAM-011 |
| Voice platform provider security evidence (SOC report or questionnaire) | SA-9 | Not requested before this assessment; requested 2026-08-12 (POAM-011) |

## 3. Rules of engagement
- No testing that could disrupt service. Network tests were read-only and ran in the 2026-08-11 maintenance window (10:00 p.m. to midnight). The restore test used the spare chassis in the warehouse, not a live OLT.
- No CPNI left the company. The portal and assistant tests used a test account. Ticket screenshots were redacted before they went into the evidence folder.
- The assessor would stop and tell the Office Manager at once about any critical exposure. The default SNMP read-write string was reported the same night.

## 4. Results summary
| Result | Determination statements |
|---|---|
| Satisfied | 17 |
| Other than satisfied | 76 |
| **Total** | **93** |

**Fully other than satisfied:** AT-3, AU-6, IA-2(1), IA-8, IR-6, RA-5. No process or technology met the objective.
**Partly working:** SC-7 (the edge filters work and nothing management-facing is exposed since 2026-08-03; inside the hut there is no segmentation), CP-9 (backups run nightly; they are not protected or off site), and AC-2 (named BSS accounts match staff; everything around them is undocumented).

**New findings from testing:**
1. The aggregation switch answered a vendor default SNMP read-write community string (IA-05e.). Added to the risk register as R-024 and to POAM-004. Removal of read-write SNMP is scheduled for 2026-09-15 in the next maintenance window.
2. The first restore of an OLT configuration to the spare chassis failed until the consultant matched the firmware version (CP-09d.[02]). The backups work, but only someone who knows the firmware history can use them. POAM-008.
3. The portal reset test succeeded with only the account number and last name, both printed on the bill (IA-08). POAM-005.

All 13 controls have at least one weakness and a POA&M item in `poam.csv`. The High items are POAM-002, POAM-003, POAM-004, POAM-005, POAM-010, POAM-012, and POAM-013: the intrusion path into the hut, the credentials found there, and the customer authentication gaps, the same themes as P01.

## 5. Deliverables
`assessment-results.csv` (93 rows), `poam.csv` (13 items), and this plan and summary. The Owner and General Manager accepted the results on 2026-08-31.
