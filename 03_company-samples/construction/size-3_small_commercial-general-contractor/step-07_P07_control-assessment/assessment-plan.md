# Security Assessment Plan and Summary: Cris Santos Company | Construction | Small

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (commercial and institutional building general contractor) |
| System assessed | Project Delivery and Payment Platform (PDPP), per the SSP (P02) |
| Tier / Vertical | Small / Construction |
| Procedures | NIST SP 800-53A Rev. 5, Release 5.2.0 (determination statements from NIST OSCAL content) |
| Assessor(s) and independence | Contracted independent assessor, not involved in operating or designing the controls. Escorted by the IT Manager |
| Assessment window | 2026-08-03 to 2026-08-07 (main office, yard, and 2 jobsites walked on 2026-08-05) |
| Relationship to CMMC | A readiness check only. The CMMC Level 1 self-assessment itself must use the NIST SP 800-171A (June 2018) objectives (32 CFR 170.15(c)(1)) and is scheduled for December 2026. The controls below were chosen so each of the 15 FAR 52.204-21 requirements is tested through at least one mapped SP 800-53 control |

## 1. Scope and controls selected
Small tier scope: 15-25 controls. **23 controls, 153 determination statements.** Controls were chosen for one of three reasons:
- they map to a FAR 52.204-21 requirement (P03, through the SP 800-171 Rev. 3 tailoring tables);
- they support the Very High and High risks in P01 (business email compromise, payment fraud, backups);
- they test the Section 889 duties.

| Control | Why selected | Depth | Coverage |
|---|---|---|---|
| AC-2, AC-3, IA-2, IA-5 | FAR (b)(1)(i), (ii), (v), (vi); P01 R-002, R-015, R-016, R-017 | Focused | Focused |
| IA-2(1), IA-2(2) | Business email compromise (P01 R-001, Very High) | Focused | Focused |
| AC-20, AC-22 | FAR (b)(1)(iii), (iv); FCI outside the boundary | Basic | Focused |
| MP-6 | FAR (b)(1)(vii) | Basic | Basic |
| PE-3, PE-8 | FAR (b)(1)(viii), (ix) | Basic | Focused (main office, yard, 2 jobsites) |
| SC-7 | FAR (b)(1)(x), (xi) | Focused | Focused |
| SI-2, SI-3 | FAR (b)(1)(xii)-(xv) | Focused | Focused |
| AU-6, SI-4 | Detection of mailbox compromise (P01 R-001) | Basic | Basic |
| AT-2 | Payment-fraud awareness (P01 R-001, R-002) | Basic | Focused |
| IR-4, IR-6 | No incident capability; Section 889 and state breach clocks | Focused | Basic |
| SA-9 | External service providers (P01 R-011, R-028) | Basic | Focused |
| SR-5 | Section 889 (FAR 52.204-25(b)(1)) | Focused | Focused (5 federal projects) |
| CP-9 | Backups (P01 R-006, High) | Focused | Focused |
| CM-8 | CMMC scope and Section 889 inventory | Basic | Focused |

## 2. Methods and objects
- **Examine:**
  - identity provider and SYS-01 user exports
  - the ERP role report and the bank portal user list
  - file-share permission exports and cloud network rules
  - antivirus and patch reports, backup reports
  - vendor contracts and SOC 2 reports
  - federal submittal logs and product data
  - the subcontract template, the training roster, and walkthrough notes
- **Interview:** CFO, IT Manager, Accounting Manager, AP clerk, Contracts Administrator, Systems Integration Manager, MSP lead technician, VP Operations, 2 superintendents, and 6 randomly selected staff (reporting and payment-fraud awareness).
- **Test:**
  - sign-in tests with a named user, a trailer account, and an administrator security key
  - a relayed push-approval test against a test tenant (not production)
  - access test of the Client Systems folder with a standard account
  - EICAR test files for antivirus detection and alert routing
  - an external scan of the file-transfer portal
  - default-credential checks on commissioning laptops and jobsite routers
  - a single-file backup restore
  - a Section 889 check of 5 closed or active federal submittals against the covered entities in FAR 52.204-25

## 3. Rules of engagement
- No testing against production identities beyond sign-in tests. The phishing relay test used a separate test tenant with a test account.
- No FCI or payroll data was copied off-site. Screenshots were redacted.
- The assessor had to stop and notify the IT Manager and CFO on any critical exposure. One stop-and-notify event occurred (see section 4).

## 4. Results summary
| Result | Determination statements |
|---|---|
| Satisfied | 54 |
| Other than satisfied | 99 |

**Fully other than satisfied:** AC-3, AC-20, IA-2(2), MP-6, PE-8, AU-6, SR-5. No process or technology existed for these.
**Largely satisfied:**
- IA-2(1): security keys for administrators
- SI-3: detection and quarantine work; only after-hours alerting failed
- CP-9: the backups exist and restore; only isolation and immutability fail

**Stop-and-notify event (new finding), 2026-08-05.** The SR-5 test of 5 federal submittals found that the FC-1 VA clinic video surveillance system (2 network video recorders, 14 cameras) uses private-label products made by a covered manufacturer under FAR 52.204-25. The equipment secures a Government facility, so it falls inside the clause's covered purposes. The assessor notified the CFO the same day.
- The Contracts Administrator reported to the FC-1 Contracting Officer on **2026-08-06**, within one business day (FAR 52.204-25(d)(2)(i)).
- The follow-up with mitigation details was filed on **2026-08-19**, within 10 business days (FAR 52.204-25(d)(2)(ii)).
- The finding raised P01 R-009 and became POAM-009 and P03 G-027.
- FC-2 submittals were rescreened on 2026-08-10 and none was found.

**Other test results worth noting:**
- A test adversary-in-the-middle page relayed a push MFA approval in the test tenant. This confirms that push MFA does not stop the business email compromise technique in P08 (POAM-002).
- A standard project engineer account could open the client credential spreadsheets (POAM-007).
- The EICAR alert raised at 19:40 was not actioned until 08:10 the next morning (POAM-022).

All 22 controls with weaknesses have POA&M items in `poam.csv`. The High items are POAM-002, POAM-007, and POAM-017. **The POA&M is an internal work plan.** CMMC Level 1 permits no POA&Ms (32 CFR 170.21(a)(1)), so every item mapped to a FAR requirement must be closed before the President affirms.

## 5. Deliverables
`assessment-results.csv` (153 rows), `poam.csv` (22 items), this plan and summary. The CFO accepted the results on 2026-08-31.
