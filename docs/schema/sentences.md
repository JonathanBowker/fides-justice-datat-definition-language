# Sentences Fields

The **Sentences Fields** section of the Judicial Electronic Data Interchange Language (JEDI) captures information about sentencing outcomes for individuals involved in cases. This includes details about the type of sentence imposed, duration, conditions, and any related legal requirements. These fields ensure accurate documentation and tracking of sentences within the justice system.

## Field Set Overview

The **Sentences Fields** encompass attributes such as sentence type, duration, conditions, and related cases, providing a complete record of sentencing information.

### Core Fields

These are the essential fields required for documenting sentences:

| Field Name                    | Type      | Description                                                                 | Example                     |
|------------------------------|-----------|-----------------------------------------------------------------------------|-----------------------------|
| `sentence.id`                | `keyword` | A unique identifier for each sentence record.                               | `SENT12345`                 |
| `sentence.case_id`           | `array`   | An array of unique identifiers for the cases associated with the sentence.  | `["CASE12345", "CASE67890"]`|
| `sentence.type`              | `keyword` | The type of sentence (e.g., imprisonment, probation, community service).    | `imprisonment`              |
| `sentence.duration`          | `text`    | The duration of the sentence (e.g., 2 years, 6 months probation).           | `2 years`                   |
| `sentence.start_date`        | `date`    | The date when the sentence begins.                                          | `2023-06-15`                |
| `sentence.end_date`          | `date`    | The date when the sentence ends (if applicable).                            | `2025-06-15`                |

### Extended Fields

These fields provide additional details and context for sentences:

| Field Name                    | Type      | Description                                                                 | Example                     |
|------------------------------|-----------|-----------------------------------------------------------------------------|-----------------------------|
| `sentence.conditions`        | `text`    | Specific conditions imposed as part of the sentence (e.g., curfew, no contact order). | `Curfew from 10 PM to 6 AM`|
| `sentence.fine_amount`       | `double`  | The amount of any fine imposed as part of the sentence.                     | `1000.00`                   |
| `sentence.supervision_required` | `boolean` | Indicates if supervision is required as part of the sentence.               | `true`                      |
| `sentence.supervisor`        | `text`    | The name or identifier of the officer or agency supervising the individual. | `Officer John Doe`          |

### Field Details

#### 1. `sentence.id`
- **Type**: `keyword`
- **Description**: A unique identifier for each sentence record.
- **Example**: `SENT12345`

#### 2. `sentence.case_id`
- **Type**: `array`
- **Description**: An array of unique identifiers representing the cases linked to the sentence, allowing tracking across multiple cases.
- **Example**: `["CASE12345", "CASE67890"]`

#### 3. `sentence.type`
- **Type**: `keyword`
- **Description**: The type of sentence imposed, such as imprisonment, probation, or community service.
- **Example**: `imprisonment`

#### 4. `sentence.duration`
- **Type**: `text`
- **Description**: The duration of the sentence.
- **Example**: `2 years`

#### 5. `sentence.start_date`
- **Type**: `date`
- **Description**: The date when the sentence begins.
- **Example**: `2023-06-15`

#### 6. `sentence.end_date`
- **Type**: `date`
- **Description**: The date when the sentence ends (if applicable).
- **Example**: `2025-06-15`

#### 7. `sentence.conditions`
- **Type**: `text`
- **Description**: Specific conditions imposed as part of the sentence.
- **Example**: `Curfew from 10 PM to 6 AM`

#### 8. `sentence.fine_amount`
- **Type**: `double`
- **Description**: The amount of any fine imposed as part of the sentence.
- **Example**: `1000.00`

#### 9. `sentence.supervision_required`
- **Type**: `boolean`
- **Description**: Indicates if supervision is required as part of the sentence.
- **Example**: `true`

#### 10. `sentence.supervisor`
- **Type**: `text`
- **Description**: The name or identifier of the supervising officer or agency.
- **Example**: `Officer John Doe`

### Usage Notes

- **Core Fields**: These fields must be present for each sentence to ensure accurate tracking and documentation.
- **Extended Fields**: Additional fields can be used when further details are available or necessary for the sentence context.

### Example Document

#### YAML

```yaml
sentence:
  id: SENT12345
  case_id: ["CASE12345", "CASE67890"]
  type: imprisonment
  duration: 2 years
  start_date: 2023-06-15
  end_date: 2025-06-15
  conditions: Curfew from 10 PM to 6 AM
  fine_amount: 1000.00
  supervision_required: true
  supervisor: Officer John Doe
```

#### JSON

```json
{
  "sentence": {
    "id": "SENT12345",
    "case_id": ["CASE12345", "CASE67890"],
    "type": "imprisonment",
    "duration": "2 years",
    "start_date": "2023-06-15",
    "end_date": "2025-06-15",
    "conditions": "Curfew from 10 PM to 6 AM",
    "fine_amount": 1000.00,
    "supervision_required": true,
    "supervisor": "Officer John Doe"
  }
}
```

This markdown file (`sentences.md`) provides a comprehensive overview of the **Sentences Fields** in the Judicial Electronic Data Interchange Language, ensuring proper documentation and tracking of sentencing outcomes associated with legal cases and individuals.