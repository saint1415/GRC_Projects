# Division Supplements to Group Security Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. |
| Authority | POL-01 section 4.5: a supplement may add stricter or division-specific requirements, never weaker ones; it must be re-aligned within 90 days after a group policy changes and attested every year; an acquired company adopts group policy within 180 days of closing |
| Owner | Each division security and compliance lead; alignment reviewed by the Group CISO |
| Status date | 2026-09-10 (group policies v2026 approved; effective 2026-10-01) |

## 1. How group policy and supplements fit together
| Layer | Examples | Who approves |
|---|---|---|
| Group policy (POL-01 to POL-05) | MFA for all workforce, one severity scale, no PAN by email, affiliates overseen as service providers | Board risk committee or Group CISO |
| Group standards | Logging standard, cloud guardrails, configuration baselines, Group AI Standard (P10) | Group CISO |
| **Division supplement** | Assessor- and customer-specific standards (for example, PCI DSS key management for the processor, storefront script control for the Software division, client environment rules for consulting) | Division president, after Group CISO alignment review |
| Division procedures | Runbooks and work instructions | Division security and compliance lead |

## 2. Supplement status
| Division | Supplement version | Last aligned to group policy | Status | Action |
|---|---|---|---|---|
| Payment Processing | v2026 | 2026-06-30 (to the 2026 draft group policies) | Aligned; minor update for the final 2026 policies due by 2026-12-30 | Confirm alignment |
| Payments Software Platform | v2025 | 2025-11 | Aligned, but missing the product and AI change gate (POL-01 4.12) and a storefront script standard | Add both by 2026-10-31 (POAM-015, POAM-017) |
| Merchant Consulting | v2024 (acquired firm's policy set) | **Never aligned** | **Drifted** (scenario gap 2); conflicts listed in section 4. The 180-day adoption rule in POL-01 4.5 is new; it would have required alignment by 2025-09-28 | Re-issue by 2026-11-30 (POAM-011) |

## 3. What each supplement adds
### 3.1 Payment Processing supplement (PCI DSS Level 1 service provider; bank service provider; financial institution)
| Topic | Division requirement | Group policy it builds on | Driver |
|---|---|---|---|
| Key management | Key custodians named in writing; dual control and split knowledge for every key ceremony; annual ceremony audit | POL-04 4.2 | PCI DSS 3.6, 3.7 |
| Detokenization | Clear PAN only to named service identities; quarterly review of detokenization volumes | POL-02 4.2 | PCI DSS 3.4, 7.2 |
| Dispute platform | Case export only for supervisors with a ticket; card images masked on upload; files purged 90 days after closure | POL-02 4.2; POL-04 4.3, 4.5 | PCI DSS 3.2.1, 3.4.1, 7.2 |
| Covered services | 4-hour determination procedure for any incident that may affect clearing, settlement, reconciliation, or funding files; contacts for all four sponsor banks confirmed quarterly | POL-03 4.5, 4.6 | 12 CFR 53.4; 225.303; 304.24 |
| Card brand notices | Liaison takes any suspected account data compromise within 1 hour; brand clocks tracked in the incident log | POL-03 4.4 | Visa WTDIC; sponsor agreements |
| Scope | Scope confirmed every six months and after significant or organizational change, with data-flow tests including email and log paths | POL-01 4.13 | PCI DSS 12.5.2.1, 12.5.3 |
| Quarterly reviews | Second-line review each quarter of log review, rule review, configuration standards, alert response, and change management | POL-01 4.9 | PCI DSS 12.4.2 |

### 3.2 Payments Software Platform supplement (gateway service provider; SOC 2 service organization)
| Topic | Division requirement | Group policy it builds on | Driver |
|---|---|---|---|
| Storefront scripts | Every script on a storefront page inventoried with justification and integrity-checked; tamper-detection on every theme; content security policy by default | POL-01 4.1 | PCI DSS 6.4.3, 11.6.1; SOC 2 CC6.6 |
| Marketplace apps | Apps that add scripts or read customer data need security review at listing and every year, and a per-app kill switch | POL-01 4.8 | SOC 2 CC9.2; 15 U.S.C. 45(a) |
| Product and AI change gate | Privacy review, SOC 2 system description impact, and merchant terms review for every feature that changes how customer data is processed or adds a subservice organization | POL-01 4.12 | SOC 2 CC2.3, CC3.4, CC8.1 |
| ISV credentials | Keys shown once; masked in the support console; rotated after any support view | POL-02 4.12 | PCI DSS 8.3.2 |
| ISV and merchant notices | ISV notice within 24 hours of an incident affecting ISV credentials or data; 48-hour notice for 140 enterprise merchants | POL-03 4.6 | ISV agreement; enterprise contracts |
| Logs | No PAN in any log field; build fails on PAN patterns | POL-04 4.6 | PCI DSS 3.2.1 |

### 3.3 Merchant Consulting supplement (service provider to the processor; dispute services; client environments)
| Topic | Division requirement | Group policy it builds on | Driver |
|---|---|---|---|
| Identity | Until migration: SYS-M1 reconciled against HR weekly; no MFA exemptions; SMS codes not accepted for CDE access after 2026-12-31 | POL-02 4.1, 4.3 | PCI DSS 8.2, 8.4; 16 CFR 314.4(f)(2) (contract) |
| Dispute evidence | Merchants upload evidence through the portal; no evidence by email; mailboxes scanned and purged | POL-04 4.3 | PCI DSS 3.2.1, 3.5 |
| Client environments | Per-person credentials in the group secret store; no shared client credentials | POL-05 4.8 | PCI DSS 8.2.3 |
| Independence | PCI readiness advisors never work on the group's own PCI DSS scope | POL-01 4.2 | PCI DSS 12.4.1 (accountability) |
| Client notices | Client notice within 72 hours of a confirmed incident affecting client data, through the group matrix | POL-03 4.6 | Engagement letters |
| Generative AI | Approved assistant only; no client data in public tools | POL-05 4.6 | 16 CFR 314.4(e) (contract) |

## 4. Merchant Consulting drift: conflicts with 2026 group policy
The 2024 policies of the acquired firm were never replaced. Where they conflict, **group policy governs now** (POL-01 4.5), but staff follow the document they know, so the conflicts are real risks (P01 MC-006; P07 PL-01 finding).

| Topic | Consulting policy (2024) | Group policy (2026) | Effect |
|---|---|---|---|
| MFA | Any second factor; office "trusted locations" exempt | MFA for all access; exemptions only with Group CISO approval; no SMS for CDE access after 2026-12-31 (POL-02 4.3) | 14 users exempt; SMS relay risk (MC-001) |
| Termination | Access removed "promptly" by ticket | Within 4 hours of the HR event (POL-02 4.5) | 37 departed consultants still active in 2026-07 (MC-002) |
| Card data | Dispute evidence accepted by email | No PAN by email; evidence portal (POL-04 4.3) | About 380,000 emails with PAN (PP-010) |
| Retention | Keep client files 7 years | Retention schedule; customer information disposed within 2 years of last use unless needed (POL-04 4.5) | Mailboxes back to 2019 |
| Generative AI | Not addressed | Approved tools only (POL-05 4.6) | Client data in public chatbots (MC-004) |
| Incident severity and notice | Firm's 3-level scale; client notice by engagement lead | One group scale (POL-03 4.2); matrix owned by counsel (POL-03 4.6) | Inconsistent escalation |
| Common control inheritance | Not addressed | Division documents inheritance (POL-01 4.6) | Gap 2 (POAM-010) |

**Why the drift happened.** The 2025 integration plan covered identity federation, EDR, and email security, but no one owned the policy set and there was no deadline for adopting group policy. **Fix:** POL-01 4.5 now requires adoption within 180 days of closing for any future acquisition, and the Group CISO's policy office tracks supplement versions in the policy register.

## 5. Attestation
Each division security and compliance lead signs an annual statement: "The division supplement does not weaken any group policy and reflects all group policy changes made in the last 12 months." The first attestations are due 2026-12-31 (Payment Processing, Software) and on re-issue (Merchant Consulting).
