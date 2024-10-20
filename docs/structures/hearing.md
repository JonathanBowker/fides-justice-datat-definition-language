# Hearing Fields

The **Hearing Fields** section of the Justice Information Exchange (JIX) language captures information about legal hearings within the criminal justice system. This includes details about the location, date, time, and participants present at the hearing. These fields ensure comprehensive documentation and tracking of hearings within the justice system.

## Field Set Overview

The **Hearing Fields** include attributes such as the court location, hearing date and time, language used, and the presence of the defendant, providing a complete record of hearings associated with cases.

### Core Fields

These are the essential fields required for documenting hearing activities:

| Field Name                    | Type      | Description                                                                 | Example                     |
|------------------------------|-----------|-----------------------------------------------------------------------------|-----------------------------|
| `hearing.id`                 | `keyword` | A unique identifier for each hearing record.                                | `HEAR12345`                 |
| `hearing.case_id`            | `array`   | An array of unique identifiers for the cases associated with the hearing.   | `["CASE12345", "CASE67890"]`|
| `hearing.location`           | `text`    | The location of the court where the hearing is held.                        | `Courtroom 5, Anytown Court`|
| `hearing.date`               | `date`    | The date when the hearing takes place.                                      | `2023-08-10`                |
| `hearing.time`               | `time`    | The time when the hearing takes place.                                      | `10:00 AM`                  |
| `hearing.language`           | `keyword` | The language used during the hearing.                                       | `English`                   |
| `hearing.defendant_present`  | `boolean` | Indicates whether the defendant is present at the hearing.                  | `true`                      |

### Extended Fields

These fields provide additional details and context for hearing activities:

| Field Name                    | Type      | Description                                                                 | Example                     |
|------------------------------|-----------|-----------------------------------------------------------------------------|-----------------------------|
| `hearing.documentation_language` | `keyword` | The language used in the documentation or transcripts of the hearing.       | `English`                   |
| `hearing.report_requested_date` | `date`    | The date when a report (e.g., Pre-Sentence Report) was requested.           | `2023-07-15`                |
| `hearing.report_completed_date` | `date`    | The date when the requested report was completed.                           | `2023-07-20`                |
| `hearing.related_materials`  | `array`   | A list of material IDs related to the hearing, such as transcripts or evidence files. | `["MAT123", "MAT456"]`      |
| `hearing.notes`              | `text`    | Additional notes or remarks about the hearing.                              | `Defendant requested an adjournment.` |

### Field Details

#### 1. `hearing.id`
- **Type**: `keyword`
- **Description**: A unique identifier for each hearing record.
- **Example**: `HEAR12345`

#### 2. `hearing.case_id`
- **Type**: `array`
- **Description**: An array of unique identifiers representing the cases linked to the hearing, allowing tracking across multiple cases.
- **Example**: `["CASE12345", "CASE67890"]`

#### 3. `hearing.location`
- **Type**: `text`
- **Description**: The location of the court where the hearing is held.
- **Example**: `Courtroom 5, Anytown Court`

#### 4. `hearing.date`
- **Type**: `date`
- **Description**: The date when the hearing takes place.
- **Example**: `2023-08-10`

#### 5. `hearing.time`
- **Type**: `time`
- **Description**: The time when the hearing takes place.
- **Example**: `10:00 AM`

#### 6. `hearing.language`
- **Type**: `keyword`
- **Description**: The language used during the hearing.
- **Example**: `English`

#### 7. `hearing.defendant_present`
- **Type**: `boolean`
- **Description**: Indicates whether the defendant is present at the hearing.
- **Example**: `true`

#### 8. `hearing.documentation_language`
- **Type**: `keyword`
- **Description**: The language used in the documentation or transcripts of the hearing.
- **Example**: `English`

#### 9. `hearing.report_requested_date`
- **Type**: `date`
- **Description**: The date when a report (e.g., Pre-Sentence Report) was requested.
- **Example**: `2023-07-15`

#### 10. `hearing.report_completed_date`
- **Type**: `date`
- **Description**: The date when the requested report was completed.
- **Example**: `2023-07-20`

#### 11. `hearing.related_materials`
- **Type**: `array`
- **Description**: A list of material IDs related to the hearing, such as transcripts or evidence files.
- **Example**: `["MAT123", "MAT456"]`

#### 12. `hearing.notes`
- **Type**: `text`
- **Description**: Additional notes or remarks about the hearing.
- **Example**: `Defendant requested an adjournment.`

### Usage Notes

- **Core Fields**: These fields must be present for each hearing to ensure accurate tracking and documentation within the case timeline.
- **Extended Fields**: Additional fields can be used when further details are available or necessary for the hearing context.

### Example Document

#### YAML

```yaml
hearing:
  id: HEAR12345
  case_id: ["CASE12345", "CASE67890"]
  location: Courtroom 5, Anytown Court
  date: 2023-08-10
  time: 10:00 AM
  language: English
  defendant_present: true
  documentation_language: English
  report_requested_date: 2023-07-15
  report_completed_date: 2023-07-20
  related_materials: ["MAT123", "MAT456"]
  notes: Defendant requested an adjournment.
```

#### JSON

```json
{
  "hearing": {
    "id": "HEAR12345",
    "case_id": ["CASE12345", "CASE67890"],
    "location": "Courtroom 5, Anytown Court",
    "date": "2023-08-10",
    "time": "10:00 AM",
    "language": "English",
    "defendant_present": true,
    "documentation_language": "English",
    "report_requested_date": "2023-07-15",
    "report_completed_date": "2023-07-20",
    "related_materials": ["MAT123", "MAT456"],
    "notes": "Defendant requested an adjournment."
  }
}
```
