# Security Assessment Plan and Results Memo: Cris Santos Company | Retail Trade | Sole Proprietorship

| Field | Value |
|---|---|
| Organization | Cris Santos Company (corner grocery with online and phone ordering) |
| System assessed | Store Sales Platform, per the system profile (P02) |
| Tier / Vertical | Sole Proprietorship / Retail Trade |
| Procedures | NIST SP 800-53A Rev. 5, Release 5.2.0 (determination statements from NIST OSCAL content) |
| Assessor(s) and independence | The owner (self-assessment), assisted by the outside IT helper. **Independence is limited**: the owner set up, runs, and assessed these controls. The IT helper ran the network tests and read the settings but also set up the router in 2022 |
| Assessment window | 2026-08-10 to 2026-08-14, after store hours (tests on 2026-08-13) |
| Also supports | Evidence for the 2026 SAQs (PCI DSS v4.0.1, N44-45-R01) and the "reasonable security" basis under FTC Act Section 5 (N44-45-R02) |

## 1. Scope and controls selected
Sole Proprietorship scope: 6-10 controls. **9 controls, 49 determination statements.** Controls were chosen because they support the High risks in P01 (R-001, R-002, R-004) or a High or Moderate PCI DSS gap in P03.

| Control | Why selected | Depth / coverage |
|---|---|---|
| IA-2(1) | MFA on the accounts that control the checkout redirect (R-001, R-004; PCI 8.4) | Basic / all 4 administrator accounts |
| IA-5 | Default, reused, and shared passwords (R-003, R-006; PCI 2.2, 8.2, 8.3) | Focused / router, terminal, Wi-Fi, store, POS |
| SC-7 | Customers on the terminal's network (R-003; PCI 1.3) | Focused / store network |
| MP-4 | Paper card data (R-002; PCI 3.3, 9.4) | Basic / pad and drawer |
| MP-6 | Disposal of customer records (R-002; Fla. Stat. 501.171(8)) | Basic |
| CM-8 | Terminal identity and inventory (R-005; PCI 9.5, 12.5) | Basic |
| SA-9 | Providers and the AI chatbot (R-008, R-014; PCI 12.8) | Focused / 6 providers |
| AU-6 | Activity review of the online store and refunds (R-001, R-006) | Basic |
| SI-3 | Malware defense on the shared laptop (R-007) | Focused / laptop |

## 2. Methods and objects
- **Examine:** account security pages, router settings, the terminal's settings menu and quick-start guide, the POS user list, the drawer and trash, the company facts system list, the merchant agreement, the processor's AOC, the website builder's SOC 2 report, and provider terms.
- **Test (2026-08-13):** sign-ins to the online store, email, merchant portal, and accounting SaaS from a new browser; the terminal manager password tried against the guide's default; a network scan from a phone joined to the customer Wi-Fi; an online open-port check; download of a standard antivirus test file on the laptop.
- **Interview:** replaced by a written **self-review**, because the only person to interview is the assessor. The owner answered the SP 800-53A interview questions in writing, and the IT helper challenged each answer against what was on screen.

## 3. Rules of engagement
- Tests only after closing. No card data was entered, copied, or photographed; screenshots were cropped to settings only.
- The network scan was limited to the store network and run from the IT helper's phone. It only listed reachable devices and open ports; it did not try to sign in to or change the terminal, which belongs to the processor.

## 4. Results summary
| Result | Determination statements |
|---|---|
| Satisfied | 17 |
| Other than satisfied | 32 |
| **Total** | **49** |

**Fully satisfied:** SI-3 (built-in antivirus detected and quarantined the test file).
**Fully other than satisfied:** IA-2(1) and AU-6.
**Partly satisfied:** IA-5, SC-7, MP-4, MP-6, CM-8, SA-9.

**New finding (closing the loop to P01):** the terminal's manager password, which allows refunds and settings changes, was still the factory default printed in the quick-start guide (IA-05e.). The owner changed it during the test on 2026-08-13. It is now part of P01 R-006 and POAM-002. The network scan also confirmed that a customer's phone on the store Wi-Fi can reach the terminal (SC-07a.[04]), which supports R-003.

The 8 controls with weaknesses each have one POA&M item in `poam.csv` (POAM-001 to POAM-008). The High items are POAM-001 (MFA, due 2026-09-15) and POAM-004 (paper card data, due 2026-09-30, with the main fix done on 2026-08-11).

## 5. Deliverables
`assessment-results.csv` (49 rows), `poam.csv` (8 items), and this memo. Accepted by the owner on 2026-09-04. Because independence is limited, POL-01 4.5 requires an outside reviewer at least every second year.
