# Foundations: topic map

The Foundations set is written by us rather than drawn from an article. To
avoid choosing topics one at a time, this map lists the core content an
intern in primary care or internal medicine meets, grouped by system.
Topics are written from the top of each group unless a rotation moves one
up. Where a guideline document is uploaded, the topic goes through the same
fact sheet and review steps as an article and is anchored to that text.

Status: done, next, later. Source: the guideline it should rest on.

## Cardiovascular

| Topic | Status | Source |
|---|---|---|
| Hypertension: diagnosis, drug choice, targets | done | ACC/AHA 2017 |
| Anticoagulation in atrial fibrillation: CHA2DS2-VASc, agent choice, bleeding | done | ACC/AHA/HRS |
| Lipids: who gets a statin, intensity, LDL goals | done | ACC/AHA 2018 |
| Chest pain in clinic: who goes to the emergency department | later | |
| Syncope: red flags and first tests | later | |
| Heart failure with preserved ejection fraction | later | AHA/ACC 2022 |
| Peripheral artery disease and claudication | later | |

## Endocrine

| Topic | Status | Source |
|---|---|---|
| Type 2 diabetes: diagnosis, targets, drug choice | done | ADA Standards |
| Insulin in hospital and at discharge: basal, correction, sliding scale | done | ADA |
| Hypothyroidism and the abnormal TSH | done | ATA |
| Hyperglycaemic emergencies: DKA and HHS basics | later | ADA |
| Osteoporosis: who to screen, who to treat | later | |

## Respiratory

| Topic | Status | Source |
|---|---|---|
| Asthma: stepwise therapy and the exacerbation | done | GINA |
| COPD: staging, inhalers, exacerbations | done | GOLD |
| Community-acquired pneumonia: severity, antibiotics, follow-up | next | ATS/IDSA 2019 |
| Pulmonary embolism: Wells, D-dimer, when to image | later | |

## Kidney and electrolytes

| Topic | Status | Source |
|---|---|---|
| Hyperkalemia: thresholds and the order of treatment | done | |
| Hyponatremia: rate of correction and the common causes | done | |
| Acute kidney injury: staging and the drugs to hold | later | KDIGO |
| Chronic kidney disease: staging and what slows it | later | KDIGO |

## Infection

| Topic | Status | Source |
|---|---|---|
| Urinary tract infection: cystitis, pyelonephritis, the catheter | done | IDSA |
| Cellulitis and abscess: when to cover MRSA | done | IDSA |
| Sepsis: recognition and the first hour | later | Surviving Sepsis |
| Clostridioides difficile: testing and treatment | later | IDSA |

## Gastrointestinal

| Topic | Status | Source |
|---|---|---|
| Upper GI bleeding: risk scores, PPI, when to scope | done | |
| Cirrhosis: ascites, SBP prophylaxis, encephalopathy | done | AASLD |
| GERD and when to scope | later | ACG |

## Neurology and psychiatry

| Topic | Status | Source |
|---|---|---|
| Depression: screening, first-line drugs, when to switch | done | |
| Stroke and TIA in clinic: antiplatelets, targets, driving | later | AHA/ASA |
| Headache red flags | later | |
| Delirium: recognising it, causes, what not to give | done | |

## Haematology and oncology

| Topic | Status | Source |
|---|---|---|
| Anaemia: the three patterns and the first tests | done | |
| Venous thromboembolism: duration of anticoagulation | done | CHEST |

## Everyday ward and clinic

| Topic | Status | Source |
|---|---|---|
| Perioperative medicine: which drugs to hold and when | done | |
| Pain: opioid conversions and safe prescribing | done | CDC 2022 |
| Preventive care: screening ages and intervals | later | USPSTF |
| Vaccines for adults | later | ACIP |

## How topics get written

1. Take the next topic in the group with the most "next" entries, or the
   one the current rotation needs.
2. If a guideline document is available, upload it and run the article
   pipeline: fact sheet, review, questions.
3. Otherwise write 12 to 15 questions from settled guideline content under
   the rules in `question-guidelines.md`, cite the guideline in the topic
   file, and mark it "review before trusting".
4. Run `python tools/check-topics.py`, add the file to the Foundations set
   in `topics/index.json`, push.
5. Play it. Notes from the game reorder this map and fix the questions.
