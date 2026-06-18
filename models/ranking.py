def rank_candidates(
        candidate_list
):

    sorted_candidates = sorted(
        candidate_list,
        key=lambda x: x["score"],
        reverse=True
    )

    return sorted_candidates