# Result Fields

The **Result Fields** section of the Justice Information Exchange (JIX) language captures information about the results of legal proceedings, including outcomes, related qualifiers, and other associated details. These fields ensure comprehensive documentation and tracking of case outcomes within the criminal justice system.

## Field Set Overview

The **Result Fields** include attributes such as result codes, descriptions, and relevant dates, providing a detailed record of the results associated with legal cases.

### Core Fields

These are the essential fields required for documenting results:

| Field Name                     | Type      | Description                                                                 | Example                     |
|-------------------------------|-----------|-----------------------------------------------------------------------------|-----------------------------|
| `result.id`                   | `keyword` | A unique identifier for each result record.                                 | `RES12345`                  |
| `result.case_id`              | `array`   | An array of unique identifiers for the cases associated with the result.    | `["CASE12345", "CASE67890"]`|
| `result.code`                 | `keyword` | The official CJS result code for the result.                                | `CJS001`                    |
| `result.description`          | `text`    | A brief description of the result.                                          | `Custodial sentence imposed.`|
| `result.type_code`            | `keyword` | The type code indicating the nature of the result (e.g., interim, final).   | `final`                     |
| `result.england_wales_indicator` | `keyword` | Indicates whether the result is applicable in England and Wales.            | `yes`                       |
| `result.start_date`           | `date`    | The date when the result code became effective.                             | `2020-01-01`                |
| `result.end_date`             | `date`    | The date when the result code ceased to be valid (if applicable).           | `2023-12-31`                |

### Extended Fields

These fields provide additional details and context for results:

| Field Name                     | Type      | Description                                                                 | Example                     |
|-------------------------------|-----------|-----------------------------------------------------------------------------|-----------------------------|
| `result.last_amended_date`    | `date`    | The date when the result code was last amended.                             | `2021-05-15`                |
| `result.applicable_qualifier_code` | `keyword` | The code for the qualifier applicable to the result.                         | `RQ002`                     |
| `result.offence_remand_status_code` | `keyword` | The remand status code associated with the offence related to the result.    | `ON_BAIL`                   |
| `result.duration_quantity`    | `integer` | The duration associated with the result (e.g., length of sentence).          | `12`                        |
| `result.date_quantity`        | `date`    | The specific date associated with the result.                                | `2023-09-01`                |
| `result.time_quantity`        | `time`    | The specific time associated with the result.                                | `14:00:00`                  |
| `result.amount_quantity`      | `decimal` | Any amount related to the result (e.g., fine amount).                        | `500.00`                    |
| `result.number_quantity`      | `integer` | Any numerical value related to the result.                                   | `2`                         |
| `result.text_quantity`        | `text`    | Any textual information related to the result.                               | `Community service order`   |
| `result.notes`                | `text`    | Additional notes or remarks about the result.                                | `Amended based on appeal outcome.` |

### Field Details

#### 1. `result.id`
- **Type**: `keyword`
- **Description**: A unique identifier for each result record.
- **Example**: `RES12345`

#### 2. `result.case_id`
- **Type**: `array`
- **Description**: An array of unique identifiers representing the cases linked to the result, allowing tracking across multiple cases.
- **Example**: `["CASE12345", "CASE67890"]`

#### 3. `result.code`
- **Type**: `keyword`
- **Description**: The official CJS result code for the result.
- **Example**: `CJS001`

#### 4. `result.description`
- **Type**: `text`
- **Description**: A brief description of the result.
- **Example**: `Custodial sentence imposed.`

#### 5. `result.type_code`
- **Type**: `keyword`
- **Description**: The type code indicating the nature of the result (e.g., interim, final).
- **Example**: `final`

#### 6. `result.england_wales_indicator`
- **Type**: `keyword`
- **Description**: Indicates whether the result is applicable in England and Wales.
- **Example**: `yes`

#### 7. `result.start_date`
- **Type**: `date`
- **Description**: The date when the result code became effective.
- **Example**: `2020-01-01`

#### 8. `result.end_date`
- **Type**: `date`
- **Description**: The date when the result code ceased to be valid (if applicable).
- **Example**: `2023-12-31`

#### 9. `result.last_amended_date`
- **Type**: `date`
- **Description**: The date when the result code was last amended.
- **Example**: `2021-05-15`

#### 10. `result.applicable_qualifier_code`
- **Type**: `keyword`
- **Description**: The code for the qualifier applicable to the result.
- **Example**: `RQ002`

#### 11. `result.offence_remand_status_code`
- **Type**: `keyword`
- **Description**: The remand status code associated with the offence related to the result.
- **Example**: `ON_BAIL`

#### 12. `result.duration_quantity`
- **Type**: `integer`
- **Description**: The duration associated with the result (e.g., length of sentence).
- **Example**: `12`

#### 13. `result.date_quantity`
- **Type**: `date`
- **Description**: The specific date associated with the result.
- **Example**: `2023-09-01`

#### 14. `result.time_quantity`
- **Type**: `time`
- **Description**: The specific time associated with the result.
- **Example**: `14:00:00`

#### 15. `result.amount_quantity`
- **Type**: `decimal`
- **Description**: Any amount related to the result (e.g., fine amount).
- **Example**: `500.00`

#### 16. `result.number_quantity`
- **Type**: `integer`
- **Description**: Any numerical value related to the result.
- **Example**: `2`

#### 17. `result.text_quantity`
- **Type**: `text`
- **Description**: Any textual information related to the result.
- **Example**: `Community service order`

#### 18. `result.notes`
- **Type**: `text`
- **Description**: Additional notes or remarks about the result.
- **Example**: `Amended based on appeal outcome.`

### Usage Notes

- **Core Fields**: These fields must be present for each result record to ensure accurate tracking and documentation within the case timeline.
- **Extended Fields**: Additional fields can be used when further details are available or necessary for the result context.

### Example Document

#### YAML

```yaml
result:
  id: RES12345
  case_id: ["CASE12345", "CASE67890"]
  code: CJS001
  description: Custodial sentence imposed.
  type_code: final
  england_wales_indicator: yes
  start_date: 2020-01-01
  end_date: 2023-12-31
  last_amended_date: 2021-05-15
  applicable_qualifier_code: RQ002
  offence_remand_status_code: ON_BAIL
  duration_quantity: 12
  date_quantity: 2023-09-01
  time_quantity: 14:00:00
  amount_quantity: 500.00
  number_quantity: 2
  text_quantity: Community service order
  notes: Amended based on appeal outcome.
```

#### JSON

```json
{
  "result": {
    "id": "RES12345",
    "case_id": ["CASE12345", "CASE67890"],
    "code": "CJS001",
    "description": "Custodial sentence imposed.",
    "type_code": "final",
    "england_wales_indicator": "yes",
    "start_date": "2020-01-01",
    "end_date": "2023-12-31",
    "last_amended_date": "2021-05-15",
    "applicable_qualifier_code": "RQ002",
    "offence_remand_status_code": "ON_BAIL",
    "duration_quantity": 12,
    "date_quantity": "2023-09-01",
    "time_quantity": "14:00:00",
    "amount_quantity": 500.00,
    "number_quantity": 2,
    "text_quantity": "Community service order",
    "notes": "Amended based on appeal outcome."
  }
  ```
