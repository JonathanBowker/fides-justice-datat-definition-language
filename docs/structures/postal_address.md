# Postal Address Fields

The **Postal Address Fields** section of the Justice Information Exchange (JIX) language captures information about the postal addresses of individuals or organisations involved in legal cases. This includes details necessary for identifying and documenting locations associated with persons or entities within the criminal justice system.

## Field Set Overview

The **Postal Address Fields** include attributes such as the address lines, postcode, and country, providing a comprehensive record of postal addresses associated with cases.

### Core Fields

These are the essential fields required for documenting postal addresses:

| Field Name                     | Type      | Description                                                                 | Example                     |
|-------------------------------|-----------|-----------------------------------------------------------------------------|-----------------------------|
| `postal_address.id`           | `keyword` | A unique identifier for each postal address record.                         | `ADDR12345`                 |
| `postal_address.case_id`      | `array`   | An array of unique identifiers for the cases associated with the address.   | `["CASE12345", "CASE67890"]`|
| `postal_address.address_line_1` | `text`    | The first line of the address, typically the building number and street name. | `123 High Street`          |
| `postal_address.address_line_2` | `text`    | The second line of the address, if applicable (e.g., building name, floor). | `Flat 2B`                   |
| `postal_address.town_city`    | `text`    | The town or city of the postal address.                                     | `Anytown`                   |
| `postal_address.county`       | `text`    | The county of the postal address.                                           | `Anyshire`                  |
| `postal_address.postcode`     | `keyword` | The postcode of the postal address.                                         | `AB12 3CD`                  |
| `postal_address.country`      | `text`    | The country of the postal address.                                          | `United Kingdom`            |

### Extended Fields

These fields provide additional details and context for postal addresses:

| Field Name                     | Type      | Description                                                                 | Example                     |
|-------------------------------|-----------|-----------------------------------------------------------------------------|-----------------------------|
| `postal_address.start_date`   | `date`    | The date when the address became valid.                                     | `2020-01-01`                |
| `postal_address.end_date`     | `date`    | The date when the address ceased to be valid (if applicable).               | `2023-12-31`                |
| `postal_address.address_type` | `keyword` | The type of address (e.g., residential, business, temporary).               | `residential`               |
| `postal_address.notes`        | `text`    | Additional notes or remarks about the postal address.                       | `This is the defendant's previous address.` |

### Field Details

#### 1. `postal_address.id`
- **Type**: `keyword`
- **Description**: A unique identifier for each postal address record.
- **Example**: `ADDR12345`

#### 2. `postal_address.case_id`
- **Type**: `array`
- **Description**: An array of unique identifiers representing the cases linked to the address, allowing tracking across multiple cases.
- **Example**: `["CASE12345", "CASE67890"]`

#### 3. `postal_address.address_line_1`
- **Type**: `text`
- **Description**: The first line of the address, typically the building number and street name.
- **Example**: `123 High Street`

#### 4. `postal_address.address_line_2`
- **Type**: `text`
- **Description**: The second line of the address, if applicable (e.g., building name, floor).
- **Example**: `Flat 2B`

#### 5. `postal_address.town_city`
- **Type**: `text`
- **Description**: The town or city of the postal address.
- **Example**: `Anytown`

#### 6. `postal_address.county`
- **Type**: `text`
- **Description**: The county of the postal address.
- **Example**: `Anyshire`

#### 7. `postal_address.postcode`
- **Type**: `keyword`
- **Description**: The postcode of the postal address.
- **Example**: `AB12 3CD`

#### 8. `postal_address.country`
- **Type**: `text`
- **Description**: The country of the postal address.
- **Example**: `United Kingdom`

#### 9. `postal_address.start_date`
- **Type**: `date`
- **Description**: The date when the address became valid.
- **Example**: `2020-01-01`

#### 10. `postal_address.end_date`
- **Type**: `date`
- **Description**: The date when the address ceased to be valid (if applicable).
- **Example**: `2023-12-31`

#### 11. `postal_address.address_type`
- **Type**: `keyword`
- **Description**: The type of address (e.g., residential, business, temporary).
- **Example**: `residential`

#### 12. `postal_address.notes`
- **Type**: `text`
- **Description**: Additional notes or remarks about the postal address.
- **Example**: `This is the defendant's previous address.`

### Usage Notes

- **Core Fields**: These fields must be present for each postal address record to ensure accurate tracking and documentation within the case timeline.
- **Extended Fields**: Additional fields can be used when further details are available or necessary for the address context.

### Example Document

#### YAML

```yaml
postal_address:
  id: ADDR12345
  case_id: ["CASE12345", "CASE67890"]
  address_line_1: 123 High Street
  address_line_2: Flat 2B
  town_city: Anytown
  county: Anyshire
  postcode: AB12 3CD
  country: United Kingdom
  start_date: 2020-01-01
  end_date: 2023-12-31
  address_type: residential
  notes: This is the defendant's previous address.
```

#### JSON

```json
{
  "postal_address": {
    "id": "ADDR12345",
    "case_id": ["CASE12345", "CASE67890"],
    "address_line_1": "123 High Street",
    "address_line_2": "Flat 2B",
    "town_city": "Anytown",
    "county": "Anyshire",
    "postcode": "AB12 3CD",
    "country": "United Kingdom",
    "start_date": "2020-01-01",
    "end_date": "2023-12-31",
    "address_type": "residential",
    "notes": "This is the defendant's previous address."
  }
}
```