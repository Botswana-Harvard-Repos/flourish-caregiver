from edc_constants.constants import NONE, NOT_APPLICABLE, OTHER
from edc_list_data import PreloadData

list_data = {
    'flourish_caregiver.chronicconditions': [
        ('mhist_asthma', 'Asthma'),
        ('mhist_hyperten', 'Hypertension'),
        ('mhist_hyperchole', 'Hypercholesterolemia'),
        ('mhist_heart', 'Heart disease'),
        ('mhist_hepb_pos', 'Hepatitis B surface Ag positive'),
        ('mhist_hepb_carrier', 'Chronic Hepatitis B carrier'),
        ('mhist_hepc', 'Hepatitis C'),
        ('mhist_diab', 'Diabetes'),
        ('mhist_other', 'Other, Specify'),
        ('mhist_na', 'Not Applicable')
    ],
    'flourish_caregiver.wcsdxadult': [
        ('who_asympt', 'Asymptomatic'),
        ('who_lymphadeno', 'Persistent generalized lymphadeno'),
        ('who_mod_wloss', 'Unexplained moderate weight loss'),
        ('who_resptract', 'Recurrent resp tract infection'),
        ('who_herpeszost', 'Herpes zoster'),
        ('who_cheilitis', 'Angular cheilitis'),
        ('who_oral_ulcer', 'Recurrent oral ulceration'),
        ('who_papular_pruri', 'Papular pruritic eruptions'),
        ('who_dermatit', 'Seborrhoeic dermatitis'),
        ('who_fungal', 'Fungal nail infections'),
        ('who_sev_wloss', 'Unexplained* severe weight loss'),
        ('who_fev', 'Unexplained persistent fever'),
        ('who_diarr', 'Unexplained chronic diarrhoea'),
        ('who_oral_candid', 'Persistent oral candidiasis'),
        ('who_leukoplakia', 'Oral hairy leukoplakia'),
        ('who_pulm_tb', 'Pulmonary tuberculosis'),
        ('who_bactinfect', 'Severe bacterial infections'),
        ('who_stomatit', 'Stomatitis/gingivitis/periodontis'),
        ('who_anemia', 'Anaemia/neutropaenia/thrombocytopa'),
        ('who_hivwaste', 'HIV wasting syndrome'),
        ('who_pneumonia', 'Pneumocystis pneumonia'),
        ('who_bact_pneumo', 'Recurrent severe bacterial pneumo'),
        ('who_herpesinfec', 'Chronic herpes simplex infection'),
        ('who_oeso_candid', 'Oesophageal candidiasis'),
        ('who_extpulm_tb', 'Extrapulmonary tuberculosis'),
        ('who_kaposi_carc', 'Kaposi\u2019s sarcoma'),
        ('who_cytomeg', 'Cytomegalovirus infection'),
        ('who_cns', 'CNS toxoplasmosis'),
        ('who_hivenceph', 'HIV encephalopathy'),
        ('who_meningitis', 'Exp cryptococcosis/meningitis'),
        ('who_dissnon_tb', 'Diss non-TB mycobacterial infection'),
        ('who_leukoence', 'Prog multifocal leukoencephalopathy'),
        ('who_crypto', 'Chronic cryptosporidiosis'),
        ('who_isospor', 'Chronic isosporiasis'),
        ('who_mycosis', 'Disseminated mycosis'),
        ('who_septica', 'Recurrent septicaemia'),
        ('who_lymphoma', 'Lymphoma'),
        ('who_cerv_carc', 'Invasive cervical carcinoma'),
        ('who_leishman', 'Atypical disseminated leishmaniasis'),
        ('who_cardiomy', 'Sympt nephropathy/cardiomyopathy'),
        ('who_na', 'Not Applicable'),
        ('who_other', 'Other, specify'),
    ],
    'flourish_caregiver.caregivermedications': [
        ('mmed_na', 'Not Applicable'),
        ('mmed_cholest', 'Cholesterol medications'),
        ('mmed_vitd', 'Vitamin D supplement'),
        ('mmed_trad_medic', 'Traditional medications'),
        ('mmed_hyper', 'Hypertensive medications'),
        ('mmed_prenatal_vit', 'Prenatal Vitamins'),
        ('mmed_diabetic', 'Diabetic medications'),
        ('mmed_asthmatic', 'Anti-asthmatic drugs'),
        ('mmed_depress', 'Antidepressant drugs'),
        ('mmed_anxiety', 'Anti-anxiety drugs'),
        ('mmed_hep', 'Anti-hepatitis medications'),
        ('mmed_heart', 'Heart disease medications'),
        ('mmed_3tc', '3TC'),
        ('mmed_truvada', 'Truvada'),
        ('mmed_efv', 'Efavirenz'),
        ('mmed_dtg', 'DTG'),
        ('mmed_atripla', 'Atripla'),
        ('mmed_comb3tc_azt', 'Combivir. (3TC,. AZT),'),
        ('mmed_nevirapine', 'Nevirapine'),
        ('mmed_aluvia', 'Aluvia'),
        ('mmed_abacavir', 'Abacavir'),
        ('mmed_tenofovir', 'Tenofovir'),
        ('mmed_tld', 'TLD (TDF,3TC, DTG)'),
        ('mmed_raltearavir', 'Raltearavir'),
        ('mmed_painkillers', 'Painkillers'),
        ('mmed_antibiotics', 'Antibiotics'),
        ('mmed_other', 'Other, Specify'),
        ('mmed_none', 'None'),
    ],
    'flourish_caregiver.deliverycomplications': [
        ('delivery_comp_ruptur', 'Uterine rupture'),
        ('delivery_comp_hemorr', 'Hemorrhage req. transfusion'),
        ('delivery_comp_preeclamp', 'Pre-eclampsia/eclampsia'),
        ('delivery_comp_previa', 'Placenta previa'),
        ('delivery_comp_abrupt', 'Placental abruption'),
        ('delivery_comp_chorio', 'Chorioamnioitis or sus. chorioamnionitis'),
        ('delivery_comp_fev', 'Intrapartum fever'),
        ('delivery_comp_other', 'Other'),
        ('delivery_comp_none', 'None')
    ],
    'flourish_caregiver.emosupporttype': [
        ('adherence_counselling', 'Adherence counseling'),
        ('grief_counselling', 'Grief counseling'),
        ('chronic_illness_diagnosis', 'Dealing with diagnosis of chronic illness'),
        ('financial_advice', 'Financial advice'),
        ('relationship_therapy', 'Relationship therapy (family, partner)'),
        ('social_welfare_support', 'Social welfare support (food basket)'),
        ('emo_trauma_therapy', 'Emotional Trauma therapy'),
        (OTHER, 'Other, specify')
    ],
    'flourish_caregiver.emohealthimproved': [
        ('difficult_to_tell',
         'Difficult to tell because I am still receiving emotional support'),
        ('mood_has_improved', 'My mood has improved'),
        ('not_able_to_relax', 'I am now able to relax'),
        ('relationship_with_other_improved',
         'My relationship with other people/family members/partner has improved'),
        ('able_to_manage_emotions',
         'I am now able to manage my thoughts, feelings and emotions'),
        ('accepted_medical_condition',
         'I have accepted my medical condition and I have learnt to stay positive'),
        ('accepted_loved_one_loss', 'I have now accepted the loss of my loved one'),
        ('feeling_fine', 'Emotional support received and feeling fine now'),
        ('no_longer_suicidal', 'I am no longer suicidal'),
        ('defaulted', 'Gave up and defaulted (No difference)'),
        (OTHER, 'Other, specify')
    ],
    'flourish_caregiver.phonenumtype': [
        ('cell_phone', 'Cell Phone'),
        ('cell_phone_alt', 'Cell Phone (alternative)'),
        ('telephone', 'Telephone'),
        ('telephone_alt', 'Telephone (alternative)'),
        ('work_contact', 'Work contact number'),
        ('alt_person_cell', 'Alternative contact person cell phone'),
        ('alt_person_tel', 'Alternative contact person telephone'),
        ('resp_person_cell', 'Responsible person cell phone'),
        ('resp_person_tel', 'Responsible person telephone'),
        (NONE, 'None')
    ],
    'flourish_caregiver.priorarv': [
        ('prior_arv_azt', 'AZT'),
        ('prior_arv_ddi', 'DDI'),
        ('prior_arv_kaletra', 'Kaletra (or Aluvia)'),
        ('prior_arv_nevirapine', 'Nevirapine'),
        ('prior_arv_3tc', '3TC'),
        ('prior_arv_atripla', 'Atripla'),
        ('prior_arv_tenofovir', 'Tenofovir'),
        ('prior_arv_truvada', 'Truvada (Tenofovir, FTC)'),
        ('prior_arv_atz', 'ATZ'),
        ('prior_arv_d4t', 'D4T'),
        ('prior_arv_raltegravir', 'Raltegravir'),
        ('prior_arv_efv', 'Efavirenz (or Sustiva)'),
        ('prior_arv_combivir', 'Combivir (AZT, 3TC)'),
        ('prior_arv_trizivir', 'Trizivir (AZT, 3TC, Abacavir)'),
        ('prior_arv_abacavir', 'Abacavir'),
        ('prior_arv_dtg', 'DTG'),
        ('prior_arv_unknown', 'ART, unknown'),
        ('prior_arv_na', 'Not Applicable'),
        ('prior_arv_specify', 'Other, specify')
    ],
    'flourish_caregiver.covidsymptoms': [
        ('c19m_iso_chestpain', 'Chest pain'),
        ('c19m_iso_chills', 'Chills'),
        ('c19m_iso_cough', 'Cough'),
        ('c19m_iso_diarr ', 'Diarrhea '),
        ('c19m_iso_fev', 'Fever > 37.5 Degree Celsius'),
        ('c19m_iso_aches', 'Muscle aches'),
        ('c19m_iso_nasal', 'Nasal Congestion'),
        ('c19m_iso_nausea', 'Nausea/vomiting'),
        ('c19m_iso_sob', 'Shortness of breath'),
        ('c19m_iso_throat', 'Sore throat'),
        ('c19m_iso_headache', 'Headache'),
        ('c19m_iso_losssmell', 'Loss of Smell'),
        ('c19m_iso_losstaste', 'Loss of Taste'),
        ('c19m_iso_nosympt', 'No Symptoms'),
    ],
    'flourish_caregiver.covidsymptomsafter14days': [
        ('c19m_14d_chestpain', 'Chest pain'),
        ('c19m_14d_chills', 'Chills'),
        ('c19m_14d_cough', 'Cough'),
        ('c19m_14d_diarr ', 'Diarrhea '),
        ('c19m_14d_fev', 'Fever > 37.5 Degree Celsius'),
        ('c19m_14d_aches', 'Muscle aches'),
        ('c19m_14d_nasal', 'Nasal Congestion'),
        ('c19m_14d_nausea  ', 'Nausea/vomiting'),
        ('c19m_14d_sob', 'Shortness of breath'),
        ('c19m_14d_throat', 'Sore throat'),
        ('c19m_14d_headache', 'Headache'),
        ('c19m_14d_losssmell', 'Loss of Smell'),
        ('c19m_14d_losstaste', 'Loss of Taste'),
        ('c19m_14d_nosympt', 'No Symptoms'),
    ],
    'flourish_caregiver.maternaldiagnoseslist': [
        ('mdiag_pneumonia', 'Pneumonia'),
        ('mdiag_chlamydia', 'Chlamydia'),
        ('mdiag_tb', 'Tuberculosis'),
        ('mdiag_depression', 'Depression'),
        ('mdiag_preeclamp', 'Pre-eclampsia'),
        ('mdiag_gonorrhea', 'Gonorrhea'),
        ('mdiag_liver', 'Liver Problems'),
        ('mdiag_hepc', 'Hepatitis C'),
        ('mdiag_syphillis', 'Syphillis'),
        ('mdiag_asthma', 'Asthma requiring steroids'),
        ('mdiag_herpes', 'Genital Herpes'),
        ('mdiag_hyperten', 'Gestational Hypertension'),
        ('mdiag_na', 'Not Applicable'),
        ('mdiag_other', 'Other, specify')
    ],
    'flourish_caregiver.tbknowledgemedium': [
        ('family', 'Family'),
        ('friends', 'Friends'),
        ('neighbors', 'Neighbors'),
        ('colleagues', 'Colleagues'),
        ('medical_staff', 'Medical Staff'),
        ('media', 'Media'),
        (OTHER, 'Other, specify')
    ],
    'flourish_caregiver.tbdiagnostics': [
        ('sputum', 'Sputum sample'),
        ('chest_xray', 'Chest XRay'),
        ('gene_xpert', 'Gene Xpert'),
        ('tst', 'TST'),
        (OTHER, 'Other, specify')
    ],
    'flourish_caregiver.caregiversocialworkreferrallist': [
        ('refer_argument', 'Arguments with partner/spouse'),
        ('refer_violence', 'Violence with partner/spouse'),
        ('refer_distrust', 'Distrust with partner/spouse'),
        ('refer_finances', 'Financial challenges'),
        ('refer_diagnosis',
         'Difficultly dealing with diagnoses of chronic illness or infectious disease'),
        ('refer_grief', 'Grief counseling (for loss of loved one)'),
        ('refer_adherence', 'Adherence counseling'),
        ('local_medical_facility', 'Local medical facility (add details under Comments)'),
        ('pediatrician_support', 'Pediatrician support'),
        ('schooling_support', 'Schooling support'),
        ('ophthalmology_eye_care', 'Ophthalmology/Eye care support'),
        ('refer_other', 'Other, specify')
    ],
    'flourish_caregiver.pregnancyinfluencerslist': [
        ('the_father', 'The father of the child'),
        ('maternal_family_members', 'Members of my family '),
        ('paternal_family_members', 'Family members of the father of my child'),
        ('anc_staff', 'The ANC staff'),
        ('no_one', 'No other individual influenced my feeding choice decision'),
        (OTHER, 'Other, specify'),
    ],
    'flourish_caregiver.afterpregnancyinfluencerslist': [
        ('the_father', 'The father of the child'),
        ('maternal_family_members', 'Members of my family '),
        ('paternal_family_members', 'Family members of the father of my child'),
        ('anc_staff', 'The ANC staff'),
        ('no_one', 'No other individual influenced my feeding choice decision'),
        (OTHER, 'Other, specify'),
    ],
    'flourish_caregiver.receivedtrainingonfeedinglist': [
        ('antenatal_clinic', 'ANC'),
        ('labour_delivery_ward', 'Labour and Delivery Ward'),
        ('maternatiy_ward', 'Maternity Ward after delivery'),
        ('flourish_team', 'The FLOURISH study team'),
        (NONE, 'None'),
    ],
    'flourish_caregiver.reasonsforinfantfeedinglist': [
        ('no_time_for_breastfeeding', 'I did not have time to breastfeed'),
        ('returned_work_school', 'I had to return to school/work'),
        ('unable_to_produce_enough_milk',
         'I was not able to produce enough breastmilk to keep my infant satisfied'),
        ('infant_refused_breastmilk', 'My infant refused breastmilk'),
        ('painfull_breastfeeding', 'Breastfeeding was too painful'),
        ('cracked_bleeding_nipples', 'My nipples were cracked and/or bleeding'),
        ('did_not_like_breast_shape',
         'I did not like the way breastfeeding changed my breast shape'),
        ('wanted_to_give_infant_traditional_medicine',
         'I wanted to give traditional medicines to my infant'),
        (OTHER, 'Other, specify'),
    ],
    'flourish_caregiver.tbvisitcarelocation': [
        ('antenatal_visit', 'Antenatal Visit'),
        ('idcc', 'IDCC'),
        ('postpartum_visit', 'Postpartum Visit'),
        ('hospital', 'Hospital'),
        ('opd', 'OPD'),
        (OTHER, 'Other, specify'),
    ],
    'flourish_caregiver.memberreadbooks': [
        ('read_mother', 'Mother'),
        ('read_father', 'Biological Father'),
        ('read_mpartner', 'Mother’s partner (not biological father)'),
        ('read_siblings', 'Child’s siblings'),
        ('read_gparents', 'Child’s grandparents'),
        ('read_aunt', 'Child’s aunts/uncles'),
        ('read_househelper', 'House-helper'),
        ('read_nanny', 'Nanny/Babysitter'),
        ('read_oth', 'Other, specify'),
        ('read_noone', 'No-one'),
        ('unknown', 'Unknown'),
        ('read_pnta', 'Prefer not to answer'),
        ('read_na', NOT_APPLICABLE),
    ],
    'flourish_caregiver.membertoldstories': [
        ('stories_mother', 'Mother'),
        ('stories_father', 'Biological Father'),
        ('stories_mpartner', 'Mother’s partner (not biological father)'),
        ('stories_siblings', 'Child’s siblings'),
        ('stories_gparents', 'Child’s grandparents'),
        ('stories_aunt', 'Child’s aunts/uncles'),
        ('stories_househelper', 'House-helper'),
        ('stories_nanny', 'Nanny/Babysitter'),
        ('stories_oth', 'Other, specify'),
        ('stories_noone', 'No-one'),
        ('unknown', 'Unknown'),
        ('stories_pnta', 'Prefer not to answer'),
        ('stories_na', NOT_APPLICABLE),
    ],
    'flourish_caregiver.membersangsongs': [
        ('sang_mother', 'Mother'),
        ('sang_father', 'Biological Father'),
        ('sang_mpartner', 'Mother’s partner (not biological father)'),
        ('sang_siblings', 'Child’s siblings'),
        ('sang_gparents', 'Child’s grandparents'),
        ('sang_aunt', 'Child’s aunts/uncles'),
        ('sang_househelper', 'House-helper'),
        ('sang_nanny', 'Nanny/Babysitter'),
        ('sang_oth', 'Other, specify'),
        ('sang_noone', 'No-one'),
        ('unknown', 'Unknown'),
        ('sang_pnta', 'Prefer not to answer'),
        ('sang_na', NOT_APPLICABLE),
    ],
    'flourish_caregiver.memberchildoutside': [
        ('outside_mother', 'Mother'),
        ('outside_father', 'Biological Father'),
        ('outside_mpartner', 'Mother’s partner (not biological father)'),
        ('outside_siblings', 'Child’s siblings'),
        ('outside_gparents', 'Child’s grandparents'),
        ('outside_aunt', 'Child’s aunts/uncles'),
        ('outside_househelper', 'House-helper'),
        ('outside_nanny', 'Nanny/Babysitter'),
        ('outside_oth', 'Other, specify'),
        ('outside_noone', 'No-one'),
        ('unknown', 'Unknown'),
        ('outside_pnta', 'Prefer not to answer'),
        ('outside_na', NOT_APPLICABLE),
    ],
    'flourish_caregiver.memberplayedwithchild': [
        ('played_mother', 'Mother'),
        ('played_father', 'Biological Father'),
        ('played_mpartner', 'Mother’s partner (not biological father)'),
        ('played_siblings', 'Child’s siblings'),
        ('played_gparents', 'Child’s grandparents'),
        ('played_aunt', 'Child’s aunts/uncles'),
        ('played_househelper', 'House-helper'),
        ('played_nanny', 'Nanny/Babysitter'),
        ('played_oth', 'Other, specify'),
        ('played_noone', 'No-one'),
        ('unknown', 'Unknown'),
        ('played_pnta', 'Prefer not to answer'),
        ('played_na', NOT_APPLICABLE),
    ],
    'flourish_caregiver.membernamedwithchild': [
        ('named_mother', 'Mother'),
        ('named_father', 'Biological Father'),
        ('named_mpartner', 'Mother’s partner (not biological father)'),
        ('named_siblings', 'Child’s siblings'),
        ('named_gparents', 'Child’s grandparents'),
        ('named_aunt', 'Child’s aunts/uncles'),
        ('named_househelper', 'House-helper'),
        ('named_nanny', 'Nanny/Babysitter'),
        ('named_oth', 'Other, specify'),
        ('named_noone', 'No-one'),
        ('unknown', 'Unknown'),
        ('named_pnta', 'Prefer not to answer'),
        ('named_na', NOT_APPLICABLE),
    ],
    'flourish_caregiver.arvinterruptionreasons': [
        ('toxicity_self', 'Toxicity, discontinued by self'),
        ('toxicity_healthcare_provider',
         'Toxicity, discontinued by healthcare provider'),
        ('no_drugs', 'No drugs available'),
        ('no_refill', 'Didn\'t get to clinic for refill'),
        ('forgot', 'Participant forgot'),
        ('traveling', 'Participant was traveling'),
        (OTHER, 'Other'),
        (NOT_APPLICABLE, 'Not Applicable'),
    ],
    'flourish_caregiver.expensecontributors': [
        ('partner', 'Partner/husband'), ('mother', 'Mother'),
        ('father', 'Father'),
        ('sister', 'Sister'), ('brother', 'Brother'), ('aunt', 'Aunt'),
        ('uncle', 'Uncle'),
        ('grandmother', 'Grandmother'), ('grandfather', 'Grandfather'),
        ('mother_in_law', 'Mother-in-law or Father-in-law'),
        ('friend', 'Friend'),
        ('unsure', 'Unsure'), (OTHER, 'Other, specify')
    ],
    'flourish_caregiver.tbtests': [
        ('chest_xray', 'Chest Xray'),
        ('sputum_sample', 'Sputum sample'),
        ('stool_sample', 'Stool sample'),
        ('urine_test', 'Urine test (LAM)'),
        ('skin_test', 'Skin test (TST/Mantoux)'),
        ('blood_test', 'Blood test (quantiferon)'),
        (OTHER, 'other')
    ],
    'flourish_caregiver.generalsymptoms': [
        ('cough', 'Cough'),
        ('fever', 'Fever'),
        ('headache', 'Headache'),
        ('vomiting', 'Vomiting'),
        ('diarrhea', 'Diarrhea'),
        ('fatigue', 'Fatigue'),
        ('congestion', 'Congestion'),
        ('enlarged_lymph_nodes', 'Enlarged Lymph nodes'),
        (OTHER, 'Other'), ],
    'flourish_caregiver.mestitisactions': [
        ('both_breasts', 'Breastfeed from both breasts'),
        ('uninfected_breast',
         'Breastfed from uninfected breast and pumped and dumped from the affected '
         'breast'),
        ('stopped_breastfeeding', 'Stopped breastfeeding'),
        ('temp_stopped',
         'Stopped breastfeeding temporarily but resumed once breast healed'),
        (OTHER, 'Other')
    ]
}

preload_data = PreloadData(
    list_data=list_data)
