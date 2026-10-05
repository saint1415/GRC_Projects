# Regulatory Gap Analysis: Cris Santos Company Holdings | Communications | Multi-Sector

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. (three divisions plus corporate shared services) |
| Tier / Vertical | Multi-Sector / Communications (focus division: Telecom Carrier) |
| Primary regulation | FCC CPNI rules, 47 CFR 64.2001-64.2011 (47 U.S.C. 222), text in force on 2026-09-23 (C-COMMUNICATIONS-R01) |
| Division regulations | Carrier: CPNI plus CALEA SSI rules, outage reporting (47 CFR Part 4), and the covered equipment report (47 CFR 1.50007). Engineering: FAR 52.204-21, 52.204-25, and 52.204-23 for its federal contracts, plus customer contract commitments. Tower: antenna structure lighting rules (47 CFR 17.6, 17.47-17.49) plus landowner and tenant data duties |
| Group-wide obligations | SEC Reg S-K Item 106 and Form 8-K Item 1.05; state breach notification laws; FTC Act Section 5 for activities that are not common carriage |
| Gap tables | `gap-analysis.csv` (Carrier, 61 rows); `gap-analysis-engineering.csv` (28 rows); `gap-analysis-tower.csv` (15 rows) |
| Assessment dates | 2026-05-04 to 2026-07-31, with evidence updated from the P07 assessment (to 2026-08-28) |
| Assessors | Division security and compliance leads with the Carrier Senior Vice President, Regulatory and Compliance, the Engineering federal contracts compliance manager, and the Tower site operations director; coordinated by the Group Chief Privacy Officer; reviewed by group internal audit and outside telecommunications counsel |
| Sources checked | eCFR full text (point in time 2026-09-23) for 47 CFR 64.2003-64.2011, 1.50007, 17.6, 17.47-17.49, and FAR 52.204-21, -23, -24, -25, -26; Federal Register API through 2026-10-05; govinfo for 47 U.S.C. 222, 15 U.S.C. 1681a and 1681m, and SEC Release 33-11216 (88 FR 51896) |

## 1. Applicability

### 1.1 Telecom Carrier: the CPNI rules apply, through the voice services
The CPNI rules bind "telecommunications carriers," defined by reference to 47 U.S.C. 153, and "shall include an entity that provides interconnected VoIP service" (47 CFR 64.2003(o)). The Carrier's 9 ILECs provide local exchange and toll service as common carriers, and the CLEC and ILECs provide interconnected VoIP (about 1.1 million lines). There is **no size threshold** in 64.2001-64.2011. The only carve-outs are service-specific: 64.2010(h) applies only to CMRS providers (no wireless service).

**Broadband is outside the CPNI rules today.** CPNI is information about "a telecommunications service" plus information in bills for telephone exchange or toll service (47 U.S.C. 222(h)(1)). After *Ohio Telecom Ass'n v. FCC* (6th Cir. 2025-01-02, No. 24-7000) set aside the 2024 reclassification order, broadband is an information service, and the FCC conformed the CFR on 2025-08-08 (90 FR 38406). No later reclassification was found in the Federal Register through 2026-10-05. Two consequences, as in the Small sample:
1. Broadband is a "communications-related service" for marketing (64.2003(e), (i)), so using voice CPNI to sell broadband needs opt-out or opt-in approval (64.2007(b)).
2. One account record holds both, so **POL-04 protects the whole customer account record to the CPNI standard.**

**Affiliates are the multi-sector issue.** The rules distinguish affiliates. A carrier may share CPNI among "affiliated entities that provide a service offering to the customer" only when the customer subscribes to more than one category of service (64.2005(a)(1)-(2)). It may disclose CPNI to affiliates "that provide communications-related services" for marketing those services with opt-out or opt-in approval, and every other use or disclosure needs opt-in approval (64.2007(b)). Outside marketing, the statute limits use to providing the telecommunications service and "services necessary to, or used in" it, plus the 222(d) exceptions (47 U.S.C. 222(c)(1), (d)). The Engineering and Tower divisions are affiliates (47 U.S.C. 153(1); 64.2003(c)) that do not provide service offerings to the Carrier's mass-market customers. So:
- Engineering crews doing restoration work on the Carrier network may receive what they need for that work (222(c)(1)(B)), under a written agreement and training.
- Standing read access for about 470 affiliate operators to every Carrier ticket is not tied to that purpose (G-003).
- The 2026 Engineering sales campaign that used Carrier enterprise service data was a disclosure for marketing a service that counsel does not treat as communications-related, so it needed opt-in approval (G-008). The Carrier must also record its affiliates' campaigns that use CPNI (64.2009(c)).

**Status of the 2023 breach amendments to 64.2011 (re-checked 2026-10-05).** The amendments remain "delayed indefinitely." The Sixth Circuit denied review on 2025-08-13 (Nos. 24-3133/3206/3252), upholding the order under 47 U.S.C. 201(b). A Federal Register search through 2026-10-05 found no FCC effective-date notice; the 2026 items that matched were the regulatory agenda and Paperwork Reduction Act notices for information collections, and none announced an effective date. No FCC rule published from 2026-09-15 to 2026-10-05 touches 64.2011. This analysis and P08 use the **current** 64.2011.

**CPNI breach and SEC disclosure fit together through Form 8-K Item 1.05(d).** The SEC identified one conflict with Item 1.05: the CPNI rule's bar on public disclosure until 7 full business days after the USSS and FBI notice. Item 1.05(d) lets a registrant "subject to 47 CFR 64.2011" delay the Item 1.05 filing for the period in 64.2011(b)(1), "in no event for more than seven business days after notification required under such provision has been made," if it notifies the SEC in correspondence on EDGAR no later than the date the filing was otherwise due (Release 33-11216, 88 FR 51896). The release says the exception does not extend to agency-directed delays under 64.2011(b)(3). The holding company is the registrant and the Carrier is the regulated carrier, so the group treats the delay as available for a CPNI breach at the Carrier; counsel confirms at each incident (P08).

### 1.2 Network Engineering Services
| Requirement | Applies? | Basis |
|---|---|---|
| FTC Safeguards Rule (N54-R01), the professional services profile's primary regulation | **No** | Engineering is not a "financial institution" under 16 CFR 314.2 (no tax preparation, lending, appraisal, or settlement activity) |
| **FAR 52.204-21** (N54-R04) | **Yes** | In all 12 federal civilian agency contracts; FCI is held in the SYS-E2 enclave. The 15 basic safeguarding requirements (52.204-21(b)(1)(i)-(xv)) and flowdown (c) are the rows NE-G01 to NE-G16 |
| FAR 52.204-25 and 52.204-23 | **Yes** | In all federal contracts. Reporting: covered telecommunications equipment within 1 business day (52.204-25(d)); Kaspersky covered articles within 3 business days (52.204-23(c)); further information within 10 business days in both |
| DFARS 252.204-7012 and CMMC (N54-R05) | **No** | No DoD contracts and no CUI |
| HIPAA (N54-R06), IRC 7216 (N54-R02) | **No** | No PHI or tax return information |
| FTC Act Section 5 | **Yes** | Engineering is not a common carrier; its security representations to customers must be accurate (NE-G22) |
| Customer contracts | **Yes** | Incident and outage notice, confidentiality, remote access, and SOC 2 terms for 64 MNO customers (NE-G23 to NE-G27) |

### 1.3 Tower and Fiber Infrastructure
| Requirement | Applies? | Basis |
|---|---|---|
| FTC Safeguards Rule (N53-R01), the real estate profile's primary regulation | **No** | Tower and dark fiber leases are real property and private-carriage leases, not the financial activities 314.2 lists (TF-G08) |
| **Antenna structure rules, 47 CFR Part 17** | **Yes** | About 6,200 registered structures with lighting specifications. The owner is responsible for lighting (17.6(a)); must observe lights every 24 hours or keep an automatic alarm system (17.47(a)); inspect alarm systems every 3 months unless exempt (17.47(b)-(c)); report uncorrected outages to the FAA (17.48(a)); keep outage records 2 years (17.49). These are not security rules, but the alarm system is a networked device fleet, so a cyber incident can cause a compliance failure |
| FTC Act Section 5 (N53-R02) | **Yes** | Landowner taxpayer and bank data; tenant information |
| CCPA (N53-R03); PCI DSS (N53-R04) | **No** | No California operations; no card acceptance |
| SEC (N53-R05) | **Via group** | The holding company is the registrant |
| State breach laws | **Yes** | About 11,800 landowners in 22 states |

### 1.4 Group-wide obligations
- **SEC (C-COMMUNICATIONS-R06; N53-R05):** Reg S-K Item 106 annual disclosure and Form 8-K Item 1.05 within 4 business days after a materiality determination (with the 1.05(d) CPNI delay above, and the Attorney General delay in 1.05(c)).
- **State breach notification laws:** each state where affected individuals reside; Florida (Fla. Stat. 501.171) is the worked example in P08.
- **CIRCIA (C-COMMUNICATIONS-R05):** not in effect; no final rule published as of 2026-10-05. Voluntary reporting to CISA and the FBI is used until then.
- **FCRA adverse action notices:** the Carrier's deposit model uses consumer report information; an action "adverse to the interests of the consumer" in connection with an application is adverse action (15 U.S.C. 1681a(k)(1)(B)(iv)) and requires the 1681m(a) notices. Covered in P10.

### 1.5 Excluded, with reasons
Submarine cable landing license rules (C-COMMUNICATIONS-R04; no cable or SLTE); CMRS-only CPNI rules (64.2010(h)); the EAS cybersecurity order (no video or broadcast service); state comprehensive privacy laws (assessed by the Group Chief Privacy Officer outside this security sample).

## 2. Regulation-by-division matrix
| Requirement | Telecom Carrier | Network Engineering Services | Tower and Fiber Infrastructure | Group (corporate) |
|---|---|---|---|---|
| C-COMMUNICATIONS-R01 FCC CPNI rules | **Primary.** Carrier and interconnected VoIP provider | Not a carrier. Receives Carrier CPNI only as an affiliate under 222(c)(1) limits; handles customers' CPNI as their agent by contract | Not a carrier. Must not receive Carrier CPNI except for a permitted purpose | Group policy POL-04 applies the CPNI standard to the whole account record |
| C-COMMUNICATIONS-R02 Outage reporting (Part 4) | **Applies** (wireline 4.3(g); VoIP 4.3(h)) | Not a reporting entity; 30-minute outage notices to carrier customers by contract | Not a reporting entity | Supports through the SOC and BIA |
| C-COMMUNICATIONS-R03 CALEA SSI | **Applies** (10 operating companies) | Not applicable | Not applicable | Group SOC must engage the LI team |
| 47 CFR 1.50007 covered equipment report | **Applies** (certified no covered equipment) | Screening supplier for the Carrier | Not applicable | Group procurement runs screening |
| C-COMMUNICATIONS-R04 Submarine cable rules | Not applicable | Not applicable | Not applicable | Not applicable |
| C-COMMUNICATIONS-R05 CIRCIA | Tracked only (not in effect) | Tracked only | Tracked only | Tracked only |
| C-COMMUNICATIONS-R06 / N53-R05 SEC | Via group | Via group | Via group | **Applies** (SEC registrant) |
| N54-R04 FAR 52.204-21 | Not applicable (transport contracts hold no FCI in Carrier systems) | **Applies** (12 contracts) | Not applicable | Not applicable |
| FAR 52.204-25 and 52.204-23 | **Applies** (federal transport contracts) | **Applies** (12 contracts) | Not applicable | Procurement screening |
| N54-R01 / N53-R01 FTC Safeguards Rule | Not applicable | Not applicable (not a financial institution) | Not applicable (not a financial institution) | Not applicable |
| FTC Act Section 5 (N53-R02) | Limited: excludes common carrier activities (15 U.S.C. 45(a)(2)); applies to broadband practices per counsel | **Applies** | **Applies** | Applies |
| 47 CFR Part 17 antenna structures | Not applicable (Carrier structures are owned by the Tower division) | Not applicable | **Applies** (about 6,200 lit structures) | Not applicable |
| FCRA adverse action (15 U.S.C. 1681m(a)) | **Applies** (deposit decisions) | Not applicable | Not applicable | AI program (P10) |
| State breach notification laws | Each state where affected customers reside (14 states) | Third-party agent duties to customers (Fla. Stat. 501.171(6) worked example) | Landowners in 22 states | Coordinates (P08) |
| SOC 2 (contractual) | Not in scope (P09) | **Required by 37 customers** (P09) | Not in scope (P09) | Group services carved in |

## 3. Method
1. **Requirements.** Each paragraph of 47 CFR 64.2005-64.2011, 1.20000-1.20006, 4.9, 4.18, 1.50007, 17.6, 17.47-17.49, and FAR 52.204-21, -23, and -25 that imposes, permits, or limits conduct became one row, cited to the paragraph (public-domain text; short quotes only). Contract and state-law rows summarize the duty in plain words.
2. **Crosswalk.** Regulatory rows carry an **author mapping** to CSF 2.0 and SP 800-53 Rev. 5; NIST has published no official mapping for these rules. Benchmark rows (G-048 to G-061) use NIST's official CSF 2.0 to SP 800-53 reference mapping (a selection of the listed controls).
3. **Evidence.** Interviews across the three divisions; configuration exports; live tests of the portal, the chatbot (2026-07-22), and the legacy billing portal (2026-07-23); a sample of 120 recorded care calls (2026-07-09); CPNI certifications and CALEA filings; FAR clause and subcontract review; RMU inventory and alarm center records; and P07 results.
4. **Status.** Met, Partially met, Not met, or Not applicable. Gap risk uses the P01 scale (Very Low to Very High). Where a rule applies to several operating companies, a row is Met only if it is met for all of them.

## 4. Results

### 4.1 Telecom Carrier (`gap-analysis.csv`)
| Requirement set | Rows | Met | Partially met | Not met | N/A |
|---|---|---|---|---|---|
| FCC CPNI rules (47 U.S.C. 222(a); 64.2005-64.2011) | 34 | 19 | 13 | 1 | 1 |
| CALEA SSI rules (1.20000-1.20006) | 8 | 3 | 3 | 2 | 0 |
| Outage reporting (Part 4) | 4 | 3 | 1 | 0 | 0 |
| Covered equipment report (1.50007) | 1 | 0 | 1 | 0 | 0 |
| NIST CSF 2.0 benchmark (voluntary) | 14 | 4 | 10 | 0 | 0 |
| **Total** | **61** | **29** | **28** | **3** | **1** |

Of the 31 partially met or not met rows, 11 are rated **High** and 20 **Moderate**. Five High rows are CPNI rules: affiliate sharing and disclosure (G-003, G-008), reasonable measures (G-022), and online authentication in the chatbot pilot (G-024, G-026). Six are network security benchmark outcomes tied to the management plane, patching, monitoring, and tenant over-access.

**Not met:** G-008 (affiliate campaign without opt-in approval); G-038 and G-041 (CALEA appendix and refiling for the 2 acquired operating companies).

**What is working:** approval flags and opt-out mechanics across both billing systems, the biennial notice, telephone and in-store authentication for in-house staff, the business customer exemption, lawful-intercept activation and records, NORS and DIRS reporting, and the reporting facility accounts.

### 4.2 Network Engineering Services (`gap-analysis-engineering.csv`)
| Requirement set | Rows | Met | Partially met | Not met | N/A |
|---|---|---|---|---|---|
| FAR 52.204-21 (15 requirements plus flowdown) | 16 | 13 | 3 | 0 | 0 |
| FAR 52.204-25 and 52.204-23 | 3 | 1 | 2 | 0 | 0 |
| FTC Safeguards Rule; DFARS and CMMC | 2 | 0 | 0 | 0 | 2 |
| FTC Act Section 5 | 1 | 0 | 1 | 0 | 0 |
| MNO customer contracts | 5 | 0 | 3 | 2 | 0 |
| State third-party agent duty | 1 | 0 | 1 | 0 | 0 |
| **Total** | **28** | **14** | **10** | **2** | **2** |

Of the 12 gaps, 1 is **High** (NE-G26, remote access terms), 9 Moderate, and 2 Low. The FCI enclave is in good shape; the gaps are in the MNO service that customers rely on. **Not met:** NE-G26 (shared gateway accounts against contract terms) and NE-G27 (no SOC 2 report yet).

### 4.3 Tower and Fiber Infrastructure (`gap-analysis-tower.csv`)
| Requirement set | Rows | Met | Partially met | Not met | N/A |
|---|---|---|---|---|---|
| Antenna structure rules (47 CFR Part 17) | 7 | 3 | 4 | 0 | 0 |
| FTC Act, state breach laws, tenant leases | 3 | 0 | 3 | 0 | 0 |
| FTC Safeguards, CCPA, PCI DSS | 3 | 0 | 0 | 0 | 3 |
| SEC (via group) | 1 | 1 | 0 | 0 | 0 |
| Group policy alignment | 1 | 0 | 0 | 1 | 0 |
| **Total** | **15** | **4** | **7** | **1** | **3** |

Of the 8 gaps, 1 is **High** (TF-G02, integrity of the automatic alarm system and the missing fallback), 6 Moderate, and 1 Low. **Not met:** TF-G15 (supplement drift and undocumented inheritance, scenario gap 9).

## 5. Group roadmap
| # | Gap (scenario gap) | Divisions | Citation | Risk | Action | Owner | Target |
|---|---|---|---|---|---|---|---|
| 1 | Affiliate access to and use of Carrier CPNI (2) | Carrier, Engineering, Tower | 64.2005(a)(2); 64.2007(b); 64.2009(c); 222(c)(1) | High | Remove the legacy role; intercompany CPNI agreement; affiliate campaigns through the Carrier tool with opt-in; register | Carrier Senior Vice President, Regulatory and Compliance | 2026-12-31 |
| 2 | Management plane and remote access in the acquired regions and SYS-E1 (1, 3, 7) | Carrier, Engineering | 64.2010(a); CSF PR.AA-01, PR.IR-01, PR.PS-02; customer contracts | High | Named AAA accounts with MFA; SBC replacement; brokered SYS-E1 sessions; SIEM onboarding | Group CISO | 2027-03-31 |
| 3 | Chatbot online authentication (4) | Carrier | 64.2010(c), (e) | High | One-time-code recovery; release gate for chatbot changes | Carrier digital channels director | 2026-12-31 |
| 4 | Tower lighting alarm system integrity and fallback (6) | Tower | 17.47(a); 17.48(a); 17.49 | High | Fallback procedure; legacy RMU remediation; records in SYS-T2 | Tower site operations director | 2027-03-31 |
| 5 | Multi-regulator notification not exercised (8) | All | 64.2011; Form 8-K Item 1.05(d); 1.20003(c); 17.48; Part 4; customer contracts | Moderate | Adopt the P08 matrix; cross-division tabletop | Group General Counsel | 2026-12-15 |
| 6 | CALEA filings for the acquired companies (5) | Carrier | 1.20003(b)(4); 1.20005 | Moderate | Refile both SSI policies | Carrier Vice President, Network Security and Lawful Intercept | 2026-10-31 |
| 7 | Covered equipment screening (10) | Engineering, Carrier | 1.50007; FAR 52.204-25(d) | Moderate | Automated screening with records; reporting procedure | Group procurement director | 2026-12-31 |
| 8 | Tower supplement drift and inheritance (9) | Tower | POL-01 4.5, 4.6 | Moderate | Re-issue supplement; inheritance matrix | Tower division security and compliance lead | 2026-12-31 |
| 9 | Certification accuracy | Carrier | 64.2009(e); 64.2008(c)(2) | Moderate | Evidence-based statement; name receiving entities in the notice | Carrier Senior Vice President, Regulatory and Compliance | 2027-02-28 |
| 10 | Legacy billing change notices and PSAP contacts | Carrier | 64.2010(f); 4.9(h)(1) | Moderate | Add notices; confirm contacts | Carrier billing vice president; Carrier NOC director | 2026-12-31 |

High and Moderate gaps are carried into the registers (P01) and the POA&M (P07). POAM-028 (certification and notice accuracy), POAM-029 (legacy billing change notices), and POAM-030 (PSAP contact confirmation) come directly from this analysis.

## 6. Pending regulatory changes
- **64.2011 amendments (delayed indefinitely).** Once effective, the FCC would be notified with the USSS and FBI within 7 business days; "breach" would cover PII as well as CPNI and inadvertent access; customer notice would be due without unreasonable delay and within 30 days of reasonable determination, with no 7-business-day wait; breaches under 500 customers with no reasonably likely harm would go into an annual summary. Because the waiting period would disappear, the Form 8-K Item 1.05(d) delay would no longer have a period to attach to; the SEC noted that the FCC proposal could eliminate the conflict. P08 carries both versions.
- **CIRCIA.** Covered cyber incident reports within 72 hours and ransom payment reports within 24 hours are expected once a final rule is published and effective. None is in effect as of 2026-10-05.
- **FAR overhaul.** The proposed rule (FR Doc 2026-12559) would renumber 52.204-21 as 52.240-5 and add CUI rules. Proposed only; no effect on Engineering's current contracts.
- **Broadband classification.** If broadband were reclassified as a telecommunications service, broadband usage data would become CPNI. The whole-account policy in section 1.1 already covers that data.
