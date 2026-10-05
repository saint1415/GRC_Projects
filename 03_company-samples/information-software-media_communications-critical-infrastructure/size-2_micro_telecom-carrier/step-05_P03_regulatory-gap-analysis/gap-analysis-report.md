# Regulatory Gap Analysis: Cris Santos Company | Communications | Micro

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (rural fiber broadband and voice carrier) |
| Tier / Vertical | Micro / Communications |
| Primary regulation | FCC CPNI rules, 47 CFR 64.2001-64.2011 (47 U.S.C. 222), text in force on 2026-09-23 (C-COMMUNICATIONS-R01) |
| Secondary regulations | CALEA system security and integrity rules, 47 CFR 1.20000-1.20008 (C-COMMUNICATIONS-R03); FCC outage reporting, 47 CFR Part 4 (C-COMMUNICATIONS-R02) |
| Voluntary benchmark | 8 NIST CSF 2.0 outcomes, used to give "reasonable measures" in 64.2010(a) a concrete meaning |
| Assessment dates | 2026-07-20 to 2026-07-31 |
| Assessor | Office Manager (security and compliance lead) with the Network Operations Lead; the telecom regulatory consultant reviewed section 1 |
| Sources checked | eCFR full text (point in time 2026-09-23) for 47 CFR 1.20002-1.20005, 4.3, 4.5, 4.7, 4.9, 4.18, 8.1, 64.2003, 64.2009-64.2011; Federal Register API (searched through 2026-10-05) |
| Approved | 2026-08-31 by the Owner and General Manager |

## 1. Applicability

### 1.1 The CPNI rules apply, through the voice service
The CPNI rules bind "telecommunications carriers," and for this subpart the term "shall include an entity that provides interconnected VoIP service" (47 CFR 64.2003(o)). The company sells interconnected VoIP under its own brand to about 390 accounts. It buys the softswitch from a wholesale hosted voice platform, but it is the provider to the customer, so the duties are the company's, not the platform's.

There is **no size threshold or small-carrier exemption** in 64.2001-64.2011. A carrier with 440 telephone numbers has the same authentication, training, certification, and breach duties as a national carrier. The only carve-outs are service-specific and do not help here: 64.2010(h) is for wireless (CMRS) providers only.

**What size changes is which rules are in play.** The company has never asked customers for CPNI approval and uses CPNI only as 64.2005 allows without approval (serving the customer, billing, fraud protection, and offers within the voice service). That makes 13 rows **not applicable today**: the approval, notice, opt-out, and outbound marketing supervision rules (64.2007(a), 64.2008, 64.2009(d), (f)), plus the CMRS and business-customer rows. They become applicable the moment the company solicits approval. POL-04 4.3 forbids using CPNI for marketing without approval, and the AI assistant's "personalized offers" setting, which did use CPNI that way, was turned off on 2026-08-14 (G-007).

### 1.2 Broadband is outside the CPNI rules today
CPNI is information about "a telecommunications service" a customer buys, plus information in bills for telephone exchange or toll service (47 U.S.C. 222(h)(1)). Broadband usage is CPNI only if broadband is a telecommunications service.
- In **Ohio Telecom Ass'n v. FCC** (6th Cir., decided 2025-01-02, No. 24-7000), the court held that broadband is an "information service" and set aside the FCC's 2024 reclassification order.
- The FCC conformed the CFR to the rules actually in effect after that decision (90 FR 38406, effective 2025-08-08).
- No later FCC action reclassifying broadband was found in the Federal Register through 2026-10-05.

**Result:** broadband usage and configuration data (IP assignments, data usage, speed tier) is not CPNI. Call detail records, voice features, and the voice lines of every bill are. Two consequences:
1. Broadband counts as a "communications-related service" for marketing purposes (64.2003(e), (i)). Using voice CPNI to recommend broadband needs approval (64.2007(b)). That is exactly what the AI assistant's default setting did (G-007).
2. The BSS keeps one record per customer. **By policy (POL-04), the company protects the whole customer account record at the CPNI level**, including broadband data and the driver license numbers that trigger Florida's breach law.

### 1.3 Status of the 2023 breach amendments to 64.2011
- The FCC's 2023 Data Breach Reporting Order (FCC 23-111, 89 FR 9968, 2024-02-12) took effect except for the amendments to 64.2011, which are delayed indefinitely until the FCC publishes an effective-date notice. The eCFR text current through 2026-09-23 still links to that amendment as not yet in effect.
- The Sixth Circuit **denied** the petitions for review on 2025-08-13 (Ohio Telecom Ass'n v. FCC, Nos. 24-3133/3206/3252), upholding the rules under 47 U.S.C. 201(b).
- A Federal Register search on 2026-10-05 found no effective-date notice. The FCC's 2026 regulatory agenda (91 FR 53092) is the latest FCC document on the proceeding.

**Result:** this analysis and the P08 runbook use the **current** 64.2011: notice to the USSS and FBI through the FCC's central reporting facility within 7 business days of reasonable determination, then a hold of 7 full business days before customer or public notice. The amended text is shown in the `pending_rule_change` column and is **not** treated as a current obligation. For this company, the most important change if it takes effect: breaches of customer PII (for example, driver license numbers) would be covered too, and breaches under 500 customers with no reasonably likely harm would go into an annual summary instead of an individual FCC notice.

### 1.4 Secondary regulations
| Regulation | Applies? | Basis |
|---|---|---|
| **CALEA SSI rules**, 47 CFR 1.20000-1.20008 (C-COMMUNICATIONS-R03) | **Yes** | CALEA's carrier definition includes an entity the FCC has found to provide a replacement for a substantial portion of local telephone exchange service (47 CFR 1.20002(e)(3)). The FCC's 2005 First Report and Order (70 FR 59664, effective 2005-11-14) established that facilities-based broadband internet access providers and interconnected VoIP providers must comply. The company is both. That order rests on CALEA's own definition, not on Title II classification, so the regulatory consultant reads the 2025 broadband decision as leaving it in place. The FCC's January 2025 CALEA cybersecurity ruling was rescinded on 2025-11-20 (90 FR 58006); only the codified SSI rules are analyzed. Rows G-035 to G-042 |
| **Outage reporting**, 47 CFR Part 4 (C-COMMUNICATIONS-R02) | **Yes** | Wireline communications provider over its own fiber (4.3(g)) and interconnected VoIP provider (4.3(h)). Thresholds are outage-based. At this size the voice user-minute tests are hard to reach (about 34 hours of total loss across 440 numbers; 4.7(e)), but the **667 OC3-minute test (4.9(f)(2)) is reached by a 30-minute loss of the 10 Gbps middle-mile circuit**. The 911 contact rule (4.9(h)(1)) and DIRS (4.18) apply regardless of thresholds. Rows G-043 to G-046 |
| Florida Information Protection Act, Fla. Stat. 501.171 | **Yes** (breach notice only) | Driver license numbers (about 1,050 accounts) and portal user names with passwords are Florida-defined personal information. Drives the P08 notification matrix, not row-by-row analysis |
| Broadband transparency and labels, 47 CFR 8.1 | Yes, but out of scope | Consumer disclosure duties, not security safeguards. Tracked by the regulatory consultant |
| CIRCIA (C-COMMUNICATIONS-R05) | **Not yet** | No final rule in the Federal Register as of 2026-10-05. The proposed rule (89 FR 23644) covers entities meeting either a size or a sector criterion; the Communications sector criterion names VoIP providers and internet service providers. The company expects to be covered if the final rule keeps it. Voluntary reporting to CISA and the FBI until then |
| SEC disclosure rules (C-COMMUNICATIONS-R06) | No | Privately held |
| Submarine cable rules (C-COMMUNICATIONS-R04) | No | No cable landing license or SLTE |

### 1.5 Why a voluntary benchmark is included
No FCC rule sets general cybersecurity controls for a carrier's network. The CPNI rules require "reasonable measures to discover and protect against attempts to gain unauthorized access to CPNI" (64.2010(a)) without saying what they are. For a micro carrier whose CPNI sits in a SaaS billing system and a wholesale voice portal, the realistic attack paths run through credentials and the network hut. Rows G-047 to G-054 record the 8 NIST CSF 2.0 outcomes that matter most for those paths and for the P08 scenario.

## 2. Method
1. **Requirements.** Each paragraph of 47 CFR 64.2005-64.2011 that imposes, permits, or limits conduct became one row, cited to the paragraph (public-domain text; short quotes only). 47 U.S.C. 222(a) is the statutory duty (G-001). The CALEA and Part 4 rows follow the same method. The CPNI row set is the same as the Small sample's, so the two can be compared.
2. **Crosswalk.** Each regulatory row was mapped to CSF 2.0 and SP 800-53 Rev. 5. This is an **author mapping**; NIST has published no mapping for 47 CFR Parts 1, 4, or 64. The benchmark rows use NIST's CSF 2.0 to SP 800-53 reference mapping (a selection).
3. **Documentary evidence.** Each status rests on a named document or test: the filed CPNI certifications (2024 to 2026), the 2017 CALEA SSI filing and the 2022 intercept record, BSS and voice platform user lists and settings, a live test of the portal reset and the AI assistant on 2026-07-24, a sample of 10 call detail requests in BSS tickets on 2026-07-27, the NORS account and the 2025 outage ticket, and the walkthrough of the office and hut on 2026-07-22. Interviews covered all 7 employees.
4. **Status.** Met, Partially met, Not met, or Not applicable **as of the end of fieldwork (2026-07-31)**. Later actions (for example, personalized offers off on 2026-08-14) appear in the remediation column but do not change the status. Gap risk uses the P01 scale.

## 3. Results summary
| Requirement set | Rows | Met | Partially met | Not met | N/A |
|---|---|---|---|---|---|
| FCC CPNI rules (47 U.S.C. 222(a); 64.2005-64.2011) | 34 | 3 | 6 | 12 | 13 |
| CALEA SSI rules (47 CFR 1.20000-1.20006) | 8 | 3 | 2 | 3 | 0 |
| Outage reporting (47 CFR Part 4) | 4 | 0 | 1 | 3 | 0 |
| NIST CSF 2.0 benchmark (voluntary) | 8 | 0 | 4 | 4 | 0 |
| **Total** | **54** | **6** | **13** | **22** | **13** |

Of the 35 partially met or not met rows, 10 are rated **High**, 20 **Moderate**, and 5 **Low**. Four High rows are CPNI authentication rules (64.2010(a), (b), (c), (e)); six are network security benchmark outcomes (credentials, authentication, software maintenance, vulnerability identification, network protection, monitoring).

**What the numbers say.** The company does the rare things well (one lawful intercept handled correctly with a complete record; fraud alerts; no CPNI marketing) and the everyday things poorly. Every day, representatives release call detail by voice recognition, and the portal lets anyone with a bill reset a password. Nothing in the company's routine has ever been written down, which is why the CPNI certification statement could not be supported (G-019).

## 4. Priority gaps
| Gap | Citation | Risk | Action | Owner | Target |
|---|---|---|---|---|---|
| Call detail released on inbound calls without a password | 64.2010(b) | High | Required PIN; otherwise send to the address of record or call the number of record | Office Manager | 2026-10-31 |
| Portal reset and assistant verification use account information | 64.2010(c), (e) | High | One-time-code reset to the number or email of record; guest verification off (done 2026-08-14) | Office Manager | 2026-11-30 |
| No reasonable measures to discover attempts on CPNI | 64.2010(a) | High | Execute P01 treatments for R-002, R-003, R-004, R-006, R-010 | Office Manager | 2026-12-31 |
| Shared and default network credentials; no MFA on voice platform and VPN | CSF PR.AA-01, PR.AA-03; supports 64.2010(a) | High | Named accounts; MFA; password manager | Network Operations Lead | 2026-09-30 (MFA); 2026-12-31 (named accounts) |
| Router and OLT firmware out of date; no vulnerability tracking | CSF PR.PS-02, ID.RA-01 | High | Upgrades on 2026-09-20; monthly advisory review | Network Operations Lead | 2026-09-30 |
| Flat hut network; no security monitoring | CSF PR.IR-01, DE.CM-01 | High | Management access lists; login and change alerts | Network Operations Lead | 2026-12-31 |
| No CPNI breach procedure or reporting facility access | 64.2011(a)-(e) | Moderate | P08 runbook; register and test facility access | Office Manager | 2026-10-31 |
| No CPNI training or express discipline | 64.2009(b) | Moderate | Annual course with signed record; POL-02 A.4 | Office Manager | 2026-10-31 |
| Certification statement not supported | 64.2009(e) | Moderate | Evidence-based statement; counsel on the 2026 filing | Owner and General Manager | 2027-03-01 |
| CALEA appendix wrong; policies never refiled | 1.20003(b)(4), (c); 1.20005 | Moderate | Rewrite and refile through CEFS | Owner and General Manager | 2026-10-31 |
| No 911 outage contacts; no DIRS procedure; 2025 outage not assessed | 4.9(f), (h)(1); 4.18 | Moderate | Contacts confirmed; outage checklist; DIRS registration; counsel reviews the 2025 outage | Network Operations Lead | 2026-09-30 to 2026-11-30 |

The full list, with evidence, is in `gap-analysis.csv`. Every High and Moderate gap is carried into the risk register (P01) and, where a control was assessed, the POA&M (P07).

## 5. Remediation plan
The plan fits a 7-person carrier: most actions are vendor settings, one-page procedures, and filings. Technical network work is done by the Network Operations Lead with the consultant. Costs are in the P01 treatment summary.

| Phase | Due | Actions | Gaps closed |
|---|---|---|---|
| 1. Stop the easy leaks | 2026-09-30 | Personalized offers off (done 2026-08-14); guest verification off (done 2026-08-14); photo ID at the counter; MFA on the voice platform and VPN; router and OLT firmware; 911 outage contacts; outage checklist; incident register | G-007, G-024, G-033, G-043, G-044, G-045, G-048, G-049 |
| 2. Write it down and train | 2026-10-31 | Required phone PIN; CPNI course for all staff; third-party CPNI access register; approval-status statement; reporting facility access; CALEA SSI rewrite and CEFS refiling; advisory review; off-site configuration backup | G-015, G-016, G-017, G-022, G-030, G-034, G-036 to G-039, G-041, G-050, G-053 |
| 3. Rebuild customer authentication | 2026-11-30 | One-time-code reset; change notices for all 4 types; breach procedure tabletop; customer notice template; DIRS registration | G-023, G-025, G-026, G-029, G-031, G-032, G-046 |
| 4. Network hardening and vendors | 2026-12-31 | Named network accounts; management access lists; security alerts; vendor reviews and contract terms; CPNI program review | G-001, G-021, G-047, G-051, G-052, G-054 |
| 5. Certification | 2027-03-01 | Evidence-based statement and complaint summary with the CPNI certification | G-019 |

**Progress check.** The Office Manager reports progress to the Owner and General Manager at a monthly 30-minute meeting, using the P07 POA&M as the tracker.

## 6. Pending regulatory changes
- **64.2011 amendments (delayed indefinitely).** If made effective: the FCC joins the USSS and FBI as a recipient within 7 business days; "breach" covers customer PII and inadvertent access; customer notice is due without unreasonable delay and within 30 days of reasonable determination, with no 7-day wait; breaches under 500 customers with no reasonably likely harm go into an annual summary. The P08 matrix carries both versions, so switching is a change to the matrix, not a redesign. Recheck the Federal Register at the start of every incident.
- **CIRCIA.** Covered cyber incident reports within 72 hours and ransom payment reports within 24 hours are expected once a final rule is published and effective. None is in effect as of 2026-10-05.
- **Broadband classification.** If broadband were reclassified as a telecommunications service, broadband usage data would become CPNI. The whole-account policy in section 1.2 already protects it.
- **DIRS rule changes.** A 2026 amendment to 4.18 (91 FR 39516) is delayed indefinitely; the current 4.18 applies.
