# Scenario facts: Cris Santos Company | Finance and Insurance | Micro

All 11 deliverables in this folder use the facts below. The company is fictitious. This scenario is independent of the other sizes. Where a fact comes from a regulation, the citation is given; regulation text was read from eCFR (current through 2026-09-23).

## 1. The organization
| Item | Fact |
|---|---|
| Legal name | Cris Santos Community Federal Credit Union (member-owned federal credit union; the README tier defaults "Cris Santos Company, LLC" and "privately held" do not fit a credit union and are replaced here) |
| Business | Community credit union (NAICS 522130): share savings, share draft (checking), and certificate accounts; consumer auto, personal, and share-secured loans; a small book of first mortgages held in portfolio; online and mobile banking; debit cards; outgoing wires for members |
| Charter and supervision | **Federal charter.** Chartered under the Federal Credit Union Act. The National Credit Union Administration (NCUA) is the chartering agency, the supervisor, and the insurer of member shares (National Credit Union Share Insurance Fund). There is no state supervisory authority. Why federal: one agency and one set of CFR rules for charter, safety and soundness, and security; the federal-only rules on disposal (12 CFR 748.0(c) and 717.83) and identity theft red flags (12 CFR 717.90) apply without a state overlay |
| Field of membership | Community charter: people who live, work, worship, or attend school in one Florida county |
| Legal form | Federal credit union chartered under the Federal Credit Union Act; a not-for-profit cooperative |
| Ownership | Owned by its members (one member, one vote). A volunteer board of directors (7 members elected by the membership) governs it. A volunteer supervisory committee (3 members appointed by the board) obtains the annual audit (12 CFR Part 715). There are no shareholders |
| Location | Florida. One office: main office with lobby, one drive-up lane, and one lobby ATM |
| Workforce | 7 employees: President and CEO, Operations Manager, Lending Manager, Accounting and Compliance Officer, Senior Member Service Representative, and 2 Member Service Representatives |
| Size | $60.0 million in total assets (fictional). Under the SBA size standard of $850 million in total assets for NAICS 522130, so SBA-small |
| Receipts | About $1.1 million a year in net revenue (fictional; income after dividends paid to members), about $4,400 per business day. Used to scale BIA impact values (P05) |
| Members | About 6,400 members. About 3,900 are enrolled in online and mobile banking; about 5,200 debit cards are active |
| Payments volume | About 25 outgoing wires a month, mostly members' home and vehicle purchases (average about $38,000; largest in 2025 was $310,000). Consumer ACH (payroll and benefit deposits, bill payments) is processed through the core. No business ACH origination |
| Lending | $41 million loan portfolio. About 900 consumer loan applications a year |
| Primary regulation | NCUA security program rule and guidelines: 12 CFR 748.0 (written security program), Appendix A to Part 748 (Guidelines for Safeguarding Member Information), and Appendix B to Part 748 (response programs and member notice). They implement GLBA section 501(b) (N52-R01). Secondary: cyber incident notification to NCUA within 72 hours, 12 CFR 748.1(c) (C-FINANCIAL-R03). Applicability is determined in the intake [obligations register](step-00_P00_intake/obligations-register.csv) (N52-R01, N52-R09, C-FINANCIAL-R03): a federally insured federal credit union (EV-020) |
| Not in scope | Decided in the intake [obligations register](step-00_P00_intake/obligations-register.csv). **OCC, Federal Reserve, and FDIC rules (the Small sample's primary and secondary regulation):** the Interagency Guidelines at 12 CFR 30 App. B, 208 App. D-2, 225 App. F, and 364 App. B (N52-R02), and the 36-hour Computer-Security Incident Notification Rule (12 CFR Part 53, 225 Subpart N, 304 Subpart C), apply to banks and bank holding companies, not to credit unions. **FTC Safeguards Rule (N52-R03):** covers financial institutions under FTC jurisdiction, which include non-federally insured credit unions; this credit union is federally insured and supervised by NCUA. **NYDFS Part 500 (N52-R04):** not New York-chartered or licensed. **SEC Regulation S-P, S-ID, and cybersecurity disclosure (N52-R05, N52-R06, N52-R08):** no broker-dealer or adviser; not an SEC registrant. **NAIC Model #668 (N52-R07):** the credit union holds no insurance license. **Payment cards:** debit cards are issued and processed by a card processor; PCI DSS obligations are noted, not assessed |
| State law approach | Florida law is cited only where a Florida duty is unavoidable: breach notification (Fla. Stat. 501.171) and funds-transfer liability under UCC Article 4A as enacted in Fla. Stat. ch. 670 |

## 2. People (role titles only)
| Role | Security and compliance duties |
|---|---|
| Board of Directors (7 volunteers) | Approves the written information security program (App. A III.A) and the Identity Theft Prevention Program (717.90(e)); receives the annual information security report (App. A III.F); reviews fidelity bond coverage each year (713.2); is told of every SAR filed (748.1(d)(4)); accepts High risks |
| Supervisory Committee (3 volunteers) | Obtains the annual supervisory committee audit (Part 715); engages and receives the independent control assessment (P07) |
| President and CEO | Managing official. Files the annual Part 748 compliance certification in the Credit Union Profile (748.1(a)); accepts Moderate risks; decides on NCUA notices; approves the deliverables |
| Operations Manager | **Information Security Officer (ISO) and Privacy Officer**, designated in writing by the board on 2026-08-25. Also the vendor manager, the MSP contact, and the primary wire approver |
| Accounting and Compliance Officer | **BSA Officer** (748.2(c)(3)); files SARs; Regulation B and privacy notice compliance; general ledger; backup wire approver |
| Lending Manager | Owner of the loan origination system; business owner of the AI credit scoring model (P10) |
| Senior Member Service Representative | Takes and keys wire requests (maker); works the shared Member Services mailbox; ATM balancing |
| Member Service Representatives (2) | Teller and member service; work the shared Member Services mailbox |
| Managed service provider (MSP) | IT support: endpoints, patching, antivirus, firewall and Wi-Fi, productivity suite administration, and the document imaging server in the cloud tenant |
| Outside CPA firm | Supervisory committee audit (financial statement audit) |

**Role overlap.** The Operations Manager is the ISO and also approves wires and manages vendors, so the ISO oversees controls they operate. This is compensated by the Supervisory Committee engaging an independent assessor (App. A III.C.3 asks that tests be conducted or reviewed by independent parties) and by the board receiving the annual report directly.

## 3. Systems

The full inventory, with the evidence behind each entry, is in [`step-00_P00_intake/asset-inventory.csv`](step-00_P00_intake/asset-inventory.csv).

| ID | System | Hosting | Holds member information? | Notes |
|---|---|---|---|---|
| SYS-01 | Core processing system (member accounts, shares, loans, general ledger, teller, ACH, BSA monitoring module) | Hosted by a core processor (service provider) | Yes | System of record. Reached over the internet with TLS from the office's fixed IP address only; teller logins use passwords (the core offers no MFA for teller users). SOC 1 Type 2 and SOC 2 Type 2 reports received each year (EV-002; EV-029) |
| SYS-02 | Online and mobile banking (bill pay, transfers, e-statements) | Vendor-hosted by a digital banking provider, integrated with SYS-01 | Yes | Member MFA is a text code at new-device registration only. Staff admin console uses MFA (EV-004) |
| SYS-03 | Wire transfer portal | Web service of the credit union's corporate credit union | Yes | Maker-checker dual control with hardware tokens for every outgoing wire (EV-005) |
| SYS-04 | Productivity suite (email, files) | SaaS | Yes | MFA on named accounts. The shared **Member Services mailbox** signed in with a password only at intake (EV-006) |
| SYS-05 | 8 desktops, 3 laptops, 2 check scanners | MSP-managed | Yes (cached) | Laptops encrypted; desktops not (EV-008; EV-009) |
| SYS-06 | Office network: firewall, staff Wi-Fi, guest Wi-Fi, VoIP phones | On-premises, MSP-managed | In transit | One internet line; guest Wi-Fi separated (EV-012; EV-035) |
| SYS-07 | Debit card processing and the lobby ATM | Card processor; ATM serviced by an ATM vendor | Yes | Outside the SSP boundary (EV-031) |
| SYS-08 | Consumer loan origination system (LOS) with the vendor's AI credit scoring add-on | Vendor SaaS | Yes | AI add-on in pilot since 2026-04-06 (P10; EV-034) |
| SYS-09 | Document imaging server (signature cards, ID copies, loan files) | One virtual server in a public cloud IaaS tenant, operated by the MSP | Yes | Daily snapshots in the same cloud account; never restore-tested (EV-013; EV-014) |

**SSP system (P02):** the *Core and Digital Banking Platform (CDBP)*: the credit union's configuration, users, and administration of SYS-01, SYS-02, and SYS-03, plus SYS-04 and SYS-09 where member information is exchanged and stored, and the endpoints (SYS-05) and office network (SYS-06) used to reach them.

## 4. Where the evidence is

This file says who the credit union is. It does not say how well its security works. That is established from evidence:
- **What the records show** is in the [intake report](step-00_P00_intake/intake-report.md) and the [evidence register](step-00_P00_intake/evidence-register.csv). For a 7-person credit union the systems of record are the core processor's user administration and reports, the online banking admin console, the wire portal, the productivity suite and MSP consoles, the MSP's reports and tickets, the payroll service, the board minutes and policy binder, the contracts and SOC report folder, and NCUA filing records. Every item has a source system, an owner, and as-of and collected dates.
- **Which rules apply** is in the [obligations register](step-00_P00_intake/obligations-register.csv).
- **Gaps against NCUA Part 748 and its appendices** are judged in the gap analysis (P03), and **whether controls work** is tested in the control assessment (P07). Both cite evidence IDs.

## 5. Scenario choices
| Deliverable | Choice |
|---|---|
| P08 incident | Business email compromise and fraudulent wire transfer: a phished password opens the shared Member Services mailbox; the attacker uses a member's home-purchase email thread to send changed wire instructions from a look-alike address, and a wire is sent without a callback. The MSP, the cyber insurer, and the fidelity bond carrier are in the notification chain |
| P09 SOC 2 | Security plus Confidentiality. The credit union is not a service organization. The readiness self-assessment is used to answer the cyber insurer's renewal questionnaire and to structure the annual board report; also a review of the core processor's SOC reports |
| P10 AI | The LOS vendor's AI credit scoring add-on for consumer auto and personal loans up to $25,000 (pilot) |
| Cloud | SaaS plus one cloud workload: the document imaging server (IaaS virtual server operated by the MSP). Vendor-agnostic |

## 6. Assessment calendar (fictional)
| Date | Event |
|---|---|
| 2026-06-29 to 2026-07-10 | Intake: evidence requests, exports from the core, the admin console, the wire portal, the suite and the MSP, the board minutes and policy binder, the contracts and SOC report folder, inventories, obligations register |
| 2026-07-13 to 2026-07-24 | BIA interviews, risk assessment and gap analysis (ISO with the MSP lead technician) |
| 2026-07-27 to 2026-07-31 | Policies drafted from the gaps |
| 2026-08-04 to 2026-08-06 | Control assessment (independent IT audit consultant engaged by the Supervisory Committee): operating tests of controls already in place; design review of the draft policies |
| 2026-08-18 | Core processor SOC report review |
| 2026-08-21 | AI credit scoring assessment |
| 2026-08-25 | Board meeting: approves the updated information security program and policies POL-02 to POL-04 (effective 2026-09-01), designates the ISO in writing, and receives the first annual information security report since 2022 |
| 2026-08-31 | Deliverables approved by the President and CEO |
| 2027-02 (planned) | Follow-up assessment: operating effectiveness of the controls the new policies introduced, after at least one quarter of operation |

## 7. Facts added while building the deliverables
These facts were added because the deliverables needed them. They do not change sections 1-6. Facts drawn from the credit union's records cite the evidence register ID they rest on.

| Topic | Added fact | Used in |
|---|---|---|
| Endpoints | SYS-05 is 8 desktops (4 teller and member service stations, 1 wire and new-accounts desk, 1 accounting, 1 lending, 1 operations) and 3 laptops (President and CEO, Operations Manager, Lending Manager). The 2 check scanners are attached to teller stations (EV-008; EV-052) | P01, P02, P04, P07 |
| Shared mailbox | The Member Services mailbox was created in 2018 as a licensed user account so that several people could sign in. It was left out of MFA "because several people use it." It holds about 3 years of email. Its password was not changed when an MSR left in March 2026 (EV-006; EV-007; EV-053) | P01, P03, P07, P08 |
| Former MSR | An MSR left on 2026-03-13. P07 testing on 2026-08-05 found her core account still enabled. Core sign-in logs showed no use after her last day, and the account was disabled that day (EV-001; EV-AC-2) | P01, P03, P07 |
| Offline teller mode | If the core is unreachable, the core's offline teller mode uses a balance file downloaded each night to the wire and new-accounts desk. It allows limited withdrawals (up to $500 per member per day) and deposits that post when the core returns (EV-043; EV-047) | P01, P05 |
| Core processor | Production and backup run at two data centers (SOC 2 system description). Stated recovery objectives: RTO 8 hours, RPO 15 minutes. The contract predates the NCUA cyber incident rule and renews on 2027-06-30 (EV-028; EV-029) | P05, P09 |
| Corporate credit union | Offers a phone-initiated wire with a PIN as an alternate procedure. The credit union has never tested it (EV-032; EV-025) | P05, P08 |
| Internet and phones | One business fiber line. The VoIP phones use the same line, so an outage also stops the phones used for callbacks (EV-012; EV-035) | P01, P05 |
| MSP contract | Help desk, patching, antivirus, firewall and Wi-Fi, productivity suite administration, and imaging server administration. 4-business-hour response, an after-hours emergency line, and no recovery time commitment (EV-033) | P04, P05, P07 |
| Insurance | Fidelity bond (NCUA Part 713) with notice-of-loss terms, and a cyber policy with a 24x7 breach hotline, panel breach counsel and forensics, and a $100,000 social engineering fraud sublimit (fictional). The cyber insurer's renewal questionnaire is due 2026-10-31 (EV-036) | P08, P09 |
| Office security | Keyed entry, alarm, vault, and cameras (748.0(b)(1)). Keys held by the President and CEO and the Operations Manager; locked network closet (EV-040; EV-052) | P02, P03 |
| Past events | In 2025 a member's online banking was taken over after a phone number change; the loss was refunded and handled with no written record. Two desktops were retired in 2024 with no disposal record (EV-007; EV-015) | P01, P03, P09 |
| Assessor | The P07 assessor is an independent IT audit consultant engaged by the Supervisory Committee. It took no part in the risk assessment or gap analysis and operates no control | P07 |
| LOS AI pilot | The AI credit scoring add-on was switched on 2026-04-06 for online consumer auto and personal loan applications up to $25,000. It auto-approves applications above the approve cutoff and routes the rest to the Lending Manager (EV-034) | P01, P10 |
| Mailbox conversion | On 2026-08-12, after the P07 finding, the MSP converted the Member Services mailbox to a delegated shared mailbox reached through each person's named account with MFA, and reset its password. About 3 years of member documents remain in it until they are moved (EV-058) | P01, P02, P07, P08 |
| Core roles and wire portal | All 3 MSRs hold the core supervisor override profile. The Operations Manager holds both the wire portal administrator role and an approver token. The online banking admin console has 5 staff users, all with MFA (EV-002; EV-AC-5; EV-004) | P02, P03, P07 |
| Imaging server backups | Daily snapshots kept 14 days in the same cloud account; the MSP's cloud console login is shared by two technicians and had no MFA at P07 testing (2026-08-05) (EV-013; EV-014; EV-IA-2(1)) | P04, P05, P07 |
| Wire file samples | June 2026 (P03): 10 wire files, 4 requested by email, 1 with a callback note. July 2026 (P07): 10 wire files, 6 requested by email, 1 with a callback note (EV-051; EV-057) | P03, P07 |
| Cyber policy renewal | The cyber policy renews on 2026-11-01; the renewal questionnaire is due 2026-10-31 (EV-036) | P09 |
| Other vendor reports | The digital banking provider's SOC 2 Type 2 report is on file and due for review by 2026-11-30; the LOS vendor's SOC 2 report has been requested and not received (EV-030; EV-034) | P02, P09, P10 |
| AI pilot results | From 2026-04-06 to 2026-08-14 the add-on scored 212 applications: 97 approved automatically; 115 referred (model recommended decline on 52); of the referred, 61 approved, 45 declined, and 9 withdrawn or incomplete. 9 of the 45 decline notices gave a score-only reason (EV-059) | P01, P10 |
