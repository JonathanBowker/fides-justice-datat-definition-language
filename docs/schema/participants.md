# Participant Fields

The **Participant Fields** section of the Judicial Electronic Data Interchange Language (JEDI) captures essential information about individuals and entities involved in cases, such as defendants, victims, legal professionals, and witnesses. These fields ensure accurate management, documentation, and tracking of participants within the justice system.

## Field Set Overview

The **Participant Fields** encompass attributes such as role, name, affiliation, and other demographic information, ensuring comprehensive documentation and accessibility.

### Core Fields

These are the mandatory fields required for all participants:

| Field Name                    | Type      | Description                                                                 | Example                     |
|------------------------------|-----------|-----------------------------------------------------------------------------|-----------------------------|
| `participant.id`             | `keyword` | A unique identifier for each participant.                                   | `PART12345`                 |
| `participant.case_id`        | `array`   | An array of unique identifiers for the cases that the participant is associated with. | `["CASE67890", "CASE12345"]` |
| `participant.role`           | `keyword` | The role of the participant in the case (e.g., defendant, judge, lawyer).   | `defendant`                 |
| `participant.name`           | `text`    | The full name of the participant.                                           | `John Doe`                  |
| `participant.affiliation`    | `text`    | The organisation or entity the participant is associated with.              | `Public Defender's Office`  |
| `participant.contact_info`   | `text`    | Contact details for the participant, such as phone number or email.         | `johndoe@example.com`       |

### Extended Fields

These fields provide additional details and context about participants:

| Field Name                    | Type      | Description                                                                 | Example                     |
|------------------------------|-----------|-----------------------------------------------------------------------------|-----------------------------|
| `participant.date_of_birth`  | `date`    | The participant’s date of birth.                                            | `1985-06-15`                |
| `participant.gender`         | `keyword` | The gender of the participant (e.g., male, female, non-binary).             | `female`                    |
| `participant.ethnicity`      | `keyword` | The ethnic background of the participant.                                   | `Hispanic`                  |
| `participant.address`        | `text`    | The residential address of the participant.                                 | `123 Elm Street, Anytown`   |
| `participant.legal_representation` | `text` | Information about the participant’s legal representation, including lawyer names or firms. | `Public Defender's Office`  |
| `participant.status`         | `keyword` | Current status of the participant in the case (e.g., in custody, on bail).  | `in custody`                |
| `participant.demographics`   | `object`  | A structured object containing multiple demographic attributes such as age, disability status, etc. | `{ "age": 35, "disability_status": "none" }` |

### Field Details

#### 1. `participant.id`
- **Type**: `keyword`
- **Description**: A unique identifier for each participant, ensuring they are distinguishable within the case records.
- **Example**: `PART12345`

#### 2. `participant.case_id`
- **Type**: `array`
- **Description**: An array of unique identifiers representing the cases that the participant is associated with, allowing the tracking of multiple cases per participant.
- **Example**: `["CASE67890", "CASE12345"]`

#### 3. `participant.role`
- **Type**: `keyword`
- **Description**: Defines the role the participant plays in the case, such as defendant, victim, judge, lawyer, or witness.
- **Example**: `defendant`

#### 4. `participant.name`
- **Type**: `text`
- **Description**: The full legal name of the participant.
- **Example**: `John Doe`

#### 5. `participant.affiliation`
- **Type**: `text`
- **Description**: The organisation or legal entity associated with the participant, such as a law firm, public defender's office, or court.
- **Example**: `Public Defender's Office`

#### 6. `participant.contact_info`
- **Type**: `text`
- **Description**: Contact information for the participant, which may include an email address, phone number, or other relevant details.
- **Example**: `johndoe@example.com`

#### 7. `participant.date_of_birth`
- **Type**: `date`
- **Description**: The participant's date of birth.
- **Example**: `1985-06-15`

#### 8. `participant.gender`
- **Type**: `keyword`
- **Description**: The gender of the participant.
- **Example**: `female`

#### 9. `participant.ethnicity`
- **Type**: `keyword`
- **Description**: The participant's ethnic background.
- **Example**: `Hispanic`

#### 10. `participant.address`
- **Type**: `text`
- **Description**: The participant's residential address.
- **Example**: `123 Elm Street, Anytown`

#### 11. `participant.legal_representation`
- **Type**: `text`
- **Description**: Information about the participant's legal representation (e.g., lawyer’s name, firm).
- **Example**: `Public Defender's Office`

#### 12. `participant.status`
- **Type**: `keyword`
- **Description**: The current status of the participant in the case (e.g., in custody, on bail).
- **Example**: `in custody`

#### 13. `participant.demographics`
- **Type**: `object`
- **Description**: Contains multiple demographic attributes such as age and disability status.
- **Example**: `{ "age": 35, "disability_status": "none" }`

### Usage Notes

- **Core Fields**: These fields must be present for each participant to ensure consistency and data accuracy.
- **Extended Fields**: Additional fields can be included as necessary, depending on the context of the case.

### Example Document

#### YAML

```yaml
participant:
  id: PART67890
  case_id: ["CASE12345", "CASE67890"]
  role: victim
  name: Jane Smith
  affiliation: None
  contact_info: janesmith@example.com
  date_of_birth: 1985-06-15
  gender: female
  ethnicity: Hispanic
  address: 123 Elm Street, Anytown, USA
  legal_representation: Public Defender's Office
  status: in custody
  demographics:
    age: 35
    disability_status: none
```

#### JSON

```json
{
  "participant": {
    "id": "PART67890",
    "case_id": ["CASE12345", "CASE67890"],
    "role": "victim",
    "name": "Jane Smith",
    "affiliation": "None",
    "contact_info": "janesmith@example.com",
    "date_of_birth": "1985-06-15",
    "gender": "female",
    "ethnicity": "Hispanic",
    "address": "123 Elm Street, Anytown, USA",
    "legal_representation": "Public Defender's Office",
    "status": "in custody",
    "demographics": {
      "age": 35,
      "disability_status": "none"
    }
  }
}
```

This markdown file (`participants.md`) now accurately reflects that participants can be associated with multiple cases by using an array for the `case_id` field. This ensures flexibility and accuracy in managing participant data within the justice system.