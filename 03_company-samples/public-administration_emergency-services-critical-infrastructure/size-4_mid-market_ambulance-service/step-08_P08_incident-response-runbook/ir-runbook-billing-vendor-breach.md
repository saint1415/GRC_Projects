# Incident Response Runbook: Billing Platform Vendor Breach

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (licensed private ambulance service; PE-backed) |
| Tier / Vertical | Mid-Market / Emergency Services |
| Incident type | A cyberattack at the billing platform vendor (SYS-03) exposes company PHI and the PHI of the 4 municipal billing services clients, and may take the platform offline. The company is a **covered entity** for its own patients and a **business associate** (and Florida third-party agent) for its clients |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile); CSF GV.SC-08 (suppliers included in incident planning) |
| Policy basis | POL-03 Incident Response Policy (4.1, 4.5 to 4.7); STD-03 Vendor risk management standard |
| Companion documents | `ir-runbook.md` (CAD ransomware); `notification-matrix.csv`; BIA (P05 BP-08, BP-09, BP-10); risk register (P01 R-013, R-014, R-047); client BAAs |
| Runbook owner | Compliance and Privacy Officer (privacy lead) with the Director of Revenue Cycle (business lead) and the Security Manager (security lead) |
| Approved | 2026-09-16 by the Chief Operating Officer |
| Last tested | Not yet. Tabletop with 2 billing services clients scheduled 2027-02-17 (POAM-014) |

## 0. Why this runbook exists
One billing platform holds every company claim and every claim the company bills for 4 municipal fire-rescue departments. About $1.87 million of company collections and about $1.0 million of client collections flow through it each week (P05 BP-08, BP-09). A breach there creates two sets of duties at once:
- **As a covered entity**, the company must decide whether its own patients' PHI was breached and give its own notices (45 CFR 164.404 to 164.408; Fla. Stat. 501.171).
- **As a business associate and a Florida third-party agent**, the company must tell each affected client quickly and give it everything it needs for the client's own notices (45 CFR 164.410; client BAAs; Fla. Stat. 501.171(6)(a)). The clients, not the company, are the covered entities for their patients.

Missing a client deadline would break the client BAAs and the trust the billing services line depends on (P01 R-044).

## 1. Roles (Govern)
| Role | Primary | Backup | Responsibility |
|---|---|---|---|
| Privacy lead | Compliance and Privacy Officer | Outside breach counsel | Decision log, breach determinations, all notices, client communication on privacy |
| Business lead | Director of Revenue Cycle | Chief Financial Officer | Claims workarounds, client service, payer contact, backlog |
| Security lead | Security Manager | Director of IT | Cut and later re-establish connections; assess spread into company systems |
| CMT chair | Chief Operating Officer | Chief Executive Officer | Declares severity 1; approves spending and statements |
| Finance | Chief Financial Officer | Controller | Cash-flow forecast for the company and the clients; credit line; lender updates |
| Legal | Outside breach counsel (insurer panel); company's outside general counsel for contract rights | n/a | Privilege, agency question, notice review, client contract remedies, vendor claims |
| Client liaison | Director of Revenue Cycle | Director of Government Contracts | One named contact per client; daily status calls |
| Communications | Chief Operating Officer | Outside crisis PR (through counsel) | Staff, patient, and media messages |

## 2. Detection and declaration (Detect / RS.MA)
| Trigger | Source | Action |
|---|---|---|
| Vendor notice of a security incident or breach (BAA; 164.410; Fla. Stat. 501.171(6)(a)) | Vendor letter or call | **Severity 1.** Record the time received; isolate connections (step 3.1); notify the Compliance and Privacy Officer |
| Vendor status page or industry alert of a cyberattack on the vendor | Vendor; Health-ISAC; news | Treat as a possible breach; request a written statement; isolate connections |
| Claims, eligibility, or remittance transactions failing for more than 2 hours | Integration engine monitoring; billing staff | Confirm with the vendor; open a vendor incident (severity 3 until a security cause is ruled out) |
| Unusual sign-ins to billing workspaces, or client data seen in the wrong workspace | Billing staff; identity provider alerts | Severity 2; security lead investigates; privacy lead assesses |
| A client reports its own patient data exposed through the platform | Client privacy officer | Severity 1; treat the client's report as possible discovery |

**Severity levels (POL-03 4.5):**
- **Severity 3:** outage under 24 hours with no data concern. The business lead manages it.
- **Severity 2:** outage expected to exceed 24 hours, or a suspected security incident without confirmed data access.
- **Severity 1:** any vendor breach affecting company or client PHI, or an outage expected to exceed the 72-hour MTD for BP-08 or BP-09. Convene the crisis management team within 2 hours.

**Record two times in the decision log:** when the company first learned of the vendor incident, and when the vendor says it discovered it. Under 164.404(a)(2) and 164.410(a)(2), discovery runs from when a breach is known, or by reasonable diligence would have been known, to a workforce member or **agent**, determined under the federal common law of agency. Counsel decides on day 0 whether the vendor acts as the company's agent, because that could move the company's discovery date back to the vendor's.

## 3. First 72 hours (RS.MA, RS.MI)
| Time | Step | Who | Done when |
|---|---|---|---|
| 0-1 h | **3.1 Isolate the connection:** disable the integration engine export to the platform, revoke the platform's API credentials, and block its address ranges at the cloud firewall. Keep staff sign-in disabled until the vendor confirms the cause | Security lead | Channels disabled; firewall rules in place |
| 0-1 h | Call the cyber insurer hotline; counsel engaged | Chief Operating Officer | Claim number; counsel on the call |
| 0-2 h | Written request to the vendor: what happened, when it was discovered, which workspaces and data elements are affected, indicators of compromise, containment status, expected restoration date, and the vendor's own Florida 10-day and HIPAA notice timing | Privacy lead | Request sent; tracked in the decision log |
| 0-4 h | Hunt for the vendor's indicators in company logs (SIEM, integration engine, identity provider); reset any shared credentials | Security lead with the MSSP | Hunt results recorded |
| 0-4 h | Start claims workarounds (section 4) | Business lead | Workarounds running |
| 0-24 h | **First call with each client's privacy officer and finance lead.** Share what is known, what is not, the expected timeline, and the client liaison's name. Do not speculate. This call does not replace the written notices in section 5 | Privacy lead with the client liaison | 4 calls held and minuted |
| 4-24 h | Cash-flow forecast for 1, 2, 4, and 6 weeks of outage, for the company and for each client | Chief Financial Officer | Forecast to the CMT |
| 24-72 h | Build the **affected individuals list**, split by: company patients versus each client's patients; data elements; state of residence. Use the vendor's file and the company's own exports to check it | Privacy lead with the Director of Revenue Cycle | List version 1 in the decision log |
| 24-72 h | Staff message to billing and field staff: what is affected, workarounds, where to send patient calls | Communications | Message sent |

## 4. Business continuity workarounds (RC.RP)
| Process (P05) | Workaround | Capacity and limits |
|---|---|---|
| BP-08 Company billing | Queue trips in the ePCR export; submit high-dollar Medicare and Medicaid claims through payer portals; track each payer's filing limit | Payer portals cover about 70% of dollars; about 3 times slower |
| BP-09 Client billing | Queue client claims; daily status call with each client; portal submission for each client's highest-value claims only with that client's written agreement | Service credits may apply under the client agreements after 5 business days |
| BP-10 PCS intake | Keep receiving by cloud fax; attach to the billing record after restoration | No limit |
| Patient payments | Pause patient statements; the hosted payment page is part of the vendor platform | Patient calls routed to a script |

If the outage will exceed 2 weeks, the CFO and the Director of Revenue Cycle present the option of a temporary second billing platform to the CMT, including client consent and BAA requirements.

## 5. Legal and notification decisions (RS.CO)
**Follow `notification-matrix.csv`.** Outside counsel confirms every notice before it goes out. The Compliance and Privacy Officer keeps the decision log (POL-03 4.6).

| Decision point | Question | Decider | Record |
|---|---|---|---|
| D1 | Was company or client PHI acquired, accessed, used, or disclosed? Presumed a breach unless a four-factor assessment (45 CFR 164.402) shows a low probability of compromise | Privacy lead with counsel | Four-factor assessment for company data, and a separate factual summary per client |
| D2 | Discovery dates: when the company knew, and whether the vendor is its agent (section 2) | Counsel | Decision log |
| D3 | Florida determination date for company data (Fla. Stat. 501.171(4)) and for the company's role as third-party agent (501.171(6)(a)) | Privacy lead with counsel | Decision log |
| D4 | Which clients are affected, and how many individuals per client | Privacy lead with the business lead | Affected list split by client |
| D5 | Does any client BAA delegate patient notices to the company? (Today none does; each client sends its own notices with the company's help) | Counsel | Client BAA review |
| D6 | Company thresholds: 500 for HHS contemporaneous notice and the Florida Department of Legal Affairs; more than 500 residents of a state for media; more than 1,000 for consumer reporting agencies | Privacy lead | Affected list |
| D7 | Law enforcement delay requested (164.412)? | Counsel | Decision log |
| D8 | Contract remedies against the vendor; whether to suspend or replace the platform | Chief Operating Officer with counsel | CMT minutes |

**Notice timeline (plan to the shortest clock):**
| When | Action | Owner |
|---|---|---|
| Day 0 | Insurer notice through the hotline | Chief Operating Officer |
| Day 0-1 | Verbal briefing to each affected client (section 3) | Privacy lead |
| Within 10 days of determination | **Written third-party agent notice to each affected client** under Fla. Stat. 501.171(6)(a), with all information the client needs for its own notices | Privacy lead with counsel |
| Within 10 business days of discovery | **Written business associate notice to each affected client** under its BAA, which also meets the HIPAA outer limit of 60 days (164.410), listing each affected individual as soon as identified, and supplemented as facts develop | Privacy lead with counsel |
| Within 30 days of determination | Florida notice to the company's own affected patients (or the HIPAA notice with a copy to the Department of Legal Affairs under the deemed-compliance path); Department of Legal Affairs notice if 500 or more of the company's patients in Florida | Privacy lead with counsel |
| Without unreasonable delay, no later than 60 days after discovery | HIPAA notices to the company's affected patients; HHS notice at the same time if 500 or more; media notice if more than 500 residents of a state | Privacy lead with counsel |
| Without unreasonable delay | Consumer reporting agencies if the company's Florida notice goes to more than 1,000 individuals at once | Counsel |
| As each client requires | Supply mailing files, call center scripts, and fact sheets so each client can send its own notices; coordinate wording so patients get consistent information | Privacy lead |
| Each other state | Apply each state's law to affected residents of other states (company patients; for client patients, the client decides with the company's data) | Counsel |

**Inbound vendor duties.** The vendor owes the company notice under its BAA and 164.410, and Florida third-party agent notice within 10 days of its own determination (501.171(6)(a)). Late or incomplete vendor notices are recorded for contract remedies, but they never extend the company's own deadlines to its clients.

**Ransom.** If the vendor is extorted, the company does not negotiate or pay on the vendor's behalf. If the vendor asks the company to contribute, the ransom procedure in `ir-runbook.md` section 7 applies, including the OFAC sanctions check.

## 6. Recovery and reconnection (RC.RP, RC.CO)
1. Reconnect only after the vendor provides a written attestation of containment and eradication, indicators of compromise, and, where available, its forensic firm's summary.
2. Issue new API credentials; restore the integration engine export with a test batch; re-enable staff sign-in with MFA and a password reset.
3. Review workspace permissions with the vendor before reopening client workspaces (POAM-020).
4. Clear the claims backlog in this order: Medicare and Medicaid claims nearest their filing limits, then high-dollar commercial claims, then client claims by each client's agreed priority.
5. Confirm with each client that its backlog is cleared, and send a written closing summary to each client.

## 7. Post-incident (ID.IM)
- Lessons-learned meeting within 14 days of recovery, with each affected client invited; written report within 30 days (POL-03 4.11).
- Update the risk register (P01 R-013, R-014, R-044, R-047), the vendor's tier review (P09 `vendor-soc2-review.csv`), and the POA&M (P07).
- Decide at the CMT whether to keep the vendor, add a secondary platform, or exit, and record the decision.
- Retain the decision log, client notices, and vendor correspondence for 6 years (POL-01 4.12; 45 CFR 164.414(b)).
