# Data Classification and Handling Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC |
| Policy ID | POL-04 |
| Owner | Operations Manager (Information Security Coordinator), with the Head of Engineering for product data |
| Approved by | CEO, 2026-08-31 |
| Effective date | 2026-09-01 |
| Review cycle | Annually (next review 2027-08-31), and before any patient data enters the cloud service |
| Implements (SP 800-53 Rev. 5) | RA-2, CM-8, SC-8, SC-12, SC-28, CP-9, CP-4, SA-9, MP-6, SI-12, PL-4 |
| CSF 2.0 | ID.AM-01, ID.AM-02, ID.AM-07, ID.AM-08, PR.DS-01, PR.DS-02, PR.DS-11 |
| Regulatory basis | FD&C Act 524B(b)(3) (SBOM) (N31-33-R05); 21 CFR 820.10(a) (ISO 13485 cl. 4.2.5, records); Fla. Stat. 501.171 (workforce personal information) |

## 1. Purpose
Sort company information by how much harm its loss, disclosure, or alteration would cause, and set simple handling rules for each level.

## 2. Scope
All workforce members, contractors, and consultants, and all company information in any form: in SaaS systems, the cloud tenant, on laptops and lab workstations, in WM-1 units, on paper, and at suppliers.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Operations Manager | Owns this policy; keeps the asset inventory; approves new tools and vendors |
| Head of Engineering | Owns product data (keys, SBOM, threat model, vulnerability records) |
| QA/RA Manager | Owns design history records and their retention |
| MSP | Laptop encryption, backup of suite configuration, device wiping, as directed |
| All workforce | Handle information according to its level |

## 4. Policy statements
4.1 Company information has three levels:

| Level | Examples | Handling |
|---|---|---|
| **Restricted** | Firmware signing key; device certificate authority keys; hub API keys and provisioning files; passwords and MFA codes; details of vulnerabilities not yet fixed and disclosed; after clearance, patient data (PHI) | Only in the key management service, the CI secret store, or the eQMS security record with named access; never in email, chat, shared links, source code, or logs; two-person control for signing keys |
| **Confidential** | Source code; design files and the design history file; threat model and risk assessments; SBOM before release; test reports; contract manufacturer data; investor and financial documents; workforce personal information | Only in approved systems (4.3); encrypted in transit and at rest; shared outside the company only under a confidentiality agreement and by authenticated transfer with an expiry |
| **Public** | Website, published CVD policy, published advisories, marketing material after review | No restriction |

When unsure, treat information as Confidential. (RA-2; ID.AM-07)

4.2 Restricted and Confidential information must be encrypted wherever it is stored, on every laptop and lab workstation, and whenever it is sent outside company systems. (SC-28; SC-8; PR.DS-01; PR.DS-02)

4.3 Confidential information may be kept only in: the source code repository, the eQMS, the productivity suite, the cloud tenant, and company-managed laptops and lab workstations. Restricted information may be kept only where the table in 4.1 says. (AC-3; SC-12)

4.4 The Operations Manager must keep one inventory of laptops, lab equipment, pre-production units (by serial number and location), SaaS services, and cloud resources, and the Head of Engineering must keep the SBOM for each released software item. Both are updated when anything is added or removed. (CM-8; ID.AM-01; ID.AM-02; 524B(b)(3))

4.5 Before any new vendor, contractor, tool, or supplier receives Restricted or Confidential information, the Operations Manager must approve it and written security terms must be in place (POL-02 A.5). It is then added to the inventory. (SA-9; GV.SC-05)

4.6 **SBOM and vulnerability data.** The SBOM for each release is Confidential until the release is cleared and then shared with FDA and customers as the labeling says. Details of an unfixed vulnerability are Restricted until the agreed disclosure date (POL-03 4.4). (CM-8; RS.CO-03)

4.7 **AI tools.** Restricted and Confidential information may be entered only into AI tools on the approved list kept by the Head of Engineering. **Today the list has no generative AI tool approved for Confidential data.** Public AI chatbots under personal accounts must never receive source code, vulnerability details, keys, or design records. AI-001 training data is handled under the conditions in P10. (PL-4; SA-9)

4.8 **Backups.** The QA/RA Manager must export the full eQMS every quarter to company storage. Cloud database snapshots must be kept at least 30 days. The signing key must have a documented, tested recovery method in the key management service. Restore tests of the cloud database and the eQMS export must be run twice a year and recorded. (CP-9; CP-4; PR.DS-11)

4.9 **Disposal.** Laptops, lab workstations, and pre-production units must be wiped before reuse, return, or disposal, or destroyed by a vendor that provides a certificate of destruction. Units returned from the partner hospital must be reflashed before reuse. The Operations Manager keeps each record. (MP-6; ID.AM-08)

4.10 **Retention.** Design history records follow the QMS retention procedure. Security records are kept as POL-02 A.7 says. Workforce personal information is kept only as long as employment and tax law require. (SI-12)

4.11 **Before patient data.** No patient data may enter the cloud service until business associate agreements with the hospital customers and a HIPAA Security Rule program for the cloud service are in place, and this policy is updated for PHI. (SA-9)

## 5. Compliance and enforcement
Breaking this policy leads to sanctions under POL-02 A.4. Compliance is checked through the monthly MSP report, the quarterly eQMS export record, restore test records, release records, and the annual assessment (P07).

## 6. Exceptions
Exceptions follow POL-02 A.9.

## 7. Related documents
POL-02; POL-03; asset inventory; SBOMs; P04 cloud control map; P10 AI risk assessment; QMS record retention procedure
