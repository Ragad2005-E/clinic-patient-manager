# Clinic Patient Manager

A Python console project by Ragad Mohammad Eid, built to practice classes, dictionaries, lists and input validation.

## Run
Requires Python 3; no external packages.
```sh
python clinic.py
```
The demonstration administrator login is `admin` / `admin`.

## Features
- Add, list, search, edit and delete patient records.
- Maintain a treatment catalog and assign treatments.
- Patient login to view and edit a record.
- Validate required fields, email format and the eight phone digits entered after `05`.

## Design
`Patient` stores a record; `Admin` manages the dictionaries and treatment catalog. `adminPage`, `patientPage` and `ClinicPatientManagementSystem` are module functions, not methods of a third class. See [the class diagram](uml.svg).

## Scope
An academic console simulation. Data exists only during the session. Passwords are held in memory as plain text, and patients can edit treatment selections. This does not implement clinical authorization or production security; use fictional records only.

## Review notes
Fixed blank required inputs, whitespace in IDs, email checks that incorrectly required `.com`, duplicate treatment selections and execution on import. Kept the original menu-based structure.

## Walkthrough
[Ragad's project video](https://youtu.be/gvoyKhetTz0)
