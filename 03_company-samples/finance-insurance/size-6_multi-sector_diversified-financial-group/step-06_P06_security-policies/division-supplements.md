# Division Supplements to Group Security Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. |
| Authority | POL-01 section 4.6: a supplement may add stricter or division-specific requirements, never weaker ones; it must be re-aligned within 90 days after a group policy changes and attested every year |
| Owner | Each division security and compliance lead; alignment reviewed by the Group CISO |
| Status date | 2026-09-10 (group policies v2026 approved; effective 2026-10-01) |

## 1. How group policy and supplements fit together
| Layer | Examples | Who approves |
|---|---|---|
| Group policy (POL-01 to POL-05) | MFA for all workforce, one severity scale, payment instruction verification in every division, affiliates treated as critical vendors | Holding company board risk committee or Group CISO |
| Group standards | Logging standard, cloud guardrails, callback standard, Group AI Standard (P10) | Group CISO |
| **Division supplement** | Regulator-specific and system-specific standards (for example, OCC notification determinations, bank service provider notices to client banks, CRE funding controls) | Division president, after Group CISO alignment review |
| Division procedures | Runbooks and work instructions | Division security and compliance lead |

## 2. Supplement status
| Division | Supplement version | Last aligned to group policy | Status | Action |
|---|---|---|---|---|
| Banking | v2026 | 2026-06-30 (to the 2026 draft group policies) | Aligned; minor update for the final 2026 policies due by 2026-12-30 (90 days after effective date) | Confirm alignment |
| Financial Software | v2025 | 2025-11 | Aligned, but missing the 4-hour determination step (POL-03 4.5), the tenant-scoped support rule (POL-02 4.2), and a change gate for the data service (POL-01 4.13) | Add by 2026-12-31 (POAM-005, POAM-008, POAM-014) |
| Commercial Real Estate | The acquired company's 2023 policy set | Never | **Not aligned** (scenario gap 2); conflicts listed in section 4 | Re-issue as a group supplement by 2026-11-30 (POAM-017) |

## 3. What each supplement adds
### 3.1 Banking supplement (national bank; OCC covered bank)
| Topic | Division requirement | Group policy it builds on | Driver |
|---|---|---|---|
| Notification incident determination | Criteria for 53.2(b)(7), including incidents that start in affiliates and deliberate platform suspensions; decision recorded with time by the bank determination officials | POL-03 4.4 | 12 CFR 53.3 |
| Wire operations | Callback to independently verified numbers for new beneficiaries over $1 million; out-of-band confirmation from a second customer officer over $5 million; dual control on every wire | POL-02 4.9, 4.13 | App. B III.C.1.a, III.C.1.e |
| Treasury management | Business users must use MFA; staff limit and entitlement changes need re-authentication and a second approver | POL-02 4.4, 4.12 | App. B II.B.3 |
| Contact center | Caller verification before account changes; 48-hour payment hold after a phone or email change | POL-02 4.13 | App. B III.C.1.a (fraudulent means) |
| Affiliates as vendors | The platform division and CRE Lending (as servicer) get annual due diligence, SOC review, and CUEC mapping | POL-01 4.8 | App. B III.D; App. D II.C.1 |
| SARs | Security incidents linked to SAR cases; SAR confidentiality | POL-03 4.8 | 12 CFR 21.11 |
| Risk limit breaches | Cyber and fraud-loss limit breaches reported to independent risk management and, per protocol, the OCC | POL-01 4.4 | App. D II.H |

### 3.2 Financial Software supplement (bank service provider; SOC 1 and SOC 2 service organization)
| Topic | Division requirement | Group policy it builds on | Driver |
|---|---|---|---|
| Client bank notices | A 4-hour determination point in every disruption; notice to each client's designated contact, or to its CEO and CIO; no client go-live without a designated contact | POL-03 4.5 | 12 CFR 53.4; 225.303; 304.24 |
| Contract notice terms | Notice register holds each client's contract notice time (24 hours for 88 clients) | POL-03 4.5 | Client contracts; Supplement A II.A.2 (client banks' guidance) |
| Support console | Tenant-scoped, ticket-linked access; no standing all-tenant access after 2026-12-31 | POL-02 4.2 | SOC 2 CC6.1, CC6.3 |
| Tenant security defaults | Business payment MFA cannot be switched off after 2027-03-31 | POL-02 4.12 | SOC CUECs; client contracts |
| Data service change gate | Attribute and model changes go through the change gate, SOC description impact review, and client notice; developer documentation kept current | POL-01 4.13 | SOC 2 CC3.4, CC8.1; Colorado SB26-189 (under counsel review) |
| Client data use | Client data used only for the contracted service; no cross-client model training without written agreement | POL-04 4.3 | Client contracts |
| Examinations | Cooperate with client banks' federal banking agencies; give new clients a service relationship notice letter | POL-01 4.9 | 12 U.S.C. 1867(c) |

### 3.3 Commercial Real Estate supplement (to be re-issued; nonbank subsidiaries under 12 CFR 225 App. F)
| Topic | Division requirement | Group policy it builds on | Driver |
|---|---|---|---|
| Loan funding | Disbursement instructions only through the secure closing portal or the bank's verified-instruction service; callback to an independently verified number; no instruction changes within 48 hours of closing without the director's approval | POL-02 4.13 | App. F III.C.1.a, III.C.1.e |
| Closer training | Payment-fraud module before handling fundings | POL-05 4.4 | App. F III.C.2 |
| Funding instruction changes | Daily report of changes in the loan system reviewed by a second closer | POL-02 4.9 | App. F III.C.1.f |
| Guarantor data | Closing packages stored in the loan system with state of residence; mailbox copies purged | POL-04 4.4 | State breach laws (generic) |
| Title and escrow agents | Approved agents must use the secure closing portal | POL-01 4.8 | App. F III.D |
| Building systems | Access control and building automation on separate segments; vendor access through PAM | POL-02 4.14 | App. B III.C.1.b (bank's duty) |
| SAR routing | Suspected fraud routed to the nonbank BSA/AML Officer | POL-03 4.8 | 12 CFR 225.4(f) |

## 4. Commercial Real Estate drift: conflicts with 2026 group policy
The acquired company's 2023 policies were never replaced. Where they conflict, **group policy governs now** (POL-01 4.6), but staff follow the document they know, so the conflicts are real risks (P01 RR-005; P07 PL-1 findings).

| Topic | 2023 division policy | Group policy (2026) | Effect |
|---|---|---|---|
| Wire instruction verification | "Confirm changes by phone with the sender" | Callback to an independently verified number (POL-02 4.13) | Closers call the number in the email or package (P03 RE-G06) |
| Training | General annual training only | Payment-fraud role training (POL-05 4.4) | Closers not trained (P03 RE-G13) |
| Incident reporting | Report to the division IT manager | Group SOC within 15 minutes for payment fraud (POL-03 4.1) | Slower escalation |
| Email retention | Keep closing email indefinitely for loan files | Records schedule; closing packages in the loan system (POL-04 4.4) | Guarantor data sprawl (P01 RR-004) |
| Service providers | Title and escrow agents on an approved list | Due diligence and contract terms (POL-01 4.8) | No security terms for agents |
| Control inheritance | Not addressed | Division documents inheritance (POL-01 4.7) | Gap 2 (POAM-018) |

**Why the drift happened.** The 2024 integration plan covered identity and email migration and stopped there. **Fix:** POL-01 4.14 now requires full integration within 12 months of any acquisition, and the Group CISO's policy office tracks supplement versions in the policy register.

## 5. Attestation
Each division security and compliance lead signs an annual statement: "The division supplement does not weaken any group policy and reflects all group policy changes made in the last 12 months." The first attestations are due 2026-12-31 (Banking, Financial Software) and on re-issue (Commercial Real Estate).
