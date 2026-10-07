# Security Assessment Plan and Summary: Cris Santos Company | Manufacturing | Small

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (connected medical device manufacturer) |
| System assessed | Device Cloud Service (DCS), per the SSP (P02), plus the device update path it serves: the firmware signing pipeline (SYS-04) and PM-2 and PM-1 monitors tested in the engineering lab |
| Tier / Vertical | Small / Manufacturing (NAICS 334510) |
| Procedures | NIST SP 800-53A Rev. 5, Release 5.2.0 (determination statements from NIST OSCAL content) |
| Assessor(s) and independence | Contracted independent assessor, not involved in designing or operating the controls. Escorted by the IT Manager (device cloud) and the Product Security Lead (lab testing) |
| Assessment window | 2026-08-10 to 2026-08-14 (PM-2 and PM-1 lab testing on 2026-08-12) |
| Also satisfies | HIPAA evaluation for the device cloud, 45 CFR 164.308(a)(8); evidence for 524B related-system processes (P03) |

## 1. Scope and controls selected
Small tier scope: 15-25 controls. **22 controls, 129 determination statements.**

The DCS is a related system of the PM-2 cyber device under FD&C Act 524B(b)(2). For that reason, the COO extended the scope past the SSP boundary to the device update path: the code-signing key on the build server and the credentials and integrity checks of fielded monitors. Controls were chosen because they:
- support the High risks in P01 (R-001, R-002, R-032) and the Moderate risks with the largest PHI exposure (R-008, R-009);
- carry the 524B postmarket elements rated High in P03 (CVD, patching, SBOM, related systems);
- cover HIPAA Security Rule standards for the device cloud with gaps in P03 (access, audit review, contingency, business associate contracts).

| Control | Why selected | Depth | Coverage |
|---|---|---|---|
| AC-2, AC-5, AC-6 | Standing all-tenant production access; signing and backup duties (G-037, G-038); R-008, R-002 | Focused | Focused |
| AU-6, AU-11, SI-4 | No log review or monitoring (G-035); R-006 | Basic | Focused |
| CA-8 | No independent testing (G-024); R-007 | Basic | Basic |
| CM-8, RA-5, RA-5(11), SR-3 | SBOM, vulnerability monitoring, CVD, component supply chain (G-004, G-009, G-017); R-003, R-004, R-013 | Focused | Focused |
| CP-4, CP-9 | Restore never tested; backups not isolated (G-043, G-044); R-016, R-017 | Focused | Focused |
| IA-2, IA-3, IA-5 | Workforce and device authentication (G-021); R-014, R-032 | Focused | Comprehensive (lab tests on 3 PM-2 and 2 PM-1 units) |
| IR-4, IR-6 | No product security incident procedure (G-040, G-063); R-018, R-024 | Focused | Basic |
| SA-9 | Log analytics vendor without a BAA (G-046); R-009 | Focused | Focused |
| SC-12, SI-7 | Code-signing key and firmware integrity (G-022); R-002, R-020 | Focused | Focused |
| SI-2 | No patch cycle for fielded devices (G-007, G-008); R-001 | Focused | Focused |

## 2. Methods and objects
- **Examine:** identity provider and cloud IAM exports, production role list, scan reports, key management policies, backup console and IAM policies, the PM-2 SBOM and release history, contracts and BAAs, the cloud provider's SOC 2 Type 2 report, the corporate incident response plan, and the draft POL-03 and P08 runbook.
- **Interview:** COO, IT Manager, Cloud Operations Lead, VP Engineering, Product Security Lead, VP QA/RA, Compliance Manager (Privacy Officer), Customer Support Manager, and 6 support and field service staff (how they route security reports).
- **Test:**
  - sign-in tests to the cloud console, bastion, and portal support view, including a hardware-key sign-in;
  - an IAM policy simulation of backup deletion by a production administrator role;
  - a test vulnerability report sent to the security@ mailbox on 2026-08-10;
  - **PM-2 lab tests (2026-08-12):** maintenance web interface credentials on 3 production units, loading a modified firmware image, and certificate-based connection to a staging copy of the ingestion gateway;
  - **PM-1 lab tests:** connection of 2 units with the same hospital key.

## 3. Rules of engagement
- No testing against production devices in hospitals or against production tenant data. Lab tests used production-build units and a staging copy of the device cloud.
- No PHI was copied out of the device cloud. Screenshots were redacted.
- The assessor stops and notifies the COO and VP QA/RA at once on finding a vulnerability that could affect patient safety in fielded devices. **This rule was triggered on 2026-08-12** (see section 4).

## 4. Results summary
| Result | Determination statements |
|---|---|
| Satisfied | 52 |
| Other than satisfied | 77 |
| **Total** | **129** |

Of the 77 other-than-satisfied statements, 11 are rated High, 63 Moderate, and 3 Low.

**Fully other than satisfied (10 controls):** AC-5, AC-6, AU-6, AU-11, CA-8, CP-4, IA-3, IR-6, RA-5(11), SC-12. No process or mechanism existed for these at assessment time.
**Fully satisfied (1 control):** IA-2. Workforce users sign in with unique accounts through the identity provider, with hardware keys for privileged roles.
**Largely satisfied:** AC-2 account creation and termination (17 of 26), SI-2 identification and testing of fixes (7 of 10), RA-5 cloud scanning (6 of 9), CP-9 backup jobs and encryption (4 of 6).

**New finding (stop-and-notify).** On 2026-08-12, lab testing found that the PM-2 maintenance web interface accepts **one service password that is the same on every unit** and is printed in the service manual (IA-05b., IA-05e., IA-05g., IA-05i.). The assessor notified the COO and VP QA/RA the same day. Actions:
- added to the risk register as R-032 (High) and to POAM-002;
- handled under the P08 runbook as a potential uncontrolled risk under FDA's postmarket cybersecurity guidance;
- customer advisory with compensating controls due 2026-09-11, and fixed firmware due 2026-10-11 (30 and 60 days after the company learned of the vulnerability).

The other High items are the code-signing key (POAM-003), the missing disclosure channel (POAM-004), and the missing patch cycle (POAM-005).

## 5. Deliverables
- `assessment-results.csv`: 129 rows, one per determination statement
- `poam.csv`: 20 items (4 High, 15 Moderate, 1 Low). Every control with a weakness has an item; AC-6 findings are tracked under POAM-001 with AC-2
- this plan and summary

The COO accepted the results on 2026-09-04 and approved continued operation of the DCS with the POA&M as conditions (SSP section 4.2).
