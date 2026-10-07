# Division Supplements to Group Security Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. |
| Authority | POL-01 section 4.5: a supplement may add stricter or division-specific requirements, never weaker ones; it must be re-aligned within 90 days after a group policy changes and attested every year |
| Owner | Each division security and compliance lead; alignment reviewed by the Group CISO |
| Status date | 2026-09-10 (group policies v2026 approved; effective 2026-10-01) |

## 1. How group policy and supplements fit together
| Layer | Examples | Who approves |
|---|---|---|
| Group policy (POL-01 to POL-05) | MFA for all workforce, one severity scale, purpose tags, no BAA no PHI | Board risk committee or Group CISO |
| Group standards | Logging standard, cloud guardrails, Group AI Standard (P10) | Group CISO |
| **Division supplement** | Regulator-specific and system-specific standards (for example, MA utilization management, ASC emergency preparedness, SaaS customer notices) | Division president, after Group CISO alignment review |
| Division procedures | Runbooks and work instructions | Division security and compliance lead |

## 2. Supplement status
| Division | Supplement version | Last aligned to group policy | Status | Action |
|---|---|---|---|---|
| Care Delivery | v2026 | 2026-06-15 (to the 2026 draft group policies) | Aligned; minor update for the final 2026 policies due by 2026-12-30 (90 days after effective date) | Confirm alignment |
| Health Plan | v2024 | 2024-03 | **Drifted** (scenario gap 2); conflicts listed in section 4 | Re-issue by 2026-11-30 (POAM-014) |
| Health-Tech SaaS | v2025 | 2025-11 | Aligned, but missing an AI and subcontractor change gate required by POL-01 4.8 and 4.12 | Add the change gate by 2026-10-31 (POAM-018) |

## 3. What each supplement adds
### 3.1 Care Delivery supplement (covered entity; also a business associate of 38 practices)
| Topic | Division requirement | Group policy it builds on | Driver |
|---|---|---|---|
| Clinical downtime | Read-only downtime workstations at every site; downtime drill each region every year | POL-03 | 164.308(a)(7)(ii)(C) |
| ASC emergency preparedness | ASC emergency plans reviewed at least every 2 years and include a prolonged cyber outage scenario | POL-03 | 42 CFR 416.54 |
| Medical devices | Devices on device network zones; unsupported devices isolated; vendor access only through PAM | POL-02 4.10 | 164.308(a)(1)(ii)(B) |
| EHR break-glass | Break-glass access reviewed by the Privacy Officer within 2 business days | POL-02 4.9 | 164.312(a)(2)(ii) |
| Privacy monitoring | Weekly EHR access monitoring review, including VIP and employee-as-patient rules | POL-01 4.7 | 164.308(a)(1)(ii)(D) |
| AI scribe | Consent captured in a required field before recording; provider attestation on every AI-assisted note | POL-05 4.7-4.8 | State recording laws (Fla. Stat. 934.03(2)(d) worked example) |
| Decision support | Every patient care decision support tool inventoried; input variables reviewed; mitigation documented | POL-01 4.12 | 45 CFR 92.210 |
| White-label practices | Incident notices to the 38 practices per their BAAs; subcontractor terms with corporate for their PHI | POL-03 4.4; POL-01 4.8 | 164.314(a)(2)(iii); 164.410 |

### 3.2 Health Plan supplement (covered entity; MA organization; state-licensed insurer and HMO)
| Topic | Division requirement | Group policy it builds on | Driver |
|---|---|---|---|
| UM and AI | No UM policy or model-assisted workflow in use without UM committee approval; reviewers document how they considered the enrollee's medical history, physician recommendations, and clinical notes | POL-01 4.12 | 42 CFR 422.137(b); 422.101(c)(1)(i) |
| Adverse decisions | Physician or appropriate professional review before any expected adverse medical necessity decision | POL-01 4.12 | 42 CFR 422.566(d) |
| Enrollee records | Purposes for enrollee information documented for every system and platform dataset | POL-04 4.3 | 42 CFR 422.118(a) |
| State insurance notices | List of states that have enacted a version of NAIC Model #668, with commissioner contacts and deadlines, kept current in the notification matrix | POL-03 4.5 | N52-R07 |
| Broker and member authentication | MFA required for brokers; no SMS-only after 2027-03-31; member step-up MFA | POL-02 4.11 | 164.312(d) |
| Call-center verification | One-time code to the member's registered phone before disclosing PHI | POL-05 | 164.514(h) |

### 3.3 Health-Tech SaaS supplement (business associate; SOC 2 service organization)
| Topic | Division requirement | Group policy it builds on | Driver |
|---|---|---|---|
| Customer notices | Notice register by customer BAA term (standard 10 calendar days for breaches, 5 business days for other incidents; 72 hours for 42 customers) | POL-03 4.4 | 164.410; 164.314(a)(2)(i)(C) |
| Subcontractors | No new subcontractor handling customer PHI until legal checks customer BAAs and SOC 2 commitments | POL-01 4.8 | 164.308(b)(2); 164.504(e)(2)(ii)(D) |
| AI and product change gate | Privacy impact analysis, BAA review, and SOC 2 system description impact for every feature that changes how PHI is processed | POL-01 4.12 | SOC 2 CC8.1; CC2.3 |
| Tenant isolation | Isolation tests in every release; row-level security by 2027-03-31 | POL-02 4.2 | 164.312(a) |
| De-identification | De-identify inside SYS-D3 before export; only for customers whose BAA permits it | POL-04 4.5 | 164.502(a)(3); 164.514(b) |
| Offboarding | Return or destroy customer PHI with a certificate within 60 days of termination | POL-04 4.7 | 164.504(e)(2)(ii)(J) |

## 4. Health Plan drift: conflicts with 2026 group policy
The 2024 Health Plan standards were written before the 2026 group policies. Where they conflict, **group policy governs now** (POL-01 4.5), but staff follow the document they know, so the conflicts are real risks (P01 HP-005; P07 PL-01a.01(b)).

| Topic | Health Plan standard (2024) | Group policy (2026) | Effect |
|---|---|---|---|
| Log retention | 90 days in application | 1 year hot, 6 years archived (logging standard; POL-01 4.11 for documentation) | Investigations and breach scoping limited to 90 days (POAM-016) |
| Broker authentication | SMS codes acceptable | MFA required; no SMS-only after 2027-03-31 (POL-02 4.11) | Broker account takeover risk (HP-006) |
| Incident severity | Health Plan 4-level scale | One group scale (POL-03 4.2) | Inconsistent escalation (P07 IR-04d.) |
| Termination | Next business day | Within 4 hours (POL-02 4.5) | Longer exposure window |
| AI use | Not addressed | AI inventory and approval (POL-01 4.12) | UM model not governed (HP-001) |
| Common control inheritance | Not addressed | Division must document inheritance (POL-01 4.6) | Gap 6 (POAM-015) |
| Data between covered entities | Feed approval only | Minimum-necessary protocol per routine feed (POL-04 4.4) | Gap 1 (P03) |

**Why the drift happened.** The 2024 re-organization moved Health Plan security under the Group CISO, but the supplement had no owner or review date. **Fix:** POL-01 4.5 now requires re-alignment within 90 days of any group change and an annual attestation, and the Group CISO's policy office tracks supplement versions in the policy register.

## 5. Attestation
Each division security and compliance lead signs an annual statement: "The division supplement does not weaken any group policy and reflects all group policy changes made in the last 12 months." The first attestations are due 2026-12-31 (Care Delivery, SaaS) and on re-issue (Health Plan).
