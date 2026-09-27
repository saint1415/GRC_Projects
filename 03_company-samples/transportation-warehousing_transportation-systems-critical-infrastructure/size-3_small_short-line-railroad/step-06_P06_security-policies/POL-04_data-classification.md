# Data Classification and Handling Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC |
| Policy ID | POL-04 |
| Owner | Manager of Safety and Security |
| Approved by | President and General Manager |
| Effective date | 2026-09-01 |
| Review cycle | Annually (next review 2027-08-31), and after major changes, incidents, or a TSA designation notice |
| Implements (SP 800-53 Rev. 5) | RA-2, MP-3, MP-4, MP-6, SC-8, SC-28, CP-9, AC-3 |
| CSF 2.0 | ID.AM-05, PR.DS-01, PR.DS-02, PR.DS-11, ID.AM-08 |
| Regulatory basis | C-TRANSPORTATION-S03 (1520.9; 1520.13; 1520.19); C-TRANSPORTATION-S06 (172.802(c)); C-TRANSPORTATION-S07 (Fla. Stat. 501.171) |

## 1. Purpose
Classify company information by sensitivity and set handling rules for each class, including the federal rules for Sensitive Security Information.

## 2. Scope
All Cris Santos Company workforce members (owners, employees, and contractors) at Central Yard, North Yard, South Yard, the tower sites, and on trains. Covers all company systems and data, including operational technology (dispatch, radio, wayside, and onboard PTC equipment) and systems that service providers operate for the company.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Manager of Safety and Security | Owns this policy; decides what is SSI; keeps the SSI access list |
| Department heads | Classify the information their departments create |
| IT Manager | Implements technical protections (encryption, access, backups) |
| All workforce | Label and handle information by its class |

## 4. Policy statements
4.1 Company information has four classes:

| Class | Examples | Handling |
|---|---|---|
| **SSI (Restricted, federal)** | TSA-marked documents; the hazmat security plan and its risk assessment where TSA has marked them; security vulnerability details that TSA treats as SSI | 49 CFR part 1520 rules below; named access only |
| **Restricted** | OT network diagrams and configurations; CAD and PTC configurations; RSSM car location data; employee personal information and medical certification records; credentials | Need-to-know access; encrypted; no personal email or AI tools |
| **Internal** | Train schedules, bulletins, shipper contracts, rates, operating procedures | Employees and approved contractors |
| **Public** | Website content, published tariffs | No restriction |

(RA-2; ID.AM-05)

4.2 **SSI handling.** SSI must be kept in the restricted SSI library or a locked container, shared only with covered persons who have a need to know, marked as 49 CFR 1520.13 specifies, and destroyed as 1520.19 specifies. Unmarked SSI received from others must be marked, and the sender told (1520.9(b)). Requests for SSI from anyone else go to TSA (1520.9(a)(3)). (AC-3; MP-3; MP-4)
4.3 The hazmat security plan is available only to the employees who implement it, on a need-to-know basis (49 CFR 172.802(c)). (AC-3)
4.4 Restricted and SSI data must be encrypted at rest and in transit. Alarm and telemetry traffic from wayside equipment must move to an encrypted path by 2027-03-31. (SC-28; SC-8; PR.DS-01; PR.DS-02)
4.5 Media holding Restricted or SSI data must be wiped or destroyed by a method that prevents recovery, with a destruction record. (MP-6; ID.AM-08)
4.6 **Backups.** CAD and other operations-critical data must be backed up daily to an isolated, immutable location, with an offline copy weekly. Restores must be tested quarterly. (CP-9; PR.DS-11)
4.7 Restricted data, SSI, and imagery of track, bridges, and signal equipment must not be put into any AI tool that is not on the approved-tools list (POL-05 4.8). (AC-3)

## 5. Compliance and enforcement
Violations are handled under the discipline procedure in POL-01 section 4.8. Consequences range from retraining to termination, depending on intent and harm; for employees covered by a collective bargaining agreement, the agreement's procedures apply. Compliance is checked through the annual control assessment (P07).

## 6. Exceptions
Exceptions follow POL-01 section 4.6. They must be written, risk-rated, approved by the policy owner (or by the majority owner for High risk), and expire within 12 months.

## 7. Related documents
POL-01; POL-02; POL-05; 49 CFR part 1520; 49 CFR 172.800-172.804; SSI access list; backup procedure
