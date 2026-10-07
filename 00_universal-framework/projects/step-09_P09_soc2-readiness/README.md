# P09. SOC 2 Readiness Checklist

**Notion project:** Complete a SOC 2 Readiness Checklist. A self-assessment against SOC 2 requirements.

## Universal approach (macro to granular)

1. **Decide whether SOC 2 fits (macro).** SOC 2 reports on controls at a *service organization*, a company that provides services to other businesses. Record why customers would ask {{company}} for one. If the scenario is not a service organization, the exercise still works as a customer-assurance readiness check, but note that another assurance mechanism may be more typical. The vertical overlay names these alternatives, for example PCI DSS for merchants and CMMC for defense contractors.
2. **Scope the system and categories.** Security (the Common Criteria, CC1-CC9) is always in scope. Add Availability, Confidentiality, Processing Integrity, or Privacy based on customer commitments.
3. **Self-assess each criterion (granular).** For each criterion ID, record the control in place, the owner, the evidence, and a readiness status.
4. **Plan remediation.** For any gap, plan the fix and start evidence collection early. A Type 2 report covers operating effectiveness over a period of time.
5. **Map to other work.** Reuse evidence from P02, P06, and P07. AICPA publishes a TSC-to-SP 800-53 mapping (see SRC-TSC).

## Copyright note

The AICPA *2017 Trust Services Criteria (With Revised Points of Focus, 2022)* is copyrighted. This checklist lists the **criterion IDs** with short topic labels written for this repository. Read the full criterion text and points of focus in the official AICPA publication (free account required).

## Outputs

`soc2-readiness.csv` (every criterion ID, pre-listed) and `soc2-readiness-summary.md`.

## Sources

SRC-TSC.
