# Regulatory Gap Analysis: Cris Santos Company | Communications | Small

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (regional broadband and wired telecommunications carrier) |
| Tier / Vertical | Small / Communications |
| Primary regulation | FCC CPNI rules, 47 CFR 64.2001-64.2011 (47 U.S.C. 222), text in force on 2026-09-23 (C-COMMUNICATIONS-R01) |
| Secondary regulations | CALEA system security and integrity rules, 47 CFR 1.20000-1.20008 (C-COMMUNICATIONS-R03); FCC outage reporting, 47 CFR Part 4 (C-COMMUNICATIONS-R02) |
| Voluntary benchmark | NIST CSF 2.0, with the CISA Cross-Sector Cybersecurity Performance Goals (CPGs) as the prioritized practice list |
| Assessment dates | 2026-07-20 to 2026-07-31 |
| Assessor | IT Manager (security and compliance lead) with the Regulatory Affairs Manager; outside telecommunications counsel reviewed section 1 |
| Sources checked | eCFR full text (point in time 2026-09-23); Federal Register API; govinfo; Sixth Circuit opinions 25a0002p.06 and 25a0224p.06 (all retrieved 2026-09-26) |

## 1. Applicability

### 1.1 The CPNI rules apply, through the voice services
The CPNI rules bind "telecommunications carriers," defined by reference to 47 U.S.C. 153, and "shall include an entity that provides interconnected VoIP service" (47 CFR 64.2003(o)). The company is covered twice over:
- It provides **local exchange and toll service** over its copper network as a common carrier. That is a telecommunications service, so the company is a telecommunications carrier.
- It provides **interconnected VoIP** over fiber (14,800 lines), which 64.2003(o) brings in expressly.

There is **no size threshold or small-carrier exemption** in 64.2001-64.2011. The only carve-outs are service-specific: 64.2010(h) applies only to CMRS providers (the company has no wireless service), and 64.2008(d)(3) applies only to carriers that send opt-out notices by email (the company mails them).

### 1.2 Broadband is outside the CPNI rules today
CPNI is information about "a telecommunications service subscribed to by any customer of a telecommunications carrier" plus information in bills for telephone exchange or toll service (47 U.S.C. 222(h)(1)). Whether broadband usage data is CPNI therefore turns on whether broadband is a telecommunications service.
- In **Ohio Telecom Ass'n v. FCC** (6th Cir., decided 2025-01-02, No. 24-7000), the court held that broadband providers "offer only an 'information service' under 47 U.S.C. 153(24)" and set aside the FCC's 2024 order (89 FR 45404) that had reclassified broadband as a telecommunications service.
- The FCC's Wireline Competition Bureau then conformed the CFR to "the rules that are actually in effect as a result of the Ohio Telecom" decision (90 FR 38406, effective 2025-08-08). That order records that the 2024 rules never took effect and that the court's mandate issued 2025-03-20.
- No later FCC action reclassifying broadband was found in the Federal Register through 2026-09-25. The FCC's 2026 regulatory agenda lists the open internet docket with "Next Action Undetermined" (91 FR 53092).

**Result:** the company's broadband internet access service is an information service, so broadband usage and configuration data (for example, IP assignments, data usage, speed tier) is **not CPNI**, and the Subpart U safeguards do not attach to it as such. The CPNI rules still reach everything tied to the voice services: call detail records, voice features and plans, and voice bills, including bundled bills that show voice charges.

**Two practical consequences:**
1. Broadband counts as a "communications-related service" for marketing purposes, because that term includes "information services typically provided by telecommunications carriers, such as Internet access" (64.2003(e), (i)). Using voice CPNI to sell broadband to a voice-only customer needs opt-out or opt-in approval (64.2007(b)). This is gap G-007 (the chatbot upsell).
2. The BSS holds one account record for bundled customers. Separating "CPNI" from "non-CPNI" fields inside that record is impractical, so **by policy (POL-04) the company protects the whole customer account record to the CPNI standard.** Broadband data practices remain subject to FTC Act Section 5, which excludes only "common carriers subject to the Acts to regulate commerce" (15 U.S.C. 45(a)(2)); counsel reads that exclusion as limited to the company's common carrier services.

### 1.3 Status of the 2023 breach amendments to 64.2011
- The FCC's 2023 Data Breach Reporting Order (FCC 23-111, 89 FR 9968, 2024-02-12) took effect 2024-03-13 **except** the amendments to 64.2011, which are "delayed indefinitely." The FCC said it "will publish a document in the Federal Register announcing the effective dates."
- The Sixth Circuit **denied** the petitions for review on 2025-08-13 (Ohio Telecom Ass'n v. FCC, Nos. 24-3133/3206/3252). The court held that 47 U.S.C. 222(a) does not give the FCC authority to impose breach reporting for customer PII, but upheld the rules under 47 U.S.C. 201(b), and found no Congressional Review Act bar.
- No effective-date notice was found in the Federal Register through 2026-09-25, the FCC's 2026 agenda shows "Next Action Undetermined" for the proceeding, and the eCFR text current through 2026-09-23 still shows the original 64.2011.

**Result:** this analysis, and the P08 runbook, use the **current** 64.2011 (law enforcement notice through the FCC reporting facility within 7 business days, then a 7-full-business-day wait before customer notice). The amended text (FCC as an added recipient, "covered data" including PII, customer notice within 30 days, an exemption for breaches under 500 customers with no reasonably likely harm) is shown in the `pending_rule_change` column and is **not** treated as a current obligation. Because the court upheld the order, the company plans for it to take effect on short notice (see section 5).

### 1.4 Secondary regulations
| Regulation | Applies? | Basis |
|---|---|---|
| **CALEA SSI rules**, 47 CFR 1.20000-1.20008 (C-COMMUNICATIONS-R03) | **Yes** | CALEA defines a telecommunications carrier as an entity "engaged in the transmission or switching of wire or electronic communications as a common carrier for hire" (47 U.S.C. 1001(8)(A)); the company's local exchange service meets that. The vertical file also records the FCC's inclusion of facilities-based broadband and interconnected VoIP providers under 1001(8)(B)(ii); this analysis did not re-read that 2005 order, and nothing here depends on it. The FCC's January 2025 declaratory ruling that read CALEA section 105 as a general cybersecurity duty was **rescinded** on 2025-11-20, and the accompanying NPRM withdrawn (FCC 25-81, 90 FR 58006). No new CALEA cybersecurity rule was found in the Federal Register through 2026-09-25. The obligations analyzed are the codified SSI rules only. |
| **Outage reporting**, 47 CFR Part 4 (C-COMMUNICATIONS-R02) | **Yes** | The company is a wireline communications provider (4.3(g)) and an interconnected VoIP provider (4.3(h)). Thresholds are outage-based, not size-based. Broadband-only outages are not reportable under the telephony user-minute test, but transport outages count under the 667 OC3-minute test (4.9(f)(2)). Rows G-043 to G-046; clocks used in P08 |
| CIRCIA (C-COMMUNICATIONS-R05) | **Not yet** | No final rule published as of 2026-09-25. The proposed rule would cover wire communications providers regardless of size, so the company expects to be covered. Voluntary reporting to CISA is used until then |
| SEC disclosure rules (C-COMMUNICATIONS-R06) | No | Privately held; not an Exchange Act registrant |
| Submarine cable rules (C-COMMUNICATIONS-R04) | No | No cable landing license or SLTE |
| EAS cybersecurity order (91 FR 48289, effective 2026-09-29) | No | Applies to EAS participants; the company offers no video or broadcast service |

### 1.5 Why a voluntary network security benchmark is included
No FCC rule sets general cybersecurity controls for a wireline carrier's network. The CPNI rules require "reasonable measures to discover and protect against attempts to gain unauthorized access to CPNI" (64.2010(a)) but do not say what those measures are, and the CALEA-based cybersecurity ruling is gone. The company therefore uses **NIST CSF 2.0** as the benchmark for "reasonable measures," prioritized using the **CISA CPGs** (current version 2.0, which CISA aligns to CSF 2.0). Rows G-047 to G-060 record the 14 CSF 2.0 outcomes most relevant to the P08 intrusion scenario. The CPG page could not be retrieved during this review (HTTP 403), so CPG goals are referenced by theme only (MFA, patching known exploited vulnerabilities, network segmentation, logging, backups, third-party risk, incident planning), and no CPG goal numbers are cited.

## 2. Method
1. **Requirements.** Each paragraph of 47 CFR 64.2005-64.2011 that imposes, permits, or limits conduct became one row, cited to the paragraph (public-domain text; short quotes only). 47 U.S.C. 222(a) is included as the statutory duty (G-001). CALEA and Part 4 rows follow the same method.
2. **Crosswalk.** Each regulatory row was mapped to CSF 2.0 and SP 800-53 Rev. 5 controls. This is an **author mapping**; NIST has published no official mapping for 47 CFR Parts 1, 4, or 64. The benchmark rows use NIST's official CSF 2.0 to SP 800-53 reference mapping (a selection of the listed controls).
3. **Evidence.** Interviews (COO, VP of Network Operations, Director of Customer Operations, Regulatory Affairs Manager, Billing Manager, Marketing Manager, NOC Manager, Network Engineering Manager, HR Manager); BSS and portal configuration; live tests of the portal password reset and the chatbot on 2026-07-24; a sample of 10 overflow call center recordings on 2026-07-27; the filed CPNI certification and CALEA policies; a walkthrough of CO-1, CO-2, and 3 cabinets on 2026-07-28.
4. **Status.** Met, Partially met, Not met, or Not applicable. Gap risk uses the P01 scale (Very Low to Very High).

## 3. Results summary
| Requirement set | Rows | Met | Partially met | Not met | N/A |
|---|---|---|---|---|---|
| FCC CPNI rules (47 U.S.C. 222(a); 64.2005-64.2011) | 34 | 9 | 13 | 10 | 2 |
| CALEA SSI rules (47 CFR 1.20000-1.20006) | 8 | 3 | 2 | 3 | 0 |
| Outage reporting (47 CFR Part 4) | 4 | 2 | 2 | 0 | 0 |
| NIST CSF 2.0 benchmark (voluntary) | 14 | 0 | 10 | 4 | 0 |
| **Total** | **60** | **14** | **27** | **17** | **2** |

Of the 44 partially met or not met rows, 10 are rated **High**, 25 **Moderate**, and 9 **Low**. Four of the High rows are CPNI authentication rules (64.2010(a), (b), (c), (e)); six are network security benchmark outcomes (vulnerability identification, patching, credentials, least privilege, segmentation, monitoring).

**What is working:** the approval flag and opt-out mechanics in the BSS, the business customer exemption contracts, in-store photo ID, lawful-intercept activation and records, and wireline NORS reporting.

## 4. Priority gaps and roadmap
| Gap | Citation | Risk | Action | Owner | Target |
|---|---|---|---|---|---|
| Online CPNI reachable with biographical or account information (portal reset; chatbot quick help) | 64.2010(c), (e) | High | Quick help disabled 2026-07-31; one-time-code reset to the telephone number or email of record | IT Manager | 2026-11-30 |
| Overflow vendor agents release call detail after SSN4 check | 64.2010(b) | High | Remove call detail screens from the vendor role; retrain; monthly sampling | Director of Customer Operations | 2026-09-30 |
| Management plane: shared and default credentials, reachable from corporate network | CSF PR.AA-01, PR.AA-05, PR.IR-01; supports 64.2010(a) | High | TACACS+ named accounts with MFA on all element types; jump-host-only access | Network Engineering Manager | 2026-12-31 |
| Unpatched edge routers; unsupported SBC; no internal scanning | CSF PR.PS-02, ID.RA-01 | High | Patch; replace or isolate the SBC; monthly authenticated scans | Network Engineering Manager | 2026-11-30 |
| No security monitoring | CSF DE.CM-01; supports 64.2010(a) | High | Managed detection with SIEM and 1-year log retention | IT Manager | 2027-01-31 |
| No CPNI breach procedure | 64.2011(a)-(e) | Moderate | Adopt P08 runbook and matrix; set up reporting facility access | Regulatory Affairs Manager | 2026-10-31 |
| CALEA SSI plan stale; no compromise reporting | 1.20003, 1.20005 | Moderate | Rewrite, refile through CEFS, add compromise reporting to P08 | Vice President of Network Operations | 2026-10-30 |
| Certification statement inaccurate | 64.2009(e) | Moderate | Counsel review; evidence-based statement for the CY2026 filing | COO | 2027-03-01 |
| Biennial opt-out notice overdue; campaign records missing | 64.2008(d)(2); 64.2009(c)-(d) | Moderate | Mail notice; pause opt-out campaigns 30 days; campaign register | Marketing Manager | 2026-11-15 |
| Training and discipline incomplete, including vendor agents | 64.2009(b) | Moderate | Annual CPNI training; CPNI sanctions in POL-01 | HR Manager | 2026-10-31 |
| Account change notices missing | 64.2010(f) | Moderate | Notices for all four change types to the number or address of record | Billing Manager | 2026-11-30 |
| PSAP contacts not confirmed annually | 4.9(h)(1) | Moderate | Confirm all contacts | NOC Manager | 2026-09-30 |

The full list with evidence is in `gap-analysis.csv`. High and Moderate gaps are carried into the risk register (P01) and, where a control was tested, the POA&M (P07).

## 5. Pending regulatory changes
- **64.2011 amendments (delayed indefinitely).** Once the FCC announces an effective date, these changes would apply to the company. The FCC would be notified along with the USSS and FBI within 7 business days. "Breach" would cover PII as well as CPNI, and inadvertent access would count, not only intentional access. Customer notice would be due within 30 days of reasonable determination, with no 7-day wait. Breaches under 500 customers with no reasonably likely harm would go into an annual summary due February 1 instead. The P08 matrix carries both versions. The procedure (G-029 to G-034) is written so that switching versions is a change to the notification matrix, not a redesign.
- **CIRCIA.** Covered cyber incident reports within 72 hours and ransom payment reports within 24 hours are expected once a final rule is published and effective. None is in effect as of 2026-09-25.
- **Broadband classification.** If broadband is ever reclassified as a telecommunications service, broadband usage data would become CPNI. The whole-account policy in section 1.2 already covers that data.
