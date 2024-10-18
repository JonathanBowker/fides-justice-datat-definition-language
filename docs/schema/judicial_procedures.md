# Judicial Procedures Fields

The **Judicial Procedures Fields** section of the Judicial Electronic Data Interchange Language (JEDI) captures information about judicial actions and court-related processes within legal cases. This includes details about hearings, motions, rulings, and other court events. These fields ensure comprehensive documentation and tracking of judicial activities as they relate to the progression of cases in the justice system.

## Field Set Overview

The **Judicial Procedures Fields** include attributes such as procedure type, date, location, and involved participants, providing a detailed record of judicial activities associated with each case.

### Core Fields

These are the essential fields required for documenting judicial procedures:

| Field Name                    | Type      | Description                                                                 | Example                     |
|------------------------------|-----------|-----------------------------------------------------------------------------|-----------------------------|
| `judicial_procedure.id`      | `keyword` | A unique identifier for each judicial procedure record.                     | `JP12345`                   |
| `judicial_procedure.case_id` | `array`   | An array of unique identifiers for the cases associated with the judicial procedure. | `["CASE12345", "CASE67890"]` |
| `judicial_procedure.type`    | `keyword` | The type of judicial procedure (e.g., hearing, ruling, motion).            | `hearing`                   |
| `judicial_procedure.date`    | `date`    | The date when the judicial procedure took place.                            | `2023-08-20`                |
| `judicial_procedure.location`| `text`    | The location where the judicial procedure occurred.                         | `Courtroom 3, Anytown District Court` |
| `judicial_procedure.description` | `text` | A detailed description of the judicial procedure.                           | `Initial hearing on motion to dismiss.`|

### Extended Fields

These fields provide additional details and context for judicial procedures:

| Field Name                    | Type      | Description                                                                 | Example                     |
|------------------------------|-----------|-----------------------------------------------------------------------------|-----------------------------|
| `judicial_procedure.participant_ids` | `array`   | An array of unique identifiers for the participants involved in the procedure. | `["PART123", "PART456"]`    |
| `judicial_procedure.status`  | `keyword` | The current status of the judicial procedure (e.g., scheduled, completed, postponed). | `completed`                 |
| `judicial_procedure.related_documents` | `array`   | A list of document IDs related to the judicial procedure, such as rulings or transcripts. | `["DOC123", "DOC456"]`      |
| `judicial_procedure.judge_id` | `keyword` | The unique identifier of the judge presiding over the judicial procedure.   | `JUDGE123`                  |
| `judicial_procedure.notes`   | `text`    | Additional notes or remarks about the judicial procedure.                   | `Judge ruled to proceed with trial.`   |

### Field Details

#### 1. `judicial_procedure.id`
- **Type**: `keyword`
- **Description**: A unique identifier for each judicial procedure record.
- **Example**: `JP12345`

#### 2. `judicial_procedure.case_id`
- **Type**: `array`
- **Description**: An array of unique identifiers representing the cases linked to the judicial procedure, allowing tracking across multiple cases.
- **Example**: `["CASE12345", "CASE67890"]`

#### 3. `judicial_procedure.type`
- **Type**: `keyword`
- **Description**: The type of judicial procedure (e.g., hearing, ruling, motion).
- **Example**: `hearing`

#### 4. `judicial_procedure.date`
- **Type**: `date`
- **Description**: The date when the judicial procedure took place.
- **Example**: `2023-08-20`

#### 5. `judicial_procedure.location`
- **Type**: `text`
- **Description**: The location where the judicial procedure occurred.
- **Example**: `Courtroom 3, Anytown District Court`

#### 6. `judicial_procedure.description`
- **Type**: `text`
- **Description**: A detailed description of the judicial procedure.
- **Example**: `Initial hearing on motion to dismiss.`

#### 7. `judicial_procedure.participant_ids`
- **Type**: `array`
- **Description**: An array of unique identifiers for the participants involved in the procedure.
- **Example**: `["PART123", "PART456"]`

#### 8. `judicial_procedure.status`
- **Type**: `keyword`
- **Description**: The current status of the judicial procedure (e.g., scheduled, completed, postponed).
- **Example**: `completed`

#### 9. `judicial_procedure.related_documents`
- **Type**: `array`
- **Description**: A list of document IDs related to the judicial procedure, such as rulings or court transcripts.
- **Example**: `["DOC123", "DOC456"]`

#### 10. `judicial_procedure.judge_id`
- **Type**: `keyword`
- **Description**: The unique identifier of the judge presiding over the judicial procedure.
- **Example**: `JUDGE123`

#### 11. `judicial_procedure.notes`
- **Type**: `text`
- **Description**: Additional notes or remarks about the judicial procedure.
- **Example**: `Judge ruled to proceed with trial.`

### Usage Notes

- **Core Fields**: These fields must be present for each judicial procedure to ensure accurate tracking and documentation within the case timeline.
- **Extended Fields**: Additional fields can be used when further details are available or necessary for the context of the judicial procedure.

### Example Document

#### YAML

```yaml
judicial_procedure:
  id: JP12345
  case_id: ["CASE12345", "CASE67890"]
  type: hearing
  date: 2023-08-20
  location: Courtroom 3, Anytown District Court
  description: Initial hearing on motion to dismiss.
  participant_ids: ["PART123", "PART456"]
  status: completed
  related_documents: ["DOC123", "DOC456"]
  judge_id: JUDGE123
  notes: Judge ruled to proceed with trial.
```

#### JSON

```json
{
  "judicial_procedure": {
    "id": "JP12345",
    "case_id": ["CASE12345", "CASE67890"],
    "type": "hearing",
    "date": "2023-08-20",
    "location": "Courtroom 3, Anytown District Court",
    "description": "Initial hearing on motion to dismiss.",
    "participant_ids": ["PART123", "PART456"],
    "status": "completed",
    "related_documents": ["DOC123", "DOC456"],
    "judge_id": "JUDGE123",
    "notes": "Judge ruled to proceed with trial."
  }
}
```

This markdown file (`judicial_procedures.md`) provides a comprehensive overview of the **Judicial Procedures Fields** in the Judicial Electronic Data Interchange Language, ensuring proper documentation and tracking of court-related activities associated with legal cases.
