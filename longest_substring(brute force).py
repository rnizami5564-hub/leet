class Solution(object):
    def lengthOfLongestSubstring(self, s):
        m_len = 0
        for i in range(len(s)):
          for j in range(i+1,len(s)+1):
            sub_s = s[i:j] 
            if len(sub_s) == len(set(sub_s)):
                m_len =  max(m_len , len(sub_s))
        return m_len
        
