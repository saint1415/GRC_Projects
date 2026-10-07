# Security Assessment Plan and Summary: Cris Santos Company | Manufacturing | Micro

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (medical device startup) |
| System assessed | Product Development and Release Platform (PDRP), per the SSP (P02), plus the release path to WM-1 units and the contract manufacturer |
| Tier / Vertical | Micro / Manufacturing (NAICS 334510) |
| Procedures | NIST SP 800-53A Rev. 5, Release 5.2.0 (determination statements from NIST OSCAL content) |
| Assessor and independence | Independent medical device cybersecurity consultant under a fixed-fee engagement. Did not take part in the risk assessment (P01) or the gap analysis (P03) and operates no control. Accompanied by the Operations Manager; the Head of Engineering and the MSP lead technician on call |
| Assessment window | 2026-08-10 to 2026-08-12 (lab testing 2026-08-11) |
| Also supports | QMSR internal evaluation of the security parts of design controls and supplier control; evidence of independent review for the 510(k) cybersecurity section |

## 1. Scope and controls selected
Micro tier scope: 10-15 controls. **13 controls, 111 determination statements.** Controls were chosen because they support the four High risks in P01 (signing key, shared device credentials, submission readiness, unmonitored components), cover section 524B gaps in P03, or test what the MSP and the contract manufacturer do for the company.

| Control | Why selected | Depth | Coverage |
|---|---|---|---|
| AC-2, PS-4 | Informal offboarding; engineering accounts outside any checklist (P01 R-011, R-006) | Focused | Comprehensive (every account in the suite, eQMS, repository, and cloud) |
| IA-2(1) | Shared cloud owner account; MSP-held logins (R-008) | Focused | Focused |
| IA-5 | Shared hub password and API key (P03 G-032; R-002) | Focused | Focused (2 lab hubs; CI logs; provisioning file) |
| SC-12 | Signing key custody (P03 G-033; R-001) | Focused | Comprehensive (the one key) |
| SI-7 | Secure boot and update integrity (P03 G-034) | Focused | Focused (2 hubs, 2 sensors) |
| CM-8 | Inventory and SBOM (524B(b)(3); R-005) | Basic | Comprehensive |
| RA-5 | Vulnerability monitoring and CVD (524B(b)(1); R-005, R-010) | Focused | Focused (3 hub components spot-checked) |
| SA-11 | Security testing (P03 G-038; R-003) | Basic | Focused |
| CP-9 | Backups of design history, cloud, and the key (R-013, R-015) | Basic | Focused |
| SI-2 | MSP patching and the unmanaged lab workstations (R-007, R-016) | Focused | Focused (2 laptops, 2 lab workstations) |
| SR-3 | Contract manufacturer handoff (P03 G-016, G-017; R-009) | Basic | Focused |
| IR-8 | Draft runbook (P03 G-040) | Basic | Basic |

## 2. Methods and objects
- **Examine:** suite, eQMS, repository, and cloud user lists; staff and contractor roster; MFA settings; CI build logs; hub base image configuration; provisioning file; release notes; verification plan and reports; anomaly list; supplier procedure, quality agreement, and 2025 audit report; draft runbook; the MSP evidence listed below.
- **Interview:** CEO, Head of Engineering, Cloud Software Engineer, Verification and Test Engineer, QA/RA Manager, Operations Manager, and the MSP lead technician.
- **Test:**
  - account lists compared with the roster in every system
  - sign-in attempts to the cloud owner account and the firewall management page (with the MSP present)
  - default maintenance password tried on 2 lab hubs; debug serial port read on 1 lab hub
  - modified software and firmware images loaded onto 2 hubs and 2 sensors to confirm secure boot and update checks
  - CI build logs searched for secrets
  - operating system version check on the 2 lab workstations and 2 laptops
  - 3 hub components checked against public vulnerability databases

### MSP evidence requested
The MSP operates the laptops and the network, so evidence came from it. Requested on 2026-08-03 with a one-week deadline:

| Item | Supports | Received |
|---|---|---|
| Monthly patch report (July 2026) and patch policy | SI-2 | Yes, 2026-08-06 |
| EDR console export | SI-2 (context), SI-3 | Yes, 2026-08-06 |
| Laptop encryption report | SC-28 (context) | Yes, 2026-08-06 |
| Firewall rule export and management login settings | IA-2(1), SC-7 | Yes, 2026-08-07 |
| Offboarding tickets for 2025-2026 | AC-2, PS-4 | Yes, 2026-08-07 |
| Technician list with access and MFA on the remote management platform | AC-17 | Not received by fieldwork end; follow-up tracked in the SSP (AC-17) |

The contract manufacturer supplied its 2025 audit response and the pilot build transfer record on 2026-08-07.

## 3. Rules of engagement
- Tests ran on lab units only. The 8 hubs at the partner hospital simulation center were not touched.
- The signing key was inspected in place (existence, protection, backup) and never copied or used.
- Secrets found during testing were reported to the Head of Engineering at once and not written into the working papers.
- The assessor would stop and report any critical exposure the same day. The CI log exposure and the contractor account were both reported on 2026-08-11.

## 4. Results summary
| Result | Determination statements |
|---|---|
| Satisfied | 35 |
| Other than satisfied | 76 |
| **Total** | **111** |

**Fully other than satisfied:** IA-2(1) and SC-12. No process or technology met the objective.
**Largely satisfied:** SA-11 (functional testing, records, and flaw tracking work; security testing is missing), SI-7 (secure boot and update verification on the devices work; nothing checks integrity outside the device), and IR-8 (the draft runbook is sound but was not approved, distributed, or tested at fieldwork).

**New findings from testing:**
1. A former firmware contractor still had write access to the firmware repository 5 months after the engagement ended (AC-02f.[04], AC-02i.01). Removed on 2026-08-11; the audit log showed no activity after the end date. Recorded in P01 R-011 and POAM-001.
2. The hub API key was printed in plain text in CI build logs readable by all repository members (IA-05g.). The debug step was removed and the logs purged on 2026-08-12. Added to the risk register as R-023; POAM-004.
3. The API key is stored unencrypted on the hub and could be read through the debug serial port of a lab unit (IA-05h.[02]). Added to R-002; POAM-004.
4. The default maintenance password worked on both lab hubs tested (IA-05e.).
5. The hub's TLS library version has published vulnerabilities that nobody has assessed (RA-05c.). POAM-006.

All 13 controls have at least one weakness and a POA&M item in `poam.csv`. The High items are POAM-003 to POAM-007: the signing key, device credentials, SBOM, vulnerability monitoring, and security testing. They are the same items the 510(k) will need (P03).

## 5. Deliverables
`assessment-results.csv` (111 rows), `poam.csv` (13 items), and this plan and summary. The CEO accepted the results on 2026-08-31.
