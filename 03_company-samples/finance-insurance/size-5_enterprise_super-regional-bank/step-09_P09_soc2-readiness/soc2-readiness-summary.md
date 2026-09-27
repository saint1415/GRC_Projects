# SOC 2 Readiness Summary: Cris Santos Company | Finance and Insurance | Enterprise

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (publicly traded bank holding company); services delivered by Cris Santos Bank, N.A. |
| Tier / Vertical | Enterprise / Finance and Insurance |
| Criteria | AICPA 2017 Trust Services Criteria (With Revised Points of Focus, 2022) |
| Service lines | SL-1 commercial treasury management and payments services (about 41,000 commercial clients, including about 120 corporate clients on host-to-host and API channels); SL-2 institutional trust, custody, and retirement plan services |
| Categories in scope | SL-1: Security, Availability, Confidentiality (new), and Processing Integrity (new). SL-2: Security, Availability, Confidentiality, and Privacy |
| Target reports | SL-1: Type 2, period 2027-01-01 to 2027-12-31 (third annual report; Confidentiality and Processing Integrity added). SL-2: first Type 2, period 2027-04-01 to 2027-09-30 |
| Files | `soc2-readiness.csv` (every criterion for each service line: 122 rows); `soc2-evidence-map.csv` (25 evidence items) |
| Prepared | 2026-08-28 by the GRC team with the service line owners; reviewed by the CISO and the Chief Audit Executive |

## 1. Why SOC 2 (or an alternative) for this organization
Most of the bank's assurance comes from examinations, not SOC reports: the OCC and the Federal Reserve examine the bank and the parent using the FFIEC IT Examination Handbook, and the bank relies on SOC 1 reports from its own service providers. Two service lines are different, because the bank **provides services to other businesses** that ask for a CPA's report on controls:
- **SL-1 commercial treasury management and payments.** Corporate clients connect their enterprise systems to the bank through host-to-host file channels and APIs, and their auditors and vendor risk teams ask for SOC 2. SL-1 has issued a SOC 2 Type 2 report (Security, Availability) since 2025; the 2025 report had no exceptions. Large clients now ask for Confidentiality (their payment and account data) and Processing Integrity (complete, accurate, timely payments).
- **SL-2 institutional trust, custody, and retirement plans.** The bank already issues a SOC 1 Type 2 report on controls relevant to clients' financial reporting. Plan sponsors and institutional clients now ask for SOC 2 covering security, availability, confidentiality, and the privacy of plan participants' personal information.

**Alternatives considered:** examinations are not shareable with clients; a SOC 1 covers financial reporting controls only; industry questionnaires do not give independent assurance. SOC 2 answers what clients ask, and the enterprise common controls (P02 section 10.3; P04 section 5) let one evidence set serve both reports, the SOX program, and examinations.

**Relationship to other assurance:** the cloud providers, the treasury platform vendor, the trust platform vendor, and the sub-custodian are subservice organizations presented with the carve-out method; their own SOC reports are reviewed under CC9.2 with complementary user entity controls mapped. SL-2 processing accuracy stays in the SOC 1 Type 2 report, so Processing Integrity is out of scope for SL-2's SOC 2.

## 2. System description (scope)
| Element | SL-1 commercial treasury management and payments | SL-2 institutional trust, custody, and retirement plans |
|---|---|---|
| Services | Commercial online banking, wire and ACH initiation, positive pay, host-to-host and API payment channels, balance reporting | Trust accounting, custody, retirement plan recordkeeping, participant portal and service center |
| Infrastructure | Treasury platform (vendor SaaS); API gateway on Cloud provider A; payments hub and core in DC-1 and DC-2 (P02, P04) | Trust platform (vendor SaaS); participant portal; core and data centers for cash movements |
| Software | Treasury platform; bank-built APIs; payments hub; fraud and sanctions platforms | Trust platform; bank-built participant portal extensions |
| People | Treasury management, payments operations, callback team, fraud operations, Cyber Defense Center | Trust operations, participant service center, Cyber Defense Center |
| Data | Client account, payment, and beneficiary data | Plan, account, and participant personal information (names, Social Security numbers, balances, beneficiaries) |
| Procedures | P06 policy hierarchy; P08 runbook; STD-02.4 payment instruction verification | P06; P08; trust operations procedures |
| Subservice organizations (carved out) | Cloud provider A; treasury platform vendor | Trust platform vendor; sub-custodian; statement and mail vendor |

The acquired bank's legacy commercial platform is **excluded** from SL-1's scope until its clients migrate (due 2027-02-26, POAM-004); SL-1 client communications say so.

## 3. Readiness results
**SL-1 commercial treasury management and payments**
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33) | 28 | 5 | 0 | 0 |
| Availability (A1, 3) | 1 | 2 | 0 | 0 |
| Confidentiality (C1, 2) | 1 | 1 | 0 | 0 |
| Processing Integrity (PI1, 5) | 4 | 1 | 0 | 0 |
| Privacy (P1-P8, 18) | | | | 18 |

**SL-2 institutional trust, custody, and retirement plans**
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33) | 28 | 4 | 1 | 0 |
| Availability (A1, 3) | 2 | 1 | 0 | 0 |
| Confidentiality (C1, 2) | 1 | 1 | 0 | 0 |
| Processing Integrity (PI1, 5) | | | | 5 |
| Privacy (P1-P8, 18) | 12 | 5 | 1 | 0 |

**SL-1** is ready to continue its Type 2 on Security and Availability, with 9 partially ready items, none Not ready: CC3.3, CC6.1, CC6.3, CC7.2, CC9.2, A1.2, A1.3, C1.1, PI1.2. They are the same issues Internal Audit found in P07 and the gap analysis found in P03: beneficiary confirmation below $100,000 (POAM-007), the beneficiary-plus-wire alert (POAM-006), mainframe access (POAM-001, POAM-002), vendor reviews and the treasury vendor's recovery time (POAM-012, POAM-018), and the cyber vault (POAM-020). Items still open when the period starts on 2027-01-01 have compensating controls today (callbacks for large wires, daily beneficiary reports, DC-2 recovery) and would be described in the report; the service auditor may report exceptions for the part of the period before they close.

**SL-2** is not yet ready for a Type 2 period to start. Not ready: CC7.2 (trust platform security events not monitored by the bank) and P6.7 (no accounting of disclosures for participants). Partially ready: CC2.3, CC3.1, CC6.1, CC9.2, A1.3, C1.2, P3.2, P4.2, P4.3, P5.1, P6.2. Closing CC7.2, the system description (CC2.3, CC3.1), and participant MFA (CC6.1) by 2027-03-31 makes SL-2 ready to start its period on 2027-04-01. P4.3, P6.2, and P6.7 close by 2027-06-30 with manual compensating procedures in place until then.

## 4. Remediation plan and evidence calendar
| Quarter | Criteria addressed | Actions | Evidence to start collecting |
|---|---|---|---|
| 2026 Q4 | SL-1 CC7.2, CC9.2; SL-2 CC9.2 | Beneficiary-plus-wire alert (POAM-006); core events to the SIEM (POAM-003); SOC review backlog and CUEC mapping (POAM-012) | Alert records; SIEM source list; SOC review files |
| 2027 Q1 | SL-1 CC3.3, PI1.2, CC6.1, CC6.3, C1.1, A1.3; SL-2 CC2.3, CC3.1, CC6.1, CC7.2, A1.3, C1.2, P3.2, P4.2, P5.1 | Out-of-band confirmation of every beneficiary (POAM-007); mainframe connector and PAM (POAM-001, POAM-002); secure message channel; full-day treasury fallback test (POAM-018); SL-2 system description; trust platform log feed; participant MFA; consent and request logs | Confirmation records; PAM reports; fallback test report; system description; alert records |
| 2027 Q1 (March) | Readiness check by Internal Audit for both service lines; SL-2 Type 2 period starts 2027-04-01 | Mock walkthrough with the service auditor | Walkthrough results |
| 2027 Q2 | SL-1 A1.2; SL-2 P4.3, P6.2, P6.7 | Cyber vault (POAM-020); automated disclosure log and disposal job | Vault restore test; disclosure log extracts |

**Evidence map.** `soc2-evidence-map.csv` lists each evidence item, its source system, owner, frequency, and the Type 2 sample the service auditor is expected to draw. Items marked "Both" are enterprise common controls collected once and used for both reports. Status: 11 collecting, 6 ready, 8 not started (each tied to a POA&M item or a 2027 Q1 action).

**Client communication:** SL-1 clients receive the 2025 report, a bridge letter, and a letter describing the Confidentiality and Processing Integrity additions; SL-2 clients receive the current SOC 1 Type 2 report, this summary, and the expected SL-2 SOC 2 report date (2027-11).
