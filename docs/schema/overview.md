# Schema Overview

The **Judicial Electronic Data Interchange Language (JEDI)** is designed to provide a standardised and interconnected approach to managing and integrating data across various processes within the criminal justice system. It provides a dot notation snake_case syntax that encompasses key components, each representing a different aspect of case data, ensuring comprehensive documentation and management.

## Key Components

The schema includes the following interconnected components:

### 1. [Participants](participants.md)
Captures information about individuals and entities involved in cases, such as defendants, victims, witnesses, and legal professionals.

### 2. [Victim Support](victim_support.md)
Documents services and support measures provided to victims, including counselling, protective orders, and other forms of assistance.

### 3. [Evidence](evidence.md)
Tracks all evidence collected and managed within cases, including physical, digital, and testimonial evidence, along with chain of custody details.

### 4. [Probation and Parole](probation_parole.md)
Records details related to probation or parole conditions for individuals, including supervision requirements and compliance tracking.

### 5. [Offences](offenses.md)
Details offences associated with cases, including charges, statutes violated, and the severity of charges.

### 6. [Sentences](sentences.md)
Captures sentencing outcomes such as the type of sentence imposed (e.g., probation, incarceration), duration, and conditions.

### 7. [Cases](cases.md)
Acts as the central hub of the schema, linking participants, offences, events, and other components together to provide a comprehensive record of each legal case.

### 8. [Events](events.md)
Documents key events throughout the case lifecycle, including hearings, arrests, evidence collection, and other procedural activities.

### 9. [Enforcement](enforcement.md)
Tracks law enforcement actions, personnel involved, and activities such as arrests, investigations, and enforcement measures related to cases.

### 10. [Judicial Procedures](judicial_procedures.md)
Documents court-related actions, including motions, rulings, hearings, and other judicial processes associated with cases.

### 11. [Bail and Detention](bail_detention.md)
Records bail conditions, detention status, and monitoring information for individuals under custody or release conditions.

## Interconnected Structure

The JEDI components are designed to work together to create a comprehensive system for tracking justice-related information:

- **Case-Centric**: The [Cases](cases.md) component serves as the central hub, connecting to all other tables such as participants, evidence, events, and judicial procedures.
- **Participant Relationships**: The [Participants](participants.md) component connects to other entities like offences, sentences, victim support, and bail/detention, ensuring a complete view of an individual’s role and involvement in the justice process.
- **Timeline Integration**: [Events](events.md), [Judicial Procedures](judicial_procedures.md), and [Enforcement](enforcement.md) actions are integrated within the timeline of each case, providing a chronological view of case progression.

This structured approach ensures that all justice-related data is documented systematically, enabling efficient tracking, analysis, and management across the criminal justice system.
