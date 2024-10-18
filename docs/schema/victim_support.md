# Victim Support Fields

The **Victim Support Fields** section of the Judicial Electronic Data Interchange Language (JEDI) documents services, protective measures, and support provided to victims involved in cases. These fields capture information on various types of victim support, including counselling, protection orders, and other assistance offered during legal proceedings.

## Field Set Overview

The **Victim Support Fields** include attributes such as the type of support provided, dates, and details about protective measures to ensure victims receive proper documentation and tracking of services.

### Core Fields

These are the essential fields required for documenting victim support:

| Field Name                    | Type      | Description                                                                 | Example                     |
|------------------------------|-----------|-----------------------------------------------------------------------------|-----------------------------|
| `victim_support.id`          | `keyword` | A unique identifier for each victim support record.                         | `SUPPORT12345`              |
| `victim_support.case_id`     | `array`   | An array of unique identifiers for the cases associated with the victim support record. | `["CASE12345", "CASE67890"]` |
| `victim_support.type`        | `keyword` | The type of support provided (e.g., counselling, shelter, legal aid).       | `counselling`               |
| `victim_support.start_date`  | `date`    | The date the support service started.                                       | `2023-08-15`                |
| `victim_support.end_date`    | `date`    | The date the support service ended (if applicable).                         | `2023-09-15`                |
| `victim_support.description` | `text`    | A detailed description of the support provided.                             | `Weekly counselling sessions`|
| `victim_support.provider`    | `text`    | The organisation or entity providing the support service.                   | `Victim Assistance Centre`  |

### Extended Fields

Additional fields may be included to provide further context and specific details:

| Field Name                    | Type      | Description                                                                 | Example                     |
|------------------------------|-----------|-----------------------------------------------------------------------------|-----------------------------|
| `victim_support.location`    | `text`    | The location where the support service is being provided.                   | `123 Support St, Anytown`   |
| `victim_support.contact`     | `text`    | Contact information for the support provider (e.g., phone number, email).   | `supportcentre@example.com` |
| `victim_support.protective_order` | `keyword` | Indicates if a protective order is part of the support provided.           | `yes`                       |

### Field Details

#### 1. `victim_support.id`
- **Type**: `keyword`
- **Description**: A unique identifier for each victim support record.
- **Example**: `SUPPORT12345`

#### 2. `victim_support.case_id`
- **Type**: `array`
- **Description**: An array of unique identifiers representing the cases linked to the victim support service, allowing the tracking of support across multiple cases.
- **Example**: `["CASE12345", "CASE67890"]`

#### 3. `victim_support.type`
- **Type**: `keyword`
- **Description**: The type of support service provided, such as counselling, shelter, or legal aid.
- **Example**: `counselling`

#### 4. `victim_support.start_date`
- **Type**: `date`
- **Description**: The date when the support service started.
- **Example**: `2023-08-15`

#### 5. `victim_support.end_date`
- **Type**: `date`
- **Description**: The date when the support service ended (if applicable).
- **Example**: `2023-09-15`

#### 6. `victim_support.description`
- **Type**: `text`
- **Description**: A detailed description of the support provided.
- **Example**: `Weekly counselling sessions`

#### 7. `victim_support.provider`
- **Type**: `text`
- **Description**: The name of the organisation or entity providing the support service.
- **Example**: `Victim Assistance Centre`

#### 8. `victim_support.location`
- **Type**: `text`
- **Description**: The location where the support service is being provided.
- **Example**: `123 Support St, Anytown`

#### 9. `victim_support.contact`
- **Type**: `text`
- **Description**: Contact information for the support provider, such as a phone number or email address.
- **Example**: `supportcentre@example.com`

#### 10. `victim_support.protective_order`
- **Type**: `keyword`
- **Description**: Indicates if a protective order is part of the support provided (e.g., yes, no).
- **Example**: `yes`

### Usage Notes

- **Core Fields**: These fields are necessary for each victim support entry to ensure that all critical information is captured.
- **Extended Fields**: Optional fields can be used when further details are available or required by the case context.

### Example Document

#### YAML

```yaml
victim_support:
  id: SUPPORT12345
  case_id: ["CASE12345", "CASE67890"]
  type: counselling
  start_date: 2023-08-15
  end_date: 2023-09-15
  description: Weekly counselling sessions
  provider: Victim Assistance Centre
  location: 123 Support St, Anytown
  contact: supportcentre@example.com
  protective_order: yes
```

#### JSON

```json
{
  "victim_support": {
    "id": "SUPPORT12345",
    "case_id": ["CASE12345", "CASE67890"],
    "type": "counselling",
    "start_date": "2023-08-15",
    "end_date": "2023-09-15",
    "description": "Weekly counselling sessions",
    "provider": "Victim Assistance Centre",
    "location": "123 Support St, Anytown",
    "contact": "supportcentre@example.com",
    "protective_order": "yes"
  }
}
```

This markdown file (`victim_support.md`) provides a comprehensive overview of the **Victim Support Fields** in the Judicial Electronic Data Interchange Language, ensuring proper documentation and tracking of support services provided to victims within the context of each legal case.
