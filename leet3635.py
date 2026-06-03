class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        ma, mb = min(s+d for s, d in zip(landStartTime, landDuration)), min(s+d for s, d in zip(waterStartTime, waterDuration))

        a, b = min((s if ma < s else ma) + d for s, d in zip(waterStartTime, waterDuration)), min((s if mb < s else mb) + d for s, d in zip(landStartTime, landDuration))

        return a if a < b else b