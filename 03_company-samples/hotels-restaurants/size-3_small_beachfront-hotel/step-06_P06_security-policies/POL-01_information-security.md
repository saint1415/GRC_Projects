# Information Security Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC |
| Policy ID | POL-01 |
| Owner | General Manager |
| Approved by | General Manager |
| Effective date | 2026-09-01 |
| Review cycle | Annually (next review 2027-08-31), and after major changes, incidents, or changes to payment design |
| Implements (SP 800-53 Rev. 5) | PM-1, PM-2, PM-9, PL-1, PS-3, PS-8, RA-3, SA-9, CA-2 |
| CSF 2.0 | GV.PO-01, GV.PO-02, GV.RR-02, GV.RR-04, GV.OC-03, GV.SC-05, GV.SC-07 |
| PCI DSS v4.0.1 | Requirements 12.1, 12.3, 12.4 (not applicable), 12.5, 12.7, 12.8 |

## 1. Purpose
Set up the Cris Santos Company information security program, assign who is accountable, and give every other security policy its authority. The program protects payment card data, guest personal information, and the systems guests rely on, including room access.

## 2. Scope
All Cris Santos Company workforce members (owners, employees, contractors, and staff supplied by the staffing company) at the hotel, its restaurant, and its bars. Covers all systems and data, including services that vendors operate for the hotel (PMS, payment services, booking engine, channel manager, cloud tenant, chatbot, and pricing system). It applies to payment card data, guest personal information, and all other hotel information.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Majority owner | Approves the security budget; accepts High and Very High risks |
| General Manager | Program owner; approves policies; accepts Moderate risks |
| Controller | PCI DSS compliance owner: merchant agreements, SAQs, attestations, service provider files |
| IT Manager (Information Security Lead) | Runs the program day to day; maintains the risk register, SSP, and PCI scope document |
| Front Office Manager, Food and Beverage Director, Chief Engineer | Apply these policies in their departments; own their systems' access and devices |
| All workforce | Follow these policies; report suspected incidents immediately |

## 4. Policy statements
4.1 The hotel must maintain an information security program that meets PCI DSS for both merchant accounts and provides reasonable security for guest personal information. It is documented in this policy set and the System Security Plan. (PM-1; GV.PO-01)
4.2 The IT Manager is the designated Information Security Lead, and the Controller is the PCI DSS compliance owner. Both designations must be in writing. (PM-2; GV.RR-02)
4.3 A risk assessment must be performed at least annually and after major changes, using NIST SP 800-30 Rev. 1. Risks must be tracked in the risk register with an owner and treatment. Targeted risk analyses must support any PCI DSS requirement whose frequency the hotel sets. (RA-3; PM-9; PCI 12.3)
4.4 Risk acceptance authority: the IT Manager may accept Low risks; the General Manager, Moderate; the majority owner, High and Very High. Risks to guest physical safety rated High may not be accepted without a dated treatment plan. (PM-9)
4.5 **PCI DSS scope.** The IT Manager and Controller must document the cardholder data environment, card data flows, and in-scope components, and confirm them at least every 12 months and after any change to payment design. SAQ answers must be supported by evidence before the attestation is signed. (CM-8; PL-2; PCI 12.5)
4.6 Exceptions to any security policy must be requested in writing, risk-rated, approved per 4.4, recorded in the risk register, and time-limited to 12 months or less. (PL-1)
4.7 Security policies must be reviewed at least annually and updated after major changes or incidents. (PL-1; GV.PO-02)
4.8 **Sanctions.** Workforce members who fail to comply with security policies must be sanctioned in proportion to intent and harm: retraining, written warning, suspension, or termination. HR must document each sanction. (PS-8; GV.RR-04)
4.9 Staff with access to card data or guest records, and managers, must pass a background check before access is granted. Background-check reports are disposed of under POL-04 4.6. (PS-3; PCI 12.7; 16 CFR 682.3)
4.10 **Service providers.** Before a vendor stores, processes, or transmits card data or guest data for the hotel, or can affect their security, it must be on the service provider list, sign a written agreement that states its security and PCI responsibilities, and pass a review. The Controller must check each provider's PCI DSS status (AOC) or SOC 2 report at least annually. (SA-9; GV.SC-05; GV.SC-07; PCI 12.8)
4.11 Security controls must be evaluated at least annually (P07) and after major changes. (CA-2)
4.12 Privacy and pricing statements the hotel publishes (privacy policy, fee descriptions, rate displays) must be reviewed by the General Manager before release and whenever practices change, so they stay accurate. (GV.OC-03; 15 U.S.C. 45(a); 16 CFR 464.2-464.3)

## 5. Compliance and enforcement
Violations are handled under the sanctions rule in POL-01 section 4.8. Sanctions range from retraining to termination, depending on intent and harm. For contracted staff, the staffing company is asked to remove the person from the hotel assignment. Compliance is checked through the annual control assessment (P07), the PCI DSS self-assessment, and the access reviews in this policy set.

## 6. Exceptions
Exceptions follow POL-01 section 4.6. They must be written, risk-rated, approved by the policy owner (or by the majority owner for High risk), and expire within 12 months. No exception may allow storage of card security codes after authorization.

## 7. Related documents
POL-02 to POL-05; System Security Plan (P02); Risk Register (P01); PCI DSS scope document; service provider list
