# %% [929. Unique Email Addresses](https://leetcode.com/problems/unique-email-addresses/)
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        r = re.compile(r"([^+@]+)(?:|\+.*)@(.*)")
        f = lambda m: f"{m.group(1).replace('.', '')}@{m.group(2)}"
        return len(set(r.sub(f, email) for email in emails))
