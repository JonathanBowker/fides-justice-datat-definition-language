# Case Taxonomy Dataset

The `case_taxonomy` dataset within Fides provides a structured and standardized approach to categorizing and organizing case-related datasets and entities used in the criminal justice system. It ensures consistency, clarity, and interoperability by providing a unified framework for all case-related information.

## Dataset Overview

The dataset includes attributes such as case types, codes, descriptions, and relationships, providing a comprehensive record of case categories and their associated entities within Fides.

### Version Information
- **Version**: 1.0
- **Approval Date**: 20th October 2024

### Purpose
The `case_taxonomy` is designed to standardize how cases are categorized and organized within the system. It connects various entities like offences, hearings, results, and evidence, ensuring all information is systematically linked and categorized for effective data management, tracking, and analysis.

### Administrative Fields

These fields are essential for managing taxonomy records related to cases:

| Field Name                       | Type      | Description                                                                       | Example                 |
|---------------------------------|-----------|-----------------------------------------------------------------------------------|-------------------------|
| `case_taxonomy.id`              | `keyword` | A unique identifier for each case taxonomy record.                                 | `CAS001`                |
| `case_taxonomy.version`         | `keyword` | The version number of the case taxonomy record.                                    | `1.0`                   |
| `case_taxonomy.effective_start_date` | `date` | The date when the case taxonomy version becomes effective.                         | `2024-10-20`            |
| `case_taxonomy.effective_end_date`   | `date` | The date when the case taxonomy version ceases to be effective (if applicable).    | `null`                  |

### Core Fields

These are the essential fields required for documenting case-related entities:

| Field Name                       | Type      | Description                                                                       | Example                 |
|---------------------------------|-----------|-----------------------------------------------------------------------------------|-------------------------|
| `case_taxonomy.code`            | `keyword` | The official code representing a case category or entity type.                     | `CRIM`                  |
| `case_taxonomy.name`            | `text`    | The name or label of the case category represented by the taxonomy code.           | `Criminal Case`         |
| `case_taxonomy.description`     | `text`    | A description of the case category or entity type.                                 | `Cases involving criminal proceedings including offences and prosecution.` |
| `case_taxonomy.parent_code`     | `keyword` | The code of the parent entity in the hierarchy (if applicable).                    | `CASE`                  |
| `case_taxonomy.level`           | `integer` | The hierarchical level of the entity within the taxonomy (e.g., 1 for top-level).  | `2`                     |

### Extended Fields

These fields provide additional details and context for case taxonomy records:

| Field Name                       | Type      | Description                                                                       | Example                 |
|---------------------------------|-----------|-----------------------------------------------------------------------------------|-------------------------|
| `case_taxonomy.relationship_type` | `keyword` | The type of relationship that the case category has with other entities (e.g., parent-child, peer-to-peer). | `parent-child`          |
| `case_taxonomy.related_entities` | `array`   | A list of related entity codes connected to the case category.                     | `["OFF", "HEAR", "RES", "EVD"]` |
| `case_taxonomy.notes`            | `text`    | Additional notes or remarks about the case category.                               | `Used in all legal proceedings to link relevant entities such as hearings and evidence.` |
| `case_taxonomy.compliance_standard` | `keyword` | The standard or regulation that the case category must comply with.                | `CJSE`                  |

### Case Taxonomy Entity Types

The case taxonomy defines several key entity types relevant to cases within the criminal justice system. Below is an overview of the core datasets included in the Fides case taxonomy:

1. **Criminal Prosecution Reference (CPR)**: Links offences and defendants, documenting prosecution processes.
2. **Hearing (HEAR)**: Records details of legal hearings, including dates, locations, and participants.
3. **Offence (OFF)**: Categorizes criminal offences and provides associated details like codes and descriptions.
4. **Result Fixed (RES)**: Details legal outcomes, including codes, descriptions, and dates.
5. **Result Qualifier Fixed (RQL)**: Adds context or qualifiers to legal results.
6. **Evidence (EVD)**: Manages information about evidence used in legal proceedings, including forensic reports and digital records.
7. **Role (ROLE)**: Identifies the roles of individuals or entities in the criminal justice system, such as defendants, witnesses, or police workers.
8. **Person (PER)**: Represents individuals involved in cases, including defendants, witnesses, and law enforcement personnel.
9. **Organisation Unit Identifier (ORG)**: Captures information about the organisational units involved in the justice system.
10. **System ID (SYS)**: Provides system identifiers for internal record management.
11. **UK Internal Country (UKIC)**: Documents the internal divisions of the United Kingdom for jurisdictional purposes.
12. **Postal Address (ADDR)**: Captures information about postal addresses associated with persons or entities in cases.

### Field Details

#### 1. `case_taxonomy.id`
- **Type**: `keyword`
- **Description**: A unique identifier for each case taxonomy record.
- **Example**: `CAS001`

#### 2. `case_taxonomy.version`
- **Type**: `keyword`
- **Description**: The version number of the case taxonomy record.
- **Example**: `1.0`

#### 3. `case_taxonomy.effective_start_date`
- **Type**: `date`
- **Description**: The date when the case taxonomy version becomes effective.
- **Example**: `2024-10-20`

#### 4. `case_taxonomy.effective_end_date`
- **Type**: `date`
- **Description**: The date when the case taxonomy version ceases to be effective (if applicable).
- **Example**: `null`

#### 5. `case_taxonomy.code`
- **Type**: `keyword`
- **Description**: The official code representing a case category or entity type.
- **Example**: `CRIM`

#### 6. `case_taxonomy.name`
- **Type**: `text`
- **Description**: The name or label of the case category represented by the taxonomy code.
- **Example**: `Criminal Case`

#### 7. `case_taxonomy.description`
- **Type**: `text`
- **Description**: A description of the case category or entity type.
- **Example**: `Cases involving criminal proceedings including offences and prosecution.`

#### 8. `case_taxonomy.parent_code`
- **Type**: `keyword`
- **Description**: The code of the parent entity in the hierarchy (if applicable).
- **Example**: `CASE`

#### 9. `case_taxonomy.level`
- **Type**: `integer`
- **Description**: The hierarchical level of the entity within the taxonomy.
- **Example**: `2`

#### 10. `case_taxonomy.relationship_type`
- **Type**: `keyword`
- **Description**: The type of relationship that the case category has with other entities.
- **Example**: `parent-child`

#### 11. `case_taxonomy.related_entities`
- **Type**: `array`
- **Description**: A list of related entity codes connected to the case category.
- **Example**: `["OFF", "HEAR", "RES", "EVD"]`

#### 12. `case_taxonomy.notes`
- **Type**: `text`
- **Description**: Additional notes or remarks about the case category.
- **Example**: `Used in all legal proceedings to link relevant entities such as hearings and evidence.`

#### 13. `case_taxonomy.compliance_standard`
- **Type**: `keyword`
- **Description**: The standard or regulation that the case category must comply with.
- **Example**: `CJSE`

### Usage Notes

- **Core Fields**: These fields must be present for each case taxonomy record to ensure consistency and accurate tracking of case-related entities.
- **Extended Fields**: Additional fields can be used when further details are available or necessary for the case taxonomy context.

### Example Document

#### YAML

```yaml
case_taxonomy:
  id: CAS001
  version: "1.0"
  effective_start_date: "2024-10-20"
  effective_end_date: null
  code: CRIM
  name: Criminal Case
  description: Cases involving criminal proceedings including offences and prosecution.
  parent_code: CASE
  level: 2
  relationship_type: parent-child
  related_entities:
    - OFF
    - HEAR
    - RES
    - EVD
  notes: Used in all legal proceedings to link relevant entities such as hearings and evidence.
  compliance_standard: CJSE
```

#### JSON

```json
{
  "case_taxonomy": {
    "id": "CAS001",
    "version": "1.0",
    "effective_start_date": "2024-10-20",
    "effective_end_date": null,
    "code": "CRIM",
    "name": "Criminal Case",
    "description": "Cases involving criminal proceedings including offences and prosecution.",
    "parent_code": "CASE",
    "level": 2,
    "relationship_type": "parent-child",
    "related_entities": ["OFF", "HEAR", "RES", "EVD"],
    "notes": "Used in all legal proceedings to link relevant

 entities such as hearings and evidence.",
    "compliance_standard": "CJSE"
  }
}
```
