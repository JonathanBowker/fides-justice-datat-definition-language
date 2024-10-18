# Evidence Fields

The **Evidence Fields** section of the Judicial Electronic Data Interchange Language (JEDI) documents information about evidence collected, managed, and presented in cases. This includes details on the type, collection method, and chain of custody, ensuring proper documentation and tracking throughout the legal process.

## Field Set Overview

The **Evidence Fields** capture attributes such as the type of evidence, collection dates, and information about the chain of custody to maintain the integrity and authenticity of evidence.

### Core Fields

These are the essential fields required for documenting evidence:

| Field Name                    | Type      | Description                                                                 | Example                     |
|------------------------------|-----------|-----------------------------------------------------------------------------|-----------------------------|
| `evidence.id`                | `keyword` | A unique identifier for each piece of evidence.                             | `EVID12345`                 |
| `evidence.case_id`           | `array`   | An array of unique identifiers for the cases associated with the evidence.  | `["CASE12345", "CASE67890"]`|
| `evidence.type`              | `keyword` | The type of evidence (e.g., physical, digital, testimonial).                | `physical`                  |
| `evidence.description`       | `text`    | A detailed description of the evidence.                                     | `Fingerprint sample from crime scene` |
| `evidence.collection_date`   | `date`    | The date when the evidence was collected.                                   | `2023-05-15`                |
| `evidence.collected_by`      | `text`    | The name or identifier of the person or officer who collected the evidence. | `Officer Jane Smith`        |

### Extended Fields

Additional fields may be included to provide further context and details:

| Field Name                    | Type      | Description                                                                 | Example                     |
|------------------------------|-----------|-----------------------------------------------------------------------------|-----------------------------|
| `evidence.location`          | `text`    | The location where the evidence was collected.                              | `123 Elm Street, Anytown`   |
| `evidence.chain_of_custody`  | `array`   | Records of each person or entity that handled the evidence and the dates.   | `[{"handler": "Officer Smith", "date": "2023-05-15"}, {"handler": "Lab Technician", "date": "2023-05-16"}]` |
| `evidence.status`            | `keyword` | The current status of the evidence (e.g., in storage, submitted to court).  | `in storage`                |
| `evidence.storage_location`  | `text`    | The location where the evidence is currently stored.                        | `Evidence Locker 5`         |
| `evidence.related_documents` | `array`   | A list of document IDs related to the evidence, such as reports or receipts. | `["DOC123", "DOC456"]`      |

### Field Details

#### 1. `evidence.id`
- **Type**: `keyword`
- **Description**: A unique identifier for each piece of evidence.
- **Example**: `EVID12345`

#### 2. `evidence.case_id`
- **Type**: `array`
- **Description**: An array of unique identifiers representing the cases linked to the evidence, allowing tracking across multiple cases.
- **Example**: `["CASE12345", "CASE67890"]`

#### 3. `evidence.type`
- **Type**: `keyword`
- **Description**: The type of evidence (e.g., physical, digital, testimonial).
- **Example**: `physical`

#### 4. `evidence.description`
- **Type**: `text`
- **Description**: A detailed description of the evidence.
- **Example**: `Fingerprint sample from crime scene`

#### 5. `evidence.collection_date`
- **Type**: `date`
- **Description**: The date when the evidence was collected.
- **Example**: `2023-05-15`

#### 6. `evidence.collected_by`
- **Type**: `text`
- **Description**: The name or identifier of the person or officer who collected the evidence.
- **Example**: `Officer Jane Smith`

#### 7. `evidence.location`
- **Type**: `text`
- **Description**: The location where the evidence was collected.
- **Example**: `123 Elm Street, Anytown`

#### 8. `evidence.chain_of_custody`
- **Type**: `array`
- **Description**: A list documenting each handler of the evidence and the date it was in their possession, ensuring the integrity of the chain of custody.
- **Example**: `[{"handler": "Officer Smith", "date": "2023-05-15"}, {"handler": "Lab Technician", "date": "2023-05-16"}]`

#### 9. `evidence.status`
- **Type**: `keyword`
- **Description**: The current status of the evidence (e.g., in storage, submitted to court).
- **Example**: `in storage`

#### 10. `evidence.storage_location`
- **Type**: `text`
- **Description**: The location where the evidence is currently stored.
- **Example**: `Evidence Locker 5`

#### 11. `evidence.related_documents`
- **Type**: `array`
- **Description**: A list of document IDs that relate to the evidence, such as lab reports or chain of custody logs.
- **Example**: `["DOC123", "DOC456"]`

### Usage Notes

- **Core Fields**: These fields must be present for each piece of evidence to ensure proper tracking and documentation.
- **Extended Fields**: Additional fields can be included as necessary to provide more context, such as storage location and chain of custody details.

### Example Document

#### YAML

```yaml
evidence:
  id: EVID12345
  case_id: ["CASE12345", "CASE67890"]
  type: physical
  description: Fingerprint sample from crime scene
  collection_date: 2023-05-15
  collected_by: Officer Jane Smith
  location: 123 Elm Street, Anytown
  chain_of_custody:
    - handler: Officer Smith
      date: 2023-05-15
    - handler: Lab Technician
      date: 2023-05-16
  status: in storage
  storage_location: Evidence Locker 5
  related_documents: ["DOC123", "DOC456"]
```

#### JSON

```json
{
  "evidence": {
    "id": "EVID12345",
    "case_id": ["CASE12345", "CASE67890"],
    "type": "physical",
    "description": "Fingerprint sample from crime scene",
    "collection_date": "2023-05-15",
    "collected_by": "Officer Jane Smith",
    "location": "123 Elm Street, Anytown",
    "chain_of_custody": [
      {"handler": "Officer Smith", "date": "2023-05-15"},
      {"handler": "Lab Technician", "date": "2023-05-16"}
    ],
    "status": "in storage",
    "storage_location": "Evidence Locker 5",
    "related_documents": ["DOC123", "DOC456"]
  }
}
```

This markdown file (`evidence.md`) provides a comprehensive overview of the **Evidence Fields** in the Judicial Electronic Data Interchange Language, ensuring proper documentation and tracking of evidence throughout the justice process.
