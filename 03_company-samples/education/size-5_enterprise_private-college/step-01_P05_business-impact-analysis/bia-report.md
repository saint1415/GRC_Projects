# Business Impact Analysis: Cris Santos Company | Educational Services | Enterprise

**Organization:** Cris Santos Company, Inc. (publicly traded postsecondary education company operating a private, for-profit college) | **Tier:** Enterprise (12,000 employees) | **Method:** NIST SP 800-34 Rev. 1 BIA template, informed by NIST IR 8286D
**Prepared by:** GRC team with process owners, 2026-06-01 to 2026-07-15 | **Approved:** Chief Operating Officer and Chief Risk Officer, 2026-08-14 | **Reported to:** board risk committee, 2026-09-10

## 1. Overview and purpose
This enterprise-wide BIA identifies the business processes the company depends on, how long each can be down, how much data each can lose, and what each depends on, including third parties, the Department of Education's systems, and the two service lines offered to other organizations. It feeds:
- the contingency and disaster recovery plans for tier-1 systems, including the Student Records and Learning Platform (SRLP);
- the written incident response plan required by the FTC Safeguards Rule (16 CFR 314.4(h)), which must help the company recover from security events;
- the availability rating and recovery objectives in the SRLP System Security Plan (P02);
- impact ratings in the enterprise risk register (P01), per NIST IR 8286D;
- the recovery order in the ransomware runbook (P08);
- the Availability criteria for the two SOC 2 service lines (P09).

**Results in one line:** 17 processes were analyzed; 7 are High criticality, 9 Moderate, and 1 Low. 7 processes need recovery within 8 hours, 2 of them within 4 hours. The dependency map (`dependency-map.csv`) lists 26 dependencies, 12 of them single points of failure and 6 never tested.

## 2. System and business description
Cris Santos Company operates one accredited private, for-profit college with a main campus in Florida, 22 additional locations in six states (23 campuses), and an online division that enrolls students in all 50 states and DC. It has 12,000 employees, about 285,000 enrolled students (about 238,000 online), and about $4.8 billion in annual receipts, of which about $3.2 billion is Title IV aid. The technology estate is described in `../00_company-facts.md` section 3: a customer-managed SIS on Cloud provider A (SYS-01), a multi-tenant SaaS LMS (SYS-02), the student portal and mobile app (SYS-03), the Department of Education connections (SYS-04), the identity platform (SYS-05), the admissions CRM (SYS-06), the data and analytics platform on Cloud provider B (SYS-07), one colocation data center (SYS-08), SD-WAN for 28 sites (SYS-09), about 22,300 endpoints (SYS-10), ERP and payroll (SYS-11), and about 1,100 vendors (SYS-14). Two service lines serve other organizations: SL-1 Workforce Education Services (about 310 employer clients) and SL-2 Online Program Services (14 partner institutions).

## 3. Impact categories and values
Dollar thresholds are scaled to about $13.2 million of receipts per calendar day and to the company's materiality framework (P08 section 6). Values are per 24 hours of outage unless stated.

| Category | Severe | Moderate | Minimal |
|---|---|---|---|
| Cost | More than $1 million per day, or more than $10 million cumulative | $100,000 to $1 million per day | Less than $100,000 per day |
| Operations | Instruction or a tier-1 student service stops for all online students or at more than 5 campuses | One service line, one state, or up to 5 campuses stop | Staff slowed but working |
| Regulatory | Missed Title IV deadline (for example, credit balance refunds), reportable breach of 500 or more consumers, Clery emergency notification failure, missed SEC filing | Missed contractual or documentation deadline; breach under 500 | Internal policy deviation |
| Safety | Plausible harm to people on campus (emergency notification or access control failure) | Delayed but safe operations (clinical placements, labs) | None |
| Reputation | National media, analyst or ratings action, accreditor or regulator inquiry, or loss of partner or employer contracts | Regional media; client complaints | Internal only |

## 4. Process criticality and downtime (from `bia.csv`)
| Process | Criticality | MTD | RTO | RPO | Quantified impact per 24 h |
|---|---|---|---|---|---|
| BP-13 Campus safety and emergency notification | High | 1 h | 30 min | 24 h | $0.05M |
| BP-03 Registration, enrollment status, and academic records | High | 24 h | 8 h | 15 min | $2.40M |
| BP-04 Financial aid processing | High | 72 h | 24 h | 15 min | $8.80M (deferred Title IV cash) |
| BP-01 Online instruction and course delivery | High | 24 h | 8 h | 1 h | $5.90M |
| BP-12 Online Program Services for partner institutions (SL-2) | High | 24 h | 8 h | 1 h | $0.45M |
| BP-05 Disbursement and credit balance refunds | High | 72 h | 48 h | 15 min | $0.60M |
| BP-06 Admissions, inquiries, and enrollment advising | High | 24 h | 8 h | 1 h | $2.60M |
| BP-07 Student support center and 24x7 technical help desk | Moderate | 12 h | 4 h | 24 h | $0.40M |
| BP-02 Campus instruction and clinical placements | Moderate | 48 h | 24 h | 4 h | $1.10M |
| BP-08 Student portal and mobile app | Moderate | 24 h | 8 h | 1 h | $0.50M |
| BP-11 Workforce Education Services employer portal and invoicing (SL-1) | Moderate | 48 h | 12 h | 1 h | $0.35M |
| BP-09 Assessments and online proctoring | Moderate | 48 h | 24 h | 1 h | $0.30M |
| BP-14 Payroll and HR, including adjunct contracts | Moderate | 72 h | 48 h | 24 h | $0.20M |
| BP-15 Financial close and SEC reporting | Moderate | 120 h | 72 h | 24 h | $0.15M |
| BP-10 Transcripts, enrollment verification, and records release | Moderate | 120 h | 72 h | 24 h | $0.10M |
| BP-16 Tuition billing, payment plans, and collections | Moderate | 168 h | 72 h | 24 h | $0.70M |
| BP-17 Learning analytics and student-success outreach | Low | 168 h | 72 h | 24 h | $0.05M |

The table is in recovery priority order (`recovery_priority` in `bia.csv`).

**What drives the values:**
- **Safety and Clery** set the shortest MTD. When a significant emergency or dangerous situation is confirmed, the College must immediately notify the campus community (34 CFR 668.46(g)(1)). The emergency notification service has redundant carriers, and campus public address systems are the fallback.
- **Instruction and enrollment status** drive the 24-hour MTDs for online instruction (BP-01), registration (BP-03), and the SL-2 partners (BP-12). Online courses run in 8-week sessions with weekly deadlines, and enrollment status drives Title IV eligibility.
- **Title IV deadlines** set the refund objectives. Credit balances must be paid no later than 14 days after they occur (34 CFR 668.164(h)(2)); refunds peak in the week after each session start, so BP-05 has a 72-hour MTD.
- **Cash, not time,** drives financial aid processing (BP-04). Each day of outage defers about $8.8 million of Title IV funds, but the work can catch up within the session, so the MTD is 72 hours.
- **Contracts** set the SL-1 and SL-2 objectives (P09). SL-2 partner contracts commit to an 8-hour LMS recovery; SL-1 employer contracts commit to 99.9% monthly availability.
- **Regulation** tightens financial close (BP-15) in the quarter-end window, when its MTD drops to 48 hours because of SEC filing deadlines.

## 5. Dependency mapping and third parties
The full map is in `dependency-map.csv`. Key findings:

1. **LMS concentration (DEP-01).** One SaaS LMS carries all online instruction for the College and for all 14 SL-2 partners. Its contract RTO is 24 hours against the BIA RTO of 8 hours for BP-01 and BP-12, and the vendor will not support a customer-observed failover test. This is P01 risk R-011 and POA&M item POAM-007.
2. **SIS recovery (DEP-03).** The SIS met its 15-minute RPO but recovered in 11.5 hours against its 8-hour RTO in the 2026-04-25 DR test, mainly because the integration services and the SAIG transmission servers were rebuilt by hand. This is P01 R-010 and POAM-006.
3. **Legacy document imaging (DEP-16).** About 14 million scanned verification and tax documents sit in a colocation system on an unsupported operating system, outside the immutable backup design, with no tested restore. This is P01 R-007 and POAM-008.
4. **Telephony and refunds (DEP-11, DEP-14).** The contact-center telephony core and the bank refund file are single points of failure with untested fallbacks. The cloud contact-center failover is configured but has never been tested, and the secondary bank's refund file format has never been tested.
5. **Title IV third-party servicer (DEP-08).** Its contract allows 10 days for incident notice, which is too slow for the FTC 30-day clock and the FSA "immediately" expectation (P03 G-031; POAM-021).
6. **Industry-wide dependency (DEP-06).** The Department of Education's systems are a single point of failure the company cannot remove; the workaround is procedural (queue and catch up).

## 6. Resource requirements
| Resource / component | Description | Supports process |
|---|---|---|
| SYS-01 SIS | Customer-managed on Cloud provider A; system of record for enrollment, grades, student financials, and financial aid | BP-02 to BP-05, BP-08, BP-10, BP-11, BP-15, BP-16 |
| SYS-02 LMS | Vendor SaaS; College tenant plus 14 partner tenants | BP-01, BP-02, BP-09, BP-12, BP-17 |
| SYS-03 Student portal and mobile app | Company-built on Cloud provider A managed containers | BP-03, BP-05, BP-08 |
| SYS-04 Department of Education connections | Two SAIG transmission servers; individually issued staff accounts | BP-04, BP-05 |
| SYS-05 Identity platform | Workforce and student SSO, MFA, PAM, identity governance | All |
| SYS-06 Admissions CRM | Vendor SaaS | BP-06 |
| SYS-07 Data and analytics platform | Cloud provider B | BP-17 |
| SYS-08 Colocation data center | Legacy imaging, telephony core, offline backup copy | BP-04, BP-05, BP-06, BP-07; recovery of all |
| SYS-09 Enterprise network | SD-WAN with cellular failover at 28 sites | All campus-based processes |
| SYS-10 Endpoints | Workforce laptops; campus lab computers | All |
| SYS-11 ERP, HR, and payroll | Vendor SaaS | BP-14, BP-15, BP-16 |
| SYS-12 Online proctoring | Vendor SaaS | BP-09 |
| SYS-13 Campus safety systems | Emergency notification service, access control, CCTV | BP-13 |
| Immutable backups | Separate backup accounts in both clouds with write-once retention; weekly offline copy to the colocation data center | RPO for all Cloud A and B workloads |
| People | Faculty, registrar, financial aid, student finance, enrollment, support center, SOC, IT operations | All |

## 7. Recovery priorities
| Priority | Resource | Expected recovery time | Alternate strategy |
|---|---|---|---|
| 1 | Emergency notification service and campus safety systems (SaaS, redundant carriers) | 30 min | Campus public address systems; phone trees |
| 2 | SYS-05 identity platform and break-glass accounts | 1 h | Sealed break-glass accounts; secondary region |
| 3 | Network core, SD-WAN, DNS, and cloud connectivity | 2 h | Cellular failover at sites |
| 4 | Security tooling (EDR console, SIEM) for clean-room validation | 2 h | Managed security service provider tooling |
| 5 | Telephony and the student support center | 4 h | Cloud contact-center failover (untested); overflow vendor |
| 6 | SYS-01 SIS (registration, academic records) and integration services | 8 h (11.5 h demonstrated) | Printed rosters; paper add/drop log |
| 7 | SYS-02 LMS access for the College and SL-2 partner tenants (vendor recovery) | 8 h target (24 h per vendor contract) | Read-only course packets; deadline extensions |
| 8 | SYS-03 student portal and mobile app | 8 h | Support center acts for students |
| 9 | SYS-06 admissions CRM | 8 h | Queued web forms; exported call lists |
| 10 | SL-1 employer portal | 12 h | Secure file transfer of progress reports |
| 11 | SYS-04 SAIG transmission servers and financial aid processing | 24 h | Department web systems for urgent cases |
| 12 | SYS-12 online proctoring | 24 h | Alternative assessments |
| 13 | Refund processing (student financials and bank files) | 48 h | Paper checks through the bank portal |
| 14 | SYS-11 ERP, HR, and payroll | 48 h | Repeat prior payroll |
| 15 | Transcripts, verification, billing, and payment plans | 72 h | Manual transcripts; processor keeps taking payments |
| 16 | SYS-07 data and analytics platform | 72 h | Last published outreach lists |
| 17 | Legacy document imaging system | Unknown (never tested) | Documents re-requested from students |

## 8. Gaps carried to other deliverables
| Gap | Carried to |
|---|---|
| LMS contract RTO 24 h against an 8 h BIA RTO; no observed failover test | P01 R-011; P02 CP-2; POAM-007 |
| SIS recovered in 11.5 h against an 8 h RTO | P01 R-010; P02 CP-10; POAM-006 |
| Legacy imaging system: unsupported, outside immutable backups, never restore-tested | P01 R-007; POAM-008 |
| Telephony failover and secondary bank refund file never tested | P01 R-031 |
| Title IV third-party servicer 10-day incident notice term | P03 G-031; POAM-021 |
| Annual emergency notification test does not include an IT outage scenario | P03 G-062; POAM-024 |
