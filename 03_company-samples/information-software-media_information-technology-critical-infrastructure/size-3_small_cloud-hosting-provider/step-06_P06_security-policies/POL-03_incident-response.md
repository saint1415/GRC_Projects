# Incident Response Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC |
| Policy ID | POL-03 |
| Owner | IT Manager |
| Approved by | Chief Operating Officer |
| Effective date | 2026-09-25 |
| Review cycle | Annually (next review 2027-09-24), and after every SEV1 incident or exercise |
| Implements (SP 800-53 Rev. 5) | IR-1, IR-2, IR-3, IR-4, IR-5, IR-6, IR-6(3), IR-7, IR-8, AU-11, SR-8 |
| CSF 2.0 | RS.MA-01, RS.MA-02, RS.AN-03, RS.CO-02, RS.CO-03, RS.MI-01, ID.IM-03 |
| Regulatory drivers | C-IT-R05 (12 CFR 53.4; 225.303; 304.24); Fla. Stat. 501.171(6); MSA 72-hour incident notice; C-IT-R01 (FedRAMP IEC rules, once certified) |

## 1. Purpose
Make sure the company detects, contains, and recovers from security incidents quickly, and meets every notice duty it owes customers, banks, and (in the future) federal agencies. The company's tools reach many customers, so one incident can become many customers' incidents.

## 2. Scope
All workforce members and all systems in scope of POL-01. This includes incidents at vendors that operate company tools (RMM, SIEM, identity, code hosting, cloud, colocation) and incidents that start in a customer environment but involve company tools.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| NOC (24x7) | Receives reports; opens the incident ticket; pages the incident commander; runs customer status communication |
| IT Manager (incident commander) | Leads response; decides severity; records the time of determination for each notice clock |
| COO (backup incident commander) | Leads if the IT Manager is unavailable; approves customer-wide communications |
| CEO | Ransom decisions; contract-level communications to banks and the agency sponsor |
| Outside counsel | Confirms every legal notice before it goes out |
| System owners | Technical containment and recovery for their systems |

## 4. Policy statements
4.1 **What counts.** A security incident is any event that actually or likely compromises the confidentiality, integrity, or availability of company or customer systems or data. It explicitly includes misuse of any tool that can act on customer environments: the RMM tool, control plane service credentials, hypervisor managers, BMCs, and the CI/CD pipeline. (IR-4; RS.MA-01)

4.2 **Report fast.** Anyone who suspects an incident must report it to the NOC **within 15 minutes** of noticing it, by phone or ticket. The NOC must open an incident ticket and page the incident commander. (IR-6; RS.MA-02)

4.3 **Severity.**
- **SEV1:** more than one customer affected, any bank customer's covered services at risk, or any administrative tool compromised.
- **SEV2:** one customer affected, or a contained compromise of company systems.
- **SEV3:** everything else.
SEV1 incidents follow the matching runbook, such as the RMM compromise runbook (P08). (IR-4; IR-8; RS.AN-03)

4.4 **Contain first.** The incident commander may take customer-affecting containment steps without further approval. Examples: suspending RMM script execution for all customers, revoking control plane credentials, or isolating a hypervisor cluster. The NOC must tell affected customers on the status page. (IR-4; RS.MI-01)

4.5 **Preserve evidence.** Responders must preserve logs, images, and tool audit trails with a chain-of-custody record before rebuilding systems. Logs needed for an open incident must be kept until the incident is closed, even beyond normal retention. (IR-4; AU-11)

4.6 **Notice clocks.** The incident commander must record the time the company **determines** each notice trigger. Notices then follow the notification matrix in P08, with counsel confirming each one:
- the bank service provider rule: as soon as possible after determining a 4-hour material disruption, or one reasonably likely;
- MSA notice to customers within 72 hours of confirmation;
- Fla. Stat. 501.171(6): notice to each customer, as covered entity, within 10 days of determining a breach of personal information the company maintains for it;
- FedRAMP incident communications, once any agency tenant exists.
(IR-6; RS.CO-02; RS.CO-03)

4.7 **Ransom.** Only the CEO may decide on a ransom payment, and only after consulting counsel and the insurer and completing an OFAC sanctions check. (IR-4)

4.8 **Vendor incidents.** Incident notices from vendors must go to the Information Security Officer, who must assess them within 24 hours. The incident commander decides whether to open an incident. (IR-6(3); SR-8)

4.9 **Test and train.**
- The incident response plan must be tested at least annually by tabletop exercise. The first exercise is due by 2026-12-15.
- NOC staff, IT, and engineers must complete incident response training every year.
(IR-2; IR-3)

4.10 **Learn.** A lessons-learned review must be held within 14 days of closing a SEV1 or SEV2 incident and documented within 30 days. Findings go into the risk register and POA&M. (IR-4; ID.IM-03)

## 5. Compliance and enforcement
Violations are handled under the sanctions statement in POL-01 section 4.7. Sanctions range from retraining to termination, depending on intent and harm. Compliance is checked through the annual control assessment (P07), exercise reports, and incident reviews.

## 6. Exceptions
Exceptions follow POL-01 section 4.6. They must be written, risk-rated, approved by the right authority, and expire within 12 months. No exception may extend a legal notice deadline.

## 7. Related documents
POL-01; P08 runbook and notification matrix; P05 BIA (recovery order); cyber insurance policy; 12 CFR 53.4; Fla. Stat. 501.171
