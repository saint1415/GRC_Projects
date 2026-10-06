# Regulatory Gap Analysis: Cris Santos Company | Accommodation and Food Services | Micro

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (independent 38-unit roadside motel) |
| Tier / Vertical | Micro / Accommodation and Food Services |
| Primary standard | PCI DSS v4.0.1 (PCI Security Standards Council). A contractual standard enforced through the merchant agreement, **not law** (N72-R01) |
| Secondary regulation | FTC Act Section 5, 15 U.S.C. 45(a) and 45(n), with the FTC Rule on Unfair or Deceptive Fees, 16 CFR Part 464 (N72-R02). Short checks: FTC Disposal Rule 16 CFR 682.3 (N72-R03); Fla. Stat. 509.101(2), 501.171(2) and (8) (N72-R04) |
| Assessment dates | 2026-07-13 to 2026-07-24; evidence refreshed with P07 results through 2026-08-05 |
| Assessor | Assistant Manager (Security and Privacy Lead) with the Owner-Manager and the MSP lead technician |
| Approved | Owner-Manager, 2026-08-31 |

## 1. Applicability

### 1.1 Franchise or independent
**Decision: the motel is independent, and the company alone owns its PCI program.** It has never been franchised. A franchised property usually has to use the brand's mandated PMS and follow the brand's PCI program, so part of the control set is shared with the franchisor.

The key precedent is *FTC v. Wyndham Worldwide Corp.*, 799 F.3d 236 (3d Cir. 2015) (No. 14-3514, opinion filed 2015-08-24). The Third Circuit affirmed that the FTC can challenge unreasonable cybersecurity as an unfair practice under 15 U.S.C. 45(a), and that the company had fair notice. The FTC alleged that the franchisor, which managed its branded hotels' PMS systems, allowed card data in clear text, easy and default passwords, no firewalls between hotel systems and the internet, unrestricted vendor access, and weak detection and incident response. For an independent motel the lesson applies directly: **the FTC would measure the motel's own practices, and several match the Wyndham list today** (rows G-003, G-007, G-010, G-032, G-034, G-045).

**The franchise offer (June 2026).** If the Owner-Manager accepts the economy brand's offer in 2027, the franchise agreement must settle four things before signing: who owns and runs the PMS and network; whose PCI program and SAQ apply; who must notify whom of a suspected compromise and how fast; and who owns guest data. Under a brand-mandated system the motel still keeps its own merchant agreement duties unless the agreement says otherwise. P01 will be reassessed at that decision.

### 1.2 PCI DSS and SAQ type
**PCI DSS applies by contract** to the merchant account. PCI SSC sets no size tiers; card brands and acquirers set merchant levels and validation methods, and the level thresholds were not verified from a card brand source, so **no level number is stated here**. The acquirer's notice of 2026-05-11 (fictional) confirms that the motel validates by self-assessment questionnaire (SAQ) and asks it to confirm eligibility for the SAQ P2PE it filed for 2025.

**The SAQ type follows the payment design, not the merchant's size.** Eligibility was tested channel by channel:

| Channel | Current design | SAQ tested | Result |
|---|---|---|---|
| Front desk card-present | 2 terminals in a PCI-listed validated P2PE solution (listing confirmed 2026-07-15) | SAQ P2PE | **Eligible on its own**, if the P2PE Instruction Manual is followed |
| Phone reservations and no-shows | Clerks key card numbers into the PMS in a browser on the shared front desk PC | SAQ P2PE, SAQ C-VT | Not eligible: card data is entered on a general-purpose PC that is also used for email and browsing |
| Crew billing | Card forms by email and on paper, keyed into the PMS | SAQ P2PE | Not eligible: card data is **stored** electronically (email) and on paper |
| OTA virtual cards | Full numbers displayed in the PMS on front office PCs | SAQ A | Not eligible while motel staff display and handle card numbers |
| Booking engine | PMS vendor's hosted payment page on the vendor's own address; the motel receives a token | SAQ A | Would fit on its own |

**Result:** as designed today, the motel would have to validate on **SAQ D for Merchants**. The 2025 SAQ P2PE was the wrong questionnaire. It was signed on the gateway sales representative's advice without scoping (row G-059).

**Decision: reduce scope first, then validate.** By 2026-11-30 the motel will (a) take phone and no-show payments by the gateway's pay-by-link, or keyed on the P2PE terminal keypad where the P2PE Instruction Manual allows; (b) stop accepting card forms and bill crews by pay-by-link with card-on-file tokens held by the gateway; (c) purge stored card data from the mailbox and the binder; and (d) charge OTA virtual cards through the PMS without displaying them. The front desk PC then never handles card data. The motel will validate for 2026 on **SAQ P2PE** (terminals) plus **SAQ A** (booking engine and pay-by-link). The acquirer agreed by email on 2026-08-19 (fictional), on condition that the redesign is complete before the attestation is signed; if it is not complete by 2026-12-15, the motel validates on SAQ D. This is the single most valuable change: it takes most of the 53 PCI DSS gaps below out of card data scope rather than fixing them one by one.

**Which rows stay relevant after the redesign.** Rows marked "expected to stay relevant after the redesign" in `applies_at_this_tier` (3.1, 3.2, 3.3.1, 9.1, 9.4, 9.5, 12.1, 12.5, 12.6, 12.8, 12.10) are the author's judgment of what still matters for paper media, the terminals, policy, awareness, service providers, and incident response. They must be confirmed against the SAQ P2PE and SAQ A questionnaires themselves when they are completed. The FTC and Florida rows apply regardless of SAQ type.

**Current version.** PCI DSS v4.0.1 is the current version, and the requirements introduced as future-dated in v4.0 have been in force since 2025-03-31 (PCI SSC blog, 2024-06-11).

### 1.3 Secondary regulation and short checks
- **FTC Act Section 5** applies with no size threshold. Broken privacy or security promises can be deceptive (45(a)(1)); unreasonable security can be unfair if it causes or is likely to cause substantial injury that consumers cannot reasonably avoid and that is not outweighed by benefits (45(n)).
- **16 CFR Part 464** (90 FR 2066, rule text at 2166; published 2025-01-10; effective 2025-05-12; text checked on eCFR as of 2026-09-23) covers "short-term lodging, including temporary sleeping accommodations at a hotel, motel, inn" (464.1). A "business" includes one that offers services "in physical locations" (464.1), so the roadside rate sign counts. Any offer, display, or advertisement of a price must show the **total price**, including the mandatory $6 fee, more prominently than other pricing (464.2(a)-(b)). An audible disclosure by telephone must be easy to hear and understand (464.1, "clear and conspicuous"). Government taxes may be excluded but must be disclosed with the final amount before the guest pays (464.2(c)). Fees must not be misrepresented (464.3).
- **FTC Disposal Rule** (16 CFR 682.3): the motel obtains background-check reports on front desk applicants.
- **Fla. Stat. 509.101(2)**: each transient establishment must keep a chronological guest register with dates of occupancy and rates, available to the division for inspection, and may keep it electronically. Registers more than 2 years old need not be made available. This sets a **2-year floor** for register data, not a reason to keep everything.
- **Fla. Stat. 501.171(2) and (8)**: reasonable security for electronic personal information, and disposal of customer records when they are no longer to be retained. Personal information includes a name with a driver license, ID card, or passport number, and a name with a card number "in combination with any required security code" (501.171(1)(g)1.a.). Breach notice under 501.171(3) to (6) is handled in P08.

**Not applicable, with reasons:** CIRCIA (proposed only; the motel is far below the SBA size standard), Illinois BIPA (no Illinois operations and no biometrics), FTC Safeguards and Red Flags Rules (no consumer credit), CCPA (no California business), the Florida Digital Bill of Rights (the $1 billion revenue test and the three further tests are not met), HIPAA, and SEC disclosure.

## 2. Method
1. **Requirements.** PCI DSS was broken down into its 12 principal requirements and their requirement groups, plus the appendices. Three items were taken to the defined-requirement level because they decide scope or carry the largest risk: 3.3.1, 6.4.3, and 11.6.1. Labels are short topics written for this analysis, not PCI SSC text, because PCI DSS is copyrighted. Read the requirement text in the official standard. Group numbers come from the company's copy of v4.0.1.
2. **FTC, Part 464, and Florida rows** cite text checked on uscode.house.gov, eCFR, the Federal Register, and the Florida Legislature's 2026 statutes.
3. **Crosswalk.** Each row maps to CSF 2.0 and SP 800-53 Rev. 5. **This is an author mapping.** No official NIST mapping from PCI DSS v4.0.1 was used.
4. **Documentary evidence.** Merchant agreement, acquirer notice, 2025 SAQ, PMS vendor and gateway AOCs, P2PE solution listing and Instruction Manual, PMS user and permission reports, suite user export, firewall and Wi-Fi configuration exports, MSP patch and antivirus reports, the website privacy statement, photos of the rate sign, a mailbox search on 2026-07-16, a network scan on 2026-07-16, three test phone calls on 2026-07-21, and a walkthrough on 2026-07-15. Interviews covered all 7 employees and the MSP lead technician.
5. **Status.** Each row was rated Met, Partially met, Not met, or Not applicable **as of the end of fieldwork**. Gaps were rated with the P01 risk scale.

## 3. Results summary
| Area | Met | Partially met | Not met | N/A | Total |
|---|---|---|---|---|---|
| PCI Req 1 Network security controls | 0 | 3 | 2 | 0 | 5 |
| PCI Req 2 Secure configurations | 0 | 1 | 2 | 0 | 3 |
| PCI Req 3 Stored account data | 0 | 0 | 5 | 2 | 7 |
| PCI Req 4 Transmission | 0 | 1 | 1 | 0 | 2 |
| PCI Req 5 Malware and phishing | 0 | 3 | 1 | 0 | 4 |
| PCI Req 6 Secure systems and software | 0 | 2 | 2 | 2 | 6 |
| PCI Req 7 Restrict access | 1 | 1 | 1 | 0 | 3 |
| PCI Req 8 Identify and authenticate | 1 | 2 | 3 | 0 | 6 |
| PCI Req 9 Physical access and devices | 1 | 1 | 3 | 0 | 5 |
| PCI Req 10 Logging | 0 | 2 | 5 | 0 | 7 |
| PCI Req 11 Security testing | 0 | 0 | 5 | 1 | 6 |
| PCI Req 12 Policies and programs | 1 | 4 | 3 | 2 | 10 |
| PCI Appendices A1-A3 | 0 | 0 | 0 | 3 | 3 |
| **PCI DSS subtotal** | **4** | **20** | **33** | **10** | **67** |
| FTC Act Section 5 | 0 | 1 | 1 | 0 | 2 |
| 16 CFR Part 464 (fees) | 2 | 1 | 1 | 0 | 4 |
| FTC Disposal Rule | 0 | 1 | 0 | 0 | 1 |
| Florida Statutes (509.101, 501.171) | 1 | 1 | 1 | 0 | 3 |
| **Total (77)** | **7** | **24** | **36** | **10** | **77** |

Of the 60 rows with gaps, 10 are rated High, 27 Moderate, and 23 Low.

**What the numbers say.** Most "Not met" rows are missing written procedures, logging, and testing that a 7-person motel has never had a reason to build. Those are exactly the rows the redesign takes out of card data scope. The rows that matter whatever happens are the stored card data (3.2, 3.3.1, 9.4), vendor remote access and shared logins (8.2, 8.4), and the incident response plan (12.10).

## 4. Priority gaps
| Gap | Row | Risk | Action | Owner | Target |
|---|---|---|---|---|---|
| Security codes kept on card forms | G-011 (3.3.1) | High | Delete and shred now; never collect the code | Assistant Manager | 2026-09-30 |
| Card forms in email and an unlocked binder | G-010 (3.2), G-040 (9.4) | High | Purge; pay-by-link replaces forms; lock and retire the binder | Assistant Manager | 2026-11-30 |
| Shared logins, stale accounts, standing vendor access | G-032 (8.2) | High | Named accounts; same-day removal; lock vendor access per session | Assistant Manager | 2026-10-31 |
| No MFA for front office users or vendor remote access | G-034 (8.4) | High | MFA for every PMS user and mailbox; one-time codes for remote tools | Assistant Manager | 2026-10-31 |
| No incident response plan | G-064 (12.10) | High | POL-03 and P08; reporting card; tabletop | Assistant Manager | 2026-11-30 |
| Flat office network | G-003 (1.3) | High | Separate networks for terminals, lock system and CCTV, and office PCs | Assistant Manager | 2026-12-31 |
| Wrong SAQ; no scope document | G-059 (12.5) | High | Scope document; redesign; SAQ P2PE plus SAQ A | Owner-Manager | 2026-12-31 |
| Security not yet reasonable (FTC; Florida) | G-068, G-076 | High | Execute the P01 and P07 plans | Owner-Manager | 2026-12-31 |
| Excess card-display rights | G-012 (3.4), G-029 (7.2) | Moderate | Remove from all but the Owner-Manager; charge without display | Assistant Manager | 2026-10-15 |
| No terminal list or inspections | G-041 (9.5) | Moderate | Device list; weekly inspection at night audit | Assistant Manager | 2026-10-31 |
| False "never stored by the motel" statement | G-069 (45(a)(1)) | Moderate | Rewrite the privacy statement | Owner-Manager | 2026-09-30 |
| Partial prices on the sign, banner, and phone | G-070, G-071 (464.2) | Moderate | Total price first everywhere | Owner-Manager; Assistant Manager | 2026-09-30 |
| No retention schedule | G-077 (501.171(8)) | Moderate | Register 2 years; ID scans checkout plus 30 days | Assistant Manager | 2026-12-31 |

The full list, with evidence, is in `gap-analysis.csv`. High and Moderate gaps are carried into the risk register (P01) and, where the control was assessed, the POA&M (P07).

## 5. Remediation plan
The plan fits a 7-person motel: most actions are vendor settings, one-page procedures, or MSP work, not new systems. Costs are in the P01 treatment summary.

| Phase | Due | Actions | Rows closed |
|---|---|---|---|
| 1. Stop the bleeding | 2026-09-30 | Delete and shred anything with a security code; lock the binder; correct the privacy statement, rate sign, banner, and phone script; onboarding and termination checklist; policy acknowledgments | G-011, G-069, G-070, G-071, G-028, G-031, G-055, G-056, G-074 |
| 2. Access and visibility | 2026-10-31 | Named Windows accounts and mailboxes; MFA for every PMS user and mailbox; lock vendor access per session; remove card-display permission; terminal list and weekly inspections; network and data-flow diagrams; staff Wi-Fi passphrase; recorder password; first ASV and internal scans; training; weekly log review; booking link check; visitor log; card data handling rules (POL-04) | G-002, G-007, G-008, G-012, G-021, G-029, G-032, G-033, G-034, G-039, G-041, G-045, G-051, G-060, G-025, G-009, G-016 |
| 3. Redesign | 2026-11-30 | Pay-by-link for phone and crew payments; keyed entry on the P2PE keypad only where the Instruction Manual allows; purge stored card data; virtual cards charged without display; provider list and responsibility matrix; incident response tabletop; procedures for networks, configuration, anti-malware, and changes | G-010, G-013, G-017, G-040, G-001, G-006, G-018, G-027, G-062, G-064 |
| 4. Defense in depth | 2026-12-31 | Separate networks; outbound rules; EDR with after-hours alerting; log retention; firmware schedule; retention schedule and PMS purge settings; targeted risk analyses; scope document | G-003, G-004, G-005, G-019, G-020, G-024, G-043, G-044, G-046, G-047, G-048, G-053, G-036, G-037, G-042, G-049, G-050, G-022, G-057, G-059, G-077, G-068, G-076 |
| 5. Validate | 2026-12-31 | SAQ P2PE plus SAQ A signed after the redesign (SAQ D if the redesign slips past 2026-12-15) | G-059 |

**Penetration testing (G-052)** is not planned, because the redesign removes the office network from card data scope; if the motel ends up on SAQ D, a penetration test after segmentation is due by 2027-03-31.

**Before signing the 2026 SAQs:** confirm each "expected to stay relevant" row against the SAQ P2PE and SAQ A questionnaires, confirm with the acquirer that the redesign is complete, and attest only to what has evidence. The 2025 attestation of "In Place" without evidence is the mistake not to repeat.

**Progress check.** The Assistant Manager reports progress to the Owner-Manager at a monthly 30-minute meeting, using the P07 POA&M as the tracker.

## 6. Pending changes and watch items
- **PCI DSS.** v4.0.1 remains current; the analysis will be updated if a later version is published.
- **FTC fee rules.** A proposed FTC rulemaking on fees for food and grocery ordered through online delivery platforms (91 FR 20381, 2026-04-16) is not final and does not affect lodging.
- **CIRCIA** final rule not published as of 2026-09-25.
- None of these is treated as a current obligation.
