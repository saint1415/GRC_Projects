# SOC 2 Readiness Summary: Cris Santos Company | Finance and Insurance | Mid-Market

| Field | Value |
|---|---|
| Organization | Cris Santos Bank, N.A. (regional commercial bank), subsidiary of Cris Santos Company, Inc. |
| Tier / Vertical | Mid-Market / Finance and Insurance |
| Criteria | AICPA 2017 Trust Services Criteria (With Revised Points of Focus, 2022) |
| Categories in scope | Security (CC1-CC9), Availability (A1), Processing Integrity (PI1), Confidentiality (C1) |
| System | Correspondent payment services: wire and ACH processing and settlement for 18 respondent institutions, on the payments hub and correspondent portal (part of the COBP, P02) |
| Target report | SOC 2 **Type 2**, observation period 2027-04-01 to 2027-09-30 (6 months), report expected by 2027-11-30 |
| Part A | Readiness assessment of correspondent services (`soc2-readiness.csv`) |
| Part B | Vendor SOC review program for Tier 1 providers (`vendor-soc2-review.csv`) |
| Prepared | 2026-08-28 by the ISO and the Correspondent Services Director, with the Third-Party Risk Manager, using P02, P05, P06, and P07 evidence; approved by the COO 2026-09-18 |

## 1. Why SOC 2 for this organization
A bank is usually **not** a SOC 2 service organization: its assurance comes from OCC examinations against the Interagency Guidelines (using the FFIEC IT Examination Handbook), internal and external audit, and its service providers' SOC reports. That is still true for the bank's own customers.

**Correspondent services change the picture.** The bank processes and settles wires and ACH for 18 smaller banks and credit unions. For those respondents, the bank is a service provider:
- respondents must oversee the bank under their own regulators' third-party expectations (for bank respondents, the same III.D duties the bank applies to its own providers);
- General Counsel's working view is that the bank owes bank respondents 53.4-type incident notices as a bank service provider (P03 G-042; P08);
- several respondents and their examiners asked in 2026 for an independent report on the bank's controls over the service.

The respondents asked for **Security, Availability, Processing Integrity, and Confidentiality**. Processing Integrity matters because respondents rely on the bank to send complete, accurate, timely payments and settlement statements. Privacy was not requested; GLBA privacy duties for the bank's own customers are handled by its privacy program.

**Why Type 2, and why not now.** A Type 2 report tests operating effectiveness over a period. P07 found High gaps in privileged access, change control, monitoring, and recovery for the very systems in scope (payments hub and portal). Starting the observation period before those are fixed would produce exceptions or a qualified opinion. The plan is to remediate through 2027 Q1 and observe from 2027-04-01.

**Alternatives considered:**
- **Type 1 first (design at a point in time):** offered to respondents as an interim report as of 2027-03-31.
- **SOC 1 (controls relevant to respondents' financial reporting):** some respondents' auditors may want it for settlement processing. It will be considered for 2028 once the SOC 2 is in place; the control set overlaps.
- **Security questionnaires only:** respondents' examiners asked for independent assurance, so questionnaires are not enough.

**Service auditor independence.** The examination will be performed by an independent CPA firm that is **not** the co-sourced IT audit firm that performed P07.

## 2. System description (scope)
| Element | In scope |
|---|---|
| Services | Wire and ACH processing and settlement for respondent institutions; daily settlement statements |
| Infrastructure | Production, shared network, security and log archive, and backup accounts of the landing zone (P04); both wire rooms and the 4 payments workstations |
| Software | Payments hub and correspondent portal; identity provider and customer identity service; SIEM |
| People | Correspondent operations (9), wire rooms (18), IT and security staff, the MSSP |
| Data | Respondents' payment orders and settlement data (Restricted under POL-04) |
| Procedures | POL-01 to POL-05, the standards index, and the P08 runbooks |
| Subservice organizations (carve-out) | Cloud provider, identity provider, MSSP. Their controls are covered by their own SOC 2 reports and the complementary subservice organization controls listed in the bank's system description. The Federal Reserve payment services are an interconnected external system, not a subservice organization |
| Complementary user entity controls (for respondents) | Respondents must request and remove their users promptly, protect their credentials, review settlement statements daily, and give the bank a designated incident contact. These go into the new respondent agreement (POAM-019) |

## 3. Readiness results (Part A)
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33 criteria) | 14 | 14 | 5 | 0 |
| Availability (A1, 3) | 1 | 1 | 1 | 0 |
| Confidentiality (C1, 2) | 1 | 1 | 0 | 0 |
| Processing Integrity (PI1, 5) | 2 | 3 | 0 | 0 |
| Privacy (P1-P8, 18) | 0 | 0 | 0 | 18 |
| **Total (61)** | **18** | **19** | **6** | **18** |

**Ready (18):**
- governance and risk: CC1.1, CC1.3, CC1.5, CC2.2, CC3.2, CC3.3;
- monitoring: CC4.1, CC4.2;
- control design: CC5.1;
- access, boundary, transmission, and malware: CC6.4, CC6.5, CC6.6, CC6.7, CC6.8;
- capacity: A1.1;
- disposal: C1.2;
- input and output integrity: PI1.2 (field validation and sanctions screening), PI1.4 (daily settlement statements reconciled to the Federal Reserve account).

**Not ready (6):**
- CC2.3: no service commitments or designated contacts with respondents;
- CC6.3: payments hub administrators with full rights; generic portal accounts outside reviews;
- CC7.2: payments hub and portal events not monitored;
- CC7.5 and A1.3: failover took 9 hours against a 4-hour RTO, and there has been no test since;
- CC8.1: payments hub configuration changes made by one administrator outside change control.

Each maps to a P07 POA&M item. The pattern matches P03 and P07: the bank's general controls are sound, but **the payments hub and portal sit outside the strongest controls, and the service commitments have never been written down**.

**Mapping to other work.** Evidence is reused from P02 (control statements), P05 (RTO 4 h and RPO 15 min for BP-02), P06 (policies and standards), P07 (test results), and P08 (respondent notices). The `related_sp800_53` column links each criterion to the P02 controls. AICPA publishes a TSC-to-SP 800-53 mapping (see SRC-TSC).

## 4. Remediation plan and evidence calendar
| Quarter | Criteria addressed | Evidence to start collecting |
|---|---|---|
| 2026 Q4 | CC1.2, CC3.4, CC5.2, CC7.1, CC7.3, CC7.4, CC8.1, PI1.3, C1.1 | Board-adopted tolerances; payments hub configuration baseline; dual approval records; change tickets for limit changes; single incident register; tabletop report; respondent contact list; data inventory reconciliation |
| 2027 Q1 | CC1.4, CC2.1, CC2.3, CC3.1, CC5.3, CC6.1, CC6.2, CC6.3, CC7.2, CC7.5, CC9.1, CC9.2, A1.2, A1.3, PI1.1, PI1.5 | New respondent agreements; system description; PAM logs; quarterly portal access reviews; SIEM use-case tickets; failover test within 4 hours; full restore records; standards; Tier 1 vendor reviews |
| 2027-03-31 | Type 1 (design) report as an interim deliverable to respondents | Management's system description and assertion |
| 2027-04-01 to 2027-09-30 | Type 2 observation period | All recurring control evidence (quarterly reviews, monthly scans, semiannual failover test, daily reconciliations, vendor reviews) |

**Status reporting.** The Correspondent Services Director reports readiness monthly to the COO and quarterly to the Board Risk Committee; respondents receive a quarterly status letter.

## 5. Vendor SOC review program (Part B)
The bank relies on provider controls for many inherited controls (P02: 8 Common/Inherited and 36 Hybrid). The Guidelines require the bank to oversee service providers and, where the risk assessment indicates, review audits or summaries of test results (12 CFR 30 App. B III.D.3; P03 G-026). The program in `vendor-soc2-review.csv` makes that reliance evidence-based and is the core of STD-03.

**Tiering approach:**
| Tier | Criteria | Assurance required | Frequency |
|---|---|---|---|
| **Tier 1** | Customer information at scale, a critical service (a High BIA process), privileged access to bank systems, or a bank service provider under 12 CFR 53.4 | SOC 2 Type 2 (and SOC 1 where financial reporting relies on it) or an equivalent independent assessment, plus bridge letter; review of opinion, scope, subservice organizations, exceptions, CUECs mapped to bank controls, availability against the BIA, and incident terms | Annually |
| **Tier 2** | Limited customer information, no privileged access, supports Moderate or Low processes | Security questionnaire; SOC 2 if available | Every 2 years |
| **Tier 3** | No customer information and no system access | Contract terms only | At renewal |

Of about 260 third parties, 34 are Tier 1 and 71 are Tier 2. The CSV holds the first 8 Tier 1 reviews completed in 2026 (through 2026-08-28). The remaining 26 Tier 1 reviews are due by 2027-03-31 (POAM-015).

**Key findings:**
1. **Core processor:** unmodified SOC 1 and SOC 2 Type 2 reports. The stated RTO of 4 hours and RPO of 15 minutes meet the BIA but are not in the contract (R-003). Two of the CUECs the bank must operate are open gaps: core user reviews against role templates (POAM-001) and security report review (POAM-005). **The processor's controls only protect the bank once those gaps close.**
2. **Payments hub vendor:** no SOC 2 report. Its implementation left the generic administrator accounts found in P07 (R-049), and its support uses a standing VPN (R-048). A SOC 2 Type 2 or equivalent will be required at the 2027 renewal.
3. **MSSP:** unmodified Type 2 (Security only) with an exception for missed 30-minute escalations in 2 of 40 samples; the SIEM platform is carved out and its own report must be obtained (R-037).
4. **53.4 contacts:** the core processor, digital banking provider, and card processor have the bank's designated contacts; the AML monitoring provider and 3 other bank service providers do not yet (due 2026-10-31).
5. **Incident terms:** notice commitments range from "without undue delay" (core processor) to 24 hours (digital banking provider, card processor). STD-03 sets a target of 24 hours for Tier 1 vendors at renewal.
