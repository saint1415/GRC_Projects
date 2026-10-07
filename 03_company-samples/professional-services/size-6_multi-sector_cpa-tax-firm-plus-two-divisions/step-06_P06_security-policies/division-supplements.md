# Division Supplements to Group Security Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. (and Cris Santos CPA Partners, LLP under the administrative services agreement) |
| Authority | POL-01 section 4.5: a supplement may add stricter or division-specific requirements, never weaker ones; it must be re-aligned within 90 days after a group policy changes and attested every year |
| Owner | Each division security and compliance lead (for CPA Partners, its risk and quality partner); alignment reviewed by the Group CISO |
| Status date | 2026-09-10 (group policies v2026 approved; effective 2026-10-01) |

## 1. How group policy and supplements fit together
| Layer | Examples | Who approves |
|---|---|---|
| Group policy (POL-01 to POL-05) | MFA for every individual, one severity scale, the call-back rule, IRC 7216 consent before any disclosure to another group entity | Board risk committee or Group CISO |
| Group standards | Logging standard, cloud guardrails, retention schedule, Group AI Standard (P10) | Group CISO |
| **Division supplement** | Regulator-specific and system-specific standards (IRS e-file duties, Regulation S-P notices, SOC 2 change gates, business associate duties) | Division president or the CPA Partners managing partner, after Group CISO alignment review |
| Division procedures | Runbooks and work instructions | Division security and compliance lead |

## 2. Supplement status
| Unit | Supplement version | Last aligned to group policy | Status | Action |
|---|---|---|---|---|
| Tax and Advisory | v2026 | 2026-06-15 (to the 2026 draft group policies) | Aligned; minor update for the final 2026 policies due by 2026-12-30 (90 days after the effective date) | Confirm alignment |
| CPA Partners | v2023 | 2023-04 | **Drifted** (scenario gap 7); conflicts listed in section 4 | Re-issue by 2026-12-31 (POAM-015) |
| Wealth | v2025 | 2025-11 (with the Regulation S-P program) | Aligned, but missing affiliate service provider oversight and the AI notes records rule | Add both by 2026-12-31 (POAM-018, POAM-019) |
| Practice Cloud | v2025 | 2025-10 | Aligned, but missing the AI and sub-processor change gate required by POL-01 4.9 and 4.13 | Add the gate by 2026-10-31 (POAM-020) |

## 3. What each supplement adds
### 3.1 Tax and Advisory supplement (Safeguards Rule financial institution; tax return preparer; ERO)
| Topic | Division requirement | Group policy it builds on | Driver |
|---|---|---|---|
| Written program index | The supplement lists every part of the written information security program (group policies, this supplement, the TPCP SSP, the risk assessment, the IR runbook) | POL-01 4.1 | 16 CFR 314.3(a) |
| Seasonal staff | Accounts activated only after the background check and training; end date April 30 entered by HR; extensions only through HR; seasonal staff use office devices only and have no remote access | POL-02 4.3, 4.6 | 314.4(c)(1)(i), (e)(1) |
| Office access | SYS-T1 access limited to the user's office queue; regional access time-limited with a named purpose | POL-02 4.2 | 314.4(c)(1)(ii); 301.7216-2(c)(2) |
| Office intake mailboxes | Retired in favor of portal upload by 2027-04-30; until then delegation-only access, no legacy authentication, no forwarding | POL-02 4.1, 4.4 | 314.4(c)(5) |
| Refund bank changes | Any change to refund bank details after intake requires a call-back to the number of record, recorded in SYS-T1 before release | POL-05 4.5 | 314.3(b)(3) |
| IRC 7216 consent | Consent register checked by the referral interface; consents at engagement start only; refusals recorded; only consented fields sent | POL-04 4.4, 4.5 | 301.7216-3(a)(3), (b)(1)-(3) |
| IRS reporting | Chief Tax Officer reports security incidents to the IRS Stakeholder Liaison no later than the next business day after confirmation, and notifies state tax agencies | POL-03 4.3, 4.4 | IRS Pub. 1345 |
| EFIN and PTIN monitoring | Weekly return-volume checks per EFIN and PTIN in season; monthly off-season | POL-01 4.10 | IRS Pub. 4557 |
| AI in preparation | AI-populated fields verified by the preparer and checked by the reviewer; no AI tool may propose tax treatments using client data until the IRC 7216 and Circular 230 review is approved | POL-05 4.8; POL-01 4.13 | 301.7216-2(d)(1); 31 CFR 10.22 |
| Client accounting payroll | Payroll deposit changes only through the client portal with client approval | POL-05 4.5 | 314.3(b)(3) |

### 3.2 CPA Partners supplement (attest firm; HIPAA business associate)
| Topic | Division requirement | Group policy it builds on | Driver |
|---|---|---|---|
| Engagement access | Engagement files open only to the assigned engagement team; independence-restricted engagements locked | POL-02 4.2 | Professional standards (noted) |
| PHI from health care audit clients | Received only through SYS-T3 secure requests; minimum necessary samples; deleted at engagement archive unless the BAA requires return | POL-04 4.1, 4.7 | 45 CFR 164.504(e) |
| Subcontractor terms | The holding company acts as CPA Partners' subcontractor for PHI only under written business associate terms | POL-01 4.6 | 164.308(b)(2); 164.314(a) |
| Business associate notices | Breach of unsecured PHI reported to the covered entity without unreasonable delay and no later than 60 days after discovery, through the combined matrix | POL-03 4.4 | 164.410 |
| SOC examination files | Outside service organizations' system descriptions and test evidence classified Confidential and kept 7 years | POL-04 4.1 | Engagement letters |
| Independence | No CPA Partners engagement for the holding company or any group entity, including Practice Cloud's SOC 2 | POL-01 4.1 | Professional standards (noted) |

### 3.3 Wealth supplement (SEC-registered adviser; Regulation S-P covered institution)
| Topic | Division requirement | Group policy it builds on | Driver |
|---|---|---|---|
| Response program | Regulation S-P response program: assess, contain, notify affected individuals within 30 days after becoming aware, unless a documented determination finds no reasonably likely substantial harm or inconvenience | POL-03 4.4 | 17 CFR 248.30(a)(3), (a)(4) |
| Affiliate service providers | Tax and Advisory and corporate are service providers when they hold Wealth customer information; due diligence files, monitoring, and 72-hour notice terms apply to them as to outside vendors | POL-01 4.6, 4.9 | 248.30(a)(5) |
| Money movement | Call-back to the number of record for every third-party transfer and every change of bank or address; second review over $50,000; requests from internal senders treated the same as external | POL-05 4.5 | 248.201(d) |
| Red flags | Identity Theft Prevention Program red flags include requests that cite tax documents and requests relayed by internal senders | POL-03 4.8 | 248.201(d)(2) |
| Records | Advice and money-movement communications only through archived channels; AI meeting summaries archived as records before any expansion of the pilot | POL-05 4.7 | 275.204-2(a)(7), (e)(1) |
| Tax return information received | Wealth may use only the fields and purposes named in a client's IRC 7216 consent; no statistical compilations from tax-derived fields | POL-04 4.4, 4.5 | 301.7216-3 (Tax and Advisory's duty) |

### 3.4 Practice Cloud supplement (SOC 2 service organization; service provider to customer firms)
| Topic | Division requirement | Group policy it builds on | Driver |
|---|---|---|---|
| Customer notices | Notice register by contract term (72 hours standard; 24 hours for 140 enterprise customers); always within state third-party agent limits | POL-03 4.6 | Customer contracts; Fla. Stat. 501.171(6)(a) (worked example) |
| Sub-processors | 30 days' notice to customers before adding a sub-processor that handles customer data; legal review against contracts and SOC 2 commitments | POL-01 4.9 | Customer contracts |
| AI and product change gate | Privacy and IRC 7216 analysis, contract review, and SOC 2 system description impact for every feature that changes how customer data is processed | POL-01 4.13 | SOC 2 CC8.1, CC2.3 |
| Tenant isolation | Isolation tests in every release; independent test each year | POL-02 4.2 | Customer contracts |
| Customer MFA | MFA on by default for new tenants; enforcement campaign for existing tenants | POL-02 4.11 | Customer firms' 314.4(c)(5) duty |
| Support access | Customer ticket and time-limited approval for any access to tenant data | POL-02 4.2 | SOC 2 CC6.3 |
| Offboarding | Return or delete customer data with a certificate within 60 days of termination | POL-04 4.7 | Customer contracts; SOC 2 C1.2 |

## 4. CPA Partners drift: conflicts with 2026 group policy
The 2023 CPA Partners supplement was written before the 2026 group policies and before the attest practice's PHI volume grew. Where they conflict, **group policy governs now** (POL-01 4.5), but staff follow the document they know, so the conflicts are real risks (P01 TX-025; P07 PL-01 findings).

| Topic | CPA Partners supplement (2023) | Group policy (2026) | Effect |
|---|---|---|---|
| Common control inheritance | Not addressed | Each unit documents inheritance every year (POL-01 4.6) | CPA Partners cannot show which group controls protect PHI (gap 7; POAM-016) |
| Subcontractor terms | Not addressed | Written intercompany terms, including HIPAA subcontractor terms (POL-01 4.6) | No business associate agreement with the holding company (POAM-023) |
| Incident notices | CPA Partners partner decides alone | Combined matrix; counsel approves (POL-03 4.5) | Notices outside the group process |
| AI use | Not addressed | AI inventory and approval (POL-01 4.13) | Audit analytics tool (AI-004) registered late |
| MFA exceptions | Partner approval | Qualified Individual approval and 12-month limit (POL-01 4.11) | Not applicable to CPA Partners' own systems, but inconsistent |
| Retention of engagement files | 10 years | Group schedule (POL-04 4.7) sets 7 years unless a professional standard requires longer | Over-retention unless justified |

**Why the drift happened.** CPA Partners is a separate firm, so its supplement was treated as its own document and left out of the group policy register. **Fix:** the Group CISO's policy office now tracks the CPA Partners supplement with the division supplements, and POL-01 4.5 applies to it.

## 5. Attestation
Each division security and compliance lead (and the CPA Partners risk and quality partner) signs an annual statement: "The supplement does not weaken any group policy and reflects all group policy changes made in the last 12 months." The first attestations are due 2026-12-31 (Tax and Advisory, Wealth, Practice Cloud) and on re-issue (CPA Partners).
