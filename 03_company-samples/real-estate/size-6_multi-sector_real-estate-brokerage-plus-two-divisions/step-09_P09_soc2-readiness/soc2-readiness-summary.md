# SOC 2 Readiness Summary: Cris Santos Company Holdings | Real Estate | Multi-Sector

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. |
| Tier / Vertical | Multi-Sector / Real Estate and Rental and Leasing |
| Criteria | AICPA 2017 Trust Services Criteria (With Revised Points of Focus, 2022). Criterion IDs and short topic labels only; the criteria text is not reproduced |
| Scoping | Per division (section 1). One readiness report: Cris Santos Title, LLC closing and escrow disbursement services (`soc2-readiness.csv`). One vendor report review covering the key SaaS and hosted providers of every division (`vendor-soc2-review.csv`) |
| Prepared | 2026-09-17 by the Group Chief Risk Officer's assurance team with the President, Title and the Title compliance officer |

## 1. Scoping decisions per division
A SOC 2 report covers controls at a **service organization** for the **user entities** that rely on its service. The question for each division is whether it provides a service that other organizations build their own controls on.

| Division | Service line | Service organization? | Decision | Categories | Report |
|---|---|---|---|---|---|
| Mortgage and Title (Title) | Closing, settlement, and escrow disbursement services for lenders, outside brokerages, and outside homebuilders (about 27% of Title's closings are for outside clients) | **Yes.** Lenders rely on Title to disburse their loan funds only as their closing instructions allow; outside builders rely on it to receive and disburse sale proceeds | **In scope.** First readiness assessment | Security, Availability, Confidentiality, Processing Integrity | Type 1 as of 2027-03-31, then Type 2 for 2027-04-01 to 2027-09-30 |
| Mortgage and Title (Home Loans) | Mortgage lending to consumers | **No.** Borrowers are consumers, not user entities. Investors that buy loans rely on loan-level representations and their own due diligence, not on Home Loans' system controls | **Out of scope** | n/a | n/a |
| Residential Brokerage | Brokerage, property management, relocation | **No for brokerage and relocation** (clients are consumers and relocation companies buying a brokerage service, not outsourcing a control). **Not yet for property management:** owners rely on rent collection and payouts, but they are mostly individuals; a few institutional owners have asked for a SOC 1, which would fit better (financial reporting) | **Out of scope**; revisit property management if institutional owners exceed 20% of managed homes | n/a | n/a |
| Homebuilding | Building and selling homes | **No.** Buyers buy a product, and trade partners are suppliers, not user entities | **Out of scope** | n/a | n/a |
| Corporate shared services | IT, security, and treasury for the subsidiaries | Internal provider, not a service organization for outside user entities | **Carved in** to Title's description as internal shared services | n/a | n/a |

**Why Processing Integrity is in scope for Title.** Title's core promise to a lender is that funds are disbursed completely, accurately, and only as instructed. That is a processing commitment, and it is also where the group's top risk lives (P01 GR-01, MT-001). **Privacy** is out of scope because Title makes no privacy commitments to user entities; consumer privacy is handled under GLBA privacy notices and state law.

**SOC 1 considered.** Lenders and outside builders mainly ask about security and disbursement integrity, not about their own financial reporting. Title will revisit a SOC 1 if a lender requires one for its financial statement audit.

**Other assurance options.** The vertical overlay names no other standard assurance mechanism. Title insurance underwriters review Title as their agent under the agency agreements; that review is not shared with lenders and does not replace a SOC 2 report.

**Out-of-scope divisions still benefit.** The vendor review in section 4 covers every division's key providers, and the group common controls that Title carves in are the same ones the other divisions inherit.

## 2. System description (scope) for Title
- **Services:** settlement statements, receipt of buyer and lender funds, disbursement of seller proceeds, payoffs, and fees from title escrow trust accounts at 4 banks; about 128,000 closings and 640,000 disbursement wires a year.
- **Infrastructure and software:** SYS-M2 title production and escrow accounting (vendor-hosted); the TMCC (SYS-B2 Closing Communications Portal and the integration service, run by the brokerage for Title); SYS-G5 payee verification and wire release; SYS-G1 identity; SYS-G2 SOC.
- **Subservice organizations (carve-out):** the title production vendor; cloud providers A and B; the identity verification service; the bank connectivity vendor.
- **Internal shared services (carved in):** corporate identity, SOC, cloud platform, and treasury hub; the brokerage's TMCC team for the portal.
- **People:** about 2,300 Title closers, processors, and disbursement staff, plus group and TMCC teams.
- **Data:** Title customer information on about 2.4 million consumers; lenders' borrower data in closing packages.
- **Complementary user entity controls:** lenders send closing instructions and funding wires only through their secure channels and confirm payoff figures through their portals; outside brokerages direct their clients to the portal for instructions.

## 3. Readiness results (`soc2-readiness.csv`)
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33 criteria) | 28 | 4 | 1 | 0 |
| Availability (A1, 3) | 2 | 1 | 0 | 0 |
| Confidentiality (C1, 2) | 1 | 0 | 1 | 0 |
| Processing Integrity (PI1, 5) | 3 | 2 | 0 | 0 |
| Privacy (P1-P8, 18) | | | | 18 |

**Why so many criteria are Ready for a first report:** the control environment, risk assessment, monitoring, identity, network, and SOC criteria are met by group common controls that P07 already tested, and Title's own wire controls (portal-only instructions, callback, dual approval, hardware-key release) are the strongest in the group.

**Not ready:**
- **CC2.3** (communication with external parties): there is no system description and no written service commitments to lenders and outside builders.
- **C1.2** (disposal of confidential information): scanned closing files from 2006 to 2015 are kept on a file server with no disposal schedule (POAM-010).

**Partially ready:** CC6.7 (nightly copy of Title customer information to the Group Data Platform, POAM-006), CC7.2 (SYS-M2 audit logs not in the SIEM, POAM-004), CC7.4 (notification matrix not exercised; no client notice commitments, POAM-007), CC9.2 (title production vendor access and RTO, POAM-017 and POAM-011), A1.3 (vendor DR never witnessed), PI1.1 (processing commitments not written), and PI1.3 (one payoff in 60 paid without portal verification, POAM-003).

## 4. Vendor SOC report reviews, all divisions (`vendor-soc2-review.csv`)
The group reviewed the assurance reports of 14 key providers across the three divisions and corporate. 12 provided SOC reports. Two did not:
- **Tenant screening provider** (Residential Brokerage): questionnaire only; model and data-source documentation not provided. Result: conditional, tied to the P10 decision on AI-001.
- **Smart-home platform vendor** (Homebuilding): never reviewed. This is the clearest example of scenario gap 5: Homebuilding vendors sit outside the group's vendor program.

The most useful part of each review was mapping the vendor's **complementary user entity controls** to the group's own controls. Several CUECs are exactly the group's open findings: MFA for every SYS-B1 and SYS-G4 user (POAM-001), timely removal of agents (POAM-002), and review of SYS-B1 audit logs (POAM-004). A vendor's clean opinion does not help if the group does not operate the controls the vendor assumes it does.

## 5. Remediation plan and evidence calendar
| Quarter | Scope | Criteria | Evidence to collect |
|---|---|---|---|
| 2026 Q4 | Title | CC6.7, CC7.2, CC7.4 | Feed paused and approved flows; SYS-M2 logs in the SIEM; tabletop report and client notice terms |
| 2027 Q1 | Title | CC2.3, PI1.1, PI1.3, C1.2, A1.3 | System description with service and processing commitments; payoff portal verification and the first quarterly callback audit; disposal records; witnessed vendor DR test. **Type 1 as of 2027-03-31** |
| 2027 Q2 | Title | CC9.2 | Vendor PAM access; amended vendor contract |
| 2027 Q2 to Q3 | Title | All in-scope criteria | Operating evidence for the first Type 2 period (2027-04-01 to 2027-09-30) |
| 2026 Q4 to 2027 Q1 | Vendors | Tenant screening and smart-home vendors | SOC reports or equivalent; contract notice terms |

**Communication:** the President, Title sends lenders and outside builders a readiness letter with the 2027 timeline and the interim security summary, and briefs the title insurance underwriters.
