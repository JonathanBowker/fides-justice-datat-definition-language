# Example Case File YAML 

This is a fully populated YAML example of a case (case.yaml) demonstrating the integration of all related fields including events, participants, offenses, evidence, judicial procedures, victim support, probation/parole, sentences, enforcement actions, and bail/detention records. This example provides a comprehensive view of how the data interrelates within the schema.

```yaml
case:
  id: CASE12345
  status: open
  type: criminal
  start_date: 2023-01-10
  end_date: null
  description: Armed robbery at a commercial property involving multiple suspects.
  location: Anytown District Court
  related_documents:
    - DOC123
    - DOC456
  notes: The case involves multiple defendants and victims, and the preliminary hearing is scheduled for the next month.

  participants:
    - id: PART123
      role: defendant
      name: John Doe
      affiliation: null
      contact_info: johndoe@example.com
    - id: PART456
      role: defendant
      name: Jane Smith
      affiliation: null
      contact_info: janesmith@example.com
    - id: PART789
      role: victim
      name: Mark Johnson
      affiliation: Private Citizen
      contact_info: markjohnson@example.com

  victim_support:
    - id: SUPPORT001
      participant_id: PART789
      type: counselling
      provider: Victim Support Services
      start_date: 2023-01-15
      end_date: 2023-02-15
    - id: SUPPORT002
      participant_id: PART789
      type: financial
      provider: Compensation Fund
      start_date: 2023-01-20
      end_date: null

  evidence:
    - id: EVID123
      type: physical
      description: CCTV footage from the crime scene
      location: Evidence Locker 5, Anytown Police Department
      chain_of_custody:
        - officer: Officer Clark
          date: 2023-01-11
          action: collected
        - officer: Officer Clark
          date: 2023-01-12
          action: stored
    - id: EVID456
      type: forensic
      description: Fingerprints lifted from the cash register
      location: Forensic Lab
      forensic_details:
        method: fingerprint analysis
        result: match with suspect John Doe
        date: 2023-01-13

  probation_parole:
    - id: PP001
      participant_id: PART123
      type: parole
      start_date: 2023-06-01
      end_date: 2024-06-01
      conditions: Regular check-ins, no contact with the victim
      supervisor: Officer Jane Smith

  offenses:
    - id: OFF123
      type: robbery
      statute: Penal Code 211
      date: 2023-01-10
      severity: felony
      description: Armed robbery at a commercial property
      location: 123 Market Street, Anytown
      status: charged
      victim_ids:
        - PART789
      offender_ids:
        - PART123
        - PART456
    - id: OFF456
      type: assault
      statute: Penal Code 240
      date: 2023-01-10
      severity: felony
      description: Assault on an employee during the robbery
      location: 123 Market Street, Anytown
      status: charged
      victim_ids:
        - PART789
      offender_ids:
        - PART123

  sentences:
    - id: SENT001
      case_id: CASE12345
      type: imprisonment
      duration: 5 years
      start_date: 2023-07-01
      end_date: 2028-07-01
      conditions: No parole for the first two years
      supervision_required: true
      supervisor: Officer Jane Smith

  events:
    - id: EVT123
      case_id: CASE12345
      type: arrest
      date: 2023-01-11
      location: 456 Elm Street, Anytown
      description: Arrest of suspect John Doe
      participant_ids: 
        - PART123
      status: completed
      related_documents:
        - DOC123
    - id: EVT456
      case_id: CASE12345
      type: search_warrant_execution
      date: 2023-01-12
      location: 123 Maple Avenue, Anytown
      description: Execution of a search warrant at Jane Smith's residence
      participant_ids:
        - PART456
      status: completed
      related_documents:
        - DOC456
    - id: EVT789
      case_id: CASE12345
      type: preliminary_hearing
      date: 2023-02-15
      location: Courtroom 2, Anytown District Court
      description: Preliminary hearing for the defendants
      participant_ids:
        - PART123
        - PART456
      status: scheduled

  enforcement:
    - id: ENF001
      case_id: CASE12345
      type: arrest
      date: 2023-01-11
      location: 456 Elm Street, Anytown
      officer_id: OFFICER001
      agency: Anytown Police Department
      status: completed
      related_documents:
        - DOC123
    - id: ENF002
      case_id: CASE12345
      type: search_warrant_execution
      date: 2023-01-12
      location: 123 Maple Avenue, Anytown
      officer_id: OFFICER002
      agency: Anytown Police Department
      status: completed

  judicial_procedures:
    - id: JP001
      case_id: CASE12345
      type: preliminary_hearing
      date: 2023-02-15
      location: Courtroom 2, Anytown District Court
      description: Preliminary hearing to determine probable cause
      judge_ids:
        - JUDGE123
      participant_ids:
        - PART123
        - PART456
      status: scheduled
      related_documents:
        - DOC456
    - id: JP002
      case_id: CASE12345
      type: bail_hearing
      date: 2023-01-13
      location: Courtroom 1, Anytown District Court
      description: Bail hearing for defendant John Doe
      judge_ids:
        - JUDGE123
      status: completed
      related_documents:
        - DOC123

  bail_detention:
    - id: BD001
      case_id: CASE12345
      type: bail
      amount: 10000.00
      status: released on bail
      date: 2023-01-14
      conditions: No contact with the victim
      location: Anytown Bail Office
      supervision_required: true
      supervisor: Officer Jane Smith

```

### Summary
- **Participants**: Involves defendants and victims, with their respective roles and details.
- **Victim Support**: Services provided to victims, such as counselling and financial assistance.
- **Evidence**: Details physical and forensic evidence, chain of custody, and analysis methods.
- **Probation/Parole**: Details supervision conditions for released participants.
- **Offenses**: Multiple offenses related to the case, linked to participants.
- **Sentences**: Outcome sentences associated with offenses.
- **Events**: Records key events, including arrests, search warrants, and hearings.
- **Enforcement**: Details enforcement actions linked to the case.
- **Judicial Procedures**: Records court proceedings, such as hearings.
- **Bail/Detention**: Details bail conditions and supervision.

This YAML example shows how interconnected entities are structured and linked within the schema, ensuring comprehensive and consistent case documentation.