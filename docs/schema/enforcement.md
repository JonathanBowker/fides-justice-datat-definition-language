# Enforcement Fields

The **Enforcement Fields** section of the Judicial Electronic Data Interchange Language (JEDI) captures information about law enforcement actions and activities related to legal cases. This includes details on arrests, investigations, and other enforcement activities carried out by law enforcement officers. These fields ensure comprehensive documentation and tracking of enforcement activities within the justice system.

## Field Set Overview

The **Enforcement Fields** include attributes such as enforcement type, officer details, date, and location, providing a detailed record of enforcement actions linked to cases.

### Core Fields

These are the essential fields required for documenting enforcement activities:

| Field Name                    | Type      | Description                                                                 | Example                     |
|------------------------------|-----------|-----------------------------------------------------------------------------|-----------------------------|
| `enforcement.id`             | `keyword` | A unique identifier for each enforcement record.                            | `ENF12345`                  |
| `enforcement.case_id`        | `array`   | An array of unique identifiers for the cases associated with the enforcement action. | `["CASE12345", "CASE67890"]` |
| `enforcement.type`           | `keyword` | The type of enforcement action (e.g., arrest, investigation, search warrant). | `arrest`                    |
| `enforcement.date`           | `date`    | The date when the enforcement action took place.                            | `2023-08-10`                |
| `enforcement.location`       | `text`    | The location where the enforcement action occurred.                         | `123 Main Street, Anytown`  |
| `enforcement.description`    | `text`    | A detailed description of the enforcement action.                           | `Arrest of suspect at residence.` |

### Extended Fields

These fields provide additional details and context for enforcement activities:

| Field Name                    | Type      | Description                                                                 | Example                     |
|------------------------------|-----------|-----------------------------------------------------------------------------|-----------------------------|
| `enforcement.officer_id`     | `keyword` | The unique identifier for the officer involved in the enforcement action.   | `OFFICER123`                |
| `enforcement.agency`         | `text`    | The name of the law enforcement agency responsible for the action.          | `Anytown Police Department` |
| `enforcement.status`         | `keyword` | The current status of the enforcement action (e.g., completed, ongoing).    | `completed`                 |
| `enforcement.related_documents` | `array`   | A list of document IDs related to the enforcement action, such as reports or warrants. | `["DOC123", "DOC456"]`      |
| `enforcement.notes`          | `text`    | Additional notes or remarks about the enforcement action.                   | `Suspect cooperated during arrest.` |

### Field Details

#### 1. `enforcement.id`
- **Type**: `keyword`
- **Description**: A unique identifier for each enforcement record.
- **Example**: `ENF12345`

#### 2. `enforcement.case_id`
- **Type**: `array`
- **Description**: An array of unique identifiers representing the cases linked to the enforcement action, allowing tracking across multiple cases.
- **Example**: `["CASE12345", "CASE67890"]`

#### 3. `enforcement.type`
- **Type**: `keyword`
- **Description**: The type of enforcement action (e.g., arrest, investigation, search warrant).
- **Example**: `arrest`

#### 4. `enforcement.date`
- **Type**: `date`
- **Description**: The date when the enforcement action took place.
- **Example**: `2023-08-10`

#### 5. `enforcement.location`
- **Type**: `text`
- **Description**: The location where the enforcement action occurred.
- **Example**: `123 Main Street, Anytown`

#### 6. `enforcement.description`
- **Type**: `text`
- **Description**: A detailed description of the enforcement action.
- **Example**: `Arrest of suspect at residence.`

#### 7. `enforcement.officer_id`
- **Type**: `keyword`
- **Description**: The unique identifier for the officer involved in the enforcement action.
- **Example**: `OFFICER123`

#### 8. `enforcement.agency`
- **Type**: `text`
- **Description**: The name of the law enforcement agency responsible for the action.
- **Example**: `Anytown Police Department`

#### 9. `enforcement.status`
- **Type**: `keyword`
- **Description**: The current status of the enforcement action (e.g., completed, ongoing).
- **Example**: `completed`

#### 10. `enforcement.related_documents`
- **Type**: `array`
- **Description**: A list of document IDs related to the enforcement action, such as reports or court documents.
- **Example**: `["DOC123", "DOC456"]`

#### 11. `enforcement.notes`
- **Type**: `text`
- **Description**: Additional notes or remarks about the enforcement action.
- **Example**: `Suspect cooperated during arrest.`

### Usage Notes

- **Core Fields**: These fields must be present for each enforcement action to ensure accurate tracking and documentation within the case timeline.
- **Extended Fields**: Additional fields can be used when further details are available or necessary for the enforcement context.

### Example Document

#### YAML

```yaml
enforcement:
  id: ENF12345
  case_id: ["CASE12345", "CASE67890"]
  type: arrest
  date: 2023-08-10
  location: 123 Main Street, Anytown
  description: Arrest of suspect at residence.
  officer_id: OFFICER123
  agency: Anytown Police Department
  status: completed
  related_documents: ["DOC123", "DOC456"]
  notes: Suspect cooperated during arrest.
```

#### JSON

```json
{
  "enforcement": {
    "id": "ENF12345",
    "case_id": ["CASE12345", "CASE67890"],
    "type": "arrest",
    "date": "2023-08-10",
    "location": "123 Main Street, Anytown",
    "description": "Arrest of suspect at residence.",
    "officer_id": "OFFICER123",
    "agency": "Anytown Police Department",
    "status": "completed",
    "related_documents": ["DOC123", "DOC456"],
    "notes": "Suspect cooperated during arrest."
  }
}
```

This markdown file (`enforcement.md`) provides a comprehensive overview of the **Enforcement Fields** in the Judicial Electronic Data Interchange Language, ensuring proper documentation and tracking of law enforcement activities linked to legal cases.