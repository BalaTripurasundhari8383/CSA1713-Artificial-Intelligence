% Facts: Diseases and their symptoms
disease(flu) :- has_symptom(fever), has_symptom(cough), has_symptom(body_ache).
disease(cold) :- has_symptom(cough), has_symptom(sneezing), has_symptom(runny_nose).
disease(covid) :- has_symptom(fever), has_symptom(cough), has_symptom(loss_of_taste).
disease(malaria) :- has_symptom(fever), has_symptom(chills), has_symptom(sweating).
disease(diabetes) :- has_symptom(frequent_urination), has_symptom(excessive_thirst), has_symptom(weight_loss).

% Rule to diagnose disease
diagnose(Disease) :- disease(Disease).
