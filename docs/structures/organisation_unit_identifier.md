# Organisation Unit Identifier Fields

The **Organisation Unit Identifier Fields** section of the Justice Information Exchange (JIX) language captures information about organisational units within the criminal justice system. This includes codes and names used to identify physical or logical units within criminal justice organisations (CJOs) or external organisations accessing the CJS Exchange. These fields ensure comprehensive documentation and standardised identification of organisational units.

## Field Set Overview

The **Organisation Unit Identifier Fields** include attributes such as organisation unit codes, names, and effective dates, providing a detailed record of the organisational structure within the criminal justice system.

### Core Fields

These are the essential fields required for documenting organisation unit identifiers:

| Field Name                    | Type      | Description                                                                 | Example                     |
|------------------------------|-----------|-----------------------------------------------------------------------------|-----------------------------|
| `organisation_unit.id`       | `keyword` | A unique identifier for each organisation unit record.                      | `ORG12345`                  |
| `organisation_unit.code`     | `keyword` | The official code representing the organisation unit.                       | `POLICE_UNIT_001`           |
| `organisation_unit.name`     | `text`    | The name of the organisation unit.                                          | `Anytown Police Department` |
| `organisation_unit.level`    | `keyword` | The hierarchical level of the organisation unit (e.g., top, middle, bottom).| `top`                       |
| `organisation_unit.start_date` | `date`    | The date when the organisation unit became effective.                       | `2020-01-01`                |
| `organisation_unit.end_date` | `date`    | The date when the organisation unit ceased to be effective (if applicable). | `2023-12-31`                |

### Extended Fields

These fields provide additional details and context for organisation units:

| Field Name                    | Type      | Description                                                                 | Example                     |
|------------------------------|-----------|-----------------------------------------------------------------------------|-----------------------------|
| `organisation_unit.parent_code` | `keyword` | The code of the parent organisation unit.                                   | `MINISTRY_001`              |
| `organisation_unit.type`     | `keyword` | The type of organisation unit (e.g., police station, court, administrative unit). | `police station`           |
| `organisation_unit.legacy_code` | `keyword` | Any legacy code previously used to identify the organisation unit.          | `OLD_CODE_123`              |
| `organisation_unit.related_cases` | `array`   | A list of case IDs linked to the organisation unit.                         | `["CASE123", "CASE456"]`    |
| `organisation_unit.notes`    | `text`    | Additional notes or remarks about the organisation unit.                    | `Merged with another unit in 2023.` |

### Field Details

#### 1. `organisation_unit.id`
- **Type**: `keyword`
- **Description**: A unique identifier for each organisation unit record.
- **Example**: `ORG12345`

#### 2. `organisation_unit.code`
- **Type**: `keyword`
- **Description**: The official code representing the organisation unit.
- **Example**: `POLICE_UNIT_001`

#### 3. `organisation_unit.name`
- **Type**: `text`
- **Description**: The name of the organisation unit.
- **Example**: `Anytown Police Department`

#### 4. `organisation_unit.level`
- **Type**: `keyword`
- **Description**: The hierarchical level of the organisation unit (e.g., top, middle, bottom).
- **Example**: `top`

#### 5. `organisation_unit.start_date`
- **Type**: `date`
- **Description**: The date when the organisation unit became effective.
- **Example**: `2020-01-01`

#### 6. `organisation_unit.end_date`
- **Type**: `date`
- **Description**: The date when the organisation unit ceased to be effective (if applicable).
- **Example**: `2023-12-31`

#### 7. `organisation_unit.parent_code`
- **Type**: `keyword`
- **Description**: The code of the parent organisation unit.
- **Example**: `MINISTRY_001`

#### 8. `organisation_unit.type`
- **Type**: `keyword`
- **Description**: The type of organisation unit (e.g., police station, court, administrative unit).
- **Example**: `police station`

#### 9. `organisation_unit.legacy_code`
- **Type**: `keyword`
- **Description**: Any legacy code previously used to identify the organisation unit.
- **Example**: `OLD_CODE_123`

#### 10. `organisation_unit.related_cases`
- **Type**: `array`
- **Description**: A list of case IDs linked to the organisation unit.
- **Example**: `["CASE123", "CASE456"]`

#### 11. `organisation_unit.notes`
- **Type**: `text`
- **Description**: Additional notes or remarks about the organisation unit.
- **Example**: `Merged with another unit in 2023.`

### Usage Notes

- **Core Fields**: These fields must be present for each organisation unit to ensure accurate tracking and documentation of the organisational structure within the criminal justice system.
- **Extended Fields**: Additional fields can be used when further details are available or necessary for the organisation unit context.

### Example Document

#### YAML

```yaml
organisation_unit:
  id: ORG12345
  code: POLICE_UNIT_001
  name: Anytown Police Department
  level: top
  start_date: 2020-01-01
  end_date: 2023-12-31
  parent_code: MINISTRY_001
  type: police station
  legacy_code: OLD_CODE_123
  related_cases: ["CASE123", "CASE456"]
  notes: Merged with another unit in 2023.
```

#### JSON

```json
{
  "organisation_unit": {
    "id": "ORG12345",
    "code": "POLICE_UNIT_001",
    "name": "Anytown Police Department",
    "level": "top",
    "start_date": "2020-01-01",
    "end_date": "2023-12-31",
    "parent_code": "MINISTRY_001",
    "type": "police station",
    "legacy_code": "OLD_CODE_123",
    "related_cases": ["CASE123", "CASE456"],
    "notes": "Merged with another unit in 2023."
  }
}
```

