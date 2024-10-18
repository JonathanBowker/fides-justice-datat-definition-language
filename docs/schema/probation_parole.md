# Probation and Parole Fields

The **Probation and Parole Fields** section of the Judicial Electronic Data Interchange Language (JEDI) captures information about probation and parole conditions for individuals involved in cases. These fields document supervision requirements, compliance monitoring, and other relevant details to manage and track individuals under court-imposed supervision.

## Field Set Overview

The **Probation and Parole Fields** include attributes such as supervision terms, start and end dates, conditions imposed, and compliance status, providing a comprehensive view of the probation and parole process for individuals in the justice system.

### Core Fields

These are the essential fields required for documenting probation and parole details:

| Field Name                    | Type      | Description                                                                 | Example                     |
|------------------------------|-----------|-----------------------------------------------------------------------------|-----------------------------|
| `probation_parole.id`        | `keyword` | A unique identifier for each probation or parole record.                    | `PP12345`                   |
| `probation_parole.case_id`   | `array`   | An array of unique identifiers for the cases associated with the probation or parole. | `["CASE12345", "CASE67890"]` |
| `probation_parole.type`      | `keyword` | The type of supervision (e.g., probation, parole).                          | `probation`                 |
| `probation_parole.start_date`| `date`    | The date when the probation or parole period begins.                        | `2023-01-01`                |
| `probation_parole.end_date`  | `date`    | The date when the probation or parole period ends.                          | `2023-12-31`                |
| `probation_parole.conditions`| `text`    | Specific conditions imposed (e.g., no alcohol consumption, curfew).         | `Curfew from 10 PM to 6 AM` |
| `probation_parole.status`    | `keyword` | The current status of the individual under supervision (e.g., compliant, non-compliant). | `compliant`                 |

### Extended Fields

These fields provide additional information and context for managing probation and parole cases:

| Field Name                    | Type      | Description                                                                 | Example                     |
|------------------------------|-----------|-----------------------------------------------------------------------------|-----------------------------|
| `probation_parole.supervisor`| `text`    | The name or identifier of the officer supervising the individual.           | `Officer Jane Smith`        |
| `probation_parole.check_in_frequency` | `keyword` | The required frequency of check-ins (e.g., weekly, monthly).              | `weekly`                    |
| `probation_parole.violation_history` | `array`   | Records of any violations during the probation or parole period.            | `["Missed check-in on 2023-02-10"]` |
| `probation_parole.notes`     | `text`    | Additional notes related to the supervision of the individual.              | `Client has shown improvement in behavior.`|

### Field Details

#### 1. `probation_parole.id`
- **Type**: `keyword`
- **Description**: A unique identifier for each probation or parole record.
- **Example**: `PP12345`

#### 2. `probation_parole.case_id`
- **Type**: `array`
- **Description**: An array of unique identifiers representing the cases linked to the probation or parole record, allowing tracking across multiple cases.
- **Example**: `["CASE12345", "CASE67890"]`

#### 3. `probation_parole.type`
- **Type**: `keyword`
- **Description**: Indicates whether the supervision is probation or parole.
- **Example**: `probation`

#### 4. `probation_parole.start_date`
- **Type**: `date`
- **Description**: The date when the probation or parole period begins.
- **Example**: `2023-01-01`

#### 5. `probation_parole.end_date`
- **Type**: `date`
- **Description**: The date when the probation or parole period ends.
- **Example**: `2023-12-31`

#### 6. `probation_parole.conditions`
- **Type**: `text`
- **Description**: Specific conditions imposed during the probation or parole period.
- **Example**: `Curfew from 10 PM to 6 AM`

#### 7. `probation_parole.status`
- **Type**: `keyword`
- **Description**: The current status of the individual under supervision (e.g., compliant, non-compliant).
- **Example**: `compliant`

#### 8. `probation_parole.supervisor`
- **Type**: `text`
- **Description**: The name or identifier of the supervising officer.
- **Example**: `Officer Jane Smith`

#### 9. `probation_parole.check_in_frequency`
- **Type**: `keyword`
- **Description**: The frequency of required check-ins (e.g., weekly, monthly).
- **Example**: `weekly`

#### 10. `probation_parole.violation_history`
- **Type**: `array`
- **Description**: A record of any violations during the supervision period.
- **Example**: `["Missed check-in on 2023-02-10"]`

#### 11. `probation_parole.notes`
- **Type**: `text`
- **Description**: Additional notes related to the individual’s behaviour or compliance during the supervision period.
- **Example**: `Client has shown improvement in behavior.`

### Usage Notes

- **Core Fields**: These fields must be present for each probation or parole record to ensure accurate tracking and management.
- **Extended Fields**: Additional fields can be used to provide more detailed information, such as supervisor details and violation history.

### Example Document

#### YAML

```yaml
probation_parole:
  id: PP12345
  case_id: ["CASE12345", "CASE67890"]
  type: probation
  start_date: 2023-01-01
  end_date: 2023-12-31
  conditions: Curfew from 10 PM to 6 AM
  status: compliant
  supervisor: Officer Jane Smith
  check_in_frequency: weekly
  violation_history: ["Missed check-in on 2023-02-10"]
  notes: Client has shown improvement in behavior.
```

#### JSON

```json
{
  "probation_parole": {
    "id": "PP12345",
    "case_id": ["CASE12345", "CASE67890"],
    "type": "probation",
    "start_date": "2023-01-01",
    "end_date": "2023-12-31",
    "conditions": "Curfew from 10 PM to 6 AM",
    "status": "compliant",
    "supervisor": "Officer Jane Smith",
    "check_in_frequency": "weekly",
    "violation_history": ["Missed check-in on 2023-02-10"],
    "notes": "Client has shown improvement in behavior."
  }
}
```

This markdown file (`probation_parole.md`) provides a comprehensive overview of the **Probation and Parole Fields** in the Judicial Electronic Data Interchange Language, ensuring proper documentation and tracking of individuals under court-imposed supervision.
