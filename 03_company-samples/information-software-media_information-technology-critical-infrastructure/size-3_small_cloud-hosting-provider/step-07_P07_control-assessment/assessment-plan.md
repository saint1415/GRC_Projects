# Security Assessment Plan and Summary: Cris Santos Company | Information Technology | Small

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (cloud hosting and managed infrastructure provider) |
| System assessed | Hosting Control Plane and Customer Portal (HCP), per the SSP (P02) |
| Tier / Vertical | Small / Information Technology |
| Procedures | NIST SP 800-53A Rev. 5, Release 5.2.0 (determination statements from NIST OSCAL content) |
| Assessor(s) and independence | Contracted independent assessor, not involved in operating or designing the controls. The FedRAMP advisor took no part in the assessment, to keep advice and assessment separate. Escorted by the IT Manager |
| Assessment window | 2026-08-10 to 2026-08-21 (DC-1 walkthrough 2026-08-12; DC-2 visit 2026-08-18) |
| Purpose | Mock assessment before any FedRAMP independent assessment (P03 roadmap), and evidence for SOC 2 readiness (P09) |
| Results accepted | 2026-09-25 by the COO (Moderate and below) and the CEO (High and Very High) |

## 1. Scope and controls selected
Small tier scope: 15-25 controls. **22 controls, 185 determination statements** (every determination statement NIST lists for each selected base control).

Controls were chosen because they:
- support the Very High and High risks in P01;
- carry High gaps in the FedRAMP Class C readiness analysis (P03); or
- underpin the bank notice duty and the SOC 2 examination.

PE-3 was added to confirm the controls inherited from the colocation providers.

| Control | Why selected | Depth | Coverage |
|---|---|---|---|
| AC-2, AC-17, IA-2, IA-5 | Shared RMM and hypervisor accounts; open RMM console; default BMC accounts (R-001 Very High, R-003, R-026) | Focused | Focused (all RMM accounts; 24 of 96 BMCs) |
| AC-6, SC-7 | Control plane master credentials; management network exposure (R-002, R-003) | Focused | Focused |
| AU-2, AU-6, SI-4 | Missing management-plane logs; no review; AI auto-close (R-015, R-016) | Focused | Basic |
| CM-3, CM-6, SA-10 | Informal data center changes; review bypass; hardening (R-011, R-017) | Focused | Focused (20 production changes) |
| CP-2, CP-4, CP-9 | No contingency plan, restore tests, or isolated backups (R-004, R-005, R-018) | Focused | Focused |
| IR-4, IR-6 | No incident plan; bank notice duty (R-022, R-029) | Focused | Basic |
| RA-5, SI-2 | Scanning and patching of hypervisors and BMCs (R-006) | Focused | Focused (all 96 hosts' versions) |
| SC-28 | Encryption at rest and module validation (R-031) | Basic | Basic |
| SA-9 | Critical vendor oversight (R-025) | Focused | Focused (6 critical vendors) |
| PE-3 | Inherited physical controls | Basic | Focused (both sites) |

## 2. Methods and objects
- **Examine:**
  - identity provider, cloud IAM, RMM, and hypervisor account exports
  - firewall and network rule exports
  - SIEM source list and AI triage settings
  - backup configuration and job history
  - pull-request history, scan reports, and patch reports
  - vendor contracts and the DC-1 colocation SOC 2 Type 2 report
- **Interview:** COO, IT Manager, Director of Platform Engineering, Engineering Manager (Control Plane), Managed Services Lead, NOC and Support Manager, Controller, HR Manager, and 8 randomly selected staff (incident reporting awareness).
- **Test:**
  - RMM console sign-in from a non-company network, with the assessor's own test account
  - hypervisor manager and BMC sign-in from the bastion and from a NOC workstation
  - default-credential check on 24 BMCs (12 per site), outside customer change windows
  - backup deletion permission check with a cloud administrator role, dry run only
  - a harmless test script run through the RMM tool against a lab server set up as a customer, to see if the SIEM detects it

## 3. Rules of engagement
- No test that could disrupt customer workloads. BMC tests used read-only sign-in checks; no host was rebooted.
- No customer data was viewed or copied. Screenshots were redacted.
- The assessor was to stop and notify the IT Manager on finding any critical exposure. **This happened once:** on 2026-08-18 the default administrator account was found enabled on 2 BMCs at DC-2. The IT Manager was notified the same day, and the accounts were disabled on 2026-08-19. The finding was added to the risk register as R-026.

## 4. Results summary
| Result | Determination statements |
|---|---|
| Satisfied | 53 |
| Other than satisfied | 132 |
| **Total** | **185** |

Risk levels of the 132 other-than-satisfied statements: 1 Very High, 45 High, 58 Moderate, 28 Low.

**Fully other than satisfied** (no plan, process, or technology existed): AC-6, AC-17, IA-2, AU-2, AU-6, CM-6, CP-2, CP-4, IR-6, SC-28.

**Largely or fully satisfied:**
- PE-3 (12 of 12): physical access at both sites, inherited from the colocation providers.
- AC-2 account creation and approval (10 of 26 satisfied): the identity-provider process works; the gaps are in removal, reviews, and shared accounts.
- IA-5 key issuance and protection (5 of 10): hardware security keys are well managed; shared and default credentials are not.
- SA-10 (5 of 11): code is under version control and flaws are tracked; the gap is the review bypass.

**Most important finding:** the RMM tool (AC-17, AC-2(9)). The test sign-in succeeded from an outside network, three technician accounts are shared, and one person can push a script to every managed customer server. The test script run through the RMM tool was not detected by the SIEM (SI-04a.02[03]). This is the Very High risk R-001 and the scenario in the P08 runbook.

**New finding:** default manufacturer administrator accounts on 2 BMCs at DC-2 (IA-05e.). Not known before testing. Added as R-026 and handled under POAM-004. All 96 BMCs are to be checked by 2026-09-30.

**How risk levels were set.** Each weakness takes the P03 gap risk for its control. It is raised to the P01 risk level where the weakness is the main cause of a higher-rated risk: AC-17b. and POAM-002 are Very High because of R-001.

All 21 controls with weaknesses have POA&M items in `poam.csv`: 1 Very High (POAM-002), 19 High, and 1 Moderate (POAM-021). PE-3 has none. CA-5 is not in the FedRAMP Class C control list, but the company keeps this POA&M for its own tracking and for the bank and SOC 2 audiences.

## 5. Deliverables
- `assessment-results.csv` (185 rows)
- `poam.csv` (21 items)
- this plan and summary

The next assessment is due by 2027-08-31, or sooner as a FedRAMP independent assessment if the sponsor decision proceeds (P03 section 4.3).
