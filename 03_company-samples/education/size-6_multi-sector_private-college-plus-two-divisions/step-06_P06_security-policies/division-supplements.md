# Division Supplements to Group Security Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. |
| Authority | POL-01 section 4.5: a supplement may add stricter or division-specific requirements, never weaker ones; it must be re-aligned within 90 days after a group policy changes and attested every year |
| Owner | Each division security and compliance lead; alignment reviewed by the Group CISO |
| Status date | 2026-09-15 (group policies v2026 approved; effective 2026-10-01) |

## 1. How group policy and supplements fit together
| Layer | Examples | Who approves |
|---|---|---|
| Group policy (POL-01 to POL-05) | MFA for all workforce and students, one severity scale, intercompany notice within 24 hours, data-sharing approvals between divisions | Board risk committee or Group CISO |
| Group standards | Logging standard, cloud guardrails, Group AI Standard (P10) | Group CISO |
| **Division supplement** | Regulator-specific and system-specific standards (FSA notices and SAIG, COPPA program and retention, HIPAA and FERPA clinic record handling) | Division president, after Group CISO alignment review |
| Division procedures | Runbooks and work instructions | Division security and compliance lead |

## 2. Supplement status
| Division | Supplement version | Last aligned to group policy | Status | Action |
|---|---|---|---|---|
| Higher Education | v2026 | 2026-06-30 (to the 2026 draft group policies) | Aligned; minor update for the final 2026 policies due by 2026-12-30 (90 days after the effective date) | Add the support access review (POL-02 4.10) and data-sharing approval steps (POL-04 4.4) |
| Education Software | v2025 | 2025-10 | Aligned, but missing the AI and children's privacy change gate and the customer access rule required by POL-01 4.12 and POL-02 4.10 | Add both by 2026-11-30 (POAM-001, POAM-014) |
| Student Health | v2023 (pre-acquisition standards) | Never aligned to group policy | **Drifted** (scenario gap 4); conflicts listed in section 4 | Re-issue by 2026-11-30 (POAM-018) |

## 3. What each supplement adds
### 3.1 Higher Education supplement (Title IV institution; FERPA)
| Topic | Division requirement | Group policy it builds on | Driver |
|---|---|---|---|
| Qualified Individual | The College CISO is the Qualified Individual; the written report to the board of trustees each October covers intercompany service providers | POL-01 4.2, 4.13 | 16 CFR 314.4(a), (i) |
| FSA breach report | The executive director of financial aid files the FSA Cybersecurity Breach Intake report immediately on any actual or suspected breach of student information, without waiting for forensic confirmation | POL-03 4.4 | SAIG Enrollment Agreement |
| Legitimate educational interest | SIS roles are built around legitimate educational interest: faculty see their sections, advisors their caseloads, admissions only onboarding fields for admitted students; warehouse roles require an approved project | POL-02 4.2 | 34 CFR 99.31(a)(1)(ii) |
| Support access to the college tenant | The registrar approves each Education Software support grant; the College CISO reviews the monthly support access summary | POL-02 4.10 | 34 CFR 99.31(a)(1)(i)(B); 314.4(c)(1) |
| SAIG workstations | Dedicated workstations in a badge-controlled room; application allow listing; no email or web browsing; individual Department system accounts only | POL-02 4.1 | SAIG Enrollment Agreement |
| Refund integrity | Bank detail changes need MFA and an out-of-band confirmation; changes in the 10 days before a refund run are reviewed | POL-02 4.12 | 34 CFR 668.164(h)(2) (timely refunds); 314.4(c)(1) |
| FAFSA data | FAFSA-derived fields restricted to the financial aid role and excluded from all models | POL-04 4.6 | HEA sec. 483 |
| Disclosure records | Automated disclosures (transcript clearinghouse, proctoring) recorded per student | POL-04 4.4 | 34 CFR 99.32(a) |
| Legacy campuses | Until retirement (2027-06-30): segmented server networks, unique local administrator passwords, MFA or retirement for the legacy SIS | POL-02 4.13 | 314.4(c)(1), (c)(5) |
| AI in admissions, advising, and proctoring | Human review rule; no score used to discourage enrollment; proctoring flags reviewed by faculty before any integrity case | POL-05 4.6; POL-01 4.12 | Title VI; Section 504; Colo. SB26-189 (from 2027-01-01) |

### 3.2 Education Software supplement (COPPA operator; school official and service provider to customers; SOC 2 service organization)
| Topic | Division requirement | Group policy it builds on | Driver |
|---|---|---|---|
| Children's information security program | The Education Software CISO coordinates the program; risk assessment and program evaluation at least annually | POL-01 4.2, 4.3 | 16 CFR 312.8(b)(1), (b)(2), (b)(5) |
| Customer tenant access | Ticket-bound, customer-approved, time-limited access through PAM; no standing access; logs available to customers | POL-02 4.10 | 312.8(b)(3); 34 CFR 99.31(a)(1)(i)(B) |
| Retention | Delete district data within 90 days after contract end; certificate to the district; monthly report of tenants past their deletion date | POL-04 4.7 | 312.10 |
| Product change gate | Every feature that changes how student or child data is processed needs a children's privacy review, a security review, a SOC 2 description impact check, and a district authorization check before release | POL-01 4.12 | 312.5(a)(1); 312.8(b)(2); SOC 2 CC8.1 |
| Subprocessors | Customers are notified before a new subprocessor processes their data; written security assurances obtained first | POL-01 4.8 | 312.8(c); customer contracts |
| Customer notices | Notice register by contract term (72 hours standard; state-specific terms for about 1,300 districts) | POL-03 4.5 | Customer contracts; state student data laws |
| Public statements | Trust page and marketing statements on security, access, and AI reviewed by privacy counsel each quarter | POL-05 | FTC Act Section 5 |

### 3.3 Student Health supplement (HIPAA covered entity; FERPA records kept for institutions)
| Topic | Division requirement | Group policy it builds on | Driver |
|---|---|---|---|
| Record status | Every record flagged PHI or FERPA record, and for students the owning institution | POL-04 4.9 | 34 CFR 99.3; 45 CFR 160.103 |
| Treatment records | Counseling and clinic records of students disclosed only to treating professionals, with consent, or as the owning institution directs | POL-04 4.5 | 34 CFR 99.3; 99.33(a) |
| Interfaces | No interface carrying clinic data leaves the EHR without the Privacy Officer's approval; aggregate data only for campus reporting | POL-04 4.4 | 45 CFR 164.502(a); 164.514(d) |
| Breach scoping | Breach assessments separate PHI (HIPAA notices) from FERPA records (institution notices under contract) | POL-03 4.4 | 164.402-164.410 |
| Identity | Legacy domain users migrated to SYS-G1 with MFA by 2027-03-31; no shared front desk logins | POL-02 4.1 | 164.312(a)(2)(i), (d) |
| Downtime and backups | Downtime procedures drilled each year; file server restores tested each quarter | POL-01 4.9 | 164.308(a)(7)(ii)(D) |
| AI scribe | Consent captured in a required field before recording | POL-05 4.7 | State recording laws (Fla. Stat. 934.03(2)(d) worked example) |
| Decision support tools | Inventory and input review for tools that use protected traits | POL-01 4.12 | 45 CFR 92.210 |

## 4. Student Health drift: conflicts with 2026 group policy
The 2023 Student Health standards were written by the clinic operator before the 2024 acquisition. Where they conflict, **group policy governs now** (POL-01 4.5), but staff follow the document they know, so the conflicts are real risks (P01 SH-005; P07 PL-1 findings).

| Topic | Student Health standard (2023) | Group policy (2026) | Effect |
|---|---|---|---|
| Authentication | Passwords only on clinic workstations | MFA for all workforce (POL-02 4.3) | About 40% of users without MFA (POAM-017) |
| Shared logins | Front desk logins allowed | Unique identity for everyone (POL-02 4.1) | Shared logins found at 3 clinics (P07) |
| Termination | Next business day | Within 4 hours (POL-02 4.5) | Longer exposure window |
| Data sharing | Clinic manager approves exports | Data-sharing approval by both data owners and the Privacy Officer (POL-04 4.4) | The 2025 utilization extract (scenario gap 2) |
| Backups | Nightly backup, no test requirement | Quarterly restore tests (supplement section 3.3) | Untested backups (POAM-019) |
| Common control inheritance | Not addressed | Division must document inheritance (POL-01 4.6) | Gap 4 (POAM-016) |
| AI use | Not addressed | AI inventory and approval (POL-01 4.12) | AI scribe pilot without required consent field |

**Why the drift happened.** The acquisition integration plan covered identity and network migration but assigned no owner to policy alignment. **Fix:** the Student Health security and compliance lead owns the re-issue (due 2026-11-30), and the Group CISO's policy office now tracks supplement versions in the policy register.

## 5. Attestation
Each division security and compliance lead signs an annual statement: "The division supplement does not weaken any group policy and reflects all group policy changes made in the last 12 months." The first attestations are due 2026-12-31 (Higher Education, Education Software) and on re-issue (Student Health).
