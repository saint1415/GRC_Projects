# Security Assessment Plan and Results Memo: Cris Santos Company | Wholesale Trade | Sole Proprietorship

| Field | Value |
|---|---|
| Organization | Cris Santos Company (IT hardware reseller) |
| System assessed | Reseller Order Desk (ROD), per the system profile (P02) |
| Tier / Vertical | Sole Proprietorship / Wholesale Trade |
| Procedures | NIST SP 800-53A Rev. 5, Release 5.2.0 (determination statements from NIST OSCAL content) |
| Assessor(s) and independence | The owner (self-assessment), assisted by the on-call IT consultant under a confidentiality agreement signed 2026-07-30. **Independence is limited**: the owner designed, operates, and assessed these controls. The consultant ran the tests with the owner and challenged each answer, but also supports the laptop and router |
| Assessment window | 2026-08-03 to 2026-08-07 (tests on 2026-08-06) |
| Relationship to CMMC | This is not the CMMC Level 1 self-assessment, which uses the NIST SP 800-171A objectives (32 CFR 170.15(c)(1)(i)) and is due 2026-10-23. It tests the controls behind the weakest FAR 52.204-21 requirements and the top supply chain risk, so the owner knows what to fix first |

## 1. Scope and controls selected
Sole Proprietorship scope: 6-10 controls. **10 controls, 52 determination statements.** Controls were chosen because they carry a FAR 52.204-21 requirement that P03 found unmet, or support a High risk in P01 (R-001, R-002, R-004).

| Control | Why selected | Depth / coverage |
|---|---|---|
| IA-2, IA-2(1), IA-2(2) | Authentication (52.204-21(b)(1)(v)-(vi)); account takeover (R-003, R-005) | Basic / every account in SYS-01, SYS-02, SYS-03 |
| AC-20 | FCI in outside systems (52.204-21(b)(1)(iii); R-006, R-007) | Focused / AI assistant and file links |
| MP-6 | Sanitization (52.204-21(b)(1)(vii); R-012) | Basic / old devices and returned stock |
| PE-3 | Physical access (52.204-21(b)(1)(viii)-(ix); R-013) | Basic / garage and cabinet |
| SC-7 | Boundary protection (52.204-21(b)(1)(x); R-008) | Focused / home router |
| SI-2 | Flaw remediation (52.204-21(b)(1)(xii)) | Basic / laptop, phone, router, staged firmware |
| SI-3 | Malicious code (52.204-21(b)(1)(xiii)-(xv)) | Focused / laptop |
| SR-11 | Component authenticity (R-001; Section 889 and counterfeit exposure) | Focused / 12 serials from 2026 non-authorized purchases |

## 2. Methods and objects
- **Examine:** account lists and security settings, the file sharing report, the AI assistant's history and data settings, router pages, update history, the carrier trade-in receipt, purchase history, and P01, P03, and P05.
- **Test (2026-08-06):** sign-ins to SYS-01, email, and both distributor portals from a new browser; a standard antivirus test file; router remote management and open ports checked from the phone hotspot; console check of 2 trade-in switches; serial lookups of 12 items in the OEM partner portals; a test that the cabinet was locked.
- **Interview:** replaced by a written **self-review**, because the only person to interview is the assessor. The owner answered the SP 800-53A interview questions in writing, and the IT consultant challenged each answer against what was on screen.

## 3. Rules of engagement
- Tests ran outside business hours. No customer data or FCI was copied; screenshots were cropped to settings only.
- The IT consultant worked only in sessions the owner started and watched.
- If a test found a live exposure, the owner could fix it at once and record both the finding and the fix.

## 4. Results summary
| Result | Determination statements |
|---|---|
| Satisfied | 21 |
| Other than satisfied | 31 |
| **Total** | **52** |

**Fully satisfied:** IA-2 (unique accounts) and SI-3 (the built-in antivirus detected and quarantined the test file).
**Fully other than satisfied:** IA-2(1), IA-2(2), AC-20, MP-6, SR-11.
**Partly satisfied:** PE-3 (the cabinet is locked and visitors are accompanied; keys, codes, and logs are not controlled), SC-7 (one managed connection; no internal boundary), SI-2 (laptop and phone current, staged firmware tested; router not).

**New finding (back to P01 as R-008):** the router's remote management was reachable from the internet with the default admin password (SC-07a.[02]). The owner changed the password and turned remote management off during the test on 2026-08-06. POAM-006 tracks the separate business network.

**Supply chain finding (P01 R-001; P08 worked example):** 2 of 12 serials checked (optical transceivers from one marketplace seller, bought 2026-06-10) returned "not found" in the OEM portal (SR-11a.[03]). The owner moved both to quarantine the same day. The OEM later confirmed them as cloned. 6 units from the same lot had been sold to 2 commercial customers; none went on a DoD order.

The 8 controls with weaknesses each have one POA&M item in `poam.csv` (POAM-001 to POAM-008). The High items are POAM-001 (MFA on the order management system) and POAM-008 (component authenticity). Every item is due by 2026-10-15 so that all 15 FAR 52.204-21 requirements can be MET at the final self-assessment.

## 5. Deliverables
`assessment-results.csv` (52 rows), `poam.csv` (8 items), and this memo. Accepted by the owner on 2026-08-31. Because independence is limited, POL-01 4.5 has the IT consultant check the evidence at every annual self-assessment.
