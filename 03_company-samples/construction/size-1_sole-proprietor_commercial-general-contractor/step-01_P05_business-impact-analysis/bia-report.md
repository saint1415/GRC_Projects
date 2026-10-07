# Business Impact Analysis: Cris Santos Company | Construction | Sole Proprietorship

**Organization:** Cris Santos Company (commercial and institutional building general contractor) | **Tier:** Sole Proprietorship (owner only, 0 employees) | **Method:** NIST SP 800-34 Rev. 1 BIA template, short form
**Prepared by:** Owner, 2026-07-14, with the on-call IT technician reviewing systems on 2026-07-15 | **Adopted:** Owner, 2026-08-31

## 1. Overview and purpose
This one-page BIA lists the five business functions the company depends on, how long each can be down, and how much data each can lose. It feeds:
- the availability rating and contingency controls in the system security plan (P02);
- the impact ratings in the risk register (P01);
- the recovery order in the business email compromise runbook (P08).

No federal rule requires this BIA. FAR 52.204-21 has no contingency requirement. The owner does it because one lost phone, one locked account, or one diverted payment can stop the whole business.

## 2. Business description
One owner runs 2 to 4 small renovation jobs at a time from a home office in Florida and subcontracts all trade work. Billing is about $15,000 in a typical month. One job (FC-1) is a VA clinic renovation that brings federal payment, wage, and safeguarding clauses. Everything runs on SaaS (project management and pay apps, accounting, email), one laptop, one phone, and a home network. See `../00_company-facts.md` sections 1 to 3.

## 3. Impact categories and values
Dollar values are scaled to about $180,000 in annual receipts. Much of each payment passes through to subcontractors, so the owner's own margin on a $15,000 month is small.

| Category | Severe | Moderate | Minimal |
|---|---|---|---|
| Cost | More than $10,000 (most of a month's billing) | $2,000 to $10,000 | Less than $2,000 |
| Operations | Jobsites stop or subcontractors walk off | Work slowed or rescheduled | Office delay only |
| Regulatory | Federal contract breach, false representation, or reportable data breach | Missed federal deadline (certified payroll, prompt payment) | Internal rule deviation |
| Safety | Plausible injury from building to wrong drawings | Delayed but safe work | None |
| Reputation | Lost client, lost prime contractor, or subcontractors refuse future work | Complaints | None outside the company |

## 4. Process criticality and downtime (from `bia.csv`)
| Process | Criticality | MTD | RTO | RPO |
|---|---|---|---|---|
| BP-01 Progress billing and collections | High | 120 h | 48 h | 24 h |
| BP-02 Subcontractor and supplier payments | High | 120 h | 48 h | 24 h |
| BP-03 Project coordination and document control | High | 24 h | 8 h | 4 h |
| BP-04 Estimating and bidding | Moderate | 24 h (bid weeks) | 8 h | 24 h |
| BP-05 Business administration and federal compliance | Low | 168 h | 72 h | 24 h |

**What drives the values:**
- **Jobsites set the shortest clock.** Subcontractor crews need current drawings and answers to RFIs every working day, so BP-03 has a 24-hour MTD. The 4-hour RPO depends on the project management vendor's backups (confirmed in its SOC 2 report, P09).
- **Payments are about integrity more than downtime.** Billing and payables can wait a few days. The real harm is a payment sent to the wrong account, which is almost never recovered. That is why P01 rates business email compromise as the top risk even though BP-01 and BP-02 tolerate 120 hours of downtime.
- **Federal clocks.** On FC-1, subcontractors must be paid within 7 days of the Government's payment (FAR 52.232-27(c)), and certified payrolls are due weekly (FAR 52.222-8(b)(1)).
- **Gap.** The 24-hour RPO for BP-04 is **not supported today**: estimates, scanned lien waivers, and W-9 forms on the laptop have no backup (P01 R-012).

**Single-person dependency (the key finding).** The owner is the only estimator, superintendent, biller, payer, bank signer, and SAM Entity Administrator. Every second factor (email text codes, bank app, government sign-in authenticator) is on one phone. A jobsite injury or a lost phone puts every function past its MTD at once, and nobody else can pay subcontractors or reach the clients. Actions (P01 R-010, due 2026-12-31):
1. Sign a standby agreement with another small general contractor to keep active jobsites supervised for up to 2 weeks.
2. Store recovery codes and a one-page emergency access sheet in a sealed envelope held by the owner's attorney.
3. Ask the bank to add a trusted family member as a limited authorized signer, or record why not.
4. Add a second sign-in method (a security key kept in the home office safe) to email and the government sign-in service.

## 5. Resource requirements
| Resource | Description | Supports |
|---|---|---|
| SYS-05 Smartphone | Every second factor; email; bank app; jobsite photos; phone tethering for internet | All |
| SYS-01 Project management and pay app SaaS | Drawings, RFIs, daily logs, pay apps; vendor backups | BP-01, BP-03 |
| SYS-03 Email and files | Pay apps, lien waivers, subcontractor invoices and quotes | BP-01, BP-02, BP-03, BP-04 |
| SYS-07 Business online banking | ACH and wires; bank app approvals | BP-02 |
| SYS-04 Laptop | Estimates, pay app preparation, scanned documents (no backup) | BP-01, BP-04 |
| SYS-02 Accounting SaaS | Invoices, bills, vendor bank details, 1099s | BP-01, BP-02, BP-05 |
| SYS-08 Federal portals | SAM (EFT), federal invoicing, SPRS (planned) | BP-01, BP-05 |
| SYS-06 Home office network | Internet for the laptop; phone tethering is the fallback | BP-01, BP-04 |
| People | Owner only; outside bookkeeper (monthly); on-call IT technician | All |

## 6. Recovery priorities
| Priority | Resource | Expected recovery time | Alternate strategy |
|---|---|---|---|
| 1 | Owner access: phone and second factors | 2 h | Recovery codes in the sealed envelope; replacement phone from the carrier; security key (planned) |
| 2 | Internet | 1 h | Phone tethering (the covered hotspot is no longer used) |
| 3 | SYS-01 project records | 8 h (vendor-hosted) | Printed plan sets in the truck; phone app |
| 4 | SYS-03 email | 8 h | Phone calls to clients and subcontractors at numbers in the contracts |
| 5 | A clean laptop | 24 h | The February 2026 laptop, wiped and updated as a spare (POL-01 8.6); IT technician rebuilds the main laptop |
| 6 | SYS-07 bank and SYS-02 accounting | 48 h | Paper checks; call-back verification before any payment |
| 7 | SYS-08 federal portals | 72 h | Phone the FC-1 Contracting Officer and paying office |
