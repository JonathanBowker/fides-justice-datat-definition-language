# Data Standards

The **Judicial Electronic Data Interchange Language (JEDI)** is built upon a set of data standards designed to ensure consistency, accuracy, and interoperability across justice-related information systems. These standards define how data should be structured, formatted, and validated, promoting uniformity across various components within the schema.

## Key Data Standards

The following data standards are applied across the JEDI to maintain high-quality data management:

### 1. Data Types
Each field within the schema is assigned a specific data type. Common data types used in the schema include:

- **Keyword**: Used for unique identifiers or predefined values (e.g., `case.id`, `participant.role`).
- **Text**: Used for descriptive fields that may contain free text (e.g., `participant.name`, `case.description`).
- **Date**: Applied to fields that require date values, formatted as `YYYY-MM-DD` (e.g., `case.start_date`, `evidence.date_collected`).
- **Boolean**: Used for fields that represent binary values, such as `true` or `false` (e.g., `bail.supervision_required`).
- **Double**: Numeric fields that require decimal values (e.g., `bail.amount`).

### 2. Naming Conventions
Field names follow consistent naming conventions to ensure clarity and uniformity:

- Field names are written in **snake_case** (e.g., `participant.contact_info`, `case.outcome`).
- Prefixes indicate the entity or component to which the field belongs (e.g., `case`, `participant`, `evidence`).

### 3. Date and Time Formatting
Dates are formatted using the ISO 8601 standard (`YYYY-MM-DD`). This format ensures consistency and enables efficient sorting and filtering of date-related data.

- Example: `2023-10-15`

### 4. Unique Identifiers
Each major entity within the schema (e.g., cases, participants, evidence) is assigned a unique identifier. These identifiers are used to link related records across different components, ensuring the integrity and traceability of data:

- **Case ID**: `CASE12345`
- **Participant ID**: `PART67890`
- **Evidence ID**: `EVID56789`

### 5. Linking and Relationships
The schema is designed to establish clear relationships between different entities:

- **Case-Centric Structure**: All components such as participants, offences, evidence, and events are linked to specific cases using unique identifiers.
- **Cross-Referencing**: Fields like `related_cases`, `case_id`, and `participant_id` are used to create relationships between entities, ensuring that all relevant information is interconnected.

### 6. Validation Rules
To maintain data integrity, certain fields have validation rules applied:

- **Mandatory Fields**: Core fields (e.g., `case.id`, `participant.name`) are mandatory and must be provided for each record.
- **Data Type Validation**: Fields are validated against their specified data types to prevent inconsistencies (e.g., ensuring `date` fields contain valid dates).
- **Enumeration Lists**: Fields with predefined values (e.g., `case.status`, `participant.role`) must match an approved list of values to ensure consistency.

### 7. Data Privacy and Security
The schema incorporates standards to protect sensitive information:

- **Anonymisation**: In certain fields, data may be anonymised to protect the identity of participants, especially for victims and witnesses.
- **Access Control**: Data should be stored and accessed following secure protocols, ensuring that only authorised personnel can view or modify sensitive information.

## Implementation Notes

- The schema should be implemented with tools and technologies that support these data standards, ensuring consistency across systems and databases.
- Regular audits and validations should be conducted to maintain data integrity and accuracy.

By adhering to these data standards, the Judicial Electronic Data Interchange Language ensures a robust, reliable, and interoperable system for managing justice-related information, promoting efficiency and consistency across the criminal justice process.
