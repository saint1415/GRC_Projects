# Security Assessment Plan and Results Memo: Cris Santos Company | Arts, Entertainment, and Recreation | Sole Proprietorship

| Field | Value |
|---|---|
| Organization | Cris Santos Company (independent event promoter with one leased room) |
| System assessed | Ticketing and Venue Operations Platform (TVOP), per the system profile (P02) |
| Tier / Vertical | Sole Proprietorship / Arts, Entertainment, and Recreation |
| Procedures | NIST SP 800-53A Rev. 5, Release 5.2.0 (determination statements from NIST OSCAL content) |
| Assessor(s) and independence | The owner (self-assessment), assisted by the on-call IT consultant under a confidentiality agreement signed 2026-07-24. **Independence is limited**: the owner designed, operates, and assessed these controls. The consultant ran the tests with the owner and read the settings on screen, but also supports the laptop and Wi-Fi |
| Assessment window | 2026-07-27 to 2026-07-31 (tests on 2026-07-29; show-night walkthrough on 2026-07-30) |
| Also supports | PCI DSS v4.0.1 evidence for the 2026 SAQ A (P03), and FTC "reasonable security" (N71-R05) |

## 1. Scope and controls selected
Sole Proprietorship scope: 6-10 controls. **9 controls, 46 determination statements.** Controls were chosen because they support the High risks in P01 (R-001, R-002, R-003), the SAQ A eligibility questions in P03, or the BIA recovery objectives in P05.

| Control | Why selected | Depth / coverage |
|---|---|---|
| IA-2(1) | MFA on the accounts that control the checkout (R-001, R-002; PCI DSS 8.4) | Basic / all 5 administrator logins |
| IA-5 | Reused and shared passwords, default passwords (R-001, R-006; PCI DSS 2.2, 8.3) | Focused / SYS-01, website, door login, router |
| SI-12 | Card data in messages and patron exports (R-003, R-005; PCI DSS 3.2, 3.3) | Focused / mailbox, phone, laptop, cloud storage |
| SA-9 | Vendors and contractors (R-013; PCI DSS 12.8) | Basic / 2 PCI providers and 3 contractors |
| AU-6 | Activity review (R-001; PCI DSS 10.4) | Basic |
| IR-6 | Incident reporting and the processor's 24-hour term (R-010; PCI DSS 12.10) | Basic |
| CP-9 | Vendor backups behind the BIA's RPO of 0 (P05) | Basic / ticketing vendor |
| SC-7 | The Room's shared Wi-Fi (R-007; PCI DSS 1.3) | Basic |
| RA-3 | Risk assessment (PCI DSS 12.3) | Basic |

## 2. Methods and objects
- **Examine:** security and user settings in SYS-01, the website builder, email, the processor portal, and accounting; the router; device encryption and lock settings; the ticketing vendor's and processor's AOCs and the vendor's SOC 2 report; the merchant agreement; P01 and P05.
- **Test (2026-07-29):** sign-ins to each administrator login from a new browser; a card-number search of the mailbox, phone, laptop, and cloud storage (run 2026-07-28 and repeated on the laptop on 2026-07-29); a sharing report for cloud storage; a payout-change alert test in SYS-01; the router's administrator login and firewall settings; the website and SYS-01 user and connected-app lists.
- **Interview:** replaced by a written **self-review**, because the only person to interview is the assessor. The owner answered the SP 800-53A interview questions in writing, and the IT consultant challenged each answer against what was on screen.

## 3. Rules of engagement
- No testing during on-sales or show hours. No patron or card data copied off any system; screenshots were cropped to settings, and card numbers found in the search were counted, not copied.
- The IT consultant worked only in sessions the owner started and watched.

## 4. Results summary
| Result | Determination statements |
|---|---|
| Satisfied | 16 |
| Other than satisfied | 30 |
| **Total** | **46** |

**Fully satisfied:** CP-9 (the ticketing vendor's backups, confirmed by its SOC 2 report, support the BIA's RPO of 0).
**Fully other than satisfied:** IA-2(1), SI-12, AU-6, IR-6.
**Partly satisfied:** RA-3 (the assessment exists; no review cycle yet), IA-5 (devices protect stored credentials; everything else fails), SA-9 (responsibilities are assigned by contract; no oversight), SC-7 (inbound traffic blocked; no internal separation).

**New finding:** a former freelance assistant, engaged until 2025-11, was still listed as an administrator on the website builder (SA-09a.[03]). A website administrator can add scripts to the pages that embed the checkout, so this goes back to P01 R-002. The owner removed the account during the test on 2026-07-29. The test also showed the router still had its default administrator password (IA-05e.), changed the same day, and that SYS-01 payout-change alerts go only to the owner's email (AU-06a.), which an attacker who controls the email could hide.

The 8 controls with weaknesses each have one POA&M item in `poam.csv` (POAM-001 to POAM-007, and POAM-009 for RA-3). Three more items come from the P03 gap analysis: POAM-008 (scripts on checkout pages), POAM-010 (fee display), and POAM-011 (PCI scope and SAQ). That makes 11 items: 4 High, 5 Moderate, and 2 Low. The High items are POAM-001 (MFA) and POAM-002 (passwords), both due 2026-09-15, and POAM-003 (card data and exports) and POAM-008 (scripts), both due 2026-09-30. All four must close before the owner signs the 2026 SAQ A.

## 5. Deliverables
`assessment-results.csv` (46 rows), `poam.csv` (11 items), and this memo. Accepted by the owner on 2026-08-31. Because independence is limited, POL-01 4.5 requires an outside reviewer at least every second year.
