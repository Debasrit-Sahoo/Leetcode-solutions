class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        mne = mno = s = 1 << 31

        for each in nums1:
            if each & 1 and each < mno:
                mno = each
            elif each < mne:
                mne = each

        return mno < mne or mne == s or mno == s