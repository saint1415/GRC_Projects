# Regulatory Gap Analysis: Cris Santos Company | Communications | Mid-Market

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (PE-backed regional broadband and wired telecommunications carrier) |
| Tier / Vertical | Mid-Market / Communications |
| Primary regulation | FCC CPNI rules, 47 CFR 64.2001-64.2011 (47 U.S.C. 222), text in force on 2026-09-23 (C-COMMUNICATIONS-R01) |
| Other rules for the primary business line | CALEA SSI rules, 47 CFR 1.20000-1.20008 (C-COMMUNICATIONS-R03); FCC outage reporting, 47 CFR Part 4 (C-COMMUNICATIONS-R02); 911 reliability, 47 CFR 9.19-9.20; caller ID authentication and robocall mitigation, 47 CFR 64.6301-64.6305; Secure Networks Act reporting, 47 CFR 1.50007 |
| Voluntary benchmark | NIST CSF 2.0, with the CISA Cross-Sector Cybersecurity Performance Goals (CPGs) as the prioritized practice list |
| Assessment dates | 2026-07-06 to 2026-07-31; evidence refreshed with P07 results through 2026-08-21 |
| Assessor | GRC analyst and the Security Manager with the Vice President of Regulatory Affairs; outside telecommunications regulatory counsel reviewed section 1; reviewed by the co-sourced internal audit firm |
| Sources checked | eCFR full text (point in time 2026-09-23) for 47 CFR 1.20000-1.20008, 1.50001-1.50007, 4.9, 4.18, 9.19, 9.20, 64.2005-64.2011, 64.6301-64.6305; Federal Register API (through 2026-10-05); FCC 26-39 (91 FR 42794) full text on govinfo |
| Approved | Chief Operating Officer, 2026-09-17 |

## 1. Applicability

### 1.1 The CPNI rules apply, through the voice services
The CPNI rules bind "telecommunications carriers," defined by reference to 47 U.S.C. 153, and include "an entity that provides interconnected VoIP service" (47 CFR 64.2003(o)). The company is covered three ways: local exchange and toll service over copper (a telecommunications service), interconnected VoIP over fiber (54,500 lines), and the hosted voice seats in Business Services, which are interconnected VoIP. The merged CLEC's voice customers billed in SYS-18 are covered too.

There is **no size threshold or small-carrier exemption** in 64.2001-64.2011. The only carve-outs are service-specific: 64.2010(h) applies only to CMRS providers (none here), and 64.2008(d)(3) applies only to carriers that send opt-out notices by email (the company mails them).

### 1.2 Broadband is outside the CPNI rules today
CPNI is information about "a telecommunications service subscribed to by any customer of a telecommunications carrier" plus information in bills for telephone exchange or toll service (47 U.S.C. 222(h)(1)). In **Ohio Telecom Ass'n v. FCC** (6th Cir., decided 2025-01-02, No. 24-7000), the court held that broadband providers offer only an information service and set aside the FCC's 2024 reclassification order. The FCC conformed the CFR on 2025-08-08 (90 FR 38406). No later reclassification was found in the Federal Register through 2026-10-05.

**Result:** broadband usage and configuration data is **not CPNI**, and the Subpart U safeguards do not attach to it as such. Two consequences:
1. Broadband is a "communications-related service" for marketing purposes (64.2003(e), (i)). Using voice CPNI to sell broadband to a voice customer needs opt-out or opt-in approval (64.2007(b)). This is gap G-007 (the churn model and chatbot offers).
2. The BSS keeps one record per customer, so **by policy (POL-04) the company protects the whole customer account record to the CPNI standard.** Broadband data practices remain subject to FTC Act Section 5, which excludes only common carriers subject to the Communications Act (15 U.S.C. 45(a)(2)); counsel reads that exclusion as limited to the company's common carrier services.

### 1.3 Status of the 2023 breach amendments to 64.2011
- The FCC's 2023 Data Breach Reporting Order (FCC 23-111, 89 FR 9968, 2024-02-12) took effect 2024-03-13 **except** the amendments to 64.2011, which are "delayed indefinitely" until the FCC publishes an effective-date notice.
- The Sixth Circuit **denied** the petitions for review on 2025-08-13 (Ohio Telecom Ass'n v. FCC, Nos. 24-3133/3206/3252), upholding the rules under 47 U.S.C. 201(b) while holding that 222(a) does not reach customer PII.
- No effective-date notice was found in the Federal Register through 2026-10-05, and the eCFR text for 2026-09-23 still shows the original 64.2011.

**Result:** this analysis and the P08 runbooks use the **current** 64.2011 (law enforcement notice through the FCC reporting facility within 7 business days, then a 7-full-business-day hold before customer notice). The company's 2024 incident response plan had applied the amended text as if it were in effect; that error is gap G-029 to G-031. The amended text is shown in the `pending_rule_change` column and section 6, and is **not** treated as a current obligation.

### 1.4 Other rules for the primary business line
| Regulation | Applies? | Basis |
|---|---|---|
| **CALEA SSI rules**, 47 CFR 1.20000-1.20008 (C-COMMUNICATIONS-R03) | **Yes** | Local exchange service as a common carrier for hire (47 U.S.C. 1001(8)(A)). The FCC's January 2025 declaratory ruling reading CALEA section 105 as a general cybersecurity duty was **rescinded** on 2025-11-20 (FCC 25-81, 90 FR 58006); the codified SSI rules remain. The 2025-07-01 merger of the CLEC entity triggered the 90-day refiling duty in 1.20005(a) (G-041) |
| **Outage reporting**, 47 CFR Part 4 (C-COMMUNICATIONS-R02) | **Yes** | Wireline provider (4.3(g)) and interconnected VoIP provider (4.3(h)), including hosted voice. Thresholds are outage-based, not size-based. PSAP notification under 4.9(h) also applies because the company is a covered 911 service provider (rows G-043 to G-046) |
| **911 reliability**, 47 CFR 9.19-9.20 | **Yes** | Five central offices are "the last service-provider facility through which a 911 trunk or administrative line passes before connecting to a PSAP," so the company "operates one or more central offices that directly serve a PSAP" (9.19(a)(4)(i)(B)). FCC 26-39 (91 FR 42794, effective 2026-08-10) **eliminated the annual certification**: providers that filed annual certifications under the 2013 rules stay subject to the legacy benchmarks and file a one-time certification 18 months after a compliance-date notice that had not been published as of 2026-10-05. The legacy benchmarks for circuits, backup power, and monitoring (9.19(c)(1)(ii), (c)(2)(ii), (c)(3)(ii)) apply now (rows G-047 to G-052) |
| **Caller ID authentication and robocall mitigation**, 47 CFR 64.6301-64.6305 | **Yes** | Voice service provider. The small voice service provider extension (64.6304(a), 100,000 or fewer lines) expired on 2023-06-30, so it does not matter that the company has about 74,000 lines (rows G-053 to G-057) |
| **Secure Networks Act reporting**, 47 CFR 1.50007 | **Yes** | Provider of advanced communications service (1.50001(a)). The company certified in 2022 that it has no covered equipment (1.50007(c)), so it files no annual report unless it later obtains covered equipment (row G-058) |
| CIRCIA (C-COMMUNICATIONS-R05) | **Not yet** | No final rule published as of 2026-10-05. Counsel reads the proposed communications-sector criteria as likely to cover the company once a rule is final; until then, reporting to CISA is voluntary |
| SEC disclosure rules (C-COMMUNICATIONS-R06) | No | Privately held; not an Exchange Act registrant |
| Submarine cable rules (C-COMMUNICATIONS-R04) | No | No cable landing license or SLTE |
| EAS rules | No | No video or broadcast service |
| Fla. Stat. 501.171 (breach notification) | Yes, in P08 | Handled in the P08 notification matrix, not as gap rows |

### 1.5 Why a voluntary network security benchmark is included
No FCC rule sets general cybersecurity controls for a wireline carrier's network. The CPNI rules require "reasonable measures to discover and protect against attempts to gain unauthorized access to CPNI" (64.2010(a)) but do not say what those measures are. The company uses **NIST CSF 2.0** as the yardstick for "reasonable measures," prioritized by the **CISA CPGs** (version 2.0, which CISA aligns to CSF 2.0). Rows G-059 to G-072 record the 14 CSF 2.0 outcomes most relevant to the P08 scenarios. CPG goals are referenced by theme only (MFA, patching known exploited vulnerabilities, segmentation, logging, backups, third-party risk, incident planning); no CPG goal numbers are cited.

## 2. Method
1. **Requirements.** Each paragraph of 47 CFR 64.2005-64.2011 that imposes, permits, or limits conduct became one row, cited to the paragraph (public-domain text; short quotes only). The CALEA, Part 4, Part 9, caller ID authentication, and Secure Networks Act rows follow the same method, limited to the paragraphs that apply to the company.
2. **Crosswalk.** Each regulatory row is mapped to CSF 2.0 and SP 800-53 Rev. 5. This is an **author mapping**; NIST has published no official mapping for 47 CFR Parts 1, 4, 9, or 64. The benchmark rows use NIST's official CSF 2.0 to SP 800-53 reference mapping (a selection of the listed controls).
3. **Evidence.** Interviews with every rule owner (Vice President of Regulatory Affairs, CTO, Vice President of Network Operations, NOC Director, Director of Network Engineering, Director of Customer Operations, Marketing Director, Billing Director, Director of Business Services, HR Director); configuration exports; filings; live tests of the portal, the chatbot, and the SYS-18 reset (2026-07-22 and 2026-07-23); walkthroughs of CO-1, CO-4, CO-6, POP-A, and 4 cabinets (2026-07-21 to 2026-07-23).
4. **Evidence sampling.** Where a requirement operates many times, a random sample was tested from a system-generated population, using the co-sourced internal audit firm's attribute sampling table (25 items for a control operating many times a year; all items for small populations):

| Population | Size | Sample | Rows | Result |
|---|---|---|---|---|
| Recorded care calls with call detail requests, July 2026 (in-house) | 920 | 25 | G-022 | 25 of 25 compliant |
| Recorded care calls with call detail requests, July 2026 (overflow vendor) | 220 | 25 | G-022 | 23 of 25 compliant |
| SYS-01 account changes (password, backup answer, online account, address), June 2026 | 4,860 | 25 | G-026 | 25 of 25 notified |
| SYS-18 account changes, 2026 Q2 | 74 | 10 | G-026 | 0 of 10 notified |
| Customer accounts (approval records) | about 198,000 | 25 | G-005 | 25 of 25 |
| Campaigns using CPNI, 12 months | 14 | 14 | G-017, G-018 | 11 recorded; 12 approved |
| In-store CPNI transactions, July 2026 | 610 | 15 | G-024 | 15 of 15 |
| Business exemption contracts | 320 | 20 | G-027 | 20 of 20 |
| Intercept records, 12 months | 31 | 10 | G-035, G-040 | 10 of 10 |
| NORS filings, 12 months | 6 | 6 | G-043 | 6 of 6 on time |
| PSAP notification events, 12 months | 9 | 9 | G-045 | 8 of 9 within 30 minutes |
| Legacy 911 circuit pairs | 14 | 14 | G-048 | 14 tagged; 12 diverse |
| Generator full-load tests at PSAP-serving offices, 2026 | 5 | 5 | G-049 | 4 of 5 passed |
| Traceback requests, 12 months | 18 | 18 | G-055 | 16 of 18 within 24 hours |

Each `evidence` cell names the sample and its result.
5. **Status.** Met, Partially met, Not met, or Not applicable. Gap risk uses the P01 scale (Very Low to Very High).

## 3. Results summary
| Requirement set | Rows | Met | Partially met | Not met | N/A |
|---|---|---|---|---|---|
| FCC CPNI rules (47 U.S.C. 222(a); 64.2005-64.2011) | 34 | 11 | 19 | 2 | 2 |
| CALEA SSI rules (47 CFR 1.20000-1.20006) | 8 | 4 | 2 | 2 | 0 |
| Outage reporting (47 CFR Part 4) | 4 | 2 | 2 | 0 | 0 |
| 911 reliability (47 CFR 9.19-9.20) | 6 | 2 | 4 | 0 | 0 |
| Caller ID authentication and robocall mitigation (64.6301-64.6305) | 5 | 2 | 2 | 1 | 0 |
| Secure Networks Act reporting (1.50007) | 1 | 0 | 1 | 0 | 0 |
| NIST CSF 2.0 benchmark (voluntary) | 14 | 2 | 12 | 0 | 0 |
| **Total** | **72** | **23** | **42** | **5** | **2** |

Of the 47 partially met or not met rows, 12 are rated **High**, 25 **Moderate**, and 10 **Low**. The High rows are three CPNI authentication and safeguard rules (64.2010(a), (b), (c)), three 911 reliability rows (9.19(b), (c)(1)(ii), (c)(2)(ii)), and six benchmark outcomes (vulnerability identification, patching, identities, least privilege, network protection, monitoring).

The five **Not met** rows: G-003 (churn model used CPNI to identify customers who call competitors, 64.2005(b)(2)); G-030 (no tested access to the FCC reporting facility, 64.2011(b)); G-038 (stale CALEA contact appendix, 1.20003(b)(4)); G-041 (CALEA policies not refiled after the merger, 1.20005(a)); G-057 (RMD filing not updated within 10 business days, 64.6305(d)(5)).

**What is working:** approval and opt-out mechanics in the BSS, the business customer exemption contracts, in-store photo ID, portal authentication, lawful-intercept activation and records, wireline NORS reporting, DIRS, STIR/SHAKEN, and diverse 911 monitoring. These are the strengths of a carrier that has run regulated voice for decades. The gaps cluster where the company has changed: the CLEC merger (SYS-18, CALEA refiling, POP contacts), new AI channels (chatbot, churn model, agent assist), and the network management plane.

## 4. Priority gaps
| Gap | Citation | Risk | Action | Owner | Target |
|---|---|---|---|---|---|
| Chatbot fallback accepted SSN4 and service address before showing CPNI (disabled 2026-07-24) | 64.2010(c) | High | Sign-in only; review 2,300 sessions with counsel | Director of Customer Operations | 2026-11-30 |
| Overflow agents can release call detail without the password | 64.2010(b) | High | Remove call detail screens from the vendor role; retrain; monthly sampling | Director of Customer Operations | 2026-10-31 |
| Two 911 circuit pairs share a fiber segment | 9.19(c)(1)(ii) | High | Build diverse routes; re-audit | Chief Technology Officer | 2026-12-31 |
| CO-6 generator failed full-load test | 9.19(c)(2)(ii) | High | Transfer switch; re-test; portable generator | Director of Network Engineering | 2026-11-30 |
| Management plane: shared accounts, POP reachability, vendor shared VPN | 64.2010(a); CSF PR.AA-01, PR.AA-05, PR.IR-01 | High | Named TACACS+ accounts with MFA; POP segmentation; access broker for vendors | Director of Network Engineering | 2027-03-31 |
| Network elements not scanned or monitored; late patches | CSF ID.RA-01, PR.PS-02, DE.CM-01 | High | Scanning, 14-day target for critical edge advisories, SIEM onboarding | Security Manager | 2027-01-31 |
| Churn model used CPNI to track calls to competitors; offers ignore approval flags | 64.2005(b)(2); 64.2007(b); 64.2009(a) | Moderate | Feature removed; approval-flag filter; register entries | Marketing Director | 2026-11-30 |
| CALEA policies not refiled after merger; stale contact appendix | 1.20003(b)(4); 1.20005(a) | Moderate | Rewrite and file through CEFS | Vice President of Network Operations | 2026-10-30 |
| CPNI breach procedure: no reporting facility access; hold not exercised | 64.2011(a)-(c) | Moderate | Facility access; tabletop 2026-11-19 | Vice President of Regulatory Affairs | 2026-11-19 |
| SYS-18: no change notices; reset by account information | 64.2010(e), (f) | Moderate | Manual notices; replace or disable reset until migration | Billing Director | 2026-12-31 |
| RMD filing out of date; 2 late tracebacks | 64.6305(a), (d)(5) | Moderate | Update filing; on-call traceback rota | Vice President of Regulatory Affairs | 2026-10-15 |
| Certification statement not evidence-based | 64.2009(e) | Moderate | Evidence-based CY2026 statement; counsel review by 2026-12-15 | Vice President of Regulatory Affairs | 2027-03-01 |
| PSAP contacts stale for POP areas; one late notice | 4.9(h)(1), (4) | Moderate | Confirm all contacts; drill | NOC Director | 2026-10-31 |

The full list with evidence is in `gap-analysis.csv`. High and Moderate gaps are carried into the risk register (P01) and the POA&M (P07: POAM-011, POAM-004, POAM-021, POAM-002, POAM-014, POAM-019, POAM-020, POAM-012, POAM-016, POAM-022).

## 5. Program roadmap
| Phase | Window | Outcomes | Gaps closed (examples) |
|---|---|---|---|
| **1. Stabilize** | 2026 Q4 | RMD updated; CALEA policies refiled; PSAP contacts confirmed; reporting facility access; overflow role fixed and agents trained; vendor shared VPN account disabled; CO-6 transfer switch; churn model approval filter; tabletop 2026-11-19 | G-057, G-038, G-041, G-045, G-030, G-022, G-016, G-049, G-007, G-015 |
| **2. Build** | 2027 Q1 | Named TACACS+ accounts with MFA on all element types; POP segmentation; network element scanning and SIEM onboarding; 911 circuit re-routes; SYS-18 notices; evidence-based CPNI certification filed by 2027-03-01 | G-021, G-048, G-026, G-019; benchmark rows G-062 to G-068 |
| **3. Prove** | 2027 Q2 | Restore tests for every cloud workload; bulk network configuration restore; SYS-18 retired into SYS-01 (2027-06-30); SOC 2 observation period for Business Services begins 2027-04-01 (P09) | G-025, G-006, G-012; benchmark rows G-067, G-072 |
| **4. Sustain** | 2027 Q3-Q4 | Annual risk assessment (July 2027); one-time 911 reliability certification prepared for the compliance-date notice; second independent assessment; vendor reassessments | G-051, G-052, G-060 |

Progress is reported quarterly to the audit committee as the count of rows moving from Partially met or Not met to Met.

## 6. Pending regulatory changes
- **64.2011 amendments (delayed indefinitely).** Once the FCC announces an effective date: the FCC would be notified along with the USSS and FBI within 7 business days; "breach" would cover inadvertent access and customer PII as well as CPNI; customer notice would be due without unreasonable delay and within 30 days of reasonable determination, with no 7-day hold; breaches under 500 customers with no reasonably likely harm would go into an annual summary. The P08 matrix carries both versions, so switching is a change to the matrix, not a redesign.
- **911 reliability (FCC 26-39).** The one-time certification and the attestation under 9.20(a) will be due on timelines set by a future compliance-date notice. The CTO tracks the Federal Register; the evidence folder (G-052) is being built now.
- **CIRCIA.** Covered cyber incident reports within 72 hours and ransom payment reports within 24 hours are expected once a final rule is published and effective. None is in effect as of 2026-10-05.
- **Robocall Mitigation Database NPRM (91 FR 57454, 2026-09-09).** Proposed only; tracked by the Vice President of Regulatory Affairs.
- **Broadband classification.** If broadband is ever reclassified as a telecommunications service, broadband usage data would become CPNI. The whole-account policy in section 1.2 already covers that data.
