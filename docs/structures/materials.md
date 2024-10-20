# Materials Fields

The **Materials Fields** section of the Justice Information Exchange (JIX) language captures information about materials related to legal cases. This includes documents, evidence files, reports, and any other physical or digital records pertinent to a case. These fields ensure comprehensive documentation and tracking of all materials associated with legal proceedings within the justice system.

## Field Set Overview

The **Materials Fields** include attributes such as material ID, type, source, and associated case information, providing a complete record of all materials linked to cases.

### Core Fields

These are the essential fields required for documenting materials:

| Field Name                | Type      | Description                                                                 | Example                     |
|--------------------------|-----------|-----------------------------------------------------------------------------|-----------------------------|
| `materials.id`           | `keyword` | A unique identifier for each material record.                               | `MAT12345`                  |
| `materials.case_id`      | `array`   | An array of unique identifiers for the cases associated with the material.  | `["CASE12345", "CASE67890"]`|
| `materials.type`         | `keyword` | The type of material (e.g., evidence file, report, transcript).             | `evidence file`             |
| `materials.source`       | `text`    | The origin or source of the material (e.g., police report, forensic lab).   | `Anytown Police Department` |
| `materials.date`         | `date`    | The date when the material was created or collected.                        | `2023-08-10`                |
| `materials.description`  | `text`    | A detailed description of the material.                                     | `Forensic analysis report for the crime scene.`               |

### Extended Fields

These fields provide additional details and context for materials:

| Field Name                | Type      | Description                                                                 | Example                     |
|--------------------------|-----------|-----------------------------------------------------------------------------|-----------------------------|
| `materials.file_type`    | `keyword` | The format or file type of the material (e.g., PDF, JPEG).                  | `PDF`                       |
| `materials.related_personnel` | `array`   | A list of IDs for personnel associated with the material, such as officers or forensic experts. | `["PERSON123", "PERSON456"]`|
| `materials.confidentiality` | `keyword` | The confidentiality level of the material (e.g., restricted, public).       | `restricted`                |
| `materials.related_events` | `array`   | A list of event IDs related to the material.                                | `["EVT123", "EVT456"]`      |
| `materials.notes`        | `text`    | Additional notes or remarks about the material.                             | `Material requires further analysis.` |

### Field Details

#### 1. `materials.id`
- **Type**: `keyword`
- **Description**: A unique identifier for each material record.
- **Example**: `MAT12345`

#### 2. `materials.case_id`
- **Type**: `array`
- **Description**: An array of unique identifiers representing the cases linked to the material, allowing tracking across multiple cases.
- **Example**: `["CASE12345", "CASE67890"]`

#### 3. `materials.type`
- **Type**: `keyword`
- **Description**: The type of material (e.g., evidence file, report, transcript).
- **Example**: `evidence file`

#### 4. `materials.source`
- **Type**: `text`
- **Description**: The origin or source of the material (e.g., police report, forensic lab).
- **Example**: `Anytown Police Department`

#### 5. `materials.date`
- **Type**: `date`
- **Description**: The date when the material was created or collected.
- **Example**: `2023-08-10`

#### 6. `materials.description`
- **Type**: `text`
- **Description**: A detailed description of the material.
- **Example**: `Forensic analysis report for the crime scene.`

#### 7. `materials.file_type`
- **Type**: `keyword`
- **Description**: The format or file type of the material (e.g., PDF, JPEG).
- **Example**: `PDF`

#### 8. `materials.related_personnel`
- **Type**: `array`
- **Description**: A list of IDs for personnel associated with the material, such as officers or forensic experts.
- **Example**: `["PERSON123", "PERSON456"]`

#### 9. `materials.confidentiality`
- **Type**: `keyword`
- **Description**: The confidentiality level of the material (e.g., restricted, public).
- **Example**: `restricted`

#### 10. `materials.related_events`
- **Type**: `array`
- **Description**: A list of event IDs related to the material.
- **Example**: `["EVT123", "EVT456"]`

#### 11. `materials.notes`
- **Type**: `text`
- **Description**: Additional notes or remarks about the material.
- **Example**: `Material requires further analysis.`

### Usage Notes

- **Core Fields**: These fields must be present for each material record to ensure accurate tracking and documentation within the case timeline.
- **Extended Fields**: Additional fields can be used when further details are available or necessary for the material context.

### Example Document

#### YAML

```yaml
materials:
  id: MAT12345
  case_id: ["CASE12345", "CASE67890"]
  type: evidence file
  source: Anytown Police Department
  date: 2023-08-10
  description: Forensic analysis report for the crime scene.
  file_type: PDF
  related_personnel: ["PERSON123", "PERSON456"]
  confidentiality: restricted
  related_events: ["EVT123", "EVT456"]
  notes: Material requires further analysis.
```

#### JSON

```json
{
  "materials": {
    "id": "MAT12345",
    "case_id": ["CASE12345", "CASE67890"],
    "type": "evidence file",
    "source": "Anytown Police Department",
    "date": "2023-08-10",
    "description": "Forensic analysis report for the crime scene.",
    "file_type": "PDF",
    "related_personnel": ["PERSON123", "PERSON456"],
    "confidentiality": "restricted",
    "related_events": ["EVT123", "EVT456"],
    "notes": "Material requires further analysis."
  }
}
```
