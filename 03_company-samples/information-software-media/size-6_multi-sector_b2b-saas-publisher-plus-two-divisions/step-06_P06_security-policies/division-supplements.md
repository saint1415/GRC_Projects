# Division Supplements to Group Security Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. |
| Authority | POL-01 section 4.5: a supplement may add stricter or division-specific requirements, never weaker ones; it must be re-aligned within 90 days after a group policy changes and attested every year |
| Owner | Each division security and compliance lead; alignment reviewed by the Group CISO |
| Status date | 2026-09-17 (group policies v2026 approved; effective 2026-10-01) |

## 1. How group policy and supplements fit together
| Layer | Examples | Who approves |
|---|---|---|
| Group policy (POL-01 to POL-05) | MFA for all workforce, no new static keys, one severity scale, affiliates treated as service providers | Board risk committee or Group CISO |
| Group standards | Logging standard, cloud guardrails, Group AI Standard (P10), secure development standard | Group CISO |
| **Division supplement** | Regulator- and contract-specific standards (for example, PCI DSS scope reviews, FAR federal project area, DPA notice clocks) | Division president, after Group CISO alignment review |
| Division procedures | Runbooks and work instructions | Division security and compliance lead |

## 2. Supplement status
| Division | Supplement version | Last aligned to group policy | Status | Action |
|---|---|---|---|---|
| Cloud Software | v2026 | 2026-06-30 (to the 2026 draft group policies) | Aligned; update for the final 2026 policies (static keys, statement reviews) due by 2026-12-30 | Confirm alignment |
| Technology Consulting | v2023 | 2023-09 | **Drifted.** Written before the 2025 acquisition and before the 2026 policies; the acquired firm still follows its own 2024 handbook | Re-issue by 2026-12-31, covering the acquired firm (POAM-019) |
| Payments and Payroll | v2026 | 2026-05-15 (aligned with the PCI DSS assessment) | Aligned, but missing the affiliate service provider rule in POL-01 4.8 | Add by 2026-11-30 (POAM-020) |

## 3. What each supplement adds
### 3.1 Cloud Software supplement (service provider to about 38,000 customers; SOC 2 service organization)
| Topic | Division requirement | Group policy it builds on | Driver |
|---|---|---|---|
| Customer notices | Notice register by customer: 72 hours from confirmation, or 48 hours for about 1,240 customers; bank-designated contacts for about 420 bank customers | POL-03 4.5 | DPAs; 12 CFR 53.4 |
| Sub-processors | No sub-processor enabled until the 30-day DPA notice has run and the security review is done | POL-01 4.8 | DPA terms; SOC 2 CC9.2 |
| Export channels | No Restricted data in the shared export bucket; handoff files go to the payroll engine's intake with 7-day retention | POL-04 4.3, 4.5 | 16 CFR 314.4(c)(6), (f) |
| Partner access | Implementation-partner roles expire at project end (at most 90 days) and are in quarterly certification | POL-02 4.6, 4.11 | SOC 2 CC6.2; trust center statement |
| AI and product change gate | Privacy impact assessment, DPA check, and SOC 2 description impact for every feature that changes how customer data is processed | POL-01 4.12; POL-04 4.4 | FTC Act Section 5; SOC 2 CC8.1, CC2.3 |
| Statements | Trust center and product page claims reviewed each quarter against P07 results | POL-01 4.13 | FTC Act Section 5 (deception) |
| Tenant isolation | Isolation tests in every release and at the canary stage | POL-02 4.2 | SOC 2 CC6.1 |

### 3.2 Technology Consulting supplement (federal contractor; HIPAA business associate; implementation partner)
| Topic | Division requirement | Group policy it builds on | Driver |
|---|---|---|---|
| Federal project area | FCI only in the federal project area; membership limited to the named team; flowdown in every subcontract | POL-04 4.7 | 48 CFR 52.204-21(b)(1)(i), (c) |
| Covered telecommunications | Report covered telecommunications equipment or services to the contracting officer within 1 business day of identification | POL-03 4.5 | FAR 52.204-25 |
| Health integrations | Synthetic test data only; ADT messages purged at project close with a destruction certificate to the client | POL-04 4.8 | 45 CFR 164.504(e)(2)(ii)(J) |
| BAA clocks | Hospital BAA notice terms (5 to 30 days) loaded into the group matrix | POL-03 4.5 | 45 CFR 164.410 |
| Migration toolkit | Per-project, per-tenant short-lived credentials; scripts only in group repositories | POL-02 4.4; POL-05 4.3 | FTC Start with Security 3 |
| Client data | Delete or return client data at project close; no client data in personal storage | POL-04 4.5 | Client contracts |
| AI on engagements | Delivery assistant only where the client opted in; never on federal engagements without written approval | POL-05 4.7 | Client contracts; 48 CFR 52.204-21(b)(1)(iv) |
| Acquired firm | Same-day leaver feed to the acquired identity provider until migration; group EDR by 2026-11-30 | POL-02 4.1 | 48 CFR 52.204-21(b)(1)(i), (xiii) |

### 3.3 Payments and Payroll supplement (financial institution under 16 CFR Part 314; PCI DSS service provider)
| Topic | Division requirement | Group policy it builds on | Driver |
|---|---|---|---|
| Qualified Individual | The division CISO is the Qualified Individual; written annual report to the division board covering affiliates and service providers | POL-01 4.2 | 16 CFR 314.4(a), (i) |
| Affiliates as service providers | The WCP and any other affiliate that holds division customer information is selected, contracted, and assessed like an outside service provider | POL-01 4.8 | 16 CFR 314.4(f); PCI DSS 12.8 |
| PCI DSS scope | Scope confirmed every six months and after any network change; segmentation tested every six months | POL-01 4.9 | PCI DSS 11.4.6; 12.5.2.1 |
| Checkout pages | Script inventory, authorization, and tamper detection on every hosted checkout page | POL-02 4.2 | PCI DSS 6.4.3; 11.6.1 |
| Notices | FTC notice within 30 days for 500 or more consumers; sponsor banks within 24 hours; card network procedures | POL-03 4.5 | 16 CFR 314.4(j); sponsor bank agreements |
| Bank detail changes | Dual approval for operations staff edits; second-channel notice to workers | POL-02 4.12 | 16 CFR 314.4(c)(1) |
| MFA exceptions | Any external user population without MFA needs written approval by the Qualified Individual | POL-02 4.3 | 16 CFR 314.4(c)(5) |

## 4. Technology Consulting drift: conflicts with 2026 group policy
The 2023 consulting standards and the acquired firm's 2024 handbook were written before the 2026 group policies. Where they conflict, **group policy governs now** (POL-01 4.5), but staff follow the document they know, so the conflicts are real risks (P01 IC-001, IC-003, IC-005).

| Topic | Consulting standard (2023) or acquired firm handbook (2024) | Group policy (2026) | Effect |
|---|---|---|---|
| Client tenant access | Granted per project; no end date | Expires at project end; quarterly certification (POL-02 4.6, 4.11) | About 1,100 tenants with leftover access (gap 3) |
| Migration credentials | Static keys issued per consultant | No new static keys; short-lived per-project credentials (POL-02 4.4) | 37 static keys (gap 1; P08 scenario) |
| Code storage | Not addressed | Group repositories only (POL-05 4.3) | Scripts with keys in personal repositories |
| Endpoint protection (acquired firm) | Antivirus | Group EDR (common control) | No central detection on 2,600 laptops (gap 9) |
| Client data retention | Keep project files 7 years | Delete or return at project close (POL-04 4.5) | Client data sprawl (IC-002) |
| Federal information | Not addressed | Federal project area (POL-04 4.7) | FCI mixed with commercial projects (gap 11) |
| Common control inheritance | Not addressed | Division must document inheritance (POL-01 4.6) | Gap 10 (POAM-019) |

**Why the drift happened.** The consulting supplement had no review date, and the acquisition integration plan covered finance and HR systems first. **Fix:** POL-01 4.5 now requires re-alignment within 90 days of any group change and an annual attestation, and acquisitions must adopt group policy within 90 days of closing as a condition in the integration plan.

## 5. Attestation
Each division security and compliance lead signs an annual statement: "The division supplement does not weaken any group policy and reflects all group policy changes made in the last 12 months." The first attestations under the 2026 policies are due 2026-12-31 (Cloud Software, Payments and Payroll) and on re-issue (Technology Consulting).
