# Incident Response Policy (Group)

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. and all divisions |
| Policy ID | POL-03 |
| Owner | Group CISO, with the Chief Product Security Officer for product incidents and the Group General Counsel for notifications |
| Approved by | Board risk committee |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review 2027-09-30), after every Severity 1 incident, and after each cross-division exercise |
| Implements (SP 800-53 Rev. 5) | IR-1, IR-2, IR-3, IR-4, IR-5, IR-6, IR-8, CP-2 |
| CSF 2.0 | RS.MA-01, RS.MA-02, RS.AN-03, RS.CO-02, RS.CO-03, RC.RP-01, ID.IM-02 |
| Regulatory basis | 524B(b)(1)-(2); 21 CFR 803, 806, 820.35(a); FDA postmarket cybersecurity guidance (2016); HIPAA 164.308(a)(6), 164.410 (DCC); 21 CFR 803.18(d) and 803.40 (Distribution); FAR 52.204-25(d); Form 8-K Item 1.05; state breach laws |
| Division supplements | Medical Devices: PSIRT procedure and FDA decision points. Distribution: holds, customer notices, and contracting officer notices. Testing: client notices under NDAs |

## 1. Purpose
Make sure the group detects, contains, and recovers from incidents consistently across divisions, that product security incidents reach the right FDA and customer decisions, and that every entity meets its own notice duties on time.

## 2. Scope
All security incidents affecting any group system or data, all product security incidents affecting marketed devices or related systems, and incidents at service providers, suppliers, and contract manufacturers that affect group data or products.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Group SOC director | Runs detection and IT incident handling 24x7; incident commander for Severity 1 and 2 IT incidents |
| Chief Product Security Officer | Incident commander for product security incidents (devices, update path, signing keys) |
| Group CISO | Declares Severity 1; briefs the board risk committee |
| VP Quality and Regulatory Affairs | MDR, correction and removal, and complaint decisions for Medical Devices |
| DCC privacy officer | Breach risk assessment and business associate notices for the DCC |
| Distribution VP quality and regulatory | Holds, distributor complaint files, importer reports |
| Distribution federal contracts compliance director | Contracting officer notices |
| Testing laboratory quality director | Client notices under NDAs |
| Group General Counsel | Owns the notification matrix; approves every external notice |
| Disclosure committee | Decides materiality for Form 8-K Item 1.05 |

## 4. Policy statements
4.1 Every workforce member must report a suspected incident to the group SOC within 1 hour of noticing it. Reports that involve a device or the release chain are routed to the PSIRT at once. (IR-6; RS.MA-02)

4.2 The group uses **one severity scale** for IT and product incidents. A product incident with possible patient harm, or tampering with the update path or signing keys, is Severity 1. Division scales are not permitted. (IR-4; IR-8; RS.MA-01)

4.3 The incident log must record every date that starts a legal clock: when the group learned of a vulnerability, when any employee became aware of an MDR-reportable event (21 CFR 803), when a PHI breach was discovered (164.410(a)(2)), when covered telecommunications equipment was identified (52.204-25(d)), and when a correction was initiated (806.10). (IR-5; RS.AN-03)

4.4 **FDA decisions.** For every product incident, the VP Quality and Regulatory Affairs must document the complaint, MDR, and correction and removal decisions, and the controlled or uncontrolled risk assessment described in FDA's postmarket guidance. Distribution must record related complaints in its device complaint files and forward them to the manufacturer the same day. (IR-6; RS.CO-02; 820.35(a); 803.18(d))

4.5 **Business associate notices.** The DCC privacy officer must document a four-factor breach risk assessment (164.402) for any incident that may involve PHI in the DCC and notify each affected hospital as its BAA requires, and no later than 60 calendar days after discovery (164.410). (IR-6; RS.CO-02)

4.6 The Group General Counsel must maintain the multi-regulator notification matrix (P08), including BAA terms, NDA terms, and federal contract terms, and review it every quarter. Every external notice must be approved by counsel. (IR-6; IR-8)

4.7 **SEC materiality.** Severity 1 incidents must be escalated to the disclosure committee within 24 hours of declaration. The committee must decide materiality without unreasonable delay. If material, the Form 8-K Item 1.05 filing must be made within 4 business days after the determination. (IR-6; RS.CO-03)

4.8 **Ransom payments** require board risk committee approval, counsel, the cyber insurer, and an OFAC sanctions check before any payment. (IR-4)

4.9 The group must run at least one cross-division exercise each year that includes a product incident, the notification matrix, and a materiality decision. (IR-3; ID.IM-02)

4.10 Evidence, including returned devices and firmware images, must be preserved with chain of custody. Logs relevant to an incident must be placed on legal hold. (IR-4; RS.AN-03)

4.11 A lessons-learned review must be completed within 30 days of recovery, with a CAPA opened in the QMS for product incidents, and the risk registers, POA&M, and this policy updated. (IR-4; ID.IM-02)

## 5. Compliance and enforcement
Violations are handled under POL-01 section 4.14. Compliance is checked through the P07 assessment (IR-3, IR-4, IR-6, IR-8) and exercise reports.

## 6. Exceptions
Exceptions follow POL-01 section 4.11. No exception may extend a legal or contractual notice deadline.

## 7. Related documents
P08 runbook and notification matrix; PSIRT procedure; POL-01; `division-supplements.md`; BIA recovery priorities (P05).
