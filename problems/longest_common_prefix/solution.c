char* longestCommonPrefix(char** strs, int strsSize) {
    int ind = 0;
    bool equal = true;
    do
    {
        if (strlen(strs[0]) > ind)
        {
            char s = strs[0][ind];
            for (int i = 1; i < strsSize; i++)
            {
                if (s == strs[i][ind]) { equal = true; }
                else { equal = false; break; }
            }
        }
        else equal = false;
        if (equal == true) ind++;
    }
    while (equal);
    char* ret = (char*)malloc(ind + 1);
    for (int i = 0; i < ind; i++)
    {
        ret[i] = strs[0][i];
    }
    ret[ind] = '\0';
    return ret;
}