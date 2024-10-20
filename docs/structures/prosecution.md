# Prosecution Fields

The **Prosecution Fields** section of the Justice Information Exchange (JIX) language captures information about the prosecution process within criminal cases. This includes identifiers, offender details, and other key information necessary for the preparation and management of prosecutions. These fields ensure comprehensive documentation and tracking of prosecution activities within the justice system.

## Field Set Overview

The **Prosecution Fields** include attributes such as offender information, offence reason, and sequence, providing a detailed record of prosecution activities linked to cases.

### Core Fields

These are the essential fields required for documenting prosecution activities:

| Field Name                | Type      | Description                                                                 | Example                     |
|--------------------------|-----------|-----------------------------------------------------------------------------|-----------------------------|
| `prosecution.id`         | `keyword` | A unique identifier for each prosecution record.                            | `PRO12345`                  |
| `prosecution.case_id`    | `array`   | An array of unique identifiers for the cases associated with the prosecution. | `["CASE12345", "CASE67890"]` |
| `prosecution.offender`   | `text`    | The name of the defendant or offender involved in the prosecution.          | `John Doe`                  |
| `prosecution.offence_reason` | `text` | The reason for the offence (e.g., theft, assault).                          | `theft`                     |
| `prosecution.date`       | `date`    | The date when the prosecution action took place.                            | `2023-08-10`                |
| `prosecution.description`| `text`    | A detailed description of the prosecution activity.                         | `Prosecution for theft at a retail store.` |

### Extended Fields

These fields provide additional details and context for prosecution activities:

| Field Name                     | Type      | Description                                                                 | Example                     |
|-------------------------------|-----------|-----------------------------------------------------------------------------|-----------------------------|
| `prosecution.sequence`        | `integer` | The sequence number representing the order of offences for the defendant.   | `1`                         |
| `prosecution.status`          | `keyword` | The current status of the prosecution (e.g., ongoing, concluded).           | `ongoing`                   |
| `prosecution.related_materials` | `array`   | A list of material IDs related to the prosecution, such as indictments or evidence files. | `["MAT123", "MAT456"]`      |
| `prosecution.notes`           | `text`    | Additional notes or remarks about the prosecution action.                   | `Defendant has legal representation.` |

### Field Details

#### 1. `prosecution.id`
- **Type**: `keyword`
- **Description**: A unique identifier for each prosecution record.
- **Example**: `PRO12345`

#### 2. `prosecution.case_id`
- **Type**: `array`
- **Description**: An array of unique identifiers representing the cases linked to the prosecution action, allowing tracking across multiple cases.
- **Example**: `["CASE12345", "CASE67890"]`

#### 3. `prosecution.offender`
- **Type**: `text`
- **Description**: The name of the defendant or offender involved in the prosecution.
- **Example**: `John Doe`

#### 4. `prosecution.offence_reason`
- **Type**: `text`
- **Description**: The reason for the offence (e.g., theft, assault).
- **Example**: `theft`

#### 5. `prosecution.date`
- **Type**: `date`
- **Description**: The date when the prosecution action took place.
- **Example**: `2023-08-10`

#### 6. `prosecution.description`
- **Type**: `text`
- **Description**: A detailed description of the prosecution activity.
- **Example**: `Prosecution for theft at a retail store.`

#### 7. `prosecution.sequence`
- **Type**: `integer`
- **Description**: The sequence number representing the order of offences for the defendant.
- **Example**: `1`

#### 8. `prosecution.status`
- **Type**: `keyword`
- **Description**: The current status of the prosecution (e.g., ongoing, concluded).
- **Example**: `ongoing`

#### 9. `prosecution.related_materials`
- **Type**: `array`
- **Description**: A list of material IDs related to the prosecution, such as indictments or evidence files.
- **Example**: `["MAT123", "MAT456"]`

#### 10. `prosecution.notes`
- **Type**: `text`
- **Description**: Additional notes or remarks about the prosecution action.
- **Example**: `Defendant has legal representation.`

### Usage Notes

- **Core Fields**: These fields must be present for each prosecution action to ensure accurate tracking and documentation within the case timeline.
- **Extended Fields**: Additional fields can be used when further details are available or necessary for the prosecution context.

### Example Document

#### YAML

```yaml
prosecution:
  id: PRO12345
  case_id: ["CASE12345", "CASE67890"]
  offender: John Doe
  offence_reason: theft
  date: 2023-08-10
  description: Prosecution for theft at a retail store.
  sequence: 1
  status: ongoing
  related_materials: ["MAT123", "MAT456"]
  notes: Defendant has legal representation.
```

#### JSON

```json
{
  "prosecution": {
    "id": "PRO12345",
    "case_id": ["CASE12345", "CASE67890"],
    "offender": "John Doe",
    "offence_reason": "theft",
    "date": "2023-08-10",
    "description": "Prosecution for theft at a retail store.",
    "sequence": 1,
    "status": "ongoing",
    "related_materials": ["MAT123", "MAT456"],
    "notes": "Defendant has legal representation."
  }
}
```
