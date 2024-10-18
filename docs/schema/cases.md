# Case Fields

The **Case Fields** section of the Judicial Electronic Data Interchange Language (JEDI) captures information about legal cases, including details about case status, type, parties involved, and important dates. The **ID** field is essential for uniquely identifying each case and linking it with other entities like participants, offenses, and judicial procedures. This comprehensive documentation allows for effective management and tracking of cases throughout their lifecycle within the justice system.

## Field Set Overview

The **Cases Fields** include attributes such as case ID, status, type, involved parties, and key dates, providing a complete record of each case and its progression.

### Core Fields

These are the essential fields required for documenting cases:

| Field Name                    | Type      | Description                                                                 | Example                     |
|------------------------------|-----------|-----------------------------------------------------------------------------|-----------------------------|
| `case.id`                    | `keyword` | A unique identifier for each case record. This ID links the case with other entities in the system. | `CASE12345`                 |
| `case.status`                | `keyword` | The current status of the case (e.g., open, closed, pending).               | `open`                      |
| `case.type`                  | `keyword` | The type of case (e.g., criminal, civil, family).                           | `criminal`                  |
| `case.start_date`            | `date`    | The date when the case was initiated.                                       | `2023-01-10`                |
| `case.end_date`              | `date`    | The date when the case was closed (if applicable).                          | `2023-06-15`                |
| `case.description`           | `text`    | A brief description of the case.                                            | `Robbery at commercial property.` |

### Extended Fields

These fields provide additional details and context for cases and link to other entities:

| Field Name                    | Type      | Description                                                                 | Example                     |
|------------------------------|-----------|-----------------------------------------------------------------------------|-----------------------------|
| `case.participant_ids`       | `array`   | An array of unique identifiers for the participants involved in the case.   | `["PART123", "PART456"]`    |
| `case.victim_support_ids`    | `array`   | An array of unique identifiers for the victim support services associated with the case. | `["SUPPORT123", "SUPPORT456"]` |
| `case.evidence_ids`          | `array`   | An array of unique identifiers for the evidence associated with the case.   | `["EVID123", "EVID456"]`    |
| `case.probation_parole_ids`  | `array`   | An array of unique identifiers for probation or parole records linked to the case. | `["PP123", "PP456"]`        |
| `case.offense_ids`           | `array`   | An array of unique identifiers for the offenses associated with the case.   | `["OFF123", "OFF456"]`      |
| `case.sentence_ids`          | `array`   | An array of unique identifiers for the sentences associated with the case.  | `["SENT123", "SENT456"]`    |
| `case.event_ids`             | `array`   | An array of unique identifiers for events related to the case.              | `["EVT123", "EVT456"]`      |
| `case.enforcement_ids`       | `array`   | An array of unique identifiers for enforcement actions linked to the case.  | `["ENF123", "ENF456"]`      |
| `case.judicial_procedure_ids`| `array`   | An array of unique identifiers for judicial procedures associated with the case. | `["JP123", "JP456"]`        |
| `case.bail_detention_ids`    | `array`   | An array of unique identifiers for bail or detention records linked to the case. | `["BD123", "BD456"]`        |
| `case.judge_ids`             | `array`   | An array of unique identifiers for the judges presiding over the case.      | `["JUDGE123", "JUDGE456"]`  |
| `case.location`              | `text`    | The location or court where the case is being processed.                    | `Anytown District Court`    |
| `case.related_documents`     | `array`   | A list of document IDs related to the case, such as motions or rulings.     | `["DOC123", "DOC456"]`      |
| `case.notes`                 | `text`    | Additional notes or remarks about the case.                                 | `Case postponed due to unavailability of key witness.` |

### Field Details

#### 1. `case.id`
- **Type**: `keyword`
- **Description**: A unique identifier for each case record. This ID is critical for linking the case to other entities like participants, victim support, evidence, and events.
- **Example**: `CASE12345`

#### 2. `case.status`
- **Type**: `keyword`
- **Description**: The current status of the case (e.g., open, closed, pending).
- **Example**: `open`

#### 3. `case.type`
- **Type**: `keyword`
- **Description**: The type of case, such as criminal, civil, or family.
- **Example**: `criminal`

#### 4. `case.start_date`
- **Type**: `date`
- **Description**: The date when the case was initiated.
- **Example**: `2023-01-10`

#### 5. `case.end_date`
- **Type**: `date`
- **Description**: The date when the case was closed, if applicable.
- **Example**: `2023-06-15`

#### 6. `case.description`
- **Type**: `text`
- **Description**: A brief description of the case.
- **Example**: `Robbery at commercial property.`

#### 7. `case.participant_ids`
- **Type**: `array`
- **Description**: An array of unique identifiers for the participants involved in the case.
- **Example**: `["PART123", "PART456"]`

#### 8. `case.victim_support_ids`
- **Type**: `array`
- **Description**: An array of unique identifiers for the victim support services associated with the case.
- **Example**: `["SUPPORT123", "SUPPORT456"]`

#### 9. `case.evidence_ids`
- **Type**: `array`
- **Description**: An array of unique identifiers for the evidence related to the case.
- **Example**: `["EVID123", "EVID456"]`

#### 10. `case.probation_parole_ids`
- **Type**: `array`
- **Description**: An array of unique identifiers for probation or parole records linked to the case.
- **Example**: `["PP123", "PP456"]`

#### 11. `case.offense_ids`
- **Type**: `array`
- **Description**: An array of unique identifiers for the offenses associated with the case.
- **Example**: `["OFF123", "OFF456"]`

#### 12. `case.sentence_ids`
- **Type**: `array`
- **Description**: An array of unique identifiers for the sentences associated with the case.
- **Example**: `["SENT123", "SENT456"]`

#### 13. `case.event_ids`
- **Type**: `array`
- **Description**: An array of unique identifiers for events related to the case.
- **Example**: `["EVT123", "EVT456"]`

#### 14. `case.enforcement_ids`
- **Type**: `array`
- **Description**: An array of unique identifiers for enforcement actions linked to the case.
- **Example**: `["ENF123", "ENF456"]`

#### 15. `case.judicial_procedure_ids`
- **Type**: `array`
- **Description**: An array of unique identifiers for judicial procedures associated with the case.
- **Example**: `["JP123", "JP456"]`

#### 16. `case.bail_detention_ids`
- **Type**: `array`
- **Description**: An array of unique identifiers for bail or detention records linked to the case.
- **Example**: `["BD123", "BD456"]`

#### 17. `case.judge_ids`
- **Type**: `array`
- **Description**: An array of unique identifiers for the judges presiding over the case.
- **Example**: `["JUDGE123", "JUDGE456"]`

### Usage Notes

- **Core Fields**: These fields must be present for each case to ensure accurate tracking and documentation within the case management system.
- **Extended Fields**: Additional fields can be used when further details are available or necessary for the context of the case.

### Example Document

#### YAML

```yaml
case:
  id: CASE12345
  status: open
  type: criminal
  start_date: 2023-01-10
  end_date: 

2023-06-15
  description: Robbery at commercial property.
  participant_ids: ["PART123", "PART456"]
  victim_support_ids: ["SUPPORT123", "SUPPORT456"]
  evidence_ids: ["EVID123", "EVID456"]
  probation_parole_ids: ["PP123", "PP456"]
  offense_ids: ["OFF123", "OFF456"]
  sentence_ids: ["SENT123", "SENT456"]
  event_ids: ["EVT123", "EVT456"]
  enforcement_ids: ["ENF123", "ENF456"]
  judicial_procedure_ids: ["JP123", "JP456"]
  bail_detention_ids: ["BD123", "BD456"]
  judge_ids: ["JUDGE123", "JUDGE456"]
  location: Anytown District Court
  related_documents: ["DOC123", "DOC456"]
  notes: Case postponed due to unavailability of key witness.
```

#### JSON

```json
{
  "case": {
    "id": "CASE12345",
    "status": "open",
    "type": "criminal",
    "start_date": "2023-01-10",
    "end_date": "2023-06-15",
    "description": "Robbery at commercial property.",
    "participant_ids": ["PART123", "PART456"],
    "victim_support_ids": ["SUPPORT123", "SUPPORT456"],
    "evidence_ids": ["EVID123", "EVID456"],
    "probation_parole_ids": ["PP123", "PP456"],
    "offense_ids": ["OFF123", "OFF456"],
    "sentence_ids": ["SENT123", "SENT456"],
    "event_ids": ["EVT123", "EVT456"],
    "enforcement_ids": ["ENF123", "ENF456"],
    "judicial_procedure_ids": ["JP123", "JP456"],
    "bail_detention_ids": ["BD123", "BD456"],
    "judge_ids": ["JUDGE123", "JUDGE456"],
    "location": "Anytown District Court",
    "related_documents": ["DOC123", "DOC456"],
    "notes": "Case postponed due to unavailability of key witness."
  }
}
```

This markdown file (`cases.md`) now comprehensively includes the **judge_ids** field as an array, reflecting that multiple judges may be involved in a single case and ensuring proper documentation of all associated elements within the justice system.