# Division Supplements to Group Security Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. |
| Authority | POL-01 section 4.5: a supplement may add stricter or division-specific requirements, never weaker ones; it must be re-aligned within 90 days after a group policy changes, must cover acquired staff from the acquisition date, and must be attested every year |
| Owner | Each division security and compliance lead; alignment reviewed by the Group CISO |
| Status date | 2026-09-15 (group policies v2026 approved; effective 2026-10-01) |

## 1. How group policy and supplements fit together
| Layer | Examples | Who approves |
|---|---|---|
| Group policy (POL-01 to POL-05) | MFA for all workforce, screening before access wherever the person works, one severity scale, flowdown before data | Board risk committee or Group CISO |
| Group standards | Logging standard, cloud guardrails, cryptography standard, Group AI Standard (P10) | Group CISO |
| **Division supplement** | Program-specific and agency-specific rules (CJIS tenant support, FTI tenancy, DPPA permitted uses, CUI enclave, FedRAMP and GovRAMP change control) | Division president, after Group CISO alignment review |
| Division procedures | Runbooks, agency fact sheet templates, work instructions | Division security and compliance lead |

## 2. Supplement status
| Division | Supplement version | Last aligned to group policy | Status | Action |
|---|---|---|---|---|
| GovTech Integration | v2026 | 2026-06-30 (to the 2026 draft group policies) | Aligned; minor update for the final 2026 policies due by 2026-12-30 (90 days after the effective date) | Confirm alignment |
| IT Consulting | v2024 | 2024-04 | **Drifted:** predates the 2025 acquisition; the acquired firm's 2023 policies still govern about 2,800 staff (scenario gap 7); conflicts in section 4 | Re-issue covering acquired staff by 2026-11-30 (POAM-025) |
| Government Software Products | v2025 | 2025-10 | Aligned, but missing the AI change gate (POL-01 4.13) and the GovRAMP significant change step | Add both by 2026-10-31 (POAM-022, POAM-023) |

## 3. What each supplement adds
### 3.1 GovTech Integration supplement (agency contractor; HIPAA business associate for the IEP; DPPA contractor for the MVSP)
| Topic | Division requirement | Group policy it builds on | Driver |
|---|---|---|---|
| Tenant-scoped support | Support and operations staff get access only to the tenants of the states for which they are screened; no cross-tenant search roles | POL-02 4.2 | CJISSECPOL v6.1 PS-3; Pub. 1075 Exhibit 7 I(2) |
| FTI tenancy | Dedicated database and customer-managed key per revenue agency; no FTI service change until the agency's IRS notification covers it | POL-04 4.2, 4.3 | Pub. 1075 sec. 3.3.1; sec. 2.E.6; Exhibit 6 |
| No FTI on the IEP | Interfaces carry no IRS income match fields; caseworker guidance; detection of pasted IRS data | POL-04 4.4 | Pub. 1075 sec. 2.C.11.2 |
| Agency fact sheets | A fact sheet per affected agency within 4 hours of a suspected incident, with no regulated data in it | POL-03 4.4 | Fla. Stat. 282.318(3)(c)9.b. (worked example); Pub. 1075 sec. 1.8.3 |
| DPPA permitted uses | Every MVSP records release logged with its permitted use; bulk requesters re-verified each year; 5-year records | POL-04 4.6 | 18 U.S.C. 2721(b)-(c) |
| Medicaid PHI on the IEP | BAA clocks in the notification matrix; intercompany subcontractor terms with corporate | POL-01 4.9; POL-03 4.5 | 45 CFR 164.410; 164.314(a)(2)(iii) |
| AI eligibility assistant | Recommendations shown only after the caseworker records their own finding; no AI text in notices | POL-01 4.13 | 7 CFR 272.4(a)(2); 42 CFR 431.10(b)(3) |
| Agency-issued accounts | Staff using agency systems follow the agency's rules; leavers reported to the agency on their last day | POL-02 4.5 | Contract terms |

### 3.2 IT Consulting supplement (DoD and federal contractor; HIPAA business associate for 19 engagements)
| Topic | Division requirement | Group policy it builds on | Driver |
|---|---|---|---|
| CUI location | CUI only in the enclave or government-furnished systems; never on acquired file shares or laptops | POL-04 4.4 | DFARS 252.204-7012(b); SP 800-171 Rev. 2 3.1.3 |
| DoD incident reporting | At least 6 staff in two locations hold DoD-approved medium assurance certificates; DoD report within 72 hours of discovery; images kept 90 days | POL-03 4.5, 4.9 | DFARS 252.204-7012(c)(1)(ii), (c)(3), (e) |
| CMMC affirmations | Counsel and internal audit review before every affirmation; SPRS updated after any scope change | POL-01 4.2 | 32 CFR 170.22; DFARS 252.204-7019, 7020 |
| Subcontract flowdown | DFARS 252.204-7012 in every DoD subcontract involving covered defense information; CMMC status checked before award | POL-01 4.9 | DFARS 252.204-7012(m); 252.204-7021 |
| Acquired estate | Phishing-resistant VPN MFA by 2026-10-31; group EDR by 2026-12-31; directory trust removed at migration | POL-02 4.3, 4.12 | SP 800-171 Rev. 2 3.5.3, 3.14.2 |
| PHI on engagements | PHI stays in client systems or the delivery workspace | POL-04 4.4 | 45 CFR 164.312(a)(2)(iv) |

### 3.3 Government Software Products supplement (SaaS publisher; CJIS contractor for the RMS; FedRAMP and GovRAMP)
| Topic | Division requirement | Group policy it builds on | Driver |
|---|---|---|---|
| RMS support by state | Support queues by state; staff take tickets only for states where they are screened and certified | POL-02 4.2 | CJISSECPOL v6.1 PS-3; SA-9 |
| Connector cryptography | Connectors at agency premises use FIPS 140-3 certified modules; inventory of module certificates | POL-04 4.2 | CJISSECPOL v6.1 SC-13 |
| AI and product change gate | Privacy and CJIS review, Group AI council review, SOC 2 system description impact, and customer notice before any feature that changes how customer data is processed, including feature-flag betas | POL-01 4.13 | SOC 2 CC3.4, CC8.1; CJISSECPOL v6.1 SA-9 |
| FedRAMP and GovRAMP changes | Significant changes assessed and reported before release | POL-01 4.6 | FedRAMP continuous monitoring; GovRAMP |
| Customer administrator MFA | Required for all customer administrator accounts by 2027-03-31 | POL-02 4.11 | SOC 2 CC6.1 |
| Security claims | Legal review of all security and compliance claims | POL-05 4.8 | FTC Act Section 5 |

## 4. IT Consulting drift: conflicts with 2026 group policy
The acquired firm's 2023 policies were never replaced, and the IT Consulting v2024 supplement predates the acquisition. Where they conflict, **group policy governs now** (POL-01 4.5), but about 2,800 staff follow the document they know, so the conflicts are real risks (P01 IC-013; P07 POAM-018, POAM-020).

| Topic | Acquired firm policy (2023) | Group policy (2026) | Effect |
|---|---|---|---|
| Remote access MFA | SMS codes accepted on the VPN | Phishing-resistant MFA; no SMS after 2026-10-31 (POL-02 4.3) | Entry path in the P08 scenario (IC-001) |
| Endpoint protection | Antivirus | Group EDR on every endpoint (common control) | Malware undetected (IC-003) |
| CUI storage | Project file shares allowed | Enclave only (POL-04 4.4) | CUI outside the enclave (IC-002) |
| Incident reporting | Report to the firm's IT help desk within 1 business day | Group SOC within 1 hour (POL-03 4.1) | DoD and agency clocks missed |
| Public AI tools | Not addressed | Approved tools only (POL-05 4.7) | Client data in public tools (IC-007) |
| Directory trusts | Not addressed | Migration only, monitored, with an end date (POL-02 4.12) | Trust live without SOC monitoring |

**Why the drift happened.** The acquisition plan put policy alignment after the system migration. **Fix:** POL-01 4.5 now requires supplements to cover acquired staff from the acquisition date, and the Group CISO's policy office tracks supplement versions and acquisitions in the policy register.

## 5. Attestation
Each division security and compliance lead signs an annual statement: "The division supplement does not weaken any group policy, covers every staff member in the division including acquired staff, and reflects all group policy changes made in the last 12 months." The first attestations are due 2026-12-31 (GovTech, Software) and on re-issue (IT Consulting).
