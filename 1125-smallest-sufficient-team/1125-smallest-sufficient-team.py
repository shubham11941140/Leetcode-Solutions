class Solution:

    def smallestSufficientTeam(self, req_skills: List[str],
                               people: List[List[str]]) -> List[int]:
        n = len(req_skills)
        skill_to_idx = {skill: idx for idx, skill in enumerate(req_skills)}
        target = (1 << n) - 1
        dp = {0: []}

        for i, person in enumerate(people):
            person_skills = 0
            for skill in person:
                if skill in skill_to_idx:
                    person_skills |= 1 << skill_to_idx[skill]

            for prev_skills, team in list(dp.items()):
                new_skills = prev_skills | person_skills
                if new_skills == prev_skills:
                    continue

                if new_skills not in dp or len(dp[new_skills]) > len(team) + 1:
                    dp[new_skills] = team + [i]

        return dp[target]
