# PRINT "Welcome to the Big Five (OCEAN) Personality Test!"
# PRINT "Please enter your name:"
# username = INPUT()

# # Initialize scores
# SET O_score = 0
# SET C_score = 0
# SET E_score = 0
# SET A_score = 0
# SET N_score = 0

# # Questions (2 per trait for example)
# FOR each question_number, question_text, trait IN list_of_questions DO

#     PRINT question_number + ". " + question_text
#     PRINT "1 = Strongly Disagree, 2 = Disagree, 3 = Neutral, 4 = Agree, 5 = Strongly Agree"

#     response = INPUT()
#     WHILE response NOT a number OR response < 1 OR response > 5 DO
#         PRINT "Please answer using a number from 1 to 5."
#         response = INPUT()
#     END WHILE

#     # Add points directly based on answer to correct trait score
#     IF trait == "O" THEN
#         O_score = O_score + response
#     ELSE IF trait == "C" THEN
#         C_score = C_score + response
#     ELSE IF trait == "E" THEN
#         E_score = E_score + response
#     ELSE IF trait == "A" THEN
#         A_score = A_score + response
#     ELSE IF trait == "N" THEN
#         N_score = N_score + response
#     END IF

# END FOR

# # Max score per trait depends on number of questions for that trait
# max_score_per_trait = (number_of_questions_per_trait) * 5

# # Define detailed interpretation function for each trait based on score ranges
# DEFINE describe_trait(score, max_score, trait_name):

#     percentage = score / max_score

#     IF trait_name == "Openness" THEN
#         IF percentage >= 0.8 THEN
#             RETURN "You are very open-minded and curious. You enjoy new experiences, creative thinking, and exploring ideas."
#         ELSE IF percentage >= 0.5 THEN
#             RETURN "You have a balanced level of openness. You sometimes enjoy new things but also prefer familiar routines."
#         ELSE
#             RETURN "You tend to prefer familiarity and routine over new experiences. You may be practical and grounded."
#         END IF

#     ELSE IF trait_name == "Conscientiousness" THEN
#         IF percentage >= 0.8 THEN
#             RETURN "You are highly organized, responsible, and reliable. You plan ahead and follow through on your goals."
#         ELSE IF percentage >= 0.5 THEN
#             RETURN "You show some level of conscientiousness, but you also value flexibility and spontaneity."
#         ELSE
#             RETURN "You might struggle with organization and planning, preferring to go with the flow rather than strict schedules."
#         END IF

#     ELSE IF trait_name == "Extraversion" THEN
#         IF percentage >= 0.8 THEN
#             RETURN "You are outgoing, energetic, and enjoy being around others. Social events energize you."
#         ELSE IF percentage >= 0.5 THEN
#             RETURN "You are moderately social, enjoying company but also valuing alone time."
#         ELSE
#             RETURN "You tend to be more reserved and reflective, preferring quieter settings or small groups."
#         END IF

#     ELSE IF trait_name == "Agreeableness" THEN
#         IF percentage >= 0.8 THEN
#             RETURN "You are very compassionate and cooperative. You value harmony and are considerate of others."
#         ELSE IF percentage >= 0.5 THEN
#             RETURN "You are reasonably agreeable, balancing kindness with standing your ground when needed."
#         ELSE
#             RETURN "You can be more competitive or skeptical, sometimes putting your own needs first."
#         END IF

#     ELSE IF trait_name == "Neuroticism" THEN
#         IF percentage >= 0.8 THEN
#             RETURN "You experience emotions intensely and may feel anxious or stressed often."
#         ELSE IF percentage >= 0.5 THEN
#             RETURN "You have average emotional reactivity, sometimes feeling stressed but generally stable."
#         ELSE
#             RETURN "You tend to be calm and emotionally stable, handling stress well."
#         END IF
#     END IF

# END DEFINE

# # Calculate max scores for each trait (assume 2 questions each here)
# max_score_O = 2 * 5
# max_score_C = 2 * 5
# max_score_E = 2 * 5
# max_score_A = 2 * 5
# max_score_N = 2 * 5

# # Get descriptions
# O_description = describe_trait(O_score, max_score_O, "Openness")
# C_description = describe_trait(C_score, max_score_C, "Conscientiousness")
# E_description = describe_trait(E_score, max_score_E, "Extraversion")
# A_description = describe_trait(A_score, max_score_A, "Agreeableness")
# N_description = describe_trait(N_score, max_score_N, "Neuroticism")

# # Output all results with detailed personality paragraphs
# PRINT "Thank you for completing the test, " + username + "!"
# PRINT "Here is your detailed personality profile based on your answers:"
# PRINT ""
# PRINT "Openness: " + O_description
# PRINT "Conscientiousness: " + C_description
# PRINT "Extraversion: " + E_description
# PRINT "Agreeableness: " + A_description
# PRINT "Neuroticism: " + N_description
# PRINT ""

# # Optional: Summary combining key traits (example)
# IF E_score > max_score_E * 0.7 AND N_score < max_score_N * 0.4 AND A_score > max_score_A * 0.6 THEN
#     PRINT "Overall, you are a friendly, energetic, and emotionally balanced person who enjoys social connections."
# ELSE IF E_score < max_score_E * 0.4 AND N_score > max_score_N * 0.7 THEN
#     PRINT "Overall, you might be more introverted and sensitive, preferring calm and quiet environments."
# ELSE
#     PRINT "Your personality has a unique balance of traits that make you who you are."
# END IF
