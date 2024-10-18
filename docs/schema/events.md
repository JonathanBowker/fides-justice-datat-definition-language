# Events Fields

The **Events Fields** section of the Judicial Electronic Data Interchange Language (JEDI) captures information about key occurrences or actions within the lifecycle of a legal case. This includes details about hearings, arrests, evidence collection, motions, and other significant activities. These fields ensure comprehensive documentation and tracking of events as they unfold in the justice system.

## Field Set Overview

The **Events Fields** encompass attributes such as event type, date, location, and involved participants, providing a detailed timeline of events within each case.

### Core Fields

These are the essential fields required for documenting events:

| Field Name                    | Type      | Description                                                                 | Example                     |
|------------------------------|-----------|-----------------------------------------------------------------------------|-----------------------------|
| `event.id`                   | `keyword` | A unique identifier for each event record.                                  | `EVT12345`                  |
| `event.case_id`              | `array`   | An array of unique identifiers for the cases associated with the event.     | `["CASE12345", "CASE67890"]`|
| `event.type`                 | `keyword` | The type of event (e.g., hearing, arrest, evidence collection).             | `hearing`                   |
| `event.date`                 | `date`    | The date when the event took place.                                         | `2023-07-15`                |
| `event.location`             | `text`    | The location where the event occurred.                                      | `Courtroom 5, Anytown District Court` |
| `event.description`          | `text`    | A detailed description of the event.                                        | `Preliminary hearing for defendant.` |

### Extended Fields

These fields provide additional information and context for events:

| Field Name                    | Type      | Description                                                                 | Example                     |
|------------------------------|-----------|-----------------------------------------------------------------------------|-----------------------------|
| `event.participant_ids`      | `array`   | An array of unique identifiers for the participants involved in the event.  | `["PART123", "PART456"]`    |
| `event.status`               | `keyword` | The current status of the event (e.g., scheduled, completed, postponed).    | `completed`                 |
| `event.related_documents`    | `array`   | A list of document IDs related to the event, such as motions or orders.     | `["DOC123", "DOC456"]`      |
| `event.notes`                | `text`    | Additional notes or remarks about the event.                                | `Judge postponed hearing due to absence of counsel.` |

### Field Details

#### 1. `event.id`
- **Type**: `keyword`
- **Description**: A unique identifier for each event record.
- **Example**: `EVT12345`

#### 2. `event.case_id`
- **Type**: `array`
- **Description**: An array of unique identifiers representing the cases linked to the event, allowing tracking across multiple cases.
- **Example**: `["CASE12345", "CASE67890"]`

#### 3. `event.type`
- **Type**: `keyword`
- **Description**: The type of event (e.g., hearing, arrest, evidence collection).
- **Example**: `hearing`

#### 4. `event.date`
- **Type**: `date`
- **Description**: The date when the event took place.
- **Example**: `2023-07-15`

#### 5. `event.location`
- **Type**: `text`
- **Description**: The location where the event occurred.
- **Example**: `Courtroom 5, Anytown District Court`

#### 6. `event.description`
- **Type**: `text`
- **Description**: A detailed description of the event.
- **Example**: `Preliminary hearing for defendant.`

#### 7. `event.participant_ids`
- **Type**: `array`
- **Description**: An array of unique identifiers for the participants involved in the event.
- **Example**: `["PART123", "PART456"]`

#### 8. `event.status`
- **Type**: `keyword`
- **Description**: The current status of the event (e.g., scheduled, completed, postponed).
- **Example**: `completed`

#### 9. `event.related_documents`
- **Type**: `array`
- **Description**: A list of document IDs related to the event, such as motions or court orders.
- **Example**: `["DOC123", "DOC456"]`

#### 10. `event.notes`
- **Type**: `text`
- **Description**: Additional notes or remarks about the event.
- **Example**: `Judge postponed hearing due to absence of counsel.`

### Usage Notes

- **Core Fields**: These fields must be present for each event to ensure accurate tracking and documentation within the case timeline.
- **Extended Fields**: Additional fields can be used when further details are available or necessary for the context of the event.

### Example Document

#### YAML

```yaml
event:
  id: EVT12345
  case_id: ["CASE12345", "CASE67890"]
  type: hearing
  date: 2023-07-15
  location: Courtroom 5, Anytown District Court
  description: Preliminary hearing for defendant.
  participant_ids: ["PART123", "PART456"]
  status: completed
  related_documents: ["DOC123", "DOC456"]
  notes: Judge postponed hearing due to absence of counsel.
```

#### JSON

```json
{
  "event": {
    "id": "EVT12345",
    "case_id": ["CASE12345", "CASE67890"],
    "type": "hearing",
    "date": "2023-07-15",
    "location": "Courtroom 5, Anytown District Court",
    "description": "Preliminary hearing for defendant.",
    "participant_ids": ["PART123", "PART456"],
    "status": "completed",
    "related_documents": ["DOC123", "DOC456"],
    "notes": "Judge postponed hearing due to absence of counsel."
  }
}
```

This markdown file (`events.md`) provides a comprehensive overview of the **Events Fields** in the Judicial Electronic Data Interchange Language, ensuring proper documentation and tracking of key events associated with legal cases.