# Business Impact Analysis: Cris Santos Company | Financial Services | Sole Proprietorship

**Organization:** Cris Santos Company (independent insurance agency) | **Tier:** Sole Proprietorship (owner-agent only, 0 employees) | **Method:** NIST SP 800-34 Rev. 1 BIA template, short form
**Prepared by:** Owner-agent, 2026-08-03, with the on-call IT consultant (services agreement since 2026-07-27) | **Adopted:** Owner-agent, 2026-09-14

## 1. Overview and purpose
This one-page BIA lists the five business functions the agency depends on, how long each can be down, and how much data it can lose. It supports:
- the availability rating in the system profile (P02);
- impact ratings in the risk register (P01);
- the recovery order in the incident runbook (P08);
- the records duty in Fla. Stat. 626.748 (policy records readily accessible for 5 years after expiration) and the premium trust fund duty in 626.561.

## 2. Business description
One licensed agent sells and services property and casualty insurance for about 510 households and 130 small businesses from a home office in Florida. The insurers underwrite, bill most policies, and pay claims; the agency quotes, binds within its authority, services policies, helps with claims, and invoices about 60 commercial policies through its premium trust account. Records live in a SaaS agency management system (AMS, SYS-01); everything else runs through email, insurer portals, a laptop, and a phone. See `../00_company-facts.md` sections 1 to 3.

## 3. Impact categories and values
Dollar values are scaled to about $180,000 in annual commissions, or about $720 per business day.

| Category | Severe | Moderate | Minimal |
|---|---|---|---|
| Cost | More than $3,600 (about a week of commissions), or any loss of trust funds | $720 to $3,600 | Less than $720 |
| Operations | Clients cannot get coverage, proof of insurance, or claims help | Service slowed; some work deferred | Administrative delay only |
| Regulatory | Reportable breach; trust fund shortfall; insurer contract breach | Missed records or notice step | Internal policy deviation |
| Reputation | Loss of an insurer appointment or of commercial clients | Complaints or online reviews | None outside the agency |

Safety is marked N/A: the agency's outages delay service but do not create physical harm.

## 4. Process criticality and downtime (from `bia.csv`)
| Process | Criticality | MTD | RTO | RPO |
|---|---|---|---|---|
| BP-01 Policy service and binding | High | 24 h | 8 h | 4 h |
| BP-02 Claims help | High | 24 h | 8 h | 24 h |
| BP-03 Premium collection and trust accounting | Moderate | 72 h | 24 h | 24 h |
| BP-04 New business and renewals | Moderate | 120 h | 72 h | 24 h |
| BP-05 Agency administration and records | Low | 168 h | 120 h | 24 h |

**What drives the values:** BP-01 and BP-02 are High because a client closing on a house or reporting storm damage cannot wait days, and the agent is the client's first call. BP-03 has a longer MTD but the most severe cost impact: a single redirected payment (the 2026-07-08 near miss was $18,400) is about 25 business days of commissions and leaves a client's policy unpaid. The 4-hour RPO for BP-01 depends on the AMS vendor's backups (P09 vendor review). The 24-hour RPO for BP-05 is **met only while the AMS vendor holds the data**: no export exists, and email and files keep only 30 days (P01 R-013, R-014).

**Single-person dependency (the key finding).** The owner is the only licensed person, the only person who can bind or change coverage (Fla. Stat. 626.112(1) bars unlicensed people from soliciting or advising), and the only holder of the AMS, email, insurer portal, and banking credentials. The AMS and email second factors are on one phone. If the owner is injured, evacuated, or without the phone after a hurricane, BP-01 and BP-02 exceed their MTD at the moment clients need them most. Actions (P01 R-009, due 2026-12-31):
1. Sign a written emergency servicing arrangement with another licensed independent agent, and confirm with each insurer how that agent can serve the agency's clients.
2. Store the AMS, email, and banking recovery codes and a one-page emergency access sheet in a sealed envelope held by the owner's attorney.
3. Send clients a contact card listing each insurer's 24-hour claims line and service center.
4. Add a second authenticator device kept in the fire safe.

## 5. Resource requirements
| Resource | Description | Supports |
|---|---|---|
| SYS-01 AMS (vendor SaaS) | Client and policy records, documents, notes; vendor backups | BP-01, BP-02, BP-03, BP-04, BP-05 |
| SYS-06 Mobile phone | Second factor for AMS and email; calls; insurer portals | BP-01, BP-02, BP-03 |
| SYS-06 Laptop | Main work device | BP-01, BP-03, BP-04, BP-05 |
| SYS-07 Home network | Internet; the phone hotspot is the fallback | BP-01, BP-02, BP-04 |
| SYS-02 Email and files | Client correspondence, invoices, documents (30-day retention) | BP-01, BP-03, BP-04 |
| SYS-03 Insurer and partner portals | Quoting, binding, ID cards, claims reporting | BP-01, BP-02, BP-04 |
| SYS-05 Accounting and banking | Trust account deposits and remittances | BP-03, BP-05 |
| Contracted services | Bookkeeper (no written terms), IT consultant (terms since 2026-07-27) | BP-03, BP-05 |
| People | Owner-agent only | All |

## 6. Recovery priorities
| Priority | Resource | Expected recovery time | Alternate strategy |
|---|---|---|---|
| 1 | Owner access: phone and second factors | 1 h | Recovery codes in the sealed envelope; replacement phone from the carrier; second authenticator in the fire safe (planned) |
| 2 | Internet | 1 h | Phone hotspot |
| 3 | A clean access device | 4 h | Phone for portals; laptop rebuilt by the IT consultant |
| 4 | SYS-01 AMS | 8 h (vendor-hosted) | Insurer portals for ID cards, binders, and claims; paper notes |
| 5 | SYS-03 insurer portals | 8 h | Insurer service centers by phone |
| 6 | SYS-05 banking and SYS-02 email for invoices | 24 h | Branch deposits and remittances; phone clients at known numbers |
| 7 | SYS-04 e-signature and comparative rater | 72 h | Paper applications; quote in insurer portals |
