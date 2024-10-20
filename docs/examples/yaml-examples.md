# Example Case File YAML 

This is a fully populated YAML example of a case (case.yaml) demonstrating the integration of all related fields including events, participants, offences, evidence, judicial procedures, victim support, probation/parole, sentences, enforcement actions, and bail/detention records. This example provides a comprehensive view of how the data interrelates within the schema.

### YAML Representation

```yaml
case:
  id: CASE12345
  status: open
  type: criminal
  start_date: "2023-01-10"
  end_date: null
  description: Armed robbery at a commercial property involving multiple suspects.
  location: Anytown District Court
  related_documents:
    - DOC123
    - DOC456
  notes: The case involves multiple defendants and victims, and the preliminary hearing is scheduled for the next month.
  criminal_prosecution_reference:
    defendant_or_offender: PART123
    offence_reason: robbery
    offence_reason_sequence: 1
  participants:
    - id: PART123
      role: defendant
      name: John Doe
      cpr: CPR12345
      contact_info:
        email: johndoe@example.com
        phone: "+44 123 456 789"
        postal_address:
          uk_address: 123 High Street, Anytown
          uk_postcode: AT1 2BC
          country: UK
      organisation_unit_identifier:
        ou_code_top_level: Police Department
        ou_code_bottom_level: Arrests Division
        ou_start_date: "2023-01-01"
        ou_end_date: null
        ou_notes: Active unit handling criminal arrests.
    - id: PART456
      role: defendant
      name: Jane Smith
      cpr: CPR67890
      contact_info:
        email: janesmith@example.com
        phone: "+44 987 654 321"
        postal_address:
          uk_address: 456 Maple Avenue, Anytown
          uk_postcode: AT3 5XY
          country: UK
    - id: PART789
      role: victim
      name: Mark Johnson
      cpr: CPR98765
      affiliation: Private Citizen
      contact_info:
        email: markjohnson@example.com
        phone: "+44 555 123 456"
        postal_address:
          uk_address: 789 Elm Street, Anytown
          uk_postcode: AT6 9ZW
          country: UK
  hearings:
    - id: HRG001
      case_id: CASE12345
      type: preliminary_hearing
      date: "2023-02-15"
      time: "10:00"
      location: Courtroom 2, Anytown District Court
      language_indicator: English
      documentation_language: English
      defendant_present: true
      related_documents:
        - DOC456
      report_requested_date: "2023-02-01"
      report_completed_date: "2023-02-10"
  offences:
    - id: OFF123
      type: robbery
      cjs_offence_code: CJS211
      description: Armed robbery at a commercial property
      location: 123 Market Street, Anytown
      date: "2023-01-10"
      severity: felony
      legislation:
        title: Penal Code 211
        jurisdiction: England and Wales
      recordable_on_pnc_indicator: true
      notifiable_to_home_office_indicator: true
      custodial_indicator: true
      max_c

ustodial_sentence_length_crown_court: 10 years
      max_fine_crown_court: unlimited
      victim_ids:
        - PART789
      offender_ids:
        - PART123
        - PART456
  results:
    - id: RES001
      case_id: CASE12345
      result_code: CJS001
      description: Preliminary hearing completed.
      type_code: interim
      england_wales_indicator: true
      start_date: "2023-02-15"
      end_date: null
      last_amended_date: "2023-02-16"
      notes: Decision pending further evidence submission.
  result_qualifiers:
    - result_id: RES001
      qualifier_code: RQ001
      description: Hearing result awaiting final ruling.
      start_date: "2023-02-15"
      last_amended_date: "2023-02-16"
      end_date: null
      notes: Requires additional forensic analysis.
  materials:
    - id: MAT001
      title: Forensic Report on CCTV Footage
      category: forensic
      source: Anytown Forensic Lab
      version: "1"
      date_published: "2023-01-13"
      description: Analysis of CCTV footage showing the robbery.
      language: English
      jurisdiction: England and Wales
      access_level: restricted
      file_type: PDF
      url: http://forensiclabs.gov.uk/reports/MAT001.pdf
      related_cases:
        - CASE12345
      author: Dr. Jane Doe
      usage_notes: For use in court proceedings only.
      expiry_date: null
      keywords:
        - CCTV
        - Forensic Report
        - Robbery
      regulatory_compliance: CJSE
      ai_rules: No AI usage without case officer approval.
```

