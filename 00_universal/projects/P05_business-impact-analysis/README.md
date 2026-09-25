# P05. Business Impact Analysis (BIA)

**Notion project:** Run a Business Impact Analysis. Criticality ratings, recovery time objectives, and resource dependencies for a business process.

## Universal approach (macro to granular)

The three steps below come from the official **NIST SP 800-34 Rev. 1 BIA template**.

1. **Set up (macro).** Define impact categories and severity values (Severe, Moderate, Minimal) for the organization, such as cost, operations, safety, regulatory, and reputation. Dollar thresholds scale with the tier.
2. **Determine process and system criticality.** List the business processes, then rate the outage impact per category. Estimate:
   - **MTD** (Maximum Tolerable Downtime): the total outage leaders will accept.
   - **RTO** (Recovery Time Objective): the maximum time a resource can stay down.
   - **RPO** (Recovery Point Objective): how far back in time data may be recovered to.
   RTO must be shorter than MTD. Record what drives each value and any manual workarounds.
3. **Identify resource requirements.** List the systems, data, people, facilities, and third parties each process depends on.
4. **Identify recovery priorities (granular).** Set the order of recovery for each resource and its expected recovery time.
5. **Link to risk.** Use the results to set impact levels in the risk register (P01), the FIPS 199 availability rating in the SSP (P02), and risk prioritization per NIST IR 8286D.

## Outputs

| File | Purpose |
|---|---|
| `bia.csv` | One row per process: impacts per category, MTD, RTO, RPO, dependencies, recovery priority. |
| `bia-report.md` | Overview, system description, impact categories, results, resource requirements, and recovery priorities. It follows the SP 800-34 template sections. |

## Quality checklist

- [ ] Every process has an MTD, and its RTO is shorter than the MTD.
- [ ] Every RPO is supported by a backup or replication method named in the resources table.
- [ ] Third-party dependencies are named, such as SaaS vendors, the MSP, and utilities.
- [ ] Sector-specific downtime drivers are cited, for example patient safety, ambulance diversion, or service restoration duties.

## Sources

SRC-800-34 (official BIA template docx linked in the source register), SRC-FIPS-199, SRC-IR-8286D.
