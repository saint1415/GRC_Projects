# Data Classification and Platform Protection Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Policy ID | POL-04 |
| Owner | GRC Manager (classification), with the VP Platform Engineering (platform protection) and the Security Engineering Lead (cryptography) |
| Approved by | Chief Technology Officer |
| Approval date | 2026-09-22 |
| Effective date | 2026-10-01 (replaces the 2024 policy) |
| Review cycle | Annually (next review 2027-09-30) |
| Implements (SP 800-53 Rev. 5) | RA-2, CM-1, CM-2, CM-3, CM-6, CM-8, CM-12, MA-1, MP-1, MP-6, PE-1, PE-2, SC-1, SC-8, SC-12, SC-13, SC-28, SI-2, SI-7, RA-5 |
| CSF 2.0 | ID.AM-01, ID.AM-05, ID.AM-07, PR.DS-01, PR.DS-02, PR.DS-10, PR.PS-01, PR.PS-02, ID.RA-01 |
| Regulatory drivers | C-IT-R01 (Rev5 Class C controls; MAS, CMU, VDR, VER rules); C-IT-R03 (252.204-7012(b)(2)(ii)(D)) |
| Supporting standards | STD-01 Asset and boundary inventory; STD-03 Secure configuration; STD-05 Secure development and software supply chain; STD-06 Encryption and key management; STD-08 Vulnerability and patch management |

## 1. Purpose
Classify information so that each kind gets the right protection, and set the platform rules (configuration, cryptography, vulnerability response, integrity, media, and facilities) that protect it.

## 2. Scope
All information the company creates or holds for customers, in every system and data center, and all platform components in both partitions.

## 3. Classification levels
| Level | Examples | Key handling rules |
|---|---|---|
| **Federal** | Agency and defense customer data in the Government Cloud, including CUI and covered defense information; government partition logs | Government partition only; U.S.-person access; FIPS 140-validated encryption at rest and in transit; never in the commercial partition, managed services, tickets, or AI tools |
| **Customer Confidential** | Commercial VM contents, customer DNS zones, backups, tenant metadata, customer credentials | Encryption at rest and in transit; access only through approved tools; no copies outside the platform without the customer's request |
| **Restricted Internal** | Service credentials, signing keys, hypervisor and BMC configuration, security logs, vulnerability data, the FedRAMP package | Need-to-know; stored in the vault, HSM, or approved repositories; never in chat or email |
| **Internal** | Policies, runbooks, most tickets, employee directory | Company systems only |
| **Public** | Website, status page, public secure configuration guide | Approved for publication |

## 4. Policy statements
4.1 **Classify and label.** Every system in the CMDB must record the highest classification it handles and its partition. Third-party information resources that handle or affect Federal data must be listed with their usage, justification, and mitigations. (RA-2; CM-8; ID.AM-05; C-IT-R01 (MAS-CSO-IIR, MAS-CSO-TPR))
4.2 **Partition separation.** Federal data must stay in the government partition. Staff must not move it elsewhere, and the sales and onboarding process must screen for it. Suspected spillage is an incident (POL-03 section 4.9). (AC-4; CM-12; PR.DS-01; C-IT-R01; C-IT-R03)
4.3 **Data locations.** The locations of Federal and Customer Confidential data, including metadata in shared systems such as ticketing and billing, must be documented and reviewed yearly. (CM-12; ID.AM-07; C-IT-R01 (MAS-CSO-MDI))
4.4 **Encryption.** Federal and Customer Confidential data must be encrypted in transit (TLS 1.2 or higher) and at rest. Federal data must use FIPS 140-validated modules, documented per service. Keys must be managed under STD-06, with signing keys in the HSM. (SC-8; SC-12; SC-13; SC-28; PR.DS-01; PR.DS-02; C-IT-R01 (CMU-CSO-CMD); C-IT-R03)
4.5 **Secure configuration.** Every platform component must follow a documented baseline (STD-03), deployed as code where possible. Drift must be checked at least weekly and deviations approved and recorded. (CM-2; CM-6; PR.PS-01; C-IT-R01)
4.6 **Change control.** Production changes must go through the change process with a security impact analysis and a FedRAMP significant change evaluation for anything that touches the government partition or shared components. (CM-3; CM-4; PR.PS-01; C-IT-R01 (SCN-CSO-EVA))
4.7 **Vulnerability response.** All in-scope components must be scanned with credentials at least monthly. Each vulnerability must be evaluated for exploitability, internet reachability, and Potential Agency Impact, and remediated within STD-08 timeframes. KEVs must be remediated by the CISA catalog due date. (RA-5; SI-2; ID.RA-01; C-IT-R01 (VDR and VER rules))
4.8 **Software integrity.** VM templates and control plane releases must be built by the pipeline, signed with a key in the HSM, and verified at deployment, with an SBOM and build provenance for each release (STD-05). (SI-7; SA-10; SA-15; PR.PS-02; C-IT-R01)
4.9 **Media and drives.** Drives must be cryptographically erased before they leave a cage and destroyed by a certified vendor, with a certificate that matches each serial number. (MP-6; MP-5; PR.DS-01; C-IT-R01)
4.10 **Maintenance.** Hardware maintenance must be scheduled and recorded. Maintenance tools and diagnostic media must be checked before use. (MA-2; MA-3; PR.PS-03; C-IT-R01)
4.11 **Facilities.** The company must keep an approved access list for each cage, review it quarterly, and rely on the colocation providers for facility controls, confirmed by their SOC 2 reports each year. (PE-2; PE-3; PR.AA-06; C-IT-R01)
4.12 **Retention and deletion.** Customer data must be deleted within 30 days after contract end unless the customer or law requires otherwise. Records follow the records schedule. (SI-12; PR.DS-01; C-IT-R01)

## 5. Compliance and enforcement
P07 and the FedRAMP annual assessment test these statements. Scan coverage, drift, and KEV metrics are reported monthly to the CTO.

## 6. Exceptions
Through POL-01 section 4.8. Known exceptions at approval: about 9,000 older commercial volumes without encryption (due 2027-06-30); commercial template signing key in the pipeline (due 2026-12-31).

## 7. Related documents
POL-01; STD-01, STD-03, STD-05, STD-06, STD-08; SSP (P02); cloud control map (P04); risk register (P01 R-006, R-011, R-024, R-033, R-037, R-038)
