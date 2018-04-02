#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 29 13:31:44 2018

@author: neurolab
"""

menu_assessments = {
        "Diagnosis": "https://ida.loni.usc.edu/pages/access/studyData.jsp?categoryId=12&subCategoryId=37",
        "Neuropsychological": "https://ida.loni.usc.edu/pages/access/studyData.jsp?categoryId=12&subCategoryId=36", 
        "Non-clinical Assessments": "https://ida.loni.usc.edu/pages/access/studyData.jsp?categoryId=12&subCategoryId=189",
        "ALL": "https://ida.loni.usc.edu/pages/access/studyData.jsp?categoryId=12"
        }

menu_biospecimen = {
        "Biosample Inventory": "https://ida.loni.usc.edu/pages/access/studyData.jsp?categoryId=11&subCategoryId=58",
        "Biospecimen Results": "https://ida.loni.usc.edu/pages/access/studyData.jsp?categoryId=11&subCategoryId=33",
        "Lab Collection Procedures": "https://ida.loni.usc.edu/pages/access/studyData.jsp?categoryId=11&subCategoryId=32",
        "ALL": "https://ida.loni.usc.edu/pages/access/studyData.jsp?categoryId=11",
        }

menu_enrollment = {
        "Enrollment": "https://ida.loni.usc.edu/pages/access/studyData.jsp?categoryId=13&subCategoryId=38"
        }

menu_genetic = {
        "Genotype Results": "https://ida.loni.usc.edu/pages/access/studyData.jsp?categoryId=18&subCategoryId=27",
        "Other Genetic Data & Info ": "https://ida.loni.usc.edu/pages/access/studyData.jsp?categoryId=18&subCategoryId=28",
        "ALL": "https://ida.loni.usc.edu/pages/access/studyData.jsp?categoryId=18"
        }

menu_imaging = {
        "MR Image Acquisition": "https://ida.loni.usc.edu/pages/access/studyData.jsp?categoryId=14&subCategoryId=45",
        "MR Image Analysis": "https://ida.loni.usc.edu/pages/access/studyData.jsp?categoryId=14&subCategoryId=30",
        "MR Image Quality": "https://ida.loni.usc.edu/pages/access/studyData.jsp?categoryId=14&subCategoryId=47",
        "PET Image Acquisition": "https://ida.loni.usc.edu/pages/access/studyData.jsp?categoryId=14&subCategoryId=46",
        "PET Image Analysis": "https://ida.loni.usc.edu/pages/access/studyData.jsp?categoryId=14&subCategoryId=34",
        "PET Image Quality ": "https://ida.loni.usc.edu/pages/access/studyData.jsp?categoryId=14&subCategoryId=48",
        "ALL": "https://ida.loni.usc.edu/pages/access/studyData.jsp?categoryId=14"
        }

menu_medicalhistory = {
        "Adverse Events": "https://ida.loni.usc.edu/pages/access/studyData.jsp?categoryId=15&subCategoryId=41",
        "Drugs": "https://ida.loni.usc.edu/pages/access/studyData.jsp?categoryId=15&subCategoryId=40",
        "Medical History": "https://ida.loni.usc.edu/pages/access/studyData.jsp?categoryId=15&subCategoryId=39",
        "Physical/Neurological Exams": "https://ida.loni.usc.edu/pages/access/studyData.jsp?categoryId=15&subCategoryId=44",
        "ALL": "https://ida.loni.usc.edu/pages/access/studyData.jsp?categoryId=15"
        }

menu_studyinfo = {
        "Data & Databases": "https://ida.loni.usc.edu/pages/access/studyData.jsp?categoryId=16&subCategoryId=43",
        "Data Submission Standards": "https://ida.loni.usc.edu/pages/access/studyData.jsp?categoryId=16&subCategoryId=62",
        "Study Protocols & CRFs": "https://ida.loni.usc.edu/pages/access/studyData.jsp?categoryId=16&subCategoryId=42",
        "ALL": "https://ida.loni.usc.edu/pages/access/studyData.jsp?categoryId=16"
        }

menu_subjectcharacteristics = {
        "Family History": "https://ida.loni.usc.edu/pages/access/studyData.jsp?categoryId=17&subCategoryId=31",
        "Subject Demographics": "https://ida.loni.usc.edu/pages/access/studyData.jsp?categoryId=17&subCategoryId=29",
        "ALL": "https://ida.loni.usc.edu/pages/access/studyData.jsp?categoryId=17"
        }

menu_testdata = {
        "Data for Challenges": "https://ida.loni.usc.edu/pages/access/studyData.jsp?categoryId=43&subCategoryId=94"
        }

menu_archive = {
        "Archived Data": "https://ida.loni.usc.edu/pages/access/studyData.jsp?categoryId=42&subCategoryId=90"
        }

menu_principal = {
        "Assessments": menu_assessments,
        "Biospecimen": menu_biospecimen,
        "Enrollment": menu_enrollment,
        "Genetic": menu_genetic,
        "Imaging": menu_imaging,
        "Medical History": menu_medicalhistory,
        "Study Info": menu_studyinfo,
        "Subject Characteristics": menu_subjectcharacteristics,
        "Test Data": menu_testdata,
        "_Archive": menu_archive
        }