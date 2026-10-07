# Regulatory Gap Analysis: Cris Santos Company | Communications | Sole Proprietorship

| Field | Value |
|---|---|
| Organization | Cris Santos Company (owner-operated wireless internet service provider) |
| Tier / Vertical | Sole Proprietorship / Communications |
| Primary regulation | FCC CPNI rules, 47 CFR 64.2001-64.2011 (47 U.S.C. 222), text in force on 2026-09-23 (C-COMMUNICATIONS-R01) |
| Secondary regulations | CALEA system security and integrity rules, 47 CFR 1.20000-1.20008 (C-COMMUNICATIONS-R03); outage rules for interconnected VoIP, 47 CFR 4.9(g), (h) and 4.18 (C-COMMUNICATIONS-R02) |
| Voluntary benchmark | 8 NIST CSF 2.0 outcomes, used to judge the CPNI "reasonable measures" duty (64.2010(a)) |
| Assessment dates | 2026-07-20 to 2026-07-24 (self-assessment) |
| Assessor | Owner-operator, with the on-call network consultant. Evidence is self-attested and checked on screen where possible. Telecommunications counsel reviewed section 1 and searched the FCC filing systems |
| Sources checked | eCFR full text (point in time 2026-09-23) for 47 CFR 1.20002-1.20006, 4.3, 4.5, 4.9, 4.18, 8.1, 9.3, 9.11, 64.2003, 64.2009-64.2011; Federal Register API (70 FR 59664; 71 FR 38091; 89 FR 9968; 89 FR 23644; 90 FR 38406; 91 FR 52251), retrieved 2026-10-05 |
| Adopted | 2026-08-31 |

## 1. Applicability
### 1.1 The CPNI rules apply, but only because of the home phone add-on
The CPNI rules bind "telecommunications carriers," and the definition "shall include an entity that provides interconnected VoIP service, as that term is defined in section 9.3" (47 CFR 64.2003(o)). The home phone add-on is real-time two-way voice that needs a broadband connection and IP-compatible equipment (the ATA) and lets users call the public telephone network, which is the 9.3 definition. The company sells it under its own name, sets the price, bills it, and supports it, so the company provides it, even though a wholesale platform does the switching. Counsel agreed with this reading on 2026-07-24.

**The test is the service, not the size.** There is no size threshold or small-carrier exemption in 64.2001-64.2011. If the company dropped the home phone add-on and sold only broadband, the CPNI rules would not apply at all (section 1.2). Keeping 58 VoIP lines brings every Subpart U duty with it, including the annual officer certification that the company has never filed (G-019).

### 1.2 Broadband data is not CPNI today
CPNI is information about "a telecommunications service" a customer buys, plus information in bills for telephone exchange or toll service (47 U.S.C. 222(h)(1)). The Sixth Circuit set aside the FCC's 2024 order that reclassified broadband as a telecommunications service (*Ohio Telecom Ass'n v. FCC*, decided 2025-01-02), and the FCC conformed its rules effective 2025-08-08 (90 FR 38406). Broadband is an information service, so the company's broadband usage data (IP assignments, data usage, speed tier, NAT logs) is **not CPNI**. Broadband data practices fall under FTC Act Section 5 instead. By policy (POL-01 8.1) the company protects the whole account record at the CPNI level, because the billing platform keeps one record per customer.

### 1.3 The 2023 breach amendments are not in effect
The FCC's 2023 Data Breach Reporting Order (89 FR 9968) amended 64.2011, but those amendments are "delayed indefinitely," and the Sixth Circuit denied review on 2025-08-13. No effective-date notice was found in the Federal Register through 2026-10-05, and the eCFR text current through 2026-09-23 still shows the original 64.2011. This analysis and the P08 runbook use the **current** rule. The amendments are shown in the `pending_rule_change` column only. If they take effect, the exemption for breaches affecting fewer than 500 customers with no reasonably likely harm would matter here, since the company has 52 home phone accounts.

### 1.4 Secondary regulations
| Regulation | Applies? | Basis |
|---|---|---|
| **CALEA SSI rules**, 47 CFR 1.20000-1.20008 | **Yes** | The FCC's 2005 First Report and Order (70 FR 59664, effective 2005-11-14) found that "providers of facilities-based broadband Internet access services and providers of interconnected voice over Internet Protocol (VoIP) services" must comply with CALEA, under the substantial replacement provision now reflected in 47 CFR 1.20002(e)(3). The company owns its radio network, so it is a facilities-based broadband provider, and it provides interconnected VoIP. The 2006 Second Report and Order (71 FR 38091) required these providers to file their system security policies within 90 days. That order noted a pending proposal to exempt small and rural broadband providers, but the current rules contain no exemption. Coverage rests on the CALEA definitions, not on the Title II classification in section 1.2. The FCC's January 2025 ruling reading CALEA as a general cybersecurity duty was rescinded on 2025-11-20 (90 FR 58006) |
| **Outage reporting for interconnected VoIP**, 47 CFR 4.9(g), (h); 4.18 | **Yes, with thresholds that are hard to reach** | Interconnected VoIP providers are covered "facilities-based or non-facilities-based" (4.3(h)). The notification triggers need 900,000 user minutes, which 58 lines would reach only after more than 10 days of total outage. The annual 911 special facility contact confirmation in 4.9(h)(1) still applies (G-044). Whether the DIRS duty in 4.18 reaches a reseller of VoIP is unclear (G-045). The wireline and wireless sections do not apply: the company is neither a wireline provider (4.3(g)) nor a CMRS provider (4.3(f)) |
| Broadband transparency and consumer labels, 47 CFR 8.1 | Yes (not a security rule) | Applies to "any person providing broadband internet access service." Labels are posted. The 2026 label order (91 FR 52251, effective 2026-09-14) eases some label requirements; the owner updates the labels when counsel confirms what changed. Not analyzed further here |
| Interconnected VoIP 911, 47 CFR 9.11 | Yes (not a security rule) | 911 service and registered locations for the home phone lines are delivered through the wholesale provider. The accuracy of registered addresses is tracked as P01 R-014 |
| CIRCIA (C-COMMUNICATIONS-R05) | **Not yet** | No final rule published as of 2026-10-05. The proposed rule's communications criterion lists fixed wireless service providers, VoIP providers, and internet service providers without a size limit, so the company expects to be covered |
| SEC disclosure rules (C-COMMUNICATIONS-R06) | No | No securities; not an Exchange Act registrant |
| Submarine cable rules (C-COMMUNICATIONS-R04) | No | No cable landing license |
| Florida breach law, Fla. Stat. 501.171 | Yes | Applies to personal information of Florida residents (for example, portal user names with passwords). Call detail alone may not be personal information under 501.171; see P08 |

### 1.5 Why a voluntary benchmark is included
No FCC rule sets general network security controls for a WISP. The CPNI rules require "reasonable measures to discover and protect against attempts to gain unauthorized access to CPNI" (64.2010(a)) without saying what they are. The company uses 8 NIST CSF 2.0 outcomes, chosen for the P08 intrusion path, as its yardstick (G-046 to G-053).

## 2. Method
1. **Requirements.** Each paragraph of 47 CFR 64.2005-64.2011 that imposes, permits, or limits conduct is one row, cited to the paragraph (public-domain text; short quotes only). Rows reuse the requirement set verified for this vertical's Small sample. CALEA and Part 4 rows follow the same method.
2. **Crosswalk.** CSF 2.0 and SP 800-53 columns for the regulatory rows are an **author mapping**; NIST has published no official mapping for 47 CFR Parts 1, 4, or 64. The benchmark rows use NIST's official CSF 2.0 to SP 800-53 reference mapping (a selection of the listed controls).
3. **Evidence.** Self-attested by the owner and checked on screen with the network consultant: SaaS settings, router configuration, an external port check (2026-07-23), a test of the AI support assistant from a phone that was not the number of record (2026-07-22), and counsel's search of the FCC's CPNI certification docket and CEFS.
4. **Status.** Met, Partially met, Not met, or Not applicable. Gap risk uses the P01 scale (Very Low to Very High).

## 3. Results summary
| Requirement set | Rows | Met | Partially met | Not met | N/A |
|---|---|---|---|---|---|
| FCC CPNI rules (47 U.S.C. 222(a); 64.2005-64.2011) | 34 | 5 | 6 | 8 | 15 |
| CALEA SSI rules (47 CFR 1.20000-1.20006) | 8 | 0 | 3 | 5 | 0 |
| Outage rules for interconnected VoIP (47 CFR 4.9(g), (h); 4.18) | 3 | 1 | 1 | 1 | 0 |
| NIST CSF 2.0 benchmark (voluntary) | 8 | 0 | 6 | 2 | 0 |
| **Total** | **53** | **6** | **16** | **16** | **15** |

Of the 32 partially met or not met rows, 6 are rated **High**, 17 **Moderate**, and 9 **Low**. Three High rows are CPNI rules (64.2009(e) certification, 64.2010(a) reasonable measures, 64.2010(c) online authentication); three are benchmark outcomes (vulnerability identification, firmware, and the management plane).

**Why 15 rows are not applicable.** The approval and notice rules (64.2007, 64.2008, 64.2009(d), (f)) apply only when a carrier uses CPNI for purposes that need customer approval, mainly marketing. The company uses CPNI only to provide, bill, and protect the home phone service. The other N/A rows are the in-store, business customer, and CMRS rules.

**What is working:** customer portal passwords and the phone callback practice already meet 64.2010(b), (c), and (e); CPNI is not used for marketing; the VoIP provider covers 911 routing and VoIP intercepts.

## 4. Action list (half page)
In order. The first four cost little and take under a day each.

| # | Action | Citation | Gap risk | Target |
|---|---|---|---|---|
| 1 | Router firmware update and management filters (management VLAN and VPN only) | 64.2010(a); CSF PR.IR-01, PR.PS-02 | High | 2026-09-15 |
| 2 | MFA on the VoIP reseller portal; password manager | 64.2010(a); CSF PR.AA-01 | High | 2026-09-15 |
| 3 | AI assistant shows CPNI only inside a signed-in portal session; account change notices for email and address | 64.2010(c), (f) | High | 2026-10-31 |
| 4 | Adopt the P08 runbook; locate the FCC reporting facility and FBI and USSS contacts; start the CPNI breach record | 64.2011; 1.20003(c) | Moderate | 2026-09-30 |
| 5 | Confirm the county 911 center outage contact; set a yearly reminder | 4.9(h)(1) | Low | 2026-10-31 |
| 6 | Vendor and advisory tracking; monthly external port check | CSF ID.RA-01, GV.SC-07 | High | 2026-10-31 |
| 7 | Write and file CALEA policies with a 24x7 appendix through CEFS | 1.20003; 1.20005 | Moderate | 2026-11-30 |
| 8 | CPNI course for the owner; sanctions and consultant CPNI clause | 64.2009(b) | Moderate | 2026-11-30 |
| 9 | Broadband intercept arrangement (trusted third party or vendor feature) | 1.20006 | Moderate | 2026-12-31 |
| 10 | With counsel, address the missed certifications and file the calendar year 2026 certification with an accurate statement | 64.2009(e) | High | 2027-03-01 |

High and Moderate gaps are in the risk register (P01: R-001 to R-008) and, where a control was tested, the POA&M (P07).

## 5. Pending regulatory changes
- **64.2011 amendments (delayed indefinitely).** If the FCC announces an effective date, the FCC would join the USSS and FBI as a recipient within 7 business days, "breach" would cover PII and inadvertent access, customer notice would be due within 30 days with no 7-day wait, and breaches under 500 customers with no reasonably likely harm would go into an annual summary instead. The P08 matrix carries both versions.
- **CIRCIA.** Covered cyber incident reports within 72 hours and ransom payment reports within 24 hours are expected once a final rule is published and effective. None is in effect as of 2026-10-05.
- **Broadband classification.** If broadband were reclassified as a telecommunications service, broadband usage data would become CPNI and the CPNI rules would reach every subscriber, not only the 52 home phone accounts. POL-01 8.1 already protects the whole account record to that standard.
