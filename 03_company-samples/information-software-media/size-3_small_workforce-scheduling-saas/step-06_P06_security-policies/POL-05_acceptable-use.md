# Acceptable Use Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC |
| Policy ID | POL-05 |
| Owner | IT Manager |
| Approved by | Chief Executive Officer |
| Effective date | 2026-09-22 (replaces the December 2025 policy adopted for the SOC 2 Type 1) |
| Review cycle | Annually (next review 2027-09-22), and after major changes or incidents |
| Implements (SP 800-53 Rev. 5) | PL-4, PL-4(1), AT-1, AT-2, AT-3, AC-11, CM-11, IA-5 |
| CSF 2.0 | PR.AT-01, PR.AT-02, GV.PO-01 |
| Also supports | SOC 2 CC1.4, CC2.2; FTC Act Section 5 reasonable security (N51-R01) |

## 1. Purpose
Set clear, plain-language rules for how the workforce uses company systems, devices, customer data, and AI tools.

## 2. Scope
All Cris Santos Company workforce members (owners, employees, and contractors), whether they work in the Florida office or remotely. Covers all company systems and data, including the Workforce Scheduling Platform (WSP), the staging environment, the source repository and CI/CD pipeline, corporate SaaS, laptops, and systems that sub-processors operate for the company. It applies to customer data (customer worker data the company processes as a service provider under the DPA) and all other company information.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| People Operations Manager | Collects signed acknowledgments at hire and annually; tracks training completion |
| IT Manager | Security awareness content, phishing simulations, and the approved AI tools list |
| Engineering Manager | Secure coding training for engineers |
| All workforce | Follow these rules |

## 4. Policy statements
4.1 Company systems are for company business. Limited personal use is allowed if it does not involve customer data or create risk. (PL-4)
4.2 Every workforce member must acknowledge this policy before receiving access and again each year. Current staff must acknowledge it by 2026-10-31. (PL-4(1))
4.3 Security awareness training is required at hire and every year, with phishing simulations at least twice a year. Engineers must also complete secure coding training every year. (AT-2; AT-3; PR.AT-01; PR.AT-02)
4.4 Use only company-managed laptops for company work. Lock your screen when you step away; laptops lock after 5 minutes idle. (AC-11)
4.5 Install software only from approved sources. Engineers may install developer tools from the approved package registries; other software and browser extensions need IT approval. (CM-11)
4.6 **Customer data.** Look at customer data only when a ticket or engineering task requires it. Do not export, download, or screenshot customer data outside approved tools, and never paste it into chat, personal email, or unapproved AI tools. (PL-4)
4.7 **Secrets.** Never put passwords, keys, or tokens in source code, tickets, chat, or documents. Report any exposed secret at once so it can be rotated (POL-03 4.2). (IA-5)
4.8 **Generative AI tools.** Use only tools on the approved AI tools list kept by the IT Manager. Approved tools are company-licensed and do not train on inputs. Customer data, secrets, and source code may be entered only into tools the list approves for that data. (PL-4)
4.9 Report suspicious messages with the Report Phishing button, and report lost or stolen devices immediately (POL-03 4.2). (AT-2)

## 5. Compliance and enforcement
Violations are handled under the sanctions statement in POL-01 section 4.7. Sanctions range from retraining to termination of employment or contract, depending on intent and harm. Compliance is checked through the annual control assessment (P07), the SOC 2 examination (P09), and the access reviews in POL-02.

## 6. Exceptions
Exceptions follow POL-01 section 4.6. They must be written, risk-rated, approved at the level set in POL-01 section 4.4, recorded in the risk register (P01), and expire within 12 months.

## 7. Related documents
POL-01; POL-02; POL-03; POL-04; approved AI tools list; training records; P10 AI risk assessment
