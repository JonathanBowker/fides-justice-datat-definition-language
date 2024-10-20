# Role Fields

The **Role Fields** section of the **Criminal Justice Schema (CJS)** defines and captures information about the roles of individuals or organisations within legal proceedings. These fields ensure precise documentation of roles and their attributes, facilitating consistent tracking within the criminal justice system.

## Field Set Overview

The **Role Fields** include attributes such as role codes, descriptions, and associated entities, providing a detailed record of each role within a case.

### Version Information
- **Version**: 5
- **Approval Date**: 17th December 2013

### Core Fields

These are the essential fields required for documenting roles:

| Field Name                     | Type      | Description                                                               | Example                     |
|-------------------------------|-----------|---------------------------------------------------------------------------|-----------------------------|
| `role.id`                     | `keyword` | A unique identifier for each role record.                                 | `ROLE12345`                 |
| `role.case_id`                | `array`   | An array of unique identifiers for the cases associated with the role.    | `["CASE12345", "CASE67890"]`|
| `role.code`                   | `keyword` | The official CJS role code for the individual or organisation.            | `DEFENDANT`                 |
| `role.description`            | `text`    | A brief description of the role within the case.                          | `The accused individual`    |
| `role.type_code`              | `keyword` | The type code indicating the nature of the role (e.g., legal, witness).   | `legal`                     |
| `role.start_date`             | `date`    | The date when the role assignment began.                                  | `2020-01-01`                |
| `role.end_date`               | `date`    | The date when the role assignment ended (if applicable).                  | `2023-12-31`                |

### Extended Fields

These fields provide additional details and context for roles:

| Field Name                     | Type      | Description                                                               | Example                       |
|-------------------------------|-----------|---------------------------------------------------------------------------|-------------------------------|
| `role.last_amended_date`      | `date`    | The date when the role details were last amended.                         | `2021-05-15`                  |
| `role.qualification_code`     | `keyword` | The code for any qualification applicable to the role.                    | `QLF002`                      |
| `role.status_code`            | `keyword` | The status code associated with the role (e.g., active, inactive).        | `ACTIVE`                      |
| `role.notes`                  | `text`    | Additional notes or remarks about the role.                               | `Role status updated based on court order.` |

### Component Parts

#### 1. **Role Type Code**
- **Field Name**: `role.type_code`
- **Type**: `keyword`
- **Description**: The type code that specifies the nature of the role (e.g., legal, witness, administrative). This code helps categorise the role accurately.
- **Example**: `legal`

#### 2. **Role Type Description**
- **Description**: Provides a textual explanation for the corresponding `role.type_code`. It offers further detail to clarify the nature of the role being referenced.
- **Example**: `Legal role related to the defence or prosecution in a case.`

### Usage Notes

- **Core Fields**: These fields must be present for each role record to ensure accurate tracking and documentation within the case timeline.
- **Extended Fields**: Additional fields can be used when further details are available or necessary for the role context.

### Example Document

#### YAML

```yaml
role:
  id: ROLE12345
  case_id: ["CASE12345", "CASE67890"]
  code: DEFENDANT
  description: The accused individual
  type_code: legal
  start_date: 2020-01-01
  end_date: 2023-12-31
  last_amended_date: 2021-05-15
  qualification_code: QLF002
  status_code: ACTIVE
  notes: Role status updated based on court order.
```

#### JSON

```json
{
  "role": {
    "id": "ROLE12345",
    "case_id": ["CASE12345", "CASE67890"],
    "code": "DEFENDANT",
    "description": "The accused individual",
    "type_code": "legal",
    "start_date": "2020-01-01",
    "end_date": "2023-12-31",
    "last_amended_date": "2021-05-15",
    "qualification_code": "QLF002",
    "status_code": "ACTIVE",
    "notes": "Role status updated based on court order."
  }
}
```
