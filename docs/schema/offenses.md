# Offenses Fields

The **Offenses Fields** section of the Judicial Electronic Data Interchange Language (JEDI) captures information about the offenses associated with legal cases. This includes details about the nature of the offense, the statutes violated, and the severity of the charges. These fields ensure comprehensive documentation and tracking of criminal activity within the justice system.

## Field Set Overview

The **Offenses Fields** encompass attributes such as offense type, description, severity, and related statutes, ensuring accurate documentation of offenses linked to cases.

### Core Fields

These are the essential fields required for documenting offenses:

| Field Name                    | Type      | Description                                                                 | Example                     |
|------------------------------|-----------|-----------------------------------------------------------------------------|-----------------------------|
| `offense.id`                 | `keyword` | A unique identifier for each offense record.                                | `OFF12345`                  |
| `offense.case_id`            | `array`   | An array of unique identifiers for the cases associated with the offense.   | `["CASE12345", "CASE67890"]`|
| `offense.type`               | `keyword` | The type of offense (e.g., theft, assault, fraud).                          | `theft`                     |
| `offense.description`        | `text`    | A detailed description of the offense.                                      | `Theft of a vehicle from a parking lot.` |
| `offense.statute`            | `keyword` | The specific statute or law violated by the offense.                        | `Penal Code Section 487`    |
| `offense.date`               | `date`    | The date when the offense occurred.                                         | `2023-06-15`                |
| `offense.severity`           | `keyword` | The severity level of the offense (e.g., felony, misdemeanor).              | `felony`                    |

### Extended Fields

These fields provide additional information and context for offenses:

| Field Name                    | Type      | Description                                                                 | Example                     |
|------------------------------|-----------|-----------------------------------------------------------------------------|-----------------------------|
| `offense.location`           | `text`    | The location where the offense took place.                                  | `123 Market Street, Anytown`|
| `offense.status`             | `keyword` | The current status of the offense (e.g., charged, under investigation).     | `charged`                   |
| `offense.victim_ids`         | `array`   | An array of unique identifiers for the victims associated with the offense. | `["VICTIM123", "VICTIM456"]`|
| `offense.offender_ids`       | `array`   | An array of unique identifiers for the offenders associated with the offense. | `["OFFENDER123"]`          |

### Field Details

#### 1. `offense.id`
- **Type**: `keyword`
- **Description**: A unique identifier for each offense record.
- **Example**: `OFF12345`

#### 2. `offense.case_id`
- **Type**: `array`
- **Description**: An array of unique identifiers representing the cases linked to the offense, allowing tracking across multiple cases.
- **Example**: `["CASE12345", "CASE67890"]`

#### 3. `offense.type`
- **Type**: `keyword`
- **Description**: The type of offense (e.g., theft, assault, fraud).
- **Example**: `theft`

#### 4. `offense.description`
- **Type**: `text`
- **Description**: A detailed description of the offense.
- **Example**: `Theft of a vehicle from a parking lot.`

#### 5. `offense.statute`
- **Type**: `keyword`
- **Description**: The specific statute or law violated by the offense.
- **Example**: `Penal Code Section 487`

#### 6. `offense.date`
- **Type**: `date`
- **Description**: The date when the offense occurred.
- **Example**: `2023-06-15`

#### 7. `offense.severity`
- **Type**: `keyword`
- **Description**: The severity level of the offense (e.g., felony, misdemeanor).
- **Example**: `felony`

#### 8. `offense.location`
- **Type**: `text`
- **Description**: The location where the offense took place.
- **Example**: `123 Market Street, Anytown`

#### 9. `offense.status`
- **Type**: `keyword`
- **Description**: The current status of the offense (e.g., charged, under investigation).
- **Example**: `charged`

#### 10. `offense.victim_ids`
- **Type**: `array`
- **Description**: An array of unique identifiers for the victims associated with the offense.
- **Example**: `["VICTIM123", "VICTIM456"]`

#### 11. `offense.offender_ids`
- **Type**: `array`
- **Description**: An array of unique identifiers for the offenders associated with the offense.
- **Example**: `["OFFENDER123"]`

### Usage Notes

- **Core Fields**: These fields must be present for each offense to ensure accurate tracking and documentation.
- **Extended Fields**: Additional fields can be used when further details are available or necessary for the case context.

### Example Document

#### YAML

```yaml
offense:
  id: OFF12345
  case_id: ["CASE12345", "CASE67890"]
  type: theft
  description: Theft of a vehicle from a parking lot.
  statute: Penal Code Section 487
  date: 2023-06-15
  severity: felony
  location: 123 Market Street, Anytown
  status: charged
  victim_ids: ["VICTIM123", "VICTIM456"]
  offender_ids: ["OFFENDER123"]
```

#### JSON

```json
{
  "offense": {
    "id": "OFF12345",
    "case_id": ["CASE12345", "CASE67890"],
    "type": "theft",
    "description": "Theft of a vehicle from a parking lot.",
    "statute": "Penal Code Section 487",
    "date": "2023-06-15",
    "severity": "felony",
    "location": "123 Market Street, Anytown",
    "status": "charged",
    "victim_ids": ["VICTIM123", "VICTIM456"],
    "offender_ids": ["OFFENDER123"]
  }
}
```

This markdown file (`offenses.md`) provides a comprehensive overview of the **Offenses Fields** in the Judicial Electronic Data Interchange Language, ensuring proper documentation and tracking of offenses linked to legal cases and individuals.