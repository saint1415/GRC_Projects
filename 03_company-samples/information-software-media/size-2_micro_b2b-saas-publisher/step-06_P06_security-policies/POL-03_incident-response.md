# Incident Response Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC |
| Policy ID | POL-03 |
| Owner | CTO (security and compliance lead) |
| Approved by | Chief Executive Officer, 2026-09-15 |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review 2027-09-15), and after any incident that required customer notice |
| Implements (SP 800-53 Rev. 5) | IR-1, IR-3, IR-4, IR-5, IR-6, IR-8, AU-6, SI-4 |
| CSF 2.0 | RS.MA-01, RS.MA-02, RS.AN-03, RS.CO-02, RS.CO-03, RC.RP-01, DE.AE-02, ID.IM-02 |
| Regulatory drivers | Customer DPA (72-hour incident notice); Fla. Stat. 501.171(6)(a) (third-party agent notice within 10 days); state breach laws where affected individuals reside; N51-R01 (FTC Act Section 5: accurate statements about incidents) |

## 1. Purpose
Make sure the company spots, contains, reports, and recovers from security incidents quickly, tells its customers within the times its contracts and the law require, and never makes a misleading statement about an incident.

## 2. Scope
Everyone who works for the company, including the contract developer, and every system in POL-02 section 2. It also covers incidents at sub-processors, the MSP, and other vendors that affect customer data. A "security incident" includes any attempted or successful unauthorized access to, use, disclosure, change, or destruction of customer or company data, any misuse of credentials or keys, malware on a company laptop, and a lost or stolen laptop.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| CTO | Incident commander and technical lead; decides severity; keeps the incident log |
| Senior Software Engineer | Backup technical lead; evidence capture in the cloud account |
| Operations and Finance Manager | Privacy lead; calls the cyber insurer; works with counsel on notice decisions; tracks notice clocks |
| Chief Executive Officer | Backup incident commander; approves every customer notice and public statement, spending, and any extortion decision |
| Customer Success Manager | Sends approved customer notices and updates; keeps the customer security contact list |
| MSP | Isolates and investigates company laptops and the productivity suite; preserves suite logs |
| Cyber insurer and its panel vendors | Breach counsel and forensic firm, engaged through the insurer's hotline |
| Everyone | Report suspected incidents at once |

## 4. Policy statements
4.1 The company must keep an incident response runbook for its most likely serious incident, a cloud credential compromise exposing customer data (P08), with the contact sheet, notice clocks, and templates. Copies must be kept outside the production account and the productivity suite (printed and in the password manager), so they can be reached if either is compromised. (IR-8; RS.MA-01)

4.2 Anyone who suspects an incident must report it to the CTO **at once, and within 1 hour at most**, by phone or chat. If the CTO cannot be reached, report to the Senior Software Engineer, then the Chief Executive Officer. Examples: a secret or key pasted somewhere public, a strange sign-in prompt, a laptop acting oddly, a customer reporting data they should not see, a lost laptop or phone, or an email claiming to have company data. (IR-6; RS.MA-02)

4.3 The CTO must log every incident, including those that turn out to be harmless, with the time of discovery, the time of confirmation, what happened, what was done, and the outcome. (IR-5)

4.4 **Customer notice.** For any incident that affects or may affect customer data, the Operations and Finance Manager starts the notice clocks at once. The company must notify each affected customer's security contact within 72 hours of confirmation (DPA), and, where personal information of Florida residents is involved, no later than 10 days after determining a breach or having reason to believe one occurred (Fla. Stat. 501.171(6)(a)), giving each customer the information it needs for its own notices. Other states' service-provider duties are checked by counsel using the P08 notification matrix. Send a short initial notice when facts are thin, then update. (IR-6; RS.CO-02; RS.CO-03)

4.5 Customers decide on their own notices to individuals and regulators, because they own the data. The company supports them with the facts, affected record lists, and, if a customer asks in writing, by sending notices on its behalf. For data the company owns (its own employees and customer user accounts), the company is the one that notifies. (RS.CO-03)

4.6 For any suspected credential compromise, data theft, or extortion, the Operations and Finance Manager must call the cyber insurer's breach hotline before hiring any outside firm. Counsel reviews every legal notice before it is sent. (IR-4; RS.MA-02)

4.7 No ransom or extortion payment may be made without the Chief Executive Officer's approval, advice from breach counsel and the insurer, and an OFAC sanctions check. (IR-4)

4.8 Every customer notice and public statement about an incident must be approved by the Chief Executive Officer and must not claim more than the facts show. Do not say "no data was accessed" unless logs prove it. (RS.CO-02; FTC Act Section 5 deception)

4.9 Sub-processors, the MSP, and the contract developer must report incidents that may affect company or customer data to the CTO as their contracts require. The CTO must log each report and handle it under this policy. (IR-6; SA-9)

4.10 **Monitoring.** The CTO or Senior Software Engineer must review cloud administrator activity and security alerts every week, and admin console sessions every month, and record the review. (AU-6; SI-4; DE.AE-02)

4.11 The runbook must be tested every year with a tabletop exercise that includes the MSP and the Customer Success Manager, and after any real incident that used it. (IR-3; ID.IM-02)

4.12 Lessons learned must be written up within 30 days of closing any incident that required customer notice or outside help, and fed into the risk register, the runbook, and training. (IR-4; ID.IM-02)

## 5. Compliance and enforcement
Breaking this policy leads to sanctions under POL-02 A.10. Failing to report is a violation; reporting a mistake in good faith is never sanctioned. Compliance is checked in the annual assessment (P07) and the annual tabletop.

## 6. Exceptions
Exceptions follow POL-02 A.9. No exception may delay a contractual or legally required notice.

## 7. Related documents
P08 Incident Response Runbook and notification matrix; POL-02; POL-04; customer security contact list; DPA; Fla. Stat. 501.171; cyber insurance policy
