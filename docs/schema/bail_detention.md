# Bail and Detention Fields

The **Bail and Detention Fields** section of the Judicial Electronic Data Interchange Language (JEDI) captures information about bail conditions and detention statuses for individuals involved in legal cases. This includes details such as bail amounts, conditions, and detention status, ensuring comprehensive documentation and tracking of pre-trial supervision and custody arrangements.

## Field Set Overview

The **Bail and Detention Fields** include attributes such as bail amount, detention status, and conditions, providing a complete record of bail and detention information associated with each case.

### Core Fields

These are the essential fields required for documenting bail and detention details:

| Field Name                    | Type      | Description                                                                 | Example                     |
|------------------------------|-----------|-----------------------------------------------------------------------------|-----------------------------|
| `bail_detention.id`          | `keyword` | A unique identifier for each bail or detention record.                      | `BD12345`                   |
| `bail_detention.case_id`     | `array`   | An array of unique identifiers for the cases associated with the bail or detention record. | `["CASE12345", "CASE67890"]` |
| `bail_detention.type`        | `keyword` | The type of record (e.g., bail, detention).                                 | `bail`                      |
| `bail_detention.amount`      | `double`  | The amount set for bail (if applicable).                                    | `5000.00`                   |
| `bail_detention.status`      | `keyword` | The current status of the individual (e.g., in custody, released on bail).  | `released on bail`          |
| `bail_detention.date`        | `date`    | The date when the bail or detention decision was made.                      | `2023-09-01`                |

### Extended Fields

These fields provide additional information and context for bail and detention records:

| Field Name                    | Type      | Description                                                                 | Example                     |
|------------------------------|-----------|-----------------------------------------------------------------------------|-----------------------------|
| `bail_detention.conditions`  | `text`    | Conditions imposed as part of bail (e.g., travel restrictions, curfew).     | `No contact with victim, curfew from 10 PM to 6 AM` |
| `bail_detention.location`    | `text`    | The location where the individual is detained or where bail conditions are being monitored. | `Anytown Detention Center`  |
| `bail_detention.supervision_required` | `boolean` | Indicates if supervision is required as part of the bail conditions.        | `true`                      |
| `bail_detention.supervisor`  | `text`    | The name or identifier of the officer or agency supervising the individual. | `Officer Jane Smith`        |
| `bail_detention.notes`       | `text`    | Additional notes or remarks about the bail or detention decision.           | `Individual must attend weekly check-ins with officer.` |

### Field Details

#### 1. `bail_detention.id`
- **Type**: `keyword`
- **Description**: A unique identifier for each bail or detention record.
- **Example**: `BD12345`

#### 2. `bail_detention.case_id`
- **Type**: `array`
- **Description**: An array of unique identifiers representing the cases linked to the bail or detention record, allowing tracking across multiple cases.
- **Example**: `["CASE12345", "CASE67890"]`

#### 3. `bail_detention.type`
- **Type**: `keyword`
- **Description**: The type of record, such as bail or detention.
- **Example**: `bail`

#### 4. `bail_detention.amount`
- **Type**: `double`
- **Description**: The amount set for bail (if applicable).
- **Example**: `5000.00`

#### 5. `bail_detention.status`
- **Type**: `keyword`
- **Description**: The current status of the individual, such as in custody or released on bail.
- **Example**: `released on bail`

#### 6. `bail_detention.date`
- **Type**: `date`
- **Description**: The date when the bail or detention decision was made.
- **Example**: `2023-09-01`

#### 7. `bail_detention.conditions`
- **Type**: `text`
- **Description**: Conditions imposed as part of bail, such as curfews or restrictions.
- **Example**: `No contact with victim, curfew from 10 PM to 6 AM`

#### 8. `bail_detention.location`
- **Type**: `text`
- **Description**: The location where the individual is detained or monitored.
- **Example**: `Anytown Detention Center`

#### 9. `bail_detention.supervision_required`
- **Type**: `boolean`
- **Description**: Indicates if supervision is required as part of the bail conditions.
- **Example**: `true`

#### 10. `bail_detention.supervisor`
- **Type**: `text`
- **Description**: The name or identifier of the officer or agency supervising the individual under bail.
- **Example**: `Officer Jane Smith`

#### 11. `bail_detention.notes`
- **Type**: `text`
- **Description**: Additional notes or remarks about the bail or detention decision.
- **Example**: `Individual must attend weekly check-ins with officer.`

### Usage Notes

- **Core Fields**: These fields must be present for each bail or detention record to ensure accurate tracking and documentation.
- **Extended Fields**: Additional fields can be used when further details are available or necessary for the context of the bail or detention decision.

### Example Document

#### YAML

```yaml
bail_detention:
  id: BD12345
  case_id: ["CASE12345", "CASE67890"]
  type: bail
  amount: 5000.00
  status: released on bail
  date: 2023-09-01
  conditions: No contact with victim, curfew from 10 PM to 6 AM
  location: Anytown Detention Center
  supervision_required: true
  supervisor: Officer Jane Smith
  notes: Individual must attend weekly check-ins with officer.
```

#### JSON

```json
{
  "bail_detention": {
    "id": "BD12345",
    "case_id": ["CASE12345", "CASE67890"],
    "type": "bail",
    "amount": 5000.00,
    "status": "released on bail",
    "date": "2023-09-01",
    "conditions": "No contact with victim, curfew from 10 PM to 6 AM",
    "location": "Anytown Detention Center",
    "supervision_required": true,
    "supervisor": "Officer Jane Smith",
    "notes": "Individual must attend weekly check-ins with officer."
  }
}
```

This markdown file (`bail_detention.md`) provides a comprehensive overview of the **Bail and Detention Fields** in the Judicial Electronic Data Interchange Language, ensuring proper documentation and tracking of pre-trial supervision and custody arrangements associated with legal cases.