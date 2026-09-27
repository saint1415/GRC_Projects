# SOC 2 Readiness Summary: Cris Santos Company | Communications | Small

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (regional broadband and wired telecommunications carrier) |
| Tier / Vertical | Small / Communications |
| Criteria | AICPA 2017 Trust Services Criteria (With Revised Points of Focus, 2022) |
| Categories in scope | Security (CC1-CC9) only, as a self-benchmark. Availability, Confidentiality, Processing Integrity, and Privacy are not in scope (section 1) |
| Target report | None. No SOC 2 examination is planned |
| Part A | Security-only self-benchmark (`soc2-readiness.csv`) |
| Part B | BSS vendor SOC 2 Type 2 report review (`vendor-soc2-review.csv`) |
| Prepared | 2026-08-24 by the IT Manager; accepted by the COO 2026-09-04 |

## 1. Why SOC 2 (or an alternative) for this organization
**The company is not a SOC 2 service organization.** A SOC 2 report describes controls at a service organization whose processing its customers rely on for their own control objectives, such as a SaaS or data processing provider. The company sells transmission: voice calling, broadband, and dedicated Ethernet. Residential customers do not ask for SOC reports. The 40 enterprise and government accounts rely on contract terms (the 99.95% availability SLA and CPNI authentication terms under 47 CFR 64.2010(g)), not on a SOC report. None has asked for one, and the vertical overlay names no sector-specific alternative assurance scheme.

The obligations that do bind the company are regulatory: the CPNI rules, CALEA, and outage reporting (P03). The best evidence for those is the P03 gap analysis, the P07 assessment, and the annual CPNI certification.

**So P09 has two parts:**
- **Part A, a Security-only self-benchmark.** The Common Criteria (CC1-CC9) are a widely understood yardstick. Scoring against them gives leadership and enterprise customers a familiar picture of the security program, and reuses P02, P06, and P07 evidence. If an enterprise or government customer later asks for assurance, the company can answer with this benchmark and the POA&M, or with a security questionnaire. Availability and Confidentiality would be added only if a customer asks.
- **Part B, a vendor SOC 2 review.** Here SOC 2 matters most. The BSS vendor **is** a service organization for the company. Its SOC 2 Type 2 report is the evidence behind the inherited controls in P02 and P04. Reviewing it every year is part of SA-9 and of the "reasonable measures" the CPNI rules require (64.2010(a)).

## 2. System description (scope)
- **Services:** voice (legacy copper and interconnected VoIP), broadband, and dedicated Ethernet for about 64,000 accounts in three Florida counties.
- **Infrastructure and software:** the Network Operations and Customer Billing Platform (OSS/BSS) and its interfaces to the voice core and access network (SSP, P02; architecture, P04).
- **People:** 250 employees and the overflow call center vendor's agents.
- **Data:** CPNI and call detail records, subscriber personal information, network configuration and outage data. Lawful-intercept data is excluded (CALEA SSI plan).
- **Procedures:** POL-01 to POL-05, the P08 runbook, NOC outage procedures, and CPNI operating procedures.

## 3. Readiness results (Part A)
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33 criteria) | 7 | 19 | 7 | 0 |
| Availability (A1, 3) | | | | 3 |
| Confidentiality (C1, 2) | | | | 2 |
| Processing Integrity (PI1, 5) | | | | 5 |
| Privacy (P1-P8, 18) | | | | 18 |

**Ready:**
- CC1.3: roles designated (security lead, CPNI compliance officer, CALEA senior officer)
- CC3.1 and CC3.2: objectives from the BIA; risk assessment done
- CC4.1 and CC4.2: independent assessment and POA&M
- CC6.5: certified disposal
- CC6.7: encryption in transit

**Not ready:**
- CC3.4: no review of significant changes (the chatbot launched without one)
- CC6.1: shared network element accounts, flat management plane, and a customer password reset the CPNI rules prohibit
- CC6.6: unpatched edge routers and an unsupported SBC
- CC7.1, CC7.2, and CC7.3: no vulnerability scanning inside the network, no security monitoring, no event triage
- CC9.2: vendors other than the BSS vendor are unreviewed

These match the High risks in P01 and the High POA&M items in P07. There is no separate SOC 2 remediation track.

## 4. Findings from the BSS vendor report (Part B)
- **Opinion:** Type 2 covering 12 months to 2026-03-31, unqualified, Security plus Availability and Confidentiality. One change management exception at the vendor (2 of 40 changes lacked documented approval), remediated.
- **Availability:** the vendor's stated RTO of 4 hours and RPO of 1 hour **meet the BIA** for customer care (BP-05: RTO 8 h, RPO 1 h). This supports accepting P01 R-023.
- **Controls the company must run.** The report lists complementary user entity controls: user provisioning and removal, federated sign-in with MFA, role assignment, audit and export report review, and configuration of customer authentication and CPNI approval settings. **Three are open gaps at the company:** audit review (POAM-006), customer authentication (POAM-001), and access reviews (POAM-011). The vendor's controls protect CPNI only once those are closed.
- **Follow-ups:**
  - Negotiate 24-hour security incident notice. The current 72-hour term leaves little room for the 7-business-day law enforcement clock (64.2011(b)) and Florida's 10-day third-party agent duty (Fla. Stat. 501.171(6)).
  - Add CPNI-specific terms at renewal (POL-01 4.9).
  - Confirm the vendor reviews its carved-out hosting provider's SOC 2 report.

## 5. Remediation plan and evidence calendar
| Quarter | Criteria addressed | Evidence to start collecting |
|---|---|---|
| 2026 Q4 | CC6.1 (portal reset, network element MFA), CC6.6, CC2.2, CC2.3, CC1.4, CC7.4 | New reset flow test results; TACACS+ accounting; patch records; training and acknowledgment records; reporting facility account; tabletop report |
| 2027 Q1 | CC7.1, CC7.2, CC7.3, CC6.8, CC9.2, CC3.4 | Authenticated scan reports; managed detection alerts and tickets; vendor assurance reports and contract amendments; change review records |
| 2027 Q2 | CC7.5, CC8.1, CC9.1, CC1.2 | Restore test records; cloud change tickets; OSS/BSS recovery plan; quarterly owner review minutes |

**Next self-benchmark:** August 2027, alongside the annual risk assessment, so that the March 2027 CPNI certification and the benchmark draw on the same evidence.
