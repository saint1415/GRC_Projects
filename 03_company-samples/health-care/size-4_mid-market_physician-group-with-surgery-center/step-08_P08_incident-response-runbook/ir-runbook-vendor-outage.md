# Incident Response Runbook: Clearinghouse or Major Vendor Outage

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (PE-backed multi-specialty physician group with an ASC and an imaging center) |
| Tier / Vertical | Mid-Market / Health Care and Social Assistance |
| Incident type | Extended outage of a critical third party: primarily the **clearinghouse** (claims, eligibility, remittance); variants for the **EHR vendor**, the **PACS vendor**, and the **prior-authorization vendor**. The outage may be caused by a cyberattack on the vendor |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile); CSF GV.SC-08 (suppliers included in incident planning) |
| Policy basis | POL-03 Incident Response Policy (4.1, 4.4, 4.9); STD-03 Vendor risk management standard |
| Companion documents | `ir-runbook.md` (ransomware); `notification-matrix.csv`; BIA (P05 BP-10, BP-02, BP-11, BP-12); risk register (P01 R-012, R-013) |
| Runbook owner | Director of Revenue Cycle (business lead) with the Security Manager (security lead) |
| Approved | 2026-09-15 by the Chief Operating Officer |
| Last tested | Not yet. Vendor outage tabletop scheduled 2027-02-24 (POAM-013) |

## 0. Why this runbook exists
One clearinghouse carries all eligibility checks, claims, and remittances. About $1.9 million of expected collections flows through it each week (P05 BP-10). A multi-week clearinghouse outage is a cash-flow crisis first and a security incident second. If the vendor was attacked, it may also be a **breach of company PHI held by a business associate**. The EHR vendor is a similar single point of failure for clinical care (P01 R-013).

## 1. Roles (Govern)
| Role | Primary | Backup | Responsibility |
|---|---|---|---|
| Business lead | Director of Revenue Cycle | CFO | Claims workarounds, payer contact, backlog |
| Security lead | Security Manager | IT Director | Cut and later re-establish connections safely; assess exposure of company PHI |
| CMT chair (if escalated) | Chief Operating Officer | CEO | Declares a severity 1 vendor outage; approves spending and communications |
| Finance | Chief Financial Officer | Controller | Cash-flow forecast; credit line; lender and PE sponsor updates |
| Vendor management | Compliance and Privacy Officer | Director of Revenue Cycle | BAA terms, breach notices from the vendor, contract remedies |
| Legal | Company's outside general counsel; breach counsel if PHI is involved | n/a | Contract rights, notices, breach determination support |
| Clinical lead (EHR or PACS variant) | Chief Medical Officer | ASC Administrator; Imaging Center Director | Downtime procedures, case decisions, ASC emergency plan |
| Communications | Director of Marketing and Communications | n/a | Staff, provider, and patient messages |

## 2. Detection and declaration (Detect / RS.MA)
| Trigger | Source | Action |
|---|---|---|
| Clearinghouse status page or notice of an outage or cyber incident | Vendor; industry alerts (Health-ISAC, HHS) | Business lead opens a vendor incident; security lead assesses connections |
| Claim or eligibility transactions failing for more than 2 hours | Interface engine monitoring; CBO staff | Confirm with the vendor; open a vendor incident |
| Vendor reports a cyberattack or suspected data compromise | Vendor notice under the BAA (164.410) | **Immediately** cut connections (step 3.1); notify the Compliance and Privacy Officer |
| EHR vendor outage longer than 1 hour | Clinical staff; vendor status page | Clinical lead activates downtime; follow the EHR variant (section 7) |

**Severity levels:**
- **Severity 3:** outage under 24 hours with no data concern. The business lead manages it.
- **Severity 2:** outage expected to exceed 24 hours, or any vendor cyber incident. Security lead engaged, and the COO is informed.
- **Severity 1:** outage expected to exceed the 72-hour MTD for BP-10, or any vendor outage affecting clinical care beyond its MTD (EHR, PACS). Convene the crisis management team (POL-03 4.4).

**Record the time the company first learned of the vendor incident.** If the vendor's incident involves company PHI, that time matters for breach analysis (section 5).

## 3. First 24 hours (RS.MA, RS.MI)
| Time | Step | Who | Done when |
|---|---|---|---|
| 0-1 h | **3.1 Isolate the connection** if the vendor reports or may have a cyber incident: disable the interface engine channels and VPN or API credentials to the vendor; block its IP ranges at the cloud firewall | Security lead | Channels disabled; firewall rules in place |
| 0-2 h | Request a written incident statement from the vendor: what happened, whether company data is affected, indicators of compromise, and the expected restoration date | Compliance and Privacy Officer | Request sent; tracked in the decision log |
| 0-4 h | Hunt for the vendor's indicators of compromise in company logs (SIEM, interface engine, cloud firewall) | Security lead with the MSSP | Hunt results recorded |
| 0-4 h | Start manual workarounds (section 4) | Business lead | Workarounds running |
| 4-8 h | Cash-flow forecast for 1, 2, 4, and 6 weeks of outage | CFO | Forecast to the COO |
| 8-24 h | Decide whether to activate the **secondary clearinghouse** (contract target 2027-03-31, P01 R-012). Until then, set up payer-portal direct submission for the top 10 payers by volume | Business lead with the CFO | Decision documented |
| 8-24 h | Staff and provider communication: what is affected, workarounds, where to send questions | Communications | Message sent |

## 4. Business continuity workarounds (RC.RP)
| Process (P05) | Workaround | Capacity and limits |
|---|---|---|
| BP-02 Eligibility | Payer portals and phone; collect copays and estimate patient responsibility conservatively | About 3 times slower; front-desk overtime |
| BP-10 Claims | Queue claims in the practice management system; submit high-dollar claims (ASC and imaging first) directly through payer portals; track the filing deadline for each payer | Top 10 payers cover about 80% of dollars |
| BP-11 Remittance and posting | Download remittance files from payer portals; post manually | Posting lag is acceptable up to 120 hours (MTD) |
| BP-12 Prior authorization | Manual portal submissions, prioritizing cases within 72 hours | About 60% of normal volume |
| Cash | Draw on the revolving credit line; ask payers whether any advance or accelerated payment arrangements are offered; defer non-critical capital spend | CFO and CEO approve; lender notice if covenants require it |

**Trigger to escalate to severity 1:** projected cash shortfall within 3 weeks, or a backlog that will breach any payer's timely filing limit.

## 5. Legal and regulatory analysis (RS.CO)
**Follow `notification-matrix.csv`.** Counsel confirms each notice.

1. **Is company PHI involved?** The clearinghouse is a business associate. It must notify the company of a breach of unsecured PHI without unreasonable delay and no later than 60 days after discovery (45 CFR 164.410), including the identities of affected individuals. The company's BAA sets 5 business days for Tier 1 vendors after renewal (STD-03).
2. **When does the company's own clock start?** Under 164.404(a)(2), the company is deemed to know of a breach when any workforce member **or agent** knows (federal common law of agency). If the vendor acts as the company's agent, its discovery may count as the company's discovery. If it is an independent contractor, the company's clock generally starts when the vendor tells the company. Counsel makes this call and records it in the decision log (D2 in `ir-runbook.md`).
3. **Who notifies patients?** The duty to notify individuals, HHS, and the media rests with the covered entity (45 CFR 164.404-164.408). If the vendor offers to send notices on the company's behalf, counsel decides whether to agree in writing, and the company remains accountable for content and timing. Counsel coordinates with other affected covered entities if the vendor proposes a joint notice.
4. **Florida.** A third-party agent that maintains personal information for the company must notify the company within 10 days of determining a breach (Fla. Stat. 501.171). The company's 30-day individual notice clock and Department of Legal Affairs notice (500 or more Floridians) then apply, subject to the deemed-compliance path for HIPAA notices with a timely copy to the Department.
5. **Contracts.** Check the vendor agreement for service credits, termination rights, and data return. Notify the hospital joint venture partner if joint venture claims are affected (joint venture agreement). Notify lenders only if the credit agreement requires notice of a material disruption (CFO with counsel).
6. **No security incident at the company.** If the vendor outage is not a cyber incident and no company PHI is affected, there is no HIPAA or Florida notification duty. Document that conclusion in the decision log.

## 6. Reconnection (RC.RP)
Do not reconnect to a vendor that had a cyber incident until:
- [ ] the vendor provides written confirmation of containment and eradication, ideally with a third-party forensic attestation;
- [ ] the vendor's indicators of compromise have been searched for in company logs with no findings;
- [ ] credentials, certificates, and API keys for the connection are rotated;
- [ ] the connection is re-established with least privilege (only the required channels) and monitored by the MSSP for 30 days;
- [ ] the CMT chair (severity 1) or the Security Manager (severity 2) approves reconnection.

Then submit the queued claims in priority order (highest dollar and nearest filing deadline first), reconcile remittances, and track the backlog daily until it clears.

## 7. Variants
| Vendor | Key differences | Clinical and regulatory notes |
|---|---|---|
| **EHR vendor** (SYS-01) | Clinical impact within hours. Vendor RTO 12 h exceeds BIA RTO 2-4 h (P05 finding 1). Use downtime report workstations (hourly extract) and paper forms | ASC: the ASC Administrator decides on starting cases (MTD 4 h) and whether to activate the ASC emergency plan (42 CFR 416.54; POL-03 4.9). E-prescribing falls back to phone or paper where the law allows |
| **PACS vendor** (SYS-03, in the company's account) | Company controls the infrastructure and backups; the vendor controls the application | Modalities store about 3 days locally; urgent reads at consoles; teleradiology overflow; critical results by phone |
| **Prior-authorization vendor** (AI-004) | Manual portal submissions | Reschedule non-urgent ASC and imaging cases without authorization; tell patients early |
| **MSSP** (SYS-08) | Loss of 24x7 monitoring | Security analysts watch EDR and IdP consoles directly on extended hours; raise alert thresholds; tell the CMT the company is operating with reduced detection |

## 8. Post-incident (ID.IM)
- Lessons learned within 14 days of full restoration, including the cash impact and any timely filing losses.
- Update the risk register (P01 R-012, R-013), the vendor tier and review (P09 `vendor-soc2-review.csv`), and this runbook.
- Recalculate BIA values (P05) if the outage showed different impacts than estimated.
- Retain the decision log and vendor correspondence for 6 years (POL-01 4.12).
