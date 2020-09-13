# %% [811. Subdomain Visit Count](https://leetcode.com/problems/subdomain-visit-count/)
class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        dc = collections.defaultdict(int)
        for cpdomain in cpdomains:
            n, url = cpdomain.split()
            n, url = int(n), url.split(".")
            for i in range(len(url)):
                dc[".".join(url[i:])] += n
        return [f"{v} {k}" for k, v in dc.items()]
