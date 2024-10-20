# Person Fields

The **Person Fields** section of the Justice Information Exchange (JIX) language captures detailed information about individuals involved in legal cases, including defendants, offenders, police personnel, and other relevant persons. These fields ensure comprehensive documentation and identification of individuals within the criminal justice system.

## Field Set Overview

The **Person Fields** include attributes such as personal identification numbers, name details, demographic information, and other relevant data, providing a complete record of individuals associated with cases.

### Core Fields

These are the essential fields required for documenting persons:

| Field Name                          | Type      | Description                                                                 | Example                     |
|------------------------------------|-----------|-----------------------------------------------------------------------------|-----------------------------|
| `person.id`                        | `keyword` | A unique identifier for each person record.                                 | `PER12345`                  |
| `person.case_id`                   | `array`   | An array of unique identifiers for the cases associated with the person.    | `["CASE12345", "CASE67890"]`|
| `person.given_name`                | `text`    | The given name of the person.                                               | `John`                      |
| `person.family_name`               | `text`    | The family name or surname of the person.                                   | `Doe`                       |
| `person.date_of_birth`             | `date`    | The date of birth of the person.                                            | `1980-01-01`                |
| `person.gender_type_code`          | `keyword` | The gender type code of the person.                                         | `male`                      |
| `person.national_insurance_number` | `keyword` | The person’s National Insurance Number, if applicable.                      | `QQ123456C`                 |
| `person.address`                   | `text`    | The postal address of the person.                                           | `123 High Street, Anytown`  |
| `person.ethnicity_self_defined_code`| `keyword` | The self-defined ethnicity code of the person.                              | `White British`             |
| `person.religion`                  | `text`    | The religion of the person, if applicable.                                  | `Christian`                 |

### Extended Fields

These fields provide additional details and context for persons:

| Field Name                          | Type      | Description                                                                 | Example                     |
|------------------------------------|-----------|-----------------------------------------------------------------------------|-----------------------------|
| `person.arrest_summons_number`     | `keyword` | The arrest summons number associated with the person.                       | `ASN123456`                 |
| `person.criminal_records_office_number` | `keyword` | The Criminal Records Office (CRO) number of the person.                     | `CRO123456`                 |
| `person.driving_licence_number`    | `keyword` | The driving licence number of the person, if applicable.                    | `D1234567`                  |
| `person.passport_number`           | `keyword` | The passport number of the person, if applicable.                           | `123456789`                 |
| `person.police_national_computer_id` | `keyword` | The Police National Computer (PNC) ID of the person.                        | `PNC123456`                 |
| `person.police_worker_collar_number`| `keyword` | The collar number for police workers associated with the person.            | `PC123`                     |
| `person.noms_number`               | `keyword` | The National Offender Management Service (NOMS) number for the person.      | `NOMS12345`                 |
| `person.language_requirement`      | `text`    | The language requirement for the person, if any.                            | `English`                   |
| `person.contact_details`           | `text`    | Contact information for the person, such as a phone number or email.        | `john.doe@example.com`      |
| `person.security_remarks`          | `text`    | Any security remarks related to the person.                                 | `Monitored for high-risk status.` |
| `person.perceived_birth_year`      | `integer` | The perceived birth year of the person, if the actual date is unknown.      | `1980`                      |
| `person.occupation_code`           | `keyword` | The occupation code describing the person’s occupation.                     | `OCC123`                    |
| `person.youth_offending_team_unique_person_id` | `keyword` | The unique ID for youth offending teams associated with the person.         | `YOT123`                    |
| `person.no_fixed_abode`            | `boolean` | Indicates whether the person has a fixed address.                           | `true`                      |
| `person.notes`                     | `text`    | Additional notes or remarks about the person.                               | `Previously convicted of similar offences.` |

### Example Document

#### YAML

```yaml
person:
  id: PER12345
  case_id: ["CASE12345", "CASE67890"]
  given_name: John
  family_name: Doe
  date_of_birth: 1980-01-01
  gender_type_code: male
  national_insurance_number: QQ123456C
  address: 123 High Street, Anytown
  ethnicity_self_defined_code: White British
  religion: Christian
  arrest_summons_number: ASN123456
  criminal_records_office_number: CRO123456
  driving_licence_number: D1234567
  passport_number: 123456789
  police_national_computer_id: PNC123456
  police_worker_collar_number: PC123
  noms_number: NOMS12345
  language_requirement: English
  contact_details: john.doe@example.com
  security_remarks: Monitored for high-risk status.
  perceived_birth_year: 1980
  occupation_code: OCC123
  youth_offending_team_unique_person_id: YOT123
  no_fixed_abode: true
  notes: Previously convicted of similar offences.
```

#### JSON

```json
{
  "person": {
    "id": "PER12345",
    "case_id": ["CASE12345", "CASE67890"],
    "given_name": "John",
    "family_name": "Doe",
    "date_of_birth": "1980-01-01",
    "gender_type_code": "male",
    "national_insurance_number": "QQ123456C",
    "address": "123 High Street, Anytown",
    "ethnicity_self_defined_code": "White British",
    "religion": "Christian",
    "arrest_summons_number": "ASN123456",
    "criminal_records_office_number": "CRO123456",
    "driving_licence_number": "D1234567",
    "passport_number": "123456789",
    "police_national_computer_id": "PNC123456",
    "police_worker_collar_number": "PC123",
    "noms_number": "NOMS12345",
    "language_requirement": "English",
    "contact_details": "john.doe@example.com",
    "security_remarks": "Monitored for high-risk status.",
    "perceived_birth_year": 1980,
    "occupation_code": "OCC123",
    "youth_offending_team_unique_person_id": "YOT123",
    "no_fixed_abode": true,
    "notes": "Previously convicted of similar offences."
  }
}
```
