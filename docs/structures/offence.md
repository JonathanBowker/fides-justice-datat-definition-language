# Offence Fields

The **Offence Fields** section of the Justice Information Exchange (JIX) language captures information about offences within the criminal justice system. This includes details on the type, category, and specifics of the offence, ensuring a consistent and standardised approach to documenting offences linked to legal cases.

## Field Set Overview

The **Offence Fields** include attributes such as the offence code, category, title, and related legal information, providing a complete record of offences associated with cases.

### Core Fields

These are the essential fields required for documenting offences:

| Field Name                | Type      | Description                                                                 | Example                     |
|--------------------------|-----------|-----------------------------------------------------------------------------|-----------------------------|
| `offence.id`             | `keyword` | A unique identifier for each offence record.                                | `OFF12345`                  |
| `offence.case_id`        | `array`   | An array of unique identifiers for the cases associated with the offence.   | `["CASE12345", "CASE67890"]`|
| `offence.code`           | `keyword` | The official code representing the offence as per the criminal justice standards. | `CJS001`                   |
| `offence.category`       | `keyword` | The category of the offence (e.g., theft, assault, fraud).                  | `theft`                     |
| `offence.title`          | `text`    | The title or name of the offence.                                           | `Shoplifting`               |
| `offence.date`           | `date`    | The date when the offence occurred.                                         | `2023-08-10`                |
| `offence.description`    | `text`    | A detailed description of the offence.                                      | `Shoplifting incident at a retail store.` |

### Extended Fields

These fields provide additional details and context for offences:

| Field Name                | Type      | Description                                                                 | Example                     |
|--------------------------|-----------|-----------------------------------------------------------------------------|-----------------------------|
| `offence.legislation`    | `text`    | The legislation under which the offence is charged.                         | `Theft Act 1968`            |
| `offence.welsh_title`    | `text`    | The Welsh title of the offence, if applicable.                              | `Ladrata Siopa`             |
| `offence.penalty`        | `text`    | The potential penalty for the offence.                                      | `Up to 6 months imprisonment or a fine` |
| `offence.related_materials` | `array`   | A list of material IDs related to the offence, such as evidence files or reports. | `["MAT123", "MAT456"]`      |
| `offence.notes`          | `text`    | Additional notes or remarks about the offence.                              | `Offender has previous convictions for similar offences.` |

### Field Details

#### 1. `offence.id`
- **Type**: `keyword`
- **Description**: A unique identifier for each offence record.
- **Example**: `OFF12345`

#### 2. `offence.case_id`
- **Type**: `array`
- **Description**: An array of unique identifiers representing the cases linked to the offence, allowing tracking across multiple cases.
- **Example**: `["CASE12345", "CASE67890"]`

#### 3. `offence.code`
- **Type**: `keyword`
- **Description**: The official code representing the offence as per the criminal justice standards.
- **Example**: `CJS001`

#### 4. `offence.category`
- **Type**: `keyword`
- **Description**: The category of the offence (e.g., theft, assault, fraud).
- **Example**: `theft`

#### 5. `offence.title`
- **Type**: `text`
- **Description**: The title or name of the offence.
- **Example**: `Shoplifting`

#### 6. `offence.date`
- **Type**: `date`
- **Description**: The date when the offence occurred.
- **Example**: `2023-08-10`

#### 7. `offence.description`
- **Type**: `text`
- **Description**: A detailed description of the offence.
- **Example**: `Shoplifting incident at a retail store.`

#### 8. `offence.legislation`
- **Type**: `text`
- **Description**: The legislation under which the offence is charged.
- **Example**: `Theft Act 1968`

#### 9. `offence.welsh_title`
- **Type**: `text`
- **Description**: The Welsh title of the offence, if applicable.
- **Example**: `Ladrata Siopa`

#### 10. `offence.penalty`
- **Type**: `text`
- **Description**: The potential penalty for the offence.
- **Example**: `Up to 6 months imprisonment or a fine`

#### 11. `offence.related_materials`
- **Type**: `array`
- **Description**: A list of material IDs related to the offence, such as evidence files or reports.
- **Example**: `["MAT123", "MAT456"]`

#### 12. `offence.notes`
- **Type**: `text`
- **Description**: Additional notes or remarks about the offence.
- **Example**: `Offender has previous convictions for similar offences.`

### Usage Notes

- **Core Fields**: These fields must be present for each offence record to ensure accurate tracking and documentation within the case timeline.
- **Extended Fields**: Additional fields can be used when further details are available or necessary for the offence context.

### Example Document

#### YAML

```yaml
offence:
  id: OFF12345
  case_id: ["CASE12345", "CASE67890"]
  code: CJS001
  category: theft
  title: Shoplifting
  date: 2023-08-10
  description: Shoplifting incident at a retail store.
  legislation: Theft Act 1968
  welsh_title: Ladrata Siopa
  penalty: Up to 6 months imprisonment or a fine
  related_materials: ["MAT123", "MAT456"]
  notes: Offender has previous convictions for similar offences.
```

#### JSON

```json
{
  "offence": {
    "id": "OFF12345",
    "case_id": ["CASE12345", "CASE67890"],
    "code": "CJS001",
    "category": "theft",
    "title": "Shoplifting",
    "date": "2023-08-10",
    "description": "Shoplifting incident at a retail store.",
    "legislation": "Theft Act 1968",
    "welsh_title": "Ladrata Siopa",
    "penalty": "Up to 6 months imprisonment or a fine",
    "related_materials": ["MAT123", "MAT456"],
    "notes": "Offender has previous convictions for similar offences."
  }
}
```