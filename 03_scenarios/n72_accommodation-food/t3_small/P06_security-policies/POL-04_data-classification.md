# Data Classification and Handling Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC |
| Policy ID | POL-04 |
| Owner | Controller |
| Approved by | General Manager |
| Effective date | 2026-09-01 |
| Review cycle | Annually (next review 2027-08-31), and after major changes, incidents, or changes to payment design |
| Implements (SP 800-53 Rev. 5) | RA-2, MP-1, MP-4, MP-6, SC-8, SC-28, SI-12, CP-9 |
| CSF 2.0 | ID.AM-07, ID.AM-08, PR.DS-01, PR.DS-02, PR.DS-11 |
| PCI DSS v4.0.1 | Requirements 3, 4, and 9.4 |

## 1. Purpose
Classify hotel information by sensitivity and set handling rules so protection matches the harm a disclosure would cause. Above all, keep card data out of places it does not need to be.

## 2. Scope
All Cris Santos Company workforce members (owners, employees, contractors, and staff supplied by the staffing company) at the hotel, its restaurant, and its bars. Covers all systems and data, including services that vendors operate for the hotel (PMS, payment services, booking engine, channel manager, cloud tenant, chatbot, and pricing system). It applies to payment card data, guest personal information, and all other hotel information.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Controller | Owns this policy and the card data handling procedure |
| Front Office Manager | Owns guest records, the guest register, and ID scan handling |
| IT Manager | Implements encryption, backup, masking, and disposal controls |
| All workforce | Label and handle information according to this policy |

## 4. Policy statements
4.1 Information must be classified in one of four levels:

| Level | Examples | Handling |
|---|---|---|
| **Restricted** | Card numbers, card security codes, guest ID scans and ID numbers, finger templates, credentials | Only in approved systems (4.2); encrypted at rest and in transit; minimum necessary |
| **Confidential** | Guest profiles and stay history, guest register, payroll, contracts, security documents | Encrypted in transit; need-to-know |
| **Internal** | Schedules, procedures, rate strategy | Workforce only |
| **Public** | Website, published rates with total price | No restriction |

(RA-2; ID.AM-07)
4.2 **Card data may exist only in the approved payment services:** the PMS card vault, the payment gateway, the P2PE devices, and the booking engine. It must **never** be written on paper, typed into email, chat, spreadsheets, or notes, stored in the file share or cloud tenant, or read over a recorded phone line. Phone payments are taken only on a P2PE device keypad or through a gateway payment link once available. (SC-28; SI-12; PCI 3.2.1, 4.2.2)
4.3 **Card security codes must never be stored** after authorization, in any form, including card authorization forms. (PCI 3.3.1)
4.4 Card authorization forms for group and third-party billing are replaced by gateway payment links by 2026-10-31. Until then, forms must be processed the same day, kept in a locked drawer, and shredded right after processing; emailed forms must be deleted from the mailbox and deleted-items folder the same day. (MP-4; MP-6; PCI 9.4)
4.5 Full card numbers must be masked when displayed. Only users approved under POL-02 4.2 may display them. (AC-3; PCI 3.4.1)
4.6 Media and paper holding Restricted or Confidential data must be shredded or wiped when no longer needed, using the locked shredding bins or a certified destruction vendor that provides certificates. This includes background-check reports. (MP-6; ID.AM-08; PCI 9.4.6; 16 CFR 682.3; Fla. Stat. 501.171(8))
4.7 **Retention schedule** (SI-12):

| Record | Keep | Why |
|---|---|---|
| Guest register data (name, dates of occupancy, rates) | 2 years after check-out, then delete or anonymize | Fla. Stat. 509.101(2): register must be available for inspection; registers older than 2 years need not be made available |
| Guest ID scans | Check-out plus 30 days | Needed only to resolve disputes at the stay; high breach impact (Fla. Stat. 501.171(1)(g)) |
| Card authorization forms | Not kept after processing | PCI 3.2.1, 3.3.1 |
| Folios and accounting records | As set by the Controller for tax and accounting purposes | Business and tax records |
| Chatbot transcripts | 90 days | Service quality review only |
| PMS report exports in the cloud tenant | 90 days | Reporting only |
| Security logs | 12 months | PCI 10.5.1 |

4.8 Backups of Restricted and Confidential data must be encrypted, stored apart from production (separate account), protected from alteration, and restore-tested quarterly. (CP-9; PR.DS-11)
4.9 Restricted data must not be entered into AI tools or other third-party services unless the tool is approved under P10 and the vendor has signed an agreement with security and data-use terms. (SA-9)

## 5. Compliance and enforcement
Violations are handled under the sanctions rule in POL-01 section 4.8. Sanctions range from retraining to termination, depending on intent and harm. For contracted staff, the staffing company is asked to remove the person from the hotel assignment. Compliance is checked through the annual control assessment (P07), the PCI DSS self-assessment, and the access reviews in this policy set.

## 6. Exceptions
Exceptions follow POL-01 section 4.6. They must be written, risk-rated, approved by the policy owner (or by the majority owner for High risk), and expire within 12 months. No exception may allow storage of card security codes after authorization.

## 7. Related documents
POL-01; POL-05; card data handling procedure; P10 AI approved-tools list; PCI DSS scope document
