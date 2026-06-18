def generate_ats_score(
        similarity_score
):

    ats_score = (
        similarity_score * 100
    )

    return round(
        ats_score,
        2
    )