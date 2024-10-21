# Data Standards

The **Criminal Justice Schema (CJS)** is built upon a set of data standards designed to ensure consistency, accuracy, and interoperability across justice-related information systems. These standards define how data should be structured, formatted, and validated, promoting uniformity across various components within the schema.

## Key Data Standards

The following data standards are applied across CJS to maintain high-quality data management:

### 1. Data Types
Each field within the schema is assigned a specific data type. The most applicable Elasticsearch data types used in the schema include:

- **`keyword`**: Used for structured text that does not need to be analyzed, such as case identifiers, legal codes, and participant roles. It is ideal for exact matches, sorting, and aggregations.
- **`text`**: Applied to unstructured text that may contain free text, such as witness statements, case descriptions, or legal documents, allowing for full-text search capabilities.
- **`date`**: Applied to fields that store date values, following the **DD-MM-YYYY** format, in compliance with ISO 8601 standards (e.g., `offence_date`, `hearing_date`).
- **`geo_point`**: Used for storing geographical locations such as crime scenes, police station locations, or courthouse addresses, enabling geo-based queries like proximity searches.
- **`boolean`**: Represents binary values (`true` or `false`), useful for fields such as `bail_granted`, `supervision_required`, or `detention_status`.
- **`long`**, **`integer`**: Applied to numeric fields storing whole numbers, such as case numbers, IDs, or counts (e.g., number of charges or witnesses).
- **`float`**, **`double`**: Used for storing numerical values that require decimals, such as `bail_amount` or `monetary_fines`.
- **`nested`**: Suitable for storing arrays of objects, where each object (e.g., multiple offences related to a case) needs to be indexed and queried independently while preserving relationships.
- **`object`**: Represents complex records that may contain multiple fields within an object (e.g., detailed information about a person, such as name, address, and contact details).
- **`array`**: Fields that can store multiple values (e.g., an array of evidence items, participant IDs, or case statuses).

### 2. Naming Conventions
Field names follow consistent naming conventions to ensure clarity and uniformity:

- Field names are written in **snake_case** (e.g., `person.contact_info`, `case.outcome`).
- Prefixes indicate the entity or component to which the field belongs (e.g., `case`, `person`, `evidence`).

### 3. Date and Time Formatting
Dates are formatted using the **DD-MM-YYYY** format according to ISO 8601 standards. This format ensures consistency and enables efficient sorting and filtering of date-related data.

- Example: `15-10-2023`

### 4. Unique Identifiers
Each major entity within the schema is assigned a unique identifier (UID) following the format of **three letters followed by seven digits (e.g., 0000001)**. These UIDs are structured to ensure integrity and traceability of data across different components and follow the order of the entities listed in the schema:

1. **Criminal Prosecution Reference ID**: `CPR1234567`
2. **Hearing ID**: `HRG0000001`
3. **Offence ID**: `OFF0000001`
4. **Organisation Unit Identifier (OU ID)**: `OU0000001`
5. **Person ID**: `PER0000001`
6. **Postal Address ID**: `ADD0000001`
7. **Result ID**: `RES0000001`
8. **Result Qualifier ID**: `REQ0000001`
9. **Role ID**: `ROL0000001`
10. **System ID**: `SYS0000001`
11. **Material ID**: `MAT0000001`

These identifiers are used to link related records across different components, ensuring the integrity and traceability of data throughout the schema.

### 5. Linking and Relationships
The schema is designed to establish clear relationships between different entities:

- **Case-Centric Structure**: All components, such as persons, offences, evidence, and events, are linked to specific cases using unique identifiers.
- **Cross-Referencing**: Fields like `related_cases`, `case_id`, `person_id`, and `material_id` are used to create relationships between entities, ensuring all relevant information is interconnected.

### 6. Validation Rules
To maintain data integrity, certain fields have validation rules applied:

- **Mandatory Fields**: Core fields (e.g., `case.id`, `person.name`) are mandatory and must be provided for each record.
- **Data Type Validation**: Fields are validated against their specified data types to prevent inconsistencies (e.g., ensuring `date` fields contain valid dates).
- **Enumeration Lists**: Fields with predefined values (e.g., `case.status`, `person.role`) must match an approved list of values to ensure consistency.

### 7. Data Privacy and Security
The schema incorporates standards to protect sensitive information:

- **Anonymisation**: Certain fields may be anonymised to protect the identity of persons, especially for victims and witnesses.
- **Access Control**: Data should be stored and accessed following secure protocols, ensuring that only authorised personnel can view or modify sensitive information.

## Major Entities

To support comprehensive and consistent data management, the **Criminal Justice Schema (CJS)** includes the following major entities:

1. **Criminal Prosecution Reference**: Links individuals to specific offences with a unique sequence and prosecution details.
2. **Hearing**: Captures data elements relevant to case hearings, including dates, locations, and outcomes.
3. **Offence (Fixed)**: Provides detailed information on offences, including CJS codes, legislative context, and indicators for recordability and notifiability.
4. **Organisation Unit Identifier**: Represents the organisational structure and units within Criminal Justice Organisations (CJOs) accessing the CJS exchange.
5. **Person**: Describes individuals involved in the justice system, such as defendants, victims, or legal professionals.
6. **Postal Address**: Details the postal addresses of persons or organisations involved in a case.
7. **Result (Fixed)**: Defines case outcomes, including interim, partial, or final results.
8. **Result Qualifier (Fixed)**: Adds additional context or information to a result, providing further classification.
9. **Role**: Shows the specific roles of persons or organisations in relation to a case.
10. **System ID**: Identifies and tracks system-related components, ensuring consistent monitoring and linking of data.
11. **Material**: Documents and evidence related to legal proceedings, such as reports, evidence files, and records.

### 8. Implementation Notes

- The schema should be implemented with tools and technologies that support these data standards, ensuring consistency across systems and databases.
- Regular audits and validations should be conducted to maintain data integrity and accuracy.

By adhering to these data standards, the **Criminal Justice Schema (CJS)** ensures a robust, reliable, and interoperable system for managing justice-related information, promoting efficiency and consistency across the criminal justice process.