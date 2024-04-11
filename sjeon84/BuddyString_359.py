class Solution(object):
  def buddyStrings(self, s, goal):
    """
    :type s: str
    :type goal: str
    :rtype: bool
    """
    l=len(s)
    if(l!=len(goal) or l==1):
        return False

    diff_digit_occurred=False
    two_same_digits=False
    fs={}

    cand_idxs=[-1, -1]

    for i in range(l):
        if(s[i]!=goal[i]):
            diff_digit_occurred=True
            if(cand_idxs[1] !=-1):
                return False
            else:
                if(cand_idxs[0] !=-1):
                    cand_idxs[1]=i
                else:
                    cand_idxs[0]=i
        if(not diff_digit_occurred and not two_same_digits):
            fs[s[i]]=fs.get(s[i],0)+1
            if (fs[s[i]]==2):
                two_same_digits=True

    if(cand_idxs ==[-1,-1]):
        return two_same_digits
    else:#if two seqs are different
        if(s[cand_idxs[0]]==goal[cand_idxs[1]] and s[cand_idxs[1]]==goal[cand_idxs[0]]):
            return True
        else:
            return False




