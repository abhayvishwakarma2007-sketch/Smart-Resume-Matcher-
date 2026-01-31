def match_candidates(df, user_query, job_role=None):
    results = []

    # Normalize user input
    user_skills = set(
        user_query.lower().replace(",", " ").split()
    )

    for _, row in df.iterrows():
        candidate_skills_raw = str(row["skills"]).lower()
        candidate_skills = set(
            candidate_skills_raw.replace(",", " ").split()
        )

        if job_role:
            if str(row["applied_job_role"]).lower() != job_role.lower():
                continue

        matched_skills = list(user_skills & candidate_skills)
        missing_skills = list(user_skills - candidate_skills)

        if not matched_skills:
            continue

        match_percent = round(
            (len(matched_skills) / len(user_skills)) * 100, 2
        )

        results.append({
            "Name": row["name"],
            "Experience (Years)": row["experience_year"],
            "Education": row["education"],
            "Applied Job Role": row["applied_job_role"],
            "Match %": match_percent,
            "Matched Skills": ", ".join(matched_skills),
            "Missing Skills": ", ".join(missing_skills)
        })

    results = sorted(results, key=lambda x: x["Match %"], reverse=True)
    return results
