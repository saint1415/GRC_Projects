# Incident Response Runbook: Compromise of Covered Defense Information (FC-4)

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (PE-backed commercial and institutional building general contractor) |
| Tier / Vertical | Mid-Market / Construction |
| Incident type | Cyber incident affecting covered defense information (CDI) on the FC-4 Army Corps of Engineers design-build contract. Variant 1: ransomware with data theft at the A&E design subcontractor. Variant 2: CUI found on an unauthorized system |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile), organized by CSF Functions |
| Policy basis | POL-03 Incident Response Policy (4.5 to 4.7, 4.9, 4.12); POL-04 CUI handling; STD-09 CUI handling standard |
| Contract basis | DFARS 252.204-7012(c) to (g) and (m)(2)(ii) in FC-4 and in the A&E subcontract (N23-R03); SP 800-171 Rev. 2 3.6.1 to 3.6.3 |
| Companion documents | `ir-runbook.md` (business email compromise); `notification-matrix.csv`; BIA (P05) BP-04; SSP (P02) section 7.2 |
| Runbook owner | Security Manager (incident commander); Director of Contracts and Compliance (DoD reporting lead) |
| Approved | 2026-09-17 by the Chief Operating Officer |
| Last tested | Not yet. CUI tabletop with a DIBNet reporting drill scheduled 2026-11-18 (POAM-013) |

## Why a separate runbook
The business email compromise runbook is about money and minutes. This one is about a contract clock: DFARS 252.204-7012 defines "rapidly report" as **within 72 hours of discovery of any cyber incident** (252.204-7012(a)), and the report can only be filed at https://dibnet.dod.mil with a DoD-approved medium assurance certificate ((c)(3)). It also requires preservation before rebuild ((e)), which reverses the usual instinct to restore fast. A "cyber incident" under the clause includes a **compromise**, and a compromise includes copying information to unauthorized media (252.204-7012(a)). That is why CUI found in the wrong place is handled here, not as a housekeeping issue.

## Scenarios
| Variant | What happens | Why it matters |
|---|---|---|
| **1. Ransomware with data theft at the A&E subcontractor** | The A&E firm's network is encrypted and the attacker posts a sample of FC-4 design sheets on a leak site. The A&E firm's 8 guest users also reach the CPE from their own laptops through the enclave virtual desktop gateway. | The A&E firm has its own duty to report to DoD within 72 hours and to give the company the DoD incident report number as soon as practicable (252.204-7012(m)(2)(ii), flowed down in the A&E subcontract). The company must find out whether **its** covered contractor information system (the CPE) was affected, and if so report its own incident |
| **2. CUI found on an unauthorized system** | CUI-marked FC-4 sheets are found in the commercial project platform (SYS-01), on a rugged tablet, in a mailbox, in personal email, or on a trade subcontractor's system that has no DFARS flowdown. This happened in 2026: 1,140 items in SYS-01 and offline sets on 26 tablets (P03 G-003, G-112) | The company must review for evidence of compromise ((c)(1)(i)) and decide whether a reportable cyber incident occurred. The review in progress is POAM-018 |

## 0. Governance, roles, and contacts (Govern)
| Tier | Members | Decides |
|---|---|---|
| **Crisis management team (CMT)** | Chair: Chief Operating Officer. CEO (CMMC Affirming Official), General Counsel, vCISO, CFO, Vice President of Operations, Director of Contracts and Compliance, FC-4 Project Executive; outside government contracts counsel | Contract and schedule impact on FC-4, relationship with the Army Corps of Engineers and the A&E firm, external statements, any effect on SPRS or CMMC representations |
| **Incident response team (IRT)** | Incident commander: Security Manager. IT Director, security analysts, panel forensic firm (through counsel), government-community cloud provider support, MSSP (corporate side only) | Containment, evidence preservation, the (c)(1)(i) review, eradication, recovery |
| **DoD reporting cell** | Lead: Director of Contracts and Compliance. Security Manager (second certificate holder), General Counsel, FC-4 Project Executive | Report content, filing at DIBNet, malware submission, contact with the Contracting Officer, subcontractor incident numbers |

| Role | Primary | Backup | How to reach |
|---|---|---|---|
| Incident commander | Security Manager | IT Director | Out-of-band group; printed call tree |
| DoD reporting lead (medium assurance certificate holder) | Director of Contracts and Compliance | Security Manager (second certificate, due 2026-10-09) | Out-of-band group |
| CUI custodian | FC-4 Project Executive | FC-4 senior Project Manager | Out-of-band group |
| Legal | General Counsel | Outside government contracts counsel; panel breach counsel through the carrier hotline | Out-of-band group |
| Cyber insurer | Carrier breach hotline | Broker | Policy card |
| A&E firm security contact | A&E firm's IT director (named in the subcontract security exhibit) | A&E principal in charge | Numbers in the FC-4 contract file |
| Government-community cloud provider | Provider security incident line (per the CRM) | Provider account team | CRM contact page in the incident binder |
| Contracting Officer (FC-4) | Army Corps of Engineers Contracting Officer | Contracting Officer's Representative | Numbers in the FC-4 contract file |
| Monitoring | Security analysts (CPE; monitoring service from 2027-01) | MSSP for corporate systems | Out-of-band group |
| Law enforcement | FBI field office | CISA | Numbers in the binder |

**Out-of-band first, and need to know.** Discuss CUI details only inside the CPE or by phone. Do not paste CUI, sheet titles, or screenshots into email, chat, or the ticket queue. The incident log records locations, counts, and markings, not content.

**Legal privilege.** Counsel engages the forensic firm. The DoD report itself is treated as information created by or for DoD (252.204-7012(c)(2)), so keep privileged analysis separate from the facts that go into the report.

## 1. Preparation checks (Identify / Protect)
- [ ] **Two valid DoD-approved medium assurance certificates** (Director of Contracts and Compliance and Security Manager). **Gap: the only certificate expired 2026-05-20; first replacement due 2026-10-09, second by 2026-10-31 (POAM-013)**
- [x] DIBNet account details and the required report elements printed in the incident binder
- [ ] Imaging kit and written procedure for enclave laptops and rugged tablets, with chain-of-custody forms. **Gap until POAM-013 closes (2026-11-30)**
- [ ] Malware isolation procedure for enclave laptops using the provider's endpoint tool (for submission to the DoD Cyber Crime Center). **Gap until POAM-013 closes**
- [x] CPE native logs retained 180 days; legal hold can be set by a CPE administrator
- [ ] CPE monitoring with 24x7 alerting. **Gap until POAM-008 closes (2027-01-31); until then a security analyst reviews CPE logs daily**
- [x] A&E subcontract includes DFARS 252.204-7012, including (m)(2)(ii)
- [ ] Trade subcontracts include DFARS 252.204-7012. **Gap until POAM-016 closes (2026-11-30); no CUI goes to a trade without it from 2026-10-15**
- [x] FC-4 CUI distribution list current (who may hold which CUI, and where)

## 2. Detection and declaration (Detect / RS.MA)
| Trigger | Source | Action |
|---|---|---|
| A subcontractor reports an incident or gives a DoD incident report number | A&E firm or trade (POL-03 4.9) | Declare. Record the number. Start the company's own review at once |
| Leak-site post, news, or threat intelligence naming the A&E firm, a trade, or FC-4 | Threat intelligence; Army Corps; FBI | Declare; preserve the post |
| CUI marking found anywhere outside the CPE (SYS-01 search, a tablet, a mailbox, a printer, a trade's portal) | Staff report; quarterly content search (STD-09); data loss prevention alert | Declare a possible cyber incident (POL-03 4.5); do not delete anything yet |
| Unusual CPE activity: sign-in from a new country, mass download, new sharing rule, disabled logging | CPE native logs; daily review; monitoring service (2027) | Disable the session; declare |
| Ransomware or malware on an enclave laptop or virtual desktop | Endpoint protection in the CPE | Isolate the device; declare |
| Lost or stolen enclave laptop or FC-4 tablet, or a lost printed CUI set | Staff report | Declare; remote wipe after the device's last known state is recorded |

**Record the time of discovery in the incident log.** The 72-hour reporting clock runs from discovery of a cyber incident (252.204-7012(a), (c)(1)(ii)). When the team cannot tell whether an event is a cyber incident, General Counsel decides within 24 hours, and the default is to prepare the report on the 72-hour timeline.

## 3. First 24 hours (RS.MA, RS.MI)
| Time | Step | Who | Done when |
|---|---|---|---|
| 0-1 h | Declare; open the out-of-band group and the incident log; record discovery time | Incident commander | Log open |
| 0-1 h | **Preserve first** (POL-03 4.7): set legal hold on CPE logs; export SYS-01 audit logs for FC-4 folders; snapshot affected virtual desktops; do not wipe or reimage any device | Security analysts; IT Director | Holds and exports confirmed with hashes |
| 0-2 h | Contain without destroying evidence. **Variant 1:** suspend the 8 A&E guest accounts and block the A&E firm's domains from CPE sharing; revoke sessions. **Variant 2:** remove access to the misplaced CUI (permissions, not deletion), and quarantine tablets in airplane mode | Security Manager; IT Director | Access removed; evidence intact |
| 0-2 h | Call the cyber insurer hotline; counsel engaged; counsel engages forensics | CFO | Claim number |
| 0-4 h | Confirm the reporting capability: valid certificate in hand, DIBNet sign-in tested | Director of Contracts and Compliance | Test sign-in succeeded |
| 2-8 h | **Variant 1:** call the A&E firm's security contact: confirm the clause duties, ask for their DoD report status and incident number, which FC-4 data and which A&E devices were affected, and whether any A&E laptop that reached the CPE is infected | FC-4 Project Executive with the Security Manager | Call record; incident number when available |
| 4-12 h | Convene the CMT: what CUI is involved, schedule impact on FC-4, whether the Contracting Officer should hear from the company before DoD contacts it | CMT chair | CMT meeting held |
| 12-24 h | Begin the (c)(1)(i) review (section 4); first decision on whether the company's own systems were affected | Security Manager with forensics | Interim finding recorded |
| By 24 h | CEO informs the audit committee chair and the PE sponsor's operating partner | CEO | Notice given |

## 4. Analysis: the review for evidence of compromise (RS.AN)
DFARS 252.204-7012(c)(1)(i) requires the company to review for evidence of compromise of CDI, including compromised computers, servers, specific data, and user accounts, and to analyze the systems that were part of the incident and other systems on its networks that may have been accessed as a result. For this company that means:
1. **CPE accounts and sessions.** Sign-ins for all 52 accounts in the incident window, with emphasis on the 8 A&E guests (variant 1). Look for new devices, new locations, mass downloads, sharing changes, and clipboard or download events from virtual desktops.
2. **Endpoints that touched CUI.** The 18 enclave laptops; the FC-4 tablets that held offline sets; any A&E laptop that connected to the CPE gateway (through the A&E firm).
3. **Data.** Which CUI items (by sheet number and marking) were on the affected systems, and whether any were opened, copied, or exported. For variant 2, list every user who could reach the misplaced items and every access in the logs (for SYS-01, the 230 external users from 14 firms).
4. **Corporate systems.** Whether the incident reached SYS-01, SYS-05, or the landing zone (for example, malware on a corporate laptop used by an FC-4 team member).
5. **Malicious software.** Isolate samples found on company systems for submission to the DoD Cyber Crime Center ((d)). Never send malware to the Contracting Officer.
6. **Personal information.** Whether employee or subcontractor personal information was also affected (Florida and other state notices through `notification-matrix.csv`).

**Decision D1: was a covered contractor information system or the CDI in it affected?** General Counsel records the decision and its basis.
- **Yes, or not ruled out:** file the company's report within 72 hours of discovery (section 6).
- **No (variant 1, A&E systems only):** record the basis (for example, no A&E guest sign-ins after the A&E firm's estimated compromise date). The A&E firm's own report covers its systems; the company records the A&E firm's incident number and keeps monitoring.

**Variant 2 specific:** CUI copied to an unauthorized system is a compromise under the clause definition. The review decides whether it was a cyber incident (through computer networks) and whether it needs a report. Where CUI sat in a commercial cloud service that does not meet FedRAMP Moderate equivalence, counsel also considers whether the company must tell the Contracting Officer about the gap in its compliance with (b)(2)(ii)(D) and correct its SPRS score (P03 G-111, G-120).

## 5. Containment and eradication (RS.MI)
1. **Only after images and logs are preserved:** remove misplaced CUI from SYS-01, tablets, mailboxes, or personal accounts, and obtain written destruction confirmation from any trade or person who received CUI improperly.
2. Reset credentials and re-register FIDO2 keys for affected CPE accounts; rebuild affected virtual desktops from the approved image; reimage affected enclave laptops after imaging.
3. Variant 1: keep A&E guest access suspended until the A&E firm confirms eradication in writing and its laptops are rebuilt or replaced; then restore access for named users only. Exchange CUI design packages through the CPE only.
4. Fix the path that let CUI escape (for example, the SYS-01 folder template, a virtual desktop download setting, a missing flowdown) before closing containment (POAM-002, POAM-016).

## 6. Reporting and communication (RS.CO)
**Follow `notification-matrix.csv`.** General Counsel approves report content; the Director of Contracts and Compliance files.

| When | Action | Owner |
|---|---|---|
| Hour 0-2 | Insurer hotline; counsel engaged | CFO |
| As soon as known | Record the A&E firm's (or a trade's) DoD incident report number (252.204-7012(m)(2)(ii)) | FC-4 Project Executive |
| **Within 72 hours of discovery** | **Company report at https://dibnet.dod.mil** with at least the required elements listed there (252.204-7012(c)(1)(ii), (c)(2)), using a medium assurance certificate. Include the subcontractor's incident number if one exists | Director of Contracts and Compliance |
| With the report | Submit isolated malicious software to the DoD Cyber Crime Center as it instructs ((d)) | Security Manager |
| For at least 90 days from the report | Preserve images of all known affected systems and relevant monitoring and packet capture data ((e)) | Security Manager |
| On DoD request | Give access to additional information or equipment for forensic analysis ((f)); provide damage assessment information through the Contracting Officer ((g)) | Director of Contracts and Compliance |
| Same day as the report (company practice) | Call the FC-4 Contracting Officer to say a report was filed and describe any schedule impact. This is a courtesy and a contract management step, not a separate clause duty | FC-4 Project Executive with General Counsel |
| As needed | Ask the government-community cloud provider for its incident information; the provider must meet (c) to (g) for the CDI it holds (252.204-7012(b)(2)(ii)(D)) | Security Manager |
| Within 30 days of a personal information determination | Florida and other state notices, if employee or subcontractor personal information was affected (Fla. Stat. 501.171) | General Counsel |
| Before the next SPRS update or affirmation | Correct the SPRS score if requirements are no longer met; if a CMMC status is held, confirm it is still current before relying on it (252.204-7021(a), "current") | GRC analyst; General Counsel; CEO as Affirming Official |
| Voluntary | FBI field office; CISA | Security Manager through counsel |

**Ransom (variant 1).** The company does not negotiate on behalf of the A&E firm. If the company itself ever receives a demand, an OFAC sanctions check and law enforcement contact come before any discussion of payment (POL-03; OFAC advisory, 2021-09-21). Paying does not remove the DoD reporting duty.

**What the company does not do.** It does not publish details of FC-4 CUI or the federal facility, comment on the A&E firm's incident, or describe the Army Corps of Engineers' facility in any statement.

## 7. Recovery (RC.RP, RC.CO)
Restore in BIA order (P05 BP-04: MTD 24 hours, RTO 8 hours), **but preservation comes first**. "Recovered" means "preserved, then rebuilt".

| Order | Resource | Target | Validation |
|---|---|---|---|
| 1 | Enclave identity tenant: affected accounts reset; guest access reviewed | 4 h | Sign-in logs clean; FIDO2 re-registered |
| 2 | Printed CUI sets for the FC-4 jobsite from the locked CUI room (workaround) | Immediate | Numbered sets signed out; never SYS-01 |
| 3 | CPE virtual desktop pool | 8 h | Rebuilt from the approved image; download and clipboard settings verified |
| 4 | CPE collaboration suite and files | 8 h | Integrity of design packages checked against the A&E firm's transmittal log; restore from the independent CPE backup (from 2026-12) |
| 5 | Enclave laptops | 24 h | Reimaged only after imaging; FIPS mode verified |
| 6 | A&E guest access | When the A&E firm confirms eradication | Named users only; new laptops or rebuilt devices |

Tell the FC-4 team, the A&E firm, and the trades what has changed, and when normal CUI exchange resumes (RC.CO).

## 8. Post-incident (ID.IM)
- Lessons-learned meeting within 14 days; written report within 30 days of closing (POL-03 4.13).
- Update the risk register (P01 R-003, R-004, R-009, R-016, R-017), the gap analysis and SPRS score (P03), the POA&M (P07), the SSP (P02 section 7.2), and training.
- Keep images and monitoring data for at least 90 days from the DoD report, and longer under any legal hold. Retain incident records for at least 6 years (POL-01 4.16).
- Brief the C3PAO readiness check (2027-03) on the incident and its corrective actions.
