# Security Assessment Plan and Summary: Cris Santos Company | Retail Trade | Small

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (independent grocery retailer, one supermarket plus online ordering) |
| System assessed | E-commerce and Loyalty Platform (ELP), per the SSP (P02) |
| Tier / Vertical | Small / Retail Trade |
| Procedures | NIST SP 800-53A Rev. 5, Release 5.2.0 (determination statements from NIST OSCAL content) |
| Assessor(s) and independence | Contracted independent assessor. Not involved in operating or designing the controls, and not the company's QSA or the storefront vendor. Escorted by the IT Manager |
| Assessment window | 2026-08-10 to 2026-08-14 (browser and sign-in tests 2026-08-12; app permissions review 2026-08-13) |
| Also supports | Evidence for the 2026 SAQ A and SAQ P2PE (PCI DSS v4.0.1, N44-45-R01) and the FTC Act Section 5 reasonable-security expectation (N44-45-R02) |

## 1. Scope and controls selected
Small tier scope: 15-25 controls. **22 controls, 149 determination statements.** Controls were chosen because they support the three High risks in P01 (R-001, R-002, R-004), cover the High and Moderate PCI DSS gaps in P03 (6.4.3, 11.6.1, 8.2, 8.4, 12.8, 12.10), or support recovery of the loyalty database. The POS system and PIN pads are outside the ELP boundary and were not assessed here. Their PCI DSS status is covered by P03 and the SAQ P2PE.

| Control | Why selected | Depth | Coverage |
|---|---|---|---|
| CM-7, CM-8, SI-7, SI-4, CM-3 | Payment page scripts and change detection (P03 G-027, G-055, G-028); R-001 (High) | Focused | Comprehensive (every script on the checkout page) |
| AC-2, AC-6, AC-17, IA-2, IA-2(1), IA-5, PS-4 | Administrator access to the storefront and cloud (P03 G-033 to G-037); R-002 (High), R-009 | Focused | Comprehensive (all 9 storefront administrators, both cloud administrators) |
| SC-7 | Flat network shared with IoT devices; R-004 (High) | Focused | Focused (office network) |
| SC-8 | Emailed loyalty exports; R-003 | Basic | Focused |
| AU-6 | No log review; R-030 | Basic | Basic |
| IR-4, IR-6 | No incident response plan (P03 G-065); R-010 | Focused | Basic |
| SA-9 | Service provider management (P03 G-063); R-021, R-025 | Focused | Focused (processor, storefront vendor, contractor, pricing vendor) |
| AT-2 | Training gap (P03 G-061); R-012 | Basic | Focused |
| CP-9, CP-4 | Backup isolation and testing; R-013 | Focused | Focused |
| RA-3 | First documented risk assessment (P03 G-058) | Basic | Basic |

## 2. Methods and objects
- **Examine:** identity provider and storefront admin exports, app permissions list, cloud IAM and logging settings, backup reports, vendor contracts and AOCs, the 2025 SAQs, training roster, HR termination tickets, the P01 register.
- **Interview:** General Manager, IT Manager, Controller, E-commerce and Marketing Manager, HR and Payroll Specialist, the marketing contractor, and 8 staff selected at random (incident reporting awareness).
- **Test:**
  - browser capture of the checkout page (scripts loaded, response headers) on 2026-08-12, compared with the capture from 2026-07-28
  - sign-in tests on the storefront admin console with each account type, including the contractor's local account
  - comparison of storefront administrators with the HR roster
  - TLS scan of the loyalty API and admin consoles on 2026-08-13
  - reachability test from an administrator PC to the refrigeration controllers (read-only, with the contractor's approval)

## 3. Rules of engagement
- No testing on the live checkout flow with real cards. Script review used a browser capture only; no scripts were changed during the assessment.
- No customer data was copied off-site. Screenshots were redacted.
- Refrigeration controllers were only checked for reachability, never logged in to, and never during store hours with a delivery in progress.
- The assessor would stop and notify the IT Manager on finding an active compromise or critical exposure. None was found, but the retired app with theme write permission was reported the same day.

## 4. Results summary
| Result | Determination statements |
|---|---|
| Satisfied | 47 |
| Other than satisfied | 102 |
| **Total** | **149** |

**Fully other than satisfied:** CM-3, AU-6, AT-2, CP-4, IR-4, IR-6, AC-6, IA-2(1), SC-8. No plan, process, or technology existed for these.
**Largely satisfied:** RA-3 (all 8 statements, now that the 2026 assessment exists), SC-7 at the external boundary, and the account creation and approval parts of AC-2.

**The checkout page result drives the SAQ decision.** CM-7, SI-7, and SI-4 show that nothing today controls or watches the scripts around the processor's payment form. Until POAM-003 and POAM-004 close, the company cannot support the SAQ A eligibility statement that its site is not susceptible to script attacks (P03 section 1).

**New finding:** a retired product reviews app still had permission to change the storefront theme code (AC-06). This was not known before testing. It was added to the risk register as R-032 and to POAM-018. The app is scheduled for removal by 2026-09-30. Testing also confirmed 4 former employees with active storefront accounts (R-009, POAM-016).

**POA&M:** 21 of the 22 controls have weaknesses (all except RA-3). They are tracked in 20 POA&M items in `poam.csv`, because AC-17 and IA-2(1) share POAM-001. Five items are High: POAM-001, POAM-003, POAM-004, POAM-005, and POAM-020. The other 15 are Moderate.

## 5. Deliverables
`assessment-results.csv` (149 rows), `poam.csv` (20 items), this plan and summary. The results were accepted by the General Manager on 2026-09-04.
